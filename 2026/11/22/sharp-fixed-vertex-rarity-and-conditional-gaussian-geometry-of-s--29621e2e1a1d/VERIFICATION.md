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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3.9 or later. The checker has no nonstandard dependencies. It enumerates signed involutions of all binary cubes of dimensions one through six, applies each group element to every cube vertex, and compares the resulting B-type and D-type totals, nonempty fixed-point counts and exact positive fixed-point spectra against the formulas. It then uses the integer recurrence \(A_n(t)=tA_{n-1}(t)+2(n-1)A_{n-2}(t)\) to check the proposed asymptotic constant for increasing sizes through one thousand.

Expected final line: `HYPERCUBE_FIXED_INVOLUTIONS_CHECKS_PASSED`.

In dimension six the direct enumeration returns 1384 B-type involutions, 752 D-type involutions and 331 vertex-fixing involutions, with spectrum \(8\mapsto120\), \(16\mapsto180\), \(32\mapsto30\), \(64\mapsto1\). The finite enumeration is not an exhaustive verification of the infinite asymptotic; the proof in RESULT.md supplies the analytic argument. The denominator asymptotics rely on the standard uniform local Fourier estimate, explained there, and are limited to fixed positive parameters and the stated parity correction.
