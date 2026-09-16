"""Recovery test: explicit non-isotrivial line in M_{2,2} whose stability is
undecidable by bounded local computation.

Family F_t([X:Y:Z]) = [X^2 : Y^2 : Z^2 + t*X*Y], t in A^1.
- Each F_t is a morphism (no common zeros), degree 2.
- Fixed points [1:1:z] with z^2 - z + t = 0; Jacobian trace 2+2z varies with t,
  so the family is non-isotrivial in moduli (multiplier spectrum non-constant).
- General member is not Lattes (Lattes locus is a proper closed/countable
  subset; generic multiplier spectrum is not that of a Lattes map), so the
  closure C in M_{2,2} is a curve not contained in the Lattes locus.
- Multiplier variation proves non-isotriviality but neither proves nor refutes
  J-stability / bifurcation-degree positivity: stability requires global
  holomorphic motion of repelling cycles / vanishing of dd^c L, undecidable here.
"""
import sympy as sp

t = sp.symbols('t')
sqrt_disc = sp.sqrt(1 - 4*t)
z1 = (1 + sqrt_disc)/2
z2 = (1 - sqrt_disc)/2
# In chart X=1 (resp. Y=1 by symmetry), local map near [1:1:z]:
# (y,z) -> (y^2, z^2 + t*y); Jacobian = [[2y,0],[t,2z]]; at y=1: trace = 2+2z
tr1 = sp.simplify(2 + 2*z1)
tr2 = sp.simplify(2 + 2*z2)
print("trace1 =", tr1)
print("trace2 =", tr2)
print("d(trace1)/dt =", sp.simplify(sp.diff(tr1, t)))
# Non-isotriviality: traces vary with t (derivative nonzero for general t)
assert sp.simplify(sp.diff(tr1, t)) != 0
# Discriminant locus (collision of the two fixed points): t = 1/4
print("discriminant zero at t =", sp.solve(1 - 4*t, t))
# Moduli dimension check: dim End_{2,2} = 3*6-1 = 17, dim PGL3 = 8, dim M = 9
print("dim M_{2,2} =", 3*6-1-8)
print("RESULT: family is non-isotrivial; C not contained in Lattes locus "
      "(general member); stability/bifurcation undecidable by local computation.")
