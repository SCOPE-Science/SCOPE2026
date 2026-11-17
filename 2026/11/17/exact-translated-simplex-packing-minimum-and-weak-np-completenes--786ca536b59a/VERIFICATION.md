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

# Verification and scope

The formula and equality-case classification follow from exact support-function evaluation and integer-coordinate range-one rigidity, not a finite enumeration. The reduction from positive-integer PARTITION is given algebraically in `RESULT.md`, with binary encoding and a pseudo-polynomial subset-sum algorithm.

Run `python3 check.py` using Python 3 standard library. It performs 300 seeded exact-rational comparisons against every primitive normal with coordinates in the finite box \([-2,2]^n\), in dimensions two through five, and five exact PARTITION reduction tests. Expected output: `PASS 305 exact rational tests (including complete primitive directions up to bound 2)`.

Finite checks cannot verify excluded directions of arbitrarily large norm; the analytic range-one proof handles those. No external proof certification or independent audit has been performed. The historical-priority comparison is provisional, not a proof of uniqueness.
