from collections import Counter
from fractions import Fraction

def predicted(n):
    N=1 << (n.bit_length()-1)
    r=n-N
    out=Counter({1:1})
    d=1
    while d<=N:
        out[d]+=d
        d*=2
    out[2*N]+=2*r
    return +out

def measured(n):
    dmax=1 << (n.bit_length()+1)
    vals={}
    d=1
    while d <= dmax:
        for phase in range(d):
            w=tuple(int((i-phase)%d==0) for i in range(n))
            vals[w]=min(vals.get(w,d),d)
        d*=2
    vals[(0,)*n]=1
    return Counter(vals.values())

for n in range(1,111):
    exp=predicted(n)
    got=measured(n)
    assert exp==got,(n,exp,got)
    assert sum(exp.values())==2*n
    N=1 << (n.bit_length()-1);r=n-N
    assert sum(d*c for d,c in exp.items())== (4*N*N+2)//3+4*N*r
    assert sum(d*d*c for d,c in exp.items())==(8*N*N*N+6)//7+8*N*N*r
print('VERIFY_OK exact_histogram_1_to_110=110 exact_moment_identities=220')
