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

# Reproduction and scope

Run `python3 verify_steiner_frobenius.py` with standard Python 3. The resulting exact integer/permutation enumeration must equal the bundled `verification_output.json`. The script asserts the group size, cardinalities of the 27 lines, 45 tritangents, 120 Steiner supports, and 25 different combined cycle profiles; it fully enumerates the group, rather than sampling elements. It asserts the five exact shortest-cycle counts, the tritangent-without-Steiner count, and the explicit five-cycle decomposition.

The general cubic-surface statements also require: (i) the classical identification of the 120 nine-line supports with unordered Steiner trihedral pairs; (ii) the fact that geometric Frobenius acts on the 27 lines through the Weyl group; and (iii) the published Frobenius equidistribution theorem. These are described and cited in RESULT.md. The conic-based blowup argument proves geometric sharpness for every prime power at least four; the script independently checks its prescribed Weyl action.

The computation is exhaustive for the abstract finite group, but is not a finite-field census of cubic surfaces. No claim of independent mathematical validation is made.
