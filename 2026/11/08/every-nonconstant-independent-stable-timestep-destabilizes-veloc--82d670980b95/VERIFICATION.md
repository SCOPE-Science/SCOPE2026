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

The unit-oscillator half-kick/drift/half-kick map is M(h)=[[1−h²/2,h],[−h(1−h²/4),1−h²/2]], det 1; direct multiplication verifies M(h)^T diag(1−h²/4,1) M(h)=diag(1−h²/4,1), positive for 0<h<2, so constant-step powers are bounded. For any distinct support timesteps a,b, independent symbolic computation verifies trace(M(a)M(b)M(a)^−1M(b)^−1)=2+a²b²(a−b)²(a+b)²/16>2, making the generated subgroup noncompact. No finite invariant set of real lines exists: singleton would give a real eigenline of elliptic A/B; a two-line set would force both matrices traceless and a=b=sqrt(2); ≥3 lines would force finite projective action inconsistent with a hyperbolic commutator. Bounded M(h) and inverse on (0,2) ensure integrable log norm; the classical Furstenberg theorem then gives an almost-sure strictly positive top norm Lyapunov exponent for every iid non-point law, and the strong law converts this to physical-time growth λ/EH>0. The point-mass exponent is zero. Independent exact check gives trace(M(1)M(6/5))=−347/250 within (−2,2), so that deterministic alternation is bounded. Finite exact checks confirm identities, not the probabilistic theorem.

## originality

PASS

Best-of-knowledge new claim is the sharp no-exception dichotomy for every iid nonconstant timestep distribution for this exact velocity-Verlet harmonic-oscillator family, proved via its explicitly hyperbolic commutator and finite-projective-orbit exclusion. Classical Furstenberg positivity is expressly an external input; earlier RKN/Verlet work inspected treats periodic timestep resonance, and related random symplectic-Euler papers address a different step matrix and mean-square rather than almost-sure norm growth. No covering all-distribution theorem was identified in actual targeted Resultary and primary-literature searches.

## value

PASS

A strong stability-versus-randomness boundary for a standard symplectic integrator is mathematically motivated: every fixed admissible step preserves an energy norm, yet arbitrary nonconstant iid modulation has positive sample-path Lyapunov exponent even when periodic alternation from the same two steps is elliptic. The exact universal quantifier and dynamical contrast are more than routine norm computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
