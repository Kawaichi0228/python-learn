from enum import Enum


# Enum(列挙体)。呼び出す側からはSwitch文と相性が良い
# (pythonには無いのでifとelifで代用)
class FizzbuzzEnum(Enum):
    FIZZBUZZ = 1
    FIZZ = 2
    BUZZ = 3


# 関数でdictを使った簡便的なやり方
def fizzBuzzDict():
    fizzbuzz_dict = {}
    fizzbuzz_dict["FIZZBUZZ"] = 1
    fizzbuzz_dict["FIZZ"] = 2
    fizzbuzz_dict["BUZZ"] = 3
    return fizzbuzz_dict
# ----------------------------------------------------------------
def calclateFizzBuzz(num):
    if (num % 3 == 0) and (num % 5 == 0): return FizzbuzzEnum.FIZZBUZZ
    if (num % 3 == 0): return FizzbuzzEnum.FIZZ
    if (num % 5 == 0): return FizzbuzzEnum.BUZZ

def main():
    # 1から100までの整数リストを作りまわす
    num_list = [num for num in range(1,101,1)]
    num_and_fizzbuzz_list = []
    for num in num_list:
        # 判定し取得した定数(number)から分岐処理
        # (PythonにはSwitch文がないため、ifとelifと使用)
        exp = calclateFizzBuzz(num) # 整数式
        if exp == FizzbuzzEnum.FIZZBUZZ: # 定数式
            num_and_fizzbuzz_list.append("FizzBuzz")
        elif exp == FizzbuzzEnum.FIZZ:
            num_and_fizzbuzz_list.append("Fizz")
        elif exp == FizzbuzzEnum.BUZZ: 
            num_and_fizzbuzz_list.append("Buzz")
        else:
            num_and_fizzbuzz_list.append(num)
    
    # 出力
    i = 1
    for fizbz in num_and_fizzbuzz_list:
        # [f-string説明(コロンの後ろ)]桁埋め文字:" ", 左寄せ"<", 桁数"8桁"
        print(f"{fizbz: <8}", end=" ")
        
        if i % 6 == 0: print() # 処理6回ごとに改行
        i += 1

if __name__ == "__main__":
    main()