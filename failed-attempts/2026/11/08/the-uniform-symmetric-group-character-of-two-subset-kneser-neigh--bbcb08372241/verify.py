"""Exact finite checks for the symmetric-group neighborhood-homology character theorem.

Python 3 standard library only. Every cycle type is tested through degree 9;
nonempty simplicial chains are also checked directly in degrees 5 and 6.
The general proof is mathematical, not an inference from these finite tests.
"""
from itertools import combinations
from math import factorial
from fractions import Fraction


def partitions(n, hi=None):
    if n == 0:
        yield ()
        return
    if hi is None:
        hi = n
    for k in range(min(hi, n), 0, -1):
        for tail in partitions(n-k, k):
            yield (k,) + tail


def permutation(p):
    ans = []
    s = 0
    for length in p:
        a = list(range(s, s+length))
        for j in range(length):
            ans.append((a[j], a[(j+1)%length]))
        s += length
    d = dict(ans)
    return tuple(d[j] for j in range(s))


def orbit_masks(n, g):
    pairs = list(combinations(range(n), 2))
    seen = set()
    masks = []
    for e in pairs:
        if e in seen:
            continue
        m = 0
        u = e
        while u not in seen:
            seen.add(u)
            m |= (1<<u[0]) | (1<<u[1])
            u = tuple(sorted((g[u[0]],g[u[1]])))
        masks.append(m)
    return masks


def chain_trace_dp(n,g):
    # Alternating sum over invariant edge sets, incl. the empty set.
    dp = [0]*(1<<n)
    dp[0]=1
    for mask in orbit_masks(n,g):
        ndp = dp[:]
        for state, weight in enumerate(dp):
            if weight:
                ndp[state|mask] -= weight
        dp=ndp
    allowed = sum(dp[s] for s in range(1<<n) if s.bit_count()<=n-2)
    return -allowed  # reduced Lefschetz number


def predicted(n, p):
    f=p.count(1)
    sign=(-1)**(n-len(p))
    return sign*(f*f-3*f+1)


def hookdim(shape):
    n=sum(shape)
    den=1
    for i, ln in enumerate(shape):
        for j in range(ln):
            right=ln-j-1
            below=sum(1 for q in shape[i+1:] if q>j)
            den*=1+right+below
    return factorial(n)//den


def z_value(p):
    z=1
    for k in set(p):
        c=p.count(k)
        z *= (k**c)*factorial(c)
    return z


def exact_face_trace(n,g):
    edges=list(combinations(range(n),2))
    eidx={e:i for i,e in enumerate(edges)}
    faces=set()
    for excluded in combinations(range(n),2):
        ids=[i for i,e in enumerate(edges) if not (set(e)&set(excluded))]
        for s in range(1,1<<len(ids)):
            faces.add(tuple(ids[j] for j in range(len(ids)) if s>>j&1))
    result=-1
    for face in faces:
        mapped=tuple(eidx[tuple(sorted((g[edges[i][0]],g[edges[i][1]])))] for i in face)
        if set(mapped)!=set(face):
            continue
        inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        result+=(-1)**(len(face)-1+inversions)
    return len(faces),result


def main():
    tests=0
    for n in range(5,10):
        chars=[]
        for p in partitions(n):
            g=permutation(p)
            lc=chain_trace_dp(n,g)
            t=(-1)**(n-4)*lc
            expected=predicted(n,p)
            assert t==expected,(n,p,t,expected)
            chars.append((p,t))
            tests+=1
            if n<=6:
                faces,lc2=exact_face_trace(n,g)
                assert lc==lc2,(n,p,lc,lc2)
        assert sum(Fraction(v,z_value(p)) for p,v in chars)==0 # no full-group fixed vectors
        assert sum(Fraction(v*((-1)**(n-len(p))),z_value(p)) for p,v in chars)==0
        assert sum(Fraction(v*v,z_value(p)) for p,v in chars)==2
        predicted_dim=predicted(n,tuple([1]*n))
        a=hookdim((2,2)+(1,)*(n-4))
        b=hookdim((3,)+(1,)*(n-3))
        assert a+b==predicted_dim
        print('n=%d classes=%d top_degree=%d dimension=%d Specht_dimensions=(%d,%d) invariants=(0,0)'%(n,len(chars),n-4,predicted_dim,a,b))
    print('cycle_type_tests=%d' % tests)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':
    main()
