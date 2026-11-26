---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Cone equality descends to quotient clusters. At a maximal quotient preimage of t, every world of C_t must be hit in that preimage cluster; the first steps toward lifts of different target children must be different immediate source children. These two arguments apply to arbitrary finite covers and give both necessary thresholds. Every internal target vertex needs a distinct internal source preimage; full k-branching gives exactly 1+kI source clusters for I internal vertices. Padding only the leaves of the internal skeleton attains the bound: target immediate leaves are hit and each internal target child cone is hit recursively. At equality no internal source vertex can be spent on a target leaf; forward and back give an ancestry isomorphism on the unique internal preimages (in the back argument the target vertex is a strict descendant). At a fixed skeleton isomorphism each terminal source cluster must land on a target leaf, and an immediate target leaf of t can only be hit above the source preimage of t by one of its terminal children, not through another target child. All other terminal-child choices among descendant target leaves are independent. Clusterwise surjections and weighted inclusion-exclusion therefore count exactly the maps on the fixed distinguishable-world source. Root-cluster permutations give the c_r divisor, including a singleton target; k=1 and q_t=0 are covered. The bounded checker is not needed for the universal proof; an independent direct enumeration in /workspace/reviews/evidence/pretree.py matched six boundary and weighted cases, including pointed counts, asymmetrical leaves over a symmetric internal skeleton, and both obstructions.

## originality

PASS

Pass for the sharp optimization, equality classification and weighted optimal-cover factorization under the stated tree-quotient assumptions. Qualitative regularization and its usual sufficient parameters are covered, and general exact counting for a fixed pair of unclustered trees is covered; neither is credited as new.

## value

PASS

This quantitatively sharpens a natural finite modal-frame regularization: padding with terminal covers avoids potentially exponential internal-branch replication, and the equality characterization determines the only minimum shape. The weighted formula distinguishes multiple realizations on that shape without enumerating general functions, including nontrivial clusters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
