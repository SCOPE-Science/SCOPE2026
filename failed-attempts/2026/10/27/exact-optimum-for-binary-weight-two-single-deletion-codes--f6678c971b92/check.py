"""Direct, standard-library finite checks of the weight-two deletion code theorem.
Run: python3 check.py
"""
from itertools import combinations

def word(n, i, j):
    a = ['0'] * n
    a[i] = a[j] = '1'
    return ''.join(a)

def descendants(s):
    return {s[:k] + s[k+1:] for k in range(len(s))}

def proposed(n):
    assert n >= 2
    near = [(i, i+1) for i in range(0,n-1,2)]
    long = [(i,i+3) for i in range(1,n-3,4)]
    return near + long

def optimum(n):
    m = n - 1
    return (m + (m+1)//2)//2

def proof_audit(n):
    vertices = list(combinations(range(n),2))
    zero_one = {v: {x for x in descendants(word(n,*v)) if x.count('1') == 1} for v in vertices}
    assert all(zero_one[v] == ({str('0')*i+'1'+'0'*(n-i-2) for i in {v[0],v[1]-1}}) for v in vertices)
    return vertices

def exact_independence(n):
    vs = list(combinations(range(n),2))
    Ds = [descendants(word(n,*v)) for v in vs]
    adj = [0]*len(vs)
    for i in range(len(vs)):
        for j in range(i+1,len(vs)):
            if Ds[i] & Ds[j]:
                adj[i] |= 1<<j
                adj[j] |= 1<<i
    best = 0
    def dfs(mask,chosen):
        nonlocal best
        if chosen + mask.bit_count() <= best: return
        if not mask:
            best = max(best,chosen)
            return
        # prioritize a high-degree vertex in current induced graph
        v = max((i for i in range(len(vs)) if mask>>i & 1), key=lambda i:(mask & adj[i]).bit_count())
        dfs(mask & ~(1<<v) & ~adj[v],chosen+1)
        dfs(mask & ~(1<<v),chosen)
    dfs((1<<len(vs))-1,0)
    return best

def main():
    for n in range(2, 41):
        vs = proof_audit(n)
        c = proposed(n)
        assert len(set(c)) == len(c) == optimum(n), (n,c)
        assert set(c) <= set(vs)
        seen = {}
        for v in c:
            for d in descendants(word(n,*v)):
                assert d not in seen, (n, v, seen[d], d)
                seen[d] = v
        if n <= 8:
            actual = exact_independence(n)
            assert actual == optimum(n), (n,actual,optimum(n))
    # Larger lengths: construction validation without enumerating all vertices.
    for n in (41,42,59,100,101,200):
        c=proposed(n)
        assert len(c)==optimum(n)
        seen=set()
        for v in c:
            dd=descendants(word(n,*v))
            assert not(dd & seen)
            seen |= dd
    print('PASS: all-vertex descendant identities n=2..40,')
    print('       exact independent-set search n=2..8,')
    print('       constructive disjointness n=2..42,59,100,101,200.')

if __name__=='__main__': main()
