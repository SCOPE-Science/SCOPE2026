# Dimensional freedom is active for the critical short-root tuple (n = 4, 5, 6)

## Context

The Alexandrov-Fenchel inequality states that for convex bodies K, L, C_1, ..., C_{n-2} in R^n,
V(K,L,C)^2 >= V(K,K,C) V(L,L,C), where V denotes mixed volume. Shenfeld and van Handel
(arXiv:2011.04059; Acta Math. 231 (2023)) completely characterized equality when the reference
bodies are polytopes: extremals arise from translation, support (agreement on the support of
S(B,C,.)), and dimensionality (degenerate pairs). For a critical but non-supercritical tuple the
dimensional mechanism may or may not be active. The admitted target asks whether it is active for
a specific mixed short-root reference tuple.

## Definitions

Fix n in {4,5,6} with standard basis e_1,...,e_n in Bourbaki coordinates. Positive C_n short
roots are g = e_i - e_j and g = e_i + e_j for 1 <= i < j <= n. The short-root zonotope is the
Minkowski sum of segments Z_n^s = sum_{i<j} ([-g_{ij}^-,g_{ij}^-] + [-g_{ij}^+,g_{ij}^^+]) with
g_{ij}^- = e_i - e_j and g_{ij}^+ = e_i + e_j; a finite sum of segments, hence a polytope.
With d_1 = e_1 + e_2 and d_2 = e_1 - e_2, the rank-two parallelogram is
F_n = [-d_1,d_1] + [-d_2,d_2] contained in E = span{e_1,e_2}. Let B^n be the Euclidean unit ball.
The reference tuple is C = (Z_n^s,...,Z_n^s,F_n) with n-3 copies of Z_n^s plus F_n (for n=4,
C = (Z_4^s,F_4)), hence n-2 entries. Write V(.) for mixed volume V_n and S(B^n,C,.) for the
mixed area measure S_{B,C_1,...,C_{n-2}} on S^{n-1}. The diagonal segments are M = [-d_1,d_1]
and N = [-d_2,d_2]. The extremal bodies are K = B^n + M and L = B^n + N. Support functions on
S^{n-1} satisfy h_{B} = 1, h_M(u) = |d_1.u|, h_N(u) = |d_2.u|.

## Result

For each n in {4,5,6}, the tuple C is critical but not supercritical, and the full-dimensional
convex bodies K = B^n + M and L = B^n + N satisfy genuine Alexandrov-Fenchel equality
V(K,L,C)^2 = V(K,K,C) V(L,L,C) > 0, yet there are no a > 0 and v in R^n with
h_K = a h_L + <v,.> on supp S(B^n,C,.). Hence the Shenfeld-van Handel dimensional extremal
mechanism is active for this critical short-root tuple. The target claim is true.

## Proof / Evidence

Criticality: Z_n^s is full-dimensional ({e_i-e_j} spans {x: sum x_i = 0} of dimension n-1 and
e_1+e_2 lies outside it), while F_n has dim 2. Any subfamily of C containing Z_n^s or B^n spans
R^n; the only subfamily spanning a proper subspace is {F_n} with dim 2 = 1+1. Thus C is critical
in the Shenfeld-van Handel sense (all k-subfamilies span dimension >= k+1) but not supercritical
({F_n} spans 2 < 1+2 = 3).

Degenerate pair: M + N + F_n lies in E with dim <= 2 < 3, so Lemma 2.2 applied to
(M,N,C_1,...,C_{n-2}) forces V(M,N,C) = V(M,M,C) = V(N,N,C) = 0. M is not a translate of N:
both are centrally symmetric equal-length segments in orthogonal directions d_1.d_2 = 0.
Normalization: R = diag(1,-1,1,...,1) fixes B^n, satisfies R(d_1) = d_2 and R(d_2) = d_1 so
R(F_n) = F_n and R(M) = N, and permutes the short-root segments up to sign (checked by cases
and computationally). By orthogonal invariance, V(M,B^n,C) = V(N,B^n,C). Thus (M,N) is a
C-degenerate pair.

Equality: by multilinearity, V(K,L,C) = V(B,B,C) + 2V(M,B,C), and the same expression holds
for V(K,K,C) and V(L,L,C) using the three vanishings and the normalization. Positivity:
every subfamily of (B,B,C) containing B or Z spans R^n and {F} has dim 2 >= 1, so
V(B,B,C) > 0 by Lemma 2.2; monotonicity gives V(K,L,C) >= V(B,B,C) > 0. Hence all three
mixed volumes are equal and positive, giving nontrivial equality. This is the Lemma 2.11
mechanism.

Support directions: let u* = (e_1+e_2)/sqrt(2) and w* = (e_1-e_2)/sqrt(2). For a zonotope the
face in direction u is the sum of segments orthogonal to u. By Lemma 2.3, u lies in
supp S(B,C,.) iff the Z-face has dim >= n-3, the F-face has dim >= 1, and their sum has
dim >= n-2. At u*, the orthogonal short roots are e_1-e_2 plus all e_i +/- e_j with
3 <= i < j <= n, spanning dimension n-1; the F-face is [-d_2,d_2] of dim 1; the sum has
dim n-1. Hence u* and -u* lie in the support by evenness; symmetrically w* and -w* lie in
the support with F-face [-d_1,d_1]. Face-dimension counts hold uniformly for n = 4,5,6.

No dilation plus translation fits: h_K = 1 + |d_1.u| and h_L = 1 + |d_2.u|. At +-u*,
h_K = 1+sqrt(2) and h_L = 1; at +-w*, h_K = 1 and h_L = 1+sqrt(2). If h_K = a h_L + <v,.>
on the support, evaluating at +-u* forces a = 1+sqrt(2) with <v,u*> = 0, while evaluating
at +-w* forces a = 1/(1+sqrt(2)) = sqrt(2)-1. Since 1+sqrt(2) != sqrt(2)-1 (2.414... vs
0.414...), no such (a,v) exists. A documented axis-aligned attempt M = [0,e_1], N = [0,e_2]
fails here because its difference coincides with a linear function on this support.

## Limitations

The result exhibits one explicit dimensional-freedom extremal pair per n in {4,5,6}; it does
not classify all extremals of this tuple, does not treat long roots or other reference bodies,
and relies on the Shenfeld-van Handel polytope critical-case lemmas (zonotopes are polytopes)
plus orthogonal-invariance computations.

## Reproducibility

The script output/artifacts/verify_support.py recomputes, for each n in {4,5,6}: the Lemma 2.3
face dimensions at u* and w* (dimA = n-1, dimB = 1, dimAB = n-1), the support-function values
(hM = sqrt(2), hN = 0 at u* and swapped at w*), the inconsistent forced dilations
a = 2.414214 vs 0.414214, full-dimensionality of Z, dim F = 2, and the reflection R permuting
short-root generators up to sign. Run `python3 output/artifacts/verify_support.py`; expected
output is recorded in output/artifacts/results.txt ending in ALL CHECKS PASSED.

## References

- Y. Shenfeld and R. van Handel, The extremals of the Alexandrov-Fenchel inequality for convex
  polytopes, arXiv:2011.04059 (2020; v2 2022); Acta Math. 231 (2023). Lemmas 2.2, 2.3, 2.5,
  Definition 2.10, Lemma 2.11, Example 2.12, Theorem 2.13.
- R. Schneider, Convex Bodies: The Brunn-Minkowski Theory (reference for mixed volumes).
