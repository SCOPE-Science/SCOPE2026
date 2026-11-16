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

# Verification of finite calculations and scope

Run `python checker.py` using Python 3 standard library; no external packages or data files are required. The program independently lists each order ideal of the two-row product poset, applies the full exact-integer Walsh--Hadamard transform, and compares every coefficient histogram with an independently constructed two-prefix signed dynamic program. It checks the congruence-dependent Fourier-zero criterion, sharp least surviving multiplier, exact convolution norm and total multiplicity at all row lengths through eight. The direct comparisons cover exactly 87,380 frequencies. The signed dynamic program checks every frequency through length seventeen without constructing the full truth table.

This arithmetic replay is a finite check only. The infinite-length classification follows from the parity argument and explicit alternating prefixes, not extrapolation. The limiting non-Gaussian law follows from the conditional characteristic-function derivation, random-walk invariance principle, fourth-moment control, and harmonic-oscillator differential equation displayed in `RESULT.md`. Its nullity-density corollary uses the no-atom property of that limit. The Brownian law has not been independently verified by an external auditor.
