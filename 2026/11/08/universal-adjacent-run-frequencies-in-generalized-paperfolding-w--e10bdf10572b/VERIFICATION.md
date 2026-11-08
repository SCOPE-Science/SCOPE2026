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

The result follows from a uniform local-sign reduction at multiples of eight and an exact \(32\)-case residue enumeration for each of the four normalized triples of early instructions. The executable file `verify.py` reproduces this complete finite step and also checks the valuation model against the paperfolding recursion on \(254\) finite instruction strings.

Executed with Python 3, `python3 verify.py` returned `VERIFY_OK symbolic_cases=256 fold_cases=254 prefix_cases=8` and the rows `0 3 1`, `3 2 3`, `1 3 0`. The eight direct long-prefix checks are supplemental: they do not independently establish the all-instruction limiting law. The proof's analytic step is the conditional unbiasedness of the unique multiple-of-eight sign in any eight-position block, established from the 2-adic valuation classes in RESULT.md.

The finite tests make no assertion about frequencies of run-length blocks longer than two. Independent external verification has not been performed.
