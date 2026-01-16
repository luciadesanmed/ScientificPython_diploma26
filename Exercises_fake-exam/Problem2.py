if __name__=="__main__":
 print("Script is running directly")

#Generate random data for 2D points coordinates. Write a function that plots them with different colors for each 90 degree section with the origin in the center. This problem should be coded as a class, i.e. you should be able to execute the code:
#pr=Problem2()
#pr.generate()
#pr.display()

import numpy as np
import matplotlib.pyplot as plt

class Problem2:
    def __init__(self,n):
        self.n=n

    def generate(self):
        lim1=-5
        lim2=5
        self.x=np.random.uniform(lim1,lim2,self.n)
        self.y=np.random.uniform(lim1,lim2,self.n)
        return self.x, self.y
        
    def display(self):
        limi=np.zeros(2)
        limi[0]=abs(np.min([np.min([self.x,self.y]),np.max([self.x,self.y])]))
        limi[1]=abs(np.max([np.min([self.x,self.y]),np.max([self.x,self.y])]))
        fig, ax = plt.subplots()
        for i in range(self.n):
            if self.x[i]>0 and self.y[i]>0:
                ax.plot(self.x[i],self.y[i],'om')
            elif self.x[i]>0 and self.y[i]<0:
                ax.plot(self.x[i],self.y[i],'oc')
            elif self.x[i]<0 and self.y[i]<0:
                ax.plot(self.x[i],self.y[i],'oy')
            elif self.x[i]<0 and self.y[i]>0:
                ax.plot(self.x[i],self.y[i],'og')
                
        ax.set_xlim([-np.max(limi),np.max(limi)])
        ax.set_ylim([-np.max(limi),np.max(limi)])
        plt.show()


pr = Problem2(200)
pr.generate()
pr.display()