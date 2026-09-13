"""Script L: sharper certified unstable expansion. Bound only the weak direction:
for y=(w,u), |y'| >= |w'|_row and combine row-wise lower bound with cone ratio.
Also certify det bounds: |det Df|_u-plane| etc. Simplest rigorous route:
certify min_w |row_w(M) . (s,y)| over cone via entrywise ell1 bounds, and use
det(M)=1 to convert: since stable contracts by <=0.221, product of the two
unstable multipliers >= 1/0.221 = 4.52, so the weak multiplier alone could still
be < 1 in principle -- that is the genuine mostly-expanding question.
Report: (i) cone invariance (done, kappa=0.3), (ii) strong expansion of some
2-frame (area), (iii) honest statement that uniform per-vector expansion needs
the refined norm below. Then directly bound min |w'| on cone boundary."""
import math
import numpy as np
A=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
w,P=np.linalg.eigh(A)
alp,bet=2*math.pi*0.03,2*math.pi*0.02
C=P.T@(A@np.eye(3))@P
E2=P.T@(A@np.array([[0.,1.,0.],[0.,0.,0.],[0.,0.,0.]]))@P*alp
E3=P.T@(A@np.array([[0.,0.,0.],[0.,0.,1.],[0.,0.,0.]]))@P*bet
# row w = index 1: center row and radii
for i,label in [(0,'s'),(1,'w'),(2,'u')]:
    print(label,"center",C[i].round(4),"rad", (np.abs(E2[i])+np.abs(E3[i])).round(4))
# lower bound min over cone |s|<=kap|y|,|y|=1 of |w'|: w'=Mi0 s+Mi1 w+Mi2 u
# certificate: min >= min_{|y|=1}|ci.y| - kap*|Mi0|, first term = norm of row restricted... bound below by (|ci1|+|ci2| stuff)? Use: min over unit y of |l.y| = 0 (l.y can vanish!) unless direction constrained -- so instead bound full |y'| with B-sigma but sigma bound was loose (1.007). Improve sigma via exact interval: B(c2,c3) affine; evaluate sigma_min on 4 corners + Lipschitz padding.
from itertools import product
def Bmat(c2,c3): return (C+c2*E2+c3*E3)[1:,1:]
corners=[Bmat(c2,c3) for c2 in (-1,1) for c3 in (-1,1)]
print("corner sigmin:",[round(float(min(np.linalg.svd(B,compute_uv=False))),4) for B in corners])
# Lipschitz: B linear in (c2,c3): ||B(x)-B(corner)||<=||E2||*|dc2|+||E3||*|dc3|; grid 8x8 + pad
n=8
smin=1e9
nE2=np.linalg.norm(E2[1:,1:],2); nE3=np.linalg.norm(E3[1:,1:],2)
for i in range(n+1):
    for j in range(n+1):
        c2,c3=-1+2*i/n,-1+2*j/n
        s=min(np.linalg.svd(Bmat(c2,c3),compute_uv=False))
        smin=min(smin,s)
pad=(nE2+nE3)/n
print(f"grid {n}x8+1 sigmin>={smin:.4f} minus pad {pad:.4f} => certified sigmin(B)>={smin-pad-1e-9:.4f}")
