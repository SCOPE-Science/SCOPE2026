# Self-review

## Correctness — PASS
Prime-by-prime identity nu_p(Q_k)=sum_{j<=floor(log_p k)}(N_{p^j}-1) holds because larger powers divide at most one window term. CRT makes the full sign mean the product of independent local signed means. For odd p each numerator is a sum of an odd number of signs and cannot vanish. For p=2 a complete 2^e-block reduces the local numerator to the cyclic truncated-valuation sum S_e(r). Splitting even/odd residues yields two exact recurrences. The arrays at levels 1 and 2 and induction give S_e(r)=0 only at r=2^(e-1); the same induction establishes nu_2(S_e(r))=nu_2(r)+1 elsewhere in the interior. Thus k+1=3*2^(e-1) exactly characterizes zero. The boundary k=1 has Q_1=1. The supplied stdlib checker passed 34161 direct quotient-residue tests, 1031 independent cyclic sums and 3373 local prime sums; finite tests are not substituted for induction.

## Originality — PASS (qualified)
The 2026 Huang–Yang full text concerns periods of multiplicative-function quotients, not averaged Liouville signs; its valuation count is known antecedent. The published complete value-frequency theorem already implies B_k as an evaluation of its prime-local generating polynomials at -1 for each fixed k: no originality is claimed for that formula, frequency, or the existence of periodicity. However, that theorem does not state a closed all-k zero classification nor the requisite dyadic noncancellation induction. The new quantified claim gives exactly the window lengths where the signed mean vanishes and proves there can be no others. A distinct-prime omega result has a different support criterion. Search results and inspected relevant source texts contain no directly covering exact zero-locus theorem. Residual risk: a prior algebraic analysis of the carry matrices could implicitly provide the same zero locus.

Closest verified comparison: Huang and Yang, arXiv:2611.15379v1, full text, versus the full published `RESULT.md` at https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-value-frequency-law-for-consecutive-arithmetic-progression--8e35eb7b4fbc. The latter is an important stronger general fixed-window theorem; it implies the exact signed mean for any given window, but the new all-window zero criterion is not stated. Nontrivial algebra is supplied rather than claiming the general frequency formula as new. Unindexed equivalent classifications remain possible.

## Mathematical value — PASS
The signed parity of the total number of prime factors is a natural multiplicative arithmetic statistic, and exact balance in an infinite parameter family is a structural question not resolved by a fixed-window frequency table. The theorem gives an unexpected sparse resonance family 2,5,11,23,... and excludes balance for every other window with a uniform 2-adic valuation rigidity lemma. This is meaningful quantitative qualitative structure beyond routine small-window enumeration, though it is not a general mean-value asymptotic.

## Limits and review status
No independent validation or priority certification has been performed. The finite checker is corroborating evidence only; the proof is the dyadic recurrence and valuation induction.

Self-review: passed. Independent audit: not yet performed.
