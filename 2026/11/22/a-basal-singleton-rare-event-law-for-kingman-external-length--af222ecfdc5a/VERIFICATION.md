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

For one named leaf, the avoidance factors at k=n,...,3 telescope to 2/[n(n−1)]; for n≥3 the n events are disjoint. Conditioned on survival, each history of the other lineages gets the same avoidance factor (depending only on the current k), so those histories retain the (n−1)-Kingman topology and the n-sample holding times are unchanged. At k≥2 the conditional singleton mean is 1+(k−1)(k−2)/(n−2), including k=2. Multiplying by 2/[k(k−1)] and summing gives the claimed mean and, since E[L_n]=2, the claimed covariance. The numerator after removing the positive factor is n−2H_n+2/n, which starts at zero and increases by 1−2/n per step. An independent rational dynamic program on states (k,w) used transition multiplicities binom(w,2), w(k−w), binom(k−w,2) for losses of 2, 1, 0 singletons; it tracked P(R), E[L 1_R] and E[L] and matched through n=25 (n=4 gives 2/3, 7/3 conditional mean, 2/9 covariance). For the limiting claim the held-out leaf contributes the entire height, and each other-stage time is shorter than the corresponding (n−1)-sample time by the factor (m−1)/(m+1) on the same exponential. The expected missing length is 4(H_n−3/2)/(n−2). Janson–Kersting give ordinary external-length variance O(log n/n) in the same pair-rate-one normalization, so the other-leaf length tends to two in L1. The height converges in L1 by summability; no independence between it and the remaining length is necessary for Slutsky. Its Laplace product and nondegeneracy (independent rate-one final interval) are valid.

## originality

PASS

Best-of-knowledge support for the aggregate external-length law on an exact rare topology, not for standard singleton survival, the root split probability in isolation, or standard Kingman external-length concentration. The closest longest-branch reference remains only partially accessible; its described statistics do not give the conditional aggregate, and no decisive stronger or equivalent result is evidenced by the inspected material.

## value

PASS

This event has probability of order 1/n but a genuine order-one effect on the entire external-length distribution. It supplies an identifiable genealogy for excess external length that is not described by typical Gaussian fluctuations, quantifies the finite association, and isolates the remaining randomness as the height.

The dated certificate retains the supplied scientific assessment, sources and limitations.
