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

# Verification details

The standalone command `python3 verify_nearperfect_hom.py` enumerated all ordered near-perfect pairings and all triangle support patterns for \(r=2,3,4\) from the defining disjointness rule. It asserted the predicted factorial node counts, uniqueness of every edge's containing triangle, connectivity of the bipartite incidence graph, the integral graph-homology ranks, the correct source-color quotient orbit counts, and preservation by adjacent-transposition generators of ground-point and source-color symmetry for \(r=2,3\). It also checked that source-color transpositions have no fixed maximal triangles.

Observed values, all exact:

| \(r\) | Ground points | Zero cells | Triangles | Spokes | \(\beta_1(X_r)\) | \(\beta_1(X_r/S_r)\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 5 | 30 | 20 | 60 | 11 | 6 |
| 3 | 7 | 630 | 630 | 1890 | 631 | 106 |
| 4 | 9 | 22680 | 30240 | 90720 | 37801 | 1576 |

The program completed with `NEAR_PERFECT_KNESER_HOM_EXACT_PASS`. Its recorded stdout appears in `verification_nearperfect_hom.txt`.

**Logical boundary:** The all-parameter proof is the support-size classification, equivariant triangle collapse and permutation-lattice exact sequence in RESULT.md. The enumerations are finite controls. No claim is made for \(r=1\), for ground cardinalities other than \(2r+1\), or for higher pair sizes. Publication priority remains uncertain pending an independent literature audit.
