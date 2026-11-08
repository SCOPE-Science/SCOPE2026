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

# Analytic and reproducibility checks

The affine branch widths and positive gaps follow directly from \(p_n=n^{-q}/\zeta(q)\) and \(I_n=[P_n-\lambda p_n,P_n]\), with \(0<\lambda<1\). The pressure root exists uniquely since its decreasing sum starts at \(N>1\) when the dimension is zero and ends below one at dimension one. The equality \(F_N(1/q)=aH_N\) is exact.

For the threshold, \(H_N=\log N+\gamma+O(N^{-1})\) and the first crossing differs from equality by at most one harmonic increment. The Laurent expansion \(\zeta(1+\varepsilon)=\varepsilon^{-1}+\gamma+O(\varepsilon)\) then gives the stated prefactor. In the centered dimension window, the logarithmic-pressure derivative equals \(\log a-\sum(\log n)/n\,/H_N\) and has leading term \(-1/(2a)\). The second derivative is bounded by the variance of \(\log n\) at maximum magnitude \(O(a^{-2})\). The moderate-deviation window has centered coordinate \(O(\log(1/a))\), so its Taylor error remains negligible.

Run `python verify_cutoff.py` in an environment with `mpmath` 1.3 or newer. The saved checker was run at 95-digit precision and emitted:

```
VERIFY_OK finite_pressure_roots=18 threshold_signs=12 high_precision=95
Analytic asymptotic and historical priority are not certified by these tests.
```

These tests cover two retained fractions, three proximity parameters each, and signed critical-window shifts. They test representative finite pressure roots and are not a substitute for the proof or an independent scientific audit.
