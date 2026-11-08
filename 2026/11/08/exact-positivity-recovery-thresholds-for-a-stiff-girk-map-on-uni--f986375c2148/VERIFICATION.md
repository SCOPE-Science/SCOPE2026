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

# Reproduction and mathematical limits

Execute `python3 verify.py` from this directory with SymPy version 1.10 or newer. The code checks the exact two-stage tableau rational identity, derivatives at negative real arguments, absorbing-column factorizations, every entry of the small-dimensional rational matrix function, row-stochasticity, algebraic boundary equalities and \([F(Q_5/2)]_{1,5}=-7/625\). The resulting success string is `EXACT_VERIFY_OK`.

The proof is independent of experimental sampling: Taylor expansion on the transient nilpotent shift gives all matrix entries, and signs of explicit rational polynomial factors cover every \(h\ge0\) in dimensions two through five. Checks are supplementary exact arithmetic, not an assertion about all possible Markov generators or numerical finite-precision behavior. The original papers establish the coefficients; the result neither verifies the full astrophysical scheme nor extrapolates the finite chain calculation to larger dimensions. Independent audit: not performed.
