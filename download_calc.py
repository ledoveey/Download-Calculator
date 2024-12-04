from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
seconds, minutes, hours = 0, 0, 0
def calculate_time():
    global seconds, minutes, hours

    gb_left_text = gb_input.text()
    speed_text = speed_input.text()

    if not gb_left_text or not speed_text:
        result_label.setText("Vyplňte obě pole!")
        return
    
    try:
        gb_left = float(gb_input.text())
        if gb_unit_selector.currentText() == "MB":
            gb_left /= 1000 

        mbps = float(speed_input.text())
        if speed_unit_selector.currentText() == "KB/s":
            mbps /= 1000

        mb_left = gb_left * 1000
        seconds = mb_left / mbps
        minutes = seconds / 60
        hours = minutes / 60

        update_result()  
    except ValueError:
        result_label.setText("Chyba: Zadejte platná čísla!")

def update_result():
    global seconds, minutes, hours
    selected_unit = result_unit_selector.currentText()
    if selected_unit == "Sekundy":
        result_label.setText(f"Zbývající čas: {seconds:.2f} sekund")
    elif selected_unit == "Minuty":
        result_label.setText(f"Zbývající čas: {minutes:.2f} minut")
    elif selected_unit == "Hodiny":
        result_label.setText(f"Zbývající čas: {hours:.2f} hodin")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Kalkulačka stahování")

dark_theme = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
        font-size: 14px;
    }
    QLineEdit {
        background-color: #3c3f41;
        border: 1px solid #5c5c5c;
        color: #ffffff;
        padding: 5px;
    }
    QPushButton {
        background-color: #5c5c5c;
        border: 1px solid #888888;
        color: #ffffff;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #6d6d6d;
    }
    QLabel {
        font-size: 16px;
    }
    QComboBox {
        background-color: #3c3f41;
        border: 1px solid #5c5c5c;
        color: #ffffff;
        padding: 5px;
    }
"""
app.setStyleSheet(dark_theme)

layout = QVBoxLayout()

gb_layout = QHBoxLayout()
gb_layout.addWidget(QLabel("Zbývá stáhnout:"))
gb_input = QLineEdit()
gb_input.textChanged.connect(calculate_time)  
gb_layout.addWidget(gb_input)

gb_unit_selector = QComboBox()
gb_unit_selector.addItems(["GB", "MB"])
gb_unit_selector.currentIndexChanged.connect(calculate_time)  
gb_layout.addWidget(gb_unit_selector)
layout.addLayout(gb_layout)

speed_layout = QHBoxLayout()
speed_layout.addWidget(QLabel("Rychlost stahování:"))
speed_input = QLineEdit()
speed_input.textChanged.connect(calculate_time)  
speed_layout.addWidget(speed_input)

speed_unit_selector = QComboBox()
speed_unit_selector.addItems(["MB/s", "KB/s"])
speed_unit_selector.currentIndexChanged.connect(calculate_time)  
speed_layout.addWidget(speed_unit_selector)
layout.addLayout(speed_layout)

result_layout = QHBoxLayout()
result_layout.addWidget(QLabel("Zobrazit výsledek v:"))
result_unit_selector = QComboBox()
result_unit_selector.addItems(["Sekundy", "Minuty", "Hodiny"])
result_unit_selector.currentIndexChanged.connect(update_result)
result_layout.addWidget(result_unit_selector)
layout.addLayout(result_layout)

result_label = QLabel("")
layout.addWidget(result_label)

window.setLayout(layout)
window.show()
app.exec_()
