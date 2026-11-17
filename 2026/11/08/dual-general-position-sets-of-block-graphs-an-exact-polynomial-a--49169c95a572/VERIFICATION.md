---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Proof on arbitrary connected block graphs: simplicial vertices never appear internally on a geodesic, so any subset works. A selected cut vertex c forces at most one selected and at most one unselected component of G-c, hence c has exactly two pure branches and selected set equals one branch plus c. General position forces selected branch to be a full pendant clique with c its only cut vertex and c occurring in two blocks. Conversely this clique has geodesically convex complement. This proves D_G=(1+z)^s+sum_B z^|B| and hereditary iff correction absent; blocks of size k<=s. Independent exhaustive P4 vertex-subset test yields [1,2,3,0,0], including the single qualified leaf-degree2 edge correction; universal claim proven structurally, not from small enumeration.

## originality

PASS

Tian–Klavžar Theorem 3.1 supplies dual iff complement geodesically convex, simplicial construction and the maximum dual gp count on block graphs, not a complete all-subset polynomial or the qualified pendant-block characterization. Earlier published general-position polynomial for block graphs concerns ordinary gp, not the dual complement-convex property. Submitted exact classification and hereditary boundary are not entailed by those primary statements.

## value

PASS

All-size enumeration of dual general-position sets over the natural broad hereditary family of connected block graphs is a motivated exact graph invariant. The additional correction for degree-two articulated pendant cliques detects the failure of downward closure; coefficients recover structural pendant-block size distribution. This is a nontrivial full classification rather than repeating known maximum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
