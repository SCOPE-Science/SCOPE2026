---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the mean-zero space, L=I−P is positive definite exactly for connected support; inverse trace tends to infinity on approach to disconnected support. The feasible closed polytope with that extension gives attainment. The Hessian along a nonzero perturbation is positive by the inverse-trace square identity, and the mean-zero restriction is injective on the row-sum-zero perturbations, giving uniqueness. Rotation invariance forces orbit weights a,b. If 2a+2b<1, rescale both by 1/(2a+2b), preserving support and multiplying L by a factor greater than one, so the optimizer has no holding. Fourier modes give the displayed D_k; not all A_k and B_k agree. At ε=1, B_k/A_k=4−2A_k and ∑1/A_k=(n²−1)/6 give F′_n(1)=(n−1)(n−3)/2. At ε=0 there is disconnection for even n, and for odd n multiplication by two shows the two endpoint values coincide, so strict convexity excludes both. For n=5, the complete graph has ε=1/2 and K=16/5; independently for n=6 the modes give F_6(ε)=2/(3/2−ε)+4/3+1/(2ε), minimized at ε=1/2, K=13/3. The stated finite resolvent follows by partial fractions and sampling the reciprocal-cosine Fourier series, retaining multiples of n with sign (−r)^n and removing k=0. The comparison ε=n^(−2/3) bounds optimal excess by O(n^(4/3)), so the first positive term gives ε_n=O(n^(−2/3)). If n√ε_n stayed bounded on a subsequence, the near-π mode in the nonnegative second sum would alone add order n² above that first term, a contradiction for either parity. Thus (−r)^n→0 and the second term is asymptotic to n/(4√ε_n), forcing ε_n bounded below on the n^(−2/3) scale. The uniform scaled correction is x/32+1/(4√x), whose unique minimum is at x=4^(2/3) with value 3/(8·4^(1/3)); compactness gives both asymptotics. Substituting ε=1/2 gives the equal-edge comparison n²/15, and the pure one-hop sum is (n²−1)/6.

## originality

PASS

Pass is for the evaluated squared-cycle design: interior edge balance, parity-resolved response and optimized n^(−2/3) boundary layer with its correction constant. In particular, existence, uniqueness, symmetry and zero holding after budget normalization are already consequences of the effective-resistance framework and are not credited as independent novelties. The same-day Möbius-ladder result establishes a genuine analogous boundary layer, not this theorem for C_n². No inspected prior statement supplies the evaluated optimum or its asymptotics for C_n².

## value

PASS

The graph remains a natural sparse test case for optimizing average travel times, and the singular optimum distinguishes this objective from equal weighting, removing a channel, or minimizing worst spectral contraction. The fractional exponent and correction follow from competing low-frequency costs near 0 and π and quantify how a nearly dominant jump type must be regularized even when it stays connected. These are useful precise design laws beyond the known general convex formulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
