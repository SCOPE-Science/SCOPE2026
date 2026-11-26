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

The stated continuous-time rates have the column/row balance needed for uniform stationarity: reversing a single flip changes the sign of T_i=s_i(s_{i−1}−s_{i+1}), and ΣT_i=0. Positivity for |δ|<1 gives uniqueness. The stationary natural-log increment is −ηT_i with η=artanh δ. For distinct i,j, the generator of s_i s_j is −2s_i s_j plus (δ/2)[s_j(s_{i−1}−s_{i+1})+s_i(s_{j−1}−s_{j+1})]; after setting j=i+2 and summing, the distance-one and distance-three sums cancel in pairs, including at N=4. Thus LQ=−2Q for Q=Σs_i s_{i+2}; the drift is δη(N−Q)/2 and the centered drift is removed by h=−δηQ/4. In stationary time, the corrected martingale has variance exactly t times the mean bracket intensity; the bounded terminal correction changes the variance by O(√t)+O(1). Averaging each corrected jump square over s_i leaves rate 1/2; the cross expectation is zero because the distance-one and distance-two sites are disjoint for N≥4. The two distance-two sites coincide iff N=4 in this range, so their sum has squared mean 4 there versus 2 otherwise, while the distance-one difference always has second moment 2. This checks the factors, including the absence of an extra factor of two from the time unit. For δ=0 all entropy increments vanish; the exceptional variance enhancement is only numerically distinct for δ≠0. The packaged rational enumerator and optional spectral test were inspected, not executed. The all-size proof takes the stationary long-time limit at each fixed N.

## originality

PASS

The supported novelty is the exact second asymptotic cumulant on the finite biased continuous-time ring with N≥4 and the unique four-site correction; the model, mean-rate formula and martingale method are not credited as new. The exact three-site SCGF in a different same-day record is an overlap for N=3 only, and its date does not substantiate precedence. An abstract of a closely related older annihilation/creation current paper was located; its full equations and parameter coverage could not be confirmed, so it is a specific residual risk, not a negative full-text finding or a reason by itself to fail.

## value

PASS

A stationary rate of entropy noise is a natural quantitative invariant beyond mean dissipation. The result identifies exactly when the noise per spin differs from its large-ring expression, rather than providing an arbitrary small-size example; the isolated wraparound is explained by the distance-two corrector. The closed coefficient gives a finite-ring benchmark for current-tilt methods with a clear distinction between stationary mean and fluctuations. It is limited to zero symmetric coupling, fixed finite rings and the second long-time cumulant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
