from log_equation import *
from filter_size import *
import scipy
from scipy import signal
from scipy import fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
from UI import *
from remez import Remez_coef_counter
from PyQt5.QtWidgets import QDialog,QDialogButtonBox,QLabel,QFileDialog

class App(object):
    def __init__(self):
        pass
    def count_but(self,foo):
        try:
            self.fs = float(foo.lineEdit_3.text())
            width = float(foo.lineEdit_4.text())
            left = float(foo.lineEdit.text())
            right = float(foo.lineEdit_2.text())
            size = int(size_count(0.1,0.01,width/self.fs))
            self.coef = scipy.signal.remez(int(size+size/2), [0, left-width, left, right, right+width, self.fs/2], [0, 1, 0], fs=self.fs)
            counter = Remez_coef_counter()
            #self.coef = counter.remez(41,[10,3,10],[0, 0.03, 0.06, 0.0733, 0.1033, 0.5])
            w, H = scipy.signal.freqz(self.coef, worN = 1024)
            foo.m.plot(0.5*self.fs*w/np.pi,np.abs(H),1,"","f,Гц","Амплитуда")

        except Exception:
            print("error")
            label = QLabel("Ошибка ввода! проверьте правильность введенных данных")
            but = QPushButton("Закрыть")
            dialog = QDialog()
            dialog.setLayout(QVBoxLayout())
            dialog.setWindowTitle("Dialog")
            dialog.layout().addWidget(label)
            dialog.layout().addWidget(but)
            but.clicked.connect(lambda:self.dialog_exit(dialog))
            dialog.exec_()


    def open_file_but(self,foo):
        sig = []
        fname = QFileDialog.getOpenFileName(foo, 'Oткрыть файл с сигналом', '', "All Files ();;Text Files (.txt)")[0]
        try:
            f = open(fname, 'r')
            with f:
                for line in f:
                    sig.append(float(line))
            t = 1/self.fs
            T = t*len(sig)
            df = 1 / T
            new_sig = scipy.signal.filtfilt(self.coef, 1, sig)
            x = range(0,len(sig))
            foo.sig.plot(x,sig,1,"","t,c","Амплитуда")
            foo.n_sig.plot(x,new_sig,1,"","t,c","Амплитуда")
            w, H = scipy.signal.freqz(self.coef, worN=1024)
            foo.m.figure.legend()
            foo.m.plot(0.5 * self.fs * w / np.pi, np.abs(H),1,"АЧХ фильтра","f,Гц","Амплитуда")

            foo.m.plot(fft.rfftfreq(len(sig))*len(x)*df,np.abs(fft.rfft(sig)*2/len(sig)),0,"АЧХ исходного сигнала","f,Гц","Амплитуда")

            foo.m.plot(fft.rfftfreq(len(sig))*len(x)*df,np.abs(fft.rfft(new_sig)*2/len(x)),-1,"АЧХ отфитрованного сигнала","f,Гц","Амплитуда")

        except Exception as e:
            print(e)


    def dialog_exit(self,dialog):
        dialog.reject()


    def open_audio(self,foo):
        options = QFileDialog.Options()
        fileName,_ = QFileDialog.getOpenFileName(foo, "Открыть аудиоайл", "",
                                                  "WAV файлы (*.wav)", options=options)
        if fileName:
            from scipy import signal
            from scipy.io.wavfile import read
            try:
                rate, self.samples = read(fileName)
            except Exception as e:
                print(e)
            buf_samples = self.samples[:]

            try:
                a = len(buf_samples[0])
                samples1 = [i[0] for i in buf_samples]
                self.two_channel = True
            except Exception as e:
                samples1 = [i for i in buf_samples]
                self.two_channel = False

            N = len(self.samples)
            fs = float(rate)
            # self.sig = signal.resample(samples1, 44100)
            sig = samples1[:]
            t = 1 / self.fs
            T = t * len(sig)
            df = 1 / T
            new_sig = scipy.signal.filtfilt(self.coef, 1, sig)
            x = range(0, len(sig))
            foo.sig.plot(x, sig, 1, "", "t,c", "Амплитуда")
            foo.n_sig.plot(x, new_sig, 1, "", "t,c", "Амплитуда")
            w, H = scipy.signal.freqz(self.coef, worN=1024)
            foo.m.figure.legend()
            foo.m.plot(0.5 * self.fs * w / np.pi, np.abs(H),1,"АЧХ фильтра","f,Гц","Амплитуда")

            foo.m.plot(fft.rfftfreq(len(sig))*len(x)*df,np.abs(fft.rfft(sig)*2/len(sig)),0,"АЧХ исходного сигнала","f,Гц","Амплитуда")

            foo.m.plot(fft.rfftfreq(len(sig)) * len(x) * df, np.abs(fft.rfft(new_sig) * 2 / len(x)), -1,
                       "АЧХ отфитрованного сигнала", "f,Гц", "Амплитуда")



import sys
if __name__ == '__main__':
    obj = App()
    app = QtWidgets.QApplication([])
    foo = Ui_MainWindow()
    foo.pushButton.clicked.connect(lambda: obj.count_but(foo))
    foo.action.triggered.connect(lambda: obj.open_audio(foo))
    foo.action_2.triggered.connect(lambda: obj.open_file_but(foo))
    foo.show()
    sys.exit(app.exec_())



