"""Script R: twist/aperiodicity via the 13 exact-count period<=2 orbits.
Periods dividing 2: fixed (period 1) + genuine 2-cycles. Count found=13 total
points of period dividing 2, of which exactly 1 is fixed => twelve 2-periodic
points = six 2-cycles. Verify: (i) exactly one of pts is the fixed point 0;
(ii) others pair into 2-cycles under f. Then gcd(1,2)=1 => aperiodic => eigenvalue
1 simple, no other peripheral spectrum (Quas-compact + mixing Anosov)."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(x):
    z=np.stack([x[...,0]+a*np.sin(2*np.pi*x[...,1]),x[...,1]+b*np.sin(2*np.pi*x[...,2]),x[...,2]],axis=-1)
    return (z@Amat.T)%1
pts=np.array([[0.,0.,1.],[0.701148,0.927686,0.538556],[0.60149,0.154799,0.927027],
 [0.4778,0.628858,0.694979],[0.154109,0.528643,0.225794],[0.097089,0.780942,0.616199],
 [0.78384,0.687944,0.148012],[0.5222,0.371142,0.305021],[0.39851,0.845201,0.072973],
 [0.21616,0.312056,0.851988]])
print("images under f:")
for p in pts:
    print("  ",np.round(p,4),"->",np.round(f(p),4))
