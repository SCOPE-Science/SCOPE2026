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

# Verification scope

Analytically checked: the fourth-autocorrelation Fourier product identity with unnormalized conventions; magnitude recovery without lower-order data; pair-sum phase ratios from reality; independence of the increments; strict three-erasure-set union bound; character multiplicativity and extension over an index-two quotient; and the exact six-point obstruction. Each step is proved in `RESULT.md`.

Executable checks: run `python3 CHECK.py` with a standard Python 3 interpreter. The script enumerates cyclic groups of order at most 18 and all their admissible spectral holes, verifies the two- and three-translate intersections, and compares all relevant zero-sum four-frequency products for the sharpness pair. A passing execution prints `CHECKS_PASSED`.

Limitations: finite enumeration does not prove the theorem for unbounded group sizes or for noncyclic groups; the general proof does. No experimental reconstruction stability or independent mathematical audit is claimed.
