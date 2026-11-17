---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Exact Pauli-projector identity gives D=1-|t|/sqrt(t^2+epsilon^2) and L=epsilon^2/(sqrt(t^2+epsilon^2)+|t|). Dominated convergence at fixed nonzero t produces moment exponents 2q below q=1/2, 2p below p=1. Scaling t=epsilon*u with density continuous positive at 0 produces exponents 1 and p+1 above transitions, and intermediate |t|^-1 integrals give logarithms at thresholds. Same-T coupling yields explicit positive finite C_P(theta), C_lambda(theta), with norm mean squares negligible versus epsilon and epsilon^3. Independent high-precision quadrature reproduces both uniform-density exact identities at epsilon=0.1,0.01. The proof, not finite quadrature, covers arbitrary eligible f.

## originality

PASS

Standard avoided-crossing diagonalization and multilevel eigenpair difficulties are prior concepts. Inspected abstracts of Dölz–Lozano-Simón 2026 and general isolated-eigenspace collocation do not claim this exact individual-eigenprojector q=1/2 versus eigenvalue p=1 statistical rate spectrum or the coupled same-T constants. Originality is best of knowledge; the highly relevant 2026 full manuscript could not be read through available interfaces and is a significant residual priority risk.

## value

PASS

A deliberately canonical 2x2 crossing benchmark distinguishes stable cluster projections from unstable individual eigenmodes. Exact moment and centered two-level variance exponents give precise test targets for multilevel uncertainty algorithms; a natural singular boundary at eigenvalue coalescence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
