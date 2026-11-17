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

# Verification and reproducibility

The proof is the symbolic case analysis in `RESULT.md`; the following finite experiments are reproducibility checks rather than replacements for it.

Run `python3 verify_labelled.py`: for \(44\) graph parameter pairs with \(r\ge1\), \(0\le u\le7\), \(2r+u\le15\), it iterates through \(261804\) labelled configurations, calculates neighbors directly, compares fixed states and true primitive two-cycle counts with the theorem, and checks the universal return-map identities. Its captured expected output is `verify_labelled.out`.

Run `python3 verify_profiles.py`: a separate implementation enumerates \(288\) weighted pair-type populations \((00,11,01/10)\) with singleton-one counts, using a local pair-neighborhood formula. It compares fixed and period-at-most-two weighted totals against the theorem, and verifies that the total population weights equal the number of labelled states. Its captured expected output is `verify_profiles.out`.

Both programs ran successfully; the displayed output files were captured from executed code. They require only Python's standard library. They cannot rule out an analytic error outside the checked domains; the all-size justification is the elementary transition classification in the proof.
