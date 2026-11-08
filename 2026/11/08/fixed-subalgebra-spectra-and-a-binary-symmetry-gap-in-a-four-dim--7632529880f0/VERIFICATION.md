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

# Reproducibility and limits

Two standalone Python 3 scripts are included with the theorem: `verify_fixed.py` and `verify_direct.py`. Execute them directly, without dependencies. `verify_fixed.py` enumerates all unital endomorphisms of the four-dimensional algebra for \(q=2,4,8\), performs exact elimination over the corresponding binary fields, and checks both fixed-dimension polynomials. It must print `VERIFY_OK_FIXED`. `verify_direct.py` constructs images of the algebra generators, verifies their square-zero relations, evaluates every algebra element under every endomorphism for \(q=2,4\), and checks the counts and Burnside identity without relying on the rank-formula implementation. It must print `VERIFY_OK_DIRECT`.

Observed endomorphism distributions for \(q=2,4,8\): `(16,38,9,1)`, `(2176,1844,75,1)`, `(197632,63944,567,1)`. Observed automorphism distributions: `(0,14,9,1)`, `(1280,1524,75,1)`, `(165888,59336,567,1)`. The program checks finite fields only; the theorem for all powers of two is proved algebraically in `RESULT.md`. No independent audit has been performed.
