# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Resonant simplicity at q^2=-1 for principal series of the affine Hecke algebra of type G2, with an exact integral engine and certified KL data

## 1. Setting and conventions

Let H be the extended affine Hecke algebra of type G2 over C with equal parameter q, q = i (q^2 = -1),
quadratic relation (T_s - q)(T_s + 1) = 0, braid relation of length 6 for the finite simple reflections
s_1, s_2. Let A = C[theta_1^{+-1}, theta_2^{+-1}] be the Bernstein commutative subalgebra, where
theta_j = theta_{alpha_j}, alpha_1 short, alpha_2 long, Cartan matrix [[2,-1],[-3,2]].
The Bernstein relation used throughout is

  T_s theta_x = theta_{sx} T_s + (q-1)(theta_x - theta_{sx})/(1 - theta_{-alpha_s}).

For t = (t_1, t_2) in T = (C*)^2 let M(t) = H otimes_A C_t be the principal series module with basis
{T_w : w in W_0}, dim M(t) = 12. The finite Weyl group W_0 acts on T by
s_1(t_1,t_2) = (1/t_1, t_1 t_2), s_2(t_1,t_2) = (t_1 t_2^3, 1/t_2);
central characters are W_0-orbits. Positive roots:
alpha_1, alpha_2, alpha_1+alpha_2, 2alpha_1+alpha_2, 3alpha_1+alpha_2, 3alpha_1+2alpha_2.

## 2. Results

**Result A (structural obstruction, proved fragment).**
At q^2 = -1 one has q + q^{-1} = 0, so the numerator factor governing the rank-one
intertwiner calculus vanishes identically. Concretely, the standard pole prediction
"alpha(t) = +-1 forces a proper submodule" FAILS: the exact integral recursion below gives

  M(1,1), M(1,-1), M(-1,1) simple (12-dimensional),

despite maximal torus resonance (every positive root takes value +-1 at these points).
Two independent certificates support each simplicity claim:
(i) exact spin saturation over Q(i,sqrt2): no nonzero proper H-stable subspace is generated
from any primary/generalized kernel vector of 8 generic integer operator combinations;
(ii) reduction mod 17 (i=4, zeta_8=2): the operator image has dimension 144 = 12^2, so by
Burnside's theorem the reduction is simple, and simplicity lifts to characteristic zero for
these integral models by Nakayama's lemma (a proper C-submodule would reduce to a proper
submodule for all but finitely many primes; exhibiting one prime with full image excludes it).

**Result B (certified block data, computed evidence).**
Exact decomposition over Q(i,sqrt2) with generalized primary kernels, cross-checked mod 17:

| representative | exact comp dims | mod-17 image dim | reading |
|---|---|---|---|
| generic (2,3) | [12] | 144 | simple |
| (1,1),(1,-1),(-1,1) | [12] | 144 | simple (resonant!) |
| (i,1),(1,i),(i,i),(-1,i) | [1,1,2,2,3,3] | 81 (46 at (i,i)) | reducible, six factors |
| (z,1),(z,z), z = zeta_8 | [6,6] | 108 | two 6-dim blocks |

Only the 144 entries are claimed as proved-simple; the 81/108/46 entries are reported as
exact-decomposition outputs plus mod-17 invariants (evidence, not simplicity certificates).

**Result C (certified affine-G2 KL infrastructure, proved computation).**
Kazhdan-Lusztig C'-recursion for the affine Weyl group of type G2 with generators
(s_0,s_1,s_2), Coxeter exponents m_01 = 2, m_02 = 3, m_12 = 6 (verified from a faithful
affine representation over Q(sqrt3)), braid-closed Bruhat intervals, mu subtraction:
C'_w = C'_{ws} C'_s - sum_{z} mu(z,ws) C'_z.
Checks passed: C'-coefficients recover polynomials in q = v^2 (no negative/odd exponents
after the +l(w) shift), degree bound deg P_{x,w} <= (l(w)-l(x)-1)/2, spot values e.g.
P([1],[1,2,1]) = 1+q, P([],[0,2,0]) = 1+q, P([],[1,2,1,2]) = 1+2q.
Tables: 735 KL pairs, 289 nonzero mu values (artifact kl_data.json).

## 3. Why this blocks the uniform target formula (and what replaces it)

The admitted target asked for a uniform closed (p-)KL/Soergel P(1) multiplicity formula at
every central character recovering Davis's q^4=1 vectors. Result A is a concrete
counterexample to the naive uniform reading: at t = (1,1) and (1,-1) every root is resonant
yet M(t) is simple, so no assignment of P(1) > 1 values can be correct there. The corrected
program must first stratify by TRUE poles of normalized intertwiners (which vanish
identically in the q+q^{-1}=0 specialization) rather than naive resonance alpha(t)=+-1.
Results B and C supply the machine-checkable anchors for that corrected formula.

## 4. Methods (reproducible)

1. Exact integral BLZ engine (artifact engine.py + exactM2.py): finite Hecke left action on
   the T-basis; exact Q-polynomial division (theta_x - theta_{sx})/(1 - theta_{-alpha_s})
   verified by multiply-back; theta_x T_w recursion on descents; specialization at exact
   t in Q(i,sqrt2). Certified by: quadratic/braid/X-commutativity/Bernstein residuals
   ~1e-12 over C, exact center orbit-sum scalarity, generic commutant dimension 1.
2. Exact decomposition: primary + generalized kernels ker((F-lambda)^k) of generic integer
   combinations, exact spin saturation, exact restriction/quotient recursion.
3. Mod-17 model (modp.py): i=4, zeta_8=2; independent BLZ implementation; Burnside image
   dimension via greedy operator-span saturation (144 = full M_12 certifies simplicity).
4. KL recursion (kl.py, klproof2.py, klcert.py): faithful Q(sqrt3) alcove matrices,
   BFS Cayley ball, braid-closure reduced-word graphs, subword Bruhat intervals,
   Hecke-action C' recursion with mu extraction as the v^{-1} coefficient.

## 5. Limitations and conjectures (clearly separated)

- Proved: engine relations, center scalarity, generic simplicity, KL polynomiality/degree
  bounds, and resonant simplicity at (1,1),(1,-1),(-1,1) by the two-method certificate.
- Computed evidence (not claimed as theorems): exact dimension vectors [1,1,2,2,3,3] and
  [6,6] (decomposition algorithm output, cross-checked mod 17 but without full block
  simplicity/diagonalization proofs); cell-constancy of the future multiplicity formula.
- Conjecture: the corrected multiplicity formula is P_{x,w}(1) evaluated on the
  normalized-intertwiner stratum, constant on two-sided cells (a-values 0,1,2,3,6 for dual
  G2), with Davis vectors as specializations; the 8th-root [6,6] blocks are the natural
  test case for the p-KL (characteristic-2/unequal-parameter) correction.

## 6. Artifacts

output/artifacts/engine.py, exact.py, exact2.py, exactM.py, exactM2.py, modp.py,
burnside.py, kl.py, klproof2.py, klcert.py, decdata.py, kltable.py, cells.py,
kl_data.json (735 pairs, 289 mu), decomp_data.json (9 representatives).
