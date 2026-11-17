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

# Computational verification

Run `python verify_hopf.py` with `requirements.txt` installed. The checker generates all first, second and third derivatives from the publicly displayed system, computes the equilibrium branch and full characteristic polynomial, then proves the root count of the eighth-degree Routh–Hurwitz polynomial by exact Sturm arithmetic. It verifies opposite exact signs at rational bracket endpoints.

The interval arithmetic uses decimal precision 45 and outward-rounded interval operations. It verifies positivity over the full isolating bracket for the first three characteristic coefficients, the Routh–Hurwitz derivative, negative carrying-capacity derivative, and positive equilibrium coordinates. Normal-form contractions use interval Cramer's-rule matrix inversions and the spectral projector onto the eigendirection with first component one. The resulting strict enclosure is
\[
-5.877089159<\ell_1<-5.877089130.
\]
The program reports `EXACT_STURM_OK`, `INTERVAL_LYAP_OK negative`, and `VERIFY_OK`. The interval bounds are certificates conditional on the exactness and outward rounding of the installed interval-arithmetic implementation, not an independent proof audit. None of the checks establish global periodic-orbit uniqueness or the stable cycle's basin size.
