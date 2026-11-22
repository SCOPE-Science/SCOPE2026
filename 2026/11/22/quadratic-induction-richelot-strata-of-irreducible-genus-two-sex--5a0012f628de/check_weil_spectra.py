from collections import Counter
from itertools import product
from check_richelot import is_irred,involutions
from check_trace import type_of

def counts(p):
    d=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    q=p*p
    def cv(v):return (v%p,v//p)
    def encode(a,b):return a%p+p*(b%p)
    mul=[[0]*q for _ in range(q)]
    for u in range(q):
        a,b=cv(u)
        for v in range(q):
            c,e=cv(v);mul[u][v]=encode(a*c+d*b*e,a*e+b*c)
    def power(x,n):
        z=1
        while n:
            if n&1:z=mul[z][x]
            x=mul[x][x];n//=2
        return z
    chi=[0]+[1 if power(x,(q-1)//2)==1 else -1 for x in range(1,q)]
    invs=involutions(p);h=Counter();examples={}
    for coeff in product(range(p),repeat=6):
        f=list(coeff)+[1]
        if not is_irred(f,p) or type_of(f,p,invs) is not False:continue
        s=0
        for x in range(q):
            r=0
            for c in f[::-1]:
                v=mul[r][x];a,b=cv(v);r=encode(a+c,b)
            s+=chi[r]
        n2=q+2+s
        assert (n2-(q+1))%2==0
        c2=(n2-q-1)//2
        h[c2]+=1;examples.setdefault(c2,f)
    return sorted(h.items()),examples
for p in (3,5):
    h,ex=counts(p)
    expected = {3:[(-1,12)],5:[(-5,20),(-1,60),(3,60),(7,60)]}[p]
    assert h == expected, (p,h,expected)
    print('p=',p,'hist c2',h,'examples',ex)
