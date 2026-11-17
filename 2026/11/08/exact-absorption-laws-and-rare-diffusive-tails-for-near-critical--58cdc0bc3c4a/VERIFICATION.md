---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The first chosen winner and next chosen winner yield only two nonabsorbed branches (m,k) and (m-1,k+1), with weights (k-1)/m and k(m-k)/[m(k+1)] for k>=2, and then unbiased two-player ruin on 0..m+k. Boundary k=0 absorbs at time1; k=1 has first-step absorption 1/m; k=m omits second branch. Solving the discrete harmonic ruin PGF yields the claimed cosh formula and exact mean 2+k(m-2)+k^2/m for k>=2, E tau=m for k=1. For k/m->alpha>0 the Laplace transform converges to Brownian first-exit with generator (1/2)d²/dx². For sparse k=o(m), the killed sine series must control high negative eigenvalue modes as the proof explicitly does; dominated convergence yields Phi(t) and the mixture weights yield the m/k prefactor. Reflection principle plus half-line survival bound shows tau/(mk)->0 and Tonelli gives ∫Phi=1. Independent direct unreduced rational Markov simulation matched ruin-mixture survival for every m=2..6, k=0..m, t=0..10; finite checks are supplementary only.

## originality

PASS

Adjei–Krishnan–Mossel 2026 v2 Remark 3.4 already explains the qualitative first-two-round reduction near one card each and predicts the mk order at sparse excess. These ideas and classic gambler ruin are credited, not presented as new. Their relevant full text does not give the exact all-(m,k) finite law/PGF, positive-density Brownian exit transform, rare diffusive theta tail, or proof of collapse in probability despite mean growth.

## value

PASS

The exact hitting-time law resolves a concrete transition case raised in the motivating primary paper. Its sparse-excess mean mk is dominated by rare m²-scale trajectories even though the typical duration divided by mk converges to zero. The explicit theta-series rare tail and all-m,k finite law are useful natural invariants, not mere simulation improvements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
