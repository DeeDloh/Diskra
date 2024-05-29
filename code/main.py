import sys

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar

from window_matrix import AdjMatrixInput
from color_group import find_color_group
from code import COLOR_PERE


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Graph Viewer')
        self.setGeometry(200, 100, 1200, 800)

        # Создание основной компоновки
        main_layout = QHBoxLayout()

        # Компоновка для кнопок
        button_layout = QVBoxLayout()

        # Создание кнопок
        self.matrix = QPushButton('Ввести матрицу смежности', self)
        self.matrix.clicked.connect(self.open_matrix_window)
        # self.show_color = QPushButton('Показать вершины по цветам', self)
        self.matrix.setFixedSize(200, 125)
        # self.show_color.setFixedSize(200, 125)

        # Добавление кнопок в компоновку
        button_layout.addWidget(self.matrix)
        # button_layout.addWidget(self.show_color)

        # Создание фигуры и полотна для графа
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Компоновка для графа
        graph_layout = QVBoxLayout()
        graph_layout.addWidget(self.toolbar)
        graph_layout.addWidget(self.canvas)

        # Добавление компоновок в основную компоновку
        main_layout.addLayout(button_layout)
        main_layout.addLayout(graph_layout)

        self.setLayout(main_layout)
        self.matrix = np.array([[1, 1, 1, 0, 0, 0, 1],
                                [1, 1, 1, 1, 0, 0, 0],
                                [1, 1, 1, 1, 0, 1, 1],
                                [0, 1, 1, 1, 1, 0, 1],
                                [0, 0, 0, 1, 1, 1, 0],
                                [0, 0, 1, 0, 1, 1, 0],
                                [1, 0, 1, 1, 0, 0, 1]])
        self.eye = np.eye(len(self.matrix))
        # Задаем цвета для каждой вершины для графа примера.
        self.node_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
        self.draw_graph()

    def draw_graph(self):
        matrix = self.matrix - self.eye
        G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
        edge_nodes = set(G)
        pos = nx.circular_layout(G.subgraph(edge_nodes))

        nx.draw(G, pos, ax=self.ax, with_labels=1, node_color=self.node_colors, node_size=700, arrows=False)
        self.canvas.draw()

    def open_matrix_window(self):
        self.win_mat = AdjMatrixInput(self)
        # Проверяет, что диаологовое окно закрыто с помощью кода accept
        if self.win_mat.exec_() == QDialog.Accepted:
            self.matrix = np.array(self.win_mat.data)
        self.new_graph()

    def new_graph(self):
        self.color_gr = find_color_group(self.matrix.copy())
        temp_node_color = [''] * len(self.matrix)
        for key, value in self.color_gr.items():
            for i in value:
                temp_node_color[i] = COLOR_PERE[key]
        self.node_colors = temp_node_color
        self.eye = np.eye(len(self.matrix))
        self.ax.cla()
        self.draw_graph()


def main():
    app = QApplication(sys.argv)
    main_window = GraphWidget()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
