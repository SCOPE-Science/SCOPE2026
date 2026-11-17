---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The exact claim covers every k>=0 at n=3·4^k, distinct linear Thue–Morse factors, and palindrome pairs with an empty part allowed. For φ=μ² with palindromic blocks B0=0110, B1=1001, every cyclic φ-image has a reversal-invariant six-factor histogram because each six-factor uses at most three source letters and cyclic binary 3-grams obey reversal balance. A factor of length 4m with a seam between unequal boundary source letters acquires one of six exceptional four-blocks. Exhaustive local cases for six-factor reversal imbalance (six anomalous blocks × 16 nearby binary contexts, plus short circular cases) give a strictly positive obstruction, so such a word cannot be a palindrome pair. Equal-boundary factors are rotations of a φ-image; unique cyclic block decoding and reflection symmetry descend the palindrome-pair property. Base length three has exactly two rotation classes (010 and 101), and actual squares in Thue–Morse ensure every rotation survives at each induction step. Primitivity and disjointness descend as well, yielding exactly 2n. Independent local checks reproduced positive seam asymmetry minima and all-good symmetry; inspected separate factor-counter independently corroborates k=0..3 only, not the infinite proof.

## originality

PASS

Borchert–Rampersad Proposition 11 gives the **same two rotation classes as a lower bound** at exactly n=3·4^k and asks for exact palindrome-pair complexity; the inspected original proposition does not provide an upper bound or rule out additional partial conjugacy classes. The submitted local reversal-spectrum seam obstruction and cyclic desubstitution prove that missing upper bound, producing exact equality and full factor classification. Bell–Shallit Lie complexity counts complete conjugacy classes, but not all partial palindrome-pair factors; no inspected stronger result implies the exclusion lemma. Originality is best-of-knowledge and limited to the exact equality and upper-bound method, not the existing lower-bound construction.

## value

PASS

Closing a named published lower bound for infinitely many naturally morphic lengths supplies a precise word-combinatorics result rather than an arbitrary fixed-length table. The complete two-orbit classification and reusable local seam obstruction explain why no extra palindrome-pair factors appear. The general all-length palindrome-pair complexity problem remains open outside this tetradic subsequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
