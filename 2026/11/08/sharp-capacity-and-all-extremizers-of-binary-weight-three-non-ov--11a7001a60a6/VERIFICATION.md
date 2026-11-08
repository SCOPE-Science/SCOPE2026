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

# Reproducibility

Run `python verify.py` with a standard Python 3 installation. The program checks 15,156 ordered pairwise comparisons in the analytically admissible candidate region through length \(18\), performs exact compatibility-graph maximum-clique and maximum-codebook counts through length \(9\), and verifies construction sizes and the residue-three maximizer pattern through length \(18\). It prints `VERIFY_OK` on success.

The direct finite checks cannot certify a theorem for every length. The infinite statement follows from the explicit orientation, index-bound, converse compatibility and integer-optimization proof in `RESULT.md`.

No independent mathematical audit has been performed. Historical priority has only been compared against the listed accessible literature and record searches.
