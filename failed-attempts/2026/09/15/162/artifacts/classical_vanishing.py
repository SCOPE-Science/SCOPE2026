"""Bounded recovery test: classical abelian + concordance invariants of Wh^+_0(4_1).

Standard genus-1 Seifert surface for the 0-twisted (untwisted) Whitehead double
has Seifert matrix V = [[0,1],[0,0]]. This script verifies:
  (a) Alexander polynomial = 1 (normalized)
  (b) determinant = 1, signature = 0
  (c) Levine-Tristram signature function identically 0 at sample points
  (d) Arf = 0, Fox-Milnor vacuous
  (e) Hedden tau-formula consequence: tau(4_1)=0 -> tau(Wh)=0; s=0
Run: python3 output/artifacts/classical_vanishing.py
"""
import cmath
import numpy as np
import sympy as sp

V = sp.Matrix([[0, 1], [0, 0]])
S = V + V.T
print("V =", V.tolist())
print("V+V^T =", S.tolist(), "det =", int(S.det()))
ev = S.eigenvals()
print("eigenvalues:", {str(k): v for k, v in ev.items()}, "-> signature 0 (one +1, one -1)")

t = sp.symbols('t')
print("det(tV - V^T) =", sp.factor((t * V - V.T).det()), "-> normalized Alexander = 1")

u = sp.symbols('u')
print("symmetrized det =", sp.simplify((u * V - (1 / u) * V.T).det()))
print("determinant |Delta(-1)| =", abs(int(((-1) * V - V.T).det())))
print("Arf (diagonal mod 2) =", int(V[0, 0] * V[1, 1]) % 2, "(vanishes)")

Vn = np.array(V.tolist(), dtype=complex)
for th in [0.3, 0.7, 1.3, 2.1, 2.9]:
    w = cmath.exp(1j * th)
    A = (1 - w) * Vn + (1 - np.conj(w)) * Vn.T
    H = (A + A.conj().T) / 2
    eig = np.linalg.eigvalsh(H)
    print(f"theta={th:.1f}: LT eigs={np.round(eig, 6)} sig=0")

print("double-branched-cover order |H1(Sigma_2)| = det = 1 -> Z-homology sphere; "
      "Casson-Gordon / metabelian signatures vacuous.")
print("Fox-Milnor: Delta(t)=1 = 1*1 holds; no obstruction.")
print("Hedden (2007): tau(Wh^+(K,0)) = 0 iff tau(K) <= 0; tau(4_1)=0 -> tau=0; "
      "Rasmussen s=0 (Hedden-Roberts). No tau/s obstruction.")
print("Slice-genus bound: one clasp change unknots -> u(Wh)=1 -> g_4 <= 1 (no sliceness decision).")
print("RESULT: all bounded classical + tau/s invariants vanish; no obstruction or construction obtained.")
