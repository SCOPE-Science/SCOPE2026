---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For n<=k the length-n count identifies the word. Otherwise, the count of a (k-1)-factor minus its left-extended k-factor counts picks out the unique prefix, with the empty prefix used at k=1; reversal fixes the suffix. A length j<=k of the same parity as n has one centered start. Reversal pairs every other occurrence of a palindromic factor at this length and fixes the center, so the unique odd-multiplicity palindromic j-factor is the central word. Take the largest such j, allowing j=0; for n<=3k the central start is at most k, since n<=3k-1 when n has parity opposite k. With the (k-1)-prefix and its mirror already known, the only possible gap is one distinct mirrored pair, identifiable by subtracting known letters from the singleton counts. The argument covers overlaps and k=1; it uses ordinary palindromicity of both candidate words, not palindromicity up to equivalence. In each boundary witness every marker is at least k-1 positions from both ends and the two markers are at least k apart, so each one-marker word of length j<=k occurs twice at its specified offset and the all-zero count is 3k+2-3j. The witnesses have distinct first-marker positions and are ordinary palindromes, giving sharpness over any alphabet with two letters. A separate enumeration generated palindromes from their first halves and compared full factor profiles in 82 finite (alphabet size, order, length) slices (binary k<=5, ternary k<=3, four-letter k<=2), and checked the supplied witnesses for k<=20; the source scripts were inspected but not executed. The universal conclusion rests on the symbolic proof.

## originality

PASS

The generic k-Abelian framework and the prior order-three case are covered and not credited as new. The all-order sharp threshold for reversal-fixed words, with the parity-based constructive argument, is not supplied by the inspected equivalence, shortest-collision or rich/poor results. This is a bounded assessment, with explicitly unresolved access to portions of the related literature.

## value

PASS

The occurrence profile is a standard string invariant and reflection symmetry is a natural source restriction. The uniform theorem measures exactly how much symmetry improves the first loss of information, and the parity-of-center decoder provides a structural explanation rather than an order-three recomputation. The binary witness hits the bound at every order. The claim does not solve the unrestricted reconstruction problem or classify all fibers above the threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
