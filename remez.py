import numpy as np
class Remez_coef_counter(object):
    def __init__(self):
        pass

    def CreateDenseGrid(self,r, numtaps, numband, bands, des,weight, gridsize,Grid,D,W,griddensity):
        delf = 0.5 / (griddensity * r)
        grid0 = bands[0]
        j = 0
        for band in range(numband):
            if band == 0:
                lowf = grid0
            else:
                lowf = bands[2 * band]
            highf = bands[2 * band + 1]
            k = int(((highf - lowf) / delf + 0.5))
            for i in range(k):
                D[j] = des[2 * band] + i * (des[2 * band + 1] - des[2 * band]) / (k - 1)
                W[j] = weight[band]
                Grid[j] = lowf
                lowf += delf
                j += 1
            Grid[j - 1] = highf


    def InitialGuess(self,r,Ext,gridsize):
        for i in range(r+1):
            Ext[i] = int(i * (gridsize - 1) / r)


    def  CalcParms(self, r, Ext, Grid, D, W, ad, x, y):
        for i in range(r + 1):
            x[i] = np.cos(np.pi* 2 * Grid[Ext[i]])
        ld = int((r - 1) / 15 + 1)
        for i in range(r + 1):
            denom = 1.0
            xi = x[i]
            for j in range(ld):
                for k in range(j,r+1,ld):
                    if k != i:
                        denom *= 2.0 * (xi - x[k])
            if (np.abs(denom) < 0.00001):
                denom = 0.00001
            ad[i] = 1.0 / denom
        numer = denom = 0
        sign = 1
        for i in range(r + 1):
            numer += ad[i] * D[Ext[i]]
            denom += sign * ad[i] / W[Ext[i]]
            sign = -sign
        delta = numer / denom
        sign = 1
        for i in range(r + 1):
            y[i] = D[Ext[i]] - sign * delta / W[Ext[i]]
            sign = -sign

    def ComputeA(self,freq, r, ad, x, y):
        denom = numer = 0
        xc = np.cos(np.pi * 2 * freq)
        for i in range(r+1):
            c = xc - x[i]
            if np.abs(c) < 1.0e-7:
                numer = y[i]
                denom = 1
                break
            c = ad[i] / c
            denom += c
            numer += c * y[i]
        return numer / denom

    def CalcError(self, r, ad, x, y, gridsize, Grid, D,  W, E):
        for i in range(gridsize):
            A = self.ComputeA(Grid[i], r, ad, x, y)
            E[i] = W[i] * (D[i] - A)

    def Search(self,r, Ext,	gridsize, E):
        foundExt = []
        for i in range(r * 2):
            foundExt.append(0)
        k = 0
        if  (((E[0]>0.0) and (E[0]>E[1])) or ((E[0]<0.0) and (E[0]<E[1]))):
            foundExt[k] = 0
            k += 1
        for i in range(1,gridsize - 1):
            if (((E[i] >= E[i - 1]) and (E[i] > E[i + 1]) and (E[i] > 0.0)) or ((E[i] <= E[i - 1]) and (E[i] < E[i + 1]) and (E[i] < 0.0))):
                    if (k >= 2 * r):
                        return -3
                    foundExt[k] = i
                    k += 1
        j = gridsize - 1
        if (((E[j] > 0) and (E[j] > E[j - 1])) or ((E[j] < 0) and (E[j] < E[j - 1]))):
                if (k >= 2 * r):
                    return -3
                foundExt[k] = j
                k += 1
        if (k < r + 1):
            return -2
        extra = k - (r + 1)
        while extra > 0:
            if (E[foundExt[0]] > 0.0):
                up = 1
            else:
                up = 0
            l = 0
            alt = 1
            for j in range(1, k):
                if (np.abs(E[foundExt[j]]) < np.abs(E[foundExt[l]])):
                    l = j
                if ((up) and (E[foundExt[j]] < 0.0)):
                    up = 0
                else:
                    if ((up==0) and (E[foundExt[j]] > 0.0)):
                        up = 1
                    else:
                        alt = 0
                        break
            if ((alt) and (extra == 1)):
                if (np.abs(E[foundExt[k - 1]]) < np.abs(E[foundExt[0]])):
                    l = k - 1
                else:
                    l = 0
            for j in range(l,k-1):
                foundExt[j] = foundExt[j + 1]
            k -= 1
            extra -= 1
        for i in range(r+1):
            Ext[i] = foundExt[i]
        return 0


    def isDone(self,r,Ext,E):
        min = max = np.abs(E[Ext[0]])
        for i in range(1,r+1):
            current = np.abs(E[Ext[i]])
            if (current < min):
                min = current
            if (current > max):
                max = current
        return ((max - min) / max) < 0.0001

    def FreqSample(self,N,A,h):
        M = (N - 1.0) / 2.0
        if (N % 2):
            for n in range (N):
                val = A[0]
                x = np.pi*2 * (n - M) / N
                for k  in range(1,int(M+1)):
                    val += 2.0 * A[k] * np.cos(x * k)
                h[n] = val / N
        else:
            for n in range(N):
                val = A[0]
                x = np.pi*2 * (n - M) / N
                for k in range (1, int(N / 2 - 1)+1):
                    val += 2.0 * A[k] * np.cos(x * k)
                h[n] = val / N


    def remez(self,numtaps,weight,bands):
        MAXITERATIONS = 40
        numbands = 3
        des= [0, 0, 1, 1, 0, 0]
        griddensity = 32
        coefs = []
        coefs.append(32)
        for i in range(1, numtaps):
            coefs.append(0)
        r = int(numtaps / 2)
        if numtaps % 2 != 0:
            r+=1
        gridsize = 0
        for i in range(numbands):
            gridsize += (int)(2 * r * (griddensity) * (bands[2 * i + 1] - bands[2 * i]) + .5)
        Grid=[]
        D=[]
        W=[]
        E=[]
        Ext=[]
        taps=[]
        x=[]
        y=[]
        ad=[]
        for i in range(gridsize):
            Grid.append(0)
            D.append(0)
            W.append(0)
            E.append(0)
        for i in range(r+1):
            Ext.append(0)
            taps.append(0)
            x.append(0)
            y.append(0)
            ad.append(0)
        self.CreateDenseGrid(r, numtaps, numbands, bands, des, weight, gridsize, Grid, D, W, griddensity)
        self.InitialGuess(r,Ext,gridsize)
        if numtaps % 2 == 0:
            for i in range(gridsize):
                c = np.cos(np.pi*Grid[i])
                D[i] /= c
                W[i] *= c
        for iter in range(MAXITERATIONS):
            self.CalcParms(r, Ext, Grid, D, W, ad, x, y)
            self.CalcError(r, ad, x, y, gridsize, Grid, D, W, E)
            err = self.Search(r, Ext, gridsize, E)
            if self.isDone(r, Ext, E):
                break
        self.CalcParms(r, Ext, Grid, D, W, ad, x, y)
        for i in range(int(numtaps/2)):
            if (numtaps % 2):
                c = 1
            else:
                c = np.cos(np.pi * i /numtaps)
            taps[i] = self.ComputeA(i/numtaps, r, ad, x, y)*c
        self.FreqSample(numtaps, taps, coefs)
        print(coefs)
        return coefs

if __name__ == '__main__':
    counter = Remez_coef_counter()
    counter.remez(41,[10,3,10],[0, 0.03, 0.06, 0.0733, 0.1033, 0.5])