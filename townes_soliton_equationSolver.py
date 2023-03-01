import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp, simps
from scipy.stats import norm
from scipy.constants import pi
from scipy import integrate

def func(r, u): #here we define the differential equation we want to solve numerically
    """
    Sistema de equações:
        dR/dr = g
        dg/dr = -1/r * g - R**3 + R
    """
    R, g = u
    return np.vstack((g, -2*R**3 + 2*R))

def bc(ya, yb): #here we define the boundary conditions. For our problem, R' at r=0 and R at infinity are both zero.
    """
    Condição de contorno:
        dR/dr(0) = 0    
        R(r = infinito) = 0
    """
    return np.array([ya[1], yb[0]]) #ya refers to the BC evaluated at the leftmost value of r and ya to the rightmost value of r

M = 10000 #number of divisions of our spatial grid
rmax = 10  #maximum value considered for r (leftmost value -> infinity)
r = np.linspace(0, rmax, M) #defining our line, i.e. that's the domain we consider for solving the ODE
sing = np.array([[0, 0],
              [0, -1]]) #this matrix brings in the singular term


guess = np.empty((2,M)) #here we insert our guess to the real solution
guess[0] = np.sqrt(1.8625)*np.sqrt(2*pi)*norm.pdf(r) 
guess[1] = 0
y1 = solve_bvp(func, bc, r, guess, S=sing, verbose=2) #here we solve the ODE of interest

R = lambda r: y1.sol(r)[0] #this is the numerical solution of the ODE
normal = lambda r: 1.86225*np.sqrt(2*pi)*norm.pdf(r)

expR = lambda r,sig: np.sqrt((1.86225*2)/(sig**2))*np.exp(-r**2/(2*sig**2))

r_plot = np.linspace(0, rmax, M)
R2_plot = R(r_plot)
R2 = np.abs(R(r_plot))**2
R4 = np.abs(R(r_plot))**4
grad = np.gradient(R(r_plot),r_plot)

I = simps(R2*r_plot*2*np.pi, r_plot)

gauss = normal(r_plot)
I2 = simps(gauss*r_plot,r_plot)

print(I)
# print(I2)

gamma = simps(2*np.pi*r_plot*grad**2, r_plot)
print(gamma)

alpha2 = simps(R2*2*np.pi*r_plot**3, r_plot)
print(alpha2)

beta = simps(R4*2*np.pi*r_plot, r_plot)
print(beta)

'''width of Townes solution'''
width = np.sqrt(simps(R2*2*np.pi*r_plot**2, r_plot)/I)
print(width)

print(R2_plot.max())
np.savetxt('townesprofile.csv', [p for p in zip(r_plot, R2_plot)], delimiter=',', fmt='%s')
np.savetxt('townesprofile_normalized.csv', [p for p in zip(r_plot/r_plot.max(), R2_plot/R2_plot.max())], delimiter=',', fmt='%s')
np.savetxt('townes_density.csv', [p for p in zip(r_plot, R2)], delimiter=',', fmt='%s')

'''plot'''
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(r_plot, R2_plot,"-k", label='Numerical')
ax.set_xlim(0, right=r_plot.max())
plt.ylabel(r'$R$',fontweight='bold',rotation=360)
plt.xlabel(r'$r$',fontweight='bold')
ax.legend()
plt.show()


fig = plt.figure()
ax = fig.add_subplot()
ax.plot(r_plot, R2,"-k", label='Numerical')
ax.set_xlim(0, right=r_plot.max())
plt.show()

