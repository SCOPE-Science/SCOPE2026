"""Independent partition-level checks for star edge colorings of K_{2,n}.

All colors are canonical nonnegative integers assigned in first-appearance order.
No closed formula is used to decide whether an assignment is star.
"""
from collections import Counter
from math import factorial


def falling(q, r):
    p = 1
    for j in range(r):
        p *= q-j
    return p


def coefficients(n):
    return {2*n-k: factorial(n)//(factorial(k)*factorial(n-2*k))
            for k in range(n//2+1)}


def obstructions(n):
    # Graph-level enumeration of simple 4-edge paths and 4-cycles.
    adj = [[] for _ in range(n+2)]
    for side in (0,1):
        for j in range(n):
            eid = side*n+j
            adj[side].append((j+2,eid))
            adj[j+2].append((side,eid))
    out = set()
    for initial in range(n+2):
        def visit(vertex, seen, edge_ids):
            if len(edge_ids)==4:
                if len(seen)==5 or (len(seen)==4 and vertex==initial):
                    out.add(tuple(edge_ids))
                return
            for nb,e in adj[vertex]:
                if nb not in seen:
                    visit(nb, seen+(nb,),edge_ids+(e,))
                elif len(edge_ids)==3 and nb==initial and len(seen)==4:
                    visit(nb, seen,edge_ids+(e,))
        visit(initial,(initial,),())
    return tuple(sorted(out))


def count_canonical(n):
    bans = obstructions(n)
    assert len(bans)>0 if n>=2 else True
    observed=Counter()
    attempted=0
    base=tuple(range(n))
    lower=[]
    def rec(i,top):
        nonlocal attempted
        if i==n:
            a=base+tuple(lower)
            attempted+=1
            for mask in bans:
                p,q,r,s=(a[j] for j in mask)
                if p==r and q==s:
                    return
            observed[top+1]+=1
            return
        for c in range(top+2):
            if c==i or c in lower:
                continue
            lower.append(c)
            rec(i+1,max(top,c))
            lower.pop()
    rec(0,n-1)
    return observed,attempted,len(bans)


def main():
    totals=0
    for n in range(2,8):
        seen,candidates,patterns=count_canonical(n)
        expected=coefficients(n)
        assert dict(seen)==expected, (n,seen,expected)
        totals+=candidates
        print(f'n={n}: tested={candidates} obstructions={patterns} classes={sum(seen.values())} distribution={dict(sorted(seen.items()))}')
    for n in range(1,101):
        vals=coefficients(n)
        k0=n//2
        assert min(vals)==2*n-k0
        assert sum(vals.values())==sum(factorial(n)//(factorial(k)*factorial(n-2*k)) for k in range(k0+1))
        if n>=2:
            q=2*n-k0
            assert sum(v*falling(q,c) for c,v in vals.items()) == vals[q]*factorial(q)
        arr=[vals[2*n-k] for k in range(k0+1)]
        assert all(arr[i]*arr[i]>=arr[i-1]*arr[i+1] for i in range(1,len(arr)-1))
    print(f'VERIFICATION_OK direct_orders=2..7 canonical_candidates={totals} arithmetic_orders=1..100')

if __name__=='__main__':
    main()
