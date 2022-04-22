#! /usr/bin/env python3.9
from lib.bmi import *
from lib.bodytype import *

def main() -> None:
    # 入力フォームを表示させる
    MSG_HEIGHT = "身長をcm単位で入力して下さい"
    MSG_WEIGHT = "体重をkg単位で入力して下さい"
    user_input_height = float(input(MSG_HEIGHT))
    user_input_weight = float(input(MSG_WEIGHT))

    """各Validationで定義した正常値の範囲外が入力されるとValueErrorを出す"""
    # 体重と身長からValueObject "BMI" を生成
    bmi = BMI(user_input_weight, user_input_height)

    # 計算されたBMIをデータ加工した文字列を出力する
    print(bmi.format_value())

    # BMI値から体型を自動判定し、体型名を出力する
    bmi_num = bmi.get_value()
    print(HumanBodyType(bmi_num).bodytype)

if __name__ == "__main__":
    main()
