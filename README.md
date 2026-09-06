# 도서 관리 시스템 (Book Management System)

콘솔 기반 도서 등록/조회/검색/대여·반납/통계 프로그램입니다.

## 실행 방법

```bash
uv run main.py
```

`uv`가 `pyproject.toml`을 보고 알아서 가상환경을 만들고 실행합니다. 별도 의존성은 없습니다(표준 라이브러리 `datetime`만 사용).

## 프로젝트 구조

```
.
├── main.py                        # 메인 루프 & 메뉴 처리
├── models/
│   ├── base_book.py                # Book (공통 속성/동작)
│   └── specialized_books.py        # PaperBook, EBook (Book 상속)
├── utils/
│   ├── helpers.py                  # get_string, get_int (입력 검증 포함)
│   └── statistics.py               # 대여 로그 통계 계산/출력
└── images/                         # 아래 README에서 쓰는 실행화면
```

## 메뉴별 기능 설명 및 실행화면

> 아래 화면들은 실제 프로그램 출력 문자열을 그대로 재현한 것으로, 하나의 시나리오(도서 2권 등록 → 조회 → 검색 → 대여 → 통계 확인 → 종료)를 기준으로 구성했습니다.

### 1. 도서 등록

`1: 종이책` 선택 시 제본방식을, `2: 전자책` 선택 시 발행유형을 추가로 입력받아 각각 `PaperBook`, `EBook` 객체로 등록합니다.

**종이책 등록**

![종이책 등록](images/02_register_paperbook.png)

**전자책 등록**

![전자책 등록](images/03_register_ebook.png)

**중복 ISBN 등록 시도** — 이미 등록된 ISBN이면 등록을 막습니다.

![중복 ISBN](images/04_register_duplicate.png)

### 2. 전체 도서 조회

등록된 모든 도서의 정보(도서명/작가명/ISBN/대여상태 + 종류별 부가정보)를 출력합니다.

![전체 도서 조회](images/05_list_all.png)

### 3. 도서 검색

입력한 문자열이 도서명에 포함된 도서를 모두 찾아 보여줍니다.

**검색 성공**

![검색 성공](images/06_search.png)

**검색 결과 없음**

![검색 결과 없음](images/07_search_empty.png)

### 4. 대여/반납 처리

ISBN으로 도서를 찾은 뒤, 현재 상태(`대여가능`/`대여불가`)를 보고 대여 또는 반납을 자동으로 판단해 처리합니다. 처리 결과는 `(ISBN, '대여'|'반납', 처리시각)` 튜플로 로그에 남습니다.

![대여 처리](images/08_rent_return.png)

### 5. 대여/반납 통계

누적된 대여 로그를 바탕으로 월간 대여 건수, 최다 대여 도서, 전체 도서별 대여 횟수(내림차순)를 출력합니다.

![대여 통계](images/09_stats.png)

### 6. 종료

프로그램을 종료합니다.

![종료](images/10_exit.png)

## 예외 처리 / 입력 유효성 검증

| 상황 | 처리 방식 |
|---|---|
| 빈 문자열 입력 | `get_string`이 값이 나올 때까지 재입력 요청 |
| 숫자가 아닌 값을 정수 입력란에 입력 | `get_int`가 `ValueError`를 잡아 재입력 요청 |
| 잘못된 출판형식 번호(1, 2 이외) | 안내 메시지 후 등록 취소, 메뉴로 복귀 |
| 존재하지 않는 메뉴 번호 | 안내 메시지 후 메뉴로 복귀 |
| 존재하지 않는 ISBN으로 대여/반납 시도 | `book_info[b_isbn]` 접근 시 발생하는 `KeyError`를 `try/except`로 처리 |

**빈 입력값**

![빈 입력값](images/11_error_empty_input.png)

**숫자가 아닌 값 입력**

![숫자 아님](images/12_error_not_number.png)

**잘못된 출판형식**

![잘못된 출판형식](images/13_error_invalid_booktype.png)

**잘못된 메뉴 번호**

![잘못된 메뉴 번호](images/14_error_invalid_menu.png)

**존재하지 않는 ISBN**

![존재하지 않는 ISBN](images/15_error_isbn_not_found.png)

## 한계점

- CR만 있고 UD는 없다. 
- 편의상 ISBN을 숫자형(정수형)으로만 받아서 실제 ISBN 코드와 괴리가 있다.
- 데이터 휘발성이 높고 일부 메뉴는 입력 유효성 위반 시 메인 메뉴로 보내버린다. 
- 실습용 간단한 콘솔 프로그램이기 때문에 실제 도서관 시스템으로서는 재설계가 필요하다. 
