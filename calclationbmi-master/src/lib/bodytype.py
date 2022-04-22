# =========================================================================
# 抽象クラス(インターフェース)のテスト
# =========================================================================

# Python インターフェース用標準モジュール: ABC (Abstract Base Class - 抽象基底クラス)
from abc import (
    ABC,
    abstractmethod
)

from .const import ERRMSG_ARGUMENT_OUTOFRANGE

# -------------------------------------------------------------------------
# 各具象クラスから体型の判定を行うクラス
# -------------------------------------------------------------------------
class HumanBodyType():
    def __init__(self, bmi) -> None:
        self.bodytype = self.__get_bodytype(bmi)
        self.__bmi = bmi

    @staticmethod
    def __get_bodytype(bmi) -> str:
        """bmiから体型を判定し、体型名を取得する"""
        if Yase.is_valid_bodytype(bmi): return Yase.format_bodytype()
        if Hyoujyun.is_valid_bodytype(bmi): return Hyoujyun.format_bodytype()
        if Himan.is_valid_bodytype(bmi): return Himan.format_bodytype()
        if KoudoHiman.is_valid_bodytype(bmi): return KoudoHiman.format_bodytype()

        # どれにも当てはまらない場合はエラー出す
        raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)


# -------------------------------------------------------------------------
# 抽象クラス (抽象メソッドの定義)
# -------------------------------------------------------------------------
"""
[概要]
最初に処理内容を具体的に書かず、後からメソッドの実装をして使用するために使う。

[内容]
各サブクラスで共通して使用するメソッド等をインターフェースとして定義
    * 定数
    * 変数
    * メソッド ※"必ず"オーバーライドを経由して実装しなければならない

[メリット]
    - 処理をサブクラスごとに変えたい場合に有効(後からメソッドの実装をするため)
    - メソッド名の統一やオーバーライド漏れを防ぐ(抽象メソッドが全て実装(具象メソッド)されていることを保証する)

[注意]
    - 抽象クラス(インターフェース)自身はインスタンス化できない(継承前提のクラス)
    - コンストラクタ・処理はここでは書かない
    - 抽象クラスで記述した全ての抽象メソッドは、必ずサブクラスでオーバーライドしなければならない
    (全て定義(実装)していない状態で、サブクラスのインスタンス生成をするとエラーが出る)
    - ただし、抽象クラスで記述したフィールド定数or変数は強制することができない(任意使用となる)
"""
class IBodyType(ABC): # ABC (Abstract Base Class - 抽象基底クラス = インターフェース)
    # フィールド定数
    STR_TYPE: str = "型" # サブクラスで使用する際は「BodyType.STR_TYPE」とする(第1引数のselfは不要)

    # フィールド変数(各サブクラスで、クラス変数orインスタンス変数として定義する)
    bodytype: str

    @abstractmethod
    def __init__(self, bmi) -> None:
        pass

    # 抽象メソッド(Abstract Method)を定義
    @classmethod
    @abstractmethod
    def format_bodytype(cls) -> str:
        pass

    @staticmethod
    @abstractmethod # 複数デコレータを指定する場合は、必ずabstractを優先して実行させる
    def is_valid_bodytype(bmi: int) -> bool: # 抽象メソッドの引数くらいは型アノテーションしてみた
        pass

# -------------------------------------------------------------------------
# 具象クラス(抽象クラスを継承した各サブクラス)
# -------------------------------------------------------------------------
"""抽象メソッドの実際の処理内容である、具象メソッド(Concrete Method)を定義
(具象メソッドの定義 = 抽象メソッドの実装)"""
class Yase(IBodyType):
    bodytype = "やせ" # クラス変数(使用する場合は func_foo(cls): cls.bar)

    def __init__(self, bmi) -> None:
        if not self.is_valid_bodytype(bmi): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        self.__bmi = bmi
    
    @classmethod
    def format_bodytype(cls) -> str:
        return f"{cls.bodytype}{IBodyType.STR_TYPE}"

    @staticmethod
    def is_valid_bodytype(bmi) -> bool:
        return bmi < 18.5 # 正常値の要件


class Hyoujyun(IBodyType):
    bodytype = "標準"

    def __init__(self, bmi) -> None:
        if not self.is_valid_bodytype(bmi): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        self.__bmi = bmi

    @classmethod
    def format_bodytype(cls) -> str:
        return f"{cls.bodytype}{IBodyType.STR_TYPE}"

    @staticmethod
    def is_valid_bodytype(bmi) -> bool:
        return 18.5 <= bmi < 25 # 正常値の要件


class Himan(IBodyType):
    bodytype = "肥満"

    def __init__(self, bmi) -> None:
        if not self.is_valid_bodytype(bmi): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        self.__bmi = bmi

    @classmethod
    def format_bodytype(cls) -> str:
        return f"{cls.bodytype}{IBodyType.STR_TYPE}"

    @staticmethod
    def is_valid_bodytype(bmi) -> bool:
        return 25 <= bmi < 30 # 正常値の要件


class KoudoHiman(IBodyType):
    bodytype = "高度肥満"
    
    def __init__(self, bmi) -> None:
        if not self.is_valid_bodytype(bmi): raise ValueError(ERRMSG_ARGUMENT_OUTOFRANGE)
        self.__bmi = bmi

    @classmethod
    def format_bodytype(cls) -> str:
        return f"{cls.bodytype}{IBodyType.STR_TYPE}"

    @staticmethod
    def is_valid_bodytype(bmi) -> bool:
        return bmi >= 30 # 正常値の要件