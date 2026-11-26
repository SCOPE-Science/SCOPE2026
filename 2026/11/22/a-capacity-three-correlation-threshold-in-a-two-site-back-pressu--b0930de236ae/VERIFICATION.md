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

The hop maps x>y to y′≤x′+1; arrivals/exits also preserve that inequality. From (j,j) one can reach (j+1,j+1) via an arrival, hop and arrival, passing through (j,j+1); further arrivals reach all other states with x≥y from (y,y). Exiting to y=0 and alternating a hop and exit drains any remaining upstream stock, including from outside the class. Thus the recurrent support and uniqueness hold for t>0. In a separate symbolic solve I constructed the full generator on (c+1)² states, replaced one adjoint equation by normalization, solved over the polynomial domain, checked all unchanged balance equations, and recovered supports 4, 8, 13 and all three rational covariances identically. Replay: `python /workspace/review_replay.py 2`. At t=1 the exact fractions are −1/25, −1/45, 1/1024. The capacity-two cubic and capacity-three septic in RESULT.md have exactly one positive sign variation and positive leading coefficient; the former changes sign across the rational enclosure and the latter stays negative at zero and at one (−8). With the strictly positive denominators this proves the stated signs, not a parameter grid inference. Only simultaneous stationary covariance at equal rates 0<t≤1 for the stated capacities is established. The supplied exact balance verifier was inspected, not executed.

## originality

PASS

The same finite-capacity dynamics are prior and the ordinary one-floor result is a baseline. The distinct claim is the sharp two-site small-capacity and drive classification and in particular the first positive capacity at unit drive. The strongest located competing finite-site result has a different generator, and the located primary back-pressure statements compare different observables or scales.

## value

PASS

The exact minimum capacity at maximal drive is a meaningful small-system test of whether the familiar exclusion anticorrelation survives back-pressure with buffers. The result separates opposite signs at adjacent capacities and identifies exactly how changing drive affects the first three capacities. That is more informative than quoting a stationary linear-system recipe or a simulation at one point; no claim of a large-chain phase transition is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
