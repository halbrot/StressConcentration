import numpy as np
import matplotlib.pyplot as plt



class Stress:
    
    def __init__(self,sigma0, a):
        self.sigma0 = sigma0
        self.a = a
        self.K1 = self.sigma0 / (3.1415 * self.a)**0.5
    
    
    def calc_area(self):
        self.theta = np.arange(-178,178.1, 1)
        self.r = np.arange(0.1,5,0.05)
        
        self.theta = np.radians(self.theta)

        self.r2, self.theta2 = np.meshgrid(self.r, self.theta)
    
    def stress(self):
        k = self.K1 / (2*3.1415*self.r2)**0.5 * np.cos(self.theta2/2)
        
        sigma_x = k * (1 - np.sin(self.theta2/2) * np.sin(3*self.theta2/2))
        sigma_y = k * (1 + np.sin(self.theta2/2) * np.sin(3*self.theta2/2))
        tau_xy = k * np.sin(self.theta2/2) * np.cos(3*self.theta2/2)
        sigma_z = 0.3 * (sigma_x + sigma_y) #平面ひずみ
        _mises = self.mises(sigma_x, sigma_y, sigma_z, tau_xy, 0, 0)

        x = self.r2 * np.cos(self.theta2)
        y = self.r2 * np.sin(self.theta2)
        
        return (x, y, _mises)

    def mises(self, x, y, z, xy, yz, zx):
        return (0.5*((x-y)**2+(y-z)**2+(z-x)**2+3*(xy**2+yz**2+zx**2)))**0.5

    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 6), dpi=100)
        contr = self.ax.contourf(*ret, cmap="jet")
        self.fig.colorbar(contr)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        plt.show()


if __name__ == "__main__":
    
    st = Stress(1000, 0.1)
    st.calc_area()
    ret = st.stress()
    st.plot()




