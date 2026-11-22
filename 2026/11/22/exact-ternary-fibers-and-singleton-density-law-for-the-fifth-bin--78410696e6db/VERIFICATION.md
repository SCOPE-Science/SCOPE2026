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

For exact finite checks, run `python3 verify.py` using Python 3 with the standard library. The program calculates the full least-period fiber histogram of \(\binom n5\) for every modulus \(3^k\), \(1\le k\le10\); verifies each predicted target multiplicity, computes the critical residues using unique Hensel lifts, checks square-root counts through level six, and verifies singleton and maximum formulas in this finite range. On success it prints `PASS: 88572 target congruences checked exhaustively; 265716 integer indices in their full periods`.

The proof for every \(k\) is the polynomial isometry and square-conjugacy argument in RESULT.md, not this finite computation. Exactly one scientific claim is evaluated, with limitations stated there. Self-review is passed; no independent audit or independent validation is claimed.
