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

Run `python3 verify_gap.py` with Python 3 and no external packages. The script computes digit sums by repeated integer division, checks explicit extremal witnesses for all target residues in bases \(2\) through \(31\), verifies the internal absence of other hits in each witness gap, checks the even-block permutation property and odd-block missing-residue property, and brute-forces consecutive occurrences within a substantial finite prefix for smaller bases.

Observed local output:

```text
VERIFY_OK bases=2..31 residues=all witness_interiors=205280 block_cases=5400 direct_consecutive_gap_checks=1919848
```

The proof requires no unbounded computer search. The checker does **not** certify all infinitely many bases or all indices; it checks exact finite examples of the two structural arguments. The all-base result is the mathematical proof in `RESULT.md`, not the test output. Historical-priority checking remains limited to the cited inspected texts and recorded searches.
