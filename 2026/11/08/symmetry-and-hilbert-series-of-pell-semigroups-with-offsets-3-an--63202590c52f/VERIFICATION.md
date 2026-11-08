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

# Verification notes
The included `check_pell35.py` was run using standard-library Python and exact integer arithmetic. It constructs the first Pell numbers, checks the recurrence identities and pairwise gcds, and computes the minimum semigroup element in every residue modulo the first generator by Dijkstra's algorithm. From the actual Apéry array it obtains the Frobenius number and genus, comparing \(2g=F+1\) with the proposed symmetry classification for each \(n\in\{3,\ldots,12\}\). The file `verification_output.txt` is the captured output and terminates in `PELL35_EXACT_APERY_CHECK_OK tested_n=3..12`. The computation does not establish the all-index assertions. These follow from the proof and the specified published three-generator symmetry criterion. No independent audit has been performed.
