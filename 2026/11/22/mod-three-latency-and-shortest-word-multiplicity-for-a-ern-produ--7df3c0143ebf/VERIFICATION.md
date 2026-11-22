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

The self-contained `verify.py` uses only the Python standard library. Execute `python3 verify.py` in its directory. The output printed during the completed run is included as `verify_output.txt`.

For every integer \(n\) from 3 through 16, the script explores the reachable graph of all pairs of nonempty subset masks for \(C_n\) and \(C_3\), with two exact deterministic letter transitions per state. Breadth-first search yields the first goal depth; path-count propagation along shortest-level edges yields the full number of shortest literal words. The count and depth agree with the claimed closed formulas. For nondivisible \(n\le13\), the script independently enumerates the source one-letter-slack candidate family, verifies it is pairwise distinct and resets \(C_n\), and checks the number also resetting \(C_3\). Witness checks extend to \(n=200\).

The source theorem for the complete one-letter-slack family is cited in `RESULT.md`; this check does not independently prove its all-length completeness. The all-length proof requires the reverse-preimage argument plus the published classification and the modular calculation, rather than extrapolating from finite BFS. No Lean task, external proof service or independent audit is asserted.
