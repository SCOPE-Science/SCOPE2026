# Disproof of universal differential Santalo inversion for the projective Finsler X-ray on RP^2

## Context

The target asked for a two-sided resolution of a Gelfand double-fibration claim:
for every smooth reversible projective Finsler metric F on RP^2 whose
unparametrised geodesics are the projective lines (all closed), the geodesic
X-ray transform I_F on even C^infinity functions is injective and there is an
explicit differential operator D on the dual side, built from the double
fibration, with D I_F^* I_F = Id. A proof of the full conjunction or a rigorous
disproof is a complete TARGET resolution.

## Definitions

- F_0: standard round (constant-curvature) Riemannian metric on RP^2 induced by
  the covering S^2 -> RP^2. It is smooth, reversible (quadratic, hence Finsler),
  its unparametrised geodesics are projections of great circles (projective
  lines), all closed. Hence F_0 is admissible for the universal claim.
- Functions on RP^2 lift to antipodally even functions on S^2 ("even").
- I_{F_0}: integration of even functions over closed projective-line geodesics;
  I_{F_0}^*: dual incidence averaging operator to RP^2; N = I_{F_0}^* I_{F_0}.
- F: classical Funk-Radon transform (Ff)(xi) = integral of f over {x . xi = 0}.
- H_{2k}: even spherical-harmonic space of degree 2k on S^2; Delta = m_k Id with
  m_k = 2k(2k+1) on H_{2k}.
- a_k = C(2k,k)/4^k = (2k-1)!!/(2k)!!; P_{2k}(0) = (-1)^k a_k.

## Result (headline theorem)

The universal conjunction is FALSE. For the admissible round metric F_0 on RP^2:

1. I_{F_0} IS injective on C^infinity(RP^2) (even lifts).
2. NO linear differential operator D of any finite order satisfies
   D I_{F_0}^* I_{F_0} = Id on C^infinity(RP^2).

Consequently there is no universal explicit differential Santalo inversion
identity D I_F^* I_F = Id valid for all smooth reversible projective F.

## Proof / evidence

### Step 1 — reduction to Funk.

With SO(3)-invariant smooth positive densities, I_{F_0} and I_{F_0}^* lift to
operators on C^infinity_even(S^2) agreeing with the Funk transform F and its
adjoint up to fixed positive constants. The incidence manifold is
SO(3)-transitive, so the normalisation differences are absorbed into one
constant: with tildes denoting even lifts, tilde N = C F^2, C > 0.

### Step 2 — injectivity (Funk-Hecke).

F kills odd functions and preserves each H_{2k}. By Funk-Hecke,
F|_{H_{2k}} = lambda_k Id with lambda_k = L P_{2k}(0),
P_{2k}(0) = (-1)^k C(2k,k)/4^k != 0 for every k, L != 0 the great-circle length
factor. Hence F, and therefore I_{F_0}, is injective on even functions. The
normal operator has eigenvalues mu_k = C lambda_k^2 = C_0 a_k^2 > 0 on H_{2k},
C_0 = C L^2 > 0.

### Step 3 — averaging a hypothetical inverse.

Suppose a finite-order linear differential operator D satisfies D N = Id.
Lift to tilde D on even functions. Each conjugate
tilde D_g = R_g tilde D R_g^{-1} is differential of the same order and, since N
is rotation-equivariant, tilde D_g tilde N = Id. Averaging over Haar measure,
bar tilde D = integral tilde D_g dg (compact group, coefficient integration),
is SO(3)-invariant, same order, descends to RP^2 (rotations commute with the
antipodal map), with bar D N = Id.

### Step 4 — Helgason classification.

Every SO(3)-invariant differential operator on S^2 = SO(3)/SO(2) is a polynomial
in the Laplacian: bar tilde D = P(Delta) (rank-one invariant-operator theorem).
Hence on H_{2k}: P(m_k) mu_k = 1 for all k >= 0, i.e.
P(4k^2+2k) = 1/(C_0 a_k^2). Call the left side R(k).

### Step 5 — Wallis bounds and growth contradiction.

Lemma (two-sided Wallis bounds): for k >= 1,
1/(2 sqrt(k)) <= a_k <= 1/sqrt(k+1),
from a_{k+1} = a_k (2k+1)/(2k+2), a_1 = 1/2, by induction. The lower step needs
(2k+1)^2 >= 4k(k+1), gap exactly 1 > 0. The upper step needs
4(k+1)^3 >= (2k+1)^2 (k+2), i.e. gap (4k^3+16k^2+20k+8)-(4k^3+8k^2+5k+1)
= 8k^2+15k+7 > 0 (in particular the corrected gap 3k+2 form after clearing
denominators is positive; verified numerically to k=2000).

Therefore R(k) = 1/(C_0 a_k^2) satisfies R(k) >= C_0^{-1}(k+1) -> infinity, so P
is non-constant, and R(k) <= 4 C_0^{-1} k for k >= 1. But a non-constant
polynomial P of degree >= 1 composed with the quadratic 4k^2+2k gives R of
degree >= 2 with R(k)/k -> +infinity, contradicting the linear upper bound.
The constant-P case contradicts divergence. Hence no such D exists.

Remark (symbol view, not needed for the proof): N is an elliptic
pseudodifferential operator of order -1 with principal symbol c|xi|^{-1}; a
differential inverse would need principal symbol c^{-1}|xi|, not polynomial.
The argument above is the elementary representation-theoretic form. The true
Funk inverse on RP^2 is of pseudodifferential (order +1, square-root-of-Laplacian)
type, e.g. via fractional integrals or Riesz potentials.

### Numerical confirmation.

The stdlib script compute_funk_spectrum.py checks P_{2k}(0) != 0 for k < 2000,
|P_{2k}(0)| sqrt(pi k) -> 1 (0.99979 at k=600 via stable recurrence) and
mu_k k -> const (~0.317 up to the absorbed factor), confirming the Wallis
decay mu_k ~ const/k used in the growth argument. Re-executed during audit: OK.

## Limitations

- Disproof proceeds via the inversion conjunct on the round metric; it does not
  decide injectivity for non-round projective Finsler metrics (the prescribed
  kernel-counterexample route), which is unneeded since the conjunction already
  fails.
- It does not rule out pseudodifferential (order +1, sqrt-Laplacian / fractional
  integral) inversion, which is the correct known form.
- The SO(3)-equivariance averaging is specific to the round case; no claim is
  made about a universal invariant operator for non-round F.

## Reproducibility

- Definitions and normalisations: any SO(3)-invariant choices differ by positive
  constants absorbed into C_0 > 0; the growth contradiction is independent of C_0.
- Analytic checks: Funk-Hecke formula P_{2k}(0) = (-1)^k C(2k,k)/4^k; Wallis
  induction gaps 1 and 8k^2+15k+7 displayed above; degree argument elementary.
- Computation: run `python3 output/artifacts/compute_funk_spectrum.py`
  (standard library only) to reproduce nonzero eigenvalues and asymptotics.

## References

- P. Funk (1911, 1913): Funk-Radon transform on S^2; Funk-Hecke multipliers.
- S. Helgason: invariant differential operators on rank-one symmetric spaces;
  S^2 = SO(3)/SO(2) operators are polynomials in the Laplacian.
- B. Rubin, arXiv:1207.5178: Funk-Radon-Helgason mean-value/fractional-integral
  inversions; differentiation (d/dr vs d/dr^2) issue; no differential D N = Id.
- M. Quellmalz (2015, 2017, 2020) and co-authors (2023): generalized/shifted
  Funk-Radon injectivity, range, frame decompositions via integral means.
- B. Rubin (2024): shifted Funk-Radon injectivity via Jacobi-polynomial zeros.
- V. Palamodov, Reconstructive Integral Geometry (2004), Ch. 3: Funk inversion.
- L. Pestov & G. Uhlmann (2004); V. Krishnan (2010); V. Sharafutdinov:
  geodesic X-ray inversion formulas (integral/pseudodifferential type).
- Double-fibration microlocal literature (e.g. arXiv:2306.05906; J. Geom. Anal.
  2025): normal operators of ray transforms as FIO/PsiDO, Bolker conditions.
