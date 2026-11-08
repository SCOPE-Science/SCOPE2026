from fractions import Fraction as F
from math import floor,ceil

def B4(x):
    x=x%1
    return x**4-2*x**3+x**2-F(1,30)
def closed(b,q):
    x=F(1,q); y=F(b,q)
    return -(B4(F(0))-B4(x)-B4(y)+F(1,2)*B4(F(b+1,q))+F(1,2)*B4(F(b-1,q)))/(6*b*b)
def overlap(b,q,j,k,z):
    l=F(b*j,q)+z; h=F(b*(j+1),q)+z
    nmin=floor(l-F(k+1,q))-1
    nmax=ceil(h-F(k,q))+1
    s=F(0)
    for n in range(nmin,nmax+1):
        lo=max(l,F(k,q)+n); hi=min(h,F(k+1,q)+n)
        if hi>lo:s+=hi-lo
    return s/b

def direct(b,q,j,k):
    breaks={F(0),F(1)}
    for jbase in (F(b*j,q),F(b*(j+1),q)):
        for kbase in (F(k,q),F(k+1,q)):
            for n in range(-2,b+4):
                z=kbase+n-jbase
                if 0<=z<=1:breaks.add(z)
    breaks=sorted(breaks)
    total=F(0)
    for lo,hi in zip(breaks,breaks[1:]):
        a=overlap(b,q,j,k,lo)-F(1,q*q)
        c=overlap(b,q,j,k,hi)-F(1,q*q)
        total+=(hi-lo)*(a*a+a*c+c*c)/3
    return total

if __name__=='__main__':
    for b in range(2,13):
        for q in range(2,11):
            res=closed(b,q)
            assert (res==0)==(b%q==0), (b,q,res)
            for j,k in [(0,0), (q-1,q-1), (0,q-1)]:
                num=direct(b,q,j,k)
                assert num==res, (b,q,j,k,num,res)
    print('PASS exact rational B4/cylinder variance for b=2..12,q=2..10, three cells each')
    for b,q in [(3,2),(2,3),(4,3),(5,3),(2,4),(3,4),(5,4),(6,4),(8,4)]:
        print(b,q,closed(b,q))
