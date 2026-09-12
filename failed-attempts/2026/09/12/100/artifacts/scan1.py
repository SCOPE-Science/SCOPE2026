"""Scan for librational periodic orbits of planar double pendulum at H0=-10."""
import numpy as np

g=9.81; m1=m2=1.0; L1=L2=1.0

def f(state):
    th1,th2,w1,w2 = state
    D = 3.0 - np.cos(2*(th1-th2))
    d = th1-th2
    a1 = (-g*3*np.sin(th1) - g*np.sin(th1-2*th2) - 2*np.sin(d)*(w2*w2 + w1*w1*np.cos(d)))/D
    a2 = (2*np.sin(d)*(2*w1*w1 + 2*g*np.cos(th1) + w2*w2*np.cos(d)))/D
    return np.array([w1,w2,a1,a2])

def energy(state):
    th1,th2,w1,w2 = state
    T = w1*w1 + 0.5*w2*w2 + w1*w2*np.cos(th1-th2)
    V = -19.62*np.cos(th1) - 9.81*np.cos(th2)
    return T+V

def rk4_step(s, dt):
    k1=f(s); k2=f(s+0.5*dt*k1); k3=f(s+0.5*dt*k2); k4=f(s+dt*k3)
    return s+dt/6*(k1+2*k2+2*k3+k4)

def integrate(s0, T, dt=0.0005):
    s=np.array(s0,float); n=int(T/dt)
    traj=np.zeros((n+1,4)); traj[0]=s
    for i in range(n):
        s=rk4_step(s,dt); traj[i+1]=s
    return traj

# check energy at bottom with various velocities
for (u,v) in [(4.0,1.0),(3.0,2.0),(2.0,3.0),(4.5,0.5),(1.0,4.0),(3.5,-1.0),(2.5,2.5)]:
    s=np.array([0.0,0.0,u,v])
    print(u,v,energy(s))

# quick long integration to see chaos/libration at H=-10: start (0,0,3.5,1.0)-> E?
s0=np.array([0.0,0.0,3.5,1.0]); print("E0",energy(s0))
tr=integrate(s0,20,dt=0.001)
print("Emax dev",np.max([abs(energy(s)-energy(s0)) for s in tr[::1000]]))
print("th1 range",tr[:,0].min(),tr[:,0].max(),"th2",tr[:,1].min(),tr[:,1].max())
# detect winding: unwrap?
print("final",tr[-1])
