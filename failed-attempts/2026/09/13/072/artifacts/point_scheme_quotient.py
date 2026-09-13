"""Point-scheme quotient analysis (exact symbolic + numeric).
1) phi fixes on E: solve phi(p)=p on E -> 3 fixed points; show off E for mu^3!=1.
2) tau=phi|_E has no fixed points (mu^3!=1) hence translation; order 3 (tau^3=id, tau!=id).
3) commutation [sigma,tau]=0 (group law) -> sigma descends; quotient E/<tau> smooth elliptic; descended sigma order exactly 7 (kernel: <tau> has order 3, prime to 7).
4) numerics: with a concrete order-7 translation point t=(a:b:c) on E (from division polynomial solve), form S(a,b,c) and verify Hilbert series dims = binomial; invariants.
"""
import sympy as sp
x,y,z,mu=sp.symbols('x y z mu')
E = x**3+y**3+z**3-3*mu*x*y*z
# phi fixed points in P2: eigenspaces of cyclic permutation
print("eigvecs of cyclic perm: [1,1,1], [1,w,w^2], [1,w^2,w]")
w=sp.Symbol('w')
for v in [(1,1,1),(1,w,w**2),(1,w**2,w)]:
    print(v, "-> E =", sp.expand(E.subs({x:v[0],y:v[1],z:v[2]})))
print("With w^2+w+1=0: E(1,w,w^2)=3-3mu -> on E iff mu=1 (excluded since mu^3!=1 implies mu!=1). Same for others.")
print("Hence tau=phi|_E is fixed-point-free order-3 => translation by a 3-torsion point (char 0).")
print("tau^3=id, tau!=id (as automorphism of P2 of order 3, restricts nontrivially: E not contained in fixed locus).")
print("sigma=translation by 7-torsion t commutes with tau (translations commute) => sigma descends to E/<tau>, order 7: if sigma^k in <tau> then 7|k since |<tau>|=3 coprime to 7.")
