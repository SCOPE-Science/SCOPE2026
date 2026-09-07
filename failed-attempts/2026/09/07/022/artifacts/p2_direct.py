#!/usr/bin/env python3
"""P2: independent direct checker via itertools.permutations.
For each n, iterate all n! perms, test all C(n,4) quads with generic
rank-tuple computation (sorting-based, INDEPENDENT of P1's lemma).
Reports counts for one class. Cross-checks P1 to n=8 (and n=9 if time).
"""
import sys, time, json, hashlib, itertools

def pat4(a,b,c,d):
    s = sorted((a,b,c,d))
    r = {v:i for i,v in enumerate(s)}
    return (r[a],r[b],r[c],r[d])

def count_direct(which, N, nmax=None):
    if which=='A':
        forb={(0,1,2,3),(0,2,3,1)}
    else:
        forb={(3,1,2,0),(3,0,1,2)}
    res={}
    for n in range(0, N+1):
        if nmax is not None and n>nmax:
            break
        if n<4:
            import math
            res[n]=math.factorial(n)
            print(f"[{which}-direct] n={n} count={res[n]} (trivial)", flush=True)
            continue
        t0=time.time()
        cnt=0
        quads=list(itertools.combinations(range(n),4))
        for p in itertools.permutations(range(n)):
            hit=False
            for (i,j,k,l) in quads:
                if pat4(p[i],p[j],p[k],p[l]) in forb:
                    hit=True; break
            if not hit:
                cnt+=1
        print(f"[{which}-direct] n={n} count={cnt} ({time.time()-t0:.1f}s)", flush=True)
        res[n]=cnt
    return res

if __name__=="__main__":
    which=sys.argv[1] if len(sys.argv)>1 else "A"
    N=int(sys.argv[2]) if len(sys.argv)>2 else 8
    t0=time.time()
    r=count_direct(which,N)
    dt=time.time()-t0
    print(json.dumps({"class":which,"counts":[r[i] for i in range(N+1)],"seconds":round(dt,2)}))
    print("checksum",hashlib.sha256(json.dumps([r[i] for i in range(N+1)]).encode()).hexdigest()[:16])
