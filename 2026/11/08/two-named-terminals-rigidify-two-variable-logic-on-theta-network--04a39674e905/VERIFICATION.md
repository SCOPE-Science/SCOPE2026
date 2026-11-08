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

# Reproducibility and limits

Execute `python verify_two_terminal_theta.py` in the directory containing the two attached verification files. No external packages or network access are used. The output must match `verification_output.txt` byte-for-byte.

The program enumerates all \(84\) unordered three-path length triples from two through eight; checks the exact midpoint witness count for \(884\) examined path lengths; verifies \(1176\) neighbor/nonneighbor configurations; reconstructs all \(84\) path multisets using only existence and at-least-two witness predicates; compares the partition formula for \(22\) edge-count offsets; and executes \(156\) independent noncounting two-variable tuple-refinement comparisons between selected named and unnamed structures.

These checks are finite and do not establish the unrestricted quantifier-depth or unbounded path-length claims. Those statements depend on the distance formula, midpoint lemma and permanent two-pebble strategy supplied in `RESULT.md`. No independent mathematical audit has been performed.
