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

Run `python3 verify_boundary.py` from the directory containing that file; Python 3 standard library suffices. The program writes `27_line_frobenius.csv` alongside itself and reports `CUBIC_27_LINE_BOUNDARY_S6_ZETA_OK` if all exact assertions pass. The included CSV is the actual regenerated output. `verification_output.txt` records one execution of the bundled checker.

The program constructs exceptional classes with the integral intersection pairing of the blowup of six points. It checks 27 vertices, 135 unordered meeting pairs, each vertex degree ten, graph connectedness, and identical adjacency obtained from a separate direct incidence description. It enumerates all 720 permutations and the eleven cycle-type classes, including positive/negative edge orbits, nodes and 270 preimage branches; compares the exact data to an explicit reference table; checks the zeta logarithmic coefficients for extension degrees one through twelve and integer bases five and seven; and checks integrality of the torus count formula at those bases.

The proofs of the geometric normalization and torus-cycle exact sequence are in `RESULT.md`. Numeric checks do not establish existence of prescribed configurations over every finite field, and no such existence is claimed. The full cubic-surface Weyl group and Eckardt degenerations are not covered. This document reports neither independent certification nor a publisher's priority determination.
