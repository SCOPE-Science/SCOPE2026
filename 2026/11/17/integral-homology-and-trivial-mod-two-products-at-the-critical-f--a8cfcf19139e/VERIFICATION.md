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

# Exact reproducibility

Run `python3 verify.py cycle_certificate.json` in a directory containing the accompanying `verify.py` and `cycle_certificate.json`. Python 3 with the standard library is sufficient. The deterministic verification reports `VERIFY_OK` and should match `verification_output.txt` exactly.

The integer steps start from the full face set, test all 65,536 sixteen-vertex masks, and perform 999 checked elementary simplicial collapse pairs. In the residual signed integer chain complex, all four boundary matrices reduce through unit pivots only. The ranks, invariant-factor condition, and resulting homology are checked. This is a complete finite computation for the exact specified graph.

The mod-two computation is independent of the collapse: it constructs all original boundary matrices, verifies that consecutive boundaries compose to zero, computes all Betti ranks, finds a nonbounding 102-simplex-supported degree-four cycle and seven independent degree-two cohomology classes, and evaluates every entry of the Alexander–Whitney cup pairing. The 7-by-7 output is zero. The supplied JSON contains explicit basis incidence vectors, with each vector encoded in hexadecimal and indexed by sorted integer simplex masks.

No general-parameter statement, integral cup-product coefficient, homotopy wedge decomposition, external certification, or independent mathematical validation is claimed.
