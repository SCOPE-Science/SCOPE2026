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

# Reproduction and limits

Run `python checker.py` after installing the dependency recorded in `requirements.txt`. The executable produces 120 seeded face-closed filtrations with ties and both dimensions 0 and 1, constructs their true boundary matrices, performs exact rational persistence reduction, then compares the full fixed-end rank-one sweep with independent null-space projection matrices for each event and also checks every available filtration index pair. Expected output:

```
PASS exact rational: seed 718 sampled filtrations 120 checks {0: 731, 1: 238} cases {0: 120, 1: 73}
```

These are 969 exact event comparisons plus off-grid comparisons; no test of arbitrary-dimensional infinite families is claimed. The proof of the general theorem is in `RESULT.md`.

The arithmetic bound excludes numerical-conditioning costs, eigendecomposition, and explicit materialization of every off-grid matrix. The new sweep uses known persistence reduction and Gram–Schmidt ingredients; its amortized global bound is not an unconditional complexity statement about the original implementation. Independent audit has not been performed.
