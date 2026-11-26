---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a permutation involution with k transpositions and f=n−2k singletons, a sign is constant on each cycle. Fixed vertices require zero singleton signs but allow either sign on each pair, which leaves k+f free bits and gives n!/(k!f!) fixing elements, all even-signed. Among all signed involutions exactly half the signs have even parity unless f=0, when all do. This verifies the exact numerator, denominators and spectrum. In the coefficient proof the Poisson saddle solves tr+2r²=n, with variance v=tr+4r². On |θ|≤n⁻²/⁵ the absolute error after quadratic expansion is bounded after integration by O(n∫|θ|³ exp(−c n θ²)dθ), i.e. relative O(n⁻¹/²). Outside both saddle neighborhoods the 2V factor supplies exp(−c n¹/⁵); the π neighborhood has exp(−2tr) times a Gaussian bound. The constants are uniform for t in a compact positive interval. Stationarity gives the derivative of the saddle exponent r_t=√(n/2)−t/4+O(n⁻¹/²), which integrated from 1 to 2 gives the 3/8 constant. For t=0 the odd case is zero and the even case has two equal saddle peaks; the ratio to A_n(2) is exponentially small. The conditional mgf is A_n(e^s)/A_n(1) with 2L_n−n equal to the singleton count. Taking s=u/(n/2)^(1/4) in the uniform expansion and subtracting the centering term leaves u²/2. The recurrence corroborates the rare-event normalization at sampled large n for both parities. The independent Laguerre reduction in the originality assessment also recovers both asymptotic claims with the requisite uniform remainder.

## originality

FAIL

The two advertised asymptotic results are direct corollaries of the classical uniform Perron expansion for Laguerre polynomials after an exact even/odd identification. The same expansion gives the entire normalized coefficient function, including the stated error and uniformity for the conditional mgf. This is verified stronger coverage plus exact substitutions, not a failure based on unavailable literature or an assertion that the identical cube-action wording was previously printed. The exact signed-cycle counts are already excluded from the claimed novelty.

## value

FAIL

The rarity and conditional geometry are natural questions, but the exact spectrum is credited known material and the advertised quantitative advance is a direct specialization of an established expansion, with parity and a standard change of variables in its generating function. The record does not isolate a new obstruction, regime, or stronger bound surviving that reduction. This is a useful exposition of an application, not a distinct mathematical contribution under the narrow-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
