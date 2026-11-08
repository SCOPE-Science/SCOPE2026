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

Run `python3 verify.py` in the same directory as the other files, using Python 3 and no external packages. Compare standard output with `verification_output.txt`, including the terminal `VERIFY_OK` line. The checker constructs finite permutation groups, directly generates the least medial congruence for three representative groups, and compares it with commutator-subgroup orbits. For \(S_3\), \(S_4\) and \(S_5\) it independently enumerates the automorphisms of the resulting small quotient; it verifies orbit totals through \(S_6\). The proof for all integers \(n\ge3\) is given in `RESULT.md` and does not depend on these finite tests. A finite run cannot certify historical novelty or substitute for independent validation.
