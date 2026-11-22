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

# Reproducibility and verification

Execute `python3 verify_kmp.py` and `python3 verify_forms.py` from the extracted directory. Both use only the Python standard library and assert all expected results directly; success prints a PASS line and exit status zero. No randomization, network access or external certificate is needed.

The first verification constructs the standard longest-prefix-suffix DFA, breadth-first enumerates every distinct transformation, and checks idempotent membership, transformation rank and total monoid size for all \(100\) parameter pairs with \(1\le r,s\le10\).

The second verification uses an independently programmed run-state transition system, enumerates its monoid, and compares actual idempotent maps against the exhaustive analytic catalogue of allowable killed sets and fixed output states. It checks exact set equality for all parameter pairs, including each unit-length-run boundary case.

All tests completed successfully. They are exhaustive only over the stated finite parameter domain; the all-order theorem is supported by the case analysis in `RESULT.md`. Earlier research's total-size formula is treated as a control, not as a newly proved size theorem. No independent mathematical audit is included.
