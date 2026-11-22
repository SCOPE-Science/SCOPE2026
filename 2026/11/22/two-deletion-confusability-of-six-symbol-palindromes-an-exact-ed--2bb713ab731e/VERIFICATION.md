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

# Reproducibility checks

From the package directory, run `python3 checks/verify_patterns.py` and `python3 checks/verify_direct.py` with the Python 3 standard library. The first enumerates every set partition of six variable positions through a restricted-growth recursion, computes longest common subsequences of the corresponding palindrome pairs, and checks the 203 templates and qualifying support multiplicities. The second constructs all two-position deletion shadows explicitly for alphabet sizes one through seven, verifies the graph and degree table, and checks explicit greedy three-subset constructions for alphabets up to size thirty. The observed terminal output included `PATTERN_OK` and `DIRECT_OK`.

The all-alphabet edge identity follows from the complete equality-partition enumeration with falling-factorial relabeling, rather than from tests over only selected alphabet sizes. The degree dependence uses the proof that at most one fresh letter can occur in a neighbor. The code-size bounds are proved graph-theoretically and constructively, not by a solver's unverified optimum. This review does not represent independent external validation.
