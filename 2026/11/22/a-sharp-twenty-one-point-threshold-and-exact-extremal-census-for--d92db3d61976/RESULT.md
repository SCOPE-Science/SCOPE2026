# A sharp twenty-one-point threshold and exact extremal census for permutation extension rank three

## Finding

Let \(\mathcal P\) be the hereditary class of all finite structures with **two named strict linear orders**. Let \(\operatorname{rk}_{P}(F)\) be the one-point-extension rank of a marked induced substructure \(F\subseteq P\), computed relative to \(\mathcal P\), and let \(\operatorname{rk}(P)=\operatorname{rk}_{P}(\varnothing)\).

**Theorem.** Every finite \(P\in\mathcal P\) with \(\operatorname{rk}(P)\ge3\) has at least \(21\) points. At size \(21\), exactly
\[
\boxed{(16\cdot180)^4=68\,797\,071\,360\,000}
\]
nonisomorphic structures attain rank at least three, and **all have rank exactly three**. Equivalently, this counts the normalized permutations of length \(21\) with one-point-extension rank three.

There is an explicit structural parametrization: the distinguished central point divides a minimal structure into four quadrants containing five points each; each quadrant has one of \(16\) five-point internal patterns, and each of the four independent interleavings of two adjacent quadrant groups is one of \(180\) allowed length-ten binary words. These choices are bijective with all minimum hosts.

## Assumptions and scope

A finite permutation of length \(n\) represents the structure on \(\{1,\ldots,n\}\) where the first named order is the natural order on positions and the second named order sorts the distinct values \(\pi(1),\ldots,\pi(n)\). Embeddings preserve and reflect **both** orders, and the class includes all possible finite permutations (not a pattern-avoidance subclass). Isomorphisms of two-order structures are rigid and normalized length-\(n\) permutations parametrize their isomorphism types.

For a finite marked set \(F\), one-point-extension types correspond exactly to the \((|F|+1)^2\) open insertion cells in the rectangle grid cut by the two ordered lists of marked coordinates. A type is realized by a point of the host outside \(F\) lying in its cell. The successor rank is defined by
\[
\operatorname{rk}_P(F)\ge k+1\quad\Longleftrightarrow\quad
\text{each one-point insertion type over }F\text{ has a realization }v
\text{ with }\operatorname{rk}_P(F\cup\{v\})\ge k.
\]
This is a finite-rank statement, not a classification of first-order quantifier-rank types or of countable permutation structures.

## Proof

**Step 1 — the two successive type conditions.** A marked pair \(\{a,b\}\) has rank at least one exactly when **all nine** of the \(3\times3\) insertion cells determined by the two positions and two values contain an unmarked point. By applying the recursive definition twice more,
\[
\operatorname{rk}(P)\ge3
\quad\Longleftrightarrow\quad
\exists a\ \forall Q\in\{\mathrm{SW},\mathrm{NW},\mathrm{SE},\mathrm{NE}\}\ \exists b_Q\in Q(a)
\quad\text{such that all nine cells for }\{a,b_Q\}\text{ are occupied}.
\]
Here \(Q(a)\) denotes an open quadrant relative to \(a\). This equivalence uses no probabilistic or numerical assumption.

**Step 2 — the sharp lower bound.** Fix \(a\) and witnesses \(b_Q\) as in Step 1. For \(b_{\mathrm{NE}}\), the northeast quadrant of \(a\) contains \(b_{\mathrm{NE}}\) and at least one point in each of the four open subquadrants obtained by cutting this northeast quadrant at \(b_{\mathrm{NE}}\). They are five distinct points. The same argument after reflecting coordinates applies to each of the other three quadrants of \(a\). The four quadrants are disjoint; including \(a\), \(|P|\ge1+4\cdot5=21\).

**Step 3 — rigidity at equality.** Suppose \(|P|=21\) and \(\operatorname{rk}(P)\ge3\). Each quadrant of \(a\) has exactly five points, so \(a\) occupies the eleventh position in **both** orders. Consequently \(a\) is unique. In each quadrant \(Q\), the witness \(b_Q\) is third in that quadrant's local first and second orders, and each of its four local subquadrants has exactly one of the other four points. Hence \(b_Q\) is uniquely determined. A five-point permutation of this kind has exactly \(16\) possibilities: two assignments of the left local positions to lower/upper values, two for the right positions, and independent two-way assignments of the two lower and two upper values.

For each of the four adjacent pairs of quadrants along a common side of \(a\), the remaining nine-cell conditions reduce to one interleaving constraint. Call the five coordinate values from the first quadrant \(A_1<\cdots<A_5\) and those from the second \(B_1<\cdots<B_5\). The two corresponding witness pairs require precisely
\[
B_1<A_3<B_5\quad\text{and}\quad A_1<B_3<A_5.
\]
There are four independent interleavings of this form: left-side horizontal, right-side horizontal, upper-side vertical, and lower-side vertical. The opposite quadrant automatically supplies the remaining single insertion cell for each witness pair. Thus no other constraints are needed.

**Step 4 — enumeration.** There are \(\binom{10}{5}=252\) interleavings of five \(A\)'s and five \(B\)'s. Exactly \(42\) violate the first inequality (\(21\) with the third \(A\) before the first \(B\), and \(21\) with it after the fifth \(B\)); symmetrically \(42\) violate the second. Exactly \(12\) violate both: the two possible cross-order arrangements each have \(\binom42=6\) realizations. Therefore
\[
L=252-42-42+12=180.
\]
Every combination of four local five-point patterns and four permitted interleavings determines a unique normalized permutation of length \(21\). Conversely, Step 3 extracts these eight choices uniquely from every minimum rank-at-least-three host. Hence the exact count is \(16^4 L^4=(2880)^4=68\,797\,071\,360\,000\). Since \(L>0\), such hosts exist, proving sharpness.

**Step 5 — exact rank at the minimum.** For a minimum host, in each local quadrant exactly one point lies strictly beyond its centre \(b_Q\) in both oriented coordinate directions. Call it \(z_Q\). For the pair \(\{a,b_Q\}\), this extreme outer insertion cell has **only** \(z_Q\) as a realization. After adding \(z_Q\), the open cell between \(b_Q\) and \(z_Q\) in both oriented coordinates is empty: it lies inside the same outer subquadrant, whose only point was \(z_Q\). Thus \(\operatorname{rk}_{P}(\{a,b_Q,z_Q\})=0\), and \(\operatorname{rk}_{P}(\{a,b_Q\})=1\). Any witness of pair rank at least one in that quadrant must be its unique centre \(b_Q\). Hence \(\operatorname{rk}_{P}(\{a\})=2\). The only possible rank-three anchor is the unique eleventh-in-both-orders point \(a\), so \(\operatorname{rk}(P)=3\).

## Verification

The standalone Python file `checker.py` independently implements insertion-cell coverage and the three-round recursive game, without using the product formula as its decision rule. It enumerates the \(120\) local five-point patterns to obtain \(16\), the \(252\) binary interleavings to obtain \(180\), and tests \(250\) randomly generated extremal structures. Each generated structure passes the direct game criterion; every one of its \(21\) single-point deletions fails the same criterion. Another \(2100\) randomized subthreshold permutations also fail, as expected. The resulting run prints two `CHECK_OK` lines. These experiments corroborate, but do not replace, the all-size proof above. To run: `python3 checker.py`.

A concrete normalized example (values shown in first-order position order) is
\[
(15,21,7,4,17,5,19,2,10,14,11,13,9,18,3,16,12,6,1,8,20).
\]

## Relationship to prior work

The one-point-extension rank is defined in López-Callejas and Navarro-Castillo (2026). Their general rank theory covers all hereditary relational classes, and their explicit finite-order calculation concerns **one** linear order: it does not yield the twenty-one-point minimum or its exact census for **two independent** linear orders. The associated structure class is the classical permutation Fraïssé class, as also used by Snowden (2024), whose measured invariant is different. Published rank-two first-order classifications of finite permutations and two-order local-type saturation results likewise do not imply a three-level **one-point-extension minimax** bound. The overlapping terminology “rank three” is not evidence of the same rank notion.

## Limitations

The result concerns finite structures with precisely two named linear orders and the third finite level of the Kubiś–Shelah-style extension rank. It does not compute higher levels, does not classify countable hosts, and does not assert a new rank theory in general. The original rank definition and the class of permutations are prior concepts. Historical priority of the sharp threshold and census has not been independently audited; the comparisons described in the review do not establish uniqueness in all literature.

## References

- C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, first posted 2026-04-15, https://arxiv.org/html/2604.14461v1 .
- A. Snowden, *The thirty-seven measures on permutations*, arXiv:2404.08775, first posted 2024-04-12, https://arxiv.org/abs/2404.08775 . Distinct invariants; cited for the finite two-order structure class.
