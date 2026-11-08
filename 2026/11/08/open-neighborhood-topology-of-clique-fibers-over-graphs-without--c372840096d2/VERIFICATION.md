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

# Finite verification of the open-neighborhood classification

Run `python3 verify_clique_fiber_open_girth.py` using Python 3 and its standard library, in the same directory as this document. `verification_output.txt` records one complete successful run. On the packaged files the final line is `ALL_CHECKS_PASS 19 total_verified_elementary_collapses 6844`.

The program builds the Cartesian-product graph from edges, reconstructs all subsets of every *open* neighborhood, and requires that each proposed elementary simplicial-collapse pair has exactly one remaining codimension-one coface. It checks the exact post-collapse face set; every interface's connected crown-graph relation complex, including its spanning-tree rank; the derived collapse count; and independently computed reduced mod-two Betti numbers for all test examples. Tests include trees with branching, a cycle, two cycles sharing one vertex, and the Petersen graph. Tests never use the proposed homotopy formula as a membership predicate.

The mathematically substantive all-parameter assertions—the existence of the two matching stages under the high-girth hypotheses, simple connectivity of row boundaries, and the relative integral \(1\)-\(2\) cell cancellation over each crown interface—are proved in RESULT.md. Finite enumeration and mod-two ranks are corroborating evidence, not a proof of homotopy equivalence for an infinite family, not a test for higher homotopy operations, and not independent mathematical audit. No Lean or external certification is claimed.
