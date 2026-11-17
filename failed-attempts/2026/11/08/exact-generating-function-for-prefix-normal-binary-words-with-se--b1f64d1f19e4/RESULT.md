# Exact generating function for prefix-normal binary words with seven ones

## Finding

For every integer \(n\ge 0\), let \(p_7(n)\) be the number of length-\(n\) binary words containing exactly seven ones such that, for every length \(k\), the initial \(k\) symbols contain at least as many ones as any other contiguous factor of length \(k\). Then the ordinary generating function has the following explicit rational form:

\[
 F_7(z):=\sum_{n\ge0}p_7(n)z^n
 =\frac{z^7 N(z)}{(1-z)(1-z^3)(1-z^4)^2(1-z^6)^3},
\]

where the degree-eighteen polynomial, written with its coefficients in ascending order, is

\[
 ( [z^j]N(z))_{j=0}^{18}=
 (1,3,9,17,35,48,76,85,108,103,108,85,76,48,35,17,9,3,1).
\]

In particular, \(p_7(n)\sim \frac{289}{2488320}n^6\), and among all length-\(n\) words containing seven ones, the proportion that are prefix normal is asymptotic to \(\frac{2023}{3456n}\). The first values, for \(n=7,\ldots,20\), are \(1,4,13,31,71,134,249,417,688,1062,1628,2367,3430,4781\).

## Assumptions and scope

The alphabet is \(\{0,1\}\), and factors are contiguous, not scattered. A word is *1-prefix normal* when \(\#_1(w[1..k])\ge \#_1(w[i..i+k-1])\) for every admissible \(k,i\). Words with seven ones must start with one to be prefix normal. All counts are for labeled linear words, not necklaces and not words up to reversal. The variable \(z\) is an ordinary length marker. All identities are formal power series over \(\mathbb Q\).

## Proof

**Reduction to a pointed lattice cone.** Any eligible word has a unique representation

\[
 w=1\,0^{r_1-1}1\,0^{r_2-1}1\cdots 0^{r_6-1}1\,0^t,
 \quad r_j\ge1,\quad t\ge0.
\]

For each \(k=1,\ldots,5\), a prefix containing \(k+1\) ones is the shortest possible factor containing \(k+1\) ones exactly when the sum of its first \(k\) successive one-to-one distances is no greater than every length-\(k\) consecutive sum of these six distances. The equivalence follows directly by comparing the distance from the first to the last one in a factor: any violation yields a shorter factor with \(k+1\) ones than the prefix of that many ones, and conversely. This is also the gap criterion of Burcsi–Fici–Lipták–Ruskey–Sawada.

Put \(r_1=1+a\), with \(a\ge0\), and \(r_{i+1}=r_1+x_i\) for \(1\le i\le5\). The one-gap inequalities are precisely \(x_i\ge0\). After cancelling the common multiples of \(r_1\), all remaining nonredundant requirements reduce to

\[
 x_2+x_3\ge x_1,\quad
 x_3+x_4\ge x_1,\quad
 x_4+x_5\ge x_1,\quad
 x_3+x_4+x_5\ge x_1+x_2.
\]

The word length is \(n=7+6a+x_1+\cdots+x_5+t\). Thus, with \(C\subset\mathbb R^5\) the closed cone given by these nine inequalities, and \(G(z)=\sum_{x\in C\cap\mathbb Z^5}z^{x_1+\cdots+x_5}\),

\[
 F_7(z)=\frac{z^7}{(1-z)(1-z^6)}G(z).
\]

**Exact cone decomposition.** The primitive extreme rays of \(C\), labeled \(v_0,\ldots,v_{12}\), are as follows (coordinates are \(x_1,\ldots,x_5\)):

| Ray | Vector | Sum of coordinates |
|---|---|---|
| 0 | 0, 0, 0, 0, 1 | 1 |
| 1 | 0, 0, 0, 1, 0 | 1 |
| 2 | 0, 0, 1, 0, 0 | 1 |
| 3 | 0, 1, 0, 0, 1 | 2 |
| 4 | 0, 1, 0, 1, 0 | 2 |
| 5 | 0, 1, 1, 0, 0 | 2 |
| 6 | 1, 0, 1, 0, 1 | 3 |
| 7 | 1, 0, 1, 1, 0 | 3 |
| 8 | 1, 1, 0, 1, 1 | 4 |
| 9 | 1, 1, 0, 2, 0 | 4 |
| 10 | 1, 1, 1, 0, 1 | 4 |
| 11 | 2, 1, 1, 1, 1 | 6 |
| 12 | 2, 1, 1, 2, 0 | 6 |

These rays are exhaustive: every extreme ray lies on at least four independent active inequalities, and solving all such four-hyperplane subsystems gives precisely the listed thirteen feasible primitive rays. The cone has nine facets, represented by the following sets of ray indices:

\[
\begin{gathered}
\{0,1,2,3,4,5\},\ \{0,1,2,6,7\},\ \{0,1,3,4,8,9\},\\
\{0,1,6,7,8,9,11,12\},\ \{0,2,3,5,6,10\},\\
\{0,3,6,8,10,11\},\ \{1,2,4,5,7,9,12\},\\
\{2,5,6,7,10,11,12\},\ \{3,4,5,8,9,10,11,12\}.
\end{gathered}
\]

Their exhaustiveness is checked by taking every independent four-ray span, choosing a rational normal, retaining spans that support all thirteen rays on the same side, and identifying coincident faces. Recursively triangulate each face by coning its smallest-index ray over the corresponding triangulations of facets not containing that ray. This standard pulling subdivision yields fifteen full-dimensional simplicial cones, with disjoint interiors and union \(C\). To partition their lattice points without double-counting common boundaries, choose the generic vector \(q=(7,11,13,17,19)\) and retain the points \(x\) for which \(x+\varepsilon q\) belongs to the corresponding simplex for all sufficiently small \(\varepsilon>0\). The vector has nonzero coordinates in every simplicial basis.

Each simplicial cone with basis matrix \(V\) contributes a product denominator \(\prod_j(1-z^{|v_j|_1})\) and a numerator recording the lattice points in its *half-open* fundamental parallelepiped. The determinant magnitudes are \(1\) for ten cones and \(2\) for five cones; therefore every numerator has just one or two monomials. The exact calculation is:

| Ray indices of simplex | Denominator exponents | Numerator exponents |
|---|---|---|
| 0,1,2,5,12 | 1,1,1,2,6 | 0,4 |
| 0,1,2,7,12 | 1,1,1,3,6 | 3 |
| 0,1,4,5,12 | 1,1,2,2,6 | 2,6 |
| 0,1,4,9,12 | 1,1,2,4,6 | 4 |
| 0,2,5,10,11 | 1,1,2,4,6 | 4 |
| 0,2,5,11,12 | 1,1,2,6,6 | 6,10 |
| 0,2,6,7,12 | 1,1,3,3,6 | 6 |
| 0,2,6,11,12 | 1,1,3,6,6 | 3 |
| 0,2,6,10,11 | 1,1,3,4,6 | 7 |
| 0,3,4,5,12 | 1,2,2,2,6 | 2,6 |
| 0,3,4,9,12 | 1,2,2,4,6 | 6 |
| 0,3,5,10,11 | 1,2,2,4,6 | 6 |
| 0,3,5,11,12 | 1,2,2,6,6 | 8,12 |
| 0,3,8,9,12 | 1,2,4,4,6 | 4 |
| 0,3,8,11,12 | 1,2,4,6,6 | 10 |

For an explicit way to verify every numerator: let \(\beta=V^{-1}q\). The coordinate interval is \([0,1)\) when \(\beta_j>0\), and \((0,1]\) when \(\beta_j<0\). When \(|\det V|=1\), the only lattice representative has coordinates one at the strict intervals and zero elsewhere. When \(|\det V|=2\), take in addition the nontrivial coset, whose coordinates have fractional parts zero or one-half; zeros in strict intervals must be replaced by one. These rules give exactly the table, without numerical approximation.

Summing the fifteen rational terms and reducing by exact polynomial arithmetic gives

\[
 G(z)=\frac{N(z)}{(1-z^3)(1-z^4)^2(1-z^6)^2}.
\]

Substitution into the previously proved relation yields the claimed \(F_7(z)\). There is no extrapolation from finite coefficients: the generating-function identity follows from an exact partition of *all* integer points of \(C\).

**Leading asymptotic.** The numerator satisfies \(N(1)=867\). At \(z=1\), the denominator of \(F_7\) has a pole of order seven with leading multiplier \(3\cdot 4^2\cdot6^3=10368\); every other root-of-unity pole has order at most five. Thus coefficient extraction yields

\[
 p_7(n)=\frac{867}{10368\cdot6!}n^6+O(n^5)
 =\frac{289}{2488320}n^6+O(n^5).
\]

Since \(\binom n7\sim n^7/7!\), division gives \(2023/(3456n)+O(n^{-2})\) for the conditional probability.

## Verification

`verify_density7.py` is self-contained apart from the documented SymPy dependency. It exactly regenerates the thirteen extreme rays from active inequalities, the nine supporting facets and the fifteen pulling simplices; checks their half-open lattice representatives and the rational identity; compares independently generated gap counts for every \(n=7,\ldots,27\) with the rational coefficients; and independently tests the definition of prefix normality on **every** seven-one word of lengths \(7,\ldots,20\) by direct sliding-window counts. Actual run output:

```
EXACT_CONE_G.F._OK; 13 rays, 9 facets, 15 pulling simplices
DIRECT_WORD_COUNTS_OK; lengths 7..20
INDEPENDENT_GAP_COUNTS_OK; lengths 7..27
LEADING_CONSTANT_OK; 289/2488320
COUNTS_7_TO_20: [1, 4, 13, 31, 71, 134, 249, 417, 688, 1062, 1628, 2367, 3430, 4781]
```

## Relationship to prior work

Fici and Lipták (2011) introduced the prefix-normal property and its connection to jumbled pattern matching. Burcsi and collaborators (2014), Section 4, Lemmas 2–3, provide the exact gap inequalities and generating functions for density at most six. Their expanded treatment (2016), Section 4.2, proves rationality at every fixed density by general lattice-point theory but explicitly says that concrete formulas beyond six were not obtained. Rationality is **not** claimed as new; the explicit density-seven numerator, denominator, coefficient sequence and leading constant are the present contribution. Adamson and collaborators (2025) study word-chain generators and prefix-normal testing, not this fixed-density generating function. A separate earlier observation about prefix-normal defects in an automatic sequence concerns a different invariant.

## Limitations

This is a fixed-density result: it says nothing new about the unrestricted asymptotic count of prefix-normal words as density grows. The general fact that fixed-density generating functions are rational was already known. Originality is judged relative to the inspected papers, indexed database hits and available overlap records, not a proof of global historical priority; an unindexed equivalent calculation or a table deposited elsewhere remains a possibility. The calculation has undergone self-review, not independent external validation.

## References

1. G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory, LNCS 6795 (2011), pp. 228–238, DOI 10.1007/978-3-642-22321-1_20; freely accessible later manuscript: https://arxiv.org/pdf/1805.12405 .
2. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824, publicly posted April 1, 2014, https://arxiv.org/pdf/1404.2824 .
3. P. Burcsi et al., *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, publicly posted November 28, 2016, https://arxiv.org/pdf/1611.09017 .
4. D. Adamson, M. Dudey, P. Fleischmann and A. Huch, *Word Chain Generators for Prefix Normal Words*, arXiv:2508.19619 (2025), https://arxiv.org/pdf/2508.19619 .
