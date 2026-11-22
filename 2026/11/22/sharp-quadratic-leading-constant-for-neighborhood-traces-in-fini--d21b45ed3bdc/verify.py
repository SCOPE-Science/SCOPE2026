#!/usr/bin/env python3
"""Reproducible exact checks for chord-neighborhood trace counts.

No external packages or data files are required.
"""
from collections import Counter
from math import comb


def word(m):
    assert m >= 3
    w = [0, 1, 2, 0]
    for j in range(3, m):
        w += [j, j - 2]
    w += [m - 2, m - 1]
    assert len(w) == 2*m
    assert all(w.count(i) == 2 for i in range(m))
    return w


def masks_from_word(w):
    s = 0
    out = [0]
    for c in w[:-1]:
        s ^= 1 << c
        out.append(s)
    return out


def model_masks(m):
    return [0, 1, 1 << (m-1)] + [3 << i for i in range(m-1)] + [7 << i for i in range(m-2)]


def runs(x, m):
    ans = []
    k = 0
    while k < m:
        if x & (1 << k):
            start = k
            while k < m and x & (1 << k):
                k += 1
            ans.append((start,k-start))
        else:
            k += 1
    return ans


def all_traces(masks):
    return {a^b for a in masks for b in masks}


def expected_types(m):
    assert m >= 7
    ans = {(): 1}
    for k in range(1, 7): ans[(k,)] = m-k+1
    ans.update({(1,1):2*m-4, (1,2):2*m-7, (2,1):2*m-7,
                (1,3):m-4, (3,1):m-4, (2,2):comb(m-3,2),
                (2,3):comb(m-4,2), (3,2):comb(m-4,2),
                (3,3):comb(m-5,2)})
    return ans


def pairings(n):
    counts=[0]*n
    def rec(w, k):
        if len(w)==2*n:
            yield tuple(w)
            return
        for i in range(k):
            if counts[i] < 2:
                counts[i] += 1; w.append(i)
                yield from rec(w, k)
                w.pop(); counts[i] -= 1
        if k<n:
            counts[k] += 1; w.append(k)
            yield from rec(w,k+1)
            w.pop(); counts[k] -= 1
    yield from rec([],0)


def geometric_crossings(w,i,j):
    """Return labels whose occurrences interlace the inserted query chord.
    Gap i is immediately before the letter at position i, modulo len(w).
    """
    if i==j: return 0
    if i>j: i,j=j,i
    positions={c:[] for c in set(w)}
    for k,c in enumerate(w): positions[c].append(k)
    v=0
    for c,(p,q) in positions.items():
        if (i<=p<j)!=(i<=q<j): v|=1<<c
    return v


def main():
    for m in range(5, 37):
        w=word(m)
        prefixes=masks_from_word(w)
        assert set(prefixes)==set(model_masks(m))
        traces=all_traces(prefixes)
        assert len(traces)==2*m*m-4*m+1,(m,len(traces))
        if m>=7:
            got=Counter(tuple(length for _,length in runs(mask,m)) for mask in traces)
            assert dict(got)==expected_types(m),(m,got)
        if m<=22:
            for i in range(2*m):
                for j in range(2*m):
                    assert geometric_crossings(w,i,j)==prefixes[i]^prefixes[j]
    # Enumerate all cyclic chord matchings of up to twelve endpoints, not samples.
    observed={}
    total=0
    for m in range(1,7):
        maximum=0; count=0
        for w in pairings(m):
            count+=1
            maximum=max(maximum,len(all_traces(masks_from_word(w))))
        assert count==__import__('math').prod(range(1,2*m,2))
        observed[m]=maximum
        total += count
    assert observed=={1:2,2:4,3:8,4:16,5:31,6:49}
    print('VERIFY_OK words=5..36 pairings=1..6 total_matchings=%d' % total)

if __name__=='__main__': main()
