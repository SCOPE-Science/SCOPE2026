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

Run `python3 CHECK.py`. This standalone Python 3 script independently computes the Apéry minimum by Dijkstra search for each residue class, directly constructs the finite gap word through the Frobenius number, counts maximal gap-run lengths, and compares each with the stated coin-cost formula for every multiplicity from 3 through 319. It also verifies the perfectness boundary and paired-run totals for the 25 parameter pairs \(1\le s,n\le5\).

These tests were executed successfully. The theorem for infinitely many multiplicities is established in RESULT.md by the Apéry-threshold calculation, the unit-jump lemma, and a direct row-by-row gap-run count; it is not inferred from finite enumeration. An independent mathematical audit has not yet been performed, and bibliographic priority is not independently certified.
