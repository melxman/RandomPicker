from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, BooleanProperty
import random

kv = '''
BoxLayout:
    orientation: 'vertical'
    padding: 30
    spacing: 20

    Label:
        id: info
        text: root.info_text
        font_size: '42sp'
        color: 0.2, 0.6, 0.8, 1

    GridLayout:
        cols: 2
        spacing: 20
        size_hint_y: .3
        disabled: not root.can_mark

        Button:
            text: '对 / Correct'
            font_size: '24sp'
            on_release: root.mark(True)

        Button:
            text: '错 / Wrong'
            font_size: '24sp'
            on_release: root.mark(False)

    Button:
        text: '提交 / Submit'
        font_size: '24sp'
        size_hint_y: .15
        disabled: not root.can_submit
        on_release: root.next_round()

    Button:
        text: '重置 / Reset'
        font_size: '24sp'
        size_hint_y: .15
        on_release: root.reset_all()

    Label:
        text: root.stat_text
        font_size: '24sp'
        color: 0.9, 0.2, 0.2, 1
'''

class RootWidget(BoxLayout):
    numbers       = ListProperty()
    info_text     = StringProperty("点击“提交”开始第一轮")
    stat_text     = StringProperty("")
    wrong_numbers = ListProperty()
    current_num   = None
    can_mark      = BooleanProperty(False)
    can_submit    = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_pool()

    def reset_pool(self):
        self.numbers = list(range(1, 41))
        random.shuffle(self.numbers)
        self.wrong_numbers.clear()
        self.current_num = None
        self.can_mark = False
        self.can_submit = True
        self.stat_text = ""

    def mark(self, ok):
        if self.current_num is not None and not ok:
            self.wrong_numbers.append(self.current_num)

    def next_round(self):
        if not self.numbers:
            self.show_result()
            return
        self.current_num = self.numbers.pop()
        self.info_text = f"选中：{self.current_num}"
        self.can_mark, self.can_submit = True, False

    def show_result(self):
        wrong = sorted(self.wrong_numbers)
        self.info_text = "全部完成！"
        self.stat_text = f"错误数量：{len(wrong)}\n错误号码：{wrong or '无'}"
        self.can_mark = self.can_submit = False

    def reset_all(self):
        self.reset_pool()
        self.info_text = "点击“提交”开始第一轮"

class RandomPickerApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    RandomPickerApp().run()