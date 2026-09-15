"""Affine Weyl group of type G2 (triangle group (2,3,6)) and Kazhdan-Lusztig polynomials.
Realization: W_aff = Q \rtimes W0 acting on coweight/root lattice; simple reflections s0,s1,s2.
We realize W_aff faithfully as affine transformations x -> Mx + b on Z^2 (root lattice coords).
s1,s2 linear as before; s0 = reflection in highest-root hyperplane: s0(x) = s_{theta}(x) + theta^v-ish.
For G2: highest root theta = 3a1+2a2 (long? 3a1+2a2). s0(x) = x - (<x,theta^v>-1) theta? In root-lattice coords need coroot pairing.
Let's construct via standard alcove geometry: use Cartan + coweights.
Simpler certified route: use Coxeter presentation (m01=6? m02=2? m12=6?) Need correct diagram for affine G2.
Affine G2 diagram: 0 connected to 1? Standard: extended node attaches to the short root? G2 affine diagram: triple bond 1-2, with 0 single-bonded to 1 (short root). So m01=3? m12=6, m02=2.
Verify: affine G2 Coxeter: s0-s1 triple? Hmm. Let's recall: G2 Dynkin: 1(triple)2 with arrow to short. Extended: 0 - 1(triple) 2 with 0-1 single? Then m01=3, m12=6, m02=2.
We implement generic KL recursion for ANY Coxeter group from presentation: list elements by BFS with rewriting using braid + quadratic (Matsumoto word problem via confluent rewriting is nontrivial). Instead realize group faithfully as matrices and define length via alcove distance (number of separating hyperplanes), Bruhat via... To keep certificate elementary, implement KL via Soergel-theoretic recursion using only Coxeter data with a faithful reflection representation and standard algorithms:
 - enumerate ball by acting on base alcove (permutations of alcoves),
 - length = gallery distance,
 - left descents from wall positions,
 - Bruhat order via subword property on ONE chosen reduced word per element (plus full reduced-word graph via braid moves),
 - KL via classical recursion P_{x,w} using a descent s of w (needs mu coefficients; standard recursion requires Bruhat interval + all P).
This is standard and rigorous given faithful representation. Faithfulness: use geometric representation of Coxeter system (Tits cone) with exact arithmetic in Q(sqrt3)? For (2,3,6): cos(pi/6)=sqrt3/2. Use exact field Q(sqrt3) as pairs.
"""
from fractions import Fraction
import itertools

# Exact field Q(sqrt3): a + b*sqrt3
class E:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        if isinstance(o,int): o=E(o)
        return E(self.a+o.a,self.b+o.b)
    def __sub__(self,o):
        if isinstance(o,int): o=E(o)
        return E(self.a-o.a,self.b-o.b)
    def __neg__(self): return E(-self.a,-self.b)
    def __mul__(self,o):
        if isinstance(o,int): o=E(o)
        # (a+b s)(c+d s)=ac+3bd + (ad+bc)s
        return E(self.a*o.a+3*self.b*o.b, self.a*o.b+self.b*o.a)
    def __truediv__(self,o):
        if isinstance(o,int): o=E(o)
        # 1/(c+ds) = (c-ds)/(c^2-3d^2)
        d=o.a*o.a-3*o.b*o.b
        assert d!=0
        return self*E(o.a/d,-o.b/d)
    def __eq__(self,o):
        if isinstance(o,int): o=E(o)
        return self.a==o.a and self.b==o.b
    def __lt__(self,o):
        if isinstance(o,int): o=E(o)
        return float(self)<float(o)
    def __le__(self,o):
        if isinstance(o,int): o=E(o)
        return float(self)<=float(o)
    def __float__(self): return float(self.a)+float(self.b)*1.7320508075688772
    def __repr__(self): return f"({self.a}+{self.b}s)"
    def __hash__(self): return hash((self.a,self.b))

def build_affine_G2():
    # Geometric representation: simple roots alpha0,alpha1,alpha2 in R^2 with B matrix:
    # B_ii=1; B_ij=-cos(pi/m_ij). m12=6 -> -sqrt3/2; m01=3 -> -1/2; m02=2 -> 0.
    sqrt3b = E(0,Fraction(1,2))  # sqrt3/2
    B = [[E(1),E(-1,0)/2*-1 if False else None,None]]  # placeholder
    # B01 = -cos(pi/3) = -1/2 ; B12 = -cos(pi/6) = -sqrt3/2 ; B02 = 0
    B = [[E(1),E(Fraction(-1,2)),E(0)],
         [E(Fraction(-1,2)),E(1),E(0,Fraction(-1,2))],
         [E(0),E(0,Fraction(-1,2)),E(1)]]
    # reflections s_i(v) = v - 2 B(v,alpha_i) alpha_i ; represent matrices 2x2 over E in basis of simple roots? rank 3 form degenerate.
    # Instead act on weight space R^2 with chosen simple roots as vectors: take alpha1=(1,0), alpha2=(-3/2, sqrt3/2)? Standard G2: angle 150deg, length ratio sqrt3.
    # Let alpha1 = (1,0) (short), alpha2 = (-3/2, sqrt3/2) (long, |a2|^2=3). Check angle: dot=-3/2, |a1||a2|=sqrt3 -> cos=-sqrt3/2 -> 150deg ok.
    # Coroots: a1^v = 2a1/(a1,a1)=2a1; a2^v=2a2/3.
    # s1(x)=x-<x,a1^v>a1; s2(x)=x-<x,a2^v>a2 with standard dot product.
    # Represent as 2x2 over E.
    # dot products: use E entries.
    a1=(E(1),E(0)); a2=(E(Fraction(-3,2)),E(0,Fraction(1,2)))
    def dot(u,v): return u[0]*v[0]+u[1]*v[1]
    def smat(a, av):
        # s(x)_j = x_j - dot(x,av)*a_j
        # matrix columns: s(e_j) = e_j - dot(e_j,av) a
        e1=(E(1),E(0)); e2=(E(0),E(1))
        import copy
        cols=[]
        for e in [e1,e2]:
            c=dot(e,av)
            cols.append((e[0]-c*a[0], e[1]-c*a[1]))
        # rows: [[c1x,c2x],[c1y,c2y]]
        return ((cols[0][0],cols[1][0]),(cols[0][1],cols[1][1]))
    av1=(E(2),E(0))
    av2=(E(Fraction(-1,1)),E(0,Fraction(1,3)))*1 if False else None
    # a2^v = 2 a2/3 = (-1, sqrt3/3)
    av2=(E(-1),E(0,Fraction(1,3)))
    S1=smat(a1,av1); S2=smat(a2,av2)
    # s0: affine reflection x -> s_theta(x) + theta^v? theta=3a1+2a2? compute theta vector:
    th=(a1[0]*3+a2[0]*2, a1[1]*3+a2[1]*2)
    # theta long? |th|^2 =? 3a1+2a2 = (3-3, sqrt3)=(0,sqrt3), |th|^2=3. long root. th^v = 2th/3 = (0, 2sqrt3/3).
    thv=(th[0]/3*2 if False else None,None)
    thv=(th[0]*E(Fraction(2,3)), th[1]*E(Fraction(2,3)))
    # s_theta matrix:
    Sth=smat(th,thv)
    return (S1,S2,Sth,th,thv,a1,a2)

S1,S2,Sth,TH,THV,A1,A2 = build_affine_G2()
print("S1=",S1); print("S2=",S2); print("Sth=",Sth); print("theta=",TH)
# verify orders: S1^2, S2^2, (S1S2)^6, (Sth*S1)^3? m01 should be 3: (s0 s1)^3=1 where s0(x)=Sth x + THV.
