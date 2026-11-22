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

Run `python3 verify_rational.py` and `python3 verify_words.py` in a standard Python 3 environment; no third-party packages or downloaded datasets are required.

`verify_rational.py` enumerates exactly 75 surjective rank labelings (the weak orders on four gaps), records their two boundary tests, constructs all generating-function numerator contributions with integer polynomial arithmetic, and checks the four claimed numerator polynomials and unrestricted partition identity. The calculation is an exact finite algebraic identity covering every weak-order cell; no symbolic software or floating point is required.

`verify_words.py` enumerates all \(\binom n4\) words at each \(4\le n\le20\), checks every proper prefix/suffix of every cyclic rotation, and verifies the gap formula and rational-series coefficients. It separately probes all \(7^4=2401\) tuples in a finite large-gap grid. The finite sample is not a proof of the all-length theorem, which rests on the universal border-case lemma and exact 75-cell decomposition in the result.

The individual programs were run successfully with Python 3. Their output includes the complete first-seventeen-length census and the exact numerator identities. No external or independent validation was performed.
