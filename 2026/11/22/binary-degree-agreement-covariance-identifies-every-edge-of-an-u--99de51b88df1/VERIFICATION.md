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

# Reproducible mathematical verification

Run `python3 verify.py` alongside this file in a standard Python 3 environment. The actually executed result was `VERIFY_OK 78 exact host laws, 450 pair covariance identities, 54 gap bounds`.

The verifier independently enumerates signed Bernoulli differences on all labelled simple hosts with two, three or four vertices and four additional heterogeneous five-vertex instances. It uses exact rational arithmetic, compares directly computed joint equality-indicator distributions with the displayed covariance formula, checks the support criterion, and tests the central-gap bounds.

The universal theorem is supported by the analytic independence, conditioning, Fourier inversion, binomial comparison and concentration arguments in RESULT.md; exact finite enumeration does not establish infinitely many cases. No external independent audit or verification has occurred.
