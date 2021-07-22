dic1 = {"pink":"粉紅色","teacher":"老師","ball":"球"}
time = 0
n = 1
while time < n:
    q = (int(input("請問你要使用什麼功能? 1,英翻中 2,中翻英 3,測驗 4,離開: ")))
    if q == 1:
        qq = (input("請輸入你要查哪一個字?:"))
        ans = dic1[qq]
        print(ans)
    if q == 2:
        qq = (input("請輸入你要查哪一個字?:"))
        ans = list (dic1.keys()) [list (dic1.values()).index (qq)]
        print(ans)
    if q == 3:
        print("pink,teacher,ball")
        q = (input("請輸入以上單字的中文"))
        ans = dic1["pink","teacher","ball"]
        if q == ans:
            print("恭喜!你答對了全部!")
        else:
            print("真可惜...你有些地方錯了!")
    if q == 4:
        break