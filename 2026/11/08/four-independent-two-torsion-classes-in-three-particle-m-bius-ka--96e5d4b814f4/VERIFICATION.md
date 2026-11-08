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
# Reproducible integral verification

The files `verify.py`, `certificate.json`, and `verification_output.txt` accompany this document. Run `python verify.py certificate.json`. No libraries beyond Python 3's standard library are needed. The program enumerates the complete weight-three integral reduced Świątkowski complex of \(\operatorname{GP}(8,3)\), reconstructs the boundary maps, verifies all \(D_2D_3=0\) identities, and calculates the modular ranks 4475, 4479, 4479 over prime fields of orders two, three and five. It checks the 1919-term primitive integer kernel vector, and the four independent binary kernel witnesses; their half-boundaries are integral cycles, with 2002, 1822, 1718 and 1652 nonzero terms respectively. The integer identities, modular-rank calculation and kernel-mod-two independence prove \(H_3\cong\mathbb Z\) and \(H_2[2]\cong(\mathbb Z/2)^4\).

The verifier was executed on the accompanying certificate, and its output matched the attached record exactly, ending with `MOBIUS_KANTOR_THREE_PARTICLE_TORSION_PASS`. This is exhaustive for the stated chain groups and exact integer assertions, not a heuristic enumeration of graphs. A published graph-configuration chain-model theorem supplies the topological interpretation. The checks neither classify all of second homology nor exclude higher-order torsion.
