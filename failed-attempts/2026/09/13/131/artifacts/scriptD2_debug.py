import numpy as np, math
Amat = np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
Ainv = np.linalg.inv(Amat)
a,b = 0.03,0.02
def S(x):
    return np.stack([x[...,0]+a*np.sin(2*np.pi*x[...,1]), x[...,1]+b*np.sin(2*np.pi*x[...,2]), x[...,2]],axis=-1)%1
def Sinv(y):
    x3=y[...,2]; x2=y[...,1]-b*np.sin(2*np.pi*y[...,2]); x1=y[...,0]-a*np.sin(2*np.pi*x2)
    return np.stack([x1%1,x2%1,x3%1],axis=-1)
def f(x): return (S(x)@Amat.T)%1
def finv(y): return Sinv((y@Ainv.T)%1)
rng=np.random.default_rng(2)
pts=rng.random((2000,3))
print("S roundtrip:",np.abs((Sinv(S(pts))-pts+0.5)%1-0.5).max())
print("A roundtrip:",np.abs((((pts@Amat.T)%1)@Ainv.T)%1-pts+0.5 if False else (((pts@Amat.T)%1)@Ainv.T)%1-pts).max() if False else "skip")
back=finv(f(pts))
print("f roundtrip:",np.abs((back-pts+0.5)%1-0.5).max())
