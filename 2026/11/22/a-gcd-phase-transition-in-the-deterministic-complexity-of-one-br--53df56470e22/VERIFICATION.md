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

# Reproduction and checked limits

Use Python 3 with no additional libraries. From the directory containing the files, run `python3 verify_subset.py` and `python3 verify_quotient.py` and compare the plain-text outputs with the bundled `.txt` files. The first independently constructs the original NFA with bitmask states, performs reachable subset traversal and complete DFA partition refinement for all \(1\le r,s\le7\), and checks direct language membership on all short binary inputs for \(r,s\le4\). The second uses a canonical transition representation, generates explicit prefixes for reachable states, and constructs distinguishing suffixes for non-equivalent pairs for \(1\le r,s\le6\). Both completed successfully.

The finite checks are exhaustive only for the stated finite ranges. They do not prove the all-parameter claim; the all-parameter proof is in `RESULT.md`. Independent mathematical review, third-party checking, and external certification have not been performed.
