from itertools import product
from fractions import Fraction

def inverse_lyndon(w):
    return all(w>w[i:] for i in range(1,len(w)))

def anti_lyndon(w):
    return all(w>w[i:]+w[:i] for i in range(1,len(w)))

def reps(n,q):
    result={}
    for d in range(1,n+1):
        for u in product(range(q),repeat=d):
            if anti_lyndon(u):
                w=tuple(u[j%d] for j in range(n))
                assert w not in result, (w,result[w],u)
                result[w]=u
    return result

def direct(n,prob):
    q=len(prob); ans=Fraction(0)
    for w in product(range(q),repeat=n):
        if inverse_lyndon(w):
            z=Fraction(1)
            for a in w:z*=prob[a]
            ans+=z
    return ans

def via_roots(n,prob):
    ans=Fraction(0)
    for w in reps(n,len(prob)):
        z=Fraction(1)
        for a in w:z*=prob[a]
        ans+=z
    return ans

for prob, N in [((Fraction(1,2),Fraction(1,2)),12),((Fraction(2,3),Fraction(1,3)),12),((Fraction(9,10),Fraction(1,10)),12),((Fraction(1,2),Fraction(1,3),Fraction(1,6)),8)]:
    for n in range(1,N+1):
        got=direct(n,prob); alt=via_roots(n,prob)
        assert got==alt,(prob,n,got,alt)
        if n in (1,5,N):print('q',len(prob),'prob',str(prob),'n',n,'P',str(got),'nP',float(n*got),'pred',float(1/(1-prob[-1])))
    print('PASS independent word/primitive-root exact rational checks through',N)
