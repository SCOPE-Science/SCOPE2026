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

# Reproducibility and checks

Run `python3 verify.py` from the directory containing the extracted files, using a standard Python 3 installation. The checker constructs the twenty coloured row-pair slots, verifies that the ten-column block visits each slot exactly twice, that the four-column subblock visits sixteen different slots, and that the five-column block has the exact two-zero/sixteen-one/two-two slot distribution. It also checks the parity obstruction for every set of zero, one or two exceptional row pairs: no such set meets all ten triangles on the five rows.

Finally it independently enumerates every possible pair of columns and row pair to count actual monochromatic rectangles in the construction at each width from one to 120, comparing that result with the theorem and the coloured-slot count.

The expected output ends with `VERIFY_OK`. Finite tests independently corroborate the proof's explicit incidence certificates and boundary cases. The unrestricted mathematical conclusion depends on the convexity, parity, and ten-residue construction arguments stated in RESULT.md. No independent audit was performed, and there is no external certification claim.
