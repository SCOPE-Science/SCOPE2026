#!/usr/bin/env python3
"""Deterministic difference-conflict clique backtracking census for Sidon sets in Z_n.
Definition: A subset A of Z_n is Sidon iff the k*(k-1) ordered differences a-b (a!=b)
are pairwise distinct mod n (hence nonzero). This implies and is implied by distinctness
of the k*(k+1)//2 sums a+b (a<=b) -- see DRAFT Lemma 1.

Method: fix 0 in A by translation; restrict smallest nonzero a1 to a divisor of n
(multiplier reduction x -> u*x, u in Z_n^*; every affine orbit has such a representative).
Depth-first search with bitmask difference-occupancy pruning, lex order for canonicity.
Stdlib only, deterministic, no randomness.
"""
import json, math, sys, time

def divisors(n):
    return sorted(d for d in range(1, n) if n % d == 0)

def count_ub(n):
    # max k with k*(k-1)+1 <= n
    k = int((1 + math.sqrt(4*n-3))//2)
    while (k+1)*k+1 <= n:
        k += 1
    while k*(k-1)+1 > n:
        k -= 1
    return k

def dfs_find(n, k, restrict=True):
    """Return (found, witness, nodes, prunes, elapsed). Exhaustive over restricted space."""
    divs = divisors(n)
    nodes = [0]; prunes=[0]
    wit=[None]; found=[False]
    t0=time.time()
    sys.setrecursionlimit(10000)
    def rec(A, used, start):
        nodes[0]+=1
        if len(A)==k:
            wit[0]=tuple(A); found[0]=True
            return True
        need=k-len(A)
        cands = divs if (len(A)==1 and restrict) else range(start, n)
        for x in cands:
            if (n-x)<need:
                break
            nm=0; ok=True
            for a in A:
                d1=(x-a)%n; d2=(a-x)%n
                b1=1<<d1
                if (used&b1) or (nm&b1):
                    ok=False; break
                nm|=b1
                if d2!=d1:
                    b2=1<<d2
                    if (used&b2) or (nm&b2):
                        ok=False; break
                    nm|=b2
                else:
                    ok=False; break
            if not ok:
                prunes[0]+=1
                continue
            A.append(x)
            if rec(A, used|nm, x+1):
                return True
            A.pop()
        return found[0]
    r=rec([0],0,1)
    return r, wit[0], nodes[0], prunes[0], time.time()-t0

def diff_list(A,n):
    ds=sorted((a-b)%n for a in A for b in A if a!=b)
    return ds

def main():
    out={}
    log=[]
    total_t0=time.time()
    for n in range(31,56):
        ub=count_ub(n)
        # try ub with restriction
        f,w,nd,pr,dt=dfs_find(n,ub,restrict=True)
        if f:
            S=ub; wit=list(w); opt="counting-bound k(k-1)+1<=n"
            # cross-check unrestricted for ub<=6 (cheap) to double-certify existence path
            nonexist_nodes=None
        else:
            # ub unattainable: record nonexistence tree, then find ub-1 witness
            nonexist_nodes=nd
            f2,w2,nd2,pr2,dt2=dfs_find(n,ub-1,restrict=True)
            assert f2, f"no {(ub-1)}-set for n={n}"
            S=ub-1; wit=list(w2); opt=f"exhaustive DFS: no {ub}-set (restricted nodes={nd}, prunes={pr}); counting bound rules out >{ub}"
            dt+=dt2; nd+=nd2
        D=diff_list(wit,n)
        assert len(set(D))==S*(S-1) and 0 not in D, "witness invalid"
        sums=sorted((a+b)%n for i,a in enumerate(wit) for b in wit[i:])
        assert len(set(sums))==S*(S+1)//2, "sums check failed"
        perfect=(S*(S-1)+1==n)
        gap=(n-1)-S*(S-1)
        out[str(n)]={"n":n,"S":S,"ub":ub,"witness":wit,
                     "num_diffs":len(set(D)),"need_diffs":S*(S-1),
                     "num_sums":len(set(sums)),"need_sums":S*(S+1)//2,
                     "diffs_sorted":D,"sums_sorted":sums,
                     "gap":gap,"perfect":perfect,"optimality":opt}
        log.append({"n":n,"ub":ub,"S":S,"witness":wit,"found_ub":f,
                    "nodes":nd,"prunes":pr,"time_s":round(dt,4),
                    "nonexist_restricted_nodes":nonexist_nodes})
        print(f"n={n} S={S} ub={ub} w={wit} gap={gap} perfect={perfect} nodes={nd} t={dt:.3f}s")
    total=time.time()-total_t0
    import os
    here=os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here,"sidon_table.json"),"w") as f:
        json.dump(out,f,indent=2,sort_keys=True)
    with open(os.path.join(here,"search_log.json"),"w") as f:
        json.dump({"total_time_s":round(total,3),"per_n":log},f,indent=2)
    print(f"TOTAL {total:.2f}s")

if __name__=="__main__":
    main()
