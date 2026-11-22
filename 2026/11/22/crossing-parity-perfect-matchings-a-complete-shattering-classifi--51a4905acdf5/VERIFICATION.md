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

# Reproduction and verification

Run `python3 verify_parity_matching.py` with Python 3.9 or newer. The script has no third-party dependencies. Its expected exact stdout is in `verification_output.txt`.

The script generates every perfect matching of six, eight and ten vertices (also four for boundary checking), computes crossing parity from explicit endpoint interlacing, and tests every binary labeling of every partial-matching support of size at most one less than the number of pairs. It checks the proposed characterization and coefficients without calling the formulas to decide shattering. There are 18,556 support/parity comparisons and 76 small forbidden-matching extension tests.

Proof obligations for arbitrary orders are discharged by the three-pair parity-avoidance base and induction, the fixed-four-vertex switch parity rule, and the isolated-chord signed Pfaffian expansion in `RESULT.md`; finite runs cannot independently certify the universal quantifiers. The six-vertex lemma's inclusion-exclusion counts and the proof that at least one positive-sign matching contains any given chord are spelled out there. The standalone script is a consistency check only. External independent mathematical audit has not been performed.
