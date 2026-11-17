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

# Reproduction
Run `python3 verify.py` (Python 3 standard library only). It exhaustively checks the ten-edge Boolean lattice for graph non-2-connectivity, all ten pentagonal dihedral permutations, the actual barycentric orbit quotient's cell counts and all mod-two boundary ranks. It also verifies \(\partial^2=0\), the mod-two Betti numbers, and the original signed Lefschetz traces. The calculation certifies the exact two-rank in degree four via the universal coefficient theorem and rational acyclicity; it is not an integral Smith-normal-form calculation and does not establish torsion exponents. The original nonequivariant sphere-wedge premise is explicitly attributed to the cited theorem.
