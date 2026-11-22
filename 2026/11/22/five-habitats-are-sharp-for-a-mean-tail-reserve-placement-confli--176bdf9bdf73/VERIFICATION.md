---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact checks and limits

The accompanying `CHECK.py` is an executable, standard-library-only Python 3 reproducer for the precise finite claim. `python3 CHECK.py` enumerates every binary state of the five-cycle, recomputes the Markov agreement-count table and verifies the polynomial identities coefficient by coefficient, with no floating-point tolerance. It also checks the four-site complement involution for all binary states and both layout classes; the triangle layout class is confirmed by symmetry.

The analytic proof separately provides the strictly positive normalizer and quadratic factor, the exact sign of the full-accessibility difference for every \(0<q<1\), and the equality case \(q=1/2\). Thus finite exhaustion is a complete proof for the stated maximum size \(5\), not an approximation to a general-cycle assertion. The normalized finite system is not a field model, and no infinite-size extrapolation is inferred. Historical originality is assessed only relative to the accessible published evidence and mathematical index comparisons; no external independent audit has been performed.
