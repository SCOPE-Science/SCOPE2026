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
The exact finite-state checks are implemented by `verify.py`, with no input files needed. Run `python verify.py` after installing NumPy and SciPy. The checker compares 15 independent labeled-versus-lumped rational expectation values, 14 exact moment identities, 48 numerical transient-survival identities and three Rayleigh convergence diagnostics. A successful replay prints the counts. The infinite-family weak-convergence claim is proved analytically from the generator, uniqueness of the limiting jump process, absorption-time tightness and the conditional independent-exponential completion representation. Exact arithmetic in finite instances is not an exhaustive verification of the asymptotic theorem. No independent mathematical audit has been performed.
