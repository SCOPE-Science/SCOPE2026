---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The frozen RESULT.md at blob a565ef3a51dc21017604939075d3d5caa98f5950 uses characteristic polynomial (lambda²+a)(1+tau lambda/q)^q−b with a>b>0. At imaginary lambda=i omega, phase forces q arctan(tau omega/q)=j pi, j<q/2; hence q=1,2 have no thresholds, q=3,4 one and q=5,6 two. Crossing derivative has real part with sign -(-1)^j, so odd crossing destabilizes and even restabilizes; tau1<tau2 by tan monotonicity and opposite denominator shifts. Independent recomputation at a=4,b=2 returned q5 thresholds 1.6768703772/7.6996347832 and q6 1.5739820059/5.2165696032. This is linear spectral, not nonlinear stability.

## originality

PASS

Best-of-knowledge PASS: the Bîrdac et al 2026 primary preprint already supplies this center characteristic form and general kernel phase condition and shows q1 and q2 non-Hopf. Its Sections 5.4/5.5 address general and Dirac cases, not the complete integer q<=6 parameter-uniform two-switch classification. The cited 2011 distributed-delay work is a general framework and remains possible alias risk.

## value

PASS

A minimal Erlang chain length for reentrant stability is a sharply motivated finite cutoff for smoothing approximation of delayed feedback; exact thresholds valid for all a>b>0 describe which approximations alter the stability diagram, not just one numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
