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

PASS. For each fixed p in (3/4,1), q in [0,1], and c>=0, the normalized future elephant martingale R_{n,m}S_m has exact mean preservation and conditional variance R^2[1-(ax/m)^2]. Using the stated published LLT and future FCLT, the expanding-in-time integer interval |S_m|<=floor(c sqrt(n)) becomes the Brownian moving boundary |z+B_u|<=c(1-delta u)^(a/delta), 0<=u<=1/delta. The finite-horizon min/max has no atoms, with immediate Brownian oscillation at z=±c. A late-first-hit decomposition and L2 maximal bound eliminate times m>>n uniformly on compact starting windows; the exponential martingale envelope controls the tails |x|>>sqrt(n). On parity lattice x≡n mod2, the 2n^(-a) local mass and 2/sqrt(n) mesh cancel, giving f_a(0) times the Brownian swept-area integral. The union of continuously moving closed intervals is connected; reflection reduces its mean length to twice the drifted-Brownian supremum. For c=0 reflection gives sqrt(8/(pi delta)); the unique arcsine-distributed argmax differentiates the supremum at c=0 giving 2 Gamma(a/delta+1/2)/(sqrt(pi) Gamma(a/delta+1)). No theorem is asserted uniformly in p, q, c or for noninterval/asymmetric moving targets. The quoted LLT and FCLT are genuinely external proof dependencies, not numerically established here.

## originality

PASS

Originality assessed against semantic published research and the listed primary sources; substantial previously established components explicitly credited. The final model-specific statement is not shown implied by examined prior results; inaccessible full texts remain explicitly qualified.

## value

PASS

PASS. A full one-parameter sharp last-visit crossover at the natural sqrt(n) window explicitly left open by Trinas is a motivated, nontrivial probability law; the swept Brownian geometry and first variation are useful beyond a table or numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
