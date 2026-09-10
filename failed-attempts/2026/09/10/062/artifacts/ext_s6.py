# H^5 at t = stem+5? No: H^{5,t} with t = stem+5 for stem 52..56 -> t=57..61.
# Need ker(d: C^5_t -> C^6_t) and im(d: C^4_t -> C^5_t).
# im rank: from ext_s5 run: rank values at t (domain C^4_t): t=56:403884, 57:370919, 58:337808, 59:304989, 60:272623.
# dimC5(t) from restricted_cobar: t=57:31270745 (too big for elimination).
# Strategy: only compute ker5 for smallest t first (t=57, stem 52): dimC5=31M -- infeasible in window.
# Instead compute Ext via known-structure cross-check: use h0/h1/h2-periodicity + vanishing line to bound cell,
# and directly search for FIRST nonzero (s,t) in stems 52-56 with s>=5 via May SS E1 degree reasons.
# May E1 for A(2): generators h_{i,j} with (s=1, t=2^j(2^i-1)): h10:(1,1)? degrees: |h10|=1? List:
# h10:t=1? h11:t=3? h12:t=7? h20:t=2? h21:t=6? h22:t=14? h30: t=4? h31: t=12? h32: t=28?
# Enumerate May monomials with stem 52..56 and minimal s; report candidates (upper bound on Ext rank).
from itertools import product
may=[("h10",1,1),("h11",1,3),("h12",1,7),("h20",1,2),("h21",1,6),("h22",1,14),("h30",1,4),("h31",1,12),("h32",1,28)]
# relations: h_{i,j}^2=0 for j=0? (exterior on h_i0); polynomial in others. Truncate exponents 0/1 for h_i0, 0..3 for others, total deg<=64.
sols={s: [] for s in [52,53,54,55,56]}
def rec(i, s, t, acc):
    if t>64: return
    if i==len(may):
        stem=t-s
        if stem in sols and s>=1: sols[stem].append((s,tuple(acc)))
        return
    name,ds,dt=may[i]
    maxe = 1 if name in ("h10","h20","h30") else 4
    for e in range(maxe+1):
        if t+e*dt>64: break
        rec(i+1, s+e, t+e*dt, acc+([e] if False else []))
    # store exponents
rec2_done=False
sols2={s: [] for s in [52,53,54,55,56]}
def rec2(i, s, t, acc):
    if t>64: return
    if i==len(may):
        stem=t-s
        if stem in sols2: sols2[stem].append((s,tuple(acc)))
        return
    name,ds,dt=may[i]
    maxe = 1 if name in ("h10","h20","h30") else 4
    for e in range(maxe+1):
        if t+e*dt>64: break
        acc.append(e); rec2(i+1,s+e*ds,t+e*dt,acc); acc.pop()
rec2(0,0,0,[])
for stem in [52,53,54,55,56]:
    cands=sorted(sols2[stem])
    print(f"stem {stem}: {len(cands)} May monomials; minimal s: {min(s for s,_ in cands) if cands else None}")
    for s,e in cands:
        if s<=8: print("   s=",s,"t=",s+stem,"exps(h10,h11,h12,h20,h21,h22,h30,h31,h32)=",e)
