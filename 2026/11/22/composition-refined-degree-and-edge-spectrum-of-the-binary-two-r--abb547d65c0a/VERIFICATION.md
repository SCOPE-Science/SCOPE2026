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

The proof relies on the published alternating-interval characterization of two common distinct one-deletion descendants. The block-decomposition theorem, edge stratification, extremal degree, and fixed-density limit are proved in `RESULT.md`.

Run `python3 verification/bruteforce.py` and `python3 verification/transfer.py` from the root of the extracted package using Python 3 standard libraries. Outputs for the recorded checks are included in `verification/bruteforce_output.txt` and `verification/transfer_output.txt`.

The first program checks all unordered pairs of binary source words through length 10 by direct deletion-set intersection. The second independently expands the formal two-state block model through length 24 and compares complete word-degree histograms through length 13. The universal assertions are not inferred from these finite checks. No independent audit has been performed.
