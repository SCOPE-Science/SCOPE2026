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

Run `python check_heisenberg.py` in a directory containing the supplied file, with Python 3, NumPy and SymPy available. The checker constructs each of six regular convolution matrices from the Heisenberg group law without loading expected matrices; constructs the corresponding nontrivial irreducible blocks separately; compares their spectral multisets and exact quadratic Gauss triple products; enumerates all 108 three-direction subgroup triples in characteristic three; and checks two characteristic-three regular ranks using exact integer linear algebra.

Expected terminal markers: `HEISENBERG_THREE_LINE_SPECTRUM_PASS` and `HEISENBERG_THREE_LINE_CENSUS_PASS`.

Numerical eigenvalue checks are finite and use floating-point arithmetic, whereas the two representative rational matrix ranks use exact arithmetic. Neither constitutes a universal-prime mathematical proof. The algebraic argument and its boundary cases appear in `RESULT.md`. Independent mathematical validation has not been performed.
