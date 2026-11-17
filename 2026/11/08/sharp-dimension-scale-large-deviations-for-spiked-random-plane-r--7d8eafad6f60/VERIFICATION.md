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

For H=lambda_perp I+Delta uu^T the Ritz optimum is squared norm of u projected onto span(v,x), so the exact spectral-gap factor is W=1-(p dot x)^2. A uniform tangent x in dimension d-1 has squared fixed-direction overlap Beta(1/2,(d-2)/2); thus each W is Beta(a_d,1/2), a_d=(d-2)/2, and conditional distribution independent of past proves the factors iid. The exact gamma-ratio formula for E[W^q] holds for q>-a_d, and at k_d=floor(cd) its scaled log moment generating function converges for theta<1/2 to -c/2 log(1-2theta). The derivative range (0,infinity), tilted variance O(1/d), and exponential tightness prove full speed-d LDP with I_c(s)=(s-c-c log(s/c))/2 on s>0 and +infinity for s<=0, plus the two one-sided exponent statements. Under all finite d>=3 the gap stays positive almost surely. The package verify.py was read and checks independent Ritz eigensolutions; no finite tests are used as the LDP proof.

## originality

PASS

Bresch–Melnyk (October 30, 2026) primary full 25-page manuscript was materially inspected: Algorithm (2), Example 2.4 and Proposition 2.5 supply exact spiked expected contraction and one-step spherical cap estimates, but not the dimension-linear k_d~cd logarithmic gap full LDP or its both-sided success/failure rates. The known conditional Beta law and generic Gartner–Ellis/Cramer machinery are ingredients, not separate inventions. Related Resultary codimension-only Beta law concerns repeated maximal eigenvalues and fixed-step small-gap local asymptotics, not joint dimension-iteration rank-one rate I_c. A hidden general Gamma/Beta-product theorem may make this rate a corollary, so best-of-knowledge priority only.

## value

PASS

The probability of obtaining a specified multiplicative Rayleigh-error reduction after a budget proportional to dimension is a natural algorithm-reliability question. The exact two-sided rare-event exponent distinguishes expected contraction from high-probability performance and supplies precise success/failure thresholds inaccessible from expectation alone. The new joint asymptotic is a substantive motivated classification even though its Beta and Gamma ingredients are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
