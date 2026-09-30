"""Springer fibre Euler number chi(B_0)=chi(Fl3)=6: Poincare poly + Weyl group."""
import sympy as sp
t = sp.symbols('t')
# Fl3 = P2-bundle over P1? Poincare: (1+t^2)(1+t^2+t^4)
P = (1+t**2)*(1+t**2+t**4)
Pexp = sp.expand(P)
print("P(Fl3) =", Pexp)
chi = Pexp.subs(t,1)
print("chi(Fl3) = P(1) =", chi)
assert chi == 6
# Bruhat cells indexed by S3: dims = lengths 0,1,1,2,2,3
lengths = [0,1,1,2,2,3]
print("Bruhat lengths:", lengths, "ncells =", len(lengths))
# Euler = ncells (each cell A^l contributes 1)
print("chi via Bruhat =", len(lengths))
# Weyl group order |S3| = 6
import math
print("|W(sl3)| = |S3| =", math.factorial(3))
# q-count check: |Fl3(Fq)| = (1+q)(1+q+q^2); at q=1 -> 6
q = sp.symbols('q')
Nq = (1+q)*(1+q+q**2)
print("|Fl3(Fq)| =", sp.expand(Nq), "-> at q=1:", Nq.subs(q,1))
assert Nq.subs(q,1) == 6
print("OK: chi(B_0) = chi(G/B) = 6.")
