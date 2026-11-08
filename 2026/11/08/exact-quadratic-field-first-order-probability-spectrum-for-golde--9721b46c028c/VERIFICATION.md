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

# Reproduction and scope

`python3 checker.py` checks the Fibonacci counts of all admissible words for lengths \(1\) through \(16\), the exact field-mixing identities on several quadratic-field targets, and equality of finite first-hit outcomes for two and six nonoverlapping marker patterns. It uses only the Python standard library and succeeds with `FIBONACCI_SPECTRUM_FINITE_CHECKS_OK`.

The infinite assertions rely on the written argument: the one-sided Markov limit, the nonoverlap argument for pattern fairness, the rational prefix mixture, and the Perron/aperiodic-monoid proof. A finite enumeration cannot verify arbitrary quantifier ranks or every \(\alpha\in\mathbb Q(\sqrt5)\). Historical priority and independent validation remain unresolved.
