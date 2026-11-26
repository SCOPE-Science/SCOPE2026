---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A connected k-vertex set of a tree is an open component exactly when its k−1 internal edges are open and all b boundary edges are closed. The independent uniform source contributes k/n. For each k, divide by (k/n)p^(k−1); equality on 0<p<1 then gives equality of all coefficients of the polynomial in 1−p. The conversion to coefficients indexed by total open edges also holds: the n−k−b remaining edges are unconstrained. I independently enumerated multisets of rooted branches and deduplicated by the minimum canonical encoding over all roots, rather than using leaf-addition with center rooting. I computed each profile by a rooted polynomial recurrence: an included vertex contributes x and each child branch contributes either y if omitted or its own connected-root profile if included. Summing over the highest included vertex adds one y for a nonroot highest vertex. This exhaustive reconstruction gave respectively 1,1,1,2,3,6,11,23,47,106,235 unrooted trees; there were no repeated profiles through ten and exactly one double class at eleven. The witnesses in that class reproduce the boundary certificate, ordered distance histogram, mean and half-probability vector. They are nonisomorphic by the distances of the degree-three vertices to the unique degree-four vertex. Replay: python3 -B /workspace/branches/independent-checks/record4.py. This checks the stated homogeneous undirected bond model with an unobserved uniform source, not a general epidemic process.

## originality

FAIL

Shown already known under an exactly equivalent invariant. Aliste-Prieto, Martin, Wagner and Zamora, Chromatic symmetric functions and polynomial invariants of trees (DOI 10.1112/blms.13144), §2.2 equations (4)–(5), define the half-generalized degree polynomial H_T, with h_T(b,c) the number of connected sets with b boundary edges and c internal edges. On trees c=k−1, so h_T(b,c)=B_T(c+1,b) and H_T(y,z)=∑ B_T(k,b)y^b z^(k−1). The same paper explicitly identifies its Fig. 2 pair as the two smallest trees with the same HDP, both directly after (5) and in Example 10. The two caterpillars there are exactly the assigned pair. The frozen theorem is the same first-collision classification, with an elementary rewrite of the known coefficients as uniform-source bond probabilities. The overlap is not merely a conjectured match to a stronger invariant or an inaccessible source.

## value

FAIL

The topology-identification question is natural, but the frozen sharp cutoff and its witness already exist for exactly the same invariant. Rewriting that invariant as a uniform-source bond law is an elementary conditioning argument, and the displayed numerical examples are recoverable from the known pair. The independent computation validates the result but is not a new classification. No distinct substantive claim remains here to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
