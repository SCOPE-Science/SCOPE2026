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

A spanning tree deletes exactly two edges, from distinct paths or the other two paths would form a cycle. Conversely cutting one edge on each of two paths connects both resulting pieces of each via the intact path. In weighted tree edge-voltage coordinates the tree energy is Euclidean, and the two omitted-edge energies are squared signed sums along their replacement paths. Their two coefficient vectors have Gram matrix diag(ℓ_i−1,ℓ_j−1)+(ℓ_r/w_r)vvᵀ with v=(√w_i,±√w_j), since the only shared edges are in arm r. This verifies positive definiteness, both nonunit eigenvalues, the n−3 unit eigenvalues on the quotient, and position independence. The diagonal entries are exactly the two omitted stretches. For (2,2,3) and (6,6,t), the two short-retention objectives increase while the two long-retention objectives decrease. Direct substitution gives equality at 36/5 for the upper eigenvalue increments and at 3(√57−3)/2 for stretch, with 7 strictly in between, so the optimizer sets are disjoint exactly on the claimed interval. At t=7, exact grounded Laplacian determinants independently gave monic polynomials (λ−1)^3(3λ²−28λ+50)/3 and (λ−1)^3(λ−2)(7λ−50)/7 for short and long retention. At n=5 all arms have length two and both objectives increase with (sum of other weights)/w_r, so they share the same maximizing-weight retained arms even at ties.

## originality

PASS

The generic cycle-space/Gram reduction and stretch trace are standard and the existence of a stretch-versus-condition-number reversal in general is not counted as new. The distinct supported finding is the explicit deletion-position-independent theta optimization, together with a sharp six-vertex switching interval and minimality in the stated family. No read distinct work supplied or directly implied that specific extremal classification.

## value

PASS

This is an exact calibration example for a standard surrogate in preconditioning. In the smallest eligible graph the trace-optimal and condition-optimal tree sets are disjoint on a whole open interval, not merely reversed for two arbitrarily chosen trees. The explicit intervals isolate the role of correlated replacement paths in the spectral objective and allow an algorithmic comparison to be checked without numerical eigensolver uncertainty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
