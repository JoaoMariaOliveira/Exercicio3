import numpy as np
import matplotlib.pyplot as plt
class PolinomPop:
    def __init__(self, Scale, PopSize):
        self.PopSize = PopSize
        self.Scale = Scale
        self.Parameters = np.random.uniform(-abs(Scale), abs(Scale), size =5)
        self.x = np.random.uniform(-(abs(Scale)**2), abs(Scale)**2, size=PopSize)
        self.j = self.Parameters[0] + self.Parameters[1]*self.x + (self.Parameters[2]/3)*self.x**2 + \
                (self.Parameters[3]/5)*self.x**3 + (self.Parameters[4]/10)*self.x**4 + \
                 np.random.normal(0,Scale**5,size = PopSize)
        self.Poly = np.poly1d(self.Parameters)
        self.y = self.Poly(self.x) + np.random.normal(0,Scale**4,size = PopSize)

    def Sample(self, SampleSize):
        sample = np.random.choice(list(range(self.PopSize)), SampleSize, replace = False)
        return self.x[sample], self.y[sample]

    def FitPolys(self, SampleSize):
        sample = self.Sample(SampleSize)
        xx = np.linspace(-abs(self.Scale**2), abs(self.Scale**2), self.PopSize)
        fig = plt.figure(figsize = [10,8])
        fig.suptitle('n = '+ str(SampleSize))
        plt.plot(self.x, self.y, 'yo')
        plt.plot(sample[0],sample[1], 'ro')
        E =list()
        for i in range(1, 5):
            fit = np.poly1d(np.polyfit(sample[0], sample[1], i))

            plt.plot(xx, fit(xx), linewidth=3)
            Ein = sum((sample[1] - fit(sample[0])) ** 2) / SampleSize
            Etot = sum((self.y - fit(self.x)) ** 2) / self.PopSize
            print("Polinomio de grau: ", i, "\nAmostra de tamanho:", SampleSize, "\n  Erro dentro da amostra:", Ein,
                  "\n  Erro fora da amostra", Etot)
            E.append([SampleSize,i,Ein, Etot])

        plt.show()
        return E

if __name__ == "__main__":
    Er=list()
    P = PolinomPop(1.5,500)
    print(P.Parameters)
    Er.append([P.FitPolys(5)])
    Er.append([P.FitPolys(10)])
    Er.append([P.FitPolys(25)])
    Er.append([P.FitPolys(50)])
    Er.append([P.FitPolys(100)])


