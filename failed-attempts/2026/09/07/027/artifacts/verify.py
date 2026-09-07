"""Stdlib-only verifier for D(C3xC3xC6)=10 claim.
Checks:
 1. Group order/exponent/invariant factors/D*.
 2. Witness S9 (from witness.json) is zero-sum-free via all 2^9-1=511 checks;
    builds full verification table and checks distinct-subsum count.
 3. Small-depth brute-force cross-check of enumerator counts (n=2,3,4) without
    the subsum-mask trick (independent logic).
 4. Element order distribution (1,2,3,6) and unique order-2 element.
Run: python3 verify.py (stdlib only, <10 s).
"""
import json, itertools, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))

def add(a,b):
    return ((a[0]+b[0])%3, (a[1]+b[1])%3, (a[2]+b[2])%6)

def order(g):
    cur=(0,0,0)
    for k in range(1,13):
        cur=add(cur,g)
        if cur==(0,0,0):
            return k
    raise AssertionError("order>12")

def is_zsf_bruteforce(S):
    n=len(S)
    for mask in range(1,1<<n):
        s=(0,0,0)
        for i in range(n):
            if mask>>i & 1:
                s=add(s,S[i])
        if s==(0,0,0):
            return False
    return True

def main():
    ELEMS=[(a,b,c) for a in range(3) for b in range(3) for c in range(6)]
    assert len(ELEMS)==54, "order must be 54"
    exps=[order(g) for g in ELEMS]
    assert max(exps)==6, "exponent must be 6"
    from collections import Counter
    dist=Counter(exps)
    assert dist[1]==1 and dist[2]==1 and dist[3]==26 and dist[6]==26, f"order dist {dist}"
    assert [g for g in ELEMS if order(g)==2]==[(0,0,3)], "unique order-2"
    # D* = 1+(3-1)+(3-1)+(6-1) = 10
    Dstar=1+(3-1)+(3-1)+(6-1)
    assert Dstar==10
    print(f"[1] group OK: |G|=54 exp=6 orders {dict(dist)} D*=10")

    with open(os.path.join(BASE,"witness.json")) as f:
        w=json.load(f)
    S9=[tuple(g) for g in w["S"]]
    assert len(S9)==9, "witness length 9"
    assert all(isinstance(g,tuple) and len(g)==3 for g in S9)
    # orders of basis elements
    # full 511 check
    bad=[]
    table=[]
    for mask in range(1,1<<9):
        s=(0,0,0)
        idx=[i for i in range(9) if mask>>i & 1]
        for i in idx:
            s=add(s,S9[i])
        table.append((mask,idx,s))
        if s==(0,0,0):
            bad.append(mask)
    assert not bad, f"witness has zero-sum masks {bad}"
    subs=set([ (0,0,0) ]+[t[2] for t in table])
    assert len(subs)==54, f"distinct subsums {len(subs)} !=54"
    print(f"[2] witness OK: length 9 zero-sum-free, 511/511 nonzero, {len(subs)} distinct subsums (=|G|)")

    NONZERO=[g for g in ELEMS if g!=(0,0,0)]
    for n,expect in [(2,1404),(3,24310),(4,297804)]:
        c=sum(1 for S in itertools.combinations_with_replacement(NONZERO,n) if is_zsf_bruteforce(list(S)))
        assert c==expect, f"n={n} got {c} expect {expect}"
        print(f"[3] brute n={n} OK: {c} zero-sum-free multisets (matches enumerator)")
    print("ALL VERIFIER CHECKS PASSED")
    print("Note: length-10 UNSAT is certified by enumerate.c (rerun via replay.sh).")

if __name__=="__main__":
    main()
