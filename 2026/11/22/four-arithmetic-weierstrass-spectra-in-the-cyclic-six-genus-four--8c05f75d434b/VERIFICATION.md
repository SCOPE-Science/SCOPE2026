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

# Verification record

The mathematical claim and hypotheses are specified in `RESULT.md`. Its proof reduces Frobenius cycles to the roots of a separable cubic and establishes exact frequencies by inclusion–exclusion and trace of cubic residues in a quadratic field. The proof, not finite sampling, covers every odd prime power congruent to two modulo three.

Run `python3 verify_frobenius.py` and `python3 verify_trace.py` with Python 3 from a directory containing both programs. Both require only the Python standard library. The first computes the actual ten-root Frobenius permutations by polynomial arithmetic for every smooth coefficient pair over prime fields of sizes 5, 11, 17, 23, 29 and 41. It prints `CUBIC_BRANCH_SPECTRA_VERIFIED` after exhaustive comparison with the four formulas. The second checks all cubic-residue trace fibers and irreducible quadratic counts over the same quadratic extension fields and prints `CUBIC_TRACE_DISTRIBUTION_VERIFIED`.

The finite verifiers do not independently certify the theorem over every nonprime finite field, and no external verification or mathematical audit has been conducted. The exact field-independent algebraic argument is given in the proof.
