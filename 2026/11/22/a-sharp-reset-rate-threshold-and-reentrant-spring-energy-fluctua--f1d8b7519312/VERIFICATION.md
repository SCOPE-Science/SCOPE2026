---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At reset epochs the retained coordinate is an affine recursion with i.i.d. interval/innovation pairs. For T~Exp(r) its multiplier (g+exp[-(1+1/g)T])/(g+1) lies strictly between 0 and 1 almost surely, so its pth-moment contraction factor is <1 for every p>=1. The innovation is Gaussian conditional on T, with variance O(1+T), so the perpetuity exists uniquely with all polynomial moments; interpolation over stationary renewals preserves these moments. Poisson compensation gives the time-stationary law as the law seen just before resets. Independent exact linear solves of the degree-two and degree-four generator equations with the reset term -r M_ij for i>0 reproduced the displayed A/[(g+1)^2 B], the positive mean, and both endpoint laws from RESULT.md 5–20, 33–69. The difference is 2P(r)/(r+4) with P strictly increasing on r>0; exact signs bracket its unique root at 0.49168 and 0.49169. The reduced g-derivative numerator has degree 7 and a positive denominator. On r=1/2+t/10, 0<=t<=1, exact signed Bernstein minima in degrees 7,5,4,3,2,1,0 are 54075/128, 126400338/15625, 131263578/15625, 463806/3125, 2461/2, 1086, 180; the minimum for -N_r(1) is 14591839608/1953125. Thus the g^6 coefficient cannot change the two Descartes sign variations; signs at 0, 1 and infinity give two distinct positive roots, hence both simple, with the claimed extremum order. At r=1/2 the signs at g=0.38,0.39,16.1,16.2 are +,-,-,+. Replay: /workspace/branches/456f1caf-8ee8-49b9-8740-f78b71b7167e/independent_check.py and exact_check_output.txt. VERIFICATION.md, verify.py and simulate.py were read as evidence, not executed. Endpoint ordering does not assert monotonicity, and the turning-point count is proved only on the stated closed rate interval. The stationary laws are taken at finite positive g before limits.

## originality

PASS

Best-of-knowledge pass for the signed spring-jump relative-variance crossover and certified two-turning-point interval, not for the probe-only reset model, mixed-moment hierarchy, or routine derivation of the jump mean from known second moments. General moment solvability does not itself classify the stationary points of this particular quotient.

## value

PASS

The observable is a specified energetic effect at each reset, distinct from either position fluctuations or the full cost of reset control. A threshold that reverses which memory endpoint has less relative noise, and an exact interval with both a maximum and a minimum between those endpoints, reveal why endpoint comparisons alone cannot identify favorable intermediate memory. No all-rate extremum classification or implemented-work claim is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
