---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In a binary palindrome the number of runs is odd. For a four-run factor the cut must be at a run boundary (internal cuts give one even-run part) and must split 1+3 or 3+1 runs; this gives precisely the two matched-endpoint conditions and the one possible double count. The two 01 rectangles intersect in the rectangle of componentwise minima, and 10, 010, 101 and unary factors give the other terms of (1). In case I the transfer d to a strictly improves the count and the quadratic bound at d=1 follows from the squared-sum inequality; II is a product bound and IV is the reversal/complement of I. In III the loss from the balanced triple bound is exactly the sum of the balancing loss and (a-1)(d-1), so the asserted equality conditions are necessary and sufficient. The construction with a=1 and the largest balanced part as a+d+2 is feasible already at n=8. The three-run count is the balanced-triple product sum with total n+1, with separate one- and two-letter checks. An independent direct enumeration replay (positive compositions of n into 1 to min(n,4) parts, fix first bit 0, collect distinct substrings with a palindromic prefix and suffix for some cut, including empty) checked 2516 hosts through n=16: exactly-four maxima 8,12,16,21 at n=4..7, formula and full classifier at n=8..16, and the at-most-four maximum throughout. Frozen RESULT.md lines 26–74 and verify.py are replay references; the supplied script was inspected, and finite counts do not prove the infinite optimization.

## originality

PASS

Prior work states the unrestricted conjecture and suggests extremizing words; neither the bounded-run theorem as a whole nor the exact four-run classification was found covered. The identical indexed record is not a second result.

## value

PASS

A natural run-complexity slice of a stated extremal conjecture. Four runs are the first case in which a factor may fail to be a palindrome pair; the exact deficit, small-length exceptions and complete maximizer classification explain what changes at that boundary. This does not settle the unrestricted conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
