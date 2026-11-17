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

# Reproducibility checks

Run `python verify.py` with Python 3. The script evaluates independently reconstructed Cartesian vertex coordinates for strictly convex alternating-radius polygons. It checks positive turns, all equal side lengths, shoelace area and the exact formulas and bounds, for even orders 4 through 100 at multiple admissible ratios and scales and for odd regular orders 3 through 101. When SymPy is present it also checks the algebraic derivative and boundary identities. A local execution returned `PASS: 283078 edge/turn/area/formula consistency checks across side counts 3..100`.

The essential infinite statement is not certified by numerical tests. Its analytic proof is in RESULT.md: the sine-law two-branch recurrence, exclusion of increasing branches by cyclic strict convexity, sharp positive-turn conditions and exact area derivative computation. There are no numerical approximations in the mathematical equality or inequality claims. The limiting degenerate polygons are excluded by the standing strict convexity hypothesis.

Independent mathematical audit: not performed.
