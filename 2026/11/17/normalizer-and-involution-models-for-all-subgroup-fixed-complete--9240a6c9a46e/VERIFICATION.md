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
# Reproduction and limits

Use a standard Python 3 interpreter and run `python verify_orbit_matching.py`. The program has no nonstandard dependencies, reconstructs full permutation subgroups, enumerates all original graph-edge orbits, checks each orbit's matching property, independently constructs equivariant-bijection and equivariant-involution candidates, compares their actual edge sets, then enumerates all compatible collections and checks the predicted polynomial coefficient by coefficient.

The final successful output is `ALL_ORBIT_TYPE_MATCHING_CHECKS_PASS cases=15 enumerated_faces=377`. Covered cases include transitive actions, regular groups \(C_3,C_4,C_2\times C_2,S_3\), disjoint nonisomorphic orbit types, and fixed points. The complete output is included in `verification_output.txt`.

The claimed infinite all-finite-group PL theorem is proved mathematically by orbit projection, equivariant maps and barycentric coordinates; this finite suite is corroboration, not an exhaustive test of all finite groups. The first-Betti formula for two regular orbits is the Euler-rank formula for the graph \(K_{s,s}\), not a numerical extrapolation. The theorem does not classify all homotopy types of \(B_{m,w,s}\) for \(m\ge3\), and publication priority has not been independently adjudicated.
