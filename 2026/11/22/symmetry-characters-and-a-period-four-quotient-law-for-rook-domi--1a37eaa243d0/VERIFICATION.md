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

The standalone Python 3 standard-library checker `verify_rook_equivariant.py` enumerates the actual faces of the rook dominance complex on the \(3\times3\), \(3\times4\), and \(4\times4\) boards. For each tested group element, it independently evaluates a signed simplicial Lefschetz sum on every invariant face and a second cycle-orbit Lefschetz sum, then matches both against the theoretical trace derived from the three integral character lines. The tests include row/column transpositions and cycles, board transposition for square boards, and products of these maps. The captured output reports 18, 9 and 18 passing actions, respectively, and the complete group-averaged reduced Euler characteristic on all 72, 144 and 1152 automorphisms for these boards, respectively. The marker `ROOK_EQUIVARIANT_CERTIFICATE_PASS` indicates the checks completed.

This finite enumeration is evidence for sign conventions and boundary examples only; it does not certify the all-parameter proof or exclude an equivalent pre-existing equivariant result. The infinite theorem follows from the written natural nerve map, integral Künneth theorem, orientation-twisted combinatorial Alexander duality and rational transfer. No independent audit was performed.
