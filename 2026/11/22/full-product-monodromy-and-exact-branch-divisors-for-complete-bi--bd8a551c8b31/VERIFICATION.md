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

# Verification record

The mathematical proof is symbolic and applies uniformly to all integers \(m\ge2\) and \(n\ge3\) in characteristic zero. Its principal steps are the invertible Lagrange evaluation map, generic symmetric invariant fields, irreducibility and simple ramification of the universal polynomial discriminant, and a tensor-product trace pairing.

The included `checker.py`, requiring Python 3 standard library only, verifies exact interpolation formulas for \(3\le n\le8\), irreducibility by rational-root exclusion for two specific cubics, their exact nonsquare discriminants and distinct quadratic subfields, and the trace-discriminant determinant identity for the resulting degree-nine tensor algebra. The explicit specialization is evidence of an instance, not a proof for all parameters.

The calculations and the general proof have had self-review. No independent mathematical audit has been performed. The arithmetic group at any chosen specialization and the compactification outside the stated parameter open are not determined by the universal theorem.
