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

# Verification of the finite Hom-complex census

Run `python3 verify.py` and compare exact stdout to `expected.txt`. The checker is standalone, requires Python 3.10 or later, and enumerates all walks, all one-coordinate transitions, and every Hom polyhedral cell as a tuple of finite sets. It checks all assertions and prints `ALL CHECKS PASSED` only after the complete census.

The geometric circle classification of a 48-vertex component follows from its 24 triangular faces having disjoint boundary-edge sets; each can be removed along a free edge, leaving a connected graph of cycle rank one. The one large component has Euler characteristic \(-10\); the theorem of Fujii–Kimura–Nozaki (2024), with its verified hypotheses, establishes that this component has the homotopy type of the connected Petersen bipartite double cover. Its exact integral first Betti number is therefore eleven. The computation does not itself certify the published theorem or independent audit.

The included finite computation proves the exact stated cases, not any larger-source or arbitrary-target family. It does not determine a full equivariant representation or construct a direct collapse of the large component.
