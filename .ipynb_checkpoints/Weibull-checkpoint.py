from scipy.special import gamma
import math

class Weibull:
    '''
w = Weibull(shape:beta,scale:theta,position:lambda)

    '''
    def __init__(self,k,lmbda,delta):
        self.k = k
        self.lmbda = lmbda
        self.delta = delta
        self.x = (np.random.weibull(k,1000)*lmbda) + delta
        _,self.bins  = np.histogram(self.x,100,density=True)


    def pdf(self):
        x = self.bins
        k = self.k
        lmbda = self.lmbda
        delta =  self.delta
        return ((k/lmbda)*((x-delta)/lmbda)**(k-1))*(np.exp(-((x-delta)/lmbda)**k))

    def cdf(self):
        x = self.bins
        k = self.k
        lmbda = self.lmbda
        delta = self.delta
        return 1- np.exp(-((x-delta)/lmbda)**k)

    def failure_rate(self):
        x = self.x
        k = self.k
        lmbda = self.lmbda
        return (k/lmbda)*((x/lmbda)**(k-1))

    def E_x(self):
        k = self.k
        lmbda = self.lmbda
        return lmbda*(gamma(1+1/k))

    def var_x(self):
        k = self.k
        lmbda = self.lmbda
        return (lmbda**2)*(gamma(1+(2/k))-((gamma(1+(1/k)))**2))

    def plot_pdf(self):
        plt.plot(self.bins,self.pdf())
    
    def plot_cdf(self):
        plt.plot(self.bins,self.cdf())

    def plot_fr(self):
        plt.plot(self.bins,self.failure_rate())
    
    def plot_hist(self):
        plt.hist(self.x)

    def find_x(self,F_x):
        return (self.lmbda)*((-math.log(1-F_x))**(1/self.k)) + self.delta
w = Weibull(25,12.887,25.5146)

X = w.find_x(0.5)
print('X:(the one with 0.5 CDF)',X)
