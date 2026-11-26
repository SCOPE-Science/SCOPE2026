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

Counted all cliques directly: each insertion adds k new cliques, exactly k−1 through a marked selected vertex, and k−2 through a selected pair. The increments for the marked counts therefore have conditional joint success probability B/M and marginal A/M. Expanding their products gives the two moment recurrences; substituting the P_s solutions verifies both forcing terms using 2a−b=k and 2a−a=a, and the seed values verify the integration constants. After centering, covariance forcing has sign β−μ²/M. The ratio μ²/(Mβ) starts above 1 and multiplies at each insertion by 1+1/[(M+k)(M+b)] because a lies exactly between b and k with spacing 1. Thus all forcing terms are strictly negative; the first-step law is equivalently omission of one uniform seed vertex and gives −1/(k+1)^2. Normalizing the centered recurrences by P_(2a), the covariance forcing summands are O((j+1)^−2), all negative, while the variance summands are positive and O((j+1)^(-1−a/k)). The latter sign follows also from the deterministic presence of an initial clique missing each seed vertex. This rules out zero leading coefficients; taking gamma-product ratios gives the stated constants. Substitution of k=2 gives the displayed finite formulas and (3−π)/(4−π), including its numerical sign. The k=2 example of late positive conditional covariance is consistent with the unconditional proof. The checker enumerates actual graphs for finite inputs and is not the proof for all k,m.

## originality

PASS

Best-of-knowledge pass for the all-size strict sign and explicit strictly negative limiting correlation in the stated growth model. One-vertex degree histograms and root limit results are credited and do not give these joint quantities. The general urn representation is not claimed as new.

## value

PASS

A resolved dependence question for two natural distinguished vertices of a standard growth process. Simultaneous attachment is possible and conditional covariance can even be positive, so the strict unconditional sign at every size is not a one-step exclusion argument. The nonzero limiting correlation distinguishes persistent dependence from a transient initialization effect and gives a usable baseline for pair moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
