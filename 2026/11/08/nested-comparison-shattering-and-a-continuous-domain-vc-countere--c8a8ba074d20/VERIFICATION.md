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

# Verification notes

The mathematical proof is given in `RESULT.md`. Reproduce the finite checks by running `python verify_single_peaked.py` with an ordinary Python 3 standard-library runtime. On the checked implementation it printed `SINGLE_PEAKED_NESTED_SHATTERING_AND_ONLINE_PASS 132154 fixed_peak_utility_cases 4094`. It checks all supports up to the first impossible size for each of eight finite axes, the strong-subcube property, the exact coefficients and concept count, and the adaptive extreme-pair tree through twelve alternatives. The second test directly verifies explicit common-peak real utility value arrays for 4,094 label vectors and their monotonic inequalities. These are finite cross-checks only; the all-size results depend on the constructions and proofs in `RESULT.md`.

A source-level comparison read Zhan's 2019 rhombus-tiling construction, Zhan's 2022 sign-representation manuscript, Basu–Echenique's 2020 example in §2.2, Karpov's 2023 single-peaked profile enumerations, and related query-elicitation and alternative permutation-shattering literature. The 2020 finite-VC example was checked against its original continuous utility definition. No external independent audit has been performed.
