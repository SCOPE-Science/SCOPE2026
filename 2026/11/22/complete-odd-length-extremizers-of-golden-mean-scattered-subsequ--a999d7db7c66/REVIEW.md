# Scientific review: odd-length golden-mean subsequence master classification

## Correctness — PASS

The claim is the complete optimizer **list and count** at odd target lengths, not merely the already-known minimum-length equation. The lower bound uses the two admissible targets \(0^{2m+1}\) and \((10)^m1\), forcing \(2m+1\) zeros and \(m+1\) ones in every shortest host. For each single-one target \(0^i1 0^{2m-i}\), a host one of zero-rank \(c\) works exactly when \(c\in\{i,i+1\}\). Covering all \(2m+1\) required ranks by \(m+1\) two-element intervals rules out duplicated ranks, forces the listed three endpoint cases, and yields \(m+2\) candidates. Every listed word embeds all legal targets by splitting them into admissible two-letter blocks, plus one letter. The \(m=0\) boundary is handled separately. Thus the proof is infinite, not empirical extrapolation.

The included independent direct-subsequence checker enumerated all \(36{,}940\) words with the forced letter counts through target length \(12\). It verified equivalence of full coverage and single-one coverage within this class, and checked the constructed words through target length \(20\). Computational evidence is corroborative and is not substituted for the four proof steps.

## Originality — PASS (with limitations)

The preceding exact-length statement for run-capped binary target families already supplies the sharp length and even-length uniqueness, so neither is claimed as new here. It explicitly gives no all-optimizer classification for odd lengths. Its length and divisible-case uniqueness do **not logically imply** the exact count \(m+2\), the listed odd extremizers, or the forced absence of `11` in unrestricted shortest hosts. The closest published primary texts address, respectively, full-alphabet \(k\)-universality in regular languages (Adamson et al., arXiv:2311.10658) and shortest common supersequence complexity for different restricted inputs (Lagoutte–Tavenas, arXiv:1309.0422). The latter contains a different three-letter example and does not cover the present family. Related published results on golden-mean universal **factor cycles** use contiguous windows, not scattered subsequences. Exact and alias searches did not reveal an equivalent odd-length extremizer classification.

Residual risk: a later or unindexed note could contain the same optimizer count; the absence of a result from search indices is not a novelty proof. The earlier length theorem and related sources remain scientifically credited rather than reconstructed or re-assessed.

## Value — PASS

The complete Fibonacci-language target family contains \(F_{k+2}\) words at length \(k\); its shortest-subsequence masters are a natural extremal supersequence problem. The pre-existing optimal-length formula left the nondivisible-length optimizer structure unresolved. Here the exact odd-length count is only linear, the entire optimizer list is explicit, and every optimum unexpectedly satisfies the source run constraint without being required to do so. The one-marker rank-cover criterion reduces an exponential-size target coverage requirement to a linear-size test **at optimal length**. This is a complete natural equality-case classification rather than an arbitrary numerical slice, although it does not claim broader downstream results.

## Scientific limitations and priority risk

The claim is limited to odd binary target lengths, contiguous-`11` avoidance for targets, and scattered-subsequence coverage; even-length uniqueness and all-length optimal lengths are prior knowledge. Searches and primary-text inspections reduce but cannot eliminate historical-priority risk. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
