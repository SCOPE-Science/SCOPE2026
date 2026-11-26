---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The tensor-sum Laplacian splits into increasing cycle spectra λ_j and λ_j+2w. There is at most one contributing space per parity at an eigenvalue, even if the same weight creates several distinct collisions. The harmonic dimensions and the PBH dimension bound give the claimed partition. On S_4, sums and differences across layers at each of positions 0,1 separate the two parity components; both are recovered by sine minors or singleton observations. On S_3 a colliding singleton is isolated at position 0 by parity, and the other component's sine coefficient is detected at position 1. In the two-input regimes sine minors suffice except at even w=2, where the merged singleton columns give full rank for adjacent same-layer sites. At arbitrary separation d, the least positive harmonic index for a vanishing sine is n/gcd(n,2d); checking whether it lies in I_n yields the gcd criterion, including d=0. At even w=2 the extra determinant compares the layer sign with the alternating spatial sign. n=3,4 have only one double harmonic; n=5 has interior cosine gap √5/2. Independent exact rational ranks passed at five instances, including every pair in n=4,w=2; n=6,w=2; and n=8,w=3 (/workspace/independent_checks.py). These are spot checks of the all-parameter proof.

## originality

FAIL

Resultary 17a8333c0dda proves the exact same minimum for every n and w in collision-multiplicity notation, with the same optimal nested witnesses and even w=2 exception. It does not explicitly tabulate all optimal pairs. That remaining assertion follows mechanically from its explicit eigenspaces and PBH restriction: in each unmerged parity band the second observation differs from its bare-cycle counterpart only by a nonzero sign, so apply the known two-site cycle criterion. For the sole two-dimensional merged level, the displayed product basis of an alternating symmetric vector and a constant antisymmetric vector restricts to (1,(-1)^d) and (1,(-1)^t); independence is exactly the claimed extra sign test. There is no other two-site case. Coverage is distinct from chronological priority, which is not established from the October and November catalog paths.

## value

FAIL

Sharp hardware-count and placement criteria are useful for this model, but the count, sharp witnesses and exceptional weight are already available in the matching indexed result. The remaining criterion is the cycle gcd test plus a direct two-column sign comparison using the known product basis; it does not supply a substantively distinct unknown exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
