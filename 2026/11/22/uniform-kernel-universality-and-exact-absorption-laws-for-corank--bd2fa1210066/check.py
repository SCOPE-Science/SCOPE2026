"""Finite-field matrix-product rank checks; Python 3 standard library only."""
from itertools import product
from collections import defaultdict
from fractions import Fraction

def mm(A,B,n,q):
    return tuple(sum(A[n*i+k]*B[n*k+j] for k in range(n))%q for i in range(n) for j in range(n))

def rank(A,n,q):
    rows=[list(A[n*i:n*(i+1)]) for i in range(n)]
    r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if rows[i][j]%q),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        t=pow(rows[r][j],-1,q)
        rows[r]=[(t*v)%q for v in rows[r]]
        for i in range(n):
            if i!=r:
                t=rows[i][j]
                rows[i]=[(rows[i][k]-t*rows[r][k])%q for k in range(n)]
        r+=1
    return r

def diag(n,r):
    return tuple(int(i==j and i<r) for i in range(n) for j in range(n))

def test(q,n,mode):
    zero=(0,)*(n*n)
    mats=list(product(range(q),repeat=n*n))
    ensemble=[]
    for M in mats:
        if rank(M,n,q)!=n-1:continue
        M2=mm(M,M,n,q)
        if mode=='idempotent' and M2==M:ensemble.append(M)
        if mode=='regular_nilpotent':
            P=M
            for _ in range(n-1):P=mm(P,M,n,q)
            if P==zero and M2!=zero:ensemble.append(M)
    assert ensemble
    assert len(ensemble)==((q**n-1)//(q-1))*q**(n-1) if mode=='idempotent' else True
    D=q**n-1
    for r in range(1,n+1):
        A=diag(n,r)
        drops=sum(rank(mm(M,A,n,q),n,q)==r-1 for M in ensemble)
        assert Fraction(drops,len(ensemble))==Fraction(q**r-1,D),(q,n,mode,r,drops,len(ensemble))
    exact={diag(n,n):1}
    pred={n:Fraction(1)}
    for k in range(1,7):
        new=defaultdict(int)
        for A,num in exact.items():
            for M in ensemble:new[mm(M,A,n,q)]+=num
        exact=dict(new)
        newp=defaultdict(Fraction)
        for r,prob in pred.items():
            if r==0:newp[0]+=prob
            else:
                p=Fraction(q**r-1,D)
                newp[r-1]+=prob*p
                newp[r]+=prob*(1-p)
        pred=dict(newp)
        mass=defaultdict(int)
        for A,num in exact.items():mass[rank(A,n,q)]+=num
        assert {r:Fraction(num,len(ensemble)**k) for r,num in mass.items()}=={r:v for r,v in pred.items() if v},(q,n,mode,k)
    # Exact partial fractions of the absorption-time survival transform.
    p_rates=[Fraction(q**r-1,D) for r in range(1,n+1)]
    coefficients=[]
    for i in range(n):
        c=Fraction(1)
        for j in range(n):
            if i!=j:c*=p_rates[j]/(p_rates[j]-p_rates[i])
        coefficients.append(c)
    for k in range(0,14):
        markov=[Fraction(0)]*(n+1)
        markov[n]=Fraction(1)
        for _ in range(k):
            nxt=[Fraction(0)]*(n+1)
            for r,weight in enumerate(markov):
                if not r:nxt[0]+=weight
                else:
                    nxt[r-1]+=weight*p_rates[r-1]
                    nxt[r]+=weight*(1-p_rates[r-1])
            markov=nxt
        survival=sum(markov[1:])
        closed=sum(coefficients[i]*(1-p_rates[i])**k for i in range(n))
        assert survival==closed,(q,n,mode,k,survival,closed)
    assert coefficients[0]==Fraction(q*(q**n-1),(q-1)*q**n)
    print('PASS',f'field={q}',f'dimension={n}',f'ensemble={mode}',f'size={len(ensemble)}',f'lengths=0..6',f'rank_layers=0..{n}')

if __name__=='__main__':
    test(2,2,'idempotent')
    test(3,2,'idempotent')
    test(2,3,'idempotent')
    test(2,3,'regular_nilpotent')
    print('All independent exact matrix/product-rank checks passed.')
