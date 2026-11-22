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

Unitary cyclic Fourier downsampling folds k and k+N/2 into Q_k=(1/√2)[[1,1],[exp(-τλ_k),exp(-τλ_(k+N/2))]]. Equal magnitudes force cos(2πk/N)=0, unique k=N/4 only for N≡0 mod4; at that alias equality of phases is sin(δτ)=0. Thus one deficient rank-one block exactly. Its Gram determinant e^(-2τ)sin²(δτ) and trace 1+e^(-2τ) give explicit least eigenvalue a(δ,τ), with compact convergence a/δ²→τ²/(1+e^(2τ)). A Rayleigh test bounds the global least eigenvalue by δ²τ²e^(-2τ) at all delays, preventing maximizer escape. The unique critical point solves τ=1+e^(-2τ), proving optimized asymptotic and convergence of maximizing times.

## originality

PASS

Earlier symmetric finite-cycle paper establishes permanent blindness when 4|N only for zero drift; integer-line reversible spectral-gap theorem already supplies exactly the 0.1207075 best-time constant and is credited. Neither determines drift-induced recovery or the discrete sin(δτ)=0 resonances. General polyphase dynamical-sampling theory offers a reduction not the exact all-N directed theorem. Recent graph sampling preprint full text unavailable: bounded risk, not automatic failure.

## value

PASS

The exact effect of directed transport on an otherwise irrecoverable alias is a natural structural dynamical-sampling question. Complete classification of exceptional observation times and sharp small-drift noise penalty meaningfully informs sampling design, beyond the known reversible constant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
