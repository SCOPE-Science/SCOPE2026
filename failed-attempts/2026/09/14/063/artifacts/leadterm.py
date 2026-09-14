import sys; sys.path.insert(0,'output/artifacts')
from qscat import E_series, mul, sinv, t
import sympy as sp
# Debug [2],[2] n=3: print raw qv at (1,1) before conversion
n=3; N=3
F1=E_series({1:1,-1:1},(1,0),N); F2=E_series({1:1,-1:1},(0,1),N)
F1i=sinv(F1,N,n); F2i=sinv(F2,N,n)
P=dict(F1i); P=mul(dict(F2i),P,N,n); P=mul(dict(F1),P,N,n); P=mul(dict(F2),P,N,n)
for k in sorted(P):
    if sum(k)==2:
        qv=sp.simplify(-(t-t**(-1))*P.get(k,0))
        print(k, "P=", sp.simplify(P.get(k,0)), "qv=", sp.together(qv))
