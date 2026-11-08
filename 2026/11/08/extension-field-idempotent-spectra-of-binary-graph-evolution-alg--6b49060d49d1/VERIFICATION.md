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

The included `verify.py` is a standalone Python standard-library calculation; run `python3 verify.py` from the directory containing this file. It directly enumerates idempotents in the algebras over explicit finite fields and separately computes the predicted binary nullities. A successful execution ends in `VERIFY_OK`.

All binary matrices were checked for dimensions one through three over the indicated binary fields, as detailed in `RESULT.md`. Six four-dimensional mixed examples over \(\mathbb F_{16}\), the degree-seven delayed-appearance example over \(\mathbb F_{128}\), and directed cycles of sizes 1–8 and extension degrees 1–20 were also checked. The finite calculations test the formula only on those instances; they are not an exhaustive argument for arbitrary dimension or extension degree. The independent mathematical audit has not been performed.
