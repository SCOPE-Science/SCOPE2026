---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stationary solution is conditionally centered Gaussian with variance M+δU, where U is the exponential filter of a symmetric sign Z. Its stationary generator gives E[U^r]=E[ZU^(r−1)] and E[ZU^(r−1)]=[(r−1)γ/((r−1)γ+k)]E[U^(r−2)] for r≥2, independently of the density calculation. Thus E[U²]=γ/(γ+k), E[U⁴]=3γ E[U²]/(3γ+k), and odd moments vanish by symmetry. This verifies the exact moment map. The standardized ratio R strictly increases from 1 to 3 and physical positivity gives exactly M>δ, with δ²=2RB/(3−R). At fixed feasible M,B the interval 0<k/(2γ)<(M²/B−1)/2 preserves all moments through degree seven; the displayed dissipation is strictly increasing across that interval. The independent stationary diffusion-current calculation agrees with published Eq. (45) and fixes its factor-of-two convention. Both explicit ambiguity witnesses and their separation were reproduced by exact rational arithmetic: python3 /workspace/evidence/bounded_checks.py 3. The bundled checker was read, not executed. No finite-sample stability, unknown-γ recovery, or asymmetric-switching theorem is established.

## originality

PASS

Credit the known forward dissipation formula and standard variance-mixture tools. The supported distinct claim is the exact and sharp stationary-position inverse, including the feasible image and unavoidable ambiguity through sixth order with unequal dissipation. The closest indexed inverse uses a different observable and variance kernel. Zhang–Wang is a named access risk, not evidence for or against priority.

## value

PASS

Identifying a hidden switching clock and dissipation from a stationary position snapshot is a natural inference question. The exact cutoff rules out all lower-order summaries even with ideal ensemble data, while the constructive inverse and strict feasibility conditions say when eighth-order data work. This is useful independently of practical high-moment estimation, which is not addressed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
