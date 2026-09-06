def stats(b_book_log):

    borrow_list = [i for i in b_book_log if i[1] == '대여']

    monthly_count = {}
    for i, j, k in borrow_list:
        month_key = k.strftime('%Y-%m')
        # 월(key)에 대여기록이 없으면(None) 0이 기본값인데 대여가 발생해서 이 함수가 실행됐으므로 +1
        # 월(Key)에 대여기록이 있으면 +1
        monthly_count[month_key] = monthly_count.get(month_key, 0) + 1

    book_count = {}
    for i, j, k in borrow_list:
        # isbn(key) 대여기록이 없으면(None) 0이 기본값인데 대여가 발생해서 이 함수가 실했됐으므로 +1
        # isbn(key) 대여기록이 있으면 +1
        book_count[i] = book_count.get(i, 0) + 1

    return monthly_count, book_count

def report(b_book_log, book_info):

    monthly_count, book_count = stats(b_book_log)

    print('★ 월간 대여 빈도\n')
    if not monthly_count:
        print('대여 기록이 없습니다.')
    else:
        for i in sorted(monthly_count):
            print(f'{i}월: {monthly_count[i]}건')

    print('\n★ 최다 대여 도서 (총 누적)\n')
    if not book_count:
        print('대여 기록이 없습니다.')
    else:
        max_count = max(book_count.values())

        for i, j in book_count.items():
            title = book_info[i].get_title()
            author = book_info[i].get_author()

            if j == max_count:
                print(f'{j}회 대여:「{title}」(작가: {author})')
    
    print('\n★ 전체 대여 빈도 (총 누적)\n')
    if not book_count:
        print('대여 기록이 없습니다.\n')

    else:
        cnt = 0
        for i, j in sorted(book_count.items(), key = lambda x: x[1], reverse = True):
            title = book_info[i].get_title()
            author = book_info[i].get_author()
            cnt += 1
            print(f'{cnt}.「{title}」(작가: {author}): {j}회 대여')
        print()

