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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no external packages. The code regenerates the test family from the \(14\) allowable biregular arc patterns between two directed three-cycles: uniform in either direction, or one of six matchings in either minority orientation. For three triangle blocks it tests \(14^3=2744\) labeled pattern selections; \(2310\) have stable refinement classes of size at most three. The predicted signed-graph orbits and automorphism-group orders agree with exact rotational-automorphism enumeration in all \(2310\) cases.

The verifier constructs the explicit nine-vertex negative-triangle witness, confirms that its stable classes have sizes \(3,3,3\) and its automorphism group is trivial, checks one mixed-component construction on twelve vertices with three fixed triangle blocks and one rotating triangle block, and checks four dominating-vertex extensions.

Exact expected output is embedded in `verification_output.txt`; the final line is `VERIFY_OK`. The unrestricted theorem is supported by the symbolic matching-and-rotation proof in `RESULT.md`; these finite tests do not replace that proof. Verification here is not an independent mathematical audit.
