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

# Computational reproducibility and proof boundaries

Execute `python3 verify.py` in the same directory. It uses only the Python standard library and compares direct semigroup membership by dynamic programming to a separately computed cyclic count formula. It also independently tests the cyclic discrepancy inequality across all unit-residue pairs for moduli \(2\) through \(180\), and verifies the explicitly constructed lower-bound witnesses over the same range.

Observed run: 10,743 matching direct semigroup examples; 835,733 unit-residue tests; all 179 witness moduli correct. The script's assertions stop execution on any discrepancy. Infinite validity follows from the written floor and subset inequalities, not from these finite checks.

No independent audit or formal mechanized verification has been performed. Earlier literature may contain a differently expressed quantitative bound; the assessed originality is limited to the checked sources.
