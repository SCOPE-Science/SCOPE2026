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

# Finite evidence and proof obligations

The all-length proof is in `RESULT.md`, not in the output logs. Core invariant: \(m_i=1-(x_i\oplus x_{i+1})\), \(y_i=1-m_{i-1}m_i\), and \(\sum m_i\equiv n\pmod2\). Verify the forced-run argument, the cyclic independence polynomial trace, and the golden-ratio extremal bound directly.

- `python3 verify_formula.py`: compares the formula against every labeled source and target for \(1\le n\le15\) (including the two smallest cyclic-degenerate cases). Expected last line: `FORMULA_VERIFY_OK`.
- `python3 verify_transfer.py`: builds a separate four-state de Bruijn transition system, compares its exact trace to independent parity-constrained dynamic programming for all targets through \(n=12\), and reproduces 250 deterministic samples at each of \(n=15,21,32,47,64\). Expected last line: `TRANSFER_VERIFY_OK`.

The finite checks cannot establish the statement for all lengths; that is supplied by the exact symbolic combinatorial proof. Historical priority and any outside audit remain unperformed. In particular the known 1989 infinite-lattice/free-boundary Rule-126 formulas and generic cyclic transfer counts are explicitly acknowledged.
