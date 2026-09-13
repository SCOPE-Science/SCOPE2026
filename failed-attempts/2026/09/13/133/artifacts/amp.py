import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import eu, es, B, Binv
def Ccoef(m, k, a, b):
    m=np.array(m,float)
    Mk = np.linalg.matrix_power(B,k) if k>=0 else np.linalg.matrix_power(Binv,-k)
    w = Mk.T @ m
    A = float(w @ (a*eu)); Bb = float(w @ (b*es))
    return (np.exp(2j*np.pi*A)-1)*(np.exp(2j*np.pi*Bb)-1)
def Fmode(m, a, b, K=60):
    m=np.array(m,float)
    return sum(Ccoef(m,k,a,b) for k in range(K+1)) - sum(Ccoef(m,-j,a,b) for j in range(1,K+1))
rhat = {(1,0):-0.02j, (-1,0):0.02j, (0,1):0.015, (0,-1):0.015}
def amps(a,b):
    out={}
    for m,rh in rhat.items():
        out[m]=abs(rh*Fmode(m,a,b))
    return out
for (a,b) in [(0.03,0.03),(0.03,-0.03),(-0.03,0.03),(0.015,0.015),(0.015,-0.015),(0.05,0.05),(0.05,-0.05),(0.05,0.02)]:
    d=amps(a,b)
    print((a,b),"A1=",d[(1,0)]+d[(-1,0)],"A2=",d[(0,1)]+d[(0,-1)],"totmin_possible=",abs((d[(1,0)]+d[(-1,0)])-(d[(0,1)]+d[(0,-1)])))
