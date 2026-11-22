---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For G=Z3 with μ total mass I, Fourier convolution gives B=μ̂(1) with B²=0, μ̂(2)=B*, and μ̂(0)=I. Every nonzero square-zero 2×2 complex matrix is unitarily similar to tE12, t=||B||>0. Fourier inversion yields A_j=(I+t ω^-j E12+t ω^j E21)/3, with eigenvalues (1±t)/3, hence positivity exactly 0≤t≤1. Direct symbolic calculation gives μ*μ=H, [A_j,A_k] eigenvalues ±i√3 t²/9 and each trace deviation 2t/3, total 2t. At t=1 atoms are rank one; for t>0 noncommutative. On Z2 the nontrivial Fourier coefficient Hermitian and square-zero forces zero; scalar Z3 likewise. Independently checked the matrix convolution products, PSD determinants (1−t²)/9, and commutator coefficient symbolically. This is a universal Fourier classification, not evidence from the finite parameter samples.

## originality

PASS

Jabbari's matrix Kawada–Itô rigidity theorem for positive matrix **idempotents** μ*μ=μ does not prohibit or classify positive roots of Haar μ*μ=H; its Example 4.1 is not a positive Haar root. Chu–Hilberdink–Howroyd's matrix-valued Choquet–Deny fixed-point criterion likewise is a different equation. The complete rank-one nilpotent Fourier orbit, positivity interval and exact extremal commutator constitute a distinct concrete theorem; priority risks remain in quantum trine POVM and finite-time-mixing folklore.

## value

PASS

Explicit minimal positive **noncommutative** convolution square root of Haar, and sharp commutator classification, marks a structural boundary of matrix-valued Kawada–Itô intuition; it is a natural finite-group rigidity counterexample, not arbitrary arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
