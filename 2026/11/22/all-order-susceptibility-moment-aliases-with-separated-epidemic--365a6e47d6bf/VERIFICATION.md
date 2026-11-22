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

# Verification and reproducibility

Run `python3 checker.py` with Python 3. The file is standalone and uses only the standard library. It verifies high-precision conservative bounds for the 18-interval sine/Gaussian integral and the Mills upper tail. These establish \(-H(1/2)>0.1115\) and an absolute final attack-fraction gap exceeding \(0.16056\). It also prints separate approximate final-pressure roots using Simpson quadrature; those approximate values are not proof certificates.

The written analytical proof establishes the equality of every susceptibility moment, all one-sided time derivatives, strict terminal-pressure uniqueness, discreteness of exceptional seeds, and nonanalyticity. Finite checks of the moment identity are consistency tests only; they cannot certify infinitely many moments. The model is an infinite-population deterministic fluid law. No finite-population stochastic, structural parameter inference, clinical forecast, or stability beyond the scalar pressure flow is certified.

The 2026 originating manuscript was accessible only through its bibliographic abstract, not its full text. The complete 2012 heterogeneous-final-size paper was examined in accessible HTML. This scientific access limitation is relevant to historical priority, not to the independently derived equations and proof given here.
