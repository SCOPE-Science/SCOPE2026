---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For exactly circulant A and an orthogonal Fourier projector Pi, block multiplication gives T_B=KR_B=[[I,0],[(I-PB)A*,PB]]. With B=P^{-1}Pi, T_0 is idempotent, and all transformed Krylov images are span{(b,(I-Pi)A*b)}, giving the exact persistent squared residual NE/(N+E) for all positive Krylov orders (mathematical spaces, even after Arnoldi breakdown). Every zero-start mask-restricted flexible iterate has physical second block in ran Pi; Fourier-mode least squares yields the stated sharp full-trial-space floor. For positive leakage epsilon, (T-I)(T-epsilon I)=0, T invertible; omitted 2x2 singular-value determinant and trace yield kappa_j and 1/epsilon asymptotics. Independent tests on 24 complex Fourier systems corroborated the identities.

## originality

PASS

PASS best of knowledge: the exact idempotent Type-2 hard-pupil transformed operator, data-dependent one-step GMRES plateau, geometric floor for all permanently range-restricted flexible maps, and sharp positive-leakage two-step/conditioning dichotomy are not given in the materially inspected motivating OFT paper or generic singular preconditioning references. The Type-2 Schur map, binary optical pupil and general possibility of GMRES breakdown are previously known and not claimed anew.

## value

PASS

A real optical pupil truncates modes regardless of Tikhonov positivity; this exact model separates algebraic solvability, Krylov residual obstruction, and extreme finite-precision sensitivity when leakage is tiny. Such a sharp model-based negative/transition result is useful to interpret or design optical Fourier preconditioners; no claim about universal noisy hardware failure is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
