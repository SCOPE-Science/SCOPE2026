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

# Verification and limits

Run `python verify.py` from the directory containing the script. It depends on no third-party packages. An execution from the actual package files produced `PASS: 171 supplementary finite checks; no infinite proof is inferred from them.` The tests cover exact closed-form spectral factors for two special Matérn smoothness values in one dimension, the spectral envelope in dimensions one through three, periodic Parseval examples in dimensions one and two, and the exact diagonal/off-diagonal expected Frobenius identity for finite iid distributions.

The general theorem is a mathematical proof in `RESULT.md`; tests do not exhaust all dimensions, density choices, Fourier modes or sample sizes. In particular numerical tests do not prove Poisson summation, the lattice inequality or the concentration theorem. The alias bound may be computed or bounded separately. The concentration result is conditional on fixed discretization parameters, and no independent validation has been undertaken.
