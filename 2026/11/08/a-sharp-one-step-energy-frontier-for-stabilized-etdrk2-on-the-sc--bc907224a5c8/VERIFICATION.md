---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reduction v=u(1+H(1-u²)), Phi=u W_B with B∈[0,H] and H<=1/alpha<=1 gives Phi>=u>=0 for u>=0 and alpha>=1. For B=H exact P(z,y,t)=[2-z(1+W_H²)]/(1-z) on [0,1]^3; independent exact algebra reconstructs 46 monomials and all 729 rational degree-eight Bernstein coefficients >=1/8 (minimum index (1,8,8)), hence Phi²+u²<=2 by endpoint interpolation and energy-difference factorization. For alpha<1 derivative at u=1 has large-step limit (1-2/alpha)²>1 (alpha=0 direct), giving energy increase near equilibrium. At alpha=1 output can exceed one; no iterated result. The exact finite coefficient certificate and Bernstein convexity, not random tests, prove positivity on the whole cube.

## originality

PASS

Best-knowledge PASS: Fu–Shen–Yang prove sufficient unconditional energy conditions with global Lipschitz nonlinearities, not an exact minimum scalar stabilizer for untruncated quartic on single-step input interval; 2026 Quan et al general framework similarly does not supply iff alpha>=1. The 2022 paper inaccessible full text remains an explicit priority risk.

## value

PASS

PASS: The absolute minimal stabilizer for all stepsizes and all inputs in the physically natural scalar order-parameter interval is a sharp structure theorem with an exact positivity certificate. The non-invariance caveat matters to numerical integrator theory and avoids an unjustified trajectory claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
