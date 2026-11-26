---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The three-gap catalogue is exhaustive because the codes for three consecutive gaps have length at most 10, and all factors of length up to 16 are covered by the four occurring μ⁴ block pairs. For the transformed checker the single-block length is 8(M+2), already greater than 3M+5; coverage needs this single-block bound, not just the pair length. At N=2M+3 the one-, two- and three-b counts are 3, 3M+3, 0, and at N+1 they are 2, 3M+6, 2; each exterior split counted is realizable by catalogue flanks. For N+t a right-special word must have trailing run M or M+1. The single-b endpoint candidate would require repeated gap 2 for one extension; at the three-b endpoint the only minimal pairs (0,1),(1,0) cannot be followed by next gap 0. In the two-b case the flanking triples allow exactly (internal gap, terminal excess)=(0,1),(1,0),(2,0), and the middle choice loses one extension at t=M+1. For palindromes between N+1 and 3M+4 only two b's are possible, with integral equal exterior length (M+1+t−g)/2 for g∈{0,1,2}; the only potential g=1 case at 3M+4 fails parity, and at 3M+5 it needs both flank gaps positive, which is forbidden. Four b's at 3M+5 would require (0,1,0), absent. This gives all adjacent sums and the plateau, including M=1. Reversal closure follows also by reversing enclosing complete gap strings: μ^(2j)(0) are palindromic prefixes, and recurrence lets each factor be enclosed by b's. Nonnegativity and the Brlek–Reutenauer identity then yield the bound. Supplied outputs report finite exact tests, not an all-M proof; scripts were inspected, not run.

## originality

FAIL

The main finding as frozen is covered in the current catalogue by a distinct stronger same-family record, which proves the larger complete initial plateau and gives exact factor-context and palindrome rules implying the requested profiles. Kim–Kwon already has the initial value. This is a content-coverage verdict, not a finding that the November 8 catalogue entry predates the November 2 entry or that the frozen proof is incorrect.

## value

FAIL

A growing exact initial deficit interval is intrinsically useful, but the submitted interval and lower bound add no quantitative information beyond the stronger same-family catalogue result. The remaining explicit right-special shorthand is a direct specialization of the complete context criterion; no independently useful uncovered theorem survives as a bounded repair of this finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
