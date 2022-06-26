from math import *
def size_count(delta_p,delta_s,delta_F):
    buf = delta_p/delta_s
    g = -14.6*log10(buf) - 16.9
    C = log10(delta_s)*(0.01201*pow(log10(delta_p),2)+0.09664*log10(delta_p)-0.51325)+(0.00203*pow(log10(delta_p),2)-0.5705*log10(delta_p)-0.44314)
    N = C/delta_F+g*delta_F+1
    return N