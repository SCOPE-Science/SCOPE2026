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

# Exact arithmetic verification

Execute `python3 verify.py` using the Python standard library. It computes both integral sequences from the published recurrence through index 399; derives their first thirteen coefficients independently from formal eta products and exact Lagrange series reversion; and compares their first eleven integer terms with Cooper's published Table 5. It tests the base-five digit-product rule on indices 0 through 399, and independently enumerates residue pairs on complete blocks of lengths \(5^L\) for \(0\le L\le7\), totaling 97,656 examined indices over overlapping blocks. It also checks the eight-cell Parseval sum against \((2\cdot5^L+5)/8\) for \(0\le L<24\) using exact integers. No external downloaded data, library, or floating-point calculation is needed.

The checks provide finite independent consistency evidence but are not a proof of the all-index Lucas congruences: the proof explicitly relies on the cited published Lucas theorem. The multinomial/character derivation establishes the closed formulas for arbitrary \(L\) and the infinite occurrence claim. External independent audit has not been performed.
