"""Stable thin-shell ratio via log-gamma; sup over p in [1,2], n to 1e6."""
import math
from math import lgamma, exp
def lgE2(n,p): return math.log(n/(n+2))+lgamma(3/p)+lgamma(n/p)-lgamma(1/p)-lgamma(n/p+2/p)
def lgE4(n,p): return math.log(n/(n+4))+lgamma(5/p)+lgamma(n/p)-lgamma(1/p)-lgamma(n/p+4/p)
def lgE22(n,p): return math.log(n/(n+4))+2*lgamma(3/p)-2*lgamma(1/p)+lgamma(n/p)-lgamma(n/p+4/p)
def s2n(n,p):
    s2=exp(lgE2(n,p)); e4=exp(lgE4(n,p)); e22=exp(lgE22(n,p))
    v1=e4-s2**2; c=e22-s2**2
    return (n*v1+n*(n-1)*c)/(n*s2**2)
print(f"{'n':>8} {'p=1':>8} {'p=1.25':>8} {'p=1.5':>8} {'p=1.75':>8} {'p=2':>8} {'p=3':>8} {'p=5':>8} {'p=10':>8}")
mx=0
for n in [2,5,10,20,50,100,500,2000,10000,100000,1000000]:
    row=[n]
    for p in [1.0,1.25,1.5,1.75,2.0,3.0,5.0,10.0]:
        v=s2n(n,p); row.append(v)
    print((" ".join([f"{row[0]:>8}"]+[f"{v:>8.4f}" for v in row[1:]])))
    for v in row[1:6]: mx=max(mx,v)
print("sup over p in [1,2] grid:",mx)
# fine p-grid at large n
print("fine p scan n=1000:")
for k in range(21):
    p=1+0.05*k
    print(f" p={p:.2f} s={s2n(1000,p):.4f}")
