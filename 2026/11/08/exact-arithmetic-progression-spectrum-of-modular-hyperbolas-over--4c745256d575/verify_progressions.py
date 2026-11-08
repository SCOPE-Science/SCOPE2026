from math import gcd, lcm
from collections import Counter

def calc(n):
    factors=[]; v=n; p=2
    while p*p<=v:
        if v%p==0:
            k=0
            while v%p==0:v//=p;k+=1
            factors.append((p,k))
        p+=1
    if v>1:factors.append((v,1))
    m=1
    for p,k in factors:
        t=(k+1)//2 if p%2 else max(1,k//2)
        # for p2: ceil((k-1)/2)=k//2
        m*=p**t
    return m,n//m

cnt=0
for n in range(2,161):
    units=[x for x in range(n) if gcd(x,n)==1]
    inv={x:pow(x,-1,n) for x in units}
    observed=Counter()
    for x in units:
        for h in range(n):
            if (x+h)%n not in inv or (x+2*h)%n not in inv:continue
            if (inv[x]-2*inv[(x+h)%n]+inv[(x+2*h)%n])%n==0:
                observed[n//gcd(n,h)]+=1
                assert all((x+j*h)%n in inv for j in range(n//gcd(n,h)))
                assert all((inv[(x+j*h)%n]-inv[x]-j*(inv[(x+h)%n]-inv[x]))%n==0 for j in range(n//gcd(n,h)))
    m,q=calc(n)
    want=Counter({d:len(units)*sum(1 for j in range(q) if q//gcd(q,j)==d) for d in range(1,q+1) if q%d==0})
    assert observed==want,(n,m,q,observed,want)
    cnt+=len(units)*n
print('VERIFY_OK moduli=2..160 checked_start_steps=',cnt, 'including 2-adic exceptions; all 3APs extend to full cycles; exact length distribution')
for n in (2,4,8,9,12,16,18,25,27,30,36,72,125):
 print(n,calc(n))
