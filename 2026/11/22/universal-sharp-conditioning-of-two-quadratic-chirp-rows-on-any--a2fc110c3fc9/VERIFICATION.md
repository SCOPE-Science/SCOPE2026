---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The two phase differences relative to x_0 are an invertible linear map of the label difference, with determinant (x_1-x_0)(x_2-x_0)(x_1-x_2); thus all nonzero ordered pairs occur once for each first label on each aperture. The row Gram eigenvalues are 3 plus or minus |1+omega^u+omega^v|. The modulus is below 3 unless both differences vanish, and the positive singular-value ratio increases strictly with it. For the maximum at least two of u,v,u-v are nonzero; each corresponding cosine is at most cos(2pi/p). Equality requires exactly one zero and the others +/-1, giving the six displayed pairs. For the minimum a repeated root gives modulus >1, and for distinct roots with a cyclic gap at least p/2 the identity |S|^2=1-8 product cos(pi*gap/p) gives modulus at least one. Balanced triples have all gaps below p/2, even at p=5, and give modulus below one. On the remaining range, strict concavity of log cos shows that transferring one unit from a larger gap to a gap at least two smaller strictly increases the product; exactly the balanced gap multiset minimizes. Its representative {0,k,2k} yields rho_p. The unique exceptional cyclic gap gives p distinct translates of the minimizing root triple, with exactly three translates containing 1 and two ways to order the other roots. Both six-per-label counts thus give 3p^2 unordered pairs. Taylor expansion gives rho_p=2pi*sqrt(3)/(3p)+O(p^-2) and tau_p=3-4pi^2/(3p^2)+O(p^-4), leading to both stated asymptotics. Independent finite enumeration for p=5,7,11,13,29,101 matched both extrema within 1e-12 and both six-counts; the proof, not enumeration, gives the universal claim. The frozen checker and verification notes were inspected without executing the uploaded code.

## originality

PASS

The minimum three-root modulus and the balanced optimizer geometry are substantially known: Barber proves the same congruence formulas and configurations for sufficiently large orders, and the exact square Fourier Riesz theorem gives the same balanced triple geometry for a different objective. Do not credit either as new over those ranges. The supported distinct result is the full two-sided row-pair conditioning classification, especially the sharp repeated-phase maximum and its multiplicity on every three-site aperture, with an argument valid for every prime p>=5. Neither prior result states or mechanically supplies that full two-sided classification.

## value

PASS

The best and especially worst nonzero singular-value ratios determine exact conditioning of two observable row combinations on any three-site aperture, independent of geometry. The equality counts explain how many label choices attain each end, and the worst case growing linearly in p is materially different from the near-isometric best case. This is a complete natural condition classification, not a claim that the balanced minimum for roots of unity is new or that arbitrary three-component inputs can be recovered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
