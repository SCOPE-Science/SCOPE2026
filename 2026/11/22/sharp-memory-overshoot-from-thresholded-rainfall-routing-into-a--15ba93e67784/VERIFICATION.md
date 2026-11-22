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

# Reproduction and claim-to-evidence

## Model
Run `python3 verify.py` (Python standard library only). It checks the raw input-moment expressions, exact derivative numerator, numerical bisection for both threshold equations and strict sign relationships at several parameter values. The script asserts 1,724 independently evaluated supplementary conditions and reports their count.

## Analytic checks
The universal result follows from direct integration under Exp(1), a stationary linear filter, the exact relation \(\rho_a(h)-a=z((1-a)h-(1+a)+z)/D_a(h)\), and the derivative sign \(2(1-z)-(1-a)h\) with \(z=e^{-h}\). Convexity and concavity prove existence, uniqueness and strict inequalities, not a finite grid. All positive-lag autocorrelations are \(a^{k-1}\rho_a(h)\).

## Scope and limits
The proof covers every \(0<a<1\), every finite \(h>0\) and every positive integer lag. The exact runoff process is mass-conserving but idealized. The supplement's floating-point tests are not exhaustive and do not prove the infinite theorem by themselves. The evidence does not establish real-world performance, stability of sample autocorrelations or historical priority outside inspected literature. Independent validation has not been performed.
