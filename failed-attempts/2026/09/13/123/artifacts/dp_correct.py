"""Corrected DP: single-variable chain with weight, exploiting simplex symmetry.
State V_k[h] = int_{Dx_k(1)} Q^h, Q arbitrary fixed combination. Expand in t_k:
Q(t',t_k) = sum_{q=0}^{J} c_q(Q') t_k^q with c_q = elementary pieces of weight J-q.
Recursion: V_k[e] = sum over t_k-expansion terms (c_q t_k^q restricted to first k-1 vars
in Q') ... simplest correct recursion: use full K-variable Q-polys but integrate one
variable at a time.

Cleaner correct approach: work with symmetric Q-basis on the CURRENT count.
Let Q^{(k)} = power-sum basis in k variables (same exponent vectors). Then
Q^{(k)}_e(t',t_k) = sum_f C(e,f) (Q'_{e-f})(t') t_k^{A(e-f)}.
V_k[e] = sum_f C(e,f) int_{Dx_{k-1}} Q'_f u^{A+1}/(A+1)... with u=1-S':
V_k[e] = sum_f C(e,f)/(A+1) * W_{k-1}[f, A+1], W_{k}[h,r]=int Q^h u^r.
W_k[h,r] = sum_f C(h,f)/(A+r+1) * W_{k-1}[f, A+r+1].
Max needed r: A+r+1 chains up to WMAX+RMAX. Since W only decreases and r increases,
cap r at WMAX+RMAX? At top, I needs r=0 only: W_50[h,0] for W(h)<=18.
Recursion needs W_49[f, A+1], A+1<=19: W-decay bounds r: r <= 19 + (depth stuff).
Bound: r + W(f) <= WMAX + RMAX always (invariant: start r+W<=18; step: (A+r+1)+W(f) = r+1+W(h) <= WMAX+RMAX+1... need cap).
Simplest: track dict keyed (h, r) computed recursively with memo + quadrature-free
base W_0[h,r] = delta_{h,0} (point mass 1). Max r encountered: A+r+1 with r<=20ish
and A<=18: <= 39. W(f)<=18. Enumerate pairs (h with W<=18, r<=40). Transitions to
(f, A+r+1) with W(f)+A+r+1 = W(h)+r+1. So S(h,r)=W(h)+r grows by 1 each level;
starting (h,0)@k=50 with W<=18: after 50 levels S<=68. Enumerate all (h, r) with
W(h)+r <= 68? That's 1410 * ~50 = 70k states x transitions — fine but W_0 base gives
Kronecker: actually W_0[h,r]=0 unless h=0. DP from k=0 up: only reachable states matter.
Simpler: bottom-up over k keeping dict {(h,r): val} only for needed keys, computed
via children from previous k. Let's just do memoized recursion top-down with exact
Fraction-free float; depth 50, branching moderate. Total distinct (k,h,r): 50*1410*~40
worst case 2.8M * avg branching — too slow in Python. Bottom-up dict is better:
needed[k] = set of (h,r) at level k. needed[50] = {(h,0)}. children: (f, A+r+1).
Then evaluate k=0..50 bottom-up only on needed sets. Branching total = sum over needed
of subterms. Should be OK.
"""
import numpy as np, math, itertools

K=50; WMAX=18
def enum_vecs(W):
    vecs=[]
    def rec(j,rem,cur):
        if j>9: vecs.append(tuple(cur)); return
        for e in range(rem//j+1):
            cur.append(e); rec(j+1,rem-j*e,cur); cur.pop()
    rec(1,W,[])
    return vecs
vecs=enum_vecs(WMAX)
Eidx={v:i for i,v in enumerate(vecs)}
E=len(vecs)
W=np.array([sum((j+1)*v[j] for j in range(9)) for v in vecs])
from math import comb
# subterms per h: list of (f, C, A)
subs=[]
for e in vecs:
    L=[]
    for f in itertools.product(*[range(x+1) for x in e]):
        c=1
        for j in range(9): c*=comb(e[j],f[j])
        A=sum((jj+1)*(e[jj]-f[jj]) for jj in range(9))
        L.append((Eidx[f],c,A))
    subs.append(L)

from fractions import Fraction
# needed sets bottom-up: need_at[k] for k=0..50
need_at=[set() for _ in range(K+1)]
for h in range(E):
    need_at[K].add((h,0))
for k in range(K,0,-1):
    for (h,r) in need_at[k]:
        for (f,c,A) in subs[h]:
            need_at[k-1].add((f,A+r+1))
print("needed sizes:", [len(s) for s in need_at][:6], "...", [len(s) for s in need_at][-3:])
print("total:", sum(len(s) for s in need_at))

lg=np.vectorize(math.lgamma)
def beta1(A,r):  # 1/(A+r+1) * ... no: factor C/(A+r+1); Beta not needed (u-power integrates directly)
    return 1.0/(A+r+1)
# bottom-up values
val=[{} for _ in range(K+1)]
for (h,r) in need_at[0]:
    val[0][(h,r)]=1.0 if h==Eidx[(0,)*9] else 0.0
for k in range(1,K+1):
    d={}
    for (h,r) in need_at[k]:
        s=0.0
        for (f,c,A) in subs[h]:
            s+=c*val[k-1][(f,A+r+1)]/(A+r+1)
        d[(h,r)]=s
    val[k]=d
    if k in (1,2,3,5,50):
        e0=Eidx[(0,)*9]; e1=Eidx[tuple([1]+[0]*8)]
        print("k=%d vol=%.10e (want %.10e)  intp1=%.10e (want %.10e)" % (
            k, d.get((e0,0), float('nan')), math.exp(-sum(math.log(i) for i in range(1,k+1)) if k>0 else 0),
            d.get((e1,0), float('nan')), math.factorial(1)/math.factorial(k+1)))
        print("   has (e0,0):", (e0,0) in d, " sample keys:", list(d)[:5])
import pickle
pickle.dump({"vecs":vecs,"val50":val[50],"val49":val[49]}, open("output/artifacts/dp_corr.pkl","wb"))
print("saved dp_corr.pkl")
