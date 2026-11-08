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

Run `python verify.py` with Python 3 and no additional dependencies. The executable independently constructs complement adjacencies for every path and cycle of each order \(5\le n\le12\). It exhaustively tests the literal sequential color-change rule on all \(16{,}320\) initial subsets across \(16\) profiles. It then compares the entire count-by-blue-set-size polynomial against the formulas, identifies every inclusion-minimal zero-forcing set, and independently tests the witness-center condition for all three-white subsets.

The run output terminates in:

`VERIFY_OK profiles 16 literal_subsets 16320 full_zero_forcing_polynomial=PASS minimum_set_classification=PASS well_forcedness=PASS exceptional_six_cycle=PASS`

These are finite corroborating checks. The all-order theorem, the exceptional six-cycle multiplicity, and well-forcedness are established by the unrestricted counting and extension arguments in RESULT.md. Independent validation has not been performed.
