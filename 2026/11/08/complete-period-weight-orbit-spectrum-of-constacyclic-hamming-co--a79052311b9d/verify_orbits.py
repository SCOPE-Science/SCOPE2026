"""Reproducible small-field check of fixed-period and Hamming-weight orbit counts.

Runs with Python 3 standard library. Finite fields are built from specified
irreducible polynomials over their prime subfields. All relevant Hamming
codewords are exhaustively enumerated for each listed parameter pair.
"""
from collections import Counter
from itertools import product
from math import comb, gcd

CASES = [
    # q, r, p, polynomial in ascending coefficient order over F_p
    (2,2,2,[1,1,1]),
    (2,3,2,[1,1,0,1]),
    (2,4,2,[1,1,0,0,1]),
    (3,2,3,[2,1,1]),
    (3,3,3,[1,2,0,1]),
    (4,2,2,[1,1,0,0,1]),
    (5,2,5,[2,1,1]),
]

def divisors(n):
    return [d for d in range(1,n+1) if n % d == 0]

def mobius(n):
    x=n; cnt=0; p=2
    while p*p<=x:
        if x%p==0:
            x//=p;cnt+=1
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    return (-1)**(cnt+(x>1))

def finite_field(p, polynomial):
    k=len(polynomial)-1; size=p**k
    def vector(a):
        return [(a//(p**i))%p for i in range(k)]
    def encode(c):
        return sum((z%p)*(p**i) for i,z in enumerate(c))
    def add(a,b):
        x=vector(a);y=vector(b)
        return encode([(x[i]+y[i])%p for i in range(k)])
    def neg(a):
        return encode([(-i)%p for i in vector(a)])
    def mul(a,b):
        x=vector(a);y=vector(b);v=[0]*(2*k-1)
        for i,xi in enumerate(x):
            for j,yj in enumerate(y):v[i+j]=(v[i+j]+xi*yj)%p
        for i in range(2*k-2,k-1,-1):
            c=v[i]
            for j in range(k): v[i-k+j]=(v[i-k+j]-c*polynomial[j])%p
        return encode(v[:k])
    def power(a,t):
        z=1
        while t:
            if t&1:z=mul(z,a)
            a=mul(a,a);t//=2
        return z
    for a in range(1,size):
        if len({power(a,k) for k in range(size-1)})==size-1:
            primitive=a;break
    else:raise AssertionError('extension field polynomial not primitive/irreducible')
    return size,primitive,add,neg,mul,power

def poly_add(a,b,scalar=1):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=scalar*v
    return z

def poly_power_linear(q,j):
    return [comb(j,k)*(q-1)**k for k in range(j+1)]

def weight_polynomials(q,r):
    n=(q**r-1)//(q-1); M=q**r-1
    # MacWilliams transform of constant-weight q-ary simplex dual.
    first=poly_power_linear(q,n)
    second=[]
    # (1-z)^{q^{r-1}}(1+(q-1)z)^{n-q^{r-1}}
    for a in range(q**(r-1)+1):
        for b in range(n-q**(r-1)+1):
            k=a+b
            while len(second)<=k:second.append(0)
            second[k]+=comb(q**(r-1),a)*(-1)**a*comb(n-q**(r-1),b)*(q-1)**b
    numer=poly_add(first,second,M)
    assert all(k%(q**r)==0 for k in numer)
    total=[i//(q**r) for i in numer]
    W={}
    for d in divisors(M):
        if d==M:W[d]=total
        else:
            g=gcd(n,d)
            if d//g%(q-1)==0:
                W[d]=[0]*(n+1)
                for k in range(g+1):W[d][k*(n//g)]=comb(g,k)*(q-1)**k
            else:W[d]=[1]
    count={}
    for d in divisors(M):
        numerator=[0]*(n+1)
        for e in divisors(d):
            mu=mobius(d//e)
            numerator=poly_add(numerator,W[e],mu)
        assert all(x%d==0 for x in numerator),(q,r,d,numerator)
        count[d]=[v//d for v in numerator]
        assert min(count[d])>=0
    assert sum(sum(row) for row in count.values())>=1
    return W,count

def run_case(q,r,p,poly):
    size,alpha,add,neg,mul,power=finite_field(p,poly)
    assert size==q**r
    n=(q**r-1)//(q-1);M=q**r-1
    lam=power(alpha,n)
    if q==p:alphabet=list(range(q))
    else:alphabet=[0]+[power(lam,j) for j in range(q-1)]
    assert len(set(alphabet))==q
    assert {mul(a,b) for a in alphabet for b in alphabet}<=set(alphabet)
    powers=[power(alpha,j) for j in range(n)]
    # First r columns give an F_q-basis of F_{q^r}; solve check equations.
    inverse={}
    for choices in product(alphabet,repeat=r):
        s=0
        for c,v in zip(choices,powers[:r]):s=add(s,mul(c,v))
        assert s not in inverse
        inverse[s]=choices
    assert len(inverse)==size
    code=set()
    for choices in product(alphabet,repeat=n-r):
        s=0
        for c,v in zip(choices,powers[r:]):s=add(s,mul(c,v))
        code.add(inverse[neg(s)]+choices)
    assert len(code)==q**(n-r)
    def shift(c):return (mul(lam,c[-1]),)+c[:-1]
    distribution=Counter(); seen=set()
    for c in code:
        if c in seen: continue
        v=c; orbit=[]
        while v not in orbit:
            assert v in code
            orbit.append(v); v=shift(v)
        assert v==c
        assert len(orbit) in divisors(M)
        distribution[len(orbit),sum(x!=0 for x in c)]+=1
        seen.update(orbit)
    W,expected=weight_polynomials(q,r)
    model={(d,w):v for d,row in expected.items() for w,v in enumerate(row) if v}
    assert distribution==model,(q,r,distribution,model)
    for d in divisors(M):
        actual=Counter(sum(x!=0 for x in c) for c in code if all(shift_n(c,shift,d)==c for _ in [0]))
        predicted={w:v for w,v in enumerate(W[d]) if v}
        assert dict(actual)==predicted,(q,r,d,actual,predicted)
    print('OK q=%d r=%d length=%d codewords=%d orbits=%d nonzero_periods=%s' %
          (q,r,n,len(code),len(seen) and sum(distribution.values()),
           sorted((d,sum(v for (dd,w),v in distribution.items() if dd==d)) for d in divisors(M) if any(dd==d for dd,w in distribution))))

def shift_n(c,shift,d):
    v=c
    for _ in range(d):v=shift(v)
    return v

if __name__=='__main__':
    for x in CASES:run_case(*x)
    print('ALL EXACT ORBIT/PERIOD/WEIGHT COMPARISONS PASSED')
