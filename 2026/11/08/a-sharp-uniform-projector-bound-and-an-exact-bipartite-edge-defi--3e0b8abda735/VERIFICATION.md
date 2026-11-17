---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Gram M=diag(alpha)+(2D+W)/6 is positive definite. Convexity of integrated nodal evaluation kernels reduces the L-infinity projector norm to vertices. The comparison resolvent B=diag(alpha)+(2D-W)/6 has positive inverse, |M^{-1}|<=B^{-1}, q=3B1-2alpha and gives norm<=3 with strictness from atoms, odd cycles, or bipartite edge sign cancellation. For bipartite G, SM S=B, so exact row value Lambda_v=3-2sum(alpha_i a_vi)-sum_e w_e a_vi a_vj/(a_vi+a_vj). The graded path recurrence yields endpoint limit 3-2^(4-n)/3 for fixed n, hence unattained sharp 3. Independently inverted rational weighted 3-vertex example with atoms, verifying all exact row deficits, but no finite sample replaces analytic proof.

## originality

PASS

PASS for the **combined extended claim**, not for its already-known universal constant. The Nov 2 published metric-graph result already proves ||P||<3 for simple graphs without atoms and sharp 3 by hypercubes, so these pieces are expressly prior coverage. This submission additionally includes nonnegative vertex atoms, multigraph edges, an exact positive bipartite atom-and-edge deficit and extremizer classification, and fixed-order geometrically graded path limit; these parameter-specific formulas are not stated or implied as complete equalities by the prior bound alone. They survive as motivated mathematically exact quantities.

## value

PASS

PASS: The full bipartite deficit is a directly usable exact stability invariant for nodal finite-element projections with edge mass and endpoint atoms, including norming vertices and all sharp kernel sign inputs. Atom-driven sign cancellation and graded-path asymptotics are natural structural refinements even though the bare constant 3 was known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
