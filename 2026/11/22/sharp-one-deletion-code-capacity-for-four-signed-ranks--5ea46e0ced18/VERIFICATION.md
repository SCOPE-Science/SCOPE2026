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

# Reproduction of the finite certificate

Run `python3 verify.py` with Python 3.9 or later and no third-party packages. The expected output starts with `VERIFY_OK` on all three lines. The script independently implements direct deletion and inverse signed-rank insertion, checks their identical incidence relations, checks the exact forty-unit total twice-weight and all 384 source inequalities, and checks twenty specified codewords for 46 disjoint received outputs. There are two unused received words. Both the upper-bound proof and the attaining code are included in `RESULT.md`.

This program covers only the signed four-rank channel defined in `RESULT.md`; it does not test larger ranks, unordered symbols, uncertain signs, or a multiple-deletion channel. Finite exact checks do not constitute independent external mathematical certification.
