---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The orthogonal spin-3 and spin-1 real bases have squared norms 24 and 8 before normalization; they are four independent OU eigenfunctions at eigenvalue -3 and exhaust the binary third chaos. Independent polar integration gives angular averages (3/8,0,1/4,1/8,3/8) and radial factors (46080,30720,21504,15360,11264), in order of increasing trace multiplicity in the fourth moment. The sole angle-dependent average acquires cos(alpha-3 beta); hence the normalized quartic coefficients are 30,168,66,40 sqrt(3). After subtracting 30(a²+b²)² and taking out b², the smallest possible quadratic form has matrix with diagonal (108,36) and off-diagonal -20 sqrt(3). Its smaller eigenvalue is positive, 72-8 sqrt(39), with positive eigenvector ratio a/b=(2 sqrt(39)-9)/(5 sqrt(3)); when b>0 equality also forces relative phase pi. Thus only b=0 minimizes the fourth moment. The upper deficit at cos(delta)=1 factors as 63(a-b/sqrt(3))²(a²+2ab/sqrt(3)+9b²/7). At its nonzero zeros the phases are aligned; the elementary formula for cos³ identifies these and only these with the rotated H3 direction. The ratio is continuous on the connected unit sphere, so all intermediate values occur. Zero is trivial in the stability estimate and excluded from the ratio. Replay: python3 -B /workspace/audit_checks/3.py (independent exact radial/angular arithmetic; the universal implications and equality checks are analytical).

## originality

PASS

Pass for the full binary-chaos lower extremum with the sharp trace stability and mixed equality geometry. Neither the value 30 on the harmonic sector by itself nor the rank-one upper endpoint is credited as novel. The classical Wiener product formula already yields the upper bound via contraction Cauchy–Schwarz and rank-one attainment.

## value

PASS

The first Gaussian cubic-chaos space with both an angular harmonic and a Wick trace sector is a natural test of how traces affect low kurtosis. The exact positive trace penalty and the phase and amplitude of its nonharmonic saturators give more than an endpoint benchmark: they identify the worst departures from the harmonic minimizers. The classical upper endpoint and a separate harmonic example are not the grounds for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
