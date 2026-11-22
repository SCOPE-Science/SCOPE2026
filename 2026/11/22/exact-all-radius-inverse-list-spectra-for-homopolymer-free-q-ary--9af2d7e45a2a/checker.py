#!/usr/bin/env python3
"""Exact independent verification of an adjacency-distinct supersequence formula."""
import itertools, math
from collections import Counter

def actual(q,m,d):
    out=Counter()
    for p in itertools.product(range(q),repeat=m+d):
        if any(p[i]==p[i+1] for i in range(len(p)-1)): continue
        # collect all DISTINCT receivers, rather than deletion locations
        rec=set()
        for ii in itertools.combinations(range(m+d),m):
            rec.add(tuple(p[i] for i in ii))
        for y in rec: out[y]+=1
    return out

def predicted(q,y,d):
    m=len(y)
    r=sum(y[i]==y[i-1] for i in range(1,m))
    # coefficient of z^(d-r) in (1+z)(q-1)^r / ((1-(q-2)z)^m(1-(q-1)z))
    k=d-r
    if k<0:return 0
    s=0
    for a in (0,1):
        if a>k:continue
        for j in range(k-a+1):
            v=k-a-j
            s+=math.comb(m+j-1,j)*((q-2)**j)*((q-1)**v)
    return (q-1)**r*s

def run():
    totalcases=totalparent=0
    for q,maxn in [(2,9),(3,8),(4,7),(5,6)]:
      for m in range(1,maxn+1):
       for d in range(0,maxn-m+1):
        obs=actual(q,m,d)
        for y in itertools.product(range(q), repeat=m):
            lhs=obs.get(y,0);rhs=predicted(q,y,d)
            assert lhs==rhs,(q,m,d,y,lhs,rhs)
            totalcases+=1
        totalparent+=q*(q-1)**(m+d-1)
      print(f'q={q} checked up to source length {maxn}')
    print('PASS',totalcases,'receiver configurations',totalparent,'source configurations (summed over lengths and deletions)')
if __name__=='__main__':run()

def direct_greedy_automaton(q,y,d):
    """Count source strings by properness and the deterministic leftmost-match DFA."""
    m=len(y);n=m+d
    # state (last_symbol, matched_length) indexed, last=-1 for empty
    cur={(-1,0):1}
    for _ in range(n):
        nxt={}
        for (last,k),v in cur.items():
            for c in range(q):
                if c==last:continue
                nk=k+(k<m and c==y[k])
                nxt[(c,nk)]=nxt.get((c,nk),0)+v
        cur=nxt
    return sum(v for (last,k),v in cur.items() if k==m)

def more_checks():
    cases=0
    for q in range(2,7):
        for m in range(1,15):
            for d in range(0,10):
                ys=[tuple(((k*i*i+3*i+i//2)%q) for i in range(m)) for k in range(1,5)]
                for y in set(ys):
                    assert direct_greedy_automaton(q,y,d)==predicted(q,y,d),(q,m,d,y)
                    cases+=1
    print('INDEPENDENT DFA PASS',cases)

if __name__=='__main__':more_checks()


def spectrum_checks():
    checked=0
    for q in range(3,9):
        for m in range(1,22):
            for d in range(0,16):
                values=[]
                for r in range(min(d,m-1)+1):
                    y=(0,)*(r+1)+tuple(1+i%2 for i in range(m-r-1))
                    assert sum(y[i]==y[i-1] for i in range(1,m))==r
                    values.append(predicted(q,y,d))
                assert all(values[i]>values[i+1] for i in range(len(values)-1)),(q,m,d,values)
                assert all(v>1 for v in values) if d>0 else values==[1]
                support=q*sum(math.comb(m-1,r)*(q-1)**(m-1-r) for r in range(min(d,m-1)+1))
                assert (support==q**m)==(d>=m-1)
                checked+=1
    print('SPECTRUM CHECK PASS',checked,'alphabet/length/deletion configurations')

if __name__=='__main__':spectrum_checks()
