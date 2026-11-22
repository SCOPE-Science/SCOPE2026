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

## Reproducibility and limits
Run `python3 verify_ep.py` using Python 3.9 or later. It verifies exact polynomial identities, the unique recovered coefficients by descending monic Euclidean division, and strict positivity of the proposed squared couplings for every \(2\le m\le45\) and \(\beta\in\{1,2/3,5/4\}\) using `fractions.Fraction` (132 test scenarios). All-order correctness is furnished by the proof in RESULT.md, not by extrapolating the finite test range. Nonzero subdiagonal entries force each eigenspace to be one-dimensional, so spectral coincidence implies a full Jordan block. Independent audit and finite-precision device modeling have not been performed.
