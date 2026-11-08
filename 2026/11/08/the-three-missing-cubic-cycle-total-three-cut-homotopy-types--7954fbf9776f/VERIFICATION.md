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

# Verification instructions and scope

The standalone exact verifier `bounded_cycle_verifier.py` requires Python 3 and only the standard library. Execute `python3 bounded_cycle_verifier.py` in a directory containing the script. Compare its stdout to `checks.txt`. It reconstructs the graph from cyclic distances, enumerates all independent triples and every bounded-independence face, generates all cover relations in the nonempty face poset, applies the fully specified lexicographic pivot matching, and verifies the **entire** reversed-arrow Hasse diagram is acyclic by a topological sort. Its own mod-two boundary-matrix ranks provide an additional arithmetic check, and every dual face of dimensions zero, one and two is explicitly verified.

The complete computed counts for \(n=13,14,15\) are respectively: independent triples \(13,28,50\); total faces including empty \(2757,3277,3964\); Hasse cover edges \(13663,16100,19500\); matched pairs \(1377,1637,1980\). Critical-cell patterns are \(\{0:1,5:1\}\), \(\{0:1,5:1\}\), and \(\{0:1,4:2\}\), where each key denotes cell dimension. The independent mod-two homology checks identify precisely one generator in degree five, one in degree five, and two in degree four. No randomized tests, samples, timeouts, or external assertions replace the exhaustive finite verification.

The leap from the finite certificate to integral homotopy requires two standard theorems, both applied explicitly in `RESULT.md`: Forman's acyclic discrete Morse theorem and combinatorial Alexander duality together with simple connectivity and Hurewicz/Whitehead. The verifier itself does not certify any work outside the three specified lengths, any general recurrence, or an independent audit.
