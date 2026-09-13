"""Full JPPZ evaluation for (g,n)=(2,4), r=k=7, legs a=(4,5,6,6), x-scale 7.
Computes T = int_{Mbar24} eps_*Ch^{[7]} / prod(1-mu_i psi_i), mu=(3,2,1,1),
as sum over stable graphs with 0..3 edges (dim count: only Gamma with
codim<=5 contribute since we need total degree 5=dim Mbar24; codim=#edges).
Strategy per graph: expand vertex/leg exponentials (kappa, psi powers) and edge factors
to needed degree; integrate over product of Mbar_{g_v,n_v} via psi engine + kappa->psi pushforward
(kappa_m(v) = pi_*(psi_{n_v+1}^{m+1}) on Mbar_{g_v,n_v+1}); edge xi_* insertions distribute
psi powers to the two branches. Denominator prod_i 1/(1-mu_i psi_i) expands as geometric series
in leg psis. Automorphism factors and r^{2g-1-h1} included. Weightings summed explicitly mod 7.
"""
from fractions import Fraction
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi

R=7; K=7; X=7
A=(4,5,6,6); MU=(3,2,1,1)
DIM=5

def bern(m):
    a=[Fraction(0)]*(m+1); a[0]=Fraction(1)
    for mm in range(1,m+1):
        s=sum(a[k]*Fraction(F(mm+1),F(k)*F(mm+1-k)) for k in range(mm))
        a[mm]=-s/Fraction(mm+1)
    return a[m]
def Bp(n,x):
    from math import comb as C
    return sum(Fraction(C(n,k))*bern(k)*(x**(n-k)) for k in range(n+1))

M=6
CV={m: -(((-1)**(m-1)))*Bp(m+1,Fraction(K,R))/(m*(m+1))*X for m in range(1,M+1)}
CL={a: {m: (((-1)**(m-1)))*Bp(m+1,Fraction(a,R))/(m*(m+1))*X for m in range(1,M+1)} for a in set(A)}
CE={w: {m: (((-1)**(m-1)))*Bp(m+1,Fraction(w,R))/(m*(m+1))*X for m in range(1,M+1)} for w in range(R)}

# ---- graph enumeration (labelled legs 0..3) ----
# graph: vertices list of (genus, legs tuple); edges list of ((v1,slot),(v2,slot)) with branch slots distinguished
graphs=[]
def add(vgen, legs, edges, aut):
    graphs.append({"v":list(vgen),"legs":[tuple(L) for L in legs],"e":list(edges),"aut":aut})
add([2],[(0,1,2,3)],[],1)
# 1-edge sep
seen=set()
for mask in range(1,(1<<4)-1):
    I1=tuple(i for i in range(4) if mask>>i & 1); I2=tuple(i for i in range(4) if not mask>>i & 1)
    if 0 not in I1: continue
    for g1 in range(3):
        for g2 in range(3):
            if g1+g2!=2: continue
            n1,n2=len(I1)+1,len(I2)+1
            if 2*g1-2+n1<=0 or 2*g2-2+n2<=0: continue
            # aut: swap iff identical (genus,legset)
            aut=1
            add([g1,g2],[I1,I2],[((0,0),(1,0))],aut)
# 1-edge nonsep loop
add([1],[(0,1,2,3)],[((0,0),(0,1))],2)
print("n graphs (0/1-edge):",len(graphs))

# weightings: for each graph, loops: w in 0..6 (edge (w, -w)); sep edge: w on side0 determined by vertex condition.
def weightings(gr):
    v=gr["v"]; legs=gr["legs"]; edges=gr["e"]
    nv=len(v)
    # unknowns: one w per edge-half on side of vertex 0 endpoint... parametrize: for each edge choose w_h (value at first-listed half), other = -w_h.
    # vertex condition: sum(legs a) + sum(incident half values) + K*(2g_v-2+n_v) = 0 mod R, n_v = #halves at v.
    # K=0 mod 7 simplifies.
    res=[]
    E=len(edges)
    for wv in itertools.product(range(R), repeat=E):
        # half values dict (v,slot)->val
        hv={}
        for e,(h1,h2) in zip(wv,edges):
            hv[h1]=e; hv[h2]=(-e)%R
        ok=True
        for vi in range(nv):
            s=sum(A[l] for l in legs[vi])+sum(val for (vv,sl),val in hv.items() if vv==vi)
            if s%R!=0: ok=False; break
        if ok: res.append(dict(hv))
    return res

for gr in graphs:
    print(gr, "#w=",len(weightings(gr)))
