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

# Reproducibility

Run `python verify_jacobi_transition.py` in a Python 3 environment with SymPy and NumPy. Successful execution prints:

`JACOBI_FIRST_REENTRANCE_PASS exact_cayley=4 exact_routh=4 exact_witnesses=3 sampled_cases=316`

The verifier reconstructs four exact kernel numerator/Cayley identities from the rising-factorial moments, performs symbolic Routh elimination for boundary orders zero through three, and confirms three exact fourth-order witness polynomials and their sign arrays. It separately evaluates 316 rational-parameter root-count cases numerically. The numerical cases do not establish any infinite-parameter assertion. The general proof instead uses algebraic identities plus the Routh–Hurwitz root-count theorem, strict positivity of all nonfinal first-column entries, and positivity of the kernel on the nonnegative real scalar axis.

The required input is only the included checker and standard installed Python libraries. The verification makes no claim of independent external mathematical audit, exhaustive literature priority certification, or classification beyond the stated boundary orders.
