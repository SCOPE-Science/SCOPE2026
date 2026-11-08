"""Direct finite-field checks for commuting idempotent inner derivations.

Only standard-library Python is required.  The matrix identities are tested on
matrix units and the ordered-pair counts are obtained by enumerating scalar-
normalized implementing matrices, not by generating the closed-form counts.
"""
import itertools
from collections import Counter
from functools import lru_cache


def field(q):
    if q in (2, 4):
        add = lambda x, y: x ^ y
        if q == 2:
            mul = lambda x, y: x & y
        else:
            def mul(x, y):
                z = 0
                while y:
                    if y & 1:
                        z ^= x
                    y >>= 1
                    x <<= 1
                    if x & 4:
                        x ^= 7
                return z
    elif q in (3, 5):
        add = lambda x, y: (x + y) % q
        mul = lambda x, y: x * y % q
    else:
        raise ValueError(q)
    neg = lambda x: x if q % 2 == 0 else (-x) % q
    inv = {a: next(b for b in range(1, q) if mul(a, b) == 1)
           for a in range(1, q)}
    return add, mul, neg, inv


def matrix_ops(n, q):
    add, mul, neg, inv = field(q)
    z = (0,) * (n*n)
    eye = tuple(int(i == j) for i in range(n) for j in range(n))
    E = [tuple(int(k == i*n+j) for k in range(n*n)) for i in range(n) for j in range(n)]
    def madd(A, B):
        return tuple(add(a, b) for a, b in zip(A, B))
    def mmul(A, B):
        return tuple(sum_q(mul(A[i*n+k], B[k*n+j]) for k in range(n))
                     for i in range(n) for j in range(n))
    def sum_q(v):
        y = 0
        for t in v:
            y = add(y, t)
        return y
    def comm(A, B):
        return madd(mmul(A, B), tuple(neg(x) for x in mmul(B, A)))
    def is_scalar(A):
        return all(A[i*n+j] == (A[0] if i == j else 0)
                   for i in range(n) for j in range(n))
    def deriv(A, B):
        return comm(A, B)
    def rank(cols):
        if not cols:
            return 0
        arr = [list(col) for col in zip(*cols)]
        r = 0
        for c in range(len(arr[0])):
            t = next((i for i in range(r, len(arr)) if arr[i][c]), None)
            if t is None:
                continue
            arr[r], arr[t] = arr[t], arr[r]
            zinv = inv[arr[r][c]]
            arr[r] = [mul(x, zinv) for x in arr[r]]
            for i in range(len(arr)):
                if i != r and arr[i][c]:
                    f = arr[i][c]
                    arr[i] = [add(x, neg(mul(f, y))) for x, y in zip(arr[i], arr[r])]
            r += 1
            if r == len(arr):
                break
        return r
    return add, mul, neg, madd, mmul, comm, deriv, is_scalar, rank, eye, E


def gl(n, q):
    z = 1
    for i in range(n):
        z *= q**n - q**i
    return z


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    num = den = 1
    for j in range(k):
        num *= q**(n-j)-1
        den *= q**(k-j)-1
    return num//den


def s(n, j, q):
    return gaussian(n, j, q) * q**(j*(n-j))


def g(n, q):
    return gl(n,q)//gl(n//2,q*q) if n%2 == 0 else 0


def expected(n, q):
    if q % 2:
        return {(0,0):1}
    N = Counter({0:1})
    for r in range(1, (n-1)//2+1):
        N[2*r*(n-r)] += s(n, r, q)
    if n % 2 == 0:
        m = n//2
        N[n*n//2] += (s(n,m,q)+g(n,q))//2
    out = Counter({(0, k):v for k,v in N.items()})
    for r in range(1, (n-1)//2+1):
        weight = s(n, r, q)
        accum = Counter()
        for j in range(r+1):
            for k in range(n-r+1):
                ell = j+k
                accum[2*ell*(n-ell)] += s(r,j,q)*s(n-r,k,q)
        if r%2==0 and (n-r)%2==0:
            accum[n*n//2] += g(r,q)*g(n-r,q)
        for k,v in accum.items():
            assert v%2==0
            out[(2*r*(n-r),k)] += weight*(v//2)
    if n%2==0:
        m=n//2
        split = s(n,m,q)//2
        nonsplit = g(n,q)//2
        accum=Counter()
        for j in range(m+1):
            for k in range(m+1):
                ell=j+k
                accum[2*ell*(n-ell)] += s(m,j,q)*s(m,k,q)
        accum[n*n//2] += g(m,q)**2
        for k,v in accum.items():
            assert v%2==0
            out[(n*n//2,k)] += split*(v//2)
        accum2 = Counter()
        for j in range(m+1):
            accum2[8*j*(m-j)] += s(m,j,q*q)
            accum2[n*n//2] += s(m,j,q*q)
        for k,v in accum2.items():
            assert v%2==0
            out[(n*n//2,k)] += nonsplit*(v//2)
    return {x:v for x,v in out.items() if v}


def enumerate_check(n,q,all_pair_direct=True):
    add,mul,neg,madd,mmul,comm,deriv,is_scalar,rank,eye,E = matrix_ops(n,q)
    reps={}
    for coords in itertools.product(range(q),repeat=n*n-1):
        A=(0,)+coords  # first diagonal entry normalized to zero
        if q%2==0:
            w=madd(mmul(A,A),A)
            good=is_scalar(w)
        else:
            # Directly evaluate idempotence without a characteristic-two shortcut.
            good=all(deriv(A,deriv(A,e))==deriv(A,e) for e in E)
        if good:
            # Directly check the original idempotence equation on matrix units.
            assert all(deriv(A,deriv(A,e))==deriv(A,e) for e in E)
            ra=rank([deriv(A,e) for e in E])
            reps[A]=ra
    # The original product rule is checked on a full matrix-unit basis.
    for A in (list(reps) if n<=3 else list(reps)[:25]):
        assert all(deriv(A,mmul(x,y)) == madd(mmul(deriv(A,x),y),mmul(x,deriv(A,y)))
                   for x in E for y in E)
    observed=Counter()
    aa=list(reps.items())
    for A,ra in aa:
        for B,rb in aa:
            pair=(ra,rb)
            c=comm(A,B)
            compat=is_scalar(c)
            # When both derivations are idempotent, a scalar commutator must vanish.
            assert compat == (c == (0,)*(n*n))
            if all_pair_direct:
                direct=all(deriv(A,deriv(B,e))==deriv(B,deriv(A,e)) for e in E)
                assert direct==compat
            if compat:
                observed[pair]+=1
    predicted=expected(n,q)
    assert dict(observed)==predicted,(n,q,predicted,observed)
    ordered=sum(observed.values())
    return f'n={n} q={q} idempotent_derivations={len(reps)} commuting_ordered_pairs={ordered} polynomial={dict(sorted(observed.items()))}'

if __name__=='__main__':
    cases=[(2,2,True),(2,3,True),(2,4,True),(3,2,True),(3,3,True),(4,2,False)]
    for case in cases:
        print(enumerate_check(*case),flush=True)
    print('COMMUTING_IDEMPOTENT_DERIVATION_BIVARIATE_RANK_OK')
