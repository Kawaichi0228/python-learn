class Score:
    """ValueObject"""
    def __init__(self, score):
        if not self.isValid(score): raise ValueError("ArgumentOutofRange")
        self.score = score
    
    @staticmethod
    def isValid(score):
        """点数は0-100点までを許可"""
        return True if 0 <= int(score) <= 100 else False
    
    def get(self):
        return self.score


class PassingRule:
    """DomainObject"""
    def __init__(self, score_list):
        self.score_list = score_list
        
        total_score = self.total(self.score_list)
        self.total_score = total_score
        
    def isPassing(self):
        """合格判定メソッド"""
        if self.rule1(): return True
        if self.rule2(): return True
        if self.rule3(): return True
        return False
    
    def rule1(self):
        """200点以上なら合格"""
        return True if self.total_score >= 200 else False

    def rule2(self):
        """80点以上2科目以上かつ30点以上1科目以上なら合格"""
        cnt_score80over = 0
        cnt_score30over = 0
        for score in self.score_list:
            if score >= 80: cnt_score80over += 1  
            elif score >= 30: cnt_score30over += 1
        
        if cnt_score80over >= 2 and cnt_score30over >= 1: return True
        return False

    def rule3(self):
        """95点以上1科目以上かつ40点以上2科目以上なら合格"""
        cnt_score95over = 0
        cnt_score40over = 0
        for score in self.score_list:
            if score >= 95: cnt_score95over += 1  
            elif score >= 40: cnt_score40over += 1

        if cnt_score95over >= 1 and cnt_score40over >= 2: return True
        return False
    
    @staticmethod
    def total(score_list):
        total = 0
        for score in score_list:
            total += score
        return total


class ApplicationService:
    ERRMSG_INPUTERROR = "入力エラー:正しい値を入力してください"
    
    def run(self):
        # inputに表示and入力させる科目名を定義
        showmsg_list = []
        SUBJECT_ENGLISH = "英語"
        showmsg_list.append(SUBJECT_ENGLISH)
        SUBJECT_MATH = "数学"
        showmsg_list.append(SUBJECT_MATH)
        SUBJECT_JAPANESE = "日本語"
        showmsg_list.append(SUBJECT_JAPANESE)

        # inputを表示し、各科目のスコアをリストへ格納する
        score_list = []
        for msg in showmsg_list:
            while True:
                try:
                    user_input_score = self.showScoreInput(msg)
                    score = Score(user_input_score)
                    score_list.append(score.get())
                    break
                except ValueError:
                    print(self.ERRMSG_INPUTERROR)
                    continue

        # スコアリストを渡し、合格or不合格の判断・計算をクラスへ委譲する
        rule = PassingRule(score_list) 

        # クラスで計算された合格結果を出力
        if rule.isPassing():
            print("合格")
        else:
            print("不合格")

    @staticmethod
    def showScoreInput(msg):
        user_input = int(input(f"{msg}の点数を入力してください"))
        return user_input


if __name__ == "__main__":
    app = ApplicationService()
    app.run()
