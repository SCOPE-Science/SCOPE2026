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

# Verification of the finite integral certificate

Run `python3 evidence/verify.py` on the extracted evidence package, using standard Python 3. The source program itself constructs the complete ordinary cut complex directly from the graph's adjacency predicate, not from a cached face list, reference output or previously generated certificate. It then matches faces, explicitly tests the directed Hasse graph for cycles, constructs integer Morse boundaries by signed gradient-path substitutions, and calculates direct simplicial mod-two ranks independently of the Morse reduction.

The full observed execution is in `evidence/CHECK_OUTPUT.txt` and ends with `PASS`. The actual recomputation checks 264 disconnected induced five-sets, all 2,489 faces, 1,218 matching pairs, and 2,488 nonempty Hasse vertices. It finds a single primitive Smith factor one in the five-to-four Morse boundary; the six-to-five boundary vanishes. The direct mod-two ranks are \((11,55,165,327,433,228)\) in degrees one through six. Together these are sufficient finite computations for the exact integral homology of this single finite complex.

No infinite-family statement, computational complexity bound, full homotopy-type classification, or external independent audit is claimed. Integer acyclicity and primitive matrix entries, rather than an experiment over one finite field, are the decisive checks for the integral statement.
