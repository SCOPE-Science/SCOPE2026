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

# Verification record
The self-contained result gives analytic proof steps 1–5, covering the exact diameter, uniform radial and arclength first variations, near-antipodal localization, dominated convergence, and both profile-tail constants. A separate executable file `verify_entropy_chords.py` uses NumPy/SciPy to integrate actual finite-deficit Euclidean-arclength point-pair events and the limiting profile; executing it produced `ALL_CHECKS_PASSED 20`.

The computations are finite diagnostics, not machine-checked infinite proofs. The first public archival source date used in this result is documented by the initial May 11, 2006 arXiv submission of Mayer and Molchanov, not the subsequent version date. No independent audit is available; no code result is represented as third-party validation.
