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

## Exact computational checks
The standalone `verify_s4.py` uses only the Python standard library. Re-run with `python3 verify_s4.py` and compare with `verification_output.txt`. It constructs all thirty directed arcs on six labels, the exact fifteen involution orbits, tests directed-forest admissibility on original arcs (not from a quotient shortcut), enumerates all twelve viable orbit vertices and thirty-six pairwise edges, and verifies that compatibility matches a separate structural criterion. It constructs an eleven-edge graph spanning tree and twenty-five exact integral fundamental cycles, each with zero boundary. It implements the full twenty-four-element residual group, proves faithfulness on a four-point affine set, and computes all first-homology traces by two independent integer methods. It checks every conjugacy-class cardinality, signed edge trace, irreducible multiplicity, and the final dimension.

## What the computations prove and do not prove
Because the finite domain consists of exactly thirty original arc vertices and twenty-four residual group elements, the direct enumeration and signed integer computations exhaust the scope of the stated six-label theorem. The standard geometric orbit-barycenter identification and rational quotient-invariants argument are given separately in `RESULT.md`. The verification does not establish any claims about other label counts or integral quotient homology. Independent mathematical audit has not been performed.
