"""Full triple census driver. Stdlib only, deterministic, seed 55 (no randomness).
Computes 56 canonical reps, runs Method A/B/C to n<=9 in parallel, asserts equality.
Writes counts.json/csv + profiles + wilf classes.
Usage: python3 census_all.py [--nmax 9] [--workers 32]
"""
import itertools, json, math, os, sys, time, hashlib
from multiprocessing import Pool

SEED = 55
NMAX = 9
WORKERS = 32
if "--nmax" in sys.argv:
    NMAX = int(sys.argv[sys.argv.index("--nmax")+1])
if "--workers" in sys.argv:
    WORKERS = int(sys.argv[sys.argv.index("--workers")+1])

# --- symmetry (self-contained, no import from sym.py to keep independence doc) ---
def rev(p): return tuple(reversed(p))
def comp(p):
    k=len(p); return tuple(k+1-x for x in p)
def inv(p):
    k=len(p); r=[0]*k
    for i,v in enumerate(p): r[v-1]=i+1
    return tuple(r)
FUNCS=(rev,comp,inv)
def canon_pair(p,q):
    seen={tuple(sorted((p,q)))}; stack=[(p,q)]; cur={(p,q)}
    while stack:
        a,b=stack.pop()
        for f in FUNCS:
            na,nb=f(a),f(b)
            key=tuple(sorted((na,nb)))
            if key not in seen:
                seen.add(key); cur.add((na,nb)); stack.append((na,nb))
    return min(tuple(sorted(x)) for x in cur)

def build_reps():
    S4=list(itertools.permutations([1,2,3,4]))
    raw=[(S4[i],S4[j]) for i in range(24) for j in range(i+1,24)]
    mp={}
    for p,q in raw:
        c=canon_pair(p,q)
        mp.setdefault(c,[]).append((p,q))
    reps=sorted(mp.keys())
    return reps, mp

# --- import method impls by exec (keep single file for replay simplicity, but
#     logic duplicated textually from methodA/B/C.py for independence audit) ---
# We import from the three files to avoid divergence; independence comes from
# their distinct implementations.
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from methodA import count_pair_A
from methodB import count_pair_B
from methodC import count_pair_C

def work_one(rep):
    p1,p2 = rep
    t0=time.time()
    cA, prof = count_pair_A(p1,p2,NMAX)
    tA=time.time()-t0
    t0=time.time()
    cB = count_pair_B(p1,p2,NMAX)
    tB=time.time()-t0
    t0=time.time()
    cC = count_pair_C(p1,p2,NMAX)
    tC=time.time()-t0
    ok = (cA==cB==cC)
    return {"rep": [list(p1),list(p2)], "counts": cA, "countsB": cB, "countsC": cC,
            "ok": ok, "tA": tA, "tB": tB, "tC": tC,
            "profile": {str(k): {str(k2):v2 for k2,v2 in v.items()} for k,v in prof.items()}}

if __name__=="__main__":
    print(f"seed={SEED} nmax={NMAX} workers={WORKERS}", flush=True)
    reps, mp = build_reps()
    print(f"reps={len(reps)} (expect 56)", flush=True)
    assert len(reps)==56, len(reps)
    # symmetry map size check
    assert sum(len(v) for v in mp.values())==276
    t0=time.time()
    with Pool(WORKERS) as pool:
        results = pool.map(work_one, reps)
    dt=time.time()-t0
    print(f"all done in {dt:.1f}s", flush=True)
    nfail = sum(1 for r in results if not r["ok"])
    print(f"failures: {nfail}", flush=True)
    for r in results:
        if not r["ok"]:
            print("MISMATCH", r["rep"], r["counts"], r["countsB"], r["countsC"], flush=True)
    # write outputs to work/ (driver) ; final copy to output/artifacts done later
    outdir = os.path.dirname(__file__)
    with open(os.path.join(outdir,"countsABC.json"),"w") as f:
        json.dump(results,f,indent=1,sort_keys=True)
    # csv
    with open(os.path.join(outdir,"counts.csv"),"w") as f:
        f.write("rep_p,rep_q,"+",".join(f"a{n}" for n in range(NMAX+1))+"\n")
        for r in results:
            p="".join(map(str,r["rep"][0])); q="".join(map(str,r["rep"][1]))
            f.write(p+","+q+","+",".join(map(str,r["counts"]))+"\n")
    # wilf clustering by vector
    from collections import defaultdict
    cl=defaultdict(list)
    for r in results:
        cl[tuple(r["counts"])].append(("".join(map(str,r["rep"][0]))+"_"+"".join(map(str,r["rep"][1]))))
    print(f"wilf classes (distinct vectors to n={NMAX}): {len(cl)}", flush=True)
    for vec,members in sorted(cl.items(), key=lambda x: (x[0],x[1])):
        print(f"  n9={vec[-1]:6d} size={len(members):2d} e.g. {members[:3]} vec={vec}", flush=True)
    # target check
    for r in results:
        key=("".join(map(str,r["rep"][0])), "".join(map(str,r["rep"][1])))
        if key in [(("1342"),("2143")),(("1432"),("2413"))]:
            print("TARGET-CLASS member:",key,r["counts"],flush=True)
    # sha
    import hashlib
    h=hashlib.sha256(open(os.path.join(outdir,"counts.csv"),"rb").read()).hexdigest()
    print("counts.csv sha256:",h,flush=True)
