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

# Reproduction and boundary checks

Run `python3 VERIFY.py` using the supplied standalone Python 3 script. Expected result: `PASS: 87475 exact assertions`. It uses Python's exact `fractions.Fraction` and no external packages. It independently enumerates all feasible integer degree assignments for 42 mean degrees and tests many rational susceptibility ratios, including both sides of every transition and the exact tie point. It also checks the matrix determinant, eigenvalue-by-trace identity, and the exact example.

The proof in `RESULT.md` is independent of this finite checker. Critical proof steps are: uniform stub-pairing gives class-size-biased neighbor distribution; the two-type next-generation matrix has rank one; swapping higher degree into the lower-susceptibility class strictly lowers the objective; integer forward differences have strictly ordered zero crossings, proving all exact minimizers and all endpoint cases. Uniformity of the empirical finite-size epidemic was not simulated or asserted. Historical originality has not been independently certified.
