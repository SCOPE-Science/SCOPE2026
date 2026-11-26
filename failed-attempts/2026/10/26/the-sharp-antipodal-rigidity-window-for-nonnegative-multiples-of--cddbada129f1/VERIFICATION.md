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

I reconstructed Φ70 as Φ35(−X), propagated the linear functional on powers using its scalar characteristic recurrence, and confirmed the sixteen positive entries at 19..34, all other entries through 53 zero, and the entry at 54 equal to −2. After shifting off the smallest occupied exponent, positivity eliminates exactly the middle block. Reduction modulo Φ70 identifies X^35 with −1, and the two remaining block polynomials have degree at most 18<24, so are equal. This argument works over R and does not assume integer coefficients or infer real divisibility from a single complex root. The 19 antipodal generators have disjoint supports and give the claimed simplicial cone; the converse follows from the binomial and degree bound. Independently convolving the stated quotient with Φ70 gives the exact 16-term W. Its degree is 54 and its coefficients in degrees 0 and 35 differ, precluding binomial divisibility. Replay: /workspace/replays/recheck_frozen.py, cyclotomic().

## originality

FAIL

The same-day Resultary theorem for nonpolygonal minimal vanishing subsets at order 2pq already supplies the sharp boundary, and its additive kernel gives a short conformal reduction that extends the boundary to the claimed real cone. The exact W is also one of that theorem’s classified checkerboards. The distinct indexed theorem thus covers the Finding, despite different wording and coefficient scope. This finding of coverage does not establish posting order or dependency on the common date.

## value

FAIL

The first failure of antipodal rigidity and the supporting cone are natural structural questions. Here the exact invariant follows from the indexed family theorem and its signed-kernel description, and W is one of its checkerboards. The frozen separating certificate is a short alternative verification, but it does not establish any additional mathematical claim beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
