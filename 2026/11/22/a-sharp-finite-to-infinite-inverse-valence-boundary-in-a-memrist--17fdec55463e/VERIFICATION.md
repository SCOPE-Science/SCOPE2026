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

The map agrees with Wang et al., Eq. (4). Eliminating the first and third coordinates fixes z=Z−y and x=σ(y+1−X)/a with y≥X−1; the signs describe distinct points except at the kink. Analyticity and nonconstancy of each scalar equation exclude infinitely many roots on any compact interval. For k<c=b/a the lower bound |Y|≥(c−k)y−c|1−X| for y≥0 is uniform on compact target sets and gives properness by continuity. For k>c, the scalar equation divided by y converges in C¹ on translated phase cells to σc+k sin(Z−y); its two simple zeros have disjoint monotonic neighborhoods and their complement stays away from zero. This gives four distinct antecedents per remote full period, with bounded edge error, and all remote roots are regular. At k=c, each sheet reduces at its sine extremum to c(u_j+s)(1−cos s)=δ with the stated signed target offset. A negative offset has no high roots, zero gives one singular root, and a positive one gives two simple roots by strict half-neighborhood monotonicity. The Taylor expansion gives s=±sqrt(2δ/(cu_j))+O(u_j^-1). The Jacobian is −aσH′_σ away from the kink; in particular (1,0,0) has an unbounded critical fiber, so equality is nonproper. This controls every fixed real target; it is not a theorem about histories in a bounded invariant region. The frozen numerical diagnostics are supplementary and were inspected, not used as the proof.

## originality

PASS

The original forward map and its Jacobian are prior. The closest inspected inverse counting results concern inequivalent maps with different leading phase equations and do not give the positive threshold k=b/a or this target-dependent critical inverse diagram. Priority outside the checked evidence is not certified.

## value

PASS

Gives a global properness and predecessor-multiplicity classification for a published nonsmooth dynamical map. At the exact coupling boundary the target determines whether there are finitely or infinitely many inverse branches and whether the remote branches are singular; this is strictly more information than the local Jacobian or forward numerical behavior. The leading counts and fold scaling quantify the classification without claiming consequences for bounded operating states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
