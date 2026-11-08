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

# Reproducibility and actual verification

The full finding is an algebraic proof, not an extrapolation from finite simulation. Both included scripts were run from the evidence source files and their deterministic stdout captured in adjacent `.out` files. `checks/verify_direct.py` enumerates every integer state with \(0\le x_v<2\deg(v)\) for the wheel of rim sizes three through six. This covers all possible immediate primitive-three states by the proof's firing-count bound. The direct update is applied three times to every candidate state; no firing-phase assumption enters that computation. It checks 649,296 candidate states in total and reports exact chip-mass counts for all primitive-three states in that range.

`checks/verify_transfer.py` independently enumerates rim phase words and local integer chip ranges for rim sizes three through twelve. It checks the full set of positive/negative mass bands, outer and inner endpoints, integer Fibonacci total, and total reciprocity. Sympy constructs the nine-state transfer and support matrices from their defined entries, computes their exact symbolic determinants, and checks the stated factorization and rational partial fraction identity. It checks the upper coefficient recurrence. Finite cases are cross-compared with direct dynamical enumeration at the four overlapping sizes.

Run using Python 3 with Sympy installed: `python3 checks/verify_direct.py`, `python3 checks/verify_transfer.py`, and `python3 checks/verify_crosscheck.py`. Both print a single JSON object with `status` equal to `PASS` on success. The output files contain the captured full JSON results. The symbolic determinants are exact polynomial identities; random numerical tests were not substituted. They and the main mathematical proof, not finite enumeration, supply the all-sizes justification.

The historical priority check is qualified by the unavailable full text of the 1992 Bitar–Goles article. The research reports only self-review, not independent audit or certification.
