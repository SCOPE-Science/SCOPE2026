# Sharp finite-variable classification of rectangular rook graphs

## Finding

For integers \(a,b\ge2\), the rectangular rook graph \(R(a,b)\) has vertex set \([a]\times[b]\), with two distinct vertices adjacent exactly when they share a coordinate. Equivalently, \(R(a,b)=K_a\square K_b=L(K_{a,b})\). All graphs here are finite, nonempty, simple, undirected, and interpreted in the pure adjacency-and-equality signature without counting quantifiers.

For any \(R(a,b)\) and \(R(c,d)\), counting-free \(\mathrm{FO}^{1}\)-equivalence and \(\mathrm{FO}^{2}\)-equivalence hold regardless of the parameters. For every integer \(k\ge3\), with no bound on quantifier depth,

\[
R(a,b)\equiv_{\mathrm{FO}^{k}}R(c,d)
\quad\Longleftrightarrow\quad
\{\!\{\min(a,k),\min(b,k)\}\!\}
=
\{\!\{\min(c,k),\min(d,k)\}\!\}.
\]

The braces denote an unordered pair with multiplicity. Consequently, exactly \(\binom{k}{2}\) different \(\mathrm{FO}^{k}\) theories occur within this family for each \(k\ge3\). Each theory has one smallest-order representative up to graph isomorphism, obtained by truncating both side sizes at \(k\); the greatest order of a smallest representative is \(k^2\). The least variable width needed to distinguish an individual \(R(a,b)\) from all other nonisomorphic members of this family is \(1+\max(a,b)\). The counting-free variable hierarchy is strict on the family at every transition from width two onward.

## Assumptions and scope

A formula of \(\mathrm{FO}^{k}\) may reuse at most \(k\) variable names in arbitrary nested Boolean combinations and first-order quantifiers; quantifier depth is unrestricted. Equivalence means agreement on every such *sentence*, not just formulas of bounded depth. Parameters \(a,b,c,d\) are integers at least two, and \(k\) is a positive integer. The defining-width statement is relative to the class of rectangular rook graphs, not to all finite graphs. No row/column unary predicates, coordinate functions, orders, or counting quantifiers are part of the signature.

## Proof

**Step 1: two-variable collapse.** The one-variable claim follows because all these graphs are nonempty and loopless. For width two, fix any already matched vertex. It has an adjacent vertex because \(a,b\ge2\), and a distinct nonadjacent vertex because both coordinates can be changed. Duplicator therefore responds to each move by preserving equality or inequality and the adjacency or nonadjacency relation to the single other pebble. This is a permanent two-pebble strategy, so the equivalence holds at every finite quantifier depth and hence at unrestricted depth.

**Step 2: the upper implication at width \(k\ge3\).** Suppose the unordered truncated parameter pairs coincide. Interchange the names of the two coordinates in one graph if necessary so that \(\min(a,k)=\min(c,k)\) and \(\min(b,k)=\min(d,k)\). Duplicator maintains a partial bijection between occupied first coordinates, and a second partial bijection between occupied second coordinates, such that corresponding pebbled vertices are obtained by applying these two maps coordinatewise. When Spoiler moves one pebble, first forget that pebble's old position. At most \(k-1\) pebbles remain, so at most \(k-1\) distinct values are occupied on either coordinate axis. Any newly chosen coordinate equals an already occupied value, in which case its paired value is forced, or is fresh. In the fresh case the other axis has a fresh value: if its sizes are below \(k\), they agree exactly; otherwise both sizes are at least \(k\), exceeding the number currently occupied. Independently extend the two partial coordinate maps and place the pebble at the paired coordinate tuple. Equalities of pebbled vertices and the condition that distinct vertices share either coordinate are preserved. Thus this defines a winning strategy for arbitrarily many rounds.

**Step 3: the lower implication.** In \(R(a,b)\), a pairwise nonadjacent set uses pairwise distinct first and second coordinates. Its maximum cardinality is therefore \(\alpha(R(a,b))=\min(a,b)\). Likewise a clique of at least three vertices must occupy one common row or one common column: after choosing two adjacent vertices in the same row (say) but with distinct columns, any third vertex adjacent to both must belong to that row, and the same argument extends to the remaining clique. Hence \(\omega(R(a,b))=\max(a,b)\), including the case where the largest clique has size two. For each \(3\le r\le k\), the existence of an independent \(r\)-set and the existence of an \(r\)-clique are expressed by existential adjacency formulas with exactly \(r\) variables. These formulas recover \(\min(\min(a,b),k)\) and \(\min(\max(a,b),k)\): values below three can only equal two by the standing hypotheses. If the unordered truncated pairs differ, one of these two capped extrema differs and an appropriate width-\(k\) sentence distinguishes the graphs.

**Step 4: enumeration and sharpness.** For \(k\ge3\), the possible canonical truncated parameters are precisely unordered pairs with repetition from \(\{2,3,\ldots,k\}\). They number \(\binom{k}{2}\); their graph orders are products of the parameters, with maximum \(k^2\). The graph's clique and independence numbers recover its two exact parameter values up to interchange, establishing uniqueness and the claimed minimum order. For an individual \(R(a,b)\), all values are seen when \(k>\max(a,b)\), whereas at \(k\le\max(a,b)\) increasing one largest coordinate produces a different but equivalent rook graph. The least relative defining width is therefore \(1+\max(a,b)\). Finally \(R(k,k)\) and \(R(k,k+1)\) agree at width \(k\) but not at width \(k+1\) for \(k\ge3\); \(R(2,2)\) and \(R(2,3)\) separate widths two and three.

## Verification

The standalone file `rook_logic_checker.py` implements the noncounting finite-variable pebble-extension partition of all ordered \(k\)-tuples, refining atomic types by *sets* of possible single-coordinate-replacement types until stabilization. It compares every ordered pair among ten rook graphs with parameters \(2\le a\le b\le5\) at widths two and three, and among six graphs with \(2\le a\le b\le4\) at width four. It reports \(236\) ordered graph comparisons, \(135{,}773\) tuple positions processed in the final partition families, and zero discrepancies with the theorem. It also tests the theory-count formula at widths three through ten and canonical-truncation identities on further bounded parameter ranges.

A separate file, `rook_extremal_checker.py`, independently enumerates candidate vertex subsets of all six rook graphs with \(2\le a\le b\le4\) and checks their clique and independence numbers and the common-coordinate property of cliques of size at least three. Both programs were executed from their own supplied source paths; exact stdout is included in their respective `.stdout.txt` files. These finite tests corroborate but do not replace Steps 1--4, which establish the statements for every allowed parameter.

## Relationship to prior work

Rook graphs are standard line graphs of complete bipartite graphs, and also Cartesian products of two complete graphs. Gray and Macpherson identify infinite balanced instances in their classification of countable connected-homogeneous graphs; their finite background also includes balanced line graphs of complete bipartite graphs. These statements concern homogeneity rather than \(\mathrm{FO}^{k}\)-equivalence of all finite rectangular boards. Pikhurko and Verbitsky describe the general finite-variable pebble-game method, and Berkholz, Krebs, and Verbitsky treat alternation and quantifier-depth complexity. Adler, Benediktsson, and Macpherson investigate the VC-dimension and VC-density of the adjacency relation in Johnson and Hamming graphs, including rook graphs as natural related substructures; VC invariants do not determine the classification above. Published work classifying the logical width of complete multipartite graphs concerns \(K_{a,b}\) and its generalizations, not their line graphs; applying a line-graph construction does not by itself preserve exact variable widths. These distinctions do not constitute a proof of global historical priority.

## Limitations

The theorem does not address products with three or more complete-graph factors, arbitrary line graphs, extra coordinate predicates, counting logics, or global defining width among all finite graphs. The classification and computations are self-contained, but priority against uninspected general product-composition results is not established. Source dates for older journal-only material may lack exact public calendar-day evidence; the dated archival anchor is the arXiv posting of Pikhurko and Verbitsky on 2010-03-25.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 2010-03-25, especially Section 3 on pebble games. https://arxiv.org/abs/1003.4865
2. R. Gray and D. Macpherson, *Countable connected-homogeneous graphs*, Journal of Combinatorial Theory, Series B 100 (2010), 97--118, DOI:10.1016/j.jctb.2009.04.002, especially Theorem 1.1 and Proposition 4.7. https://doi.org/10.1016/j.jctb.2009.04.002
3. C. Berkholz, A. Krebs, and O. Verbitsky, *Bounds for the quantifier depth in finite-variable logics: Alternation hierarchy*, arXiv:1212.2747 (2012). https://arxiv.org/abs/1212.2747
4. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik--Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (2020). https://arxiv.org/abs/2007.16042
