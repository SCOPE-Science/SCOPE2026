# Depth-two forest statistics determine every vertex degree of Catalan matroid polytopes

## Finding

For every integer \(n\ge 1\), form the canonical Catalan matroid base polytope \(P_n\subset\mathbb R^{2n}\) as the convex hull of the incidence vectors of up-step positions of all Dyck words of semilength \(n\). Let \(G_n\) be its ordinary, undirected one-skeleton. Identify a Dyck word \(w\) with its rooted ordered forest of \(n\) matched parenthesis pairs. Let \(s_1,\dots,s_k\) be the numbers of nodes in the full subtrees rooted at the children of depth-one roots (the depth-two subtree sizes). Then the exact polytope vertex degree is

\[
\boxed{\deg_{G_n}(w)=\binom n2+\sum_{i=1}^k\binom{s_i}{2}.}
\]

Put \(C_j=\binom{2j}{j}/(j+1)\) and define the excess-degree polynomial
\[
F_n(q)=\sum_{w\in\mathrm{Dyck}_n}q^{\deg_{G_n}(w)-\binom n2},\qquad F_0(q)=1.
\]
Its full two-variable generating function and coefficient recurrence are
\[
H(z,q)=\sum_{s\ge1}C_{s-1}z^s q^{\binom s2},\qquad
\sum_{n\ge0}F_n(q)z^n=\frac{1-H(z,q)}{1-z-H(z,q)},
\]
\[
F_n(q)=F_{n-1}(q)+\sum_{s=1}^{n-1}C_{s-1}q^{\binom s2}F_{n-s}(q)\quad(n\ge1).
\]

For every \(n\ge1\), the minimum degree is \(\binom n2\), attained exactly by the \(2^{n-1}\) Dyck paths of height at most two. For \(n\ge3\), the maximum is \((n-1)^2\), attained exactly by words \(UUQDD\), where \(Q\) runs over all Dyck words of semilength \(n-2\); there are \(C_{n-2}\) such vertices. At \(n=1,2\), maximum and minimum coincide and every vertex is simultaneously extremal.

## Assumptions and scope

A Dyck word has \(n\) up steps \(U\), \(n\) down steps \(D\), and every partial height (\(U\mapsto+1\), \(D\mapsto-1\)) is nonnegative. Its incidence vector is the length-\(2n\) zero-one vector of its \(U\) positions. Different Dyck words give different vertices of \(P_n\). Two vertices of any matroid base polytope are adjacent precisely when their bases differ by one element, i.e. their words differ by exchanging one \(U\) and one \(D\) (see An–Jung–Kim). The forest is the unique usual balanced-parenthesis forest, with depth-one nodes as top-level roots. Each \(s_i\) includes the depth-two child and all its descendants. Isolated top-level roots contribute no \(s_i\). The symbols \(q,z\) are formal variables; every coefficient is a finite polynomial.

## Proof

**Local exchange lemma.** For an earlier \(U\) at position \(a\) and a later \(D\) at position \(b\), exchanging them lowers every original partial height at positions \(a,\dots,b-1\) by exactly two. It yields another Dyck word exactly when all those original heights are at least two. Conversely, for an earlier \(D\) and a later \(U\), exchanging the steps raises the affected partial heights by two and is always admissible. These conditions directly follow by comparing the two partial-sum sequences and show that every admissible unequal-symbol exchange gives a distinct neighbor.

Label each matched \(UD\) pair by its forest node. For two *distinct* nodes, there are precisely two candidate exchanges of one opening with the other closing. They have the following complete classification:

- If one node is a depth-one root and the other is its descendant, neither exchange is valid: one lowering interval reaches height one, and the other contains a height-one endpoint.
- If both nodes belong to the same subtree rooted at a depth-two node, both exchanges are valid. In the nested case, both lowering intervals remain at height at least two; in the disjoint case the reverse-order exchange raises heights and the other lowering interval also stays above level one.
- In every other distinct-node pair exactly one exchange is valid. For disjoint nodes the swap of the earlier closing with the later opening always raises heights, while the other interval touches height at most one unless both nodes share a depth-two subtree. For nested nodes not covered by the first case, the outer node has depth at least two and the pair shares a depth-two ancestor, so this case cannot arise.

A node's own matched opening and closing can be exchanged exactly when the node has depth at least two. If there are \(r\) depth-one roots, there are \(n-r\) such self-node exchanges. There are also exactly \(n-r\) pairs consisting of a root and one of its descendants (each nonroot has one root ancestor). Every pair of *distinct* nodes supplies a baseline one exchange, except those \(n-r\) root–descendant pairs which supply zero, and pairs internal to each depth-two subtree which supply two instead. Hence the total is
\[
\binom n2-(n-r)+\sum_i\binom{s_i}{2}+(n-r)=\binom n2+\sum_i\binom{s_i}{2}.
\]

**Generating function.** A depth-two primitive subtree of size \(s\) consists of its opening/closing pair surrounding an arbitrary Dyck word of semilength \(s-1\); there are \(C_{s-1}\) possibilities. It independently contributes weight \(z^s q^{\binom s2}\). Consequently an ordered sequence of these subtrees has series \(1/(1-H)\), and a whole root component has series \(z/(1-H)\). A general Dyck forest is an ordered sequence of root components, so its series is \(1/(1-z/(1-H))=(1-H)/(1-z-H)\). Multiplying out gives \((1-z-H)F=1-H\). Comparing coefficients yields the displayed recurrence, where the extra term from \(-H\) cancels the \(s=n\) term on the left. This is an identity of formal power series with constant term one.

**Extrema.** Each term \(\binom{s_i}{2}\) is nonnegative, and it vanishes exactly when all depth-two subtrees have one node. This means no node lies deeper than level two. Such forests consist of root components \(U(UD)^jD\), for \(j\ge0\), and are counted by the \(2^{n-1}\) compositions of \(n\). Since the depth-two subtrees are disjoint, \(\sum_i s_i\le n-1\); moreover \(\sum_i\binom{s_i}{2}\le\binom{n-1}{2}\). For \(n\ge3\), equality forces exactly one depth-one root and exactly one depth-two subtree of size \(n-1\). The corresponding Dyck word is \(UUQDD\), with arbitrary \(Q\in\mathrm{Dyck}_{n-2}\), so the maximum is \(\binom n2+\binom{n-1}{2}=(n-1)^2\) and there are \(C_{n-2}\) such vertices. For \(n=1,2\) the claimed direct exceptions follow from the same degree identity.

## Verification

The standalone Python 3 standard-library checker `catalan_degree_checker.py` enumerates all \(C_n\) Dyck words for every \(1\le n\le9\). For each word, it (1) recomputes every exchange and tests Dyck feasibility without using the forest formula; (2) parses nested pairs to evaluate the forest formula; and (3) independently derives the excess-degree polynomial by the recurrence. It checks equality of all three degree counts and the extremal counts. It prints `CATALAN_POLYTOPE_DEGREES_EXACT_PASS` on success. For \(n=3,4,5\), it finds respectively \(8,47,244\) undirected polytope edges by summing degrees and dividing by two. The finite enumeration is a cross-check only; the proof covers every positive integer \(n\).

Run with `python3 catalan_degree_checker.py`. No external packages, source downloads, or outside data are required.

## Relationship to prior work

The Dyck-up-step matroid is classical (Ardila). Bidkhori studies lattice-path matroid polytopes and gives aggregate edge-enumeration results; An, Jung and Kim establish the general matroid-polytope adjacency criterion and face/edge enumeration. Cohen, Tetali and Yeliussizov analyze the random-transposition basis-exchange walk and its mixing on Dyck words. The present result refines the aggregate one-skeleton counts to every local vertex degree, its full degree-distribution generating series, and the rigid extremal families. Neither the aggregate count alone nor the global mixing bound implies these evaluated local identities without additional analysis. Searches also considered other degree-refined exchange graphs, but their move rules or underlying polytopes differ.

## Limitations

This theorem concerns the unweighted, undirected one-skeleton of the **ordinary** Catalan matroid base polytope, not the flip graph of triangulations, the Dyck deletion graph, or the one-skeleton of a generalized Catalan matroid. The full degree polynomial is specified by a formal generating function/recurrence rather than a closed elementary coefficient expression. No spectral gap, mixing constant, or novel total-edge formula is asserted. Historical novelty is a best-knowledge comparison, not a proof of first discovery; a non-indexed equivalent of the depth-two forest statistic could exist. The computational check ends at semilength nine.

## References

- Federico Ardila, *The Catalan matroid*, Journal of Combinatorial Theory, Series A (2003), DOI: https://doi.org/10.1016/S0097-3165(03)00121-3.
- Hoda Bidkhori, *Lattice Path Matroid Polytopes*, arXiv:1212.5705 (first posted 2012-12-22), https://arxiv.org/abs/1212.5705.
- Suhyung An, JiYoon Jung and Sangwook Kim, *Facial structures of lattice path matroid polytopes*, arXiv:1701.00362 (first posted 2017-01-02), https://arxiv.org/abs/1701.00362.
- Emma Cohen, Prasad Tetali and Damir Yeliussizov, *Lattice Path Matroids: Negative Correlation and Fast Mixing*, arXiv:1505.06710 (2015), https://arxiv.org/abs/1505.06710.
