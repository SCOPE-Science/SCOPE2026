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

# Reproducible verification

The standalone Python 3 file `CHECK.py` uses only the standard library. Run `python3 CHECK.py` from the directory containing this document and the file. Verified result during preparation:

`VERIFY_OK exact_rational_identities=35 root_and_multiplier_cases=7 basin_cases=5 critical_clocks=2 total_checks=48`

Exact rational tests verify the orbit identity, the derivative identity and the double-root fold relation for multiple admissible and extended algebraic parameters. Numerical tests check representative root counts, periodic orbit amplitudes and multiplier signs, a five-state basin partition, and the two critical clocks. The proof in RESULT.md supplies the all-parameter conclusions; these finite checks cannot prove exhaustive global claims or independent mathematical certification.
