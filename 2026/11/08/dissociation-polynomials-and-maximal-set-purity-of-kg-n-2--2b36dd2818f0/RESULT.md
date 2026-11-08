# Dissociation polynomials and maximal-set purity of \(KG(n,2)\)

## Finding
For every integer \(n\ge4\), let \(G_n=KG(n,2)\), whose vertices are the two-element subsets of \([n]\), with two vertices adjacent if and only if the subsets are disjoint. A *dissociation set* is a vertex set whose induced graph has maximum degree at most one; it is *inclusion-maximal* if no vertex can be added while retaining that property. Write \(N=\binom n2\).

The complete dissociation polynomial \(D_n(z)=\sum_{S\subseteq V(G_n):\,\Delta(G_n[S])\le1}z^{|S|}\) is
\[
\boxed{D_n(z)=1+Nz+\binom N2z^2+\binom n3z^3+n\sum_{j=3}^{n-1}\binom{n-1}{j}z^j+\binom n4(12z^3+15z^4+6z^5+z^6).}
\]
For \(n\ge5\), the inclusion-maximal dissociation sets are precisely (i) the \(n\) complete stars \(\{\{v,w\}:w\ne v\}\) and (ii) the \(\binom n4\) collections of all six pairs of a fixed four-element subset. For \(n=4\), only the full six-vertex set is inclusion-maximal. Consequently their cardinality polynomial is
\[
\boxed{M_n(z)=\binom n4 z^6+\mathbf1_{\{n\ge5\}}nz^{n-1}.}
\]
All inclusion-maximal dissociation sets have the same cardinality if and only if \(n\in\{4,7\}\). When \(n\ge9\), their possible cardinalities are exactly \(\{6,n-1\}\); therefore the \(n-8\) consecutive sizes \(7,8,\ldots,n-2\) are unattainable.

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled on \([n]\). The dissociation condition is imposed on **induced** subgraphs, not arbitrary edge subgraphs. The word *maximal* means maximal by inclusion, not maximum by cardinality. The binomial coefficient \(\binom ab\) is zero if \(b>a\). The claims cover exactly integers \(n\ge4\), including the disconnected graph \(KG(4,2)\).

## Proof
Identify each selected vertex of \(G_n\) with an edge of the complete graph on \([n]\). The dissociation condition says that each selected edge is disjoint from at most one other selected edge.

**Structural dichotomy.** Let \(F\) be the selected edge family. Suppose it contains two disjoint edges \(ab\) and \(cd\). Every additional edge in \(F\) must intersect both \(ab\) and \(cd\), since otherwise one of these two selected vertices would have two selected neighbors in \(G_n\). Thus every other edge lies among \(ac,ad,bc,bd\). So \(F\) is contained in the complete six-edge family of pairs on the uniquely determined four-element support \(\{a,b,c,d\}\). Conversely, any subset of these six pairs is a dissociation set, because the Kneser graph on those six vertices is the three-edge matching \(KG(4,2)\).

Otherwise the members of \(F\) are pairwise intersecting. Such a family is contained in a star or the three edges of a triangle: if there are two distinct edges \(ab\) and \(ac\), then any edge avoiding \(a\) must be \(bc\); if \(bc\) occurs, no edge \(ad\) for \(d\notin\{a,b,c\}\) can occur. Families of size zero or one fit a star as well. This proves the complete structural dichotomy without assuming maximality.

**All-set count.** All zero-, one-, and two-element choices are dissociation sets, contributing \(1+Nz+\binom N2z^2\). Among pairwise-intersecting families of cardinality at least three, an ordinary star of \(j\ge3\) edges has a unique center and contributes \(n\binom{n-1}{j}\) configurations. In addition, there are exactly \(\binom n3\) intersecting triangles of size three; they are not stars. Every remaining family of cardinality at least three contains a disjoint pair, hence lies on a unique four-element support. Of the \(\binom63=20\) three-edge subsets of the six pairs on four labels, precisely eight are pairwise-intersecting (four three-edge stars and four triangles), leaving twelve. Every four-, five-, or six-edge subset has a disjoint pair (a pairwise-intersecting family has at most three members on four labels), yielding counts \(\binom64=15\), \(\binom65=6\), and \(\binom66=1\). Such a family has exactly four labels in its support; its four-set is uniquely determined, so none is counted twice. Combining these contributions proves \(D_n(z)\).

**Maximal-set count.** Suppose an inclusion-maximal \(F\) contains a disjoint pair. By the dichotomy it lies inside a complete six-edge family on four labels, and any omitted edge of that four-label family can be added without violating dissociation. Therefore \(F\) equals the full six-edge family. Conversely, such a full family is maximal: any additional pair \(uv\) not entirely inside its four labels is disjoint from at least three of the six selected pairs (if exactly one of \(u,v\) lies inside, the three pairs formed from the other three labels are disjoint; if neither lies inside, all six are disjoint). Hence its addition gives a selected vertex at least two neighbors.

Now suppose \(F\) is pairwise-intersecting. If contained in a triangle, it can be extended to the full six-edge family on a four-set, because \(n\ge4\), and hence is not maximal. Otherwise it is contained in a star and, unless the star is complete, can be extended by another edge of that star. A complete star for \(n=4\) is contained in the six-edge family and is not maximal. For \(n\ge5\), however, a complete star is maximal: any omitted pair \(uv\) avoids its center and is disjoint from \(n-3\ge2\) star edges. These are all possibilities. For \(n=4\), every proper dissociation set extends inside the six-edge family. Counting the four-sets and complete stars proves \(M_n(z)\).

**Purity and gaps.** In \(n=4\) only size six occurs. For \(n\ge5\), the two disjoint structural families have sizes six and \(n-1\). These coincide if and only if \(n=7\). For \(n\ge9\), sizes six and \(n-1\) omit exactly \(7,\ldots,n-2\), a sequence of \(n-8\) integers. This proves the remaining assertions.

## Verification
The accompanying standard-library Python file `verify.py` constructs each Kneser graph directly, enumerates **every** vertex subset for \(n=4,5,6,7\), checks induced degrees and the possibility of adding each omitted vertex, then compares both cardinality polynomials exactly. It examines \(2^6+2^{10}+2^{15}+2^{21}=2,131,008\) subsets. It also generates both claimed maximal-set families and checks validity/maximality directly for \(n=8,9,10,11,12\). The latter generated-family checks are not exhaustive for larger orders. All machine checks are finite corroboration; the above proof is valid for every \(n\ge4\).

## Relationship to prior work
Brešar and Dravec (2021), Proposition 2.1, **already proved** the sharp maximum dissociation number \(\max\{n-1,6\}\) for \(KG(n,2)\) and the key observation that any dissociation set containing two disjoint pairs is contained in the associated six-edge four-set. Those facts, including the maximum-size conclusion, are **not** claimed as new. Here the further pairwise-intersecting family analysis, exact counting of every coefficient, classification of **all inclusion-maximal** rather than only maximum-cardinality sets, and resulting \(n=4,7\) purity criterion form the assessed finding.

Brešar, Hartnell, and Rall (2017) introduced and studied uniformly dissociated graphs, with general results for small dissociation numbers and large girth; these results do not explicitly give the all-order Kneser classification above. Tu, Xiao, and Lang (2023) studied the dissociation polynomial of **cubic graphs**, particularly universal inequalities. Within the Kneser family \(KG(n,2)\), only \(KG(5,2)\) is cubic; their results do not yield this all-order coefficient formula.

## Limitations
This is a theorem for the two-subset Kneser graphs only; it does not classify \(KG(n,k)\) for \(k>2\). The known maximum dissociation number and the four-support containment lemma belong to prior literature. The novelty assessment refers to the complete enumerator and the maximal/facet and purity classification; equivalent unpublished or unindexed treatments remain a priority risk. The computation proves statements only for its listed finite orders, not the unrestricted theorem. No independent mathematical audit has been performed.

## References
1. B. Brešar, B. L. Hartnell, and D. F. Rall, *Uniformly dissociated graphs*, Ars Mathematica Contemporanea **13** (2017), 293–306. Published online 2017-03-09. DOI: https://doi.org/10.26493/1855-3974.1013.46a .
2. B. Brešar and T. Dravec, *On the dissociation number of Kneser graphs*, arXiv:2108.10801 (first public version 2021-08-24), especially Proposition 2.1. https://arxiv.org/abs/2108.10801 .
3. J. Tu, J. Xiao, and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics **8** (2023), 10021–10032, published 2023-02-23. DOI: https://doi.org/10.3934/math.2023507 .
4. J. Tu, Y. Li, and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402 (first public version 2021-03-02). https://arxiv.org/abs/2103.01402 .
