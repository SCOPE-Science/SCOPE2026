"""Independent finite checks for width/height-bounded automorphism periods.
Run: python checker.py
"""
import itertools
import math
from functools import lru_cache


def prime_powers(t):
    parts=[]
    p=2
    while p*p<=t:
        if t%p==0:
            q=1
            while t%p==0:
                q*=p
                t//=p
            parts.append(q)
        p+=1
    if t>1: parts.append(t)
    return sorted(parts, reverse=True)


def height_cost(parts,w):
    parts=sorted(parts,reverse=True)
    if not parts: return 1
    if max(parts)>w: return None
    @lru_cache(None)
    def solve(i,bins):
        if i==len(parts): return len(bins)
        a=parts[i]
        choices=[]
        for j,c in enumerate(bins):
            if c+a<=w:
                bs=list(bins);bs[j]+=a
                choices.append(solve(i+1,tuple(sorted(bs))))
        bs=tuple(sorted(bins+(a,)))
        choices.append(solve(i+1,bs))
        return min(choices)
    return solve(0,())


def posets(n):
    pairs=list(itertools.combinations(range(n),2))
    for choices in itertools.product(range(3), repeat=len(pairs)):
        rows=[1<<i for i in range(n)]
        for (i,j),direction in zip(pairs,choices):
            if direction==1: rows[i]|=1<<j
            if direction==2: rows[j]|=1<<i
        if any((rows[j] & ~rows[i]) for i in range(n) for j in range(n) if (rows[i]>>j)&1):
            continue
        yield tuple(rows)


def width_height(rows):
    n=len(rows)
    width=max((sum(1 for i in range(n) if mask>>i &1) for mask in range(1,1<<n) if all(not ((rows[i]>>j)&1) and not ((rows[j]>>i)&1) for i in range(n) for j in range(i+1,n) if mask>>i&1 and mask>>j&1)),default=0)
    @lru_cache(None)
    def height(i):
        return 1+max((height(j) for j in range(n) if j!=i and ((rows[i]>>j)&1)),default=0)
    return width,max(map(height,range(n)))


def order(perm):
    n=len(perm); seen=set(); r=1
    for i in range(n):
        if i not in seen:
            c=0;j=i
            while j not in seen:
                seen.add(j);c+=1;j=perm[j]
            r=math.lcm(r,c)
    return r


def automorphisms(rows):
    n=len(rows)
    for p in itertools.permutations(range(n)):
        if all(((rows[i]>>j)&1)==((rows[p[i]]>>p[j])&1) for i in range(n) for j in range(n)):
            yield p


def explicit_model(parts,groups):
    # groups: lists of prime-power orbit sizes; ordinal sum of antichain levels
    levels=[]
    permutation=[]
    for group in groups:
        start=len(permutation)
        for a in group:
            lo=len(permutation)
            permutation.extend(range(lo+1,lo+a))
            permutation.append(lo)
        levels.append(tuple(range(start,len(permutation))))
    rows=[]
    for level_index,level in enumerate(levels):
        for i in level:
            rows.append((1<<i)|sum(1<<j for later in levels[level_index+1:] for j in later))
    return tuple(rows),tuple(permutation)


def packing(parts,w):
    best=None
    def rec(idx,groups):
        nonlocal best
        if best is not None and len(groups)>len(best): return
        if idx==len(parts):
            best=[g[:] for g in groups]
            return
        x=parts[idx]
        for g in groups:
            if sum(g)+x<=w:
                g.append(x);rec(idx+1,groups);g.pop()
        groups.append([x]);rec(idx+1,groups);groups.pop()
    if not parts: return [[1]]
    rec(0,[])
    return best


def run():
    number=0;auto=0
    for n in range(1,5):
        for P in posets(n):
            number+=1
            w,h=width_height(P)
            for f in automorphisms(P):
                auto+=1
                t=order(f)
                parts=prime_powers(t)
                assert sum(parts)<=n if parts else n>=1
                assert max(parts,default=1)<=w
                assert height_cost(parts,w)<=h
                assert t>0 and math.lcm(*range(1,w+1))%t==0
    print('EXHAUSTIVE_POSETS_OK',number,auto)
    constructed=0
    for t in range(1,121):
        parts=prime_powers(t)
        if not parts:
            P,f=explicit_model(parts,[[1]])
            assert order(f)==t
            continue
        for w in range(max(parts),min(15,t)+1):
            groups=packing(parts,w)
            assert len(groups)==height_cost(parts,w)
            P,f=explicit_model(parts,groups)
            # rows of level sums, with possible zero-size no because t>1
            W,H=max(map(sum,groups)),len(groups)
            assert W<=w and H==len(groups)
            assert order(f)==t
            assert len(P)==sum(parts)
            assert f in set(automorphisms(P)) if len(P)<8 else all(((P[i]>>j)&1)==((P[f[i]]>>f[j])&1) for i in range(len(P)) for j in range(len(P)))
            constructed+=1
    print('CONSTRUCTIVE_MODELS_OK',constructed)
    for w in range(1,13):
        L=math.lcm(*range(1,w+1)); q=prime_powers(L)
        print(w, L, max(1,sum(q)), height_cost(q,w))

if __name__=='__main__':run()
