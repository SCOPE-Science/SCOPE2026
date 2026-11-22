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

The companion `verify_potts.py` uses only Python 3 standard-library exact integers and rational numbers. Run `python3 verify_potts.py` in the extracted directory; it verifies every exact integer dual inequality, every periodic witness, and eleven independently computed length-20 ground energies. It does not independently certify all previously published material, full historical priority or the limiting argument; those are given as a mathematical proof in `RESULT.md`. The finite checks do not substitute for proof at arbitrary length.
