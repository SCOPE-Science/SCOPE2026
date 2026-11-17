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

# Verification of the high-energy residence theorem

The analytic proof uses only polynomial expansion, analytic simple-turning-root continuation, a positive quadratic factor and bounded regularized quadratures. The error estimates hold for each fixed coefficient quadruple, with \(h>0\).

**Critical symbolic identities:** \(s=-k_2/(3h)\) eliminates the cubic term in the potential, leaving \(K_2=k_1-k_2^2/(3h)\) and \(K_1=F-k_1k_2/(3h)+2k_2^3/(27h^2)\). After rescaling, the perturbations are \(O(A^{-2})\) and \(O(A^{-3})\). For zero odd perturbation, the position mean vanishes and the original sign-cut moves by \(-s/A\); this produces the leading signed coefficient. The period-normalized unperturbed density integrates to one because \(I=\int_0^1(1-u^4)^{-1/2}du\).

**Numerical check:** run `python verify.py` in this directory with NumPy and SciPy. The program evaluates the original physical-time quadratures without resolving the square-root turning singularities numerically, tests three parameter sets and checks reconstruction algebra. Expected terminal marker: `QUARTIC_SIGNED_RESIDENCE_INVERSE_CHECK_OK`. Floating-point tolerance and finite-energy samples do not certify an infinite-energy limit.

**Unproved extensions:** noisy finite-energy estimation; uniformity as \(h\downarrow0\); damped or time-dependent forced dynamics; recovery of \(k_1\) or \(F\) from these two limits; publication-priority completeness. No independent mathematical audit has been performed.
