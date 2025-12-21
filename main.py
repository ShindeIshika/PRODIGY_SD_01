import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox, QFrame
)
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

# ---------- Window ----------
window = QWidget()
window.setWindowTitle("Temperature Converter")
window.setFixedSize(500, 380)
window.setStyleSheet("background-color: #F4F6F7;")

# ---------- Card Container ----------
card = QFrame()
card.setFixedSize(420, 300)
card.setStyleSheet("""
QFrame {
    background-color: white;
    border-radius: 12px;
}
""")

# ---------- Title ----------
title = QLabel("🌡️ Temperature Converter")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("""
font-size: 22px;
font-weight: bold;
color: #2C3E50;
""")

subtitle = QLabel("Convert Celsius and Fahrenheit easily")
subtitle.setAlignment(Qt.AlignCenter)
subtitle.setStyleSheet("""
font-size: 12px;
color: #7F8C8D;
""")

# ---------- Input ----------
input_box = QLineEdit()
input_box.setPlaceholderText("Enter temperature")
input_box.setStyleSheet("""
QLineEdit {
    padding: 10px;
    font-size: 14px;
    border-radius: 6px;
    border: 1px solid #D5DBDB;
}
QLineEdit:focus {
    border: 1px solid #3498DB;
}
""")

# ---------- Dropdown ----------
unit_selector = QComboBox()
unit_selector.addItems([
    "Celsius → Fahrenheit",
    "Fahrenheit → Celsius"
])
unit_selector.setStyleSheet("""
QComboBox {
    padding: 8px;
    border-radius: 6px;
    border: 1px solid #D5DBDB;
}
""")

# ---------- Button ----------
convert_button = QPushButton("Convert")
convert_button.setCursor(Qt.PointingHandCursor)
convert_button.setStyleSheet("""
QPushButton {
    background-color: #3498DB;
    color: white;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
}
QPushButton:hover {
    background-color: #2E86C1;
}
""")

# ---------- Result ----------
result_label = QLabel("Result will appear here")
result_label.setAlignment(Qt.AlignCenter)
result_label.setStyleSheet("""
font-size: 14px;
color: #2C3E50;
""")

# ---------- Card Layout ----------
card_layout = QVBoxLayout(card)
card_layout.setSpacing(12)
card_layout.setContentsMargins(30, 25, 30, 25)

card_layout.addWidget(title)
card_layout.addWidget(subtitle)
card_layout.addSpacing(10)
card_layout.addWidget(input_box)
card_layout.addWidget(unit_selector)
card_layout.addWidget(convert_button)
card_layout.addSpacing(5)
card_layout.addWidget(result_label)

# ---------- Center Card ----------
main_layout = QVBoxLayout(window)
main_layout.setAlignment(Qt.AlignCenter)
main_layout.addWidget(card)

# ---------- Logic ----------
def convert_temperature():
    value = input_box.text().strip()
    if not value:
        result_label.setText("❌ Please enter a value")
        return

    choice = unit_selector.currentIndex()

    if choice == 0:
        mode = "C2F"
    else:
        mode = "F2C"

    try:
        exe_path = os.path.join(os.path.dirname(__file__), "temperature_converter.exe")

        output = subprocess.check_output(
        [exe_path, value, mode],
        stderr=subprocess.STDOUT,
        text=True
).strip()


        unit = "°F" if mode == "C2F" else "°C"
        result_label.setText(f"✅ {output} {unit}")

    except:
        result_label.setText("❌ Conversion failed")

convert_button.clicked.connect(convert_temperature)

# ---------- Show ----------
window.show()
app.exec()
