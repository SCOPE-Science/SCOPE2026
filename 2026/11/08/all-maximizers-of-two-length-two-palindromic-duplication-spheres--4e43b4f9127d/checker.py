#!/usr/bin/env python3
"""Standalone finite checks for maximal two-step length-two palindromic duplication spheres."""
from itertools import product


def duplicate(word, start):
    assert 0 <= start <= len(word)-2
    return word[:start+2] + word[start:start+2][::-1] + word[start+2:]


def descendants(word):
    return {duplicate(duplicate(word, i), j)
            for i in range(len(word)-1) for j in range(len(word)+1)}


def canonical_histories(n):
    entries = []
    for s in range(n-1):
        entries.extend([(s, s), (s, s+1), (s, s+2)])
        if s < n-2:
            entries.extend([(s, s+3), (s+1, s)])
        for r in range(s+2, n-1):
            entries.append((s, r+2))
    assert len(entries) == (n*n+5*n-8)//2
    return entries


def signatures(n):
    original=tuple(range(n))
    return {h: duplicate(duplicate(original,h[0]),h[1])
            for h in canonical_histories(n)}


def symbolic_check():
    cases=0
    for n in range(2,28):
        d=signatures(n)
        sigs=list(d.values())
        for i in range(len(sigs)):
            for j in range(i):
                assert any(abs(a-b)==1 for a,b in zip(sigs[i],sigs[j])), (n,i,j)
                cases+=1
        # Independently verify each stated witness in the proof table.
        for s in range(n-1):
            local={'A':(s,s),'B':(s,s+1),'C':(s,s+2)}
            if s<n-2:
                local.update({'D':(s,s+3),'E':(s+1,s)})
            for a,b,p in [('A','B',s+3),('A','C',s+4),('B','C',s+3),
                          ('A','D',s+4),('A','E',s+4),('B','D',s+3),
                          ('B','E',s+3),('C','D',s+5),('C','E',s+5),
                          ('D','E',s+6)]:
                if a in local and b in local:
                    u,v=d[local[a]][p],d[local[b]][p]
                    assert abs(u-v)==1,(n,s,a,b,p,u,v)
            for r in range(s+2,n-1):
                R=(s,r+2)
                for a,p in [('A',s+4),('B',s+3),('C',r+4),
                            ('D',s+5),('E',s+5)]:
                    if a in local:
                        u,v=d[local[a]][p],d[R][p]
                        assert abs(u-v)==1,(n,s,a,r,p,u,v)
                for t in range(r+1,n-1):
                    u,v=d[R][r+4],d[(s,t+2)][r+4]
                    assert abs(u-v)==1,(n,s,r,t,u,v)
        # Every possible history has the same index-word as a canonical history.
        cset=set(sigs)
        original=tuple(range(n))
        for i in range(n-1):
            first=duplicate(original,i)
            for j in range(n+1):
                assert duplicate(first,j) in cset
    print('Symbolic history tests: n=2..27, nonidentical canonical pairs:',cases)


def exhaustive_check():
    words=0
    configs=[(2,10),(3,8),(4,6)]
    for q, maximum_n in configs:
        for n in range(2, maximum_n+1):
            mx=(n*n+5*n-8)//2
            attained=0
            for word in product(range(q),repeat=n):
                sphere=len(descendants(word))
                proper=all(word[k]!=word[k+1] for k in range(n-1))
                assert sphere<=mx, (q,n,word,sphere,mx)
                assert (sphere==mx)==proper,(q,n,word,sphere,mx)
                attained+=sphere==mx
                words+=1
            assert attained==q*(q-1)**(n-1),(q,n,attained)
            print('q, n, max, number of maximizing sources:',q,n,mx,attained)
    print('Total source words verified:',words)


if __name__=='__main__':
    symbolic_check()
    exhaustive_check()
    print('All finite checks passed.')
