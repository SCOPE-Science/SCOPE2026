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

On fixed bi-infinite grid, Steffen limiter has same-sign secants and partial slopes in [0,2]. Hermite derivative A=6t(1−t), B=3t²−4t+1, C=3t²−2t has ∫|B|=∫|C|=8/27 and A+aB+bC≥0 for 0≤a,b≤2 by checking four polynomial corners. Perturbing just one secant gives central TV h_i|δs_i| and neighboring TV ≤(16/27)(h_{i-1}+h_{i+1})|δs_i|. Telescope finite secant changes and pass to bi-infinite ℓ¹ by Fatou; this proves upper bound. Choose adjacent secants large positive compared to the center so both strict selector branches are 2s_i, giving exact lower bound for each i, including infinite unbounded mesh-ratio case. Independent exact basis/abs integrals and h triples (2,1,3) give 107/27. Individual signals are cellwise monotone, so one-input TV preservation is separate from two-input bound.

## originality

PASS

Best-of-knowledge original contribution remains after subtracting credited prior special or broader results; each of four implication comparisons and source inspections below document the boundaries. 

## value

PASS

The sharp iff mesh-shape-regularity criterion for two-input BV stability of an established interpolation scheme locates a meaningful conditioning failure invisible in monotone one-signal TV. It is an all-grid structural boundary with explicit local witnesses, not a cosmetic uniform-grid constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
