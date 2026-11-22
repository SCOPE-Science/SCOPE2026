"""Finite checks for the finite-depth Bochvar normal-form theorem.

The proof of the unrestricted theorem is mathematical, not an inference from
finite computation. The script independently computes term operations for
small cases and compares them to the predicted combinatorial census.
"""
from itertools import product
from math import comb

U = 2

def closure(seeds, unary_box=True):
    """Complete closure under Bochvar negation, truth test, and disjunction."""
    seen = set(seeds)
    frontier = list(seeds)
    while frontier:
        f=frontier.pop()
        N=len(f)
        candidates=(bytes(2 if a==2 else 1-a for a in f),
                    bytes(int(a==1) for a in f))
        # Iterate current finite set: only earlier pairs needed at time of insertion.
        for h in candidates:
            if h not in seen:
                seen.add(h);frontier.append(h)
        for g in tuple(seen):
            h=bytes(2 if a==2 or b==2 else max(a,b) for a,b in zip(f,g))
            if h not in seen:
                seen.add(h);frontier.append(h)
    return seen

def make_worlds(n,k):
    # A pointed valuation on a deterministic n-cycle is a word of n colors.
    allwords=list(product(range(3), repeat=n*k))
    ix={word:i for i,word in enumerate(allwords)}
    shift=[]
    for word in allwords:
        rotate=word[k:]+word[:k]
        shift.append(ix[rotate])
    return allwords,shift

def exact_count(k,L):
    return sum(comb(k,s)*2**(2**s*3**(k*L-s)) for s in range(k+1))

def test(n,k,depth):
    words,shift=make_worlds(n,k)
    N=len(words)
    start={bytes([0]*N),bytes([1]*N)}
    for var in range(k):
        start.add(bytes(w[var] for w in words))
    current=closure(start)
    allcounts=[len(current)]
    for _ in range(depth):
        # A new box reads one successor's previous-depth value, but keeps the
        # operand's local undefined value. It is only applied to depth<d terms.
        new={bytes(2 if f[i]==2 else (1 if f[shift[i]]==1 else 0)
                   for i in range(N)) for f in current}
        current=closure(current|new)
        allcounts.append(len(current))
    for d,observed in enumerate(allcounts):
        L=min(d+1,n)
        expected=exact_count(k,L)
        assert observed==expected,(n,k,d,observed,expected)
    # Independently verify every resulting function's undefined set and
    # its bounded-prefix invariance, with no use of the normal-form proof.
    L=min(depth+1,n)
    prefix=[w[:k*L] for w in words]
    groups={}
    for i,p in enumerate(prefix):groups.setdefault(p,[]).append(i)
    for f in current:
        assert all(len({f[i] for i in ids})==1 for ids in groups.values())
        supports=[]
        for mask in range(1<<k):
            u_pattern=tuple(any(w[j]==2 and ((mask>>j)&1)
                                for j in range(k)) for w in words)
            if all((f[i]==2)==u_pattern[i] for i in range(N)):
                supports.append(mask)
        assert len(supports)==1
    print('VERIFIED',{'cycle_length':n,'letters':k,'depth':depth,
                      'depth_census':allcounts,'checked_term_functions':len(current)})

if __name__=='__main__':
    test(1,1,0)
    test(1,2,0)
    test(2,1,1)
    test(3,1,1)
    print('VERIFY_OK')
