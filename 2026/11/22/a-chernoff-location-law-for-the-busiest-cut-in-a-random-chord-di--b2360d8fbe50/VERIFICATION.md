---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python verify.py` (Python 3 standard library only). The exact program enumerates all perfect matchings of \(4,6,8,10,12\) endpoints, reconstructs all cut profiles and tests means, variances, transition probabilities conditional on open count, and parity. It passed 195 assertions, including 10,395 twelve-endpoint matchings.

The limiting theorem is justified analytically: verify exact drift from the pairing exposure Markov chain, \(|\xi|\le2\), predictable variance tending uniformly to one in \(n^{2/3}\) windows, the local martingale functional limit, and the dyadic localization bound \(C(n^2/R^3+n/R^2)\). Do not treat the finite enumeration as verification of the infinite limit or of historical originality. The distributional conversion to the standard Chernoff location uses Brownian scaling, not empirical fitting.

No independent mathematical audit has been performed. The references and originality comparison document the remaining risk of an equivalent generic maximum-process result in older literature.
