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

The analytical argument is in `RESULT.md`, including the strict arm-replacement inequality, explicit integer-discrepancy witnesses, and permutation-module rank formula. Those steps prove the infinite family without relying on finite enumeration.

For an independent finite arithmetic check, run `python CHECKER.py` using Python 3 and SymPy. The script enumerates all signed edge increments in 30 mixed-arm spiders, computes rational centered norms directly from vertex potentials, and computes the rank of direct contact-potential matrices. It then compares against the explicit discrepancy, contact, and affine-dimension formulas. Expected final line:

`MIXED_ARM_SPIDER_ALL_CHECKS_PASS`

The tested domain satisfies \(2\le q\le6\), \(1\le p\le11\), \(p+2q\le14\), representing 152,928 signed potentials in total. This verification is finite only. No independent audit, proof-assistant verification, or external certification has been performed.
