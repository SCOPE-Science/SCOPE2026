# Independent mathematical audit

## correctness

PASS

The greedy universal-subsequence arch criterion is bidirectional: h complete shortest all-symbol arches yield every h-letter subsequence, while choosing each arch endpoint’s new letter and the missing suffix letter constructs an absent (h+1)-word. If |w|_b=k and index k, exactly k arches each use one b, and the only forms are ba or a^(u+1)b, with final all-a suffix. Count baseline C=binom(k,2), plus 1+(k-i+1)u in each positive-orientation i-th arch; extract z^r in (1-z)^(-1)prod_(j=1)^k(1+q/(1-zq^j)) to prove all coefficient formulas. Reversing w maps C to k(k+r)-C and preserves index, giving reciprocity. Low-edge coefficients from selecting positive arches and the last two u-extras follow exactly; independent brute full-subsequence tests matched k=3,r=1; k=4,r=0,1,2; k=5,r=1. Infinite k,r argument is unique factorization.

## originality

PASS

The 2026 primary Fazekas–Huang–Mercaş paper on binary Parikh-matrix subsequence universality gives existential and universal-index thresholds and an approximation scheme for fixed target patterns, not this exact per-C distribution of maximizing words. Adamson et al count/rank universal words by length without joint k+r letter content and scattered ab inversion. Published first-gap spectrum only gives finite fiber index sets through length eight. The coefficient product conditions on a *saturated letter multiplicity*, a genuinely finer enumeration not implied by those statements. Best-of-knowledge priority remains subject to unindexed refinements.

## value

PASS

An exact coefficient-extractable polynomial refining subsequence universality by both content and binary Parikh-pair statistic directly answers a natural distribution question within equivalence classes. Its arch interpretation, reciprocity, edge coefficients and degree cutoffs provide reusable exact data, not merely a relabeling of known univariate universal-word counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
