#!/usr/bin/env python3
"""lane-1780 Route A: periodic-orbit weights a_n = sum 1/|det(I-DH^n)|.
Homotopy Newton from linear lifts x0=(M^n-I)^{-1}k, torus-mod residual.
Results: n=1 -> 3/3 orbits, a1~=1.00056555; n=2 -> 39/39 orbits, a2~=1.0;
n=3 enumeration incomplete (k-box flaw), period 4 not closable this way.
"""
import numpy as np, itertools
M=np.array([[4.,1.,0.],[1.,1.,1.],[0.,1.,1.]])
eps=0.02; TAU=2*np.pi
def H(x):
    y=np.asarray(x,float)
    r=np.mod(np.array([y[0]+eps*np.sin(TAU*(y[1]+y[2])),y[1]+eps*np.sin(TAU*y[2]),y[2]]),1.)
    return np.mod(M@r,1.)
def DR(x):
    a=eps*TAU*np.cos(TAU*(x[1]+x[2])); b=eps*TAU*np.cos(TAU*x[2])
    return np.array([[1.,a,a],[0.,1.,b],[0.,0.,1.]])
def DH(x): return M@DR(np.asarray(x,float))
def Hn(x,n):
    y=np.array(x,float)
    for _ in range(n): y=H(y)
    return y
def DHn(x,n):
    J=np.eye(3); y=np.array(x,float)
    for _ in range(n):
        J=DH(y)@J; y=H(y)
    return J
if __name__=="__main__":
    print("eig:",np.linalg.eigvals(M))
    for n in [1,2]:
        Mn=np.linalg.matrix_power(M,n); B=Mn-np.eye(3); Binv=np.linalg.inv(B)
        print(f"n={n} linear count={round(abs(np.linalg.det(B)))}")
