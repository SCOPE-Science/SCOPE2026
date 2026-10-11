---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Direct differentiation gives strict convexity of the scalar barrier objective and \(F_\delta′(0)=D(\mu)/\tau-\mu/\delta\), so zero targeting exists exactly when \(D(\mu)>0\) and then \(\delta_*=\tau\mu/D\). Substitution of \(\tau(\mu)=c\mu^a/(\mu^a+b)\) gives \(D(\mu)/\mu=x_2+\zeta c\mu^{a-1}/(\mu^a+b)\), from which the \(a>1\), \(a<1\), and strict \(a=1\) cases follow. On \(x_2+(c/b)\zeta=0\), exact cancellation gives \(D=x_2\mu^2/(\mu+b)>0\) and \(\delta_*=c/x_2\). The inspected verifier and independent arithmetic agree. The source paper prints a sign inconsistency in its displayed derivative, but its objective and denominator in equation (30) agree with the direct differentiation used here.

## originality

FAIL

The final claim is mechanically implied by two formulas printed in the same prior primary source. Equation (30) gives the zero-target relaxation with denominator \(\mu x_2+\tau\zeta\), including the requirement that the denominator be positive, and equation (32) gives exactly \(\tau(\mu)=c\mu^a/(\mu^a+b)\). Substituting equation (32) into equation (30) yields \(D(\mu)/\mu=x_2+\zeta c\mu^{a-1}/(\mu^a+b)\); the claimed exponent split and the critical coefficient identity are immediate elementary limits/algebra. Under implication-based originality, the fact that the source does not package that substitution as a named theorem does not make the corollary original.

## value

FAIL

The solver-tuning question is practically motivated, but the claimed mathematical content is a direct substitution of two same-source scalar formulas followed by elementary one-term asymptotics. Under the stated value bar this is a routine deduction rather than a separately motivated structural lemma, boundary theorem, or nontrivial classification. Correctness and practical relevance do not rescue a mechanically covered result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
