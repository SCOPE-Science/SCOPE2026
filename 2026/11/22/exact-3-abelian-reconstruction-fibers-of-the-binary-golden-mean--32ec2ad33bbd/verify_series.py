"""Independent parameter-sum, class-size partition, and rational-series checks.

Run: python3 verify_series.py
No third-party packages are used.
"""
from collections import Counter
from math import comb


def coeffs(num, den, N):
    out=[]
    for n in range(N+1):
        x=(num[n] if n < len(num) else 0)
        x-=sum(den[j]*out[n-j] for j in range(1,min(n,len(den)-1)+1))
        assert x % den[0] == 0
        out.append(x//den[0])
    return out


def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

N=130
Cnum=[1,0,-1,1,1,1]
Cden=multiply(multiply([1,-1],[1,-1]),multiply([1,-1],[1,1]))
Snum=[1,1,0,1,2,3,1,-1,-3,-1]
Sden=multiply(multiply([1,-1],[1,-1]),[1,1])
C=coeffs(Cnum,Cden,N)
S=coeffs(Snum,Sden,N)
for n in range(N+1):
    fibers=Counter()
    if n>=0: fibers[1]+=1  # the all-zero word
    for m in range(1,(n+1)//2+2):
        for c in range(m):
            for u in range(3):
                for v in range(3):
                    excess=n-(2*m-1+c+u+v)
                    if excess<0:continue
                    r=c+(u==2)+(v==2)
                    if r==0:
                        if excess:continue
                        size=comb(m-1,c)
                    else:
                        size=comb(m-1,c)*comb(excess+r-1,r-1)
                    fibers[size]+=1
    assert C[n]==sum(fibers.values()), ('profile count',n,C[n],sum(fibers.values()))
    assert S[n]==fibers[1], ('singleton',n,S[n],fibers[1])
    # Number of constrained words, independently via Fibonacci recurrence
    a,b=1,2
    if n==0:F=1
    elif n==1:F=2
    else:
        for j in range(2,n+1):a,b=b,a+b
        F=b
    assert F==sum(k*v for k,v in fibers.items()),('total',n,F,sum(k*v for k,v in fibers.items()))
    if n>=7:
        assert S[n]==(2*n+7 if n%2 else 2*n+6)
    if n>=2:
        k=n//2
        assert C[n]==(3*k*k-k+3 if n%2 else 3*k*k-4*k+4)
    if n in (0,5,10,20,40,80,130):
        print(f'n={n} profile_classes={C[n]} singleton_classes={S[n]} words={F}')
print('VERIFY_SERIES_OK')
