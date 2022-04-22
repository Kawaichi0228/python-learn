#! /usr/bin/env python3.9
def call_func_object(func_object) -> None:
    """コールバック関数を呼び出す(単体)"""
    func_object() # カッコをつけることで関数を呼び出せる

def call_func_object_to_list(func_object_list) -> None:
    """コールバック関数を呼び出す(複数:リストでループ)"""
    for func in func_object_list:
        func() # カッコをつけることで関数を呼び出せる

def process_call_func_object() -> None:
    """コールバック関数を渡す(関数をオブジェクトとして変数に代入する)
     - コールバック関数に引数を渡したいときはlambda式を使う"""
    callback_func = (
        lambda num1=80, num2=15: 
        print_double(num1, num2)
    )
    call_func_object(callback_func)

def process_call_func_object_to_list() -> None:
    """コールバック関数を渡す(関数をオブジェクトとして変数に代入(append)する)
    - コールバック関数に引数を渡したいときはlambda式を使う"""
    callback_func_list = []
    callback_func_list.append(lambda num1=200, num2=300: 
                        print_double(num1, num2))
    callback_func_list.append(lambda num1=1500, num2=3200: 
                        print_double(num1, num2))
    callback_func_list.append(lambda num1=80, num2=15: 
                        print_double(num1, num2))
    call_func_object_to_list(callback_func_list)

def print_double(num1, num2) -> None:
    """コールバック関数として使うための関数"""
    print(num1 * 2)
    print(num2 * 2)

def main() -> None:
    print("----------------------------------------------------------")
    print("引数として与えられた関数オブジェクト(単体)の実行を開始します")
    print("----------------------------------------------------------")
    process_call_func_object()

    print("----------------------------------------------------------")
    print("引数として与えられた関数オブジェクト(複数)の実行を開始します")
    print("----------------------------------------------------------")
    process_call_func_object_to_list()

if __name__ == "__main__":
    main()