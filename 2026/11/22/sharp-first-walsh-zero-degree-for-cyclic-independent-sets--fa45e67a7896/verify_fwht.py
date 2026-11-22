"""Independent enumeration + integer Walsh-Hadamard proof checks for cyclic independent sets.
Python 3 standard library; no external inputs.  Finite tests, not the all-n theorem.
"""
from math import comb

def check(n):
    size=1<<n
    a=[0]*size
    full=size-1
    for s in range(size):
        shift=((s<<1)|(s>>(n-1))) & full
        if not (s&shift): a[s]=1
    # Walsh-Hadamard transform, independent of transfer trace formula.
    step=1
    while step<size:
        for base in range(0,size,step*2):
            for j in range(step):
                x,y=a[base+j],a[base+step+j]
                a[base+j]=x+y;a[base+step+j]=x-y
        step*=2
    z=[s for s,v in enumerate(a) if v==0]
    if n%3:
        assert not z,(n,len(z))
    else:
        k=n//3
        assert z and min(s.bit_count() for s in z)==k+1
        assert all(s.bit_count()>=k+1 for s in z)
    return len(z),min((s.bit_count() for s in z),default=None)
if __name__=='__main__':
    for n in range(3,19):
        print('FWHT',n,*check(n))
