# Enumerating every minimum independent dominating set of path–clique direct products

## Finding
Let \(P_n\) be the path on the labeled vertices \(1,\ldots,n\), let \(K_q\) have the labeled colors \(1,\ldots,q\), and let \(P_n\times K_q\) denote their direct (categorical/tensor) product. Write \(N(n,q)\) for the number of distinct minimum-cardinality maximal independent vertex sets, with all graph vertices labeled. For all integers \(n,q\ge2\), the following formulas hold.

For \(q\ge3\), put
\[
 r=\left\lfloor\frac{n+1}{3}\right\rfloor,\qquad
 t=n-3r+1\in\{0,1,2\}.
\]
Then the independent domination number and the number of its minimizers are
\[
 i(P_n\times K_q)=n-r+1=\left\lceil\frac{2n+2}{3}\right\rceil,
\qquad
 N(n,q)=\binom{r+t-1}{t}q(q-1)^{r-1}
 +\mathbf{1}_{\{(n,q)=(3,3)\}}.
\]
Except when \((n,q)=(3,3)\), **every** minimizer consists of one selected vertex in each nonempty clique fiber, and its selected path positions are exactly \(r\) consecutive monochromatic runs, each of length at least two, separated by exactly one empty fiber. Consecutive runs have different colors, their endpoints occupy the endpoints of the path, and the total run-length excess over two is exactly \(t\). When \((n,q)=(3,3)\), one additional minimizer consists of all three vertices in the middle fiber.

For \(q=2\), put \(k=\lceil n/3\rceil\). The product is two disjoint copies of \(P_n\), and
\[
 i(P_n\times K_2)=2k,\qquad
 N(n,2)=\binom{k+1}{3k-n}^{\!2}.
\]
Here every minimizer is the independent choice of a minimum maximal independent set in each path component. In particular, for \(q\ge3\) the minimum-set multiplicity grows exponentially with the path length even though the minimum size does not depend on \(q\).

## Assumptions and scope
The graphs are finite, simple and undirected; all vertices remain individually labeled, and sets are counted without quotienting by color permutations or path reversal. Two vertices \((j,a)\) and \((j',a')\) are adjacent exactly when \(|j-j'|=1\) and \(a\ne a'\). An independent dominating set is equivalently a maximal independent set; \(i(G)\) denotes the minimum cardinality of such a set. The formulas cover exactly all integers \(n,q\ge2\), not \(n=1\) or \(q=1\).

## Proof
**Layer classification.** Fix \(q\ge3\) and a maximal independent set \(S\). In path layer \(j\), either no vertex is selected (state \(E\)), exactly one vertex of color \(a\) is selected (state \(R_a\)), or all \(q\) vertices are selected (state \(F\)). Indeed, if two different colors are selected in a layer, independence forces each adjacent layer to be empty. Any omitted color in the original layer would then have no selected neighbor, violating domination. Adjacent nonempty singleton layers necessarily have the same color. A singleton layer needs at least one adjacent singleton layer of that color: otherwise its unselected vertices cannot be dominated. Every empty layer must have an adjacent full layer, or have two adjacent singleton layers of distinct colors. These conditions are also sufficient for independence and domination.

Consequently every valid row word has a unique decomposition into pieces, each being either a full layer \(F\) of length one or a monochromatic singleton run \(R_a^\ell\) with \(\ell\ge2\). Between two pieces is one empty layer, except that two full pieces may be separated by two empty layers. Two singleton runs across a single empty layer must have distinct colors. A boundary empty layer is permitted precisely when the adjacent piece is full; in particular three consecutive empty layers are impossible. This exhaustive description includes both endpoint cases and the exceptional word \(E,F,E\).

**Eliminating full layers at minimum weight.** Let \(f\) be the number of full pieces, \(r'\) the number of singleton-run pieces, and \(\ell_1,\ldots,\ell_{r'}\ge2\) their lengths. Let \(d\) count two-empty separators between full pieces, and let \(b\in\{0,1,2\}\) count boundary empty layers. (Each pair of consecutive pieces has at least one empty separator.) With \(w=|S|\), exact length and weight bookkeeping gives
\[
 n=\sum_{j=1}^{r'}\ell_j+r'+2f-1+d+b,
 \qquad w=\sum_{j=1}^{r'}\ell_j+qf,
\]
and hence
\[
 3w-2n=\sum_{j=1}^{r'}(\ell_j-2)+(3q-4)f+2-2d-2b.\tag{1}
\]
If \(f\ge2\), then \(d\le f-1\), \(b\le2\), and (1) yields \(3w-2n\ge(3q-6)f\ge6\). If \(f=1\) and \(b\le1\), (1) yields \(3w-2n\ge3q-4\ge5\). Finally, \(f=1,b=2\) forces the entire row word to be \(E,F,E\), so \(n=3\) and \(w=q\). Thus for \(n\ge4\) every set containing a full piece satisfies \(3w-2n\ge5\). The three-layer exception is compared directly with the singleton optimum below.

**Optimal singleton words and enumeration.** If \(f=0\), the decomposition has \(r'\ge1\) singleton runs, no boundary empty layers, and exactly \(r'-1\) single-empty separators. Therefore \(n=\sum\ell_j+r'-1\ge3r'-1\) and \(w=n-r'+1\). Maximizing the number of runs gives \(r'=r=\lfloor(n+1)/3\rfloor\), \(w_0=n-r+1=\lceil(2n+2)/3\rceil\), and \(3w_0-2n\in\{2,3,4\}\). Equation (1) shows that any full-containing word with \(n\ne3\) has strictly larger cardinality. At \(n=3\) the full word \(E,F,E\) has weight \(q\), equal to \(w_0=3\) only for \(q=3\); for \(q\ge4\) it is strictly heavier. Thus all minimizers are exactly the stated singleton words except for that one extra set.

For the singleton words, write \(\ell_j=2+e_j\). The nonnegative integers \(e_j\) sum to \(t=n-3r+1\), so their number is \(\binom{r+t-1}{t}\). The first run has \(q\) possible colors, and each next run has \(q-1\) colors because neighboring runs must differ. Multiplying proves the formula and the claimed bijective classification.

**The two-color boundary.** For \(q=2\), the direct product of the bipartite path with \(K_2\) has two connected components, each an isomorphic labeled copy of \(P_n\). In a path, any minimum maximal independent set has \(k=\lceil n/3\rceil\) vertices, with at most one unselected vertex before its first chosen vertex, at most one after its last, and one or two unselected vertices between consecutive chosen vertices. Starting from the largest possible total length \(3k\), the deficit \(3k-n\) is distributed by reducing by one the maximum allowed unselected gap at any of \(k+1\) distinguishable gap positions. Every such choice gives a distinct minimum maximal independent set. Thus their number is \(\binom{k+1}{3k-n}\), and choosing independently in both components proves the squared formula.

## Verification
The standalone file `verify.py` implements two distinct checks. First, it constructs product graphs directly and exhaustively checks independence and domination for every subset at or below the predicted minimum size, for 27 small parameter pairs. Second, a finite-state dynamic program counts minimum valid layer words for all \(2\le n\le80\) and \(2\le q\le8\), totaling 553 parameter pairs, and compares with the closed forms. Both checks passed. The finite computations are consistency checks; the preceding bijections and inequalities prove the complete infinite statement.

Reproduce using Python 3 with `python verify.py`; no external libraries or online services are required.

## Relationship to prior work
Kuenzel and Rall, *On independent domination in direct products* (first public arXiv version 23 March 2022), Proposition 6, established the numerical values of \(i(P_n\times K_q)\), and their Lemma 4 and conditions 1–4 encode the possible layer occupancies. Their paper provides example optimal words but does not give the total number or a classification of **all** optimal words. The present contribution is an exact labeled multiplicity formula for all parameters, with the structural exclusion of full layers except at \((3,3)\). These multiplicities require additional global gap counting and a strict full-layer inequality, not simply the preexisting minimum-size formula. Earlier results on well-covered direct products concern equality of all maximal-set sizes, not the count of minimum sets. The usual path-counting identity supplies the separate \(q=2\) boundary.

## Limitations
The enumeration is for labeled graph vertices and the direct product only, not the Cartesian or strong products. It does not enumerate nonminimum maximal independent sets or color-permutation orbits. The result has been checked against identified literature and mathematical-record searches but may have an unindexed equivalent; a potentially relevant 2016 dissertation on uniqueness and some direct products could not be read beyond its public abstract. There has been no independent mathematical audit.

## References
1. K. Kuenzel and D. F. Rall, *On independent domination in direct products*, arXiv:2203.12397v1 (23 March 2022), Section 3, Lemma 4, Proposition 6, and Table 2. https://arxiv.org/abs/2203.12397
2. K. Kuenzel and D. F. Rall, *On well-covered direct products*, arXiv:1901.03218v1 (10 January 2019); Discussiones Mathematicae Graph Theory 42 (2022), 627–640. https://arxiv.org/abs/1901.03218
3. J. T. Hedetniemi, *Problems in Domination and Graph Products*, Clemson University dissertation (2016), abstract and bibliographic record. https://open.clemson.edu/all_dissertations/1640/
