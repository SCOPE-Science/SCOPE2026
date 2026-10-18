---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The full tetrahedron has fifteen nonempty faces and 28 Hasse cover pairs. An independent endpoint-disjoint matching enumerator generated exactly 14,720 nonempty Hasse matchings, tested directed Hasse-graph acyclicity on each, retaining exactly 12,820 finite simplices with full f=(28,300,1544,3932,4632,2128,256). Recomputing signed chain traces for all 24 S4 vertex permutations produced class Lefschetz (100,2,0,1,0), hence top homology character (99,1,-1,0,-1) after subtracting H0=trivial. The actual verification.py independently crosschecks orbit-block fixed simplex traces and Specht inner products (4,13,8,12,4). Concentration in degree 4 with rank99 follows from Scoville arXiv:2604.18172, Theorem 20/Table 2; the present finite trace recheck alone would not independently prove that homology concentration. Theorem plus complete finite computation suffices for the rational character claim.

## originality

FAIL

A published same-mathematical-object SCOPE record has precisely the same complete S4 class-character vector and identical five Specht multiplicities. This is decisive direct coverage, not a weaker action-exists theorem nor a mere overlap in 99-dimensional Betti number. No surviving distinct claim was supplied.

## value

FAIL

Computing a complete group character would be meaningful if unknown; however the same table and irreducible decomposition for the same tetrahedral Morse complex have already been published. The submission adds no unreported group-action invariant, boundary phenomenon or structural theorem, so independent enumeration/reproducibility is not a new mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
