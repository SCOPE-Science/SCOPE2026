"""Stage A: class set of definite quaternion order disc 43 + Brandt T_2. GF(2) stability, exact lattices."""
import itertools
from fractions import Fraction
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf_c

def mul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-a1*b1-43*a2*b2-43*a3*b3,
            a0*b1+a1*b0+43*a2*b3-43*a3*b2,
            a0*b2+a2*b0-a1*b3+a3*b1,
            a0*b3+a3*b0+a1*b2-a2*b1)
def tr(a): return 2*a[0]
def nrd(a): return a[0]**2+a[1]**2+43*a[2]**2+43*a[3]**2
def conj(a): return (a[0],-a[1],-a[2],-a[3])
Z1=(Fraction(0),)*4
E=[(Fraction(1),Fraction(0),Fraction(0),Fraction(0)),
   (Fraction(0),Fraction(1),Fraction(0),Fraction(0)),
   (Fraction(1,2),Fraction(0),Fraction(1,2),Fraction(0)),
   (Fraction(0),Fraction(1,2),Fraction(0),Fraction(1,2))]
P=sp.Matrix([[sp.Rational(1),0,sp.Rational(1,2),0],[0,1,0,sp.Rational(1,2)],[0,0,sp.Rational(1,2),0],[0,0,0,sp.Rational(1,2)]])
Pinv=P.inv()
def to_elt(n):
    nq=tuple(Fraction(int(v)) for v in n)
    return (nq[0]*E[0][0]+nq[1]*E[1][0]+nq[2]*E[2][0]+nq[3]*E[3][0],
            nq[0]*E[0][1]+nq[1]*E[1][1]+nq[2]*E[2][1]+nq[3]*E[3][1],
            nq[0]*E[0][2]+nq[1]*E[1][2]+nq[2]*E[2][2]+nq[3]*E[3][2],
            nq[0]*E[0][3]+nq[1]*E[1][3]+nq[2]*E[2][3]+nq[3]*E[3][3])
def to_n(q):
    v=Pinv*sp.Matrix([sp.Rational(x) for x in q])
    assert all(sp.simplify(v[i]).is_integer for i in range(4)), (q,v)
    return tuple(int(v[i]) for i in range(4))
def left_mul_quat(a):
    M=sp.zeros(4,4)
    for j in range(4):
        q=[Fraction(0)]*4; q[j]=Fraction(1); q=tuple(q)
        p=mul(a,q)
        for i in range(4): M[i,j]=sp.Rational(p[i])
    return M
def left_action_n(a): return (Pinv*left_mul_quat(a)*P).applyfunc(sp.simplify)
def right_action_n(a):
    # right mult by a on O in n-coords
    M=sp.zeros(4,4)
    for j in range(4):
        q=list(to_elt([int(k==j) for k in range(4)]))
        p=mul(tuple(q),a)
        v=Pinv*sp.Matrix([sp.Rational(x) for x in p])
        for i in range(4): M[i,j]=sp.simplify(v[i])
    return M

GENS_N=[(0,1,0,0),(0,0,1,0),(0,0,0,1)]
ACTS=[left_action_n(to_elt(g)) for g in GENS_N]
ACTS_MOD2=[]
for A in ACTS:
    G=[[int(A[i,j])%2 for j in range(4)] for i in range(4)]
    ACTS_MOD2.append(G)
def matvec_mod2(G,v): return tuple(sum(G[i][j]*v[j] for j in range(4))%2 for i in range(4))

# 2-dim subspaces of F2^4 containing... enumerate all 2-dim subspaces (35)
def all_2planes():
    planes=set()
    vecs=[v for v in itertools.product([0,1],repeat=4) if any(v)]
    for a in vecs:
        for b in vecs:
            if b==a: continue
            # span
            s=tuple(sorted({(0,0,0,0),a,b,tuple((a[i]+b[i])%2 for i in range(4))}))
            # check b not multiple of a (over F2 multiples are only a itself)
            if tuple((a[i]+b[i])%2 for i in range(4))==(0,0,0,0): continue
            planes.add(s)
    return sorted(planes)
planes=all_2planes()
print("num 2-planes:",len(planes))
stable=[]
for S in planes:
    ok=True
    for G in ACTS_MOD2:
        for v in S:
            if matvec_mod2(G,v) not in S:
                ok=False; break
        if not ok: break
    if ok: stable.append(S)
print("stable 2-planes:",len(stable))
for S in stable: print("  ",S)

# HNF helpers (integer row lattices)
def row_hnf(gens):
    M=sp.Matrix([[int(v) for v in g] for g in gens])
    return hnf_c(M.T).T
def hnf_det(H):
    d=1
    for i in range(min(H.rows,H.cols)): d*=abs(int(H[i,i]))
    return d
def in_lattice(H,v):
    Hm=sp.Matrix(H); vv=sp.Matrix([sp.Rational(x) for x in v])
    try: c=Hm.LUsolve(vv)
    except Exception: return False
    return all(sp.simplify(c[i]).is_integer for i in range(c.rows))
def dual_basis(H):
    # dual w.r.t. standard dot product: rows of H^{-T}
    B=sp.Matrix(H)
    return (B.inv().T)
def lattice_sum(H1,H2):
    return row_hnf(list(H1.tolist())+list(H2.tolist()))
def lattice_intersect(H1,H2):
    D1=dual_basis(H1); D2=dual_basis(H2)
    S=row_hnf((D1.col_join(D2)).tolist())
    return dual_basis(S)
def scale_lattice(H,s):
    return (sp.Matrix(H)*sp.Rational(s))
def to_int_hnf(H):
    # H rational full-rank: clear denominators -> integer HNF of same lattice? only if H already integral span... use: Hn = HNF of num lattice then divide
    dens=[sp.Rational(H[i,j]).q for i in range(H.rows) for j in range(H.cols)]
    L=1
    for d in dens: L=L*d//sp.gcd(L,d)
    HI=row_hnf([[int(sp.Rational(H[i,j])*L) for j in range(H.cols)] for i in range(H.rows)])
    return (HI, L)

HO=row_hnf([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
H2O=row_hnf([[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]])
print("idx 2O:",hnf_det(H2O))

def ideal_from_plane(S):
    # preimage in O of S under O -> O/2O
    gens=[[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]]
    for v in S:
        if any(v): gens.append(list(v))
    return row_hnf(gens)

def right_order(H):
    # {x in B : H*x subset H}; search in (1/2)O first? denominators bounded: use (1/4)O to be safe then verify maximality via disc
    # condition: for each row-generator g (quat), g*x in lattice(H)
    gens=[tuple(sp.Rational(H[i,j]) for j in range(4)) for i in range(H.rows)]
    # unknown x = sum t_k E_k, t in Q^4; condition: to_n(g*x)... use n-coords: right action matrices
    conds=[]
    for g in gens:
        gq=to_elt([int(v) for v in g]) if all(sp.simplify(v).is_integer for v in g) else None
        # general: right mult by x as linear map on quat coords; convert
        pass
    return None

# right order via direct rational linear algebra on n-coordinate denominator-bounded search:
# x in (1/2)O: t in (1/2)Z^4; conditions g*x in H for 4 HNF-diagonal generators g of I.
def right_order_search(H,den=2):
    Hm=H
    # generators of I as quat elements
    Igens=[to_elt([int(H[i,j]) for j in range(4)]) for i in range(H.rows)]
    sols=[]
    rng=range(-den*3,den*3+1)
    for t in itertools.product(rng,repeat=4):
        x=add4(*[scale4(E[k],Fraction(t[k],den)) for k in range(4)])
        ok=True
        for g in Igens:
            p=mul(g,x)
            if not in_O(p):
                ok=False; break
            if not in_lattice(Hm,to_n(p)):
                ok=False; break
        if ok: sols.append(tuple(Fraction(v,den) for v in t))
    return sols
def add4(*vs):
    r=[Fraction(0)]*4
    for v in vs:
        for i in range(4): r[i]+=v[i]
    return tuple(r)
def scale4(v,s): return tuple(x*s for x in v)
def in_O(p):
    try: to_n(p); return True
    except Exception: return False

for S in stable:
    H=ideal_from_plane(S)
    print("plane",S,"index:",hnf_det(H))
    sols=right_order_search(H,den=2)
    print("  right-order elts (den 2, box):",len(sols))
