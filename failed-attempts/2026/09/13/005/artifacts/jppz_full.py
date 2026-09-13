"""Definitive route-(ii) evaluator via JPPZ Cor 4 for (g,n)=(2,4), r=k=7, legs a=(4,5,6,6), x=7.
For each stable graph: automorphisms, weighting sums mod 7, series expansion, exact psi/kappa integration.
Cross-checks: DL genus-1 d=1 case (must give 0), then the (2,7,(3,2,1,1)) target."""
from fractions import Fraction
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi

R=7; K=7; X=7
A=(4,5,6,6); MU=(3,2,1,1); DIM=5

def bern(m):
    a=[Fraction(0)]*(m+1); a[0]=Fraction(1)
    for mm in range(1,m+1):
        s=sum(a[k]*Fraction(F(mm+1),F(k)*F(mm+1-k)) for k in range(mm))
        a[mm]=-s/Fraction(mm+1)
    return a[m]
def Bp(n,x):
    from math import comb as C
    return sum(Fraction(C(n,k))*bern(k)*(x**(n-k)) for k in range(n+1))
M=9
CV={m: -(((-1)**(m-1)))*Bp(m+1,Fraction(K,R))/(m*(m+1))*X for m in range(1,M+1)}
def cl(a,m): return (((-1)**(m-1)))*Bp(m+1,Fraction(a,R))/(m*(m+1))*X
def ce(w,m): return (((-1)**(m-1)))*Bp(m+1,Fraction(w,R))/(m*(m+1))*X

def aut_order(gv, assign, edges):
    nv=len(gv); cnt=0; tot=0
    for perm in itertools.permutations(range(nv)):
        tot+=1
        if tuple(gv[perm[i]] for i in range(nv))!=(tuple(gv)): continue
        if tuple(perm[assign[l]] for l in range(len(assign)))!=tuple(assign): continue
        e2=sorted(tuple(sorted((perm[i],perm[j]))) for (i,j) in edges)
        if sorted(edges)==e2: cnt+=1
    return cnt

def h1(nv, edges): return len(edges)-nv+1

def weightings(gv, assign, edges, r=R):
    nv=len(gv); E=len(edges); out=[]
    for wv in itertools.product(range(r), repeat=E):
        hv={}
        for e,(i,j) in zip(wv,edges):
            # two half-edges: (eIdx,0)->e, (eIdx,1)->-e
            pass
        # build per-vertex incident sums with explicit half-edge indexing
        ok=True
        # halves: for edge q=(i,j): half q0 at i value w, half q1 at j value -w
        for v in range(nv):
            s=sum(A[l] for l in range(len(assign)) if assign[l]==v)
            for q,(i,j) in enumerate(edges):
                if i==v: s+=wv[q]
                if j==v: s-=wv[q]
            if s%r!=0: ok=False; break
        if ok: out.append(tuple(wv))
    return out

# series utilities: expansions in psi-leg powers, kappa powers per vertex, edge psi powers.
# Per graph+weighting, contribution = r^{2g-1-h1}/|Aut| * xi_*[ V * L * E ] where
# V = prod_v exp(sum_m CV[m] kappa_m(v)); L = prod_legs exp(sum_m cl(a_leg,m) psi_leg^m);
# E = prod_edges (1-exp(S_e))/(psi+psi'), S_e = sum_m ce(w,m)[psi_h^m-(-psi_h')^m].
# Total needed degree: deg(V)+deg(L)+deg(E') + #edges = DIM - (denominator psi degree d_denom); we expand
# 1/prod(1-mu_i psi_i) = sum mu_i^{p_i} psi_i^{p_i} and convolve: iterate p distributions with sum<=DIM.

def kappa_to_psi(g, nlegs, m, extra):
    """Integral of kappa_m(v) * prod psi^{extra} over Mbar_{g,nlegs}: = int_{Mbar_{g,nlegs+1}} psi_{new}^{m+1} prod psi^{extra}."""
    return psi(g, tuple(list(extra)+[m+1]))

def eval_graph(gv, assign, edges, wv, maxdeg=DIM):
    """Return dict {legpow_tuple: Fraction} = class xi_*(V L E) expanded, as polynomial in leg psis
    (legs indexed 0..3) times boundary pushforward; then integrate each monomial against denom series.
    Handles kappa_1.. only to needed degree via kappa->psi identity iteratively (kappa products via multiple new markings)."""
    nv=len(gv)
    nlegs_v=[sum(1 for l in range(4) if assign[l]==v) for v in range(nv)]
    # half-edge indexing: halves list per vertex: legs + edge-halves
    # For integration we need, per vertex, a psi-monomial on (legs + edge branches).
    # Enumerate exponent allocations up to maxdeg via recursion over factors.
    # Factors: for each vertex: kappa series; for each leg: psi series; for each edge: edge series (involving both branches).
    # Represent state: per-vertex dict {(kind,index): power}: legs ('leg',l), branches ('br',q,side), plus kappa multiset.
    # Brute force: iterate total-degree-bounded exponent tuples. Degrees: kappa_m:m, psi^m:m, edge piece deg>=1 (edge factor has overall 1/(psi+psi') so pieces have deg>=0 after expansion... careful).
    # Edge factor: (1-exp(S))/(x+y), S = sum_m c_m (x^m-(-y)^m), x=psi_h, y=psi_h'. Expand: = -S/(x+y) - S^2/2(x+y) - ...
    # Each S has min degree 1 (m=1 gives c(x+y) so S/(x+y) starts deg 0). So edge factor starts at degree 0 (constant = -c_1*... ). Expand to needed total.
    results={}  # key: (legpows tuple len4, per-vertex branch pows, per-vertex kappa tuple) -> coeff; then integrate.
    # Simpler: recursion over monomial choices.
    # Precompute series pieces:
    # leg series for leg l: {p: coeff} deg p<=maxdeg
    legser={}
    for l in range(4):
        a=A[l]; d={0:Fraction(1)}
        # exp(sum_m cl(a,m) t^m) truncated
        s={0:Fraction(1)}
        for m in range(1,M+1):
            c=cl(a,m)
            # multiply by exp(c t^m) = sum_j c^j t^{mj}/j!
            ns=dict(s)
            # actually do power-series exp properly below; here iterative:
            pass
        # direct: coefficient of t^p in exp(sum c_m t^m)
        coef={p:Fraction(0) for p in range(maxdeg+1)}; coef[0]=Fraction(1)
        # standard exp recursion: coef[p] = (1/p) sum_{m=1..p} m * ... no—use Bell: coef = exp; cdot: coef[p]=sum_{partitions} prod c_m^{e_m}/e_m!
        for p in range(1,maxdeg+1):
            tot=Fraction(0)
            # iterate exponent vectors via recursion
            def rec(m, rem, prod):
                global_tot=[Fraction(0)]
            tot=expcoef([cl(a,m) for m in range(1,M+1)], p)
            coef[p]=tot
        legser[l]=coef
    return legser

def expcoef(c, p):
    # coef of t^p in exp(sum_{m>=1} c_m t^m), c list 1-indexed
    if p==0: return Fraction(1)
    tot=Fraction(0)
    def rec(m, rem, prod, first=True):
        nonlocal tot
        if rem==0:
            tot+=prod; return
        if m>len(c)-1 or m>rem: return
        pw=Fraction(1)
        for e in range(0, rem//m+1):
            rec(m+1, rem-e*m, prod*pw//F(e) if e else prod)
            pw*=c[m-1] if m-1 < len(c) else Fraction(0)
    # fix indexing: c[m] for m>=1
    tot=Fraction(0)
    def rec2(m, rem, prod):
        nonlocal tot
        if rem==0: tot+=prod; return
        if m>len(c) or m>rem: return
        pw=Fraction(1)
        for e in range(rem//m+1):
            rec2(m+1, rem-e*m, prod*pw/Fraction(F(e)))
            pw*=c[m-1]
    rec2(1,p,Fraction(1))
    return tot

if __name__=="__main__":
    print(expcoef([Fraction(1),Fraction(1)],3))  # e^{t+t^2}: coef t^3 = 1/6+1+1=... check: e^t e^{t^2} = (1+t+t^2/2+t^3/6)(1+t^2+t^4/2): t^3: 1/6+1=7/6
