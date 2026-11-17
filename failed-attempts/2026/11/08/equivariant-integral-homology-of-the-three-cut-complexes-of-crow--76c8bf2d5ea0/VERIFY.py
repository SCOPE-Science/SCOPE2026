"""Finite checks for the three-cut complexes of matching-deleted bicliques.

Run with Python 3.10+ (standard library only). The proof for all n is in RESULT.md;
these finite calculations independently test the face description, chain ranks,
and equivariant character formulas at the indicated small orders.
"""
import itertools
import math
import random


def choose(n, k):
    return math.comb(n, k) if n >= k >= 0 else 0


def dual_faces(n, extra_edges=False):
    """Simplices with <=2 of each color and disjoint labels, plus optional diagonal edges."""
    out = [[] for _ in range(4)]
    for k in range(1, 5):
        for a in range(max(0, k-2), min(2, k)+1):
            for ai in itertools.combinations(range(n), a):
                for bj in itertools.combinations((j for j in range(n) if j not in ai), k-a):
                    out[k-1].append(tuple(ai) + tuple(n+j for j in bj))
    if extra_edges:
        out[1].extend((i, n+i) for i in range(n))
    return [sorted(s) for s in out]


def rank_mod2(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def betti_mod2(faces):
    sizes = [len(level) for level in faces]
    ranks = []
    for k in range(1,4):
        ids = {s:i for i,s in enumerate(faces[k-1])}
        cols = []
        for s in faces[k]:
            col=0
            for i in range(len(s)):
                col ^= 1 << ids[s[:i]+s[i+1:]]
            cols.append(col)
        ranks.append(rank_mod2(cols))
    return [sizes[0]-ranks[0]-1,
            sizes[1]-ranks[0]-ranks[1],
            sizes[2]-ranks[1]-ranks[2],
            sizes[3]-ranks[2]]


def cycle_counts(p):
    n=len(p); seen=set(); cnt={}
    for i in range(n):
        if i in seen:
            continue
        v=i; k=0
        while v not in seen:
            seen.add(v); k+=1; v=p[v]
        cnt[k]=cnt.get(k,0)+1
    return cnt


def predicted_traces(p, swap):
    c=cycle_counts(p)
    f=c.get(1,0); t=c.get(2,0); u=c.get(4,0)
    if not swap:
        return [2*f, 2*f*(f-1)-2*t,
                f*(f-1)*(f-2)-2*t*f,
                choose(f,2)*choose(f-2,2)-2*t*choose(f,2)+t*(t-1)]
    return [0,-2*t,0,4*choose(t,2)-2*u]


def direct_traces(faces,p,swap):
    n=len(p)
    def act(v):
        return p[v%n]+(n if ((v>=n)^bool(swap)) else 0)
    result=[]
    for level in faces:
        tr=0
        for face in level:
            image=[act(v) for v in face]
            if set(image) != set(face):
                continue
            inversions=sum(image[i]>image[j]
                           for i in range(len(image)) for j in range(i+1,len(image)))
            tr+=(-1)**inversions
        result.append(tr)
    return result


def disconnected_triple(n, triple):
    adj=lambda x,y: ((x<n)!=(y<n)) and (x%n != y%n)
    return sum(adj(x,y) for x,y in itertools.combinations(triple,2))<2


def check_dual_definition(n, y):
    yy={tuple(s) for level in y for s in level}
    yy.add(())
    full=(1<<(2*n))-1
    for mask in range(1<<(2*n)):
        v=tuple(i for i in range(2*n) if mask>>i & 1)
        if len(v)<=2:
            expected=True
        else:
            expected=all(not disconnected_triple(n,t)
                         for t in itertools.combinations(v,3))
        if expected != (v in yy):
            raise AssertionError((n,v,expected))
        # The primal face condition is the existence of a disconnected triple
        # inside the complement. Thus the primal complex is the Alexander dual.
        comp=tuple(i for i in range(2*n) if not mask>>i & 1)
        primal=any(disconnected_triple(n,t) for t in itertools.combinations(comp,3))
        assert primal == (comp not in yy)


def test():
    for n in range(4,9):
        x=dual_faces(n)
        y=dual_faces(n,True)
        assert [len(s) for s in x] == [2*n,2*n*(n-1),
                                      n*(n-1)*(n-2),choose(n,2)*choose(n-2,2)]
        if n>=5:
            b=1+n*(n-5)*(n-3)*(n-2)//4
            assert betti_mod2(x)==[0,0,0,b]
            assert betti_mod2(y)==[0,n,0,b]
        if n<=6:
            check_dual_definition(n,y)
        print('n=%d f=%s mod2-betti=%s' % (n,[len(s) for s in y],betti_mod2(y)))
    rng=random.Random(314159)
    for n in (5,6,7,8):
        F=dual_faces(n)
        perms=list(itertools.permutations(range(n))) if n<=6 else []
        if n>=7:
            for _ in range(240):
                p=list(range(n));rng.shuffle(p);perms.append(tuple(p))
        for p in perms:
            for swap in (False,True):
                got=direct_traces(F,p,swap)
                want=predicted_traces(p,swap)
                assert got==want,(n,p,swap,got,want)
        print('n=%d checked %d permutations x 2 color actions' % (n,len(perms)))
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    test()
