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

The finite checker `verify.py` constructs the closed neighborhoods from adjacency, reconstructs the geometric fixed-point orbit-complex for 233 subgroup/parameter cases over ten multipartition profiles, and performs exact reduced mod-two boundary-rank calculations. Run `python3 verify.py`; the recorded unmodified output is `verify_output.txt` and ends `ALL_VERIFY_OK`.

The proof, not the finite tests, establishes every integral homotopy type for arbitrary finite parameters and arbitrary part-preserving subgroups. The checker does not test all subgroups or certify integral homology independently. No independent audit has been performed.
