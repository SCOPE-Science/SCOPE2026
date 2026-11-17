"""Independent suffix-driven enumeration and polynomial check.
Run: python3 verify_suffix.py
"""
from collections import Counter
from math import comb

def suffix_hist(k,n):
    # Suffix nodes are appended from the sink toward the source.
    # Each suffix is represented by its excitation activity times as a tuple.
    summary=Counter({():1})
    for _ in range(n):
        nxt=Counter()
        for suffix, multiplicity in summary.items():
            for initial in range(k):
                # The local state evolves against the precomputed suffix indicator.
                state=initial
                activity=[]
                for t in range(len(suffix)+k+2):
                    if state==1: activity.append(t)
                    influence=(t in suffix)
                    state=(state+1)%k if state!=0 else (1 if influence else 0)
                activity=tuple(sorted(set(activity).union(suffix)))
                assert activity==tuple(range(len(activity))) or activity==()
                nxt[activity]+=multiplicity
        summary=nxt
    expected=Counter({(): (k-1)**n})
    for b in range(1,n+1): expected[tuple(range(b))]=comb(n,b)*(k-1)**(n-b)
    assert summary==expected, (k,n,summary,expected)
    return summary

for k in range(3,8):
    for n in range(1,8):
        s=suffix_hist(k,n)
        print(f"k={k} n={n} active_bursts={len(s)-1} total={sum(s.values())} longest_burst_count={s[tuple(range(n))]} PASS")
