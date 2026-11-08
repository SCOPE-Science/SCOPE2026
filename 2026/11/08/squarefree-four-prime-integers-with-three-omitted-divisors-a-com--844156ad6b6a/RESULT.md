# Squarefree four-prime integers with three omitted divisors: a complete classification

## Finding
A positive integer \(n\) is called **3-near-perfect in the three-distinct-divisor sense** when there exist three pairwise distinct positive proper divisors \(d_1,d_2,d_3\) with
\[
\sigma(n)=2n+d_1+d_2+d_3,
\]
where \(\sigma\) is the sum-of-divisors function. Here “3-near-perfect” means existence of *exactly three terms in this representation*, not exclusion of other representations involving fewer terms.

**Theorem.** Among squarefree positive integers having exactly four distinct prime factors, the 3-near-perfect integers are precisely
\[
\begin{gathered}
210,330,390,510,570,690,770,798,858,910,1190,1302,1430,1554,1610,\\
1806,1938,2002,2010,2090,2130,2210,2530,2590,2870,2990,3010,3230,\\
3290,3354,3738,3770,4026,4070,4510,4686,4690,4970,5110,5170,5538,\\
6474,6942,7490,8034,8890,9590,9906,10842,11622,12714.
\end{gathered}
\]
There are \(51\) such integers, and their combined number of *unordered* triples of distinct proper divisors satisfying the equation is \(60\). Exactly eight integers possess more than one admissible triple.

## Assumptions and scope
Squarefree means no prime-square divisor. Prime factors are distinct by hypothesis; all divisors are positive; triples are unordered sets, so permutations are not counted. The definition does not assert the absence of additional decompositions with other numbers of omitted divisors. Although some literature permits the whole number to be an omitted divisor, it is impossible in this class: the divisor-sum ratio is always at most \(\frac32\frac43\frac65\frac87=\frac{96}{35}<3\), whereas omitting the whole number would force a ratio greater than \(3\). Thus the classification is unchanged under either convention. The result concerns the full infinite four-prime squarefree class, not a bounded initial segment.

## Proof
**Step 1: parity and a first prime restriction.** For odd squarefree \(n\) with four prime factors, monotonicity of \((p+1)/p\) bounds
\[
\frac{\sigma(n)}n\le\frac43\cdot\frac65\cdot\frac87\cdot\frac{12}{11}=\frac{2304}{1155}<2.
\]
Hence an admissible \(n\) must be even. Write \(n=2pqr\), with odd primes \(3\le p<q<r\). The necessary condition \(\sigma(n)>2n\) first gives \(p\le7\), because for \(p\ge11\) the largest possible ratio occurs for \((p,q,r)=(11,13,17)\) and is \(4536/2431<2\). If \(p=7\), the only possible pair is \((q,r)=(11,13)\): both \((7,11,17)\) and \((7,13,17)\) give ratios below \(2\), so all larger \(q,r\) are excluded. If \(p=5\), then \(q\le17\): the minimal excluded configuration \((5,19,23)\) already has ratio \(864/437<2\), and the ratio decreases when \(q,r\) increase.

**Step 2: bounding the remaining prime when \(p=3\).** For \(n=6qr\), expansion gives
\[
\sigma(n)-2n=12r+12q+12.
\]
Suppose \(q\ge29\), so \(r>q\). Then \((q-12)r>12(q+1)\), implying \(qr>12r+12q+12\). Thus no omitted divisor can be divisible by \(qr\). The remaining proper divisors are contained in
\[
\{1,2,3,6,q,2q,3q,6q,r,2r,3r,6r\}.
\]
The sum of any three distinct members of this set is at most \(11(1+q+r)\): within each of the three groups (constant divisors, multiples of \(q\), and multiples of \(r\)), the sum of at most three distinct coefficients from \(\{1,2,3,6\}\) is at most \(6+3+2=11\). But \(11(1+q+r)<12(1+q+r)\), contradiction. Therefore \(q\le23\).

**Step 3: a finite *exact* reduction without a cutoff on \(r\).** For each allowed pair, namely
\[
(p,q)\in\{(3,5),(3,7),(3,11),(3,13),(3,17),(3,19),(3,23),
(5,7),(5,11),(5,13),(5,17),(7,11)\},
\]
put
\[
A=-pq+3p+3q+3,\qquad B=3(p+1)(q+1).
\]
Multiplicativity gives
\[
\sigma(2pqr)-4pqr=Ar+B.
\]
Let \(D=\{1,2,p,2p,q,2q,pq,2pq\}\). Every proper divisor of \(2pqr\) appears **exactly once** in the list
\[
\{d:d\in D\}\ \cup\ \{dr:d\in D\setminus\{2pq\}\}.
\]
Thus there are exactly \(15\) distinct choices before selecting a triple. For a three-element choice write its divisor sum as \(Cr+E\), where \(C\) is the sum of its coefficients attached to \(r\) and \(E\) the sum of its coefficients independent of \(r\). For every triple, \(E\le 2pq+pq+2q=3pq+2q<B\). Hence equality \(Ar+B=Cr+E\) cannot occur with \(A=C\), and in every case forces the unique candidate
\[
r=\frac{E-B}{A-C}.
\]
The certificate evaluates all \(\binom{15}{3}=455\) unordered choices for each of the twelve pairs. It retains a candidate precisely if the fraction is an integer, \(r>q\) is prime, and the three proper divisors satisfy the displayed defining equality. This is exhaustive because all infinite choices of \(r\) have been reduced to a single rational candidate for each of \(12\cdot455=5460\) finite templates; no brute-force upper bound on \(r\) is assumed.

**Step 4: finite evaluation.** The supplied standalone standard-library program `check.py` implements Step 3 with integer arithmetic and elementary trial-division primality. It reports the \(51\) values displayed above and exactly \(60\) unordered witnessing triples. For each retained triple it separately confirms proper divisibility and the defining equation. An independent direct scan of every integer through \(13000\), factoring each and enumerating triples of proper divisors, reproduces the same complete sets of integers and triples. Step 3, rather than the direct bounded scan, is what proves that no larger integer qualifies.

The eight integers with multiple representations are \(570,690,858,910,1610,2210,3010,4690\). Of these \(910\) has three unordered omitted triples; each of the other seven has two.

For reproducibility, the complete witness table follows; each parenthesized entry is an unordered triple of proper divisors.

| Integer | Excluded-divisor triples |
|---:|---|
| 210 | (21, 30, 105) |
| 330 | (6, 33, 165) |
| 390 | (3, 30, 195) |
| 510 | (6, 15, 255) |
| 570 | (5, 10, 285), (15, 95, 190) |
| 690 | (1, 2, 345), (3, 115, 230) |
| 770 | (1, 77, 110) |
| 798 | (1, 57, 266) |
| 858 | (1, 13, 286), (3, 11, 286) |
| 910 | (1, 13, 182), (1, 65, 130), (35, 70, 91) |
| 1190 | (7, 35, 170) |
| 1302 | (3, 31, 434) |
| 1430 | (10, 11, 143) |
| 1554 | (1, 21, 518) |
| 1610 | (1, 5, 230), (5, 70, 161) |
| 1806 | (3, 7, 602) |
| 1938 | (19, 102, 323) |
| 2002 | (1, 13, 14) |
| 2010 | (5, 201, 670) |
| 2090 | (11, 19, 110) |
| 2130 | (1, 213, 710) |
| 2210 | (5, 26, 85), (17, 34, 65) |
| 2530 | (23, 46, 55) |
| 2590 | (37, 70, 185) |
| 2870 | (7, 14, 287) |
| 2990 | (1, 2, 65) |
| 3010 | (1, 14, 301), (5, 10, 301) |
| 3230 | (1, 2, 17) |
| 3290 | (1, 2, 329) |
| 3354 | (39, 86, 559) |
| 3738 | (7, 534, 623) |
| 3770 | (2, 5, 13) |
| 4026 | (22, 183, 671) |
| 4070 | (2, 11, 55) |
| 4510 | (1, 10, 41) |
| 4686 | (2, 213, 781) |
| 4690 | (7, 70, 335), (10, 67, 335) |
| 4970 | (2, 71, 355) |
| 5110 | (1, 70, 365) |
| 5170 | (1, 5, 22) |
| 5538 | (26, 71, 923) |
| 6474 | (2, 83, 1079) |
| 6942 | (1, 78, 1157) |
| 7490 | (2, 35, 535) |
| 8034 | (26, 39, 1339) |
| 8890 | (7, 10, 635) |
| 9590 | (2, 5, 685) |
| 9906 | (2, 39, 1651) |
| 10842 | (3, 26, 1807) |
| 11622 | (6, 13, 1937) |
| 12714 | (2, 3, 2119) |

## Verification
Run `python3 check.py` from the package directory; no third-party modules, downloaded tables or external files are needed. The program evaluates all \(5460\) finite templates, independently scans \(n\le13000\), and asserts equality of both solution sets and witness-triplet sets. The actual output is in `check_output.txt`. These are exact finite computations; the elementary inequalities and rational-candidate reduction in the preceding proof provide the required global completeness argument.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery and Zelinsky (2023) introduce and classify several two-omitted-divisor families, notably those supported on two distinct primes, but their theorems do not yield the present *three*-omitted-divisor, *four*-distinct-prime squarefree census. Fearon and collaborators (2025) complete the two-prime-support case for two omitted divisors; their Section 6.3 lists only eight initial 3-near-perfect examples (all below the first four-prime squarefree example) and notes the challenge of finding analogous families. Those results do not imply this four-prime three-omission classification. A published three-prime-support *three-deficient-perfect* classification concerns the opposite divisor-sum sign and a different support. The known squarefree four-prime *two-near-perfect* census similarly imposes only two omitted divisors. The present proof gives a complete finite reduction specific to three omitted divisors.

## Limitations
The claim is restricted to squarefree integers having four distinct prime factors and the existence of three distinct omitted proper divisors. It makes no claim about higher prime support, non-squarefree integers, or minimal possible omitted-divisor count. All \(60\) witness triples are verified exactly; independent external mathematical review has not been performed. Literature indexing cannot establish absolute novelty.

## References
- V. Aryan, D. Madhavani, S. Parikh, I. Slattery, J. Zelinsky, *On 2-Near Perfect Numbers*, arXiv:2310.01305 (first posted 2023-10-02), https://arxiv.org/abs/2310.01305.
- R. Fearon, H. Foushee, B. Porosoff, A. Skula, J. Zelinsky, K. Zhang, *Complete characterization of 2-near perfect numbers with exactly 2 prime factors*, arXiv:2508.06651 (2025-08-08), https://arxiv.org/abs/2508.06651.
- M. Tang, X. Ma, M. Feng, *On near-perfect numbers*, Colloquium Mathematicum 144 (2016), https://doi.org/10.4064/cm6588-10-2015 (single omitted divisor).
