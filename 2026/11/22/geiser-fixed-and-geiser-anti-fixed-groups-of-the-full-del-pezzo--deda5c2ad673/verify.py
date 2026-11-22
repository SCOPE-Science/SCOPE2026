#!/usr/bin/env python3
"""Exact reproducible integer verification for the 56 exceptional curve intersection multigraph."""
from itertools import combinations
from collections import Counter


def classes():
    out = []
    # Coordinates are dH - sum(m_i E_i) on the blowup of seven general points.
    for i in range(7):
        m = [0] * 7
        m[i] = -1
        out.append((0, *m))
    for I in combinations(range(7), 2):
        out.append((1, *[int(i in I) for i in range(7)]))
    for I in combinations(range(7), 5):
        out.append((2, *[int(i in I) for i in range(7)]))
    for i in range(7):
        out.append((3, *[1 + int(j == i) for j in range(7)]))
    assert len(out) == 56
    return out


def pairing(a, b):
    return a[0] * b[0] - sum(x * y for x, y in zip(a[1:], b[1:]))


def matrix_data():
    vec = classes()
    assert all(pairing(a, a) == -1 for a in vec)
    assert tuple(sum(a[j] for a in vec) for j in range(8)) == (84,) + (28,) * 7
    count = Counter()
    lap = [[0] * 56 for _ in range(56)]
    for i in range(56):
        for j in range(i + 1, 56):
            w = pairing(vec[i], vec[j]); count[w] += 1
            assert 0 <= w <= 2
            lap[i][j] = lap[j][i] = -w
            lap[i][i] += w; lap[j][j] += w
    assert count == Counter({0: 756, 1: 756, 2: 28}), count
    assert all(lap[i][i] == 29 for i in range(56))
    assert all(sum(row) == 0 for row in lap)
    for i in range(56):
        assert Counter(-lap[i][j] for j in range(56) if j != i) == Counter({0: 27, 1: 27, 2: 1})
    # Factorization L = 28 I - B^T J B, where J=diag(1,-1^7).
    # The nonzero spectrum of B^T J B equals that of J B B^T.
    gram8 = [[sum(v[i] * v[j] for v in vec) for j in range(8)] for i in range(8)]
    assert gram8[0][0] == 168
    assert all(gram8[0][i] == 60 for i in range(1, 8))
    assert all(gram8[i][j] == (32 if i == j else 20) for i in range(1, 8) for j in range(1, 8))
    assert all(lap[i][j] == (28 if i == j else 0) - pairing(vec[i], vec[j]) for i in range(56) for j in range(56))
    # On six independent differences of last seven coordinates the eigenvalue is -12.
    # On top/symmetric coordinates J BB^T acts as ((168,420),(-60,-152)),
    # with trace 16 and determinant -336; eigenvalues 28 and -12.
    assert 168 - 152 == 28 - 12
    assert 168 * (-152) - 420 * (-60) == 28 * (-12)
    return lap


def p_adic_smith(A, p, precision):
    """Exact p-Smith valuations via invertible operations over Z/p^precision."""
    n = len(A)
    mod = p ** precision
    M = [[z % mod for z in row] for row in A]
    vals = []
    for k in range(n):
        best = precision; ii = jj = None
        for i in range(k, n):
            for j in range(k, n):
                z = M[i][j]
                if z == 0:
                    continue
                v = 0
                while z % p == 0:
                    z //= p
                    v += 1
                if v < best:
                    best = v; ii = i; jj = j
                if best == 0: break
            if best == 0: break
        assert ii is not None, (p, k, "precision too low or singular")
        M[k], M[ii] = M[ii], M[k]
        for row in M: row[k], row[jj] = row[jj], row[k]
        div = p ** best
        pivot = M[k][k]
        assert pivot % div == 0
        inverse = pow((pivot // div) % (mod // div), -1, mod // div)
        M[k] = [(x * inverse) % mod for x in M[k]]
        assert M[k][k] == div
        for i in range(k+1, n):
            assert M[i][k] % div == 0
            t = M[i][k] // div
            if t:
                M[i] = [(x - t*y) % mod for x, y in zip(M[i], M[k])]
        for j in range(k+1, n):
            assert M[k][j] % div == 0
            t = M[k][j] // div
            if t:
                for i in range(k,n):
                    M[i][j] = (M[i][j] - t*M[i][k]) % mod
        assert all(M[i][k] == 0 for i in range(k+1,n))
        assert all(M[k][j] == 0 for j in range(k+1,n))
        vals.append(best)
    return vals


def bareiss_det(matrix):
    """Independent fraction-free exact determinant over the integers."""
    A = [list(row) for row in matrix]
    n = len(A)
    prev = 1
    sign = 1
    for k in range(n - 1):
        pivot = A[k][k]
        if pivot == 0:
            for r in range(k + 1, n):
                if A[r][k]:
                    A[k], A[r] = A[r], A[k]
                    sign = -sign
                    pivot = A[k][k]
                    break
        assert pivot != 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = A[i][j] * pivot - A[i][k] * A[k][j]
                assert value % prev == 0
                A[i][j] = value // prev
            A[i][k] = 0
        prev = pivot
    return sign * A[n - 1][n - 1]


def geiser_permutation(vec):
    """The Geiser conjugate of E has class -K_S - E."""
    minus_k = (3,) + (1,)*7
    ids = {x:i for i,x in enumerate(vec)}
    tau = [ids[tuple(minus_k[k]-e[k] for k in range(8))] for e in vec]
    assert all(tau[tau[i]] == i and tau[i] != i for i in range(56))
    assert len({tuple(sorted((i,tau[i]))) for i in range(56)})==28
    return tau


def equivariant_presentation(L, tau, deleted, epsilon):
    """Presentation of K/(tau-epsilon)K, epsilon=+1 or -1."""
    ids=[i for i in range(56) if i != deleted]
    M=[[L[i][j] for j in ids] for i in ids]
    # Basis of Div^0 is [vertex_i]-[vertex_deleted], i != deleted.
    return [M[r] + [int(ids[r]==tau[i])-int(ids[r]==tau[deleted])
                        -epsilon*int(ids[r]==i) for i in ids]
            for r in range(len(ids))]


def p_adic_rect_smith(A, p, precision):
    """Rectangular Smith valuations by invertible Z/p^k operations."""
    n=len(A); m=len(A[0]); mod=p**precision
    M=[[int(z)%mod for z in row] for row in A]
    vals=[]
    for k in range(n):
        best=precision; ii=jj=None
        for i in range(k,n):
            for j in range(k,m):
                z=M[i][j]
                if not z: continue
                v=0
                while z%p==0: z//=p; v+=1
                if v<best: best=v; ii=i; jj=j
                if best==0: break
            if best==0: break
        assert ii is not None
        M[k],M[ii] = M[ii],M[k]
        for row in M: row[k],row[jj] = row[jj],row[k]
        div=p**best
        inv=pow(M[k][k]//div,-1,mod//div)
        M[k]=[(z*inv)%mod for z in M[k]]
        assert M[k][k] == div
        for i in range(k+1,n):
            assert M[i][k]%div==0
            t=M[i][k]//div
            if t: M[i]=[(x-t*y)%mod for x,y in zip(M[i],M[k])]
        for j in range(k+1,m):
            assert M[k][j]%div==0
            t=M[k][j]//div
            if t:
                for i in range(k,n): M[i][j]=(M[i][j]-t*M[i][k])%mod
        assert all(M[i][k]==0 for i in range(k+1,n))
        assert all(M[k][j]==0 for j in range(k+1,m))
        vals.append(best)
    return vals


def equivariant_check(L):
    tau=geiser_permutation(classes())
    assert all(L[tau[i]][tau[j]]==L[i][j] for i in range(56) for j in range(56))
    targets={
        1:{2:Counter({0:28,1:1,2:26}),5:Counter({0:55}),7:Counter({0:29,1:26})},
       -1:{2:Counter({0:28,1:6,2:14,4:7}),5:Counter({0:48,1:7}),7:Counter({0:34,1:21})},
    }
    for deleted in (0,7,28,55):
        for eps in (1,-1):
            C=equivariant_presentation(L,tau,deleted,eps)
            for p,precision in ((2,115),(5,8),(7,48)):
                vals=p_adic_rect_smith(C,p,precision)
                assert Counter(vals)==targets[eps][p], (deleted,eps,p,Counter(vals))
    for eps, expected in ((1,[1]*28+[2]+[28]*26),
                           (-1,[1]*28+[2]*6+[28]*14+[560]*7)):
        local={p:sorted([v for v,mult in counts.items() for _ in range(mult)])
               for p,counts in targets[eps].items()}
        factors=[2**local[2][i]*5**local[5][i]*7**local[7][i] for i in range(55)]
        assert factors==expected, (eps, factors)
    assert 2**53*7**26*2**62*5**7*7**21 == 2*(2**114*5**7*7**47)


def main():
    L=matrix_data()
    # Matrix-tree theorem and eigenvalue decomposition give 28^48 * 40^7 / 56.
    expected_order = 2**114 * 5**7 * 7**47
    assert (28**48 * 40**7) // 56 == expected_order
    # Every root's Smith valuations. Precision strictly exceeds determinant p-adic exponent.
    targets={2:Counter({0:8,2:40,4:1,5:6}),
             5:Counter({0:48,1:7}),
             7:Counter({0:8,1:47})}
    for deleted in (0,7,28,55):
        A=[[L[i][j] for j in range(56) if j!=deleted]
           for i in range(56) if i!=deleted]
        assert bareiss_det(A) == expected_order
        for p,prec in ((2,115),(5,8),(7,48)):
            vals=p_adic_smith(A,p,prec)
            assert Counter(vals)==targets[p], (deleted,p,Counter(vals))
            assert sum(vals) == {2:114,5:7,7:47}[p]
    # Align nondecreasing local valuations to produce global invariant factors.
    local = {p:sorted([v for v,n in c.items() for _ in range(n)])
             for p,c in targets.items()}
    factors=[2**local[2][i]*5**local[5][i]*7**local[7][i] for i in range(55)]
    assert factors==[1]*8 + [28]*40 + [560] + [1120]*6, Counter(factors)
    assert __import__('math').prod(factors)==expected_order
    equivariant_check(L)
    print('GEISER_FIXED_ANTIFIXED_COMPONENT_GROUPS_OK')
    print('nodes=812 genus=757 spectral=0^1,28^48,40^7')
    print('smith=1^8,28^40,560^1,1120^6')
    print('fixed=2+28^26; anti=2^6+28^14+560^7')

if __name__=='__main__': main()
