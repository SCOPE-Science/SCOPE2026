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

# Reproduction and scope

The two standard-library Python 3 verification scripts operate on finite cases only, and were run directly against the embedded code after extraction from the JSONL package. Execute `python3 verification/check_literal.py` and `python3 verification/check_dp.py` from the finding root, then compare their exact single-line stdout with `verification/literal_output.txt` and `verification/dp_output.txt`, respectively.

The first script independently enumerates all binary words of the computed shortest length and tests both subsequences literally for each of 715 positive parameter quadruples with total input length from 4 through 13 inclusive. It examines 655,464 candidate output words. The second uses a distinct shortest-common-supersequence recursion to compute distinct outputs for 1,296 quadruples with components at most six, and checks all maximizing parameters at every total input length from 4 through 54. Both procedures agree with the formula and equality statement.

These experiments are finite consistency checks and do not establish all-parameter correctness. The all-length proof and disjointness of zero-sharing versus one-sharing output classes appear in RESULT.md. All output counts are of distinct words, not embeddings. Scientific literature comparisons are detailed in REVIEW.md and AUDIT.json. No independent scientific audit has been performed.
