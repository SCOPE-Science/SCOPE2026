"""Exact finite-coordinate tests for ray Lipschitz commutators.

The tests check finite identities and Abel-sum consequences. They are
supplementary to the analytic infinite-dimensional proof.
"""
from fractions import Fraction
from math import comb, log


def parent(v):
    return [v[0]]+v[:-1]


def multiply(a,b):
    return [x*y for x,y in zip(a,b)]


def commutator(psi,f,m):
    result=[Fraction(0)]*len(f)
    for j in range(m+1):
        w=f
        for _ in range(m-j):
            w=parent(w)
        w=multiply(psi,w)
        for _ in range(j):
            w=parent(w)
        result=[a+(-1)**j*comb(m,j)*b for a,b in zip(result,w)]
    return result


def diff(psi,n,m):
    return sum(((-1)**j*comb(m,j)*psi[n-j] for j in range(m+1)),Fraction(0))


def trial_rows(psi,m,N):
    rows=[]
    for n in range(1,N+1):
        row=[]
        for k in range(N+1):
            f=([Fraction(1)]*(N+1) if k==0 else
               [Fraction(0) if j<k else Fraction(1) for j in range(N+1)])
            y=commutator(psi,f,m)
            row.append(y[n]-y[n-1])
        rows.append(row)
    return rows


checks=0
for N in range(6,12):
    for m in range(1,4):
        for seed in range(16):
            psi=[Fraction(((7*n+5*seed+3*n*n)%17)-8,n+4) for n in range(N+1)]
            rows=trial_rows(psi,m,N)
            for n in range(m+2,N+1):
                row=rows[n-1]
                d=diff(psi,n,m)
                dd=diff(psi,n,m+1)
                assert row[0]==dd
                checks+=1
                for k in range(1,N+1):
                    expected=dd if k<=n-m-1 else (d if k==n-m else 0)
                    assert row[k]==expected
                    checks+=1
                assert sum(map(abs,row[1:]))==(n-m-1)*abs(dd)+abs(d)
                checks+=1

# Alternating and quarter-rotation modulations: exact row-sum upper bounds
# for H U_q H. This is NOT a numerical test for infinite compactness.
for q in [-1,1j]:
    for n in [12,18,24,40,64,100]:
        norm=sum(abs(sum(q**j/j for j in range(k+1,n))) for k in range(1,n-1))/n
        assert norm<=12*(1+log(n))/n
        checks+=1

print('RAY_CALKIN_COMMUTATOR_CHECK_OK',checks)
