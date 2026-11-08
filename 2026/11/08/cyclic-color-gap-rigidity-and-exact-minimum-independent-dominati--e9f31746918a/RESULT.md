# Cyclic color-gap rigidity and exact minimum independent-domination multiplicities in \(C_n\times K_q\)

## Finding

For every pair of integers \(n\ge 6\) and \(q\ge3\), let \(G_{n,q}=C_n\times K_q\) denote the **direct (categorical/tensor) graph product**, not the Cartesian product. Put \(k=\lfloor n/3\rfloor\) and \(r=n-3k\in\{0,1,2\}\). The already-known independent domination number is \(i(G_{n,q})=\lceil2n/3\rceil\). We classify **all** independent dominating sets attaining that minimum and obtain their exact multiplicity:

\[
\boxed{
M_{n,q}=\frac{n}{k}\binom{k+r-1}{r}
\left((q-1)^k+(-1)^k(q-1)\right).
}
\]

The fraction is an integer after multiplication by the binomial coefficient. Equivalently, the geometric factor is \(3\) if \(n=3k\), \(n\) if \(n=3k+1\), and \(n(k+1)/2\) if \(n=3k+2\). The second factor is the number of proper \(q\)-colorings of a cyclic sequence of \(k\) blocks; at \(k=2\), the two blocks simply have distinct colors.

Precisely, every minimum independent dominating set has \(k\) empty cycle-coordinate layers. Read cyclically between consecutive empty layers; each intervening run has length at least two, contains exactly one chosen vertex in each layer, and uses a **constant** \(K_q\)-coordinate color. The colors of neighboring runs differ. Conversely, each such gap-and-color configuration is a minimum independent dominating set. The positive-run lengths are exactly \(2+e_1,\ldots,2+e_k\), where all \(e_j\ge0\) and \(\sum_j e_j=r\).

For \(q=3\), the multiplicities at \(n=6,7,8,9\) are respectively \(18,42,72,18\). In particular, the already-known minimum size does not determine a constant number of extremizers: the number of distinct minimum configurations depends exponentially on the compressed color-cycle length.

## Assumptions and scope

All graphs are finite and simple. The cycle coordinates are labelled by \(\mathbb Z/n\mathbb Z\) and the complete-graph coordinates by \([q]=\{1,\ldots,q\}\). Distinct vertices \((i,a)\) and \((j,b)\) of \(G_{n,q}\) are adjacent exactly when \(j=i\pm1\pmod n\) and \(a\ne b\). A set is *independent dominating* if no pair of its vertices is adjacent and every omitted vertex has a selected neighbor; equivalently, it is an inclusion-maximal independent set. The independent domination number is the smallest cardinality among such sets. The formula counts labelled vertex subsets, without quotienting by cycle rotations, reflections or color permutations.

Let \(X_i=\{(i,a):a\in[q]\}\), let \(S_i=S\cap X_i\), and set \(w_i=|S_i|\). Indices of layers are cyclic throughout.

## Proof

**1. A three-layer lower bound.** Every dominating set \(S\) satisfies
\[
  w_{i-1}+w_i+w_{i+1}\ge 2\qquad(i\in\mathbb Z/n\mathbb Z).
\]
Indeed, if the three layers contain no selected vertex, the entire middle layer is undominated. If they contain a single selected vertex in the middle layer, any other vertex of that layer is undominated, because adjacency changes the cycle coordinate. If the only selected vertex is in a neighboring layer and has color \(a\), the middle vertex with color \(a\) is undominated. These cases exhaust totals at most one, and use \(q\ge3\). Summing the inequalities over all cycle coordinates gives \(3|S|\ge2n\) and hence \(|S|\ge\lceil2n/3\rceil\).

**2. Sharpness.** Let \(k=\lfloor n/3\rfloor\ge2\) and \(r=n-3k\). On the labelled cycle, place \(k\) empty layers and, between consecutive empty layers, \(k\) positive runs of respective lengths \(2+e_j\) with nonnegative \(e_j\) summing to \(r\). Assign a constant color to each run, choosing colors unequal across every intervening empty layer. This cyclic coloring exists for every \(q\ge3\) and \(k\ge2\): for two runs choose any two distinct colors, and for three or more use a proper coloring of the ordinary cycle. Select the unique vertex of that color in each positive layer. Two selected vertices in adjacent layers have the same color and therefore are nonadjacent in the direct product. Every omitted vertex in a positive layer has a color different from the run color and hence a selected neighbor in another layer of that same run; every vertex in an empty layer has two selected neighbors in neighboring layers of distinct colors, one of which differs from its own color. Thus the selection is independent dominating with \(n-k=\lceil2n/3\rceil\) vertices.

**3. Full layers cannot occur in a minimum set.** Fix a minimum independent dominating set \(S\). Define the nonnegative window excess
\[
  \delta_i=w_{i-1}+w_i+w_{i+1}-2.
\]
By Step 1 and sharpness,
\[
  \sum_i\delta_i=3\lceil2n/3\rceil-2n\in\{0,1,2\}.
\]
First, a partial occupied layer of cardinality between \(2\) and \(q-1\) is impossible in *any* independent dominating set: any selected vertex in an adjacent layer would be adjacent to at least one of two selected distinct-color vertices in this layer; hence both adjacent layers would be empty. But any missing vertex in the partially occupied layer would then lack a selected neighbor. It follows that every occupied layer has cardinality either one or \(q\). If a layer is full, then it has \(q\ge3\) selected vertices and each of the three distinct windows containing it has excess at least \(q-2\ge1\), contradicting \(\sum_i\delta_i\le2\). Consequently, every layer of a minimum set is either empty or a singleton.

**4. Exact shape of the singleton pattern.** An empty layer with singleton neighbors must have *both* neighbors occupied, and their colors must differ: otherwise the vertex with their common color (or an arbitrarily chosen color if a neighbor is empty) would lack a selected neighbor. Hence no two empty layers are consecutive. Furthermore a singleton layer cannot have both neighbors empty, because its other \(q-1\) vertices would not be dominated. Thus every positive run between empty layers has length at least two. Adjacent singleton layers must have equal colors by independence, so each run is monochromatic. The neighboring runs must have different colors by the empty-layer condition. Since a minimum set has \(n-k\) singleton layers, it has exactly \(k\) empty layers. The length of its \(j\)th positive run is \(2+e_j\) with \(e_j\ge0\); adding the \(k\) empty layers yields \(\sum_j e_j=n-3k=r\). This proves necessity; Step 2 proves sufficiency.

**5. Counting without rotation quotient.** Mark one of the \(k\) empty layers as distinguished. It may have any of \(n\) cycle positions. The ordered cyclic list of excess run lengths is a weak composition of \(r\) into \(k\) parts, counted by \(\binom{k+r-1}{r}\). Each unmarked configuration has exactly \(k\) choices of distinguished empty layer, so the number of *labelled* empty-layer configurations is
\[
  \frac n k\binom{k+r-1}{r}.
\]
The number of ways to color the \(k\) positive runs so neighboring runs have different colors is
\[
  c_k(q)=(q-1)^k+(-1)^k(q-1).
\]
For \(k\ge3\), this follows by taking the trace of the \(k\)th power of the matrix with zeros on the diagonal and ones elsewhere, which has eigenvalues \(q-1\) once and \(-1\) with multiplicity \(q-1\). For \(k=2\), both cyclic adjacency constraints reduce to the single distinctness requirement, and the same expression equals \(q(q-1)\). The chosen colors and run lengths uniquely determine the selected vertex set. Multiplying the two factors proves the formula and the complete classification. \(\square\)

## Verification

The included script `scripts/verify.py` constructs the labelled direct-product edges from the definition and tests independence and domination on vertex subsets, without using the layer-classification lemma as its acceptance criterion. It exhaustively examines every subset of size at most the claimed optimum in seven parameter cases: \((n,q)=(6,3),(7,3),(8,3),(9,3),(6,4),(7,4),(6,5)\). Across these cases it tests \(786909\) subsets, finds no independent dominating set below the claimed minimum, and matches every claimed minimum-set multiplicity. It also evaluates the closed formula on \(162\) additional integer parameter pairs; these evaluations alone are arithmetic checks, not independent enumeration. Run from the artifact directory with `python3 scripts/verify.py` using Python 3 and its standard library only.

The verified console result begins with `VERIFY_OK` and ends with `literal_independent_dominating_test=PASS minimum_multiplicities=PASS`. The finite checks corroborate but do not establish the theorem for unbounded parameters; Steps 1–5 provide the proof.

## Relationship to prior work

Kuenzel and Rall, *On independent domination in direct products*, arXiv:2203.12397 (first public 23 March 2022), give the scalar independent domination number for \(C_n\times K_q\) and \(P_n\times K_q\) in their Proposition 6, and describe a general weak-partition framework for all maximal independent sets in products with a complete graph. Both are prior coverage, not new claims here. The earlier paper *On well-covered direct products*, arXiv:1901.03218, contains the general layer-size lemma. Bakal and Mane, arXiv:2506.11865, independently provide a three-column domination lower bound and recover scalar domination values for these products. Jahari and Alikhani, arXiv:1808.07369, develop independent-domination polynomials for other graph operations and families. The present theorem derives a **closed count and full minimum-set classification**, not a new scalar minimum and not an enumeration of all maximal independent sets of all cardinalities.

## Limitations

The result is established only for \(n\ge6\) and \(q\ge3\). Smaller cycle lengths have distinct boundary behavior; the bipartite-double-cover case \(q=2\) is not included. The count distinguishes labelled sets rather than symmetry orbits. Although the accessible literature checked does not give this exact count and rigidity theorem, there remains a risk that an equivalent formula is present under a different terminology, or that it has been recorded as an implicit special case of a more general enumeration. No independent mathematical audit has been performed.

## References

1. K. Kuenzel and D. F. Rall, *On independent domination in direct products*, arXiv:2203.12397, first public 2022-03-23; journal DOI 10.1007/s00373-022-02600-0. https://arxiv.org/abs/2203.12397
2. K. Kuenzel and D. F. Rall, *On well-covered direct products*, arXiv:1901.03218, first public 2019-01-10. https://arxiv.org/abs/1901.03218
3. D. M. Bakal and S. A. Mane, *The domination and secure domination numbers of direct product of cliques with paths and cycles*, arXiv:2506.11865, first public arXiv 2025-06-13. https://arxiv.org/abs/2506.11865
4. S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369, first public 2018-08-21. https://arxiv.org/abs/1808.07369
