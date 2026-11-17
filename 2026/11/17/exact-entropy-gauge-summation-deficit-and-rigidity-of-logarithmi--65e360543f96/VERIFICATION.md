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

Analytic verification: the gauge is coordinatewise increasing on nonnegative sequences; the joint distribution built from coordinate masses makes summand gauge sums equal to \(S(1+H(J\mid I))\), and the gauge of the coordinatewise absolute envelope equals \(S(1+H(J))\). The Shannon chain rule yields the displayed exact nonnegative deficit. Equality is characterized by zero divergence, zero row-conditional entropy, and zero column-conditional entropy. Pinsker and the binary-entropy chord bound give the stated quantitative rigidity cutoff.

Finite checks: after extraction, execute `python3 check.py`. The script tests the exact four-term identity on 8,400 deterministic random finite arrays, verifies nonnegativity to roundoff, and tests extremal coordinate arrays. Finite tests are diagnostics, not infinite-dimensional certification.

Full-text comparison: the 2026 motivating preprint's Section 4 and related theorem statements were inspected in accessible HTML. A closely related result concerning a different rearrangement gauge was compared at the mathematical-statement level. Older related primary work was identifiable, but full-text comparison remained limited; this is a priority limitation rather than evidence that the older literature is disjoint.

Independent audit: not yet performed.
