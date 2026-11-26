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

Frequency Plancherel with dω/(2π) gives the stated normalized Gaussian–quadratic multiplier. The even decaying analytic multiplier reaches a maximum but no nonzero L² function is supported on its maximizing set. For t>0 its derivative is 2 exp(−a²−t²) sinh(2at) times (h_a(t)−a²−γ), divided by √π(γ+1/2). The partial fraction series makes h'_a(t)/(2t) strictly decreasing from 4a²/3−1 to −1. For a≥√3/2 the bound h_a−a²<1/4 follows for u=2at≤3/2 from u coth u<1+u²/3 and monotonicity of s+u²/(4s) on s≥3/4, and for u≥3/2 from AM–GM and 2u/(exp(2u)−1)<1/4. This settles the centered regimes. For γ<1/4 and a≥a_c the hump maximizer satisfies u/(2a²)=coth u−u csch²u<1, so the envelope decreases strictly; u tends to infinity as a tends to infinity since (coth u−u csch²u)/u has a positive limit at zero and is positive on bounded intervals. The envelope is bounded above by 2u/(exp(2u)−1) and below by its positive test value at u=2a²; it tends to zero. The resulting unique fold has lower off-center height than center height, whereas at a_c the off-center height is higher. The difference decreases strictly on the intervening outer branch, by stationarity and strict decrease of the density beyond a_c. This gives one equal-height crossing and a strictly larger right norm slope; no inner stationary point can tie the center. The quadratic and quartic h_a coefficients give the two onsets, and the explicit sinh factor gives the order-six positive critical deficit. Checked the supplied verification description and code by inspection; independent Simpson quadrature and bisection gave a*=0.95234115163 and t*=0.82899868124 for γ=1/8, and displacement-to-prediction ratios 0.999941 and 0.999995 for γ=1/4 and γ=0.4 near the continuous transitions. The numerical checks are ancillary to the analytic argument.

## originality

PASS

The supported distinction is the global phase classification for the incoherent mixture on the frequency-unbounded strip, including the exact weight separating discontinuous and continuous transitions. The same strip with a pure first-Hermite window already has a first-order transition, and the same pair of channels on a disk already has an eigenvalue inversion law. Neither inspected result covers the retained weight-dependent strip classification.

## value

PASS

The optimizer map and norm corner resolve how including a Gaussian channel changes concentration in a natural time marginal. The exact tricritical weight and fourth-root law distinguish global and local transitions; they are not a restatement of Plancherel or of the pure endpoint. The scope excludes finite frequency cutoffs and coherent windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
