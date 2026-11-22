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

# Verification steps and limits

Execute `python3 checker.py`. It uses only `fractions.Fraction` from the Python standard library and checks all 25 ambiguity-squared polynomials by exact cyclic exponent convolution, exact cubic root bracketing with \(\sqrt5\) contained between two rationals, strict positivity at 19 non-active frequency shifts, and the global minimax derivative inequalities. It is independent of numerical optimization software, external code, and statistical sampling. Root decimal approximations are supplementary.

The strict global maximum is proved for every real \(t\ge0\), not just tested parameters. The Fourier-phase-retrieval consequence uses the published nonzero-ambiguity criterion. No full-spark claim or certification is made for the unregularized window. Independent validation has not been performed.
