# Exact square spectra of three-marker binary circular words and a five-ninths law

## Finding

Let \(w\) be a binary circular word of length \(n\ge3\) containing exactly three occurrences of the letter \(1\). Let \(g_0,g_1,g_2\ge1\) be the successive cyclic distances between these occurrences (thus \(n=g_0+g_1+g_2\)), and sort them as \(a\le b\le c\). A *circular square* is a distinct literal word \(XX\), where \(X\ne\varepsilon\) and \(2|X|\le n\), appearing contiguously in some rotation of \(w\). Write \(S_\circ(w)\) for the number of these square words. Then

\[
\boxed{S_\circ(w)=\left\lfloor\frac{c-1}{2}\right\rfloor+M(a,b,c),}
\]

where

\[
\boxed{M(a,b,c)=\begin{cases}
a,&a=b=c,\\
a+(2a-c)_+,&a=b<c,\\
a+\min(b,2a),&a<b=c,\\
2a+(a+b-c)_+,&a<b<c,
\end{cases}}
\qquad t_+=\max(0,t).
\]

The following rule classifies **each square**, not merely its number. The unary squares are exactly \(0^{2h}\) for \(1\le h\le\lfloor(c-1)/2\rfloor\). For each of the three consecutive-one distances \(g_j\), consider

\[
\max(0,g_j-g_{j+1})\le i\le\min(g_j-1,g_{j-1}-1),\qquad i\in\mathbb Z,
\]

with subscripts modulo three. Every mixed square, and no other one, is

\[
\boxed{\big(0^i1\,0^{g_j-i-1}\big)^2}
\]

for at least one such pair \((j,i)\). Coincident literal words from different gaps are counted only once.

For a uniformly sampled, **indexed** length-\(n\) binary word \(W_n\) with exactly three ones (not a uniformly sampled rotation class),

\[
\boxed{\mathbb E[S_\circ(W_n)]=\frac59n+O(1).}
\]

More precisely, if \((A,B,C)\) is the sorted version of \(\operatorname{Dirichlet}(1,1,1)\), then

\[
\boxed{\frac{S_\circ(W_n)}n\xrightarrow{\mathrm d} \frac C2+2A+(1-2C)_+.}
\]

The limiting law is nonconstant and has mean exactly \(5/9\). No claim is made for circular words with four or more marked ones.

## Assumptions and scope

The alphabet is binary, every cyclic gap is **strictly positive**, and the circle contains exactly three marked ones (the others are zeros). Adjacent ones are permitted, so a gap may equal one. The circle's length \(n\) bounds the total length of each counted square, including those crossing a chosen cut. Different square roots give different literal square words; distinct occurrences of the same square are identified. The indexing choice is irrelevant to \(S_\circ\). A circular word is not a word where factors may wrap arbitrarily many times: only the length bound \(2|X|\le n\) applies.

## Proof

**1. Classification by marked letters.** A square contains an even number of ones. With three ones in the entire circle and length at most \(n\), it contains either zero or exactly two ones. The former squares are the unary words \(0^{2h}\). The longest cyclic run of zeros has length \(c-1\), proving their stated range.

A square containing exactly two ones has one one in each half. Its root is uniquely \(X=0^i1\,0^k\) with \(i,k\ge0\). Thus \(XX\) contains the two ones separated by \(i+k\) zeros, i.e. by the distance \(d=i+k+1\). Because no third one occurs within the square, these must be *consecutive* ones of the circle and hence \(d=g_j\) for some \(j\). The prefix \(0^i\) must fit after the preceding marked one, so \(i\le g_{j-1}-1\). The final \(0^k\) must fit before the following marked one, so \(k\le g_{j+1}-1\). Conversely these two inequalities, together with \(i+k=g_j-1\), place the complete square contiguously around that consecutive pair without including another one. They also give \(2g_j\le n-1\) whenever any such solution exists, since summing the inequalities gives \(g_j-1\le (g_{j-1}-1)+(g_{j+1}-1)\); hence the required total-length bound is automatic. Solving for \(i\) gives exactly the displayed interval. This proves the exhaustive square classification.

**2. Counting distinct roots.** The square \((0^i1\,0^{d-i-1})^2\) determines the pair \((d,i)\) uniquely as a literal word, so equal gap lengths can produce duplicate squares, but unequal gap lengths cannot. A circle with three marked ones has every ordering of \((a,b,c)\) equivalent, up to rotation and reversal, so the multiset of the three gaps suffices.

If \(a<b<c\), the intervals from gaps \(a\) and \(b\) each contain \(a\) roots, and the interval from \(c\) contains \((a+b-c)_+\) roots. Their root lengths differ, giving \(2a+(a+b-c)_+\) distinct mixed squares.

If \(a=b<c\), the two equal short gaps yield the same \(a\) literal roots; the long gap yields \((2a-c)_+\) further roots. This gives \(a+(2a-c)_+\).

If \(a<b=c\), the short gap yields \(a\) roots. The two equal long gaps yield integer root-offset intervals \([0,a-1]\) and \([b-a,b-1]\); their union has \(\min(b,2a)\) elements. This gives \(a+\min(b,2a)\).

If \(a=b=c\), all three gap intervals are identical and contain the \(a\) roots with offsets \(0,\ldots,a-1\). Thus the mixed count is \(a\). In each case the unary and mixed square sets are disjoint. This proves the boxed exact formula for every admissible \(n\) without any finite cutoff.

**3. Uniform gap law.** Choose \(W_n\) uniformly among the \(\binom n3\) indexed words with three ones, and independently choose one of its three ones as an anchor. Specifying its indexed anchor location together with the ordered positive distance triple is bijective, so the triple is uniform among the \(\binom{n-1}{2}\) positive compositions of \(n\). Its scaled coordinates converge in distribution to \(\operatorname{Dirichlet}(1,1,1)\). Equal-gap triples form \(O(n)\) compositions among \(\Theta(n^2)\), so their probability is \(O(1/n)\). Outside those diagonals, the formula of step 2 gives

\[
\frac{S_\circ(W_n)}n=\frac{c}{2n}+2\frac an+\left(1-2\frac cn\right)_++O(1/n).
\]

The continuous mapping theorem establishes the displayed distributional limit. The difference between the right-side quantity and the exact count on the equal-gap diagonals is at most \(O(n)\), so their total contribution to the *unscaled expectation* is \(O(1)\). The right-side function is piecewise linear and Lipschitz on the compact simplex; its average over the positive-composition grid differs from its uniform-simplex integral by \(O(1/n)\), as follows by comparing each lattice triangle with its area integral and bounding the boundary triangles. After scaling by \(n\), this contributes at most \(O(1)\). The flooring terms likewise contribute at most \(O(1)\).

**4. Exact limiting mean.** For three uniform Dirichlet coordinates, the mean smallest coordinate is \(\mathbb EA=1/9\), while the mean largest is \(\mathbb EC=H_3/3=11/18\); both identities follow by integrating the order-statistic tails, or from normalized independent unit exponentials. Since \(A+B=1-C\), the correction is \((A+B-C)_+=(1-2C)_+\). On \([1/3,1/2]\), inclusion-exclusion for the uniform simplex gives \(\mathbb P(C\le t)=(3t-1)^2\). Therefore

\[
\mathbb E(1-2C)_+=2\int_{1/3}^{1/2}(3t-1)^2\,dt=\frac1{36}.
\]

Consequently

\[
\mathbb E\left[\frac C2+2A+(1-2C)_+\right]
=\frac{11}{36}+\frac29+\frac1{36}=\frac59.
\]

The limiting function varies on positive-area open subsets (for instance near the balanced point and near a simplex vertex), hence the limit is nondegenerate. The uniform-grid estimate above proves the stated \(5n/9+O(1)\) expectation, not merely convergence of the normalized expectation. \(\square\)

## Verification

`python3 verify_circular.py` constructs literal circular square sets independently by scanning all starting positions and permissible half-lengths; it compares the full sets with the structural-root classification and checks the four-case closed count for all \(15^3=3375\) positive gap triples with coordinates at most fifteen, and 240 reproducible longer random triples. The output is in `verification_outputs/circular.txt`.

`python3 verify_statistics.py` independently computes the mean from the union of integer offset intervals for thirteen selected lengths through \(500\), prints exact rational means and their differences from \(5n/9\), and verifies the exact Dirichlet-mean arithmetic. The output is in `verification_outputs/statistics.txt`. Both programs use only the Python standard library. Finite runs corroborate but do **not** replace the unrestricted combinatorial and analytic arguments above.

## Relationship to prior work

Hamai's 2026 study of **unrestricted** circular words proves the sharp universal bound \(\lfloor3(n-\sigma)/2\rfloor\); it neither conditions on three marked letters nor enumerates their individual square factors. Charalampopoulos and colleagues' 2026 CPM paper develops unrestricted circular upper bounds and Fibonacci-based lower constructions, not a fixed-three-marker gap classification. The previously published four-cyclic-run binary formula concerns words with exactly two zero and two one runs, whereas the present sparse family has three marked ones and up to six cyclic runs. The known exact square census for **linear** three-one words uses four *linear* zero gaps and does not imply the cyclic three-gap formula or its different expected density. A specialized result for **Abelian-square equivalence classes** at three markers counts equal-half-composition types, not distinct literal ordinary squares; it cannot recover their exact offset multiplicity. These comparisons are about mathematical implication, not titles. Unindexed equivalent work remains a residual priority risk.

## Limitations

The theorem concerns distinct literal ordinary squares in binary circles with exactly three ones, not an unrestricted square extremum, squares with multiplicity, Abelian squares, or circles with four or more ones. It does not provide an all-length exact finite expectation as a closed rational function, although the finite counts can be computed from the complete formula. The limiting distribution is specified by a Dirichlet pushforward without a closed density. Historical priority is qualified by the accessible corpus and specific comparisons; independent validation has not been performed.

## References

1. R. Hamai, *An Asymptotically Tight Bound on the Number of Distinct Squares in Circular Words*, first posted 2026-09-25, arXiv:2609.32084v1, https://arxiv.org/abs/2609.32084 .
2. P. Charalampopoulos, M. Mohamed, J. Radoszewski, W. Rytter, T. Waleń and W. Zuba, *Improved Bounds on the Maximum Number of Distinct Squares in Circular Words*, CPM 2026, https://doi.org/10.4230/LIPIcs.CPM.2026.6 .
3. S. Li and Y. Song, *A Tighter Upper Bound for the Number of Distinct Squares in Circular Words*, first posted 2026-05-12, arXiv:2605.12215, https://arxiv.org/abs/2605.12215 .
4. M. Amit and P. Gawrychowski, *Distinct Squares in Circular Words* (2017), arXiv:1708.00639, https://arxiv.org/abs/1708.00639 .
5. *Exact square spectra and sharp maxima for four-run binary circular words*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-square-spectra-and-sharp-maxima-for-four-run-binary-circul--f790bfb03bb7 .
6. *Exact distinct-square counts and aggregate law for binary words with three ones*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-distinct-square-counts-and-aggregate-law-for-binary-words--9614b0d1e103 .
7. *Exact cyclic Abelian-square type spectrum with three marked letters*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-abelian-square-type-spectrum-with-three-marked-lett--dff15673ad39 .
