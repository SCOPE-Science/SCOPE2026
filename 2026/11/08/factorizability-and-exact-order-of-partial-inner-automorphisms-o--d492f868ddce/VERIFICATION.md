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
# Verification

The symbolic proof in `RESULT.md` applies to every finite-dimensional vector space over every field. The finite checks below corroborate rather than replace it.

Run `python verify.py` and `python verify_full.py` in one directory containing both scripts. `verify.py` enumerates every matrix for four finite configurations and compares actual two-sided fixed domains, inclusion, intersection strata and idempotents with independent formulas. `verify_full.py` enumerates all generating pairs over both two-dimensional prime fields (\(256\) and \(6561\) pairs) and checks that each partial map is the restriction of a conjugation by an invertible matrix. It additionally constructs every nonzero proper domain and every conjugation restriction in \(M_3(\mathbb F_2)\), verifies pointwise stabilizer sizes independently of the formula, and obtains \(15506\) distinct partial maps.

The exact captured output is `verification_output.txt`; this was regenerated from the provided scripts. Calculated larger orders are arithmetic consequences of the proved formula, not exhaustive direct enumerations. The finite checker is limited to prime fields \(\mathbb F_2,\mathbb F_3\) and dimensions at most three. No independent mathematical audit has been performed.
