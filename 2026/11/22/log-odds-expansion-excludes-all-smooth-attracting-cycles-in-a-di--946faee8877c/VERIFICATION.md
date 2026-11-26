---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For a branch write y=x+s x(1−x), |s|≤1. The image of an interior point stays interior, including s=±1. Expansion gives x(1−x)f′(x)=y(1−y)+(y−x)². Thus the log-odds branch derivative is exactly 1+(y−x)²/[y(1−y)]. Staying off both thresholds ensures a smooth branch itinerary locally through each finite return. Over the cycle the log-odds coordinate factors cancel, and at least one step is nonzero. The product is therefore >1 and is bounded below by 1+4 times the sum of the squared increments, using y(1−y)≤1/4 and dropping all cross terms. This proves hyperbolic repulsion at every least period in scope. Independently, the specified example has steps ±7/50, ordinary derivatives 61/40 and 449/561, product 27389/22440, and lower bound 723/625. CHECK.py was inspected, not executed; the exact arithmetic and branch proof do not depend on that script. No differentiability at the cuts or conclusion about their periodic cycles or about endpoints is needed.

## originality

PASS

The nearest prior sources cover the exact map's two-cycle existence and all-period repulsion for a different one-cut map. Neither implies the universal quantitative multiplier theorem for the given three independent branch coefficients. The identical indexed record is not independent coverage; the decision is limited to the stated formula and repulsion obstruction in the two-cut family.

## value

PASS

A parameter- and period-uniform stability obstruction resolves a natural question about the existing two-cut model: existence results for specific cycles cannot determine whether an interior, smooth itinerant attractor can be periodic. The formula gives a quantitative reason that holds even on branches with ordinary contraction, and the rational two-cycle establishes that the obstruction is not vacuous. Neither global convergence nor exclusion of border cycles is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
