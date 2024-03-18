# BMI計算函數
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# 使用者輸入
weight = float(input("請輸入您的體重（公斤）："))
height = float(input("請輸入您的身高（公尺）："))

# 計算BMI
bmi = calculate_bmi(weight, height)

# 顯示結果
print(f"您的BMI是：{bmi:.2f}")

# 根據BMI值給出健康建議
if bmi < 18.5:
    print("您的BMI屬於「體重過輕」範圍。建議您增加營養攝取，並進行適當的運動。")
elif bmi >= 18.5 and bmi < 24.9:
    print("恭喜，您的BMI屬於「正常體重」範圍。請繼續保持健康的飲食和運動習慣。")
elif bmi >= 25 and bmi < 29.9:
    print("您的BMI屬於「過重」範圍。建議您透過健康飲食和規律運動來控制體重。")
else:
    print("您的BMI屬於「肥胖」範圍。建議尋求醫生或營養師的專業建議，制定健康的減重計畫。")
