# Mathematical review: sharp circular covers of four-letter palindromes

## Correctness — PASS

For \(q\ge2\) the proof classifies every possible proper overlap between two distinct \(abba\) targets. It translates cyclic consecutive target starts into a directed flow on first letters, proving the baseline \(3q^2-\binom q2\) bound and the additional even-\(q\) parity cost. Euler tours of \(K_q\) for odd \(q\), and \(K_q\) minus a perfect matching for even \(q\ge4\), give explicit optimum hosts; \(q=2\) has an independently checked witness. All quantifiers and boundary cases are covered. The included Python script produced `VERIFY_OK` on constructions for \(2\le q\le10\) and exact independent tour optimization for \(q=2,3,4\). The universal proof does not depend on finite enumeration.

## Originality — PASS (qualified)

Actual related-research searches compared ordinary reversal palindromes with their nearest aliases, two-letter overlap transitions, shortest circular superstrings, parity-based Euler tours, tandem squares and reverse-complement palindromes. The indexed tandem-square result gives \(2q(q+1)\) for target \(abab\), not the present \(abba\). The fixed-point-free complement result gives \((5q^2-q)/2\) for the different target \(ab\overline b\overline a\), and the ternary length-five palindrome result addresses length five. The 2013 Orenstein–Shamir full article concerns covering every length-\(k\) word up to reverse complement, not the restricted ordinary-palindrome set. OEIS A330022 already gives the binary length-four linear result \(12\); that instance is expressly credited and is not claimed new. The arbitrary-alphabet parity theorem was not found in actual searches. This is evidence for qualified originality, not proof of global uniqueness. Full manuscripts of the relevant indexed 2026 records could not be inspected, leaving priority risk.

## Mathematical value — PASS

This settles the minimum length of a single cyclic test string covering all ordinary even-four palindrome motifs over *every* alphabet. It is an all-parameter optimal value, with an explicit constructive algorithm and a nontrivial odd-versus-even correction arising from graph parity. The invariant is a natural constrained-motif covering length rather than an arbitrary selected slice; it is pertinent to universal word and sequence-design questions. It does not purport to settle longer palindromes or arbitrary reversal-invariant word families.

## Limits and priority caveat

Full open-access 2013 paper and OEIS entry were materially inspected. The related indexed 2026 descriptions were compared at statement and parameter level but their complete public manuscripts could not be read in this session. Independent review and exhaustive prior-art search have not been performed.

Self-review: passed. Independent audit: not yet performed.
