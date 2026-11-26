---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed RESULT.md lines 25–75. For a positive contraction, the off-diagonal squared row norm is at most q(1-q), where q is its diagonal element, since B^2<=B. Cauchy–Schwarz and scalar maximization give the sharp row sum C_n=(1+sqrt(n))/2; the stated rank-one orthogonal projector attains it. Applying the row and column bounds to the symmetric exponential factors in two-input Duhamel gives the upper bound C_n^2 m_mu on the full closed cone. For the lower bound, A=-(mu+delta)I-M(I-P) has strict slack delta; adding h times the all-ones matrix is admissible for |h|<delta/n and the direction has max-entry norm one. For t>0 and interior integration parameters both exponential factors converge to scaled P as M tends to infinity. The derivative integrands are dominated by C_n^2 t exp(-(mu+delta)t); the t=0 atom contributes zero. The first diagonal entry of PJP is C_n^2. Taking delta down to zero via monotone convergence recovers the sharp two-input supremum. This includes n=1, a constant filter and mu=0 with finite first moment. The three specializations follow from the delta measure and the gamma integral. CHECK.py was inspected, not run; the frozen file records no independent, expert or Lean verification.

## originality

FAIL

The exact coefficient is mechanically implied by the distinct indexed Resultary theorem 2a72590f2caf on bounded positive spectral intervals, not just analogous to it. Affine translation, nonnegative Taylor coefficients and exhaustion of the negative cone give the exact claimed constant, including the endpoint with no analyticity across zero. Both records have the same displayed date. The finding is a correct self-contained proof, but a distinct mathematical result relative to that theorem is not established; this assessment does not assign priority, allege copying or identify the unnamed negative-half-line reference in the comparator.

## value

FAIL

The sharp coefficient is useful; the direct Duhamel proof also gives a clear witness. But as a proposed distinct exact result, the claimed half-line classification and the displayed heat and resolvent constants are all routine consequences of the indexed exact finite-window formula. No further non-implied mathematical claim of sufficient value is established in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
