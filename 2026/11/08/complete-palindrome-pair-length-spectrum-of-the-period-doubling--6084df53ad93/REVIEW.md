# Independent mathematical audit

## correctness

PASS

Reconstructed all-length proof. (i) A finite word splits into at most two palindromes iff its reversal is a cyclic conjugate, a published equivalence. (ii) For every j>=1 the substitution δ(1)=10, δ(0)=11 has δ^j(a)=U_j π_j(a), common palindrome prefix U_j of length 2^j−1 and a permutation π_j; induction gives U_(j+1)=U_j π_j(1) U_j. This makes δ^j preserve reversal-conjugacy. An arbitrary length m·2^j factor is a rotation of δ^j(v) for an m-factor v: its last r<2^j boundary letters coincide because all images share U_j. All binary words of lengths 1,3,5 are PP (independently exhaustively checked), so universal PP holds at 1,3,5 times 2^j. (iii) The proven period-doubling factor complexity C(1)=2,C(2)=3,C(2m)=2C(m),C(2m−1)=C(m)+C(m−1), combined with the published exact palindromic-periodicity count F(q+r) (2024 Thm14 / 2025 Thm13) gives C−F equal to 2r, 2r−q/2, 2r−q, 2r−3q/2 on four successive dyadic quarter-intervals. Since PP implies palindromic periodicity, universal PP requires C=F and thus only 1,3,5,7 dyadic families. (iv) b=0111010 occurs starting at index 1 and is not conjugate to its reversal. If v contains 1 then δ(v) contains a 0 only in odd positions, so a conjugacy between δ(v) and δ(v^R) must have even offset, descending to a conjugacy of v and v^R. Thus δ^j(b) is a non-PP occurring factor of length 7·2^j. All 7·2^j factors are still palindromic periodicities by C=F. Base n=1,2,3 and dyadic quarter boundaries covered. Independently reconstructed the canonical seven-blob Git tree 5c1b7ad5... and checked finite factor classification through 128, using two nested prefixes; finite enumeration is corroboration, not proof.

## originality

PASS

Best-of-knowledge originality: the exact factorwise palindrome-pair length set of the classical binary period-doubling fixed point is not established by the inspected prior theorems. The 2024/2025 Fici–Shallit–Simpson formula is for the strictly larger palindromic-periodicity language and yields only a necessary four-family condition; it leaves the 7·2^j ambiguity and does not assert the palindrome-pair positive lifts at 3·2^j,5·2^j. An explicit factor 0111010 and substitution descent exclude the fourth family. The 2015 property-PP paper concerns Sturmian, other constructed, and Thue–Morse words, not this sequence. The 2021 prefix PPL invariant, 2026 prior Lie-complexity classification, and OEIS A275202 count different objects/invariants. Search failures alone are not proof of novelty; residual priority risk remains.

## value

PASS

Gives a complete, naturally motivated classification of the factorwise two-palindrome (property-PP) length spectrum for a standard aperiodic automatic word, rather than a finite threshold, code refactor, arbitrary slice or restatement of known factor counts. The exact separation between the symmetric (two-palindrome) factor condition and the strictly broader palindromic-periodicity condition occurs at infinitely many 7·2^j lengths with explicit morphic witnesses. Three positive dyadic families and one sharp excluded family provide structural information usable in comparisons of palindromic factorization, automatic-sequence invariants and symbolic dynamics. No general theorem beyond the fixed point is claimed or required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
