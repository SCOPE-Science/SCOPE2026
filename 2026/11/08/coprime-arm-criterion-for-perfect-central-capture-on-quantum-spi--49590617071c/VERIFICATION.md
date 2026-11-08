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

# Reproduction of the coprime-arm survivor law

With Python 3, NumPy, SciPy, and SymPy installed, execute from the directory containing the two embedded scripts:

```bash
python verify_arithmetic.py
python verify_projector.py
```

`verify_arithmetic.py` builds the exact integer adjacency matrix and computes the rank of the walk matrix generated from the central vertex. Across 145 three- or four-arm spiders, it compares the exact dark dimension to \(\sum_{b\ge2}\varphi(b)(m_b-1)_+\) and checks the if-and-only-if pairwise-coprime boundary. This check uses no eigenvalue approximations.

`verify_projector.py` uses numerical eigendecomposition of the **full** adjacency matrix, separates exact spectral coincidences to tolerance \(10^{-7}\), and constructs the zero-center eigenspace projection directly, without relying on the arithmetic formula. It then compares the entire direct projector with an explicit arithmetic-mode projector and checks every diagonal entry against the site-resolved formula for the same 145 graphs, at tolerance \(2\times10^{-9}\); the observed maximum discrepancy was below \(10^{-14}\). It also computes twelve non-Hermitian finite-time evolution operators with positive loss rates and checks their norms against the exact infinite-time projections to tolerance \(3\times10^{-5}\) for the specified examples.

All tested dimensions, graph-building conventions, and parameter values are contained in the source. These finite checks do not prove the universal quantifiers; the analytic proof in `RESULT.md` supplies them. The finite-time checks do not establish uniform convergence rates. Independent audit is not yet performed.
