---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The reduced CTMC rates (k-m)(alpha*h+eta/2), m[alpha(1-h)+eta/2], and hub flip eta/2+beta m/k or eta/2+beta(k-m)/k follow from independent clocks. Applying the generator to r distinct leaf products closes F_r and H-products G_r. Eliminating F_{r+1} gives the displayed positive denominator r(alpha+eta)+eta+beta[1-(k-r)alpha/(k(alpha+eta))]>0; at r=k its unwanted F_{k+1} coefficient is zero. Polynomial expansion E[s^M]=sum_r binom(k,r)F_r(s-1)^r gives the exact binomial inversion and full law, with no asymptotic approximation. Strict eta>0 ensures unique stationary state. Independent rational 8-state generator solved for k=3, alpha=beta=eta=1 and matched full marginals (17,27,27,17)/88 and F=(1,1/2,13/44,17/88), G=(1/2,15/44,21/88,15/88). Beta-limit moment argument fixes the fixed-rate limiting law, but is not the novel part.

## originality

PASS

PASS on the distinct exact O(k) triangular all-order finite-size stationary joint law; existing exact stationary variance and beta-limit papers cover only second moments or the scaling limit. General noisy voter duality remains a real uninspected-article priority risk.

## value

PASS

Natural finite-star stationary probabilities and hub/count correlations are not determined by variance or limiting beta density. Exact positive-denominator O(k) moment recursion and O(k^2) inversion furnish a reusable all-k benchmark of the full finite stationary measure, rather than a normalization exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
