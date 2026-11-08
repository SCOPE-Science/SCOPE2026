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

# Reproduction and evidentiary limits

Use Python 3 with its standard library. Place `verify.py` and `collapse_certificate.json` in the same directory and run `python verify.py` there. The exact packaged execution output appears in `verification_output.txt`; successful replay ends with `VERIFY_OK`.

The verifier independently builds the Euclidean coordinates from the regular hexagonal antiprism formula, checks all 66 distance pairs numerically against the symbolic five-shell classification (absolute tolerance \(10^{-12}\)), enumerates every nonempty subset of twelve vertices and checks the clique condition exactly from the integer/radical shell codes. It replays each of 126 stored elementary free-face pairs, checking that each deleted face has a unique immediate coface in the remaining complex at that moment. It verifies all surviving face vectors, the closed angular edge cochain at the two circle scales, the integral winding of a horizontal hexagon, the four-triangle filling at the next scale, and that the final noncomplete graph's forbidden-edge subgraph is one twelve-cycle. It also runs independent binary boundary-rank calculations on every stage.

The exact symbolic identities and recurrence for independence complexes are proved or cited in `RESULT.md`; numeric Euclidean comparisons are a cross-check, not their proof. Binary homology ranks do not certify integral torsion-freeness; the separate collapse, fundamental-group, and cycle-independence arguments supply the integral homotopy statements. No unbounded family or uncomputed scale is inferred from a finite experiment. Scientific novelty remains subject to external literature and peer scrutiny.
