"""メソッドチェーン"""
class AddText:
    def __init__(self):
        self.text = ''

    def add(self, add_text):
        self.text += add_text
        return self

    def __repr__(self):
        return self.text

a = AddText()
b = a.add('test').add('_test')
