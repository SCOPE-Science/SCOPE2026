---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A new interval [u,v] meets precisely the intersection of the suffix r_i≥u and prefix l_i≤v. To realize an interior block [i,j] one needs r_(i−1)<u<v<l_(j+1), along with u≤r_i and v≥l_j. Necessity of the flank bounds follows from hitting i and j and monotonicity; if the flanks are disjoint, take u strictly between r_(i−1) and min(r_i,l_(j+1)), and then v strictly between max(u,l_j) and l_(j+1). This proves sufficiency with a positive-length witness; a free end handles a boundary block, and a distant interval realizes the empty type. The absent blocks are in bijection with edges (a,b) spanning at least two index steps, with exponent b−a−1. An absent consecutive edge partitions the entire graph across that cut, so the consecutive edges form a spanning path in each component and number m−c. The defect is therefore e−m+c, and zero defect means exactly that the consecutive paths are all the edges. This last argument proves the equality case without a claw-free or chordality lemma. The singleton base is covered, and the extension count excludes equalities to named vertices; no re-representation or propriety of the enlarged graph is required.

## originality

PASS

The distinct contribution, under the inspected evidence, is the exact fixed-base obstruction, its degree refinement and cycle-rank defect, not the existence or sharpness of a quadratic bound. No priority certification is made.

## value

PASS

This refines a motivated trace bound from an extremal number into an exact obstruction for each labelled candidate block. For a fixed base it gives both the realizable types of each cardinality and a graph-intrinsic obstruction to saturation, and resolves all equality cases within the proper-base family. The cycle-space defect captures information the general VC dimension and the extremal count lose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
