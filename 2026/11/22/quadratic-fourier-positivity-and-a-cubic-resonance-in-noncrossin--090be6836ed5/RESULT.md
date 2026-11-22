# Quadratic Fourier positivity and a cubic resonance in noncrossing-partition arcs

## Finding

For every integer \(n\geq5\), let \(E_n=\{(i,j):1\leq i<j\leq n\}\), and identify a noncrossing set partition of \([n]\) with the binary incidence vector of its *successor arcs*: consecutive entries of each block, in increasing order, are joined by an arc. Let \(f_n:\mathbb F_2^{E_n}\to\{0,1\}\) be the indicator of these distinct arc vectors, and define unnormalized convolution \(T_nh=f_n*h\). Every Walsh multiplier \(\widehat f_n(S)\), where \(S\subseteq E_n\) has at most two arcs, is **strictly positive**.

The first cubic obstruction is explicit at six labels: precisely **25** of the \(\binom{15}{3}=455\) cubic multipliers vanish. Across all \(2^{15}=32768\) frequencies, the six-label convolution has
\[
\operatorname{rank}(T_6)=23684,\qquad \operatorname{nullity}(T_6)=9084.
\]
Every six-label multiplier is divisible by \(4\), and the smallest nonzero absolute multiplier is exactly \(4\). In particular the operator preserves all degree-at-most-two Walsh modes although it loses higher-frequency information.

## Assumptions and scope

A partition \(\pi\) of the linearly ordered set \([n]\) is *noncrossing* if no distinct blocks contain respectively \(a<c\) and \(b<d\) with \(a<b<c<d\). The successor arcs of a block \(b_1<\dots<b_r\) are exactly \((b_1,b_2),\ldots,(b_{r-1},b_r)\). These arcs uniquely determine the partition. Two arcs cross when their four endpoints strictly interleave. Throughout \(C_k=\frac1{k+1}\binom{2k}{k}\) denotes the \(k\)-th Catalan number and \(\widehat f_n(S)=\sum_{\pi\in\mathrm{NC}_n}(-1)^{|S\cap A(\pi)|}\), with no probability normalization. The polynomial degree of a Walsh mode is \(|S|\), not the number of arcs of a sample partition.

The all-size assertion concerns only degree at most two; the full rank and all cubic-zero multiplicities are claimed **only** for \(n=6\). This distinction is essential.

## Proof

**One-arc count.** For an arc \(e=(i,j)\) of length \(d=j-i\), the number \(N_e\) of noncrossing partitions containing it is
\[
N_e=C_{d-1}C_{n-d}.
\]
Indeed, the points strictly between \(i\) and \(j\) partition independently because \(e\) joins consecutive members of its block; contracting the arc in the remaining region leaves a noncrossing partition on \(n-d\) points. Catalan log-convexity implies \(N_e=C_{n-1}\) for \(d=1\), while \(N_e\leq C_{n-2}\) for every \(d\geq2\). A pair of *distinct* arcs of length one is contained in exactly \(C_{n-2}\) partitions: contracting both produces a bijection to \(\mathrm{NC}_{n-2}\), even when the arcs meet at an endpoint.

**Positivity.** For two different arcs \(e,f\), let \(N_{ef}\geq0\) count partitions containing both. Inclusion-exclusion gives the exact character formula
\[
\widehat f_n(\{e,f\})=C_n-2N_e-2N_f+4N_{ef}.
\]
For neither arc of length one, this is at least \(C_n-4C_{n-2}>0\), since \(C_n/C_{n-2}\geq5\) for \(n\geq3\). When exactly one arc has length one, it is at least
\[
C_n-2C_{n-1}-2C_{n-2}
=\frac{6(n-1)(n-4)}{n(n+1)}C_{n-2}>0
\quad(n\geq5).
\]
When both have length one, contraction gives the exact positive value
\[
C_n-4C_{n-1}+4C_{n-2}
=\frac{4(n^2-5n+9)}{n(n+1)}C_{n-2}>0.
\]
For a singleton frequency the same counting yields \(\widehat f_n(\{e\})=C_n-2N_e\geq C_n-2C_{n-1}>0\) for \(n\geq3\); the constant coefficient equals \(C_n>0\). Thus all degree-at-most-two coefficients are positive for every \(n\geq5\).

**Cubic sharpness at six labels.** The three arcs \((1,2),(1,3),(1,4)\) cannot coexist in a successor-arc set because each uses the same left endpoint. Their single-arc containment counts at \(n=6\) are \(42,14,10\), hence the corresponding cubic coefficient is exactly \(132-2(42+14+10)=0\). This is an explicit, non-computational zero witness.

**Exact finite census and nullity.** Every noncrossing partition produces a collection of noninterleaving arcs having at most one arc entering and one leaving each vertex. Conversely, any such arc collection is a disjoint union of increasing directed paths; its components give a unique noncrossing partition. Therefore iterating all \(2^{15}\) subsets of the fifteen possible arcs, retaining precisely those satisfying the three local constraints (no crossing, in-degree at most one, out-degree at most one), is an exhaustive finite argument. The standalone integer checker implements this characterization independently of a restricted-growth-word partition generator, confirms that they give identical sets of exactly \(132\) vectors, computes every Walsh multiplier by exact integer butterflies and directly recomputes all \(32768\) signed sums without using the transform. The count of exact zeros by degree is:

| Walsh degree | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Zero multipliers | 25 | 95 | 366 | 960 | 1610 | 1830 | 1785 | 1362 | 720 | 255 | 65 | 10 | 1 |

There are no zeros of degree zero, one, or two. The row sums to \(9084\); diagonalization of convolution by the Walsh character basis gives rank \(32768-9084=23684\). This computation is exhaustive over a stated *finite* set, not a numerical extrapolation. A machine-readable list of all 25 cubic zeros accompanies the checker.

Finally \(N_e\) is even for every arc at \(n=6\), since the five possible arc-length counts are \(42,14,10,10,14\). For any frequency \(S\), reducing the expansion \(\prod_{e\in S}(1-2\mathbf1_{e\in A(\pi)})\) modulo four gives \(\widehat f_6(S)\equiv C_6-2\sum_{e\in S}N_e\equiv0\pmod4\). The exhaustive spectrum contains multiplier \(-4\) at \(S=\{(1,3),(1,5),(2,3),(2,4)\}\), proving the sharp nonzero magnitude \(4\).

## Verification

Run `python3 checks/verify_noncrossing_arcs.py` using Python 3.8 or newer from the extracted package root. Only the Python standard library is needed. The checker independently generates partitions by restricted-growth words and arcs by direct edge-subset constraints, compares the generated supports, tests Catalan cardinalities, checks exact Parseval and parity identities, independently evaluates all six-label Fourier characters by direct summation, verifies the zero-degree histogram, the fourfold divisibility and least positive magnitude, and compares the 25 cubic zeros to `checks/cubic_zeros_n6.csv`. Its exact finite results also include the neighboring cases \(n=4\) (nullity \(20\)) and \(n=5\) (nullity \(164\)); these provide contextual consistency checks, not an infinite-rank claim. The proof of all-size quadratic positivity above is analytic and does not depend on those experiments.

## Relationship to prior work

Classical noncrossing set partitions and their Catalan counts underlie the calculation. Chen–Deng–Du–Stanley–Yan (2005) give crossing/nesting characterizations for partitions. Reading (2014) identifies standard noncrossing partitions with left noncrossing arc diagrams, precisely motivating the positional successor-arc representation. Armstrong–Stump–Thomas (2011) study noncrossing partitions via Coxeter-theoretic bijections and cyclic sieving. These combinatorial enumerations do not, in the inspected material, give positivity of the signed positional Fourier coefficients or the exact six-label Boolean convolution rank.

An earlier relation-incidence Fourier calculation for noncrossing partitions records *every* same-block pair, rather than only *consecutive* within-block arcs. The two embeddings are not related by a linear coordinate change on the Boolean cube: same-block relations on nonconsecutive vertices require transitive closure of successor arcs. Consequently its modulo-four multiplier statements do not imply the present all-size positivity or the six-label successor-arc nullity. Likewise, Fourier sampling on noncrossing perfect matchings involves a different Catalan set and incidence geometry.

## Limitations

No full-rank classification is asserted beyond six labels, and no classification of cubic zeros for all larger sizes is proved. The six-label nullity and the precise number of cubic zeros rely on the exhaustive, reproducible finite integer certificate, not on a closed-form all-size formula. The literature comparison is bounded and does not establish absolute historical priority; a specialized unindexed signed noncrossing-arc enumerator could overlap. Independent scientific validation has not been performed.

## References

- W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, arXiv:math/0501230, first submitted 2005-01-14. https://arxiv.org/abs/math/0501230
- N. Reading, *Noncrossing arc diagrams and canonical join representations*, arXiv:1405.6904, first submitted 2014-05-27. https://arxiv.org/abs/1405.6904
- D. Armstrong, C. Stump, H. Thomas, *A uniform bijection between nonnesting and noncrossing partitions*, arXiv:1101.1277, first submitted 2011-01-06. https://arxiv.org/abs/1101.1277
