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

# Finite reproducibility record

Run `python3 verify.py` using a standard Python installation, version 3.9 or later. No third-party packages, external services or downloaded data are required. The full run prints the marker `ICOSAHEDRAL_4CUT_INTEGRAL_HOMOTOPY_VERIFIED` and the counts reproduced in `verification_output.txt`.

The code constructs the twelve-vertex icosahedron independently from its six fivefold edge orbits, checks degree five and thirty edges, enumerates all 495 four-element subsets, and builds all faces of the ordinary four-cut complex. A second direct predicate evaluates the face condition on all 4096 vertex subsets. It explicitly identifies the twelve missing six-element faces as complements of closed vertex neighborhoods.

The first staged vertex-element matching has 1738 pairs and leaves only six dimension-six and twenty-one dimension-seven cells in the *reduced* complex. A full directed topological sort verifies all 19536 Hasse incidences. The signed integral chain projection gives a six-by-twenty-one boundary with exactly one primitive unit column. Direct mod-two boundary elimination and a second matching using reversed vertex order are separate consistency checks. The homotopy conclusion uses the integral attaching degrees; it is not inferred from mod-two Betti numbers.

The verification is exhaustive for this twelve-vertex finite complex, not an infinite-family certification. Independent expert validation has not been performed.
