from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from matplotlib.figure import Figure
import random
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=None, height=None, dpi=100):
        fig = Figure(figsize=(width, 2))
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # FigureCanvas.setSizePolicy(self,
        #                             QSizePolicy.Expanding,
        #                             QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)
        #self.plot()

    def plot(self,x,y,flag,label,xlabel,ylabel):
        ax = self.figure.add_subplot(111)
        if flag==1:
            ax.clear()
        ax.plot(x,y,label=label)
        if flag==-1:
             self.figure.legend()
        #ax.set_title('АЧХ фильтра')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.figure.tight_layout()
        self.draw()