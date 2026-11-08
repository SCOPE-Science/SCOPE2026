# Complete induced- and maximal-induced-matching polynomials of cycle powers

## Finding
For every pair of integers \(r\ge1\) and \(n\ge2r+1\), let \(C_n^r\) be the graph on \(\mathbb Z/n\mathbb Z\) whose edges join vertices of cyclic distance at most \(r\). An *induced matching* is a set of edges whose endpoints induce a disjoint union of single edges. Such a matching is *inclusion-maximal* if no further edge can be added while preserving this property. Let \(I_{n,r}(z)\) and \(M_{n,r}(z)\) be the cardinality polynomials of all induced matchings (including the empty one) and all inclusion-maximal induced matchings, respectively.

Define two power series in an indeterminate \(x\):
\[
B_r(x)=\left(\sum_{\ell=1}^{r}x^{\ell}\right)
       \left(\sum_{g=r+1}^{\infty}x^g\right)
 =\frac{x^{r+2}(1-x^r)}{(1-x)^2},
\qquad
F_r(x)=\left(\sum_{\ell=1}^{r}x^{\ell}\right)
       \left(\sum_{g=r+1}^{2r+2}x^g\right)
 =\frac{x^{r+2}(1-x^r)(1-x^{r+2})}{(1-x)^2}.
\]
Then the complete polynomials are
\[
\boxed{I_{n,r}(z)=1+\sum_{k\ge1}\frac nk[x^n]B_r(x)^kz^k,}
\qquad
\boxed{M_{n,r}(z)=\sum_{k\ge1}\frac nk[x^n]F_r(x)^kz^k.}
\]
The coefficient extractions are finite because the lowest exponent in each block series is \(r+2\). Despite the rational expressions, all claimed coefficients are nonnegative integers.

The exact cardinality spectrum of inclusion-maximal induced matchings is
\[
\boxed{\operatorname{supp}M_{n,r}=
\left\{\left\lceil\frac{n}{3r+2}\right\rceil,
\left\lceil\frac{n}{3r+2}\right\rceil+1,\ldots,
\left\lfloor\frac{n}{r+2}\right\rfloor\right\}.}
\]
Thus the smallest inclusion-maximal induced matching has \(\lceil n/(3r+2)\rceil\) edges; the largest has \(\lfloor n/(r+2)\rfloor\) edges; and every intervening cardinality occurs. If \(r+2\) divides \(n\), exactly \(r+2\) maximal induced matchings achieve the largest cardinality. If \(3r+2\) divides \(n\), exactly \(3r+2\) maximal induced matchings achieve the smallest cardinality.

For example,
\[
I_{9,1}(z)=1+9z+18z^2+3z^3,\quad
M_{9,1}(z)=9z^2+3z^3,
\]
\[
I_{12,2}(z)=1+24z+96z^2+4z^3,\quad
M_{12,2}(z)=84z^2+4z^3.
\]

## Assumptions and scope
The graph is simple and undirected. The parameter restriction \(n\ge2r+1\) is essential to the chosen representation: every graph edge has exactly one clockwise orientation of length \(\ell\in\{1,\ldots,r\}\). In particular, the graph may be complete when \(n=2r+1\); these boundary cases are included. The zero-edge matching is counted only in \(I_{n,r}\), never in \(M_{n,r}\).

## Proof
Fix a clockwise orientation of the underlying labeled \(n\)-cycle. Write an edge of \(C_n^r\) uniquely as the ordered clockwise arc \((a,a+\ell)\) where \(1\le\ell\le r\). Given a nonempty induced matching with \(k\) edges, its endpoints occur in noninterleaving pairs along the cycle. Indeed, if an endpoint of a second chosen edge were strictly inside the clockwise arc of a first edge of length at most \(r\), that endpoint would be adjacent in \(C_n^r\) to at least one endpoint of the first edge, violating inducedness.

List the \(k\) oriented chosen edges in clockwise order. For edge \(i\), denote its clockwise internal length by \(\ell_i\), and denote by \(g_i\) the number of clockwise steps from the terminal vertex of this edge to the initial vertex of the next chosen edge, using cyclic indices. Then
\[
1\le\ell_i\le r,\qquad \sum_{i=1}^{k}(\ell_i+g_i)=n.
\]
The matching is induced **if and only if**
\[
g_i\ge r+1\qquad(1\le i\le k).
\]
Necessity follows from the edge connecting consecutive chosen endpoints if the gap has at most \(r\) steps. For sufficiency, the shortest clockwise or counterclockwise route between endpoints of distinct chosen edges crosses at least one such gap and therefore has more than \(r\) steps; hence no endpoint adjacency occurs between different chosen edges.

Now consider an induced matching. Any edge that could be added must have both endpoints in a single open gap between consecutive chosen edges, because its endpoints cannot cross a chosen edge arc. A vertex of this gap can serve as a new endpoint only if it is at least \(r+1\) steps clockwise after the preceding terminal chosen endpoint and at least \(r+1\) steps before the next initial chosen endpoint. Thus the eligible positions are the integer points from offset \(r+1\) through offset \(g_i-r-1\) in a gap of length \(g_i\). They contain two consecutive positions if and only if \(g_i\ge2r+3\), in which case their joining edge is available; with fewer than two eligible positions there is no addable edge. Consequently, an induced matching is inclusion-maximal **if and only if**
\[
r+1\le g_i\le2r+2\qquad(1\le i\le k).
\]
This criterion remains valid for \(k=1\), where the single gap runs from the chosen edge's terminal endpoint back to its initial endpoint.

Each pair \((\ell_i,g_i)\) contributes a block of length \(\ell_i+g_i\). The allowed blocks are counted by \(B_r(x)\) for general induced matchings, and by \(F_r(x)\) for maximal ones. For fixed \(k\), each ordered collection of \(k\) blocks summing to \(n\) and each choice of the initial labeled vertex (\(n\) choices) produces a matching with one distinguished chosen edge. Conversely every matching with \(k\) edges has exactly \(k\) choices of distinguished edge, so dividing by \(k\) gives precisely \(n/k\) times the coefficient of \(x^n\) in the relevant \(k\)-th power. This proves the two polynomials.

Every integer block length from \(r+2\) to \(3r+2\) has positive coefficient in \(F_r(x)\): it is a sum of one integer from \([1,r]\) and one from \([r+1,2r+2]\). Thus a \(k\)-edge maximal induced matching exists precisely when \(k(r+2)\le n\le k(3r+2)\). The displayed interval for \(\operatorname{supp}M_{n,r}\) follows, including existence at each intervening cardinality.

When \(n=k(r+2)\), every block is the unique shortest block \((\ell,g)=(1,r+1)\), hence there are \(n/k=r+2\) such matchings. When \(n=k(3r+2)\), every block is the unique longest block \((\ell,g)=(r,2r+2)\), hence there are \(n/k=3r+2\). This establishes the two divisibility rigidity counts. No other parameter restrictions are required.

## Verification
The standalone standard-library program `verify.py` independently constructs graph edges using cyclic distance, enumerates candidate edge-subsets, tests inducedness by all four cross-endpoint distances, and tests inclusion-maximality by attempted addition of every remaining edge. For \(1\le r\le4\) and \(2r+1\le n\le16\), it matches both coefficient polynomials in all 44 graph instances. The run examined 116,874 candidate edge-subsets, identifying 5,627 induced matchings and 3,230 inclusion-maximal ones. A separate exact-arithmetic check for 888 parameter pairs (\(1\le r\le8\), \(2r+1\le n\le120\)) checks integrality, support, and the two extremal coefficients. Its output is:

`VERIFY_OK graph_instances=44 edge_subset_candidates=116874 induced_matchings=5627 maximal_induced_matchings=3230 arithmetic_parameter_pairs=888`

The unlimited-parameter conclusion follows from the proof above, not from finite testing. Run with `python3 verify.py`; it requires only the Python standard library.

## Relationship to prior work
Romeo's work on circulant graphs (2018, Corollary 3.3) already identifies the **maximum induced-matching cardinality** \(\lfloor n/(r+2)\rfloor\) when \(r<\lfloor n/2\rfloor\); the excluded boundary \(n=2r+1\) is a complete graph and has the same scalar maximum trivially. That scalar result is not claimed as new. The present statement determines the **entire labeled distributions** for induced matchings and maximal induced matchings, including the minimum size of an inclusion-maximal solution, all possible sizes, and two exact extremal multiplicities.

General work of Basavaraju and collaborators bounds the total number of maximal induced matchings in triangle-free graphs; the main case \(r\ge2\) of a cycle power contains triangles, and in any event a bound cannot imply the displayed exact size polynomial. Yuan and collaborators study extremal numbers of maximal induced matchings over all connected graphs, not their size enumerators for cycle powers. Complexity studies of minimum maximal induced matchings provide context but no identified equivalent special-family count. Specific priority risks appear below.

## Limitations
The theorem concerns only consecutive-distance cycle powers \(C_n^r\), not arbitrary circulant connection sets, and it counts labeled matchings in the canonical labeled graph rather than rotation or dihedral equivalence classes. It makes no assertion about complexity for general graphs. The method uses a cyclic gap decomposition; the \(r=1\) case is closely related to classical maximal independent-set recurrences and should not be separately presented as a new phenomenon. Publication priority remains provisional: unindexed specialized enumerations, particularly via independence domination polynomials of squared line graphs, may already imply some or all formulas. The full text of certain older hardness papers was not accessible; their abstracts do not report a cycle-power enumerator. No independent mathematical audit has been performed.

## References
- Francesco Romeo, *Chordal circulant graphs and induced matching number*, arXiv:1811.06409 (first publicly posted 2018-11-15), Section 3, Corollary 3.3. https://arxiv.org/abs/1811.06409
- Manu Basavaraju, Pinar Heggernes, Pim van 't Hof, Reza Saei, and Yngve Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180 (2013). https://arxiv.org/abs/1312.5180
- Bo-Jun Yuan, Zhao-Yu Yang, Lu Zheng, and Shi-Cai Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288 (first publicly posted 2024-10-15). https://arxiv.org/abs/2410.11288
- Juhi Chaudhary and B. S. Panda, *On Two Variants of Induced Matchings*, ICS 2022 proceedings, first online 2023-02-10. DOI:10.1007/978-981-19-9582-8_4.
- Yury L. Orlovich and Igor E. Zverovich, *Maximal induced matchings of minimum/maximum size*, DIMACS Technical Report 2004-26, abstract and bibliographic record. https://archive.dimacs.rutgers.edu/TechnicalReports/abstracts/2004/2004-26.html
