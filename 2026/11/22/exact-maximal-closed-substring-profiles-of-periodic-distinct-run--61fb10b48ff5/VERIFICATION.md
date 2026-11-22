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

# Verification and scope

The statement is proved for every positive run-length vector on at least three pairwise distinct cyclic run letters, every number of completed periods at least one, and every partial prefix of the next period. See `RESULT.md` for the exhaustive classification into complete unary runs, partial complete returns, and a single possible whole-prefix interval; its proof establishes the formula for all parameters.

The standalone `verify_prefix_mcs.cpp` uses literal longest-border checks followed by internal-border occurrence checks and adjacent one-character-extension maximality. It independently constructs all predicted intervals. Build and run with `c++ -std=c++17 -O2 verify_prefix_mcs.cpp -o verify_prefix_mcs && ./verify_prefix_mcs`. The recorded run output is in `verify_prefix_mcs.txt`. Exhaustive and seeded testing only corroborates the symbolic proof and does not replace it.

The source comparison is limited to the inspected indexed papers, full-text records, and available sections of the run-length preprint. No independent external audit is claimed.
