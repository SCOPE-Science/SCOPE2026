"""Micro-test 2: reduction loop trace + cancellation-aware benchmark."""
P = 32003
def E(*v):
    return tuple(v)
f1 = {E(1,0,0,1,0): 1, E(0,2,0,0,0): P - 1}
f2 = {E(1,0,0,0,1): 1, E(0,1,1,0,0): P - 1}
f3 = {E(0,1,0,0,1): 1, E(0,0,1,1,0): P - 1}
GB = [f1, f2, f3]
LTs = [E(1,0,0,1,0), E(1,0,0,0,1), E(0,1,0,0,1)]
# trace reduction of a single monomial t = a^1 b^2 d^1 e.g.
D = {E(2,0,0,2,0): 1}
def divmod_term(t, lt):
    if all(t[k] >= lt[k] for k in range(5)):
        return tuple(t[k] - lt[k] for k in range(5))
    return None
def one_step(D):
    for t in list(D):
        for gi, lt in enumerate(LTs):
            q = divmod_term(t, lt)
            if q is not None:
                return t, gi, q
    return None
hit = one_step(D)
print("first hit:", hit, flush=True)
# Now: reduce S(0,1) = e*f1 - d*f2 = -e b^2 + d b c manually:
# e*f1 = ade - b^2 e; d*f2 = ade - bcd; S = bcd - b^2 e.
S = {E(0,1,1,1,0): 1, E(0,2,0,0,1): P - 1}
print("S(0,1) =", S, flush=True)
# term bcd = (0,1,1,1,0): divisible by LT of f3=(0,1,0,0,1)? needs e: no. by f1? needs a: no. by f2? needs a: no.
# term b^2 e = (0,2,0,0,1): divisible by f3? (0,2,0,0,1)-(0,1,0,0,1)=(0,1,0,0,0). yes.
# reduce: b^2 e -> b*(cd) [since f3: be = cd]. gives bcd - bcd = 0. So S reduces in ONE step.
# Verify:
q = divmod_term(E(0,2,0,0,1), LTs[2])
print("q =", q, flush=True)
G = GB[2]
DD = dict(S)
t = E(0,2,0,0,1); lc = DD.pop(t)
for tt, c in G.items():
    u = tuple(tt[k]+q[k] for k in range(5))
    DD[u] = (DD.get(u,0) - lc*c) % P
    if DD[u]==0: del DD[u]
print("after one step:", DD, flush=True)
print("CONCLUSION: S(0,1) reduces in 1 step; the generic loop must be fine.", flush=True)
print("So why 2001 steps? Check: maybe divisor choice hits t with q and G has 2 terms; fine.", flush=True)
# emulate loop exactly with dict iteration to find cycle: count distinct states?
import time
t0=time.time()
D = {E(0,1,1,1,0): 1, E(0,2,0,0,1): P - 1}
seen=set(); steps=0
while True:
    key = tuple(sorted(D.items()))
    if key in seen:
        print("CYCLE at step", steps, "size", len(D), flush=True); break
    seen.add(key)
    hit=None
    for t in D:
        for gi, lt in enumerate(LTs):
            qq = divmod_term(t, lt)
            if qq is not None:
                hit=(t,gi,qq); break
        if hit is not None: break
    if hit is None:
        print("TERMINATED at step", steps, D, flush=True); break
    t,gi,qq = hit; lc=D.pop(t)
    for tt,c in GB[gi].items():
        u=tuple(tt[k]+qq[k] for k in range(5))
        D[u]=(D.get(u,0)-lc*c)%P
        if D[u]==0: del D[u]
    steps+=1
    if steps>50:
        print("NO TERMINATION in 50 steps; |D|=",len(D)," terms:",sorted(D.items()), flush=True); break
print("time", time.time()-t0, flush=True)
