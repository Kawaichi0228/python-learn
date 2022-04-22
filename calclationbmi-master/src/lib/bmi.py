from .const import ERRMSG_ARGUMENT_OUTOFRANGE

# ValueObject(値そのものをクラス化) + 完全コンストラクタ(Complete Constructor)
class BMI:
    # ValueObject: 原則的に"1個"のインスタンス変数のみ用意
    def __init__(self, weight_kg, height_cm) -> None:
        # 完全コンストラクタ: コンストラクタでバリデーション(不正値を除外)
        if not self.__is_valid_weight_kg(weight_kg): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        if not self.__is_valid_height_cm(height_cm): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        self.__weight_kg = weight_kg # 完全コンストラクタ: プロパティをダンダー(__)にすることで、セッターを禁止
        self.__height_cm = height_cm

        # bmiを計算
        bmi = self.__calc(self.__weight_kg, self.__height_cm)
        if not self.__is_valid_bmi(bmi): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        # if not self.is_valid_bmi(bmi): raise ArgumentOutOfRangeException(ERRMSG_ARGUMENT_OUTOFRANGE)
        self.__bmi = bmi

    # 完全コンストラクタ: bmiを計算し確定させるメソッド(calc)
    @staticmethod
    def __calc(weight_kg, height_cm) -> float:
        height_m = height_cm / 100 # cm単位→m単位へ変換
        return float(weight_kg / height_m **2)

    # 完全コンストラクタ: バリデーションメソッド
    # デコレータ: @staticmethod = インスタンス関数・変数と一切のやり取りをしないメソッド(暗黙の第一引数(self)も受け取らない)
    @staticmethod
    def __is_valid_weight_kg(weight_kg) -> bool:
        return 25 <= weight_kg <= 150  # 正常値の要件

    @staticmethod
    def __is_valid_height_cm(height_cm) -> bool:
        return 100 <= height_cm <= 240  # 正常値の要件

    @staticmethod 
    def __is_valid_bmi(bmi) -> bool:
        return 10 <= bmi <= 50  # 正常値の要件

    # 完全コンストラクタ: インスタンス変数用のゲッタ
    def get_value(self) -> float:
        return self.__bmi

    # インスタンスメソッド。表示用に加工したデータ(format)のゲッタ
    def format_value(self) -> None:
        return f"BMI = {self.__bmi}"

"""
# -------------------------------------------------------------------------
# 独自例外クラス(未使用)
# -------------------------------------------------------------------------
class ArgumentOutOfRangeException(Exception):
    def __init__(self, msg) -> None:
        self._msg = msg

    def __str__(self) -> str:  # 特殊メソッド（戻り値はstr型only）
        return self._msg
"""