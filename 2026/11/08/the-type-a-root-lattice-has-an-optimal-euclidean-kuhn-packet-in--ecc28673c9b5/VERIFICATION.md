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

# Reproduction and limits

The file `verify.py` is a standalone standard-library Python 3 checker. Run it in the same directory using `python3 verify.py`.

It enumerates every permutation of the simple roots for each \(1\le n\le7\), constructs all \(n+1\) prefix-sum simplex vertices, and checks exactly (using integer and rational arithmetic) the proposed containing shifted cube, center and cosphere squared radius. It independently computes Eulerian numbers by their recurrence and verifies exact multiplicities. It also checks finitely many lattice-neighbor inequalities in dimensions at most three.

The completed run reported **46,387 exact finite comparisons with no assertion failures**. The code has no external dependencies. A finite check is not an infinite proof, and these computations do not certify originality. The universal claim depends on the self-contained Voronoi and coordinate arguments in `RESULT.md` and the general comparison proved in the cited source.

The difference between a simplex's *circumsphere radius* and its *minimum-enclosing-ball radius* is essential. The proof only uses the circumspheres as upper bounds; it never identifies every circumsphere as a minimum enclosing ball. Historical priority remains provisional. Independent validation or audit has not been performed.
