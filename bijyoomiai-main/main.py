#! /usr/bin/env python3.9
"""
継承(is-a)より集約(has-a) + 委譲(delegation)を試すためのモジュール
"""
# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from format import Format
from util import Util

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class BijyoOmiai:
    # 生成する点数の下限と上限
    POINT_LBOUND = 1
    POINT_UBOUND = 100

    def __init__(self, name_list, miokuri, decision_criteria_rank) -> None:
        # has-a関係: 読み込みたいクラスのインスタンス化 = 依存性の注入(DI, 依存オブジェクトの注入)
        self.util = Util()
        self.format = FormatBijyoOmiai(self)

        # 引数 -> インスタンス変数化
        self.name_list = name_list # お見合いする美女の名前格納用
        self.miokuri = miokuri
        self.decision_criteria_rank = decision_criteria_rank
        
        # 渡されたarg name_listからお見合いで1人の美女を決める処理
        self.name_and_score = {}
        self.name_and_score_sortedbyscore = {}
        self.decided_bijyo_name = ""
        self.decidedBijyo()
    
    def decidedBijyo(self) -> None:
        # 美女の人数だけループ
        for i in range(1, len(self.name_list) + 1,1):
            # 美女の名前とランダムに付けた点数を辞書へ追加
            bijyo_name = self.name_list[i - 1] # list indexのbase 0 に合わせるため -1
            score_and_bijyo = self.__scoringBijyo(bijyo_name) # 名前を指定した美女に点数を付ける
            self.name_and_score.update(score_and_bijyo)

            # 見送りルール: カウンタが見送り開始人数以下なら順位を判定せずに次の美女へ
            if i <= self.miokuri: continue
            
            # 順位判定: 美女のランクをdictから取得
            rank = self.__getBijyoRank(bijyo_name)

            # 美女決定: 判定した順位が、指定した順位以下ならその美女に決定しループを抜ける
            if rank <= self.decision_criteria_rank:
                self.decided_bijyo_name = bijyo_name
                break

        # 最後まで指定した順位以内の美女が見つからなかった場合
        if self.decided_bijyo_name == "":
            self.decided_bijyo_name = bijyo_name # 一番最後にお見合いした人にやむをえず決定
            
    def __scoringBijyo(self, bijyo_name) -> dict:
        point = self.util.getRandomNum(self.POINT_LBOUND, self.POINT_UBOUND) #item: ポイントをランダム生成
        # (keyとitemを辞書として生成し追加)
        bijyo_and_score = {bijyo_name: point}
        return bijyo_and_score
        
    def __getBijyoRank(self, bijyo_name) -> int:
        bijyo_dict = self.name_and_score
        # itemの点数を基準に辞書を降順ソート
        self.name_and_score_sortedbyscore = self.util.descendingSortDict(bijyo_dict)
        
        # 美女の順位の判定(辞書から、現在の美女の点数が何番目に位置するかで判定)
        rank = self.util.getDictionaryIndex(dict(bijyo_dict), bijyo_name, base=1)
        return rank

    # has-a関係: 呼び出したクラスのメソッドを、このクラスの公開メソッドとするために定義
    # (ようはオーバーライドもどき。オーバーライドと違い、別名でaliasしてもよい！)
    def formatOmiai(self) -> list:
        return self.format.omiai()

    def formatDecidedBijyo(self) -> str:
        return self.format.decidedBijyo()

    def formatBijyoRanking(self) -> list:
        return self.format.bijyoRanking()


class FormatBijyoOmiai():
    def __init__(self, BijyoOmiai) -> None:
        # has-a関係: 読み込みたいクラスのインスタンス化 = 依存性の注入(DI, 依存オブジェクトの注入)
        self.format = Format()

        # 引数 -> インスタンス変数化
        self.BijyoOmiai = BijyoOmiai

    def omiai(self) -> list:
        format_list = []
        i = 1
        for nm, score in self.BijyoOmiai.name_and_score.items():
            # 美女の名前と点数
            format_list.append(f"{nm}:{score}点")
            # 指定した見送り人数以下なら、見送りの文字列を追加
            if i <= self.BijyoOmiai.miokuri: format_list.append("(見送り・・・)")
            i += 1
        return format_list
    
    def decidedBijyo(self) -> str:
        # 選んだ1人の美女
        # MEMO:"\"で行継続させる場合には、行ごとにクォートで囲う必要があるため注意
        format_text = self.format.highlight(f"あなたが選んだ美女\n" \
            f"[{self.BijyoOmiai.decided_bijyo_name}:" \
            f"{self.BijyoOmiai.name_and_score[self.BijyoOmiai.decided_bijyo_name]}点]"
            )
        return format_text

    def bijyoRanking(self) -> list:
        # 美女リスト(各順位)
        format_rank = [f"[{i}位]"
                       for i in range(1, len(self.BijyoOmiai.name_and_score_sortedbyscore) + 1, 1)]
        format_list_nm_and_score = [f"{nm}:{score}点"
                                    for nm, score in self.BijyoOmiai.name_and_score_sortedbyscore.items()]
        format_list_join = [f"{format_rank[i]} {format_list_nm_and_score[i]}"
                            for i in range(0, len(self.BijyoOmiai.name_and_score_sortedbyscore))]
        return format_list_join


# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def main() -> None:
    """View"""
    # Input(ControllerへRequestするための値)
    # - お見合いに参加する美女を定義
    name_list = [
        "1人目", "2人目", "3人目", "4人目", "5人目",
        "6人目", "7人目", "8人目", "9人目", "10人目"
    ]
    # - 決める1人の美女を判定するのに、n人目まで見送るか定義
    MIOKURI = 4
    # - 見送り以降にお見合いした美女が、n位以下なら許容して決定する
    DECISION_RANK = 5
    
    # ControllerへRequest
    omiai = BijyoOmiai(name_list, MIOKURI, DECISION_RANK)

    # ControllerからResponce
    # - お見合いの結果を出力
    format = Format() # 依存性の注入(DI)
    print(format.gume("お見合い開始"))

    # - お見合い中の美女と点数を出力
    print_list = omiai.formatOmiai()
    [print(format.normal(msg)) for msg in print_list] # 出力
    
    # - 決めた1人の美女を出力
    print(omiai.formatDecidedBijyo())
    
    # - お見合いした美女全員の順位を表示
    print(format.gume("美女の順位一覧"))
    print_list = omiai.formatBijyoRanking()
    [print(format.normal(msg)) for msg in print_list] # 出力


if __name__ == "__main__":
    main()