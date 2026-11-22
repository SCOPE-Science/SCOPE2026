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

# Verification details

The exact finite-extension verifier is `verify.py`, which uses only the Python standard library. Run `python verify.py` in the same directory as the supporting files. The independently recorded output appears in `verification_output.txt` and ends with `VERIFICATION_OK`.

The verifier enumerates every possible partial-order relation compatible with the fixed linear extension and the named antichain, and checks strict transitivity directly, for all insertion patterns with zero through five named parameters. It compares the counts of comparable and incomparable ordered pairs against the explicit placement formulas, then tests their exact sums against the closed forms through 40 parameters. The proof in `RESULT.md` establishes the all-size result; no finite verification extrapolation is used as an infinite proof.

The computation does not independently establish historical priority. Independent mathematical audit has not been performed.
