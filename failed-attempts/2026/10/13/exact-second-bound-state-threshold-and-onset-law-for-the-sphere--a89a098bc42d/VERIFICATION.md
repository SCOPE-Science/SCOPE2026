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

The source uses Φ(−ν²) for the matrix denoted Φ(ν) in the finding; no coupling rescaling is needed. Write A=4πΦ. Its scaled zero-energy determinant is D, and A11(0)=−μ. Its negative inertia is two for D>0 and one otherwise. For ν>0 the derivative is the positive-definite resolvent Gram matrix, since no nonzero combination of the distinct point and surface measures vanishes and the resolvent smoothing is injective. The large-ν matrix becomes positive definite; strict eigenvalue flow therefore gives exactly one crossing per initially negative eigenvalue and no positive-ν crossing from the zero mode at D=0. The off-diagonal is nonzero, so the zero eigenvalues are simple. Solving D>0 gives the stated finite λc precisely when μa²>R. For the onset, direct expansion gives det A = D − [D/μ + (aμ−1)²/(a²μ)]ν + [−1+2μR/3−R²/(3a²)]ν² + O(ν³). For D↓0 the smaller positive root tends to zero: at any fixed ν>0 the eigenvalue emerging from zero at threshold has become positive, and continuity gives the same sign nearby in D. Balancing the first nonzero ν term proves both asymptotics; on aμ=1 the ν² coefficient is −[(a−R)²+2a²]/(3a²)<0 and (D/μ)ν=o(D). The written expansion was checked symbolically in a separate replay using the first three entry coefficients; the frozen finite root scan was inspected, not executed. No assertion about the spectral nature of the state at energy exactly zero is needed or certified.

## originality

FAIL

No verbatim statement of the threshold and onset was located, but the defining primary paper already supplies the exact normalized two-by-two matrix, positive eigenvalue flow and the spectral equivalence with its zeros. Evaluating the determinant at zero and Taylor expanding it through order two is sufficient to recover the entire claimed negative-spectrum result, including the exceptional coefficient. This is demonstrable implication coverage, not a finding of verbatim publication or a conclusion based on inaccessible literature.

## value

FAIL

The sharp transition and different onset orders are naturally motivated and useful to spell out. In the frozen scope, however, the 2022 result already specifies the exact spectrum by an explicit two-by-two determinant, proves the relevant sign flow, and exhibits the transition. The proposed outputs require only evaluating this same determinant at zero and its first two Taylor coefficients; the finding does not solve a separate threshold-state or multi-parameter problem. This makes the result useful exposition of a known model rather than a distinct valuable exact finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
