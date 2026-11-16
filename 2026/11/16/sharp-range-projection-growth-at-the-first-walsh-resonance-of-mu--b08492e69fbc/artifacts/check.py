from fractions import Fraction
from itertools import product
from math import comb

def fwht(a):
    a=list(a);n=len(a);stride=1
    while stride<n:
        for i in range(0,n,2*stride):
            for j in range(i,i+stride):
                x,y=a[j],a[j+stride]
                a[j],a[j+stride]=x+y,x-y
        stride*=2
    return a

def run(m):
    q=1<<m;r=q+1;dim=m*r;N=1<<dim
    if dim<=10:
        a=[0]*N
        for x in range(N):
            blocks=[(x>>(m*i))&(q-1) for i in range(r)]
            a[x]=int(sum(v!=0 for v in blocks)<=1)
        w=fwht(a)
        assert all(w[i]==q*(sum(((i>>(m*j))&(q-1))==0 for j in range(r))-1) for i in range(N))
        support=[int(u!=0) for u in w]
        h=fwht(support)
        direct=Fraction(sum(abs(v) for v in h),N)
        zeros=sum(v==0 for v in w)
        assert zeros==r*(q-1)**(r-1)
        formula=Fraction(1)+Fraction(r*(q-1)**(r-1)*((q-2)*2**(r-1)+2),q**r)
        assert direct==formula,(direct,formula)
        print(f'm={m},q={q},r={r},N={N},zeros={zeros},rank={N-zeros},norm={direct},float={float(direct):.10f}')
    else:
        formula=Fraction(1)+Fraction(r*(q-1)**(r-1)*((q-2)*2**(r-1)+2),q**r)
        print(f'm={m},q={q},r={r},N={q**r},zeros={r*(q-1)**(r-1)},norm={formula}')
for m in (1,2,3):run(m)
