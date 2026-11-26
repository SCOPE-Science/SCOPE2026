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

Kim's arXiv:2611.22021 Theorem 4.6 (PDF p. 13) supplies precisely the one-degree concentration and rank, with degree 3t−1 when n=5t and 3t+e−2 otherwise. For an invariant oriented face consisting of h vertex orbits, orientation sign times alternating chain sign is (−1)^(h−1), including the augmented empty-face term. This yields the stated −I(Q_g;−1) and correct trace normalization. Rotation orbits are the residues modulo d=gcd(n,a) in two layers; folding and discarding looped orbits gives signed sums 1,−1,1,−1 for d=1,2,3,4 and Kim's Euler characteristic applies otherwise. In the reflection calculation, folding the two steps in the inner layer gives the specified loop deletions and adjacent-column extra edges at the endpoints; the outer step deletes the self-paired end wherever applicable. Process the first two columns with the left cap's constraints and weights to produce a row indexed by (u_prev,v_prevprev,v_prev); process the last two from each incoming state with the right cap's constraints to produce a column. Interactions from the caps to the unaffected columns are bulk edges of range at most two, accounted for by this state, so the intervening factor really is T^(L−4). Independently checking T^9=−T^4 proves the sign flip after five more columns for L≥8. The exact seeds at n=5..24 bridge all smaller steps; d_(n+10)−d_n=6 does not change parity. The independent replay /workspace/evidence/petersen.py (petersen.txt) verifies the transfer identity, cap graphs in their non-overlapping ranges, and all element traces via signed orbit sums and quotient character averages for n=5..45. This supports the finite computations, not a substitute for the cap and matrix proof. Over Q the barycentrically subdivided orbit cochains are the invariant cochains, so the character average applies to the ordinary quotient. In rank one the rotations are trivial for odd n and nontrivial for even n; in rank four the signed five-point rotation spectrum has no eigenvalue 1. This gives exactly the listed four residue classes. The cited cycle result states n≥12; for n=5..11 the comparison was verified separately over Q by exact simplicial boundary and character computation (small_cycle_replay.py and small_cycle_replay.log under /workspace/branches/3c13a1ca-e19e-46da-8565-31430b5e94fd). Thus the mathematical equality holds in the smaller cases too, but those cases should not be attributed to the cited n≥12 cycle theorem. Character equality gives rational module isomorphism, not an equivariant homotopy equivalence.

## originality

PASS

The distinct claim is the complete all-n classification for the canonical GP(n,2) action, including the reflection signs in rank one and hence the quotient law, and its comparison with the cyclic complex. Do not credit the character values or rational acyclicity for the entire 5|n subfamily as a separate contribution: a distinct same-day record explicitly covers them, and within-day priority is not established. Likewise do not credit the known special cases, the nonequivariant homotopy classification, the signed orbit-face method in isolation, or the prior character formula for the other cycle complex. The material overlap does not imply the rank-one signs for this action or the full all-n theorem.

## value

PASS

The reflection signs on the rank-one cases distinguish natural actions that have the same ordinary homology. The full classification determines exactly which geometric dihedral quotients have positive-degree rational cohomology and gives a useful uniform comparison between two different natural complexes. The value is not just extending a finite table or restating the already overlapping rank-four result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
