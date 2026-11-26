"""Independent Hamming-cover-radius and Poisson-moment checks for Q_d OR dynamics."""
from math import comb, exp
from itertools import combinations

def radius(mask,d):
    n=1<<d
    if mask==0: return 0
    seeds=[i for i in range(n) if (mask>>i)&1]
    return max(min((v^s).bit_count() for s in seeds) for v in range(n))

def tally(d):
    par=[[i for i in range(1<<d) if i.bit_count()%2==b] for b in (0,1)]
    vals=[]
    for cl in par:
        cc={}
        for bits in range(1<<len(cl)):
            mask=sum(1<<v for j,v in enumerate(cl) if bits>>j&1)
            r=radius(mask,d)
            t=max(0,r-1)
            cc[t]=cc.get(t,0)+1
        vals.append(cc)
    assert vals[0]==vals[1]
    N=1<<(d-1);U=N*((1<<d)-d-1)-N*comb(d,2)//2
    assert vals[0].get(d-1,0)==N
    if d>=3:assert vals[0].get(d-2,0)==U
    return vals[0]

if __name__=='__main__':
    for d in range(2,6):
        c=tally(d)
        print('radius histogram d=%s'%d,c)
    for d in (8,10,12,16,20):
        q=.5;M=2**d
        lam=M*q**d
        fact2=M*(M-1-comb(d,2))*q**(2*d)+M*comb(d,2)*q**(2*d-2)
        print('poisson moments d',d,'lambda',lam,'second_factorial_moment',fact2,'error',abs(fact2-lam*lam))
