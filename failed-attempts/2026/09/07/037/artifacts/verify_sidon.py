#!/usr/bin/env python3
"""Independent replay verifier for the Sidon census (stdlib only, deterministic).
- Re-reads sidon_table.json, checks each witness with naive set logic (no bitmasks):
  ordered differences distinct+nonzero AND sums (a<=b) distinct.
- Checks counting bound ub(n) = max k with k(k-1)+1<=n, and S(n)<=ub.
- For S(n)==ub: optimality follows from counting bound alone (no search needed).
- For S(n)==ub-1 (gap cases n=32,33,34,43,44,45,46,47): re-proves no ub-set exists by an
  INDEPENDENT exhaustive search: plain DFS over sorted sets containing 0 with Python-set
  difference tracking, NO divisor/multiplier pruning, NO bitmasks (different code path
  from sidon_census.py). Asserts search completes with zero hits.
Usage: python3 verify_sidon.py  (run in same directory as sidon_table.json)
"""
import json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))

def count_ub(n):
    k = int((1 + math.sqrt(4*n-3))//2)
    while (k+1)*k+1 <= n: k += 1
    while k*(k-1)+1 > n: k -= 1
    return k

def is_sidon_sets(A, n):
    seen=set()
    for a in A:
        for b in A:
            if a==b: continue
            d=(a-b)%n
            if d==0 or d in seen: return False
            seen.add(d)
    return len(seen)==len(A)*(len(A)-1)

def sums_ok(A, n):
    seen=set()
    L=list(A)
    for i,a in enumerate(L):
        for b in L[i:]:
            s=(a+b)%n
            if s in seen: return False
            seen.add(s)
    return len(seen)==len(L)*(len(L)+1)//2

def independent_no_k_set(n, k):
    """Exhaustive DFS without any automorphism pruning, set-based. Returns (nodes, elapsed)."""
    nodes=[0]
    t0=time.time()
    sys.setrecursionlimit(10000)
    found=[False]
    def rec(A, used, start):
        nodes[0]+=1
        if found[0]: return True
        if len(A)==k:
            found[0]=True
            return True
        need=k-len(A)
        for x in range(start, n):
            if (n-x)<need: break
            newds=[]
            ok=True
            for a in A:
                d1=(x-a)%n; d2=(a-x)%n
                if d1==0 or d2==0 or d1 in used or d2 in used or d1 in newds or d2 in newds:
                    # careful: if d1==d2 (n even, d=n/2) then the two ordered pairs collide
                    ok=False; break
                if d1==d2:
                    ok=False; break
                newds.extend([d1,d2])
            # also need newds internally distinct (checked incrementally above, but double-check)
            if not ok: continue
            if len(set(newds))!=len(newds): continue
            A.append(x)
            if rec(A, used|set(newds), x+1):
                return True
            A.pop()
        return found[0]
    # subtle bug guard: the loop above checks d2 in newds before appending d1 of same a?
    # Reimplement cleanly per candidate to avoid order bug:
    found=[False]; nodes=[0]
    def rec2(A, used, start):
        nodes[0]+=1
        if len(A)==k:
            found[0]=True
            return True
        need=k-len(A)
        for x in range(start, n):
            if (n-x)<need: break
            coll=set()
            ok=True
            for a in A:
                for d in ((x-a)%n,(a-x)%n):
                    if d==0 or d in used or d in coll:
                        ok=False; break
                    coll.add(d)
                if not ok: break
            # need 2*len(A) distinct new diffs; if n even and x-a==n/2, coll has 1 not 2 -> fail
            if not ok or len(coll)!=2*len(A):
                continue
            A.append(x)
            if rec2(A, used|coll, x+1):
                return True
            A.pop()
        return found[0]
    r=rec2([0],set(),1)
    return (not r), nodes[0], time.time()-t0

def main():
    with open(os.path.join(HERE,"sidon_table.json")) as f:
        T=json.load(f)
    assert sorted(map(int,T.keys()))==list(range(31,56)), "missing n"
    total_nodes=0
    for ns in range(31,56):
        e=T[str(ns)]
        n=e["n"]; S=e["S"]; A=e["witness"]; ub=e["ub"]
        assert n==ns and len(A)==S and 0 in A and A==sorted(A), f"witness shape n={n}"
        assert all(0<=a<n for a in A)
        assert count_ub(n)==ub, f"ub mismatch n={n}"
        assert S<=ub, f"S>ub n={n}"
        assert is_sidon_sets(A,n), f"diff check failed n={n}"
        assert sums_ok(A,n), f"sums check failed n={n}"
        assert e["num_diffs"]==S*(S-1) and e["num_sums"]==S*(S+1)//2
        assert e["gap"]==(n-1)-S*(S-1)
        assert e["perfect"]==(S*(S-1)+1==n)
        if S==ub:
            print(f"n={n} S={S}=ub OK by counting bound (witness diffs+ sums verified)")
        else:
            assert S==ub-1, f"unexpected gap n={n}"
            # independent exhaustive proof that no ub-set exists
            ok,nd,dt=independent_no_k_set(n,ub)
            assert ok, f"INDEPENDENT SEARCH FOUND {ub}-set for n={n} -- table wrong!"
            total_nodes+=nd
            print(f"n={n} S={S}=ub-1 OK witness verified + independent exhaustive no-{ub}-set (nodes={nd} t={dt:.2f}s)")
        # k+1 also impossible by bound for S==ub; for S==ub-1, ub+1 impossible by bound too
        assert (ub+1)*ub+1>n, "bound sanity"
    print(f"ALL 25 CHECKS PASSED. Independent nonexistence nodes total={total_nodes}")

if __name__=="__main__":
    main()
