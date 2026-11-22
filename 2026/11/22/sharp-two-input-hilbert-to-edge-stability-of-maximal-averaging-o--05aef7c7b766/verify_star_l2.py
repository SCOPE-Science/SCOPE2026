#!/usr/bin/env python3
"""Standalone finite checks for the sharp star maximal-gradient stability formula.
Stdlib only. Finite tests supplement the exact proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random
from itertools import product


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def rows(m):
    n=m+1
    ident=[]
    for i in range(m):
        a=[F(0)]*n
        a[0]=-1; a[i+1]=1
        ident.append(tuple(a))
    g=tuple([F(-m,n)]+[F(1,n)]*m)
    return ident,g


def lambda_squared(m):
    t=m*(m+2)
    return (t+sqrt(t*t-4*(m+1)))/(2*(m+1))


def mm(x):
    a=[abs(z) for z in x]
    m=len(a)-1; avg=sum(a)/(m+1)
    out=[max(a[0],avg)]
    out += [max(a[i],(a[0]+a[i])/2,avg) for i in range(1,m+1)]
    return out


def energy(x):
    return sum((x[i]-x[0])**2 for i in range(1,len(x)))


def verify_rational_gram():
    certificates=0
    for m in range(2,21):
        I,G=rows(m)
        for a in I:
            assert dot(a,a)==2
            assert dot(a,G)==1
        for i in range(m):
            for j in range(m):
                assert dot(I[i],I[j])==(2 if i==j else 1)
        assert dot(G,G)==F(m,m+1)
        assert abs((m+1)*lambda_squared(m)**2-m*(m+2)*lambda_squared(m)+1) < 1e-8 * (1+ m*(m+2)*lambda_squared(m))
        certificates+=m*m+3*m+2
    return certificates


def verify_entrywise_majorants():
    certificates=0
    for m in range(2,8):
        I,G=rows(m)
        # Every hub-identity branch has no more than m-1 identity rows.
        # Replacing each half-identity row by a G row increases all
        # Gram entries; then replace G rows by I rows until m-1 I remain.
        for code in product((0,1,2),repeat=m):
            if code.count(0)==m: continue
            x=[I[i] if c==0 else tuple(v/F(2) for v in I[i]) if c==1 else G for i,c in enumerate(code)]
            k=code.count(0)
            new=[I[i] if c==0 else G for i,c in enumerate(code)]
            for a in range(m):
                for b in range(m):
                    assert dot(x[a],x[b]) <= dot(new[a],new[b])
                    certificates+=1
            # Turn all but one G row into I: Gram again increases.
            if k < m-1:
                positions=[i for i,c in enumerate(code) if c!=0]
                for i in positions[:-1]: new[i]=I[i]
                prior=[I[j] if c==0 else G for j,c in enumerate(code)]
                for a in range(m):
                    for b in range(m):
                        assert dot(prior[a],prior[b]) <= dot(new[a],new[b])
                        certificates+=1
        # hub-average branches are a row restriction of P=I-J/n,
        # the orthogonal projector; no arbitrary matrix test needed.
    return certificates


def verify_witnesses():
    c=0
    for m in list(range(2,21))+[25,40,70]:
        n=m+1; lam=lambda_squared(m)
        I,G=rows(m)
        b=lam-m
        v=[float(sum((I[i][j] for i in range(m-1)),F(0))+b*G[j]) for j in range(n)]
        g=[2]+[2+1/(4*m)]*(m-1)+[1]
        t=1e-6/(m*m)
        f=[g[j]+t*v[j] for j in range(n)]
        x=mm(g); y=mm(f)
        assert abs(x[0]-g[0])<1e-12
        assert all(abs(x[i]-g[i])<1e-12 for i in range(1,m))
        assert abs(x[-1]-sum(g)/n)<1e-12
        assert all(z>0 for z in f)
        ratio=energy([y[i]-x[i] for i in range(n)])/sum((f[i]-g[i])**2 for i in range(n))
        assert abs(ratio-lam) <= 3e-6*lam, (m,ratio,lam)
        c+=1
    return c


def verify_random_pairs():
    rng=Random(251126)
    c=0
    for m in range(2,17):
        lam=lambda_squared(m)
        for _ in range(400):
            if c%3==0:
                f=[rng.random()*5 for _ in range(m+1)]
                g=[rng.random()*5 for _ in range(m+1)]
            elif c%3==1:
                f=[(rng.random()-.5)*4 for _ in range(m+1)]
                g=[(rng.random()-.5)*4 for _ in range(m+1)]
            else:
                f=[complex(rng.random()*5-2.5,rng.random()*5-2.5) for _ in range(m+1)]
                g=[complex(rng.random()*5-2.5,rng.random()*5-2.5) for _ in range(m+1)]
            y=mm(f);x=mm(g)
            lhs=energy([y[i]-x[i] for i in range(m+1)])
            rhs=lam*sum(abs(f[i]-g[i])**2 for i in range(m+1))
            assert lhs<=rhs+2e-9*(1+rhs), (m,lhs,rhs)
            c+=1
    return c

if __name__=='__main__':
    print('exact rational Gram identities:',verify_rational_gram())
    print('exact rational branch domination comparisons:',verify_entrywise_majorants())
    print('positive strict-region norming witnesses:',verify_witnesses())
    print('real / signed / complex direct pairs:',verify_random_pairs())
    print('ALL CHECKS PASSED')
