# calclationbmi-master

## 目的
- 授業で学んだPythonの機能を復習するため
- 追加や変更に強いコード設計を勉強し試すため(DDDなど)

## 内容

授業の課題であった

- 体重と身長からbmiを計算
- bmiをもとに体型を判定

を以下のようなif分岐多用で書くのではなく、きちんと設計して書いてみたかったので、クラス化した。

```python
# bad
if bmi < 18.5:
    bodytype = "やせ"
elif 18.5 <= bmi < 25:
    bodytype = "標準"
elif ...:
    ...
```
