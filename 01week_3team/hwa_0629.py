# ---------------------------------------------------------
# 0629 수정사항
#   1) 카테고리를 Entry에서 Combobox로 수정!
#   2) 저축 입력 추가
#   3) 1일 지출 검색
# ---------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk  import Label,Button,Entry,Combobox,Treeview

DIR_PATH = "../week1/info/"
date_input=0
money_input=0
category_input=0

# 함수 설정 ---------------------------------------------------------------

# '입력' 버튼 눌렀을 때, 데이터 .txt파일에 입력

def onClick_p():
    global date_input, money_input
    date_input=entry_day.get()
    money_input=entry_price.get()
    print(date_input, money_input)

    txt = [entry_day.get(), entry_price.get()]
    messagebox.showwarning("가계부 입력", txt)


def onClick_m():
    global date_input, money_input, category_input
    date_input=entry_day.get()
    money_input=entry_price.get()
    category_input=entry_category.get()
    print(date_input, money_input, category_input)

    txt = [date_input, money_input, category_input]
    messagebox.showwarning("가계부 입력", txt)


def onClick_a():
    global date_input, save_input
    date_input=entry_day.get()
    save_input=entry_price.get()
    print(date_input, save_input)

    txt = [entry_day.get(), entry_price.get()]
    messagebox.showwarning("가계부 입력", txt)


# def Cal():
# label.configure(text="결과 값 = " + str(eval(entry.get())))



# 민수 ---------------------------------------------------------------------

while True:  # 메뉴 선택
    print("===== 가계부 =====")
    print("1. 수 입  입 력")
    print("2. 지 출  입 력")
    print("3. 저 축  입 력")
    print("4. 1일 지출 검색")
    print("5. 1달 지출 검색")
    print("6.기간별 지출 검색")
    print("7. 종        료")
    print("=" * 18)
    choice = input("번호 선택 : ")

    # 1. 수입 입력하기
    if choice == "1":

        root = tk.Tk()                 # 윈도우 창 생성
        root.title('수입 입력')         # 제목 설정
        root.geometry("300x200")      # 창 크기 설정(x,y좌표 고정)
        root.resizable(False, False)  # 창 크기 조절 X

        # grid 레이아웃을 이용해서 Label과 Entry 위젯 배치 ----------
        lab_day = Label(root, text='날짜 : ', font=5)
        lab_price = Label(root, text='금액 : ', font=5)

        entry_day = Entry(root, width=15, font=7)
        entry_price = Entry(root, width=15, font=7)

        lab_day.grid(row=0, column=0, padx=10, pady=10)
        entry_day.grid(row=0, column=1, padx=10, pady=10)
        lab_price.grid(row=1, column=0, padx=10, pady=10)
        entry_price.grid(row=1, column=1, padx=10, pady=10)

        # Button 위젯 배치 ------------------------------------
        btn_input = Button(root, text='입력', width=8, command=onClick_p)
        btn_input.grid(row=2, column=0, columnspan=2)

        root.mainloop()         # 윈도우가 종료될 때까지 실행


        # date_input = input("입력 날짜:(ex.06.25): ")
        # money_input = input("지출 금액:(ex.10000): ")
        print(" [ 수입 총액 ]")
        F=Flow_money(date_input,money_input)
        F.money_in()


    # 2. 지출 입력하기
    elif choice == "2":

        root = tk.Tk()                  # 윈도우 창 생성
        root.title('지출 입력')          # 제목 설정
        root.geometry("350x250")       # 창 크기 설정(x,y좌표 고정)
        root.resizable(False, False)   # 창 크기 조절 X

        # grid 레이아웃을 이용해서 Label과 Entry, Combobox 위젯 배치 -----------------
        lab_day = Label(root, text='날  짜 : ', font=5)
        lab_price = Label(root, text='금  액 : ', font=5)
        lab_category = Label(root, text='내  용 : ', font=5)

        entry_day = Entry(root, width=15, font=7)
        entry_price = Entry(root, width=15, font=7)

        values = ["고정지출", "식비", "특수비용"]
        entry_category = Combobox(root, height=10, values=values)
        entry_category.set("카테고리 선택")

        lab_day.grid(row=0, column=0, padx=20, pady=10)
        entry_day.grid(row=0, column=1, padx=0, pady=10)
        lab_price.grid(row=1, column=0, padx=20, pady=10)
        entry_price.grid(row=1, column=1, padx=0, pady=10)
        lab_category.grid(row=2, column=0, padx=20, pady=10)
        entry_category.grid(row=2, column=1, padx=0, pady=10)

        # Button 위젯 배치 ------------------------------------
        btn_input = Button(root, text='입력', width=8, command=onClick_m)
        btn_input.grid(row=3, column=0, columnspan=2)

        root.mainloop()  # 윈도우가 종료될 때까지 실행


        # date_input = input("입력 날짜:(ex.06.25): ")
        # money_input = input("지출 금액:(ex.10000): ")
        # category_input = input("해당 카테고리(의,식,주): ")
        print(" [ 지출 총액 ]")
        F = Flow_money(date_input, money_input, category_input)
        F.money_out()

    # 3.저축 확인 및 입력하기
    elif choice == "3":

        root = tk.Tk()                 # 윈도우 창 생성
        root.title('저축 입력')         # 제목 설정
        root.geometry("300x200")      # 창 크기 설정(x,y좌표 고정)
        root.resizable(False, False)  # 창 크기 조절 X

        # grid 레이아웃을 이용해서 Label과 Entry 위젯 배치 ----------
        lab_day = Label(root, text='날짜 : ', font=5)
        lab_price = Label(root, text='금액 : ', font=5)

        entry_day = Entry(root, width=15, font=7)
        entry_price = Entry(root, width=15, font=7)

        lab_day.grid(row=0, column=0, padx=10, pady=10)
        entry_day.grid(row=0, column=1, padx=10, pady=10)
        lab_price.grid(row=1, column=0, padx=10, pady=10)
        entry_price.grid(row=1, column=1, padx=10, pady=10)

        # Button 위젯 배치 ------------------------------------
        btn_input = Button(root, text='입력', width=8, command=onClick_a)
        btn_input.grid(row=2, column=0, columnspan=2)

        root.mainloop()  # 윈도우가 종료될 때까지 실행



        # print("=== 현재 저축 현황 ====")
        #
        # date_input = input("입력 날짜:(ex.06.25): ")
        # save_input = input("입력 금액:(ex.10000): ")
        print(" [ 저축 총액 ]")
        F = Flow_money(date_input, save_input)
        F.money_save()
        M = Moneyinfo("../../../Documents/카카오톡 받은 파일/account/account/save", "S", 0)
        M.cal()

    # 4.해당 날짜 지출 검색
    elif choice == "4":

        root = tk.Tk()                 # 윈도우 창 생성
        root.title('1일 지출 검색')      # 제목 설정
        root.geometry("400x200")      # 창 크기 설정(x,y좌표 고정)
        root.resizable(False, False)  # 창 크기 조절 X



        label = Label(root, text='날짜 입력(ex.06.23) : ', font=5)
        entry = Entry(root, width=10, font=7)

        label.grid(row=0, column=0, padx=10, pady=10)
        entry.grid(row=0, column=1, padx=10, pady=10)



        #
        # # grid 레이아웃을 이용해서 Label과 Entry 위젯 배치 ----------
        # lab_day = Label(root, text='날짜 : ', font=5)
        # lab_price = Label(root, text='금액 : ', font=5)
        #
        # entry_day = Entry(root, width=15, font=7)
        # entry_price = Entry(root, width=15, font=7)
        #
        # lab_day.grid(row=0, column=0, padx=10, pady=10)
        # entry_day.grid(row=0, column=1, padx=10, pady=10)
        # lab_price.grid(row=1, column=0, padx=10, pady=10)
        # entry_price.grid(row=1, column=1, padx=10, pady=10)
        #
        # # Button 위젯 배치 ------------------------------------
        # btn_input = Button(root, text='입력', width=8, command=onClick_a)
        # btn_input.grid(row=2, column=0, columnspan=2)
        #
        root.mainloop()  # 윈도우가 종료될 때까지 실행



        # 출력되는 데이터 타입 확인! -> str or list



        date_input = input("일 입력(ex.06.23): ")
        M = Moneyinfo("../../../Documents/카카오톡 받은 파일/account/account/use", date_input)
        M.cal()


    # 5.해당 월 지출 검색
    elif choice == "5":
        month_input = input("월 입력(ex.01): ")
        M = Moneyinfo("../../../Documents/카카오톡 받은 파일/account/account/use", month_input)
        M.cal()

    # 6. 기간별 지출 검색
    elif choice == "6":
        inputMon = input("월을 입력하시오(ex 00) : ")
        n1 = int(input("일을 입력하시오(ex 0) : "))
        n2 = int(input("일을 입력하시오(ex 0) : "))
        print(day1(n2) - day2(n1))
    # 7.종료하기
    elif choice == "7":
        break

    # 8.재입력
    else:
        print("1 ~ 7 중 다시 입력해주세요.")



# 추가 수정사항 ------------------------------------
# 1) 종료하기 값 6 -> 7
# 2) 재입력 print("1~7 중 다시 입력해주세요.")
# 3) 저축 입력(변수명) 날짜 -> 내용으로 변경? 아님 그대로 날짜 유지?
# -----------------------------------------------