"""Exhaustive, independent finite-field checks for prescribed nilpotent power fibers.
Usage: python verify_roots.py
Only standard-library Python is required.
"""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import prod


def partitions_bounded(total, cap, maximum=None):
    if total == 0:
        yield ()
        return
    m = min(total, cap, total if maximum is None else maximum)
    for x in range(m, 0, -1):
        for tail in partitions_bounded(total-x, cap, x):
            yield (x,)+tail


def centralizer_order(part, q):
    if not part:
        return 1
    E = sum(sum(x >= j for x in part)**2 for j in range(1,max(part)+1))
    answer=Fraction(q**E)
    for size in set(part):
        multiplicity = part.count(size)
        for i in range(1,multiplicity+1):
            answer *= Fraction(q**i-1,q**i)
    assert answer.denominator == 1, (part,q,answer)
    return int(answer)


def prediction(n,m,q):
    if m >= n:
        return Counter()
    target=(2,) + (1,)*(n-2)
    ctarget=centralizer_order(target,q)
    out=Counter()
    for nu in partitions_bounded(n-m-1,m):
        lam=(m+1,)+nu
        denom=centralizer_order(lam,q)
        assert ctarget % denom == 0, (n,m,q,lam,ctarget,denom)
        out[n-len(lam)]+=ctarget//denom
    return out


class Field:
    def __init__(self,q):
        self.q=q
        self.p={2:2,3:3,4:2,5:5}[q]
        if q==4:
            self.add=[[a^b for b in range(q)] for a in range(q)]
            self.mul=[[self._gf4_mul(a,b) for b in range(q)] for a in range(q)]
        else:
            self.add=[[(a+b)%q for b in range(q)] for a in range(q)]
            self.mul=[[(a*b)%q for b in range(q)] for a in range(q)]
    @staticmethod
    def _gf4_mul(a,b):
        u=(a&1)*(b&1)
        v=((a>>1)*(b&1))^((a&1)*(b>>1))
        w=(a>>1)*(b>>1)
        return (u^w) | ((v^w)<<1)  # x^2=x+1


def matrix_mul(A,B,n,F):
    out=[0]*(n*n)
    mul=F.mul
    add=F.add
    for i in range(n):
        for k in range(n):
            v=A[i*n+k]
            if not v: continue
            for j in range(n):
                w=B[k*n+j]
                if w:
                    index=i*n+j
                    out[index]=add[out[index]][mul[v][w]]
    return out


def mat_rank(A,n,F):
    arr=[A[i*n:(i+1)*n] for i in range(n)]
    p=0
    for c in range(n):
        s=next((i for i in range(p,n) if arr[i][c]),None)
        if s is None: continue
        arr[p],arr[s]=arr[s],arr[p]
        pivot=arr[p][c]
        inv=next(v for v in range(1,F.q) if F.mul[v][pivot]==1)
        arr[p]=[F.mul[inv][x] for x in arr[p]]
        for i in range(p+1,n):
            factor=arr[i][c]
            if not factor:continue
            for j in range(c,n):
                # subtraction is multiplication by -1, or xor in characteristic two
                term=F.mul[factor][arr[p][j]]
                arr[i][j]=F.add[arr[i][j]][term] if F.p==2 else (arr[i][j]-term)%F.q
        p+=1
        if p==n:break
    return p


def test(q,n):
    F=Field(q)
    C=[0]*(n*n)
    C[1]=1   # elementary matrix E_01
    zero=[0]*(n*n)
    # Every m-th root must commute with C. The centralizer of E_01
    # consists precisely of matrices with X[i,0]=0 (i>0),
    # X[1,j]=0 (j!=1), and X[0,0]=X[1,1].
    fixed={(i,0) for i in range(1,n)} | {(1,j) for j in range(n) if j!=1}
    free=[(i,j) for i in range(n) for j in range(n)
          if (i,j) not in fixed and (i,j)!=(1,1)]
    assert len(free)==n*n-2*n+2
    hist={m:Counter() for m in range(2,n)}
    for values in product(range(q),repeat=len(free)):
        A=[0]*(n*n)
        for (i,j),value in zip(free,values):
            A[i*n+j]=value
        A[n+1]=A[0]  # X[1,1]=X[0,0]
        B=matrix_mul(A,A,n,F)
        for m in range(2,n):
            if B==C:
                hist[m][mat_rank(A,n,F)]+=1
            if m+1<n:
                B=matrix_mul(B,A,n,F)
    for m in range(2,n):
        expected=prediction(n,m,q)
        assert hist[m]==expected,(q,n,m,hist[m],expected)
        print('q=%d n=%d m=%d rank_histogram=%s total=%d PASS' %
              (q,n,m,dict(sorted(hist[m].items())),sum(hist[m].values())))


if __name__=='__main__':
    for q,n in [(2,3),(3,3),(4,3),(5,3),(2,4),(3,4),(2,5)]:
        test(q,n)
    print('ALL_MINIMAL_NILPOTENT_POWER_FIBERS_PASS')
