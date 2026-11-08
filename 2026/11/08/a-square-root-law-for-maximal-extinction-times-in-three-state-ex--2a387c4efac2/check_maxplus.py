#!/usr/bin/env python3
"""Check exact excitation-count/max-neighborhood representation for all initial path words through length eight."""
from itertools import product

def update(a):
    return tuple((2 if v == 1 else 0 if v == 2 else
                  int((i>0 and a[i-1]==1) or (i+1<len(a) and a[i+1]==1)))
                 for i,v in enumerate(a))

def potentials(a):
    h=[0]
    for l,r in zip(a,a[1:]):
        h.append(h[-1]+int(l==0 and r==1)-int(l==1 and r==0))
    return tuple(h)

def max_step(h):
    return tuple(max(h[max(0,i-1):min(len(h),i+2)]) for i in range(len(h)))

count=0
for n in range(1,9):
    for initial in product(range(3),repeat=n):
        a=initial; h=potentials(a)
        for t in range(n+3):
            assert potentials(a)==tuple(v-h[0] for v in h), (n,initial,t,'gradient')
            b=update(a); h2=max_step(h)
            assert tuple(y-x for x,y in zip(h,h2))==tuple(int(u==0 and v==1) for u,v in zip(a,b)), (n,initial,t,'increment')
            a=b;h=h2
        count+=1
    print('n',n,'all',3**n,'checked')
print('MAXPLUS_OK',count)
