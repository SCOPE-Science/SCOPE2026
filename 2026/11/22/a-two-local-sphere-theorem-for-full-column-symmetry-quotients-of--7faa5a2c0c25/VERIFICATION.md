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

The capacity bound in Jojić–Panina–Vrećica–Živaljević, Theorem 6.1, is 2n ≥ 6+3−1, giving four-connectivity of the cover for n≥4. Each column transposition fixes a vertex outside its swapped pair, so the fixed-point generators exhaust the acting group in Armstrong's orbit fundamental-group formula. On a closed flag simplex, any two points identified by the action have the same face-cardinality support: there is at most one vertex of each cardinality in that flag, so they are the same point. This gives regular quotient cells, and their faces are exactly the flag deletions. I recomputed the complete boundary ranks independently by enumerating the allowed largest-face column masks, enumerating all labeled subset flags ending at each such face, then identifying flags by sorted cumulative column histories. Replay: python3 -B /workspace/quotient_recompute.py 4 5 6. Counts match the frozen table and the rank lists are (76,1084,4493,6841,3419), (82,1264,5519,8731,4499), and (83,1288,5633,8911,4589), with boundary-square zero and Betti vector (1,0,0,0,0,1) in each case. An occupied-column injection or bijection extends to a column permutation, and at most six columns occur in any largest face; this proves all-width stabilization and PL compatibility, not merely agreement of sampled Betti numbers. Finite generation and universal coefficients remove lower two-local homology and all two-primary torsion; top homology is free of rank one. Simply connected localization, the first nonzero Hurewicz class, and localized Whitehead give the stated two-local sphere, not an integral equivalence.

## originality

PASS

The inspected comparisons cover connectivity and homotopy of the cover, or a different column action. They do not give the characteristic-two geometric full-symmetric quotient invariant. The exact indexed matching record is the assigned result itself, not another theorem.

## value

PASS

For a natural full column action with many stabilizers, the actual quotient mod-two homology cannot be read off from the nonequivariant wedge or from rational representations. The complete orbit calculation and finite stabilization yield a uniform homotopy classification at the prime where the elementary averaging argument fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
