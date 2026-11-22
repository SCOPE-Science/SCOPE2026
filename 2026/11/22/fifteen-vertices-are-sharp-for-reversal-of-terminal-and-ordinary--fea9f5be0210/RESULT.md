# Fifteen vertices are sharp for reversal of terminal and ordinary mean tree distances

## Finding
For an unweighted undirected tree \(T\) of order \(n\ge2\), let \(L(T)\) be its set of degree-one vertices, \(\ell=|L(T)|\), and
\[
\Delta(T)=\frac{\sum_{\{u,v\}\subseteq L(T)}d_T(u,v)}{\binom{\ell}{2}}-\frac{\sum_{\{u,v\}\subseteq V(T)}d_T(u,v)}{\binom{n}{2}}.
\]
Every tree of order \(2\le n\le14\) satisfies \(\Delta(T)\ge0\). The smallest possible order with \(\Delta(T)<0\) is \(15\). Exactly three unlabelled trees of that order have \(\Delta(T)<0\): the brooms \(B_{7,7}\), \(B_{8,6}\), and \(B_{9,5}\), with respective differences \(-1/10\), \(-4/45\), and \(-2/105\). The uniquely most negative 15-vertex tree is \(B_{7,7}\).

## Assumptions and scope
The graphs are finite, simple, undirected, connected, unweighted trees. Distinct unordered vertex pairs are sampled uniformly, separately for the leaf sample and the whole-vertex sample; the means are **not** expectations obtained by first choosing a random tree. A broom \(B_{b,p}\) has a center vertex joined to \(b\) distinct pendant leaves and to a simple path of \(p\) edges, all meeting only at the center; it has \(n=b+p+1\) vertices and \(\ell=b+1\) leaves for \(b\ge2,p\ge2\). The sharp minimality is over all unlabelled trees and all orders from two through fifteen, with no bounded-degree restriction.

## Proof
For each edge \(e\), removal divides the vertices into sides of cardinalities \(s_e\) and \(n-s_e\), with \(a_e\) and \(\ell-a_e\) leaves on the two sides. Each pair's unique connecting path crosses \(e\) exactly when its endpoints lie on different sides, hence
\[
W(T)=\sum_e s_e(n-s_e),\qquad W_L(T)=\sum_e a_e(\ell-a_e).
\]
Thus an exact sign test uses only integer arithmetic:
\[
\operatorname{sgn}\Delta(T)=\operatorname{sgn}\bigl(n(n-1)W_L(T)-\ell(\ell-1)W(T)\bigr).
\]
The supplied `verify.py` enumerates **each unlabelled free tree** of each order from three through fifteen via NetworkX's `nonisomorphic_trees`, computes the two edge-cut sums exactly and compares using rational numbers. The known counts of nonisomorphic free trees at orders 3 through 15 are, respectively,
`1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741`.
The program asserts every count and every minimum; it finds no negative difference at orders three through fourteen and exactly three negative isomorphism classes at fifteen. At order two the two samples coincide, so \(\Delta(T)=0\). Every negative fifteen-vertex representative is checked for isomorphism with precisely one of the three stated brooms.

For an independent closed-form verification of the three witnesses, the brooms have
\[
W_L(B_{b,p})=b(b+p),\qquad W(B_{b,p})=b(n-1)+\sum_{j=1}^{p}j(n-j),\quad n=b+p+1.
\]
Indeed, each of the \(b\) short-arm edges separates one vertex, and the long-arm edges separate successively \(j\) from \(n-j\) vertices. The leaf-pair sum counts \(\binom b2\) short-short pairs at distance two and \(b\) short-long pairs at distance \(p+1\). Substitution gives, in order \((b,p)=(7,7),(8,6),(9,5)\),
\[
(n,\ell,W,W_L)=(15,8,378,98),(15,9,336,112),(15,10,296,126).
\]
Dividing by the corresponding pair counts proves the three displayed differences. Exact enumeration shows that no other 15-vertex tree reverses the inequality and that \(-1/10\) is uniquely smallest at this order.

## Verification
Run `python verify.py` using Python 3.9 or newer with NetworkX 3.x. The checker asserts the entire sequence of unlabelled-tree totals, every minimal difference through order fifteen, exactly three reversing classes at order fifteen, each class's broom isomorphism type, all rational indices, and a second direct all-pairs shortest-path calculation for each witness. It prints `EXHAUSTIVE_TREE_CENSUS_PASS` on successful completion. The exhaustive result is conditional on the standard complete nonisomorphic-tree generator's documented enumeration; the code and all expected counts are supplied, so the finite classification is reproducible. There is no asymptotic or infinite-order claim.

## Relationship to prior work
Lundblad and Wagner (arXiv:2611.16674v1, public 2026-11-12) study normalized ordinary and terminal Wiener indices of random trees. Their introduction explicitly notes that leaves need not be farther apart on average in every deterministic tree; their theorems concern random-tree distributions rather than the **smallest unweighted deterministic counterexample** or the complete 15-vertex classification. Earlier work introduces and studies the terminal Wiener index but does not, in the checked sources, establish this sharp finite boundary. An earlier 2026 conference version of their work concerns external path length, rather than the complete 2026 November terminal-Wiener comparison. This result is a sharp quantitative boundary for the deterministic phenomenon; priority outside inspected sources remains unverified.

## Limitations
The sharpness assertion is finite (orders at most fifteen); it does not characterize all later reversing trees, weighted trees, or other leaf-selection rules. Completeness uses the independent mathematical guarantee of the standard nonisomorphic-tree generator, rather than an accompanying hand-derived classification of all 7741 shapes at order fifteen. Independent mathematical audit has not been performed. Historical bibliographic priority has not been exhaustively established.

## References
- J. Lundblad and S. Wagner, *The External Path Length and Terminal Wiener Index in Random Trees*, arXiv:2611.16674v1 (2026-11-12), https://arxiv.org/html/2611.16674v1.
- J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, LIPIcs AofA 2026, published 2026-07-13, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.AofA.2026.2.
- NetworkX documentation, `nonisomorphic_trees` (generation of nonisomorphic free trees), https://networkx.org/documentation/stable/reference/generated/networkx.generators.nonisomorphic_trees.nonisomorphic_trees.html.
