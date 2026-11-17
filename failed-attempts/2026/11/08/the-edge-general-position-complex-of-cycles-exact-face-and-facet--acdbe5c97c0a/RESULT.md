# The edge-general-position complex of cycles: exact face and facet polynomials

## Finding
For each integer \(n\ge3\), let \(C_n\) be the simple cycle with edges indexed cyclically by \(\mathbb Z/n\mathbb Z\). Call \(S\subseteq E(C_n)\) **edge-general-position** when no shortest path contains three edges of \(S\). Define its face polynomial \(P_n(z)=\sum_{S\text{ edge-general-position}}z^{|S|}\) and facet polynomial \(M_n(z)=\sum_{S\text{ inclusion-maximal edge-general-position}}z^{|S|}\). All edge subsets, including the empty set, contribute to \(P_n\).

For \(3\le n\le5\),
\[
P_n(z)=(1+z)^n,\qquad M_n(z)=z^n.
\]
For \(n=2h\ge6\), the complete polynomials are
\[
\begin{aligned}
P_{2h}(z)&=1+2hz+\binom{2h}{2}z^2+
\frac{h(h-1)(h+4)}3z^3+\binom h2z^4,\\
M_{2h}(z)&=\frac{h(h-1)(h-2)}3z^3+\binom h2z^4.
\end{aligned}
\]
For \(n=2h+1\ge7\), they are
\[
\begin{aligned}
P_{2h+1}(z)&=1+(2h+1)z+\binom{2h+1}{2}z^2+
\frac{(2h+1)(h^2+7h-6)}6z^3+(2h+1)(h-1)z^4,\\
M_{2h+1}(z)&=\frac{(2h+1)(h-2)(h-3)}6z^3+(2h+1)(h-1)z^4.
\end{aligned}
\]
These are identities of integer-coefficient polynomials, with no omitted higher-degree terms.

The combinatorial classification is also exact. If \(n\ge6\) and \(S\) has \(k\ge3\) chosen edges, write the positive clockwise gaps between consecutive chosen edge indices as \(d_1,\ldots,d_k\), with indices taken cyclically. Then
\[
S\text{ is edge-general-position}\quad\Longleftrightarrow\quad
 d_i+d_{i+1}\ge\lfloor n/2\rfloor\ \text{for every }i.
\]
Every such set has at most four edges. Every valid four-edge set is inclusion-maximal; a valid three-edge set is inclusion-maximal precisely when all three gaps are at most \(\lfloor n/2\rfloor-1\). Sets of at most two edges are never maximal when \(n\ge6\).

In particular the minimum size of a maximal edge-general-position set is \(4\) for \(n=7\), is \(3\) for \(n=6\) or \(n\ge8\), and is \(n\) for \(3\le n\le5\). The maximum size is the already known \(n\) for \(n\le5\) and \(4\) for \(n\ge6\). The edge-general-position complex of a cycle is therefore pure exactly for \(n\in\{3,4,5,7\}\).

## Assumptions and scope
All graphs are finite, simple and undirected. An edge of \(C_n\) is indexed by its initial vertex along one fixed orientation. A path is shortest when its edge length equals the graph distance between its endpoints. For \(C_n\), the maximum shortest-path length is \(h=\lfloor n/2\rfloor\). Inclusion-maximal means maximal under adding an edge, rather than maximum cardinality. The cyclic-gap statements concern a fixed subset of at least three distinct edges; gaps are positive and sum to \(n\).

## Proof
**1. Cyclic gap criterion.** Let \(n\ge6\), and let selected edge indices \(i_1,\ldots,i_k\) appear in clockwise order, \(k\ge3\). Write \(d_j=i_{j+1}-i_j\pmod n\) with positive representatives. The clockwise edge arc starting at selected edge \(i_j\) and ending at selected edge \(i_{j+2}\) contains precisely \(d_j+d_{j+1}+1\) edges. If its length is at most \(h\), it is a shortest path containing three selected edges. Conversely, if a shortest path contains at least three selected edges, three consecutive selected edges within that path (hence consecutive in the cyclic order) occupy an arc of at most \(h\) edges. Thus validity is equivalent to \(d_j+d_{j+1}+1>h\) for every \(j\), or \(d_j+d_{j+1}\ge h\). Summation over all \(k\) inequalities gives \(2n\ge kh\). If \(n=2h\), then \(2n=4h<5h\); if \(n=2h+1\ge7\), then \(2n=4h+2<5h\). No valid set therefore has five or more edges.

**2. Three-edge faces.** For three selected edges the gap condition is \(n-d_j\ge h\) for each \(j\), equivalently \(1\le d_j\le c=\lceil n/2\rceil\), with \(d_1+d_2+d_3=n\). The number of positive ordered compositions satisfying these upper bounds is
\[
U_3(n,c)=\binom{n-1}{2}-3\binom{n-c-1}{2}.
\]
Indeed, the bad compositions with a specified gap at least \(c+1\) number \(\binom{n-c-1}{2}\), and two gaps cannot both exceed \(c\). Each unordered selected triple has exactly three choices of a marked starting selected edge, whereas each ordered gap triple together with a starting edge among the \(n\) edge indices determines one marked selection. The number of valid triples is therefore \(nU_3(n,c)/3\). Substituting \(n=2h\), \(c=h\), or \(n=2h+1\), \(c=h+1\), simplifies to the respective coefficients displayed in \(P_n\).

**3. Four-edge faces.** For four cyclic gaps \((a,b,c,d)\) the criterion is \(a+b,b+c,c+d,d+a\ge h\). Because opposite sums add to \(n\), when \(n=2h\), each of those adjacent sums equals \(h\). This forces \((a,b,c,d)=(a,b,a,b)\) with \(a,b\ge1\) and \(a+b=h\). There are \(h-1\) rooted gap quadruples. Counting a starting edge in \(n\) ways and dividing by the four marked choices gives \(n(h-1)/4=\binom h2\) distinct four-edge faces.

If \(n=2h+1\), both \(a+b\) and \(b+c\) must lie in \(\{h,h+1\}\); their opposite sums then automatically satisfy the criterion. For each of the four ordered possibilities for these two sums, the positive solutions for \((a,b,c,d)\) number exactly \(h-1\). For example, if both sums equal \(h\), let \(b\in\{1,\ldots,h-1\}\), giving \((a,b,c,d)=(h-b,b,h-b,b+1)\); the other three possibilities similarly have \(h-1\) solutions. There are \(4(h-1)\) rooted gap quadruples, hence \(n(h-1)\) distinct four-edge faces.

**4. Which faces are facets?** Every four-edge face is a facet by Step 1. A valid triple with gaps \((a,b,g)\) can be extended to a valid four-edge set only by splitting one gap. The four-edge inequalities imply that both the split pair \(u+v=g\) and the pair of original unsplit gaps \(a+b=n-g\) must be at least \(h\). Hence that original gap must satisfy \(g\ge h\). Conversely, suppose a valid triple has a gap \(g\ge h\). Validity already gives \(g\le\lceil n/2\rceil\). If \(n=2h\), necessarily \(g=h\) and \(a+b=h\); splitting \(g\) into \((a,b)\) produces the valid four-gap tuple \((a,b,a,b)\). If \(n=2h+1\) and \(g=h+1\), then \(a+b=h\), and splitting into \((a,b+1)\) works. If \(g=h\), then \(a+b=h+1\); splitting into \((a,b-1)\) works when \(b\ge2\), and splitting into \((a-1,b)\) works when \(b=1\) (then \(a=h\ge3\)). In each case the resulting four adjacent gap sums are at least \(h\). Thus a valid triple is a facet exactly if \(d_1,d_2,d_3\le h-1\).

Every two-edge set can be extended to a valid triple: its two cyclic gaps sum to \(n\), and at least one is at most \(\lceil n/2\rceil\). Split the other, which has size at least two, into two positive pieces each at most \(\lceil n/2\rceil\); such a split exists because the gap is at most \(n-1\le 2\lceil n/2\rceil\). The resulting three gaps meet the triple criterion. Sets with fewer edges also extend. Therefore there are no facets of size at most two.

**5. Three-edge facets.** Their number is \(n/3\) times the number of positive compositions of \(n\) into three parts, each at most \(h-1\). Inclusion-exclusion gives
\[
U_3(n,h-1)=\binom{n-1}{2}-3\binom{n-h}{2}+3\binom{n-2h+1}{2},
\]
where \(\binom ab=0\) for \(a<b\) or \(a<0\). There are no triple intersections of the forbidden conditions. For even \(n=2h\), the last term is zero, yielding \(h(h-1)(h-2)/3\) three-edge facets. For odd \(n=2h+1\), the double intersections are exactly the three permutations of \((h,h,1)\), yielding \((2h+1)(h-2)(h-3)/6\). Combined with Step 3 these are precisely the displayed facet polynomials.

**6. Boundaries and purity.** For \(n\le5\), the cycle has diameter at most two, so every subset of edges is valid and the entire edge set is the only facet. For \(n\ge6\), every four-edge coefficient is positive, while the three-edge facet coefficient is zero exactly for \(n=7\) (among these orders). Therefore the stated lower/upper cardinalities and purity classification follow. \(\square\)

## Verification
Run `python3 verify.py` using Python's standard library. The code independently enumerates *all shortest-path arcs* (not gap compositions) to test every edge subset for \(3\le n\le18\); it checks coefficientwise counts and all facets by one-edge extensions. It also checks the gap classifications and enumerates all three-, four-, and five-edge subsets for \(19\le n\le26\). These computations are finite corroboration; Steps 1–6 prove the unrestricted statements.

## Relationship to prior work
Manuel, Prabha and Klavžar introduced edge general position and already observed \(\operatorname{gp}_e(C_n)=n\) for \(3\le n\le5\) and \(4\) thereafter. Tian, Klavžar and Tan explicitly restated that result in Proposition 1.1(i) of their 2024 paper. Those **maximum cardinalities are not new**. The contribution here is the complete cyclic-gap classification, the coefficients counting *every* feasible edge set, the entire inclusion-maximal census, and the exceptional purity of \(C_7\); the inspected primary texts do not state these stronger results. The 2024 general-position polynomial of Iršič and collaborators counts vertex sets, not edge sets. Later work on edge-general-position numbers of general graphs and cacti addresses scalar extremal parameters rather than the full cycle facet profile.

## Limitations
This is a result on simple cycles, not arbitrary cactus graphs, graph products, or higher \(k\)-edge-general-position variants. The exact priority assessment is provisional: an unindexed equivalent might exist; relevant 2025 scalar-extremal papers and the 2024 \(k\)-general-position paper were not all available in complete full text. Independent mathematical review has not been performed. No finite enumeration alone establishes the infinite family theorem.

## References
- P. Manuel, R. Prabha, S. Klavžar, *Edge General Position Problem*, arXiv:2105.04292v1 (first public 2021-05-10), https://arxiv.org/abs/2105.04292, subsequently *Bull. Malays. Math. Sci. Soc.* 45 (2022), 2997–3009.
- J. Tian, S. Klavžar, E. Tan, *Extremal Edge General Position Sets in Some Graphs*, *Graphs and Combinatorics* 40, article 40 (2024), https://doi.org/10.1007/s00373-024-02770-z.
- V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, *Results in Mathematics* 79, article 110 (2024), https://doi.org/10.1007/s00025-024-02133-3.
- Y. Cao, S. Ji, *A note on the edge general position number of cactus graphs*, *Open Mathematics* 23 (2025), https://doi.org/10.1515/math-2025-0207.
- Z.-L. Li, S.-C. Gong, *Graphs Whose Edge General Position Number is 4*, *Bull. Malays. Math. Sci. Soc.* 48, article 87 (2025), https://doi.org/10.1007/s40840-025-01870-0.
- P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357 (2022 preprint), https://arxiv.org/abs/2207.07357.
