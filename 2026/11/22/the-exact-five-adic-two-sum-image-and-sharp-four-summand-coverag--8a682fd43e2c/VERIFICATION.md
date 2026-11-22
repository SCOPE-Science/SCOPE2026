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

# Finite verification and boundaries

Execute `python3 verify_motzkin_sumsets.py` using Python's standard library. The successful replay terminates in `VERIFY_OK checks=2570258`.

The checker generates the first 1,601 Motzkin numbers from an integer recurrence, checks each against the 2004 zero-index criterion, directly constructs all finite projections of \(X\) and \(\mathcal Z\), enumerates ordered twofold and fourfold supports for \(1\le k\le6\), and tests the exact formulas and all five signed-four-variable digit patterns. These are finite spot checks and full enumerations only at the specified finite moduli. The infinite twofold support and sharp fourfold coverage are mathematical consequences of the checked antecedent and the proof in RESULT.md; they are not certified by the finite run alone.

The checker does not count fiber multiplicities or claim exact ordinary integer representations. The original Deutsch--Sagan Motzkin-zero criterion is treated as published mathematical input, not re-proved in this package. Independent mathematical audit has not been performed.
