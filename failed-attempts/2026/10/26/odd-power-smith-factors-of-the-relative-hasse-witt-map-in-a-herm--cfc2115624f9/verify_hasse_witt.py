"""Exact small-prime independent checks for a one-parameter Artin--Schreier family.
Run with Python 3; standard library only. The universal statement is proved in RESULT.md.
"""
from itertools import combinations
from math import comb, factorial


def inv(x,p):
    return pow(x%p,-1,p)


def determinant_mod_p(mat,p):
    a=[[int(t)%p for t in row] for row in mat]
    n=len(a)
    val=1
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:
            return 0
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            val=-val
        t=a[j][j]
        val=val*t%p
        t_inv=inv(t,p)
        for k in range(j+1,n):
            mult=a[k][j]*t_inv%p
            for l in range(j+1,n):
                a[k][l]=(a[k][l]-mult*a[j][l])%p
            a[k][j]=0
    return val%p


def rank_mod_p(mat,p):
    a=[list(map(lambda x:x%p,row)) for row in mat]
    if not a: return 0
    m,n=len(a),len(a[0]);r=0
    for j in range(n):
        q=next((z for z in range(r,m) if a[z][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        ti=inv(a[r][j],p)
        for z in range(r+1,m):
            mul=a[z][j]*ti%p
            if mul:
                a[z][j:]=[(v-mul*w)%p for v,w in zip(a[z][j:],a[r][j:])]
        r+=1
        if r==m:break
    return r


def verify_prime(p):
    basis=[(i,j) for j in range(p-1) for i in range(p-1-j)]
    idx={v:k for k,v in enumerate(basis)}
    g=p*(p-1)//2
    assert len(basis)==g
    # Construct entries from the Cartier expansion, not from anticipated blocks.
    A=[[{} for _ in basis] for _ in basis]
    for ci,(i,j) in enumerate(basis):
        for t in range(j+1):
            for s in range(t+1):
                m=i+(p+1)*(t-s)+2*s
                if m%p!=p-1:continue
                out=((m-p+1)//p,j-t)
                assert out in idx
                ri=idx[out]
                c=(-1)**t*comb(j,t)*comb(t,s)%p
                A[ri][ci][s]=(A[ri][ci].get(s,0)+c)%p
    assert all(len({d:c for d,c in entry.items() if c})<=1 for row in A for entry in row)
    # A is Cartier after adjoining a^(1/p); transpose A^[p] is the
    # Hasse--Witt matrix. Valuations (exponents) stay as constructed.
    M=(p-1)//2
    expected_factors=[]
    for v in range(p-2):
        rows=[(v-2*r,r) for r in range(v//2+1)]
        cols=[(p-3-v-2*c,v+1+c) for c in range(M-(v+1)//2)]
        k=min(len(rows),len(cols))
        expected_factors.extend(2*t-1 for t in range(1,k+1))
        for r,out in enumerate(rows):
            for c,source in enumerate(cols):
                actual={e:z for e,z in A[idx[out]][idx[source]].items() if z}
                t=source[1]-out[1]
                s=1+r+c
                coef=(-1)**t*comb(source[1],t)*comb(t,s)%p
                assert actual=={s:coef},(p,v,r,c,actual,s,coef)
        # Independent determinant check for the leading Hankel minors.
        for t in range(1,k+1):
            mat=[[inv(factorial(1+i+j),p) for j in range(t)] for i in range(t)]
            det=determinant_mod_p(mat,p)
            formula=(-1)**(t*(t-1)//2)
            for u in range(t):
                formula=formula*factorial(u)*inv(factorial(u+t),p)%p
            assert det==formula%p and det!=0
            # Every t-minor has valuation >= t^2; leading t-minor attains t^2.
            assert sum(1+i+i for i in range(t))==t*t
    desired=[]
    for r in range(1,(p+1)//4+1):
        desired.extend([2*r-1]*(p+2-4*r))
    assert sorted(expected_factors)==sorted(desired),(p,expected_factors,desired)
    assert len(desired)==(p*p-1)//8
    assert sum(desired)==sum(expected_factors)
    if p<=13:
        eval_mat=[[sum(coeff.values())%p for coeff in row] for row in A]
        assert rank_mod_p(eval_mat,p)==len(desired)
        assert all(not A[i][j].get(0,0) for i in range(g) for j in range(g))
    return g,len(desired),sum(desired),{e:desired.count(e) for e in sorted(set(desired))}


def main():
    for p in (3,5,7,11,13,17,19,23):
        g,rank,length,profile=verify_prime(p)
        print(f'p={p} genus={g} generic_rank={rank} torsion_length={length} exponents={profile}')
    print('VERIFY_OK: direct Cartier coefficients, block minors, factorial determinants, ranks and Smith profiles')

if __name__=='__main__':main()
