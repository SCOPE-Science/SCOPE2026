#!/usr/bin/env python3
"""Independent verifier: re-derives every claim in orbit_table.jsonl from scratch.

Independent = separate code path (own bases/rank/Tutte/orbit routines, own pivot),
reading only the 'blocks' columns of each row and asserting all other columns.
Also replays: global PG(3,2) lemma, U(2,5) nonrepresentability, quadric witness.
Exit nonzero on ANY mismatch. stdlib only.
"""
import itertools, json, sys

N, R = 9, 4
G = list(range(N))
S9 = 362880

fails = []
def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)

def bases(blocks):
    nb = set()
    for b in blocks:
        for q in itertools.combinations(sorted(b), R):
            nb.add(frozenset(q))
    return frozenset(frozenset(q) for q in itertools.combinations(G, R)
                     if frozenset(q) not in nb)

def rk(S, B):
    S = set(S)
    return max(len(S & set(b)) for b in B)

def tutte(B, ground, first):
    memo = {}
    def rec(g, bs):
        k = (g, bs)
        if k in memo: return memo[k]
        if not g: return {(0,0):1}
        e = g[0] if first else g[-1]
        rest = tuple(x for x in g if x != e)
        ina = any(e in b for b in bs)
        if not ina: r = {(i,j+1):c for (i,j),c in rec(rest,bs).items()}
        elif all(e in b for b in bs):
            r = {(i+1,j):c for (i,j),c in rec(rest,frozenset(b-{e} for b in bs)).items()}
        else:
            d1 = rec(rest, frozenset(b for b in bs if e not in b))
            d2 = rec(rest, frozenset(b-{e} for b in bs if e in b))
            r = dict(d1)
            for kk,vv in d2.items(): r[kk] = r.get(kk,0)+vv
        memo[k]=r; return r
    return rec(tuple(ground), frozenset(B))

rows = [json.loads(l) for l in open("output/artifacts/orbit_table.jsonl")]
check(len(rows) == 18, f"row count == 18 (got {len(rows)})")
seen_all = set()
names = set()
for r in rows:
    name, bl = r["name"], [tuple(sorted(b)) for b in r["blocks"]]
    names.add(name)
    B = bases(bl)
    check(len(B) == r["n_bases"] == r["T11"], f"{name}: nbases/T11")
    # exchange (independent loop order)
    ok = True
    Bl = list(B); S = set(B)
    for x1 in Bl:
        for x2 in Bl:
            for e in x1 - x2:
                if not any((x1-{e})|{f} in S for f in x2-x1): ok=False
    check(ok, f"{name}: basis exchange")
    check(rk(G,B)==4, f"{name}: rank 4")
    # triple axiom + hyperplane recovery
    H = set()
    good = True
    for t in itertools.combinations(G,3):
        if sum(1 for b in bl if set(t)<=set(b))>1: good=False
        if rk(t,B)==3:
            cl = frozenset(set(t)|{e for e in G if e not in t and rk(set(t)|{e},B)==3})
            H.add(cl)
    check(good, f"{name}: pairwise block intersection <=2")
    big = sorted(sorted(h) for h in H if len(h)>=4)
    check(big==sorted(list(b) for b in [sorted(x) for x in bl]), f"{name}: block recovery")
    check(sum(1 for h in H if len(h)==3)==r["n_hyperplanes_small"], f"{name}: small-hyperplane count")
    # orbit: enumerate images, lex-least, stabilizer
    key0 = tuple(sorted(tuple(sorted(b)) for b in bl))
    imgs = set(); least = key0
    for p in itertools.permutations(G):
        k = tuple(sorted(tuple(sorted(p[e] for e in b)) for b in bl))
        imgs.add(k)
        if k<least: least=k
    check(key0==least, f"{name}: lex-least representative")
    check(len(imgs)==r["orbit_size"], f"{name}: orbit size {len(imgs)}")
    check(r["orbit_size"]*r["stabilizer_order"]==S9, f"{name}: orbit-stabilizer")
    check(imgs.isdisjoint(seen_all), f"{name}: disjoint from previous orbits")
    seen_all |= imgs
    # tutte, pivots swapped vs census (census max-first here first, etc.)
    p1 = tutte(B,G,True); p2 = tutte(B,G,False)
    check(p1==p2, f"{name}: pivot agreement")
    check(sorted([[i,j,c] for (i,j),c in p1.items()])==sorted(r["tutte_poly"]), f"{name}: tutte poly")
    ev = lambda p,x,y: sum(c*x**i*y**j for (i,j),c in p.items())
    check(ev(p1,1,1)==r["T11"] and ev(p1,2,1)==r["T21"] and ev(p1,1,2)==r["T12"], f"{name}: T evals")
    check(ev(p1,2,1)==130+len(B), f"{name}: T21 identity")
    nsp = sum(1 for k in range(N+1) for s in itertools.combinations(G,k) if rk(s,B)==4)
    check(nsp==r["T12"], f"{name}: T12 spanning identity")
    # U25 witness replay
    C,E,D = r["U25_contract"],r["U25_ground"],r["U25_delete"]
    check(sorted(set(G)-set(C)-set(E))==sorted(D), f"{name}: witness partition")
    rc = lambda X: rk(set(X)|set(C),B)-2
    check(rk(C,B)==2 and rc(E)==2, f"{name}: witness rank")
    check(all(rc([a,b])==2 for a,b in itertools.combinations(E,2)), f"{name}: witness pairs")
    check(all(rc(list(t))==2 for t in itertools.combinations(E,3)), f"{name}: witness triples")

# global lemmas replay
n=0
for S in itertools.combinations(range(1,16),9):
    if all((a^b^c)!=0 for a,b,c in itertools.combinations(S,3)): n+=1
check(n==0, "global: no triple-independent 9-set of F2^4\\{0}")
for q in (2,3):
    found=False
    for A in itertools.product(range(q),repeat=6):
        cols=[(1,0),(0,1),(A[0],A[1]),(A[2],A[3]),(A[4],A[5])]
        if all((cols[i][0]*cols[j][1]-cols[i][1]*cols[j][0])%q!=0
               for i,j in itertools.combinations(range(5),2)): found=True; break
    check(not found, f"global: U(2,5) not representable over GF({q})")
# quadric witness
def r3(M):
    M=[list(v) for v in M]; Rr,Cc,rr=len(M),4,0
    for c in range(Cc):
        piv=next((i for i in range(rr,Rr) if M[i][c]%3),None)
        if piv is None: continue
        M[rr],M[piv]=M[piv],M[rr]
        inv=pow(M[rr][c]%3,-1,3); M[rr]=[(x*inv)%3 for x in M[rr]]
        for i in range(Rr):
            if i!=rr and M[i][c]%3:
                f=M[i][c]%3; M[i]=[(a-f*b)%3 for a,b in zip(M[i],M[rr])]
        rr+=1
    return rr
Z=[(0,0,1,1),(0,0,1,2),(0,1,0,1),(0,1,0,2),(1,0,0,1),(1,0,0,2),(1,1,1,0),(1,1,2,0),(1,2,1,0),(1,2,2,0)]
W=Z[:9]
check(r3(W)==4 and all(r3(list(t))==3 for t in itertools.combinations(W,3)), "global: quadric 9-set paving rank-4")
big=[sorted(q) for q in itertools.combinations(range(9),4) if r3([W[i] for i in q])==3]
check(len(big)>=3, f"global: witness has >=3 large blocks ({len(big)})")
print("FAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
