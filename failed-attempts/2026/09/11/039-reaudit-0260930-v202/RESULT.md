# The stated Perron-root gap above the 3-braid minimum is false: an explicit central-twist counterexample

## Context

The admitted target claimed an explicit Perron-Frobenius dilatation gap above the known
3-braid minimum for the named non-extremal train-track family: every pseudo-Anosov
beta in B3 not conjugate to a power of sigma1 sigma2^{-1} (or its inverse) and with total
syllable length >= 3 satisfies lambda(beta) >= rho, where rho ~= 2.747 was stated to be
the largest real root of f(t) = t^4 - 3t^3 - t^2 + 3t - 1. The global 3-braid minimum
(3+sqrt(5))/2 attained by gamma = sigma1 sigma2^{-1} is classical (cf. Lanneau-Thiffeault,
minimum-dilatation of braids on punctured discs, Theorem 1.1: n=3 minimum 2.61803 with
polynomial X^2-3X+1 and braid sigma1 sigma2^{-1}); no track-restricted floor above it was known.

## Definitions

- B3 = <sigma1, sigma2 | sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2>.
- gamma = sigma1 sigma2^{-1} (the extremal minimizer).
- Delta = sigma1 sigma2 sigma1 (Garside half-twist); Delta^2 is the central full twist.
- beta* = gamma Delta^2 = sigma1 sigma2^{-1}(sigma1 sigma2 sigma1)^2.
- e: B3 -> Z, sigma_i |-> 1, the abelianization (exponent sum), a conjugacy invariant.
- f(t) = t^4 - 3t^3 - t^2 + 3t - 1; rho denotes its largest real root.
- A braid beta in B3 is pseudo-Anosov iff its image in B3/<Delta^2> ~= PSL(2,Z) is
  hyperbolic (|tr| > 2); its dilatation then equals the spectral radius of any lift to
  SL(2,Z): for |tr| = T > 2, det = 1, lambda = (T + sqrt(T^2-4))/2
  (standard Birman-Series / Casson-Bleiler / Los theory for 3-braids).

## Result

The claimed universal floor is FALSE. The braid
beta* = sigma1 sigma2^{-1}(sigma1 sigma2 sigma1)^2 satisfies:

1. beta* is pseudo-Anosov with dilatation lambda(beta*) = (3+sqrt(5))/2 ~= 2.618;
2. beta* is not conjugate in B3 to any power (sigma1 sigma2^{-1})^{+-k}, and its
   alternating syllable length is 7 >= 3 — so it lies in the scope of the target claim;
3. (3+sqrt(5))/2 < 2.62 < 2.747 < 3 < rho, where rho in (3, 3.1) is the true largest real
   root of f. In particular lambda(beta*) < rho and below the target's stated 2.747.
   Additionally f(2.747) < 0 (exactly -5549417340919/10^12), so the target's stated
   approximation 2.747 is not near a root of its own polynomial.

Hence no floor lambda(beta) >= rho holds over all in-scope non-extremal 3-braids.

## Proof / evidence

Exact integer/rational certificate (machine-verified, exact arithmetic only):

- Model sigma1 |-> A = [[1,1],[0,1]], sigma2 |-> B = [[1,0],[-1,1]].
  Braid relation holds exactly: ABA = BAB = [[0,1],[-1,0]] =: W (image of Delta).
- W^2 = -I, so Delta^2 maps to -I: central and in the kernel of projectivization.
  Hence beta* and gamma share the same PSL(2,Z) image (central-twist invariance).
- gamma |-> G = A B^{-1} = [[2,1],[1,1]] (corrected display; the draft's [[2,1],[-1,0]]
  has a sign typo in the (2,1) entry — trace/determinant claims and code use the correct
  matrix): tr G = 3, det G = 1.
- beta* |-> B* = G W^2 = -G: tr B* = -3, det B* = 1.
- |tr B*| = 3 > 2, so beta* is pseudo-Anosov; characteristic polynomial x^2+3x+1 gives
  eigenvalues (-3+-sqrt(5))/2 and spectral radius (3+sqrt(5))/2, identical to lambda(gamma).
- Non-conjugacy: e(gamma) = 1+(-1) = 0 so e(gamma^{+-k}) = 0 for all k, while
  e(beta*) = e(gamma)+e(Delta^2) = 0+6 = 6 != 0. Thus beta* is not conjugate to any
  (sigma1 sigma2^{-1})^{+-k}.
- In-scope syllable count: beta* = sigma1 sigma2^{-1} sigma1 sigma2 sigma1 sigma1 sigma2 sigma1
  = sigma1 | sigma2^{-1} | sigma1 | sigma2 | sigma1^2 | sigma2 | sigma1: 7 alternating
  syllables >= 3 under either counting convention.
- Root enclosure: f(3) = -1 < 0; f(3.1) = 16691/10000 = 1.6691 > 0 (exact rational).
  Exact identity f'(t)-24 = (t-3)(4t^2+3t+7) gives f'(t) >= f'(3) = 24 > 0 for all t >= 3,
  so f is strictly increasing on [3,inf): exactly one root in (3,3.1), none in [3.1,inf),
  i.e. the largest real root rho lies in (3,3.1), in particular rho > 3.
- sqrt(5) < 2.24 since 5 < 2.24^2 = 5.0176, so lambda(beta*) = (3+sqrt(5))/2 < 5.24/2 = 2.62.
- Corroboration only (not part of the proof): 12-iterate Artin-action cyclic-word-growth
  replay gives identical lengths [2,6,16,42,110,288,754,1974,5168,13530,35422,92736] for
  gamma and beta*, consistent with equal growth rate.

Structural point: a pure PSL(2,Z)-trace floor cannot exceed (3+sqrt(5))/2 over the full
complement of the extremal conjugacy class, because the central full twist preserves the
projective class (hence dilatation) while changing exponent sum (hence conjugacy class).
Any repaired gap must restrict the center power or use a finer invariant.

## Limitations

Disproof of the universal floor only; says nothing about a repaired gap with bounded
center power or finer invariants. Uses standard B3/PSL(2,Z) classification plus the exact
certificate; the finite cyclic-growth replay is corroboration only.

## Reproducibility

Run `python3 output/artifacts/verify_disproof.py` (stdlib only: exact integer/Fraction
arithmetic, no floats). Expected output ends with `ALL_CHECKS_PASSED`, replaying the
braid relation, Delta^2 -> -I, traces +-3, exponent sums 0 vs 6, sqrt(5) < 2.24 bound,
f(3)/f(3.1)/f(2.747) evaluations, derivative identity spot-checks, and the 12-iterate
growth replay.

## References

- E. Lanneau, J.-L. Thiffeault, On the minimum dilatation of braids on punctured discs,
  arXiv:1004.5344 (2010); Theorem 1.1 (n=3 minimum (3+sqrt5)/2, X^2-3X+1, sigma1 sigma2^{-1}).
- E. Hironaka, E. Kin, A family of pseudo-Anosov braids with small dilatation,
  Geom. Topol. Monogr. (2006).
- E. Lanneau, J.-L. Thiffeault, On the minimum dilatation of pseudo-Anosov
  homeomorphisms on surfaces of small genus.
- B. Farb, C. Leininger, D. Margalit, Small dilatation pseudo-Anosov homeomorphisms
  and 3-manifolds.
- Standard B3/<Delta^2> ~= PSL(2,Z) 3-braid classification: Birman-Series,
  Casson-Bleiler, Los theory.
