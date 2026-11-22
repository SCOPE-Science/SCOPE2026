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

With dependencies in `requirements.txt`, execute `python artifacts/verify_five_cycle.py`. The original successful console output is stored at `artifacts/checks.txt`; it reports exact algebraic stencil, eigenvalue and projector assertions, high-precision independent matrix-exponential checks over 220 sample times (7,260 comparisons), and high-precision roots. The direct matrix exponential was computed independently of the algebraic spectral expression.

The exact sign law is not certified by the numerical samples: the proof in `RESULT.md` establishes that the only possibly negative entry has one and only one positive zero, using strict exponential-rate ordering and boundary signs. Numerical time-grid testing cannot by itself prove a global statement over all positive real times. The proof concerns exact five-by-five semidiscrete evolution, with no time integration truncation error and no claim for other mesh sizes.
