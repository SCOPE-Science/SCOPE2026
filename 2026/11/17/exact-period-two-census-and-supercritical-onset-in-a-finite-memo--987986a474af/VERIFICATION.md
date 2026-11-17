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

# Verification of the period-two theorem

From the included file `check_period2.py`, execute `python3 check_period2.py` with a Python 3 installation containing NumPy. Actual execution returned:

`VERIFY_OK exact_fraction_cases=48 exact_period2_instances=144 spectral_cases=36 local_multiplier_cases=108`

The checker uses exact rational arithmetic for 48 order/memory pairs, confirms the characteristic factorization and the alternating-tail sum identity, and verifies phase identities and strict positivity for 144 rational parameter cases. It additionally compares the analytic leading two-step multiplier with the computed monodromy and checks strict spectral separation at 36 sampled order/memory pairs. The finite sample is not a proof for arbitrary fractional order, unbounded memory length or every parameter; the analytical identities and inequalities in `RESULT.md` give those statements.

The published first-flip boundary is acknowledged as prior. The new proof establishes the global primitive-two-cycle census and the previously unverified uniform genericity conditions. The normal-form coefficient uses the critical eigenvector normalized to first component one. There is no claim of independent examination or external certification.
