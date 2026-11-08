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

# Reproducibility and verification limits

The mathematical derivations and boundary conditions appear in `RESULT.md`. Running `python verify.py` with Python 3 and no external dependencies performs exact rational enumeration of binary valuation outcomes for markets of up to five goods and several rational parameter pairs. It separately compares candidate allocations, tests the sharp four-good witness, and checks small-probability expansions and leading optimality for additional fixed goods counts. The verifier reports 330 checks and the witness gap `7902186119/1000000000000`.

The general phase diagram, uniqueness of the critical probability, and the fixed-population asymptotic optimizer rely on the symbolic proof, not on finite enumeration or on a numerical root finder. The decimal expansion of the unique critical parameter is descriptive; its exact specification is the polynomial root. Source-priority comparisons were based on the relevant public full-text sections and bibliographic evidence; no independent publication-priority certification is claimed.
