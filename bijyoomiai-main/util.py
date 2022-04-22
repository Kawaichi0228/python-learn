import random

class Util:
    @staticmethod
    def getRandomNum(from_, to_) -> int:
        return random.randint(from_,to_)
    
    @staticmethod
    def getDictionaryIndex(dict_, targetkey, base=0) -> int:
        """dictから指定したkeyのindexを取得
        MEMO: 辞書のkeyをindexとして取得が分からなかったので関数作った
        """
        i = base
        for key in dict_.keys():
            if key == targetkey:
                index = i 
                break
            i += 1
        return index
    
    @staticmethod
    def descendingSortDict(dict_) -> dict:
        tmp_dict_ = sorted(dict_.items(), reverse=True, key=lambda x : x[1])
        return dict(tmp_dict_) # MEMO: なぜか正常な辞書が作成できなかったのでdictで変換