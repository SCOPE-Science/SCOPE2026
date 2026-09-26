# Complete local-solubility certificate for the Châtelet cell y²−17z²=(x²−3)(x²−5)

## Context

The Hasse principle and sufficiency of the Brauer–Manin obstruction for
Châtelet / degree-4 del Pezzo surfaces is a recognized frontier
(Colliot-Thélène/Sansuc, Colliot-Thélène/Skorobogatov program).
Each new explicit local-solubility record for a fixed coefficient cell
calibrates that boundary and anchors later Brauer evaluations.
This record treats the single cell

    X₀ : y² − 17z² = (x² − 3)(x² − 5)   over Q,

with affine model U₀ : F(x,y,z) = y²−17z²−(x²−3)(x²−5) = 0,
and quaternion algebra A = (17, x²−3).
No Hasse-principle failure is claimed: X₀(Q) is nonempty (see below).

## Definitions

- P(x) = (x²−3)(x²−5) = x⁴−8x²+15.
- Bad set S = {∞, 2, 3, 5, 17}: ∞ archimedean; {2,3,5} discriminant
  primes of P; 17 ramification prime of the constant slot a=17.
- Witness P₀ = (x,y,z) = (2,4,1).

## Result

(a) For every v ∈ {∞, 2, 3, 5, 17}, P₀ is an explicit Q_v-point of X₀:
exact integral equality F(P₀) = 0 over Z (hence a Z_p-point for every
finite p, in particular for 2, 3, 5, 17) plus real equality at ∞.

(b) For every prime p outside {2, 3, 5, 17}, P₀ reduces to a smooth
F_p-point, so X₀(Q_p) is nonempty, uniformly in p with the single
point P₀.

In particular X(A_Q) ≠ ∅ via the diagonal adelic point (P₀)_v.
The diagonal Brauer sum for A at P₀ is 0 (x²−3 = 1 is a square
everywhere locally), so there is no Hasse failure at this cell.

## Proof / evidence

Witness check: y²−17z² = 16−17 = −1; (x²−3)(x²−5) = (1)(−1) = −1.
Hence F(2,4,1) = 0 exactly over Z.

Gradient: ∇F = (−4x³+16x, 2y, −34z); at P₀, ∇F = (0, 8, −34) ≠ 0 over Q,
so P₀ is a smooth Q-point (hence smooth Q_v-point wherever the
reduction is smooth, and an exact Z_v-solution everywhere).

Five-place table:
- v = ∞: real equality 16−17 = −1 holds in R; P₀ ∈ X(R).
- v = 2: F(P₀) = 0 over Z implies equality in Z₂; exact Z₂-solution,
  hence Q₂-point. Reduction mod 2 is singular (∇F ≡ 0 mod 2),
  openly recorded; Q₂-status is unaffected since no lifting is needed.
- v = 3: exact Z₃-solution; ∇F mod 3 = (0,2,2) ≠ 0 (smooth reduction).
- v = 5: exact Z₅-solution; ∇F mod 5 = (0,3,1) ≠ 0 (smooth reduction).
- v = 17: exact Z₁₇-solution; ∇F mod 17 = (0,8,0) ≠ 0 (smooth reduction).

Uniform cover: for any prime p ∉ {2,3,5,17}, F(P₀) = 0 over Z gives
F(P₀) ≡ 0 mod p, and (8,−34) ≢ (0,0) mod p because gcd(8,34) = 2
and p is odd (p ≠ 2; p = 17 is excluded and in any case (0,8,0) ≠ 0).
Thus P₀ reduces to a smooth F_p-point and is an exact Z_p-solution,
so X₀(Q_p) ≠ ∅. One point, uniform in p.

Discriminant: for P(x) = x⁴−8x²+15 with P′(x) = 4x³−16x, the 7×7
Sylvester determinant (Bareiss) gives Res(P,P′) = 3840 = 2⁸·3·5,
cross-checked by (16√15)² = 3840. Hence discriminant primes {2,3,5};
with a-ramification 17 and ∞, S = {∞,2,3,5,17} is forced.

## Limitations

- This is the preset local-solubility fallback, not a Hasse-failure
  witness. The admitted Hasse-failure target (X₀(A_Q) ≠ ∅ but
  X₀(Q) = ∅ with universal Brauer sum 1/2) is false: P₀ ∈ X₀(Q),
  X₀(Q) is infinite, and the diagonal Brauer sum is 0.
- The uniform cover uses the single global integral point P₀
  (exact Z-equality), which is stronger than per-place Hensel logs
  but means no distinct bad-place lifts are exhibited.
- Projective-closure smoothness and Azumaya residue details in
  supporting worklogs are proof-sketch level and not needed for
  this certificate.

## Reproducibility

Stdlib-only (integers), offline replay:

    python3 output/artifacts/fallback_certificate.py  # FALLBACK_OK
    python3 output/artifacts/discriminant.py          # VERIFY_OK_DISC
    python3 output/artifacts/locals.py                # VERIFY_OK_LOCALS
    python3 output/artifacts/reduction.py             # VERIFY_OK_REDUCTION
    python3 output/artifacts/good.py                  # VERIFY_OK_GOOD
    python3 output/artifacts/replay_all.py            # REPLAY_ALL_OK (27/27)

## References

- Viray, Failure of the Hasse principle for Châtelet surfaces in
  characteristic 2. https://arxiv.org/abs/0902.3644
  (char-2 construction; disjoint base field/cell).
- Huang–Liang, Hasse principle violation for algebraic families of del
  Pezzo surfaces of degree 4 ... (g = 1 mod 4 parametric families).
  https://arxiv.org/abs/2312.11204
- Lyczak–Sarapin, Quartic del Pezzo surfaces with a Brauer group of
  order 4 (order-4 study; explicit failures at p = 13).
  https://arxiv.org/abs/2110.13687
- Rome, A Positive Proportion of Hasse Principle Failures in a Family
  of Châtelet Surfaces. https://arxiv.org/abs/1803.07017
