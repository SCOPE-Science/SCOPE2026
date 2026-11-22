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

The standalone `verify.py` reconstructs an exact binary-section finite automaton from the coefficientwise identity \(B(x)=(1-x)^{-2}B(x^2)\), rather than depending on a stored transition table. It checks closure of exactly 100 states, validates all 16,384 initial coefficient residues against independent Euler-product arithmetic, verifies 800 matrix annihilation values for the eight histogram recurrences, and verifies 100 further values certifying the stable-suffix bound. Its output is the `VERIFY_OK` line documented in `RESULT.md`.

The global claims use Cayley–Hamilton after exact, finite, dimension-100 certificates, not empirical extrapolation from the sample. The ten-unstable-suffix invariant is what upgrades dyadic-block counts to ordinary natural density and a logarithmic discrepancy bound. The three-square deduction uses Legendre's standard theorem. Independent mathematical audit was not performed.
