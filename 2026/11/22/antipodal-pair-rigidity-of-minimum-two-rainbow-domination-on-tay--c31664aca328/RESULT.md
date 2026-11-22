# Antipodal-pair rigidity of minimum two-rainbow domination on Taylor graphs

## Finding

Let \(G\) be any finite, simple, connected distance-regular graph with intersection array \(\{k,\mu,1;1,\mu,k\}\), where \(k\ge5\) and \(3\le\mu\le k-2\). For each of two named colors, independently choose one antipodal pair (the two vertices at distance three), and assign that color to both endpoints of that pair and to no other vertices. These, including the choices where the two selected pairs coincide, are **all** minimum two-rainbow dominating functions. Every such function has weight four. Since the graph has \(k+1\) antipodal pairs, there are exactly \((k+1)^2\) minimum functions.

The twelve-vertex icosahedral graph, with intersection array \(\{5,2,1;1,2,5\}\), also has this rigidity despite failing the hypothesis \(\mu\ge3\). It has exactly \(6^2=36\) minimum named-color functions. The twenty-vertex Johnson graph \(J(6,3)\), with intersection array \(\{9,4,1;1,4,9\}\), has exactly \(10^2=100\) minimum named-color functions. The numerical minimum weight alone is not claimed new.

## Assumptions and scope

A two-rainbow dominating function is \(f:V(G)\to\{\varnothing,\{1\},\{2\},\{1,2\}\}\). If \(f(v)=\varnothing\), the union of labels of its neighbors must contain both colors. Its weight is \(\sum_{v\in V(G)}|f(v)|\). Both colors are named (interchanging the names generally gives a different function). Put \(A=\{v:1\in f(v)\}\), \(B=\{v:2\in f(v)\}\); thus \(w(f)=|A|+|B|\), and the requirement is that every vertex outside \(A\cup B\) has a neighbor in each of \(A\) and \(B\). A Taylor graph here means exactly a graph with the displayed intersection array, not an arbitrary antipodal graph.

## Proof

**Taylor geometry.** The intersection array implies every vertex has \(k\) neighbors at distance one, \(k\) at distance two, and exactly one at distance three, by the intersection-number recurrence. Therefore \(|V(G)|=2k+2\). Let \(x^*\) denote the unique distance-three vertex from \(x\). The distance-three relation consists of a perfect matching: by distance symmetry \((x^*)^*=x\). Since \(N(x)\cap N(x^*)=\varnothing\) and both neighborhoods have \(k\) vertices among the \(2k\) vertices distinct from \(x,x^*\), the neighborhoods partition those \(2k\) vertices. Thus each antipodal pair dominates every vertex outside it.

**Weight and color-support sizes.** If \(w(f)\le3\), at least one of \(A,B\) has at most one vertex. At least \(2k-1\) vertices then have empty labels; a single vertex can reach only \(k\) of them, and an absent color reaches none. Since \(2k-1>k\), no such function exists. Giving both colors separately to the endpoints of any antipodal pair yields a valid function of weight four (even if the same pair is chosen for both colors), so the minimum weight is four. At weight four, a color support of size zero or one is impossible: there are at least \(2k-2>k\) empty-label vertices. Consequently \(|A|=|B|=2\) for every optimum, counting a doubly labelled vertex in both sets.

**Support rigidity.** Let \(A=\{x,y\}\) be a color support of size two. A four-weight function has at least \(2k-2\) empty vertices, all of which must lie in \((N(x)\cup N(y))\setminus\{x,y\}\). If \(x,y\) are adjacent, their number of common neighbors is \(a_1=k-\mu-1\), and the outside union size is \(2k-2-a_1\), strictly below \(2k-2\) when \(\mu\le k-2\). If \(x,y\) are at distance two, they have exactly \(c_2=\mu\) common neighbors, and the outside union size is \(2k-\mu\), also strictly below \(2k-2\) when \(\mu\ge3\). Thus the pair must be at distance three, i.e. antipodal. This applies separately to \(A\) and \(B\). Conversely every ordered choice of antipodal pairs works as shown above. The number of antipodal pairs is \((2k+2)/2=k+1\), proving the theorem.

**Icosahedral boundary.** Here \(a_1=2\) excludes adjacent supports as before, but \(c_2=2\) permits equality in the distance-two counting inequality. Suppose \(A=\{x,y\}\) is distance two. It has exactly eight neighbors outside itself and there are at least eight empty vertices. Equality is forced: \(A\cap B=\varnothing\) and \(B\) is precisely the complement of \(A\cup N(A)\), consisting of two vertices. In the icosahedral graph these two residual vertices are adjacent for all thirty distance-two unordered pairs. This finite structural fact follows by checking the fivefold cyclic ring model (twelve vertices: two poles; five upper and five lower vertices; both ring cycles; upper vertex \(i\) joined to lower vertices \(i\) and \(i-1\)). The accompanying independent checkers explicitly verify the pair enumeration and residual-edge condition. Such an adjacent \(B\) can cover only \(2k-2-a_1=6\) empty vertices, a contradiction to the required eight. Therefore in the icosahedron as well, both color supports must be antipodal pairs. There are six pairs and thirty-six ordered choices.

**Johnson example.** In \(J(6,3)\), vertices are three-element subsets of a fixed six-element set, joined when they intersect in two elements. It has parameters \(k=9\) and \(\mu=4\) in the Taylor intersection array, so the theorem yields one hundred optima, supported on ordered complementary-pair choices.

## Verification

Two independently programmed enumerators are included. `check.py` constructs the pentagonal-ring icosahedron and \(J(6,3)\), computes all distances, tests all pairs of two-vertex color supports and all support sizes of total weight at most three, and checks the residual-vertex lemma for all thirty distance-two icosahedral pairs. `check.cpp` builds both graphs separately with bit masks, checks all ordered pairs of two-subsets and all supports of weight at most three, and verifies every predicted optimum. Run with `python3 check.py` and `g++ -std=c++17 -O2 check.cpp -o check && ./check`. Expected output: 36 and 100 minima, followed by `PASS`. Finite enumeration confirms the two instances and the icosahedral boundary lemma; the general infinite-class theorem is proved symbolically above, not inferred from examples.

## Relationship to prior work

Brešar, Henning and Rall introduced rainbow domination and its relationship with ordinary domination of graph products. Stępień and Zwierzchowski studied two-rainbow domination on Cartesian products of cycles, explicitly giving the standard minimum-weight bound \(2|V(G)|/(\Delta(G)+2)\). This bound already establishes weight at least four on each displayed finite example and on the stated Taylor graphs; the new assertion is the exhaustive *identity* of every optimal named-color function. Standard Taylor-graph tables supply the antipodal intersection arrays, but not this optimal-label rigidity. Published results concerning rainbow domination on generalized Petersen graphs, crown graphs, and the Petersen graph address different graph classes or boundary regimes and do not imply the stated Taylor result.

## Limitations

This does not classify all rainbow-dominating functions of greater weight, nor does it cover Taylor graphs with \(\mu\le2\) other than the explicitly handled icosahedron, or with \(a_1=0\) (for instance crown graphs). The special residual-edge claim is checked finitely for the fixed icosahedron. An unindexed published computation of minimum two-rainbow labelings on some Taylor graph may exist; mathematical priority remains subject to further historical inspection. Independent validation has not been performed.

## References

1. B. Brešar, M. A. Henning, D. F. Rall, *Rainbow domination in graphs*, Taiwanese Journal of Mathematics 12 (2008), 213–225. https://doi.org/10.11650/twjm/1500602498
2. Z. Stępień, M. Zwierzchowski, *2-Rainbow domination number of Cartesian products: \(C_n\square C_3\) and \(C_n\square C_5\)*, first published online 14 December 2012. https://doi.org/10.1007/s10878-012-9582-8
3. E. W. Weisstein, *Taylor Graph*, MathWorld. https://mathworld.wolfram.com/TaylorGraph.html
4. DistanceRegular.org, *Taylor Graphs*. https://www.math.mun.ca/distanceregular/indexes/taylorgraphs.html
