import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget, QPushButton, QSpinBox, QHBoxLayout, QLabel)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt


class AdjMatrixInput(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Adjacency Matrix Input")
        self.setGeometry(100, 100, 800, 600)

        self.table_widget = QTableWidget(self)

        # Create spin boxes to set the size of the matrix
        self.size_spinbox = QSpinBox(self)
        self.size_spinbox.setRange(1, 20)  # Set range as needed
        self.size_spinbox.setValue(4)  # Default value
        self.size_spinbox.valueChanged.connect(self.update_table_size)

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Size:"))
        size_layout.addWidget(self.size_spinbox)

        self.layout = QVBoxLayout()
        self.layout.addLayout(size_layout)
        self.layout.addWidget(self.table_widget)

        self.submit_button = QPushButton("Ввод", self)
        self.submit_button.clicked.connect(self.submit_matrix)
        self.layout.addWidget(self.submit_button)

        self.close_button = QPushButton("Закрыть", self)
        self.close_button.clicked.connect(self.close)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

        self.update_table_size()

    def update_table_size(self):
        size = self.size_spinbox.value()
        self.table_widget.setRowCount(size)
        self.table_widget.setColumnCount(size)

        int_validator = QIntValidator(0, 1, self)  # Allow only 0 or 1

        for row in range(size):
            for col in range(size):
                item = self.table_widget.item(row, col)
                if not item:
                    item = QTableWidgetItem()
                    self.table_widget.setItem(row, col, item)
                if row == col:
                    item.setText("1")
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Make diagonal cells non-editable
                else:
                    item.setText("0")
                    item.setFlags(item.flags() | Qt.ItemIsEditable)  # Make other cells editable
                    item.setData(Qt.UserRole, int_validator)
                item.setTextAlignment(Qt.AlignCenter)

    def submit_matrix(self):
        size = self.table_widget.rowCount()
        matrix = []

        for row in range(size):
            matrix_row = []
            for col in range(size):
                item = self.table_widget.item(row, col)
                if item and item.text().isdigit():
                    matrix_row.append(int(item.text()))
                else:
                    matrix_row.append(0)
            matrix.append(matrix_row)

        # print("Adjacency Matrix:")
        # for row in matrix:
        #    print(row)

        self.data = matrix
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdjMatrixInput()
    window.show()
    sys.exit(app.exec_())
