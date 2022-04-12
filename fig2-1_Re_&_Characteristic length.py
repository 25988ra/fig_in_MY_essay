import numpy as np 
import matplotlib.pyplot as plt 
def Re(u,rho,L,mu):
    return u*rho*L/mu
u = np.linspace(1,10,4)
rho = 1*10**3
L = np.arange(1,1000)
mu = 8.9*10**(-4)
Re_c = np.ones(len(L))*2300

plt.ylabel("Re")
plt.xlabel("L  ($\mu m$)")

for i in range(4):
    plt.plot(L,Re(u[i]*10**(-1),rho,L*10**(-6),mu))
plt.plot(L,Re_c)
legend_list = ["u_m = %.2f m/s"%(u[i]*10**(-1)) for i in range(4)]

legend_list.append("$Re_{cr}$=2300")
plt.legend(legend_list,loc = "upper left")
plt.show()
