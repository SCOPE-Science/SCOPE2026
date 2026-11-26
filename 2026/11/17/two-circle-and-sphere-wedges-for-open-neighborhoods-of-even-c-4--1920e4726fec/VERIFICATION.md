---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the even \(C_4\square C_n\) open-neighborhood theorem

The proof in `RESULT.md` checks the unique maximal coface of each removed flank edge, the two elementary collapse pairs in each tetrahedron, and the resulting union of two-column tetrahedral boundaries. The barycentric formula for the strong deformation retraction agrees on all overlapping tetrahedra, fixes the retained union and commutes with all coordinate rotations and reflections. For the ordinary orbit space the proof identifies its points exactly with the quotient of one tetrahedral boundary by the permutations preserving its two column pairs, and gives explicit coordinates on that quotient as a closed disk. These exact arguments prove the all-parameter result.

The original standalone Python 3 script `verify_even_tori.py` and its expected stdout in `EXPECTED.txt` are unchanged. They check a different discrete Morse reduction with integer winding for \(n=6,8,\ldots,20\), and also the mod-two homology for \(n=6,8,10,12\). They corroborate the homotopy consequence in finitely many cases; they do not test the new embedded collapse target or equivariance.
