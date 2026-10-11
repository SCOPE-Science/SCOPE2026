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

At the published extremizer, \(F_0=p_0\overline H\), so at a zero of \(H\), \(dF_0=p_0\,d\overline H\) and \(J_{F_0}=-|p_0|^2J_H\). The source proves \(H\) has no singular zeros and counts \(n\) sense-preserving and \(2n-1\) sense-reversing zeros, yielding the audited reversed Jacobian split. Applying the real-analytic implicit-function theorem simultaneously at the finitely many simple roots gives distinct analytic branches under all coefficient perturbations; continuity preserves signs, and the published universal \(3n-1\) upper bound rules out any additional roots.

## originality

FAIL

The full-coefficient openness claim is a routine local consequence of the already published sharpness proof. Lazebnik--Lundberg prove an extremal example with exactly \(3n-1\) zeros, verify that the associated harmonic function has no singular zeros, and in Remark 3.5 already record openness under variation of the construction parameter \(c\). Their paper also quotes the prior universal \(3n-1\) upper bound. Once every base zero is nonsingular, the real-analytic implicit-function theorem applied to the full finite coefficient vector gives \(3n-1\) persistent distinct branches; the existing global upper bound prevents extra roots. The orientation split persists by continuity of the nonzero Jacobian. Thus the audited theorem is implication-covered even though the exact phrase “all coefficients” is not printed in the source.

## value

FAIL

Robustness of a nonsingular extremizer is a natural question, but once the source has already proved every extremal zero nonsingular and even remarks on one-parameter openness, extending the same implicit-function argument to the full finite coefficient vector is routine. The upper bound closes the count automatically. Under the stated value bar this does not constitute an independent mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
