# Sharp ground-set visibility in triangular Johnson graphs

## Finding

Let \(T_n=J(n,2)=L(K_n)\) for each integer \(n\ge3\): the vertices are the two-element subsets of an \(n\)-element ground set, and two distinct vertices are adjacent precisely when their underlying pairs intersect. Work in the pure simple-graph signature with equality and one adjacency relation, without counting quantifiers. Write \(G\equiv_{\mathrm{FO}^{k}}H\) for agreement on every first-order sentence using at most \(k\) reusable variable names, with no quantifier-depth restriction.

**Theorem (sharp two-per-pebble cutoff).** For every \(k\ge2\) and \(n,m\ge3\),
\[
T_n\equiv_{\mathrm{FO}^{k}}T_m
\quad\Longleftrightarrow\quad
\min\{n,2k\}=\min\{m,2k\}.
\]
For \(k=1\), all graphs in the family have the same theory. Consequently, at each \(k\ge2\) exactly \(2k-2\) distinct \(k\)-variable theories occur. The representative of minimum order for the common tail theory is \(T_{2k}\); every smaller parameter \(3\le n<2k\) represents a separate theory. The largest order of a smallest representative is exactly \(\binom{2k}{2}\). The least variable width that distinguishes \(T_n\) from every nonisomorphic member of this family is \(\lfloor n/2\rfloor+1\). The hierarchy is strict at every transition from width one onward.

Equivalently, every \(\mathrm{FO}^{k}\) sentence, regardless of its quantifier depth, has a constant truth value on the tail \(T_{2k},T_{2k+1},\ldots\); the cutoff \(2k\) is optimal as a uniform bound.

## Assumptions and scope

All structures are finite, nonempty, loopless, undirected graphs, and all ground sets are unlabelled up to bijection. All quantification is over the graph's vertices, **not** over hidden ground-set elements. The distinction and minimality claims are relative to the specified one-parameter family, not to arbitrary graphs. The graph \(T_n\) has \(\binom n2\) vertices; distinct parameters yield nonisomorphic graphs.

## Proof

**1. Permanent back-and-forth above the cutoff.** Fix \(k\ge2\) and \(n,m\ge2k\). In the ordinary \(k\)-pebble game, maintain a bijection between the ground elements used as endpoints of the currently pebbled two-subsets in the two graphs, carrying each pebbled two-subset to its matched two-subset. This is stronger than preserving the atomic graph diagram.

When a pebble is moved, first discard it on both sides and restrict that endpoint bijection to the endpoints of the other, at most \(k-1\), pebbled graph vertices. Their union has at most \(2(k-1)\) ground elements. A newly selected two-subset on the Spoiler side has zero, one or two endpoints in that union. Map any old endpoints by the maintained bijection and choose distinct fresh endpoints on the Duplicator side for the remaining zero, one or two positions. At least \(2k-2(k-1)=2\) unused ground elements are always available, on either side of the game. The endpoint map extends to a bijection of the new used supports, so it preserves equality of pebbled two-subsets and whether they meet. Thus Duplicator can maintain a partial isomorphism through arbitrarily many rounds. By the finite-variable pebble-game theorem, the two graphs agree on every \(\mathrm{FO}^{k}\) sentence.

**2. Separating each parameter below the cutoff.** Suppose \(3\le n<m\) and \(n<2k\). Put \(t=n+1\) and \(r=\lceil t/2\rceil\), so \(4\le t\le2k\) and \(r\le k\). Consider existential sentences using distinct graph vertices \(x_1,\ldots,x_r\), with pairwise inequalities explicitly imposed.

If \(t=2r\) is even, require the chosen vertices to be pairwise nonadjacent. Under the two-subset interpretation they are \(r\) disjoint edges and use exactly \(2r=t\) ground elements. This pattern exists in \(T_m\) but not \(T_n\).

If \(t=2r-1\) is odd, require that among the chosen vertices the **only** adjacent pair is \(x_1,x_2\), all other pairs being nonadjacent. The two underlying edges for \(x_1,x_2\) share exactly one endpoint; all other edges are disjoint from one another and from both of these. The pattern therefore uses exactly \(3+2(r-2)=2r-1=t\) distinct ground elements. Again it exists in \(T_m\) but not \(T_n\). Every pattern is an existential \(\mathrm{FO}^{k}\) sentence because \(r\le k\). These two cases distinguish any smaller parameter from a larger one whenever the smaller lies below \(2k\).

**3. Counting and width consequences.** The parameters \(3,\ldots,2k-1\) yield \(2k-3\) individual theories, and all parameters \(n\ge2k\) yield one additional theory, totaling \(2k-2\). The smallest graph in the tail class is \(T_{2k}\), of order \(\binom{2k}{2}\). To isolate \(T_n\) within the family, precisely the widths satisfying \(2k>n\) suffice, whose minimum is \(\lfloor n/2\rfloor+1\). For each \(k\ge2\), the pair \(T_{2k},T_{2k+1}\) agrees at width \(k\) but separates at width \(k+1\). Width one cannot distinguish any nonempty simple graphs with the same diagonal adjacency, so \(T_3,T_4\) witness strictness from width one to two.

## Verification

The included `verify_orbit_game.py` exhaustively enumerates the isomorphism orbits of ordered \(k\)-tuples of graph vertices under permutations of the underlying ground set, constructs all one-coordinate pebble-replacement orbits, and iteratively refines atomic diagram colors by the sets of successor colors. Its finite fixed point is the unlimited-round \(k\)-pebble equivalence on those finite samples. It compares every pair among six ground-set orders at each of widths two, three and four, checking \(45\) cross-order comparisons with no discrepancies. The largest run has \(715\) orbit positions across its six graphs, and refinement stabilizes after four rounds.

The independent program `verify_witness.py` searches actual collections of two-subsets for the even and odd separating patterns, checking their nonexistence on \(t-1\) ground points and existence on \(t\) for every \(4\le t\le9\). It passes all \(12\) checks. The expected recorded outputs are in `verify_orbit_game.out` and `verify_witness.out`. Run `python3 verify_orbit_game.py` and `python3 verify_witness.py` from a directory containing these four files, with Python 3 and no third-party libraries. Finite computations do not replace the general proof above.

## Relationship to prior work

The underlying graphs are standard triangular/Johnson graphs. Pikhurko and Verbitsky's *Logical Complexity of Graphs: A Survey* (first public version 2010-03-25) develops the graph-width and pebble-game setting, but the inspected sections and term search did not present the present family-specific equivalence cutoff. Grohe's *Fixed-Point Definability and Polynomial Time on Chordal Graphs and Line Graphs* (first public version 2010-01-14) studies a stronger counting-and-fixed-point logic for broad graph classes, not this exact counting-free variable-width threshold. Ganesan's *On the Automorphism Group of a Johnson Graph* (2014) treats automorphisms, explicitly notes that \(J(n,2)\) is the complete-graph line graph, and does not establish the logical classification. Dabrowski and Moss's 2000 distance-extension theorem targets \(J(n,3)\) and is not an implication of the claimed \(J(n,2)\) two-subset result.

The rook graphs \(L(K_{a,b})\) provide a related but different two-coordinate incidence family; their finite-variable classification does not determine that of \(L(K_n)\), where unordered two-subsets and their intersection patterns govern pebble extension. No claim of exhaustive historical priority is made.

## Limitations

The theorem is relative to \(\{J(n,2):n\ge3\}\) and does not establish the width needed to define these graphs among **all** finite graphs. It does not classify the Johnson graphs \(J(n,r)\) for \(r\ge3\), counting logic, fixed-point logic, or signatures naming ground elements. The primary novelty uncertainty is whether a general, previously published substitution/pebble-extension theorem already implies the sharp cutoff without naming it. An independent mathematical audit has not been performed.

## References

1. M. Grohe, *Fixed-Point Definability and Polynomial Time on Chordal Graphs and Line Graphs*, arXiv:1001.2572, first posted 2010-01-14, https://arxiv.org/abs/1001.2572.
2. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, first posted 2010-03-25, https://arxiv.org/abs/1003.4865.
3. A. Ganesan, *On the Automorphism Group of a Johnson Graph*, arXiv:1412.5055, first posted 2014-12-09, https://arxiv.org/abs/1412.5055.
4. A. Dabrowski and L. S. Moss, *The Johnson Graphs Satisfy a Distance Extension Property*, Combinatorica 20 (2000), 295–300, DOI 10.1007/S004930070027 (abstract inspected; full text not verified).
