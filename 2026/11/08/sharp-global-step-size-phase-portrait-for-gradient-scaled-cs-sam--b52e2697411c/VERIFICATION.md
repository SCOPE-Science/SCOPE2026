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

The exact double-scaled quadratic update reduces to t+=t|1-gamma F_rho(t)| with t=ell|x|, F_rho(t)=(1+t+rho)/(1+(2+rho)t+t²). F decreases strictly and t F increases strictly for t>=0, rho>=0. If gamma<=2/(1+rho), positive amplitudes strictly decrease to zero; at equality Taylor gives t_k~(1+rho)/[2(1+3rho+rho²)k]. Above the threshold the unique p>0 solves gamma F(p)=2, while monotone tF proves strict contraction of |t-p| on (0,2p), with eventual entrance from t>=2p unless finite zero hit. Thus every nonterminating orbit approaches the nonzero sign-alternating two-cycle. Rational checks verify direct reduction and a specific exact 2-cycle; this is not a general-function theorem.

## originality

PASS

Best-of-knowledge original under actual inspected statements; significant access or historical-priority risks are explicitly retained.

## value

PASS

A sharp complete global phase portrait for a specified two-stage curvature-scaled optimization rule, including critical 1/k decay and stable nonoptimal supercritical oscillation, identifies an algorithmic parameter boundary not supplied by generic sufficient convergence statements. Its very narrow scalar nonminimal-scale setting and limited algorithmic interpretation are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
