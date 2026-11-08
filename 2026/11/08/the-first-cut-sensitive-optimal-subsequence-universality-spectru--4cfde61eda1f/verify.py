#!/usr/bin/env python3
"""Self-contained exhaustive verification of a small de Bruijn universality census."""
from collections import Counter
import csv
from pathlib import Path

def cycles_euler(n):
    assert 2 <= n <= 5
    mask=(1<<(n-1))-1; ne=1<<n
    def rec(v, used, bits):
        if len(bits)==ne:
            if v==0:
                s=''.join(map(str,bits))
                start=(s+s[:n-1]).index('0'*n)
                yield s[start:]+s[:start]
            return
        for bit in (0,1):
            e=2*v+bit
            if not (used>>e)&1:
                yield from rec(e&mask,used|(1<<e),bits+[bit])
    yield from rec(0,1,[0])

def cycles_feedback(n):
    assert 2 <= n <= 5
    states=1<<n; tails=1<<(n-1)
    for truth in range(1<<tails):
        v=0; seen=0; letters=[]
        for j in range(states):
            if (seen>>v)&1: break
            seen |= 1<<v
            letters.append((v>>(n-1))&1)
            v=((v<<1)&(states-1))|(((v>>(n-1))&1)^((truth>>(v&(tails-1)))&1))
        if len(letters)==states and v==0:
            yield ''.join(map(str,letters))

def greedy_arches(w):
    mask=0; k=0
    for b in w:
        mask |= 1<<int(b)
        if mask==3:
            k+=1; mask=0
    return k

def independent_shortest_absent(w):
    # Suffix dynamic program for shortest unavailable scattered subsequence.
    n=len(w); successor=[n,n]; dp=[1]*(n+1)
    for i in range(n-1,-1,-1):
        successor[int(w[i])]=i
        vals=[]
        for b in (0,1):
            p=successor[b]
            vals.append(1+(dp[p+1] if p<n else 0))
        dp[i]=min(vals)
    return dp[0]

def statistics(s,n,check_dp=False):
    N=1<<n; vals=[]
    for i in range(N):
        r=s[i:]+s[:i]; w=r+r[:n-1]
        a=greedy_arches(w)
        if check_dp:
            assert independent_shortest_absent(w)==a+1,(s,i,a)
        vals.append(a)
    return min(vals),max(vals)

def run():
    expected={2:{(2,2):1},3:{(3,4):2},4:{(5,7):8,(6,7):8},5:{(10,12):512,(11,13):1536}}
    for n in (2,3,4,5):
        first=set(cycles_euler(n));second=set(cycles_feedback(n))
        assert first==second,(n,len(first),len(second),len(first^second))
        assert len(first)==(1<<((1<<(n-1))-n))
        for s in first:
            assert s.startswith('0'*n)
            assert len({(s+s[:n-1])[i:i+n] for i in range(1<<n)})==1<<n
        counts=Counter(statistics(s,n,True) for s in first)
        assert counts==expected[n],(n,counts)
        print(f'n={n}: {len(first)} cycles, intrinsic min/max arch census {dict(sorted(counts.items()))}')
    # Symmetry-refined census modulo reversal and symbol complementation.
    def canonical(s):
        k=(s+s[:4]).index('00000')
        return s[k:]+s[:k]
    def complement(s):
        return ''.join('1' if ch=='0' else '0' for ch in s)
    pool=set(cycles_feedback(5))
    seen=set(); orbit_distribution=Counter()
    for s in sorted(pool):
        if s in seen: continue
        orbit={canonical(t) for t in (s,s[::-1],complement(s),complement(s[::-1]))}
        assert orbit <= pool
        stats={statistics(t,5,True) for t in orbit}
        assert len(stats)==1
        orbit_distribution[(next(iter(stats)),len(orbit))]+=1
        seen.update(orbit)
    assert len(seen)==2048
    assert orbit_distribution=={
        ((10,12),2):16, ((10,12),4):120,
        ((11,13),2):16, ((11,13),4):376
    },orbit_distribution
    print('symmetry orbit census',dict(sorted(orbit_distribution.items())))
    path=Path(__file__).resolve().with_name('CENSUS.csv')
    assert path.is_file(), 'CENSUS.csv is a required evidence file'
    with path.open(encoding='utf-8',newline='') as stream:
        reader=csv.DictReader(stream)
        assert reader.fieldnames==['canonical_cycle','worst_cut_index','best_cut_index']
        actual=[(row['canonical_cycle'],int(row['worst_cut_index']),int(row['best_cut_index'])) for row in reader]
    expected_rows=[(s,*statistics(s,5,True)) for s in sorted(cycles_feedback(5))]
    assert actual==expected_rows, 'saved census does not match independently regenerated census'
    print('saved 2048-row census verified')
    print('DEBRUIJN_SUBSEQUENCE_CENSUS_VERIFY_OK')

if __name__=='__main__':run()
