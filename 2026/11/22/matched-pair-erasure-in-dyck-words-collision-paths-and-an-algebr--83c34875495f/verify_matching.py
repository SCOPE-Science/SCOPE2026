"""Exact finite checks for matching-pair erasure in Dyck words.

Run: python3 verify_matching.py
Uses only Python's standard library.
"""
from collections import Counter
from functools import lru_cache

@lru_cache(None)
def dyck(n):
    if n == 0:
        return ('',)
    return tuple('(' + a + ')' + b for k in range(n)
                 for a in dyck(k) for b in dyck(n - k - 1))

def matching_outputs(w):
    stack = []
    out = []
    for j, c in enumerate(w):
        if c == '(':
            stack.append(j)
        else:
            i = stack.pop()
            out.append(w[:i] + w[i + 1:j] + w[j + 1:])
    return out

def structural_count(w, check_classes=True):
    stack = []
    parent = {}
    children = {-1: []}
    for i, c in enumerate(w):
        if c == '(':
            par = stack[-1] if stack else -1
            parent[i] = par
            children[par].append(i)
            children[i] = []
            stack.append(i)
        else:
            stack.pop()
    unary = sum(len(kids) == 1 for p, kids in children.items() if p != -1)
    leaf_pairs = sum(
        sum(not children[x] and not children[y]
            for x, y in zip(kids, kids[1:]))
        for kids in children.values()
    )
    if check_classes:
        # Build the equivalence relation predicted by elementary collision links.
        leader = {v:v for v in parent}
        def root(x):
            while x != leader[x]:
                leader[x] = leader[leader[x]]
                x = leader[x]
            return x
        def join(a,b): leader[root(a)] = root(b)
        for v,kids in children.items():
            if v != -1 and len(kids) == 1:join(v,kids[0])
            for x,y in zip(kids,kids[1:]):
                if not children[x] and not children[y]:join(x,y)
        stack = []
        removed = {}
        for j,c in enumerate(w):
            if c == '(':stack.append(j)
            else:
                i = stack.pop()
                removed[i] = w[:i]+w[i+1:j]+w[j+1:]
        labels = list(parent)
        for a in labels:
            for b in labels:
                assert (removed[a]==removed[b]) == (root(a)==root(b)),(w,a,b)
    return len(parent) - unary - leaf_pairs

def poly_add(a, b):
    out = Counter(a)
    for k, v in b.items(): out[k] += v
    return {k:v for k,v in out.items() if v}

def poly_mul(a, b):
    out=Counter()
    for i, x in a.items():
        for j, y in b.items(): out[i+j] += x*y
    return dict(out)

def poly_scale_one_minus_u(a):
    out = Counter()
    for k, v in a.items():
        out[k] += v
        out[k+1] -= v
    return {k:v for k,v in out.items() if v}

def formula_polynomials(nmax):
    f=[{0:1}]
    for n in range(1,nmax+1):
        square=Counter()
        for i in range(n):
            for power, count in poly_mul(f[i],f[n-1-i]).items():
                square[power] += count
        prev=poly_add(f[n-1],f[n-2] if n>=2 else {})
        corr=poly_scale_one_minus_u(prev)
        result=Counter(square)
        for power, count in corr.items():result[power]-=count
        if n==1:
            result[0]+=1
            result[1]-=1
        f.append({k:v for k,v in result.items() if v})
    return f

def main():
    F=formula_polynomials(10)
    checked=0
    for n in range(1,11):
        dist=Counter()
        for w in dyck(n):
            d=len(set(matching_outputs(w)))
            assert structural_count(w)==d, (n,w,d,structural_count(w))
            dist[n-d]+=1
            checked+=1
        assert dist==Counter(F[n]),(n,dist,F[n])
        assert max(n-c for c in dist)==(1 if n==1 else n-1)
        if n>=2:
            fib1,fib2=1,1
            for _ in range(n):fib1,fib2=fib2,fib1+fib2
            assert dist[1]==fib1, (n,dist[1],fib1)
            assert dist[n-1]==2, (n, dist)
    print('VERIFY_OK sizes=1..10 words=%s quadratic=OK collision=OK extrema=OK' % checked)

if __name__=='__main__':
    main()
