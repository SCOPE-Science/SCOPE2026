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

# Reproduction and boundaries

Run `python3 verify.py` (standard library only) next to this document. The verifier enumerates 450011 integer-coefficient arrays from sixteen small residue grids, confirms the minimal positive support, and checks the explicit CRT witnesses for 99 moduli and three dimensions (297 checks). Its concluding line is `VERIFY_OK`. Arithmetic is exact; no randomized tests are used.

The unrestricted theorem follows from the valuation-normalized Newton expansion, the field degree-two root bound, the two-adic Boolean low-digit support estimate, and exact CRT witnesses in `RESULT.md`. The enumeration alone cannot prove an infinite-parameter classification. The prime-power normalization depends on the actual function being nonzero, and the argument includes all prime-power and one-variable boundary cases.

No independent mathematical audit has been performed. The originality comparison is strongest for the originating arXiv paper and may be incomplete for related quaternary coding theory.
