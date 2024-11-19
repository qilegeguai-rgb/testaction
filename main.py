from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QButtonGroup 循环激活示例")
        self.setGeometry(100, 100, 300, 200)

        # 主部件和布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 创建按钮组
        self.button_group = QButtonGroup(self)

        # 创建按钮并添加到按钮组
        for i in range(1, 4):
            button = QPushButton(f"按钮 {i}")
            button.setEnabled(False)  # 初始状态不可点击
            self.button_group.addButton(button, i)  # 使用按钮 ID 作为索引
            layout.addWidget(button)

        # 激活第一个按钮
        self.button_group.button(1).setEnabled(True)

        # 连接按钮组的信号
        self.button_group.buttonClicked.connect(self.on_button_clicked)

        self.setCentralWidget(central_widget)

    def on_button_clicked(self, clicked_button):
        # 获取当前点击按钮的 ID
        current_id = self.button_group.id(clicked_button)

        # 禁用当前按钮
        clicked_button.setEnabled(False)

        # 计算下一个按钮的 ID（循环激活）
        print(len(self.button_group.buttons()))
        ss = current_id % len(self.button_group.buttons())
        print(ss)
        next_id = (current_id % len(self.button_group.buttons())) + 1
        self.button_group.button(next_id).setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()