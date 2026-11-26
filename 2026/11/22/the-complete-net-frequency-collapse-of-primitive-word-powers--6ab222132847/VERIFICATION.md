---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under the stated convention a repeated occurrence is net iff both available one-letter extensions are unique, treating missing boundary extensions as unique. If p is the primitive-root length, equality of two cyclic rotations would give a proper cyclic period dividing p. Hence long factors can occur at only one phase. All occurring strings of length at most p repeat at starts r and r+p for some r<p, within the first 3p positions; this excludes net occurrences of lengths below p. For length at least p an occurrence class at positive phase has at least two identical left extensions whenever repeated. At phase zero with at least three occurrences, all positive starts have repeated left extensions, and the zero start's right extension repeats at p. With just starts 0 and p, the positive start is the only possible source of its left extension. The zero start's right extension then occurs only once precisely when the second occurrence runs to the right boundary; otherwise both right extensions repeat. This gives exactly the two occurrences of v^(e-1), including p=1. Independently, /workspace/audit-replay/2.py used forward and reverse longest common prefixes of suffix pairs to derive net intervals from equal longest-repeat lengths on both sides. Output 2.txt records 9332 primitive-power cases at exponents 3,4,5,7 (binary roots through length 9, ternary through 6, four-symbol through 4) and the four asserted square intervals. The tests corroborate rather than replace the proof.

## originality

PASS

Best-of-knowledge pass on the uniform primitive-power law specifying both the unique factor with positive net frequency and both exact positions, together with the exponent-two boundary. Generic net-frequency algorithms and results for restricted morphic families do not furnish that closed classification in the compared statements. External full-text access was limited, in particular for the most plausible adjacent epistandard work.

## value

PASS

Periodic powers are a natural canonical test family for context-sensitive repeats. The result removes every other possible occurrence and gives factor and positions uniformly in the period, alphabet and exponent, which is stronger than a bound or a finite catalog. The square witness distinguishes a genuine sharp structural threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
