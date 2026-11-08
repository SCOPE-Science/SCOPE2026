# Scientific review: Exact tortoise-complexity spectra for two-run periodic binary words

## Correctness: PASS

The first iterate is analyzed by the unique zero-gap decomposition of a binary word. The tortoise map preserves the number of ones, fixes every trailing gap of the factor image, and replaces the two initial zero gaps by their sum. For factors of \((0^a1^b)^\omega\) with \(b\ge2\), equality of images from different factors forces the initial gaps to be \((a,0)\) and \((0,a)\). Their one collision pair exists at exactly one length in each interval: \(2\le n\le a+1\) for the one-one pair, and \(a+2\le n\le a+b\) for the multi-one pair. There are no later equal images. This agrees with the independently established ordinary factor-complexity formula \(\min(n,a)+\min(n,b)\).

For \(b=1\), each cyclic phase is described by its initial-zero count \(d\in\{0,\ldots,a\}\). The number of ones is either \(q\) or \(q+1\) when \(n=q(a+1)+r\). All factors with at most \(k\) ones have sorted images; factors with \(k+1\) ones have distinct initial-zero counts \(d+ka\); when all factors have more than \(k\) ones, all \(a+1\) phases remain distinct. The proof covers all integer parameters, including \(a=1\), \(k=1\), exact multiples of the period and the sharp recovery boundary. The standalone checker implements deletion and zero-gap recurrence independently, checks all stated formulas in 15,810 finite parameter-length instances, and passes. These tests supplement rather than replace the proof.

## Originality: PASS (provisional priority)

Campbell–Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first public 2026-04-28, revised 2026-10-05), defines the complexity and proves a general comparison with ordinary complexity for bounded-gap sequences; its explicit exact calculations concern paperfolding and Thue–Morse words. The primary full text of the initial preprint and the available revised HTML introduction were inspected. Neither supplies the exact parameterized two-run one-iterate collision law, the singleton-run all-iterate formula, or its sharp recovery threshold. The general bounded-gap comparison alone does not imply these values. Defant–Kravitz, *Stack-sorting for words*, arXiv:1809.09158, introduces the sorting operator, but the available abstract is not an exact factor-language spectrum for this family. The latter work was not fully read, which remains a specific bibliographic risk. Semantic record comparisons found no direct coverage: records on group complexity of the same periodic words and on tortoise complexity of distinct automatic/aperiodic words do not imply the claimed operator-image counts. Unpublished or unindexed equivalent calculations cannot be excluded by search.

## Value: PASS

Iterated sorting on finite factors is a motivated recent complexity invariant. The result gives a complete first-iterate spectrum across an infinite two-parameter periodic family, including a unique collision at **every** nontrivial short length, rather than merely an eventual bounded deficit. The singleton-run subfamily has a complete, exact all-iteration hierarchy with repeated global collapses and an optimally determined recovery boundary. This sharp phase-dependent behavior is not apparent from the general published bounds and supplies a tractable reference family for further studies of tortoise-factor complexity. The scope intentionally stops short of all iterations for \(b\ge2\).

## Limits and closest sources

Primary source: https://arxiv.org/html/2604.25811v1; revised version https://arxiv.org/html/2604.25811v2. Foundational source: https://arxiv.org/abs/1809.09158. No independent external mathematical audit has been performed. An equivalent formula in a complete version of the foundational paper, or in unindexed work, is a residual priority risk. The finite checker cannot establish any infinite-parameter statement on its own.

Self-review: passed. Independent audit: not yet performed.
