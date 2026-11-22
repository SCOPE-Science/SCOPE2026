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

The analytically established assertions are the exact chord formula and normalized integral, the diameter classification, three fixed-height asymptotic probabilities, and the fixed-parameter crossover. The proof checks the correct invariant sampling convention and normalizes against the actual circular-segment perimeter.

Run `python CHECK.py` with NumPy installed to perform the deterministic numerical experiment. The script compares numerical line-measure quadrature with the proposed limits in five fixed geometries and six crossover parameter choices and performs three algebraic/symmetry checks. These fourteen diagnostics are **not** exhaustive symbolic or interval certificates; the proof, not the sampled quadrature, carries the asymptotic claims. The integral is valid without the checker. No external independent audit has been performed.
