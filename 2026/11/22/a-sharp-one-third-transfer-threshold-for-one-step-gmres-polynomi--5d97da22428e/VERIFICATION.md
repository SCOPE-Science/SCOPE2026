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

# Verification evidence and limits

The exact analytical argument is given in `RESULT.md`, with an explicit finite-dimensional criterion derived from independent training and deployment Rayleigh quotients, a Toeplitz-symbol bound and long-path limiting extremizers. The full universal result does not depend on random tests.

Run `python verify_transfer.py` using Python 3.10+, SymPy and NumPy. The verifier checks the symmetrized-inverse identity symbolically for sizes 2–8, three-site closed-form eigenvalues, the sharp polynomial boundary, the exact two-site witness, transfer identities with random vectors, extreme-eigendirection witnesses, and a finite long-path amplifier. The executed package returned 961 successful assertions.

The tests cover finite dimensions and parameter samples, not exhaustive cases. The proof covers exact arithmetic, including equality cases. Independent validation has not been performed.
