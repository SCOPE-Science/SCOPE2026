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

# Reproducibility and boundaries

Run `python verify.py` with SymPy available. The checker works directly in exact symbolic Fourier arithmetic, verifies the normalized first- and second-order equations from the full self-consistent transfer identity on a nonconstant two-block graphon, and checks the explicit block degree and neighbor-degree factors. It should output `VERIFY_OK`.

The universal result is proved by the analytic norm contraction of the uncoupled Perron operator and the holomorphic Banach-space implicit-function theorem, not by this finite example. No finite experiment certifies existence or convergence for every graphon. The theorem covers sufficiently small complex coupling, and its physical positive density exists for sufficiently small real coupling. Only local uniqueness of the analytic density is claimed. An independent mathematical audit has not been performed.
