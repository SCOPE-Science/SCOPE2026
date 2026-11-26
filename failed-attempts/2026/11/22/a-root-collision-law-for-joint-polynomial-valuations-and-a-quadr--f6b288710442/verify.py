"""Direct integer-count tests for the joint simple-root valuation law.
Run: python verify.py. Requires only Python 3 standard library.
The algebraic proof, not these finite computations, supports all prime powers.
"""
from fractions import Fraction
from itertools import product


def valuation_truncated(a,p,k):
    if a == 0:
        return k
    j=0
    while j<k and a%p==0:
        a//=p
        j+=1
    return j


def quadratic(a,b):
    return lambda n:(n-a)*(n-b)


def lift_simple_roots(f,p,k):
    roots=[a for a in range(p) if f(a)%p==0]
    assert all(sum(1 for h in range(p) if f(h)%p==0) <=2 for _ in [0])
    levels=[roots]
    modulus=p
    for e in range(2,k+1):
        roots=[r+j*modulus for r in roots for j in range(p) if f(r+j*modulus)%(modulus*p)==0]
        modulus*=p
        levels.append(roots)
    return levels


def exercise(p, f, g, K, tag):
    froot=lift_simple_roots(f,p,K)
    groot=lift_simple_roots(g,p,K)
    af=len(froot[0]); bg=len(groot[0]); assert af<=2 and bg<=2
    # All lifted root sets stay of constant size because each root is simple.
    assert all(len(a)==af and len(b)==bg for a,b in zip(froot,groot))
    checks=0
    for k in range(1,K+1):
        mod=p**k
        values=[(valuation_truncated(f(n),p,k),valuation_truncated(g(n),p,k)) for n in range(mod)]
        Nm={m:len(set(froot[m-1])&set(groot[m-1])) for m in range(1,k+1)}
        for t in range(1,k+1):
            ca=sum(x>=t for x,y in values)
            cb=sum(y>=t for x,y in values)
            assert ca==af*p**(k-t),(tag,p,k,t,'marginal f',ca)
            assert cb==bg*p**(k-t),(tag,p,k,t,'marginal g',cb)
            checks+=2
            for s in range(1,k+1):
                obs=sum(x>=t and y>=s for x,y in values)
                expected=Nm[min(t,s)]*p**(k-max(t,s))
                assert obs==expected,(tag,p,k,t,s,obs,expected)
                checks+=1
        # Exact finite precision covariance, from the tail sums.
        avgx=Fraction(sum(x for x,y in values),mod)
        avgy=Fraction(sum(y for x,y in values),mod)
        cross=Fraction(sum(x*y for x,y in values),mod)
        expected_x=Fraction(af*(1-Fraction(1,p**k)),p-1)
        expected_y=Fraction(bg*(1-Fraction(1,p**k)),p-1)
        predicted_cross=sum((Fraction(1,p**m)*Nm[m]*(1+2*sum(Fraction(1,p**h) for h in range(1,k-m+1)))) for m in range(1,k+1))
        assert avgx==expected_x and avgy==expected_y and cross==predicted_cross,(tag,p,k)
        checks+=3
    return checks, [(m,len(set(froot[m-1])&set(groot[m-1]))) for m in range(1,K+1)]


def main():
    cases=[
       (3,quadratic(0,1),quadratic(0,2),6,'one exact shared root'),
       (3,quadratic(0,1),quadratic(3,2),6,'one depth-one shared residue'),
       (3,quadratic(0,1),quadratic(0,1),6,'two exact shared roots'),
       (5,quadratic(0,1),quadratic(5,2),5,'one depth-one shared residue'),
       (5,quadratic(0,1),quadratic(2,3),5,'no shared residue'),
       (5,quadratic(0,1),quadratic(5,6),5,'two depth-one shared residues'),
       (7,lambda n:n*n-2,lambda n:n*n-44,4,'both irreducible over Q, two overlaps'),
       (5,lambda n:n*n-n+5,lambda n:n*n-2*n+5,5,'both irreducible over Q, one overlap'),
       (3,lambda n:n*n-n+3,lambda n:n*n+n+3,6,'both irreducible over Q, one overlap'),
       (5,quadratic(0,1),quadratic(25,2),5,'one depth-two shared residue'),
       (7,lambda n:n*n-2,lambda n:n*n+1,4,'one polynomial no roots'),
    ]
    checked=0
    for p,f,g,k,tag in cases:
        n,cm=exercise(p,f,g,k,tag)
        checked+=n
        print(f'p={p}, depth={k}, {tag}: {n} exact identities; root overlap={cm}')
    print(f'PASS: {checked} exact marginal, tail and cross-moment tests')

if __name__=='__main__':main()
