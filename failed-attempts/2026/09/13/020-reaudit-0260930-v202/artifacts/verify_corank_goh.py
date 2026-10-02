"""Verify corank-3 abnormality, Goh degeneracy, and normal lift of exp(t X1)
in the free step-4 rank-2 Carnot group (growth vector (2,3,5,8)).

Hall basis order: [X1, X2, X12, X112, X212, X1112, X2112, X2212]
  X12=[X1,X2]; X112=[X1,X12]; X212=[X2,X12];
  X1112=[X1,X112]; X2112=[X2,X112]=[X1,X212] (Jacobi); X2212=[X2,X212].
Exact rational arithmetic (sympy). ad_X1^4 = 0 (step 4).
"""
import sympy as sp

names = ['X1', 'X2', 'X12', 'X112', 'X212', 'X1112', 'X2112', 'X2212']
n = 8
ad = sp.zeros(n)  # ad_X1: ad[i,j] = coeff of basis i in [X1, basis j]
ad[2, 1] = 1  # [X1,X2]   = X12
ad[3, 2] = 1  # [X1,X12]  = X112
ad[5, 3] = 1  # [X1,X112] = X1112
ad[6, 4] = 1  # [X1,X212] = X2112 (Jacobi: [X1,[X2,X12]]=[X2,[X1,X12]])
assert (ad**4).is_zero_matrix, "ad_X1 must be nilpotent of index <=4"

s, t = sp.symbols('s t')
ad2, ad3 = ad**2, ad**3
Epos = sp.eye(n) + s*ad + s**2/2*ad2 + s**3/6*ad3   # Ad_{exp(s X1)}
Eneg = sp.eye(n) - t*ad + t**2/2*ad2 - t**3/6*ad3   # Ad_{exp(-t X1)}

# ---- Endpoint-map image: span_s { Epos*X1, Epos*X2 }, s in [0,1] ----
sample = [sp.Rational(0), sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(1)]
rows = []
for sval in sample:
    M = Epos.subs(s, sval)
    rows.append(M[:, 0].T)
    rows.append(M[:, 1].T)
A = sp.Matrix.vstack(*rows)
rank = A.rank()
print("rank(dE image) =", rank)
assert rank == 5, rank
# columns X212(4), X2112(6), X2212(7) of A vanish -> image subset of the other 5
for j in (4, 6, 7):
    assert all(A[:, j][k] == 0 for k in range(A.rows)), j
print("image = span{X1,X2,X12,X112,X1112} exactly; corank =", n - rank)
assert n - rank == 3

# ---- Abnormal-lift space = left nullspace (annihilator of image) ----
ns = A.nullspace()
print("dim abnormal covector space =", len(ns))
assert len(ns) == 3
for k, v in enumerate(ns):
    H1 = sp.expand(v.dot(Eneg[:, 0]))  # p(t)(X1)
    H2 = sp.expand(v.dot(Eneg[:, 1]))  # p(t)(X2)
    G = sp.expand(v.dot(Eneg[:, 2]))   # p(t)([X1,X2]) = Goh entry
    assert H1 == 0 and H2 == 0, (k, H1, H2)
    assert G == 0, (k, G)
    print(f"abnormal basis vec {k}: H1={H1}, H2={H2}, Goh={G}")
print("All abnormal lifts satisfy H1=H2=0 and Goh matrix identically 0 (rank 0).")

# ---- Explicit normal lift p0 = X1^* ----
p0 = sp.zeros(n, 1)
p0[0] = 1
H1 = sp.expand(p0.dot(Eneg[:, 0]))
H2 = sp.expand(p0.dot(Eneg[:, 1]))
print("normal lift: H1 =", H1, ", H2 =", H2)
assert H1 == 1 and H2 == 0
print("Normal lift verified: u=(H1,H2)=(1,0) reproduces gamma*(t)=exp(t X1).")
print("ALL CHECKS PASSED: corank=3 (not 1); Goh rank 0; normal-abnormal (not strictly abnormal).")
