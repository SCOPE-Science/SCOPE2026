"""Exact finite tests for the barycentric isospectral-direction theorem.

The theorem's uniform proof is in RESULT.md; these calculations check examples
and its matrix identities independently over Q and over finite fields.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def rank_mod(A, p):
    M = [[int(x) % p for x in row] for row in A]
    r = 0
    for j in range(len(M[0])):
        piv = next((k for k in range(r, len(M)) if M[k][j]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][j], -1, p)
        M[r] = [x * inv % p for x in M[r]]
        for k in range(len(M)):
            if k != r:
                fac = M[k][j]
                M[k] = [(x - fac * y) % p for x, y in zip(M[k], M[r])]
        r += 1
    return r


def exact_moment_check(d):
    n = len(d)
    w = [F(1, __import__('math').prod(di-dj for j, dj in enumerate(d) if j!=i))
         for i, di in enumerate(d)]
    S = [sum(w[i]*d[i]**k for i in range(n)) for k in range(n)]
    assert S == [F(0)]*(n-1) + [F(1)], (d, S)
    B = [[F((di-dj)**2) for dj in d] for di in d]
    BW = [[B[i][j]*w[j] for j in range(n)] for i in range(n)]
    BWB = mul(BW, B)
    target = F(1) if n==5 else F(0)
    assert all(x==target for row in BWB for x in row)
    assert all(x==0 for row in mul([[BWB[i][j]*w[j] for j in range(n)]
                                    for i in range(n)],B) for x in row)
    return True


def finite_mod_example(n, p, seed):
    rng = Random(seed)
    d = u = None
    for _ in range(100000):
        sample = rng.sample(range(1,p),n)
        weights = [pow(__import__('math').prod((di-dj)%p for j,dj in enumerate(sample)
                         if j!=i)%p, -1, p) for i,di in enumerate(sample)]
        if all(pow(w, (p-1)//2, p)==1 for w in weights):
            d=sample
            roots={a*a%p:a for a in range(1,p)}
            u=[roots[w] for w in weights]
            break
    assert d is not None, 'No split example located'
    v=[d[i]*u[i]%p for i in range(n)]
    N=[[(u[i]*v[j]-v[i]*u[j])%p for j in range(n)] for i in range(n)]
    Q=[[(d[j]-d[i])*N[i][j]%p for j in range(n)] for i in range(n)]
    assert all((Q[i][j]-(d[i]-d[j])**2*u[i]*u[j])%p==0
               for i in range(n) for j in range(n))
    N2=mul(N,N)
    ND=[[N[i][j]*d[j]%p for j in range(n)] for i in range(n)]
    assert all(x%p==0 for row in N2 for x in row)
    assert all(x%p==0 for row in mul(ND,N) for x in row)
    Q2=mul(Q,Q)
    Q3=mul(Q2,Q)
    assert rank_mod(Q,p)==3
    assert rank_mod(Q2,p)==(1 if n==5 else 0)
    assert all(x%p==0 for row in Q3 for x in row)
    for t in [0,1,2,7]:
        g=[[((1 if i==j else 0)+t*N[i][j])%p for j in range(n)] for i in range(n)]
        gi=[[((1 if i==j else 0)-t*N[i][j])%p for j in range(n)] for i in range(n)]
        I=mul(g,gi)
        assert all(I[i][j]%p==(1 if i==j else 0) for i in range(n) for j in range(n))
        dg=[[d[i]*gi[i][j]%p for j in range(n)] for i in range(n)]
        lhs=mul(g,dg)
        assert all((lhs[i][j]-d[i]*(i==j)-t*Q[i][j])%p==0
                   for i in range(n) for j in range(n))
    classes=set()
    for bits in product([1,-1],repeat=n-1):
        signs=[1]+list(bits)
        Qs=tuple((signs[i]*signs[j]*Q[i][j])%p
                 for i,j in combinations(range(n),2))
        classes.add(Qs)
    assert len(classes)==2**(n-1)
    return d


def main():
    for n in range(5,11):
        assert exact_moment_check(list(range(n)))
        assert exact_moment_check([j*j+3*j+1 for j in range(n)])
        print(f'exact rational residue/matrix identities n={n}: PASS')
    for n in (5,6,7):
        d=finite_mod_example(n, 1009, 900+n)
        print(f'finite-field unipotent conjugation, rank, sign orbit n={n}: PASS, d={d}')
    print('All finite checks PASS. They supplement, not replace, the proof for all n.')


if __name__=='__main__':
    main()
