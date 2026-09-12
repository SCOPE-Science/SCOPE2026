"""Poincare section scan at H0=-10 region: find recurrent/periodic librational orbits."""
import numpy as np
exec(open('output/artifacts/scan1.py').read().split("# quick")[0])

def energy_of(th1,th2,w1,w2):
    T = w1*w1 + 0.5*w2*w2 + w1*w2*np.cos(th1-th2)
    V = -19.62*np.cos(th1) - 9.81*np.cos(th2)
    return T+V

def w2_from_energy(th1,th2,w1,H0):
    V = -19.62*np.cos(th1) - 9.81*np.cos(th2)
    c=np.cos(th1-th2)
    # 0.5 w2^2 + w1 c w2 + (w1^2 + V - H0)=0
    a=0.5; b=w1*c; cc=w1*w1+V-H0
    disc=b*b-4*a*cc
    if disc<0: return None
    return (-b+np.sqrt(disc))/(2*a), (-b-np.sqrt(disc))/(2*a)

H0=-10.0
# section th2=0? Let's integrate from grid and record section th1=0 crossings
def section_map(s0, maxT=30, dt=0.0005):
    s=np.array(s0,float); prev=s.copy(); out=[]
    n=int(maxT/dt)
    for i in range(n):
        s=rk4_step(s,dt)
        if prev[0]<0 and s[0]>=0 and s[2]>0:  # th1 crossing up
            a=-prev[0]/(s[0]-prev[0]); sc=prev+a*(s-prev)
            out.append(sc.copy())
        prev=s.copy()
        if len(out)>40: break
    return np.array(out)

starts=[]
for w1 in [3.0,3.5,4.0,4.5]:
    sols=w2_from_energy(0.0,0.3,w1,H0)
    print("w1",w1,"sols",sols, "Echk", [energy_of(0,0.3,w1,w) for w in sols] if sols else None)
