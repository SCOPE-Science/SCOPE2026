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

# Verification of the two-step length-three palindromic sphere theorem

## How to reproduce
Execute `python3 checker.py` under Python 3 without third-party dependencies. Its recorded output is `checker_output.txt`. The code directly forms every duplication history; it also computes modular-difference signatures independently of the formula in the proof and compares them to all displacement cases.

## Checks actually performed
The test exhaustively determines the exact-two sphere maximum among all \(29,511\) ternary words of lengths \(3\) through \(9\), checks the binary maxima at these lengths without claiming a binary theorem, and inspects exact history fibers on ternary periodic sources at \(47\) lengths up to \(128\). It makes \(14,190\) independent comparisons between direct signatures and the finite symbolic displacement table. The longest tested periodic source has \(8,628\) ordered histories and \(7,626\) different descendants, with all duplicate fibers of size two. Exact integer calculations are used.

## Mathematical proof boundary
The uniform derivation does not rely on extrapolation. The general upper bound follows from disjoint commuting original blocks, and the ternary attainment proof follows from exhaustive *symbolic* cases for relative operation starts and injectivity of the resulting signatures except for commuting histories. Computer enumeration is a finite cross-check, not a complete computer proof over unbounded \(n\).

## Validation boundary
This is a self-reviewed result, not an independent mathematical or historical certification. The existing result for odd block lengths with \(q\ge n\) does not establish the fixed-three-letter theorem for \(n\ge4\); the prior universal upper bound is acknowledged. Other odd block lengths, binary inputs and optimal code sizes are not determined here.
