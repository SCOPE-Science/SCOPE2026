# Complete connected mutual-visibility polynomial for high-girth clique-fiber products

## Finding

Let \(H\) be a finite simple connected graph of girth at least five, with \(|V(H)|\ge2\), and let \(q\ge3\). Put \(X=H\square K_q\). Write \(C_X(z)\) for the generating polynomial of **nonempty connected mutual-visibility sets** by cardinality. Then

\[
\boxed{C_X(z)=|V(H)|\big((1+z)^q-1\big)+|E(H)|qz^2(1+2z)^{q-1}.}
\]

Every counted set lies in one clique fiber, or lies in two adjacent fibers and uses exactly one common color coordinate. In the latter case, each other color occurs in at most one of those two fibers. These alternatives are exhaustive and disjoint.

It follows that \(\mu_c(X)=q+1\) and that precisely \(|E(H)|q2^{q-1}\) maximum sets exist. In fact, *every inclusion-maximal* connected mutual-visibility set is maximum, of size \(q+1\). The total number of nonempty admissible sets is \(|V(H)|(2^q-1)+|E(H)|q3^{q-1}\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Connectedness means that the subgraph *induced* by the selected vertices is connected; singletons count as connected. Girth is at least five, with infinite girth allowed for forests. The vertices of \(H\square K_q\) are pairs \((h,c)\), where \(h\in V(H)\) and \(c\in[q]\). Edges change either the first coordinate along an edge of \(H\), or the second coordinate within a complete graph, but never both. A pair of selected vertices is mutually visible if **at least one** shortest path between them has all internal vertices outside the selected set. The empty set is not counted.

For a selected set \(S\), its fiber section is \(S_h=\{c:(h,c)\in S\}\). The formula counts labelled subsets; no quotient by graph or color automorphisms is taken.

## Proof

**Lemma 1 (at most two selected fibers).** Let \(S\) be connected and mutually visible. Form a graph \(T\) on the base vertices with nonempty fiber sections, joining distinct \(u,v\) precisely when \(uv\in E(H)\) and \(S_u\cap S_v\ne\varnothing\). The graph \(T\) is connected because any path in the induced graph \(X[S]\) can change base coordinates only at an edge of \(T\). Suppose \(T\) has at least three vertices. A connected graph with at least three vertices has two adjacent edges \(uv\) and \(vw\), with \(u,v,w\) distinct. Choose \(a\in S_u\cap S_v\) and \(b\in S_v\cap S_w\).

The girth hypothesis ensures that the two-edge walk \(u-v-w\) is the **unique** base geodesic from \(u\) to \(w\): a triangle would give a one-edge shortcut and a quadrilateral would give another two-edge route. If \(a=b\), the only two-step product geodesic between \((u,a)\) and \((w,a)\) passes through \((v,a)\in S\), so these selected vertices are not visible. If \(a\ne b\), any product geodesic from \((u,a)\) to \((w,b)\) consists of the two forced base steps and a single color change. The color change occurs before, between, or after the base steps. In every case the geodesic passes through \((v,a)\in S\) or \((v,b)\in S\) internally. Again visibility fails. Thus \(T\), and hence the base support of \(S\), has at most two vertices.

**Lemma 2 (exact two-fiber criterion).** If the base support is exactly \(\{u,v\}\), connectivity forces \(uv\in E(H)\) and \(A=S_u\), \(B=S_v\) to have a nonempty intersection. If distinct \(a,b\) both belong to \(A\cap B\), consider the selected endpoints \((u,a)\) and \((v,b)\). They have distance two, and their two possible internal geodesic vertices are \((u,b)\) and \((v,a)\), both selected. Hence mutual visibility forces \(|A\cap B|=1\).

Conversely, if \(uv\in E(H)\) and \(|A\cap B|=1\), the selected induced subgraph comprises two cliques linked by the unique matching edge of the common color, so it is connected. Pairs within one clique or with the same color across cliques are adjacent. For a pair \((u,a),(v,b)\) with \(a\ne b\), the two length-two geodesics have intermediate vertices \((u,b)\) and \((v,a)\). If both were selected, both \(a\) and \(b\) would lie in \(A\cap B\); this contradicts \(|A\cap B|=1\). At least one geodesic therefore avoids \(S\) internally. This proves sufficiency. A nonempty subset of a single clique fiber is, of course, connected and mutually visible.

**Counting.** Each single fiber contributes \((1+z)^q-1\). For every unordered base edge, there are \(q\) choices of the unique common color, giving \(z^2\); for each of the other \(q-1\) colors there are exactly three possibilities: absent, in the first fiber only, or in the second fiber only, with weight \(1+2z\). Thus each edge contributes \(qz^2(1+2z)^{q-1}\). The base supports make these contributions disjoint. Summation proves the generating polynomial.

**Maximum and inclusion-maximal sets.** Single-fiber sets have size at most \(q\). Two-fiber sets have exactly one common color and at most one occurrence of each remaining color, so have size at most \(q+1\). This bound is attained over every base edge by placing all remaining colors on either endpoint. There are \(2^{q-1}\) choices of these assignments for each edge and common color, giving exactly \(|E(H)|q2^{q-1}\) maximum sets. Any single-fiber set can be extended to an admissible two-fiber set (first fill its fiber, if necessary, then add one vertex with a color already selected to an adjacent fiber). Any two-fiber admissible set smaller than \(q+1\) can be extended by assigning a missing color to either endpoint. Thus precisely the maximum sets are inclusion-maximal. Substituting \(z=1\) gives the total cardinality.

## Verification

The self-contained `verify.py` separately constructs the graph, computes all-pairs shortest distances and internal geodesic masks, enumerates **every** vertex subset in ten bounded examples, tests induced connectivity and all-pair visibility directly, and compares its full cardinality profile with the claimed polynomial. Examples include trees, stars, paths, \(C_5\) and \(C_6\), as well as clique widths from two (the previously known boundary) through five. The largest examined graph has sixteen vertices; its full power set is traversed. All ten independent definition-level checks return `EXHAUSTIVE_OK`, followed by `VERIFY_OK`. Finite tests corroborate the unrestricted proof; they are not its justification.

For example, \(H=C_5\) and \(q=3\) give \(C_X(z)=15z+30z^2+65z^3+60z^4\). This yields sixty maximum four-element sets.

## Relationship to prior work

Tonny K B and Shikhi M introduce connected mutual visibility in arXiv:2609.18877v1 (submitted 2026-09-16). Their full manuscript establishes structural bounds and examples, including the girth criterion for graphs having connected mutual-visibility number two, but does not determine the clique-fiber product's all-set polynomial.

The published 2026 note *Connected mutual-visibility in Cartesian products of high-girth graphs* establishes the exact maximum three and Cartesian-corner minimizers when **both** nontrivial Cartesian factors have girth at least five. Its theorem applies to \(K_2\), but **does not apply to** \(K_q\) with \(q\ge3\), because those cliques contain triangles. The present theorem both handles that excluded factor and counts every admissible set, rather than only its maximum ones. The known two-color case agrees with the formula but is excluded from the new range.

Cicerone, Di Stefano, and Klavžar investigate **ordinary** mutual visibility in Cartesian products (arXiv:2112.13024v2), where no induced-connectedness condition is imposed. Tonny and Shikhi's earlier visibility-polynomial article arXiv:2509.22571v1 likewise counts ordinary visibility sets on different families. Neither statement implies the connected enumeration here. These comparisons rely on inspected full text, not just titles. No stronger covering all-size theorem was found in the searched records; historical priority remains provisional.

## Limitations

The theorem requires the base graph to be connected and triangle-/quadrilateral-free, and the new range is \(q\ge3\). It makes no claim for bases with shorter cycles, disconnected bases, or different Cartesian factors. In particular, the shortest-path uniqueness lemma can fail on graphs containing a four-cycle. The all-set polynomial excludes the empty set. The origin of the connected mutual-visibility invariant is recent, so unindexed or parallel results remain a plausible originality risk. No independent mathematical audit or independent validation has been performed.

## References

1. Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877v1 (submitted 2026-09-16), https://arxiv.org/abs/2609.18877 .
2. *Connected mutual-visibility in Cartesian products of high-girth graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-connected-mutual-visibility-cartesian-high-girth--9bfa61f8ea8a .
3. S. Cicerone, G. Di Stefano and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024v2, https://arxiv.org/abs/2112.13024 .
4. Tonny K B and Shikhi M, *Visibility Polynomial of Some Graph Classes*, arXiv:2509.22571v1, https://arxiv.org/abs/2509.22571 .
