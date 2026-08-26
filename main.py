from models.specialized_books import PaperBook, EBook
from utils.helpers import get_int, get_string

def main():

    book_info = {}
    book_isbn = set()

    while True:
        print('======= 도서 관리 시스템 =======')
        print(' 1. 도서 등록')
        print(' 2. 전체 도서 조회')
        print(' 3. 도서 검색')
        print(' 4. 대여/반납 처리')
        print(' 5. 종료')
        print('================================')
        select = get_int('*수행할 작업메뉴의 번호를 입력하세요.: ')

        if select == 1:
            print('\n[도서 관리 시스템 > 1. 도서 등록]\n')

            title = get_string('*도서명 : ')
            author = get_string('*작가명 : ')
            isbn = get_int('*ISBN : ')

            if isbn in book_isbn:
                print(f'\n[!] 이미 등록된 ISBN 정보입니다.\n')
                continue

            book_type = get_int('*출판형식을 선택하세요(1: 종이책, 2: 전자책). : ')
            if book_type == 1:
                binding = get_string('*제본방식 : ')
                new_book = PaperBook(title, author, isbn, binding)
            elif book_type == 2:
                format = get_string('*발행유형 : ')
                new_book = EBook(title, author, isbn, format)
            else:
                print('\n[!] 종이책인 경우 숫자 1, 전자책인 경우 숫자 2를 입력하세요.\n')
                continue

            book_info[isbn] = new_book
            book_isbn.add(isbn)
            print(f'\n[V]「{title}」도서 등록 완료\n')

        elif select == 2:
            print('\n[도서 관리 시스템 > 2. 전체 도서 조회]\n')

            if not book_info:
                print('\n[!] 등록된 도서가 없습니다.\n')
            else:
                for i in book_info.values():
                    print(i.display_info(), '\n')

        elif select == 3:
            print('\n[도서 관리 시스템 > 3. 도서 검색]\n')
            result = False
            search = get_string('*검색할 도서명을 입력하세요.: ')

            for i in book_info.values():
                if search in i.get_title():
                    print()
                    print(i.display_info(), '\n')
                    result = True

            if result != True:
                print('\n[!] 검색 결과가 없습니다.\n')

        elif select == 4:
            print('\n[도서 관리 시스템 > 4. 대여/반납 처리]\n')
            b_isbn = get_int('*대여/반납 처리할 도서의 ISBN을 입력하세요.: ')

            if b_isbn not in book_info:
                print('\n[!] 해당 도서를 찾을 수 없습니다.\n')
            else:
                b_book = book_info[b_isbn]

                if b_book.get_status():
                    b_book.set_status(False)
                    print(f'\n[V]「{b_book.get_title()}」도서 대여 완료\n')
                else:
                    b_book.set_status(True)
                    print(f'\n[V]「{b_book.get_title()}」도서 반납 완료\n')

        elif select == 5:
            print('\n[프로그램을 종료합니다.]\n')
            break

        else:
            print('\n[!] 해당하는 작업메뉴의 번호만 입력하세요.\n')

if __name__ == '__main__':
    main()