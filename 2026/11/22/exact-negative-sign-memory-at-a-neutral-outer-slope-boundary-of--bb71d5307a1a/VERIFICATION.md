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

# Verification and reproducibility

## Analytic checks
The stationary weights on cells \(R_k,L_k\) each equal \((m-k)/(m(m+1))\). Every noncentral cell moves inward by one; each central cell maps to each opposite cell with probability \(1/m\). These facts verify the transfer equations exactly for every integer \(m\ge2\). Any block of \(m\) iterates has an inner expansion factor \(m\), and the finite directed graph has coprime return lengths two and three. The renewal recursion has the explicit solution \(q_m(n)=2(1-1/m)^n-1\), and the residual-time formula yields the closed stationary correlation.

The finite difference is \([4-8(1-1/m)^n]/(m+1)\). The only integer equality of zero for \(m\ge2,n\ge1\) occurs at \(m=2,n=1\). Uniform rescaled convergence follows by the standard elementary limit \((1-1/m)^{\lfloor tm\rfloor}\to e^{-t}\).

## Executable checks
Run `python3 verify_stationary_sign.py`. This script uses exact `fractions.Fraction` values, reconstructs the full finite Markov matrix independently of the closed form and checks stationarity and 493 exact correlations across integer \(m=2,\ldots,30\). It also checks the finite minimizing lag and piecewise maps on rational midpoints. It produces no network traffic or third-party dependencies.

## Boundaries
Finite checks do not prove statements for all integers. The correlation formula is claimed only for \(0\le n\le m\). The absolutely continuous invariant probability can coexist with singular invariant measures. The originality comparison cannot exclude inaccessible or unindexed equivalent published results. Independent audit and independent validation have not been performed.
