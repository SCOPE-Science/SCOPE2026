"""Check commuting tuples of square-zero derivations on truncated local algebras.
Uses direct coefficient differentiation and finite-field arithmetic, independently
of the component proof. Standalone, Python 3, no external packages.
"""
from itertools import product

def mul(a,b,q):
    if q==2: return a&b
    if q==4:
        v=0
        for i in range(2):
            if (b>>i)&1: v ^= a<<i
        if v&8:v ^= 0b1100
        if v&4:v ^= 0b0111
        return v
    raise ValueError(q)
def deriv_squarezero(f,q):
    n=len(f)
    if n%2 and f[0]: return False
    fp=tuple(f[i] if i%2 else 0 for i in range(1,n))+(0,)
    for t in range(n):
        x=0
        for i in range(t+1): x ^= mul(f[i],fp[t-i],q)
        if x:return False
    return True

def bracket_zero(f,g,q):
    n=len(f)
    fp=tuple(f[i] if i%2 else 0 for i in range(1,n))+(0,)
    gp=tuple(g[i] if i%2 else 0 for i in range(1,n))+(0,)
    for t in range(n):
        x=0
        for i in range(t+1):
            x ^= mul(f[i],gp[t-i],q)^mul(g[i],fp[t-i],q)
        if x:return False
    return True

def expected(h,k,q):
    return q**(h*k)+(h//2)*(q**(h*k)-q**(k*(h-1)))

def run(q,n,k):
    h=n//2
    good=[f for f in product(range(q),repeat=n) if deriv_squarezero(f,q)]
    if k==2:
        actual=sum(bracket_zero(f,g,q) for f in good for g in good)
    else:
        actual=0
        for row in product(good,repeat=k):
            if all(bracket_zero(row[i],row[j],q) for i in range(k) for j in range(i)):
                actual+=1
    want=expected(h,k,q)
    assert actual==want,(q,n,k,actual,want)
    print('PASS',q,n,k, 'squarezero',len(good),'commuting tuples',actual)

if __name__=='__main__':
    for q,n,k in [(2,2,2),(2,3,2),(2,4,2),(2,5,2),(2,6,2),(2,7,2),(2,8,2),(2,4,3),(2,5,3),(2,6,3),(2,4,4),(4,2,2),(4,3,2),(4,4,2),(4,5,2),(4,4,3)]:
        run(q,n,k)
    print('ALL_RESTRICTED_COMMUTING_TUPLES_PASS')
