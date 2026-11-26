"""Independent phase-labelled enumeration for synchronous period-three chip-firing."""
from itertools import product
from collections import defaultdict
import math
from verify_kmn3 import prediction

def phase_enum(m,n):
    h=defaultdict(int)
    for col_l in product(range(3),repeat=m):
        if len(set(col_l))<3:continue
        a=[col_l.count(i) for i in range(3)]
        for col_r in product(range(3),repeat=n):
            if len(set(col_r))<3:continue
            b=[col_r.count(i) for i in range(3)]
            choices=[]
            for c in col_l:
                if c==0:lo=n
                elif c==1:lo=b[1]+b[2]
                else:lo=b[2]
                choices.append(range(lo,lo+b[(c-1)%3]))
            for c in col_r:
                if c==0:lo=m
                elif c==1:lo=a[1]+a[2]
                else:lo=a[2]
                choices.append(range(lo,lo+a[(c-1)%3]))
            pp={0:1}
            for r in choices:
                new=defaultdict(int)
                for mass,num in pp.items():
                    for z in r:new[mass+z]+=num
                pp=new
            for mass,num in pp.items():h[mass]+=num
    return dict(h)

def E(m,n):
    if min(m,n)==3:
        t=max(m,n)
        return 6*(3**t-3*2**t+3)
    return 3*m*n*((m-1)*2**(n-1)+(n-1)*2**(m-1)-2*m*n+2)

if __name__=='__main__':
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,4),(5,5)]:
        direct=phase_enum(m,n)
        h,p=prediction(m,n)
        assert direct==p,(m,n, direct,p)
        lo=m*n+m+n-3;hi=2*m*n-m-n
        assert p[lo]==E(m,n)
        assert p[hi]==(3**m-3*2**m+3)*(3**n-3*2**n+3)
        assert set(p)==set(range(lo,hi+1))
        assert sum(h.values())%3==0
        print('independent-phase',m,n,'colorings', (3**m-3*2**m+3)*(3**n-3*2**n+3), 'coeffs',len(p),'first-last',p[lo],p[hi],'total primitive',sum(h.values()), 'PASS')
