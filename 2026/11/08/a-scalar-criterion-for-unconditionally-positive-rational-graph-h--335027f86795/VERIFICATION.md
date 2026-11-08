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

# Exact checks and limits

The standalone `artifacts/verify_exact.py` uses only Python's standard-library `fractions.Fraction` and direct Gauss–Jordan elimination; it contains no external data dependency. It checks the rational Padé matrix step against the independently coded spectral projector entry formula, checks strict positivity and row sums, and checks the four-vertex path counterexample.

Executed command: `python artifacts/verify_exact.py` (after extracting the file).

Observed output: `PASS cases=45 exact_entries=1630 P4_h20_entry01=-643260/32303047`.

The 45 combinations comprise nine graph-part configurations and five exact rational positive steps. This is a finite spot-check only. The general equivalence and strict Gauss–Legendre conclusion follow from the analytical proof in `RESULT.md`, not from enumeration or solver success. No independent external audit was conducted.
