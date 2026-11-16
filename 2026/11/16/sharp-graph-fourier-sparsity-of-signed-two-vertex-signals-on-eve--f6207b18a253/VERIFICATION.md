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

# Verification of the path-graph Fourier sparsity theorem

The proof consists of an exact trigonometric product identity, an integer linear-congruence zero-count lemma, and global upper bounds on zero sets split by path-length parity. It covers all integer path lengths at least two; it does not require a numerical limiting argument. The boundary cases of length two, odd prime order and powers of two are covered by the equality classification.

Two reproducibility checks were executed from the included standalone source files:

- `python check_exact.py`: PASS, using only Python's integer arithmetic. For all path lengths \(2\le n\le80\), all \(170{,}640\) distinct unordered vertex pairs and binary relative signs were enumerated; predicted minimum, all equality sets and cardinalities were checked exactly.
- `python check_dct.py`: PASS, with `mpmath` at 90 decimal digits. For all \(2\le n\le22\), all \(3{,}542\) pairs and binary relative signs, direct Laplacian cosine-transform coefficients agreed with the integer-congruence zero classification at tolerance \(10^{-65}\).

The exact congruence checker verifies finite specializations but is not a substitute for the all-dimension reasoning; the numerical checker is corroboration only. Historical publication priority and robustness for unequal or noisy amplitudes are not mathematically certified here. Independent audit status remains unperformed.
