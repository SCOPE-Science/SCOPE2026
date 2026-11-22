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

# Verification of the minimal-ideal orbit census

The proof in `RESULT.md` uses (1) exact multiplication in the truncated algebra, (2) the induced action on the six-dimensional socle, (3) weighted graph support and explicit normalizations, and (4) an \(S_3\) Burnside count. No experiment is used to infer an infinite-field formula.

`check_orbits.py` independently enumerates the projective socle lines and the actions of generators of the induced automorphism group. The odd-field generators are adjacent coordinate permutations and primitive diagonal scalings. The even-field generators are adjacent coordinate permutations, elementary transvections, and a nonzero diagonal scalar in the extension-field case. These generate the required linear groups. The encoded quadratic action uses coefficients of \((Mx_i)(Mx_j)\).

Run `python check_orbits.py`; it must report orbit counts \(2,13,2,18,25\) for field orders \(2,3,4,5,7\) respectively, with all projective points covered. For an additional check, import `orbit_census` and invoke `orbit_census(11)`, obtaining 41 orbits on 177156 points. Expected counts are independently derived symbolically in `RESULT.md`. These finite tests validate the implementation in the specified cases only.

The literature-priority comparison is necessarily bounded; existence of an undiscovered equivalent result is not ruled out. No independent audit or certification is asserted.
