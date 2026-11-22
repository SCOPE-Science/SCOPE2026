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

The standalone `verify_symbolic.py` first checks the exact eight-orbit determinant and proves the two rational covariance identities and same-shore relation by symbolic cancellation over \(\mathbb Q(n,g)\); it prints `BIPARTITE_KMP_SYMBOLIC_CERTIFICATE_PASSED`.

The standalone `verify.py` file uses exact rational linear algebra on a vertex-pair basis, not the eight-orbit system used in the proof. Execute with Python 3 and SymPy:

```
python verify.py
```

Observed output from the packaged source: `BIPARTITE_KMP_EXACT_MOMENTS_PASSED cases= 12`. The cases are all pairs of \(n\in\{2,3,4\}\) and \(g\in\{1/2,2,5,12\}\), at bath means \(T=2\), \(T+\Delta=5\). They test the \(BB\) and \(PQ\) formulas; for \(n\ge3\) they also test the \(PP\) identity. The executable checks the limiting polynomial factorization. These are finite tests, not an exhaustive proof over \(n\), \(g\), or temperatures.

The analytic proof applies to all \(n\ge3\), all \(g,T,\Delta>0\). Its critical checks are the generator's exact degree-two closure, the explicit eight-equation coefficient determinant, positive coefficients of \(S_n\), one sign change in \(R_n\), and the limiting factored quartic. There is no computational or scientific claim about higher moments, finite-time kinetics, unequal shore sizes, or definitive historical priority.
