# Review of exact dyadic pair correlations of the Baum–Sweet support

## Correctness (PASS)

The claim is an all-parameter theorem for non-cyclic pairs at exactly power-of-two shifts inside dyadic prefixes. The support language is \(1(1\mid00)^*\), and the \(r\)-bit suffix language has exactly \(F_{r+1}\) words. The proof partitions high quotients before and after addition by one. Every non-all-ones quotient has incompatible adjacent zero-run parity requirements; all-ones quotients require an even number of trailing ones. This yields the unique complete paired-index set and the cutoff \(2t+r<m\), including the \(r=0\) and initial-index cases. Independent direct all-pair enumeration through \(m=15\) and digit-carry dynamic programming through \(m=60\) passed. Those finite checks are not the proof of unbounded quantifiers.

## Originality (PASS, qualified)

The closest fully inspected research records are [*Exact dyadic gap law for the Baum–Sweet support*](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-gap-law-for-the-baum-sweet-support--98bde352d9b4) and [*The complete return-gap law for the Baum–Sweet sequence*](https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-complete-return-gap-law-for-the-baum-sweet-sequence--34910b02e3eb). Both count gaps between consecutive support indices and do not determine arbitrary pairs at distance \(2^r\) by their published statements. In particular no successive gap at any power of two greater than two exists, although the present counts at those powers are positive. OEIS A060142 gives an equivalent support definition; the accessible Mérai–Winterhof and Adamczewski–Rivoal texts concern pseudorandomness measures and generating functions rather than this exact incidence classification. Historical priority over unindexed work, and the content of the unavailable original 1976 paper, cannot be guaranteed.

## Mathematical value (PASS)

The exact two-point family is a natural, mathematically motivated correlation invariant for sparse automatic supports and is strictly different from a gap multiset. Its full starting-position classification and exact \(F_{r+1}\lfloor(m-r+1)/2\rfloor\) count capture how binary carry can preserve two support conditions. This supplies a sharp structural benchmark across every dyadic scale rather than a finite census or an elementary rewrite of a pre-existing pair formula.

## Limits and reproducibility

The result does not cover non-power-of-two shifts or general probabilistic autocorrelations. Run `python3 checks/direct_check.py` and `python3 checks/carry_automaton.py` from the package root; no external packages are required. Both have been executed. The proof, not finite checking, supports the universal conclusion.

Self-review: passed. Independent audit: not yet performed.
