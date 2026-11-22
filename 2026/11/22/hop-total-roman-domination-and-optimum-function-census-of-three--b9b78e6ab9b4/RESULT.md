# Hop-total Roman domination and optimum-function census of three-subset Kneser graphs

## Finding

Let \(n\ge8\) be an integer. The three-subset Kneser graph \(G_n=\operatorname{KG}(n,3)\) has one vertex for each triple in \([n]\); two vertices are adjacent when the triples are disjoint. A *hop-total Roman dominating function* is a function \(f:V(G_n)\to\{0,1,2\}\) such that every zero-labelled vertex has a two-labelled vertex at graph distance **exactly two**, and the subgraph induced by all nonzero-labelled vertices has no isolated vertex. Its weight is the sum of its labels. Denote by \(\gamma_{\mathrm{htR}}(G_n)\) its minimum weight and by \(A_n\) the number of minimum functions on labelled graph vertices, with labels \(0,1,2\) distinguished.

Write \(r=\lfloor n/3\rfloor\) and \(s=n-3r\in\{0,1,2\}\). Then
\[
\boxed{\gamma_{\mathrm{htR}}(G_n)=2r-\mathbf{1}_{\{s=0\}}.}
\]
Every minimum function is exactly one of the following types, and all functions described are valid:

1. **\(s=0\), \(r\ge3\).** Partition \([n]\) into \(r\) disjoint triples; designate one triple to be labelled \(1\), label the other \(r-1\) triples \(2\), and label all other graph vertices \(0\).
2. **\(s=1\), \(r\ge3\).** Label \(r\) triples by \(2\), every other graph vertex by \(0\). Either the selected triples are pairwise disjoint (one ground element unused), or exactly two selected triples share exactly one ground element, all their other intersections are empty (two ground elements unused).
3. **\(s=2\), \(r\ge2\).** Label \(r\) mutually disjoint triples by \(2\), every other graph vertex by \(0\), leaving two ground elements unused.

The complete count of **minimum** functions is
\[
\boxed{A_n=\begin{cases}
\dfrac{n!}{6^r(r-1)!},&s=0,\\[4pt]
\dfrac{n!}{6^r r!}+\dfrac{n!}{16\cdot6^{r-2}(r-2)!},&s=1,\\[4pt]
\dfrac{n!}{2\cdot6^r r!},&s=2.
\end{cases}}
\]
In particular \(\gamma_{\mathrm{htR}}(G_8)=4\), \(\gamma_{\mathrm{htR}}(G_9)=5\), \(\gamma_{\mathrm{htR}}(G_{10})=6\), and \((A_8,A_9,A_{10},A_{11},A_{12})=(280,840,40600,15400,61600)\).

## Assumptions and scope

All graphs are finite, simple, undirected, and have distinct labelled ground elements. "Distance exactly two" means shortest-path distance two in \(G_n\), not distance at most two and not adjacency. The positive induced graph is computed with the **ordinary Kneser adjacency** (disjointness), not with distance-two adjacency. The enumeration distinguishes all ground-element labels, but does not assign names to the selected triple blocks beyond their numerical Roman values. This is a theorem for every integer \(n\ge8\); no claim is made for \(n<8\) or for other Kneser ranks.

## Proof

**1. The distance-two criterion.** Let \(X,Y\) be distinct triples of \([n]\). If they are disjoint, then they are adjacent, so their distance is one. If they intersect, they are nonadjacent and \(|X\cup Y|\le5\). Because \(n\ge8\), at least three ground elements lie outside \(X\cup Y\); these form a triple adjacent to both \(X\) and \(Y\). Hence
\[
\operatorname{dist}_{G_n}(X,Y)=2\quad\Longleftrightarrow\quad X\ne Y\ \text{and}\ X\cap Y\ne\varnothing.
\]
The exclusion \(X=Y\) matters: a vertex cannot hop-dominate itself at distance two.

**2. Forced ones and a universal lower bound.** Let \(D\) be the set of triples labelled \(2\); put \(m=|D|\), \(U=\bigcup_{X\in D}X\), and \(u=|U|\le3m\). A triple entirely inside \([n]\setminus U\) meets no defender and thus cannot carry label \(0\). It also is not a defender, so its label is necessarily \(1\). Every triple meeting \(U\) but not belonging to \(D\) is allowed to carry label \(0\), since it meets some different selected triple. Consequently every admissible function satisfies
\[
\operatorname{wt}(f)\ge2m+\binom{n-u}{3}
\ge 2m+\binom{\max\{n-3m,0\}}3,
\]
where the binomial coefficient is zero if the upper argument is below three. This bound does not assume that the positive induced graph has no isolates, so it applies a fortiori to hop-total Roman functions.

For \(m=0\), the weight is \(\binom n3\), since all graph vertices must be labelled \(1\). For \(m\ge r+1\), it is at least \(2r+2\). For \(1\le m\le r-2\), let \(F(m)=2m+\binom{n-3m}3\). Here \(n-3m\ge6+s\); the difference \(F(m+1)-F(m)=2+\binom{n-3m-3}3-\binom{n-3m}3\) is negative (the three-step decrease in the cubic binomial exceeds two). Thus
\[
\operatorname{wt}(f)\ge F(r-2)=2r-4+\binom{6+s}3>2r.
\]
This interval is empty when \(r=2\). The only remaining cases are:
\[
\begin{array}{c|c|c}
&s=0&s=1\quad\text{or}\quad2\\\hline
m=r-1&2r-2+\binom33=2r-1&\ge 2r-2+\binom43=2r+2\\
m=r&\ge2r&\ge2r.
\end{array}
\]
Therefore every hop-total Roman function has weight at least \(2r-1\) for \(s=0\), or at least \(2r\) for \(s=1,2\).

**3. Equality and optimizer rigidity.** When \(s=0\), equality forces \(m=r-1\), exactly three unused ground elements, and precisely one labelled \(1\) triple. Thus \(u=3(r-1)\) and the defenders are pairwise disjoint; the one labelled \(1\) vertex is the triple complementary to their union. All other vertices have label \(0\). When \(s\ne0\), equality forces \(m=r\) and no vertex labelled \(1\); it also forces fewer than three ground elements outside \(U\). For \(s=2\), this is possible only with \(u=3r\), so the defenders are disjoint. For \(s=1\), either \(u=3r\) (disjoint) or \(u=3r-1\). The latter implies one duplicated ground element in the selected triples and hence exactly one intersecting pair, with all other pairs disjoint. There are no other equality patterns.

**4. Existence and the total-positive condition.** In every classified configuration, all zero-labelled triples intersect a selected defender by construction, and are different from that defender. Step 1 makes their required distance exactly two. The positive graph in the \(s=0\) case consists of \(r\) mutually disjoint triples and hence induces \(K_r\), which has no isolates. For \(s=1\) with disjoint selected triples and for \(s=2\), the positive graph is \(K_r\). In the overlapping \(s=1\) case, the two intersecting defenders are adjacent in \(G_n\) to each of the other \(r-2\) defenders. Since \(r\ge3\), these provide positive neighbors and every defender is nonisolated. Thus every equality pattern is valid, and the lower bound is sharp.

**5. Counting.** For \(s=0\), choose an unordered matching of \(r-1\) triples and let the remaining triple be the uniquely labelled \(1\) vertex; the count is \(n!/[6^r(r-1)!]\). For \(s=2\), choose \(r\) unordered disjoint triples and two unused points, yielding \(n!/[2\cdot6^rr!]\). For \(s=1\), the disjoint case has count \(n!/[6^rr!]\). In the one-overlap case, the shared ground point is uniquely determined, as is the unordered pair of unused ground points; split the other four points of the two overlapping triples into an unordered pair of unordered pairs, and partition the remaining \(3(r-2)\) points into \(r-2\) unordered triples. The result is
\[
\frac{n!}{(2!)\,(2!)^2\,(2!)\,6^{r-2}(r-2)!}
=\frac{n!}{16\cdot6^{r-2}(r-2)!}.
\]
The four factorial factors respectively account for the two unused points, two two-point branches, and swapping the two overlapping blocks. This is a bijection, so there is no overcount. Summing both \(s=1\) types completes the proof. \(\square\)

## Verification

The standalone file `check_supports.cpp` enumerates every possible defender subset able to reach the claimed weight for \(8\le n\le12\). It computes ordinary Kneser graph distances by breadth-first search, checks the distance-two characterization, determines all forced label-one triples, and directly tests both hop defense and the no-positive-isolates requirement. Its exhaustive counts are \(280,840,40600,15400,61600\). The independent `check_formula.py` computes the factorial formula for \(8\le n\le18\) and enumerates the two structural types at order ten, yielding \(2800\) disjoint and \(37800\) one-overlap optima. The construction verifier `check_constructions.py` checks explicit functions against the definition for \(8\le n\le20\), including the overlap case. Use `sh run_checks.sh` in a directory containing the supplied scripts; `verification_output.txt` contains the actual expected output. These finite computations are reproducibility checks; the all-order proof is the preceding structural argument.

## Relationship to prior work

Abdollahzadeh Ahangar, Chellali, Sheikholeslami and Soroudi [1] introduced hop-total Roman domination, specifically the distance-exactly-two defender requirement together with ordinary-adjacency totality, and studied paths, cycles, general structural bounds, and complexity. The present result fixes instead the entire three-subset Kneser family and counts all minima. The article's accessible abstract and indexed sections did not reveal a Kneser formula, but complete page-by-page inspection was not possible; this is an explicit priority limitation.

Zec and Grbić [2] investigate ordinary Roman, total Roman, and signed Roman domination on Kneser graphs. Their ordinary and total Roman minimum of \(2(k+1)\) applies to \(\operatorname{KG}(n,k)\) when \(n\ge k(k+1)\), but those functions defend zeros through adjacency (disjoint triples), whereas hop-total Roman functions defend zeros via distance two (intersecting triples). Their theorem therefore neither implies nor contradicts the present residue-dependent minimum and optimizer census. The full authorized open-access article, including its theorem and conclusion, was inspected for this comparison.

The published Roman-domination polynomial of triangular graphs [3] concerns two-subset intersection graphs and ordinary Roman defense. The published Kneser total-Roman reconfiguration theorem [4] concerns optimum **adjacency-based** total Roman functions of arbitrary rank; its claimed optimum is independent of large \(n\) when the rank is fixed. Both articles were compared at statement and proof level, not only by matching titles. Neither implies the current three-subset hop-total classification. Published results on hop-total Roman weight polynomials of matching-deleted bicliques likewise concern a different graph family [5]. A related reformulation is domination by intersection in the three-uniform complete hypergraph with the ordinary disjointness-based totality constraint; potential equivalent earlier work under that terminology is an originality risk.

## Limitations

The rank is fixed to three, the ground-set size is at least eight, and the theorem enumerates minimum-weight functions only, not all feasible functions or reconfiguration edges. The proof does not settle larger Kneser ranks, graph families of diameter greater than two, or the minimum for the small non-diameter-two boundary. No unindexed-publication priority guarantee or independent external validation is asserted. Computations cross-check the result but do not substitute for the infinite proof.

## References

1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, and M. Soroudi, “Hop total Roman domination in graphs,” *AKCE International Journal of Graphs and Combinatorics* **20** (2023), 73–78. Published online 2023-03-30. DOI: https://doi.org/10.1080/09728600.2023.2184288
2. T. Zec and M. Grbić, “Several Roman domination graph invariants on Kneser graphs,” *Discrete Mathematics & Theoretical Computer Science* **25** (2023), article 14. First public arXiv version 2022-04-12. https://arxiv.org/abs/2204.05664 ; DOI: https://doi.org/10.46298/dmtcs.10506
3. “Roman-domination polynomial of triangular graphs, with minimum-function census,” public result, 2026-10-13. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-roman-domination-polynomial-of-triangular-graphs-with-minimum-fu--66092f59608f
4. “A sharp token-sliding mobility transition for optimal total Roman functions on Kneser graphs,” public result, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-token-sliding-mobility-transition-for-optimal-total-roma--a3f3d09e0ceb
5. “Affine hop-total-Roman weight polynomials under matching deletion from complete bipartite graphs,” public result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-affine-hop-total-roman-weight-polynomials-under-matching-deletio--c53bd47d7c27
