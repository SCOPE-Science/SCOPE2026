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

# Mathematical verification

The result has an analytic proof based on independently distributed Gaussian signs and absolute values, the Dirichlet moments of normalized squared Gaussians, and the known Johnson incidence spectral theorem. The derivation addresses all integer dimensions and sign counts in the stated domain. In particular, the exact fourth-correlation formula proves the quadratic non-isotropy obstruction for every admissible dimension, not merely those tested computationally.

Run `python3 verify_sign_layer.py` with NumPy installed to construct the full continuous concentration matrix independently by enumerating sign vectors and integrating absolute moments. The test passed 37 complete matrix eigenspectra in dimensions \(4\) through \(8\) (degrees up to \(4\)), with maximum eigenvalue error less than \(8\times10^{-16}\). It also verified the linear tightness criterion for every \(2\le d\le39\) and every sign count. Run `python3 verify_exact_signs.py` using only the Python standard library; the exact rational checks passed all 20,291 dimension/sign-count pairs for \(4\le d\le200\). Both programs test claimed identities but cannot independently certify infinitely many cases or historical novelty.

No independent mathematical audit has been performed.
