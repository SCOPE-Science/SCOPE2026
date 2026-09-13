import numpy as np
B = np.array([[2.,1.],[1.,1.]])
Bi = np.array([[1.,-1.],[-1.,2.]])
eu = np.array([-0.8506508083520399, -0.5257311121191336])
es = np.array([0.5257311121191336, -0.8506508083520399])

def rvec(Y):
    return 1 + 0.04*np.sin(2*np.pi*Y[...,0]) + 0.03*np.cos(2*np.pi*Y[...,1])

def Delta_grid(X, a, b, N=14):
    """X: (G,2). returns (G,) Delta values."""
    Xu = (X + a*eu) % 1.0; Xs = (X + b*es) % 1.0; Xus = (X + a*eu + b*es) % 1.0
    Xk, Xuk, Xsk, Xusk = X.copy(), Xu.copy(), Xs.copy(), Xus.copy()
    tot = rvec(Xuk)-rvec(Xusk)-rvec(Xk)+rvec(Xsk)
    for k in range(1, N+1):
        Xk=(Xk@B.T)%1.0; Xuk=(Xuk@B.T)%1.0; Xsk=(Xsk@B.T)%1.0; Xusk=(Xusk@B.T)%1.0
        tot += rvec(Xuk)-rvec(Xusk)-rvec(Xk)+rvec(Xsk)
    Xk, Xuk, Xsk, Xusk = X.copy(), Xu.copy(), Xs.copy(), Xus.copy()
    for j in range(1, N+1):
        Xk=(Xk@Bi.T)%1.0; Xuk=(Xuk@Bi.T)%1.0; Xsk=(Xsk@Bi.T)%1.0; Xusk=(Xusk@Bi.T)%1.0
        tot += rvec(Xk)-rvec(Xuk)+rvec(Xusk)-rvec(Xsk)
    return tot
