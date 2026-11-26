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

The pole edge forbids a face containing both poles. Deleting them yields a join X of Ind(P_{ell_i-1}); the two pole cones have bases Y_u,Y_v which are joins of Ind(P_{ell_i-2}), with the actual inclusions into X. The path formula follows by folding vertex 3 onto vertex 1 (its open neighborhood contains that of vertex 1), leaving P_2 disjoint from P_{n-3}, and treating P_0,P_1,P_2 explicitly. Thus X is contractible exactly when some length has residue 2, and the bases are contractible exactly when some length has residue 0; each noncontractible join has formal sphere dimension R-1. For all lengths 1 mod 3, the path endpoint inclusion is obtained by attaching a cone on the contractible Ind(P_{3a-2}); gluing along this subcomplex gives a homotopy equivalence, and joins preserve it. The first pole cone then leaves a contractible space and the second gives S^R. With a residue-0 arm both bases are contractible so the cones preserve X. In the remaining case, X is contractible, hence both maps through it are null, and the two cones yield the wedge of two S^R. If all arms have length 2 the join-unit convention means the bases have empty realization; the interior simplex and two isolated poles give exactly three components. This is an all-parameter homotopy proof, not a Betti-number extrapolation.

## originality

PASS

No inspected source covers ordinary independence homotopy for a direct pole edge with arbitrarily many additional arms of arbitrary mixed residues. The nearest same-day recorded calculation omits the pole edge and restricts arm lengths to 3 and 4; its sphere agrees in the overlapping length regime, but its graph and result are not equivalent. This is a bounded assessment, not a priority claim.

## value

PASS

This classifies a natural generalization of the theta graph at the level of homotopy, not merely homology. Both the collapse to a point when residues 0 and 2 mix and the sharp two-summand limit, independent of how many arms occur, are useful distinctions. The exact pole-attachment test explains why adding arbitrarily many routes does not create higher wedge multiplicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
