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

# Verification

Run `python verify.py` with Python 3 and its standard library. The code uses integer weights for all finite checks. It exhausts weighted labeled-edge multigraphs up to the stated sizes, checks every orientation and every Lorenz partial sum after repair, and separately compares unconstrained versus EFX-optimal peak and square loads. It also checks a seeded random family and the asymmetric two-item boundary and an instance with no global Lorenz maximum.

Expected terminating summary: `PASS 9401 weighted multigraph instances 159039 orientations`. These checks have been executed using the supplied code; their exhaustiveness is only within the declared finite bounds. The universal real-weight theorem is justified by the proof in `RESULT.md`, not the test output.

The audit is a self-review only. Independent audit has not been performed.
