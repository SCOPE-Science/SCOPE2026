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

# Verification

The analytical result is established by explicit Gram and binary-spin completions, a product-fiber volume computation, beta integrals, and a gamma-ratio asymptotic; the proof covers every integer \(n\ge1\). The unit-cube normalization is fixed in the theorem statement.

Execute `python verify.py` with Python 3, `numpy`, `scipy`, and `mpmath`. In the documented run it reported `PASS: 2216 deterministic checks`. The checks include \(23\) separate high-precision numerical integrations for each body, direct cut-polytope convex-hull volumes for \(n=1,2,3,4\), explicit valid Gram completions, exact-spin conditional probability constructions for local cut fibers, and large-integer asymptotic consistency.

A finite verifier cannot itself establish the all-dimensional theorem or historical priority. The page-boundary cases \(t=\pm1\) are measure-zero and are handled by closedness. The new full-dimensional elliptope volume has no external independent audit in this package.
