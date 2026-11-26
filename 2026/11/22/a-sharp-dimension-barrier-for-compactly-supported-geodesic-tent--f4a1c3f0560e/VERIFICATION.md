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

For 0<c<π the circular Fourier integrals are c² at zero and 2(1−cos nc)/n² otherwise. For c≥π the truncation is inactive everywhere, including at c=π; the hemisphere-sign product averages to 1−2θ/π, so adding the positive constant c−π/2 gives PSD in every dimension. Two distinct antipodal pairs with coefficients (1,1,−1,−1) witness failure of strict PD. On S², integrate the Legendre ODE twice: [sin θ P_n(cos θ)] at θ=c contributes −sin c P_n(cos c), while zero has no boundary term, giving the exact displayed sign and normalization of I_n. The generating-function expansion into frequencies n−2k has nonnegative weights summing to one; away from the central k range integrated frequencies give O(1/n), and in the central range the weights are O(1/n) and the sum of frequency reciprocal bounds contributes the log, including the two resonances. In DLMF 18.15.12–13, taking M=1 and simplifying the signed binomial gives the claimed amplitude and phase and an O_c(n^(−3/2)) pointwise error. Dividing by n(n+1) yields the stated leading term and remainder. For rational c/(2π) the equally spaced orbit has at least three points: their cosines sum to zero and cannot all vanish. For irrational c/(2π) density gives both signs bounded away from zero. The lower-order error cannot remove these strict subsequence signs. Schoenberg's criterion and equatorial S² restriction exclude all higher dimensions.

## originality

PASS

The result proves the exact per-cutoff PSD boundary and an infinite-sign asymptotic for the linear profile. Its framework and positive side are classical. Earlier truncated-power statements include a threshold conjecture, a result at and above power 3/2 for small support, and a close quadratic calculation; the inspected results do not imply the frozen linear classification or its coefficient asymptotic. The quadratic proof supplies a related method and should be distinguished from an earlier theorem covering this claim.

## value

PASS

This gives a useful exact dimension and support boundary for the simplest compact geodesic covariance candidate. It rules out even cutoffs arbitrarily close to π on S² while the untruncated limit is PSD, and identifies the negative high-frequency mechanism and its scale. The distinction between a strict sign obstruction at every proper support and merely lacking a sufficient criterion is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
