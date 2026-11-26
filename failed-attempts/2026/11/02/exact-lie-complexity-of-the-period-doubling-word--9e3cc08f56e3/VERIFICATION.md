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

The all-rotations condition and the four representative families hold for the stated p=μ^ω(0). The recurrence p_(2j)=0, p_(2j+1)=1−p_j rules out 11 and then 0000. At an odd length at least five, two ones give a directed cyclic separation that is odd in one of the two orders, contradicting the common parity of ones in any factor; if there are fewer than two ones, a rotation exposes four consecutive zeros. At length 2m≥4 a qualifying word has a one; rotating so all ones are at odd relative positions yields a unique letterwise preimage. All even rotations of the image occur at even absolute start positions, forced by a one in an odd relative position, so all its preimage rotations occur. Conversely every even rotation of μ(y) for a Lie representative y is the image of a rotation of y and occurs aligned; the following 0 completes the one-position-advanced rotation, giving all odd rotations. A rotation identifying two such aligned images must be even, proving class injectivity. The m=1 step for representatives is justified directly: μ(0)=01 and μ(1)=00 are the two distinct length-two classes. At length three, the five triples with no adjacent ones occur in the prefix, and 101 does not qualify because a rotation has 11; the two classes are [000] and [001]. Iterating gives exactly the four asserted families on the two disjoint support sets. The package's finite coverage claim also holds: a length-n window with n≤2^m lies in at most two m-level images of adjacent letters, and all three possible adjacent pairs occur in μ^4(0). The supplied script was inspected, not executed. Our own bounded replay, python3 /workspace/branches/independent_math_checks.py, independently constructs exact factor languages from parent factors and checks the full representative sets through n=200. This corroborates, but does not replace, the all-length proof.

## originality

FAIL

Earlier-dated October Resultary Findings directly state the identical count, the identical four morphically iterated representatives, and the doubling law for the same word and invariant. Frozen record 4 also establishes the same count and class map; it need not have priority for the decision. The exact coverage includes this record's claimed constructive increment, so there is no distinct surviving claim.

## value

FAIL

The exact Lie classes of a canonical automatic word and the alignment-based structural proof are mathematically useful, but are already covered. The finite coverage bound used to corroborate them is a direct uniform-substitution window argument and is not an independently valuable new claim. No nonroutine remainder justifies a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
