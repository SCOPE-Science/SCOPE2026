# Rank spectra and sharp extension cutoff in asymmetric biclique partial-automorphism monoids

## Finding

For integers \(a>b\ge1\), let \(G=K_{a,b}\) be the finite simple complete bipartite graph with distinguished vertex classes of sizes \(a\) and \(b\). Let \(\operatorname{PAut}(G)\) be the inverse monoid of all bijections between vertex-induced subgraphs of \(G\). For a partial automorphism \(f\), its rank is \(|\operatorname{dom}f|\). Call \(f\) **extendible** if it is a restriction of an automorphism of the entire graph. Define the rook polynomial and the cross-class partial-matching polynomial by
\[
 R_s(z)=\sum_{k=0}^s\binom{s}{k}^{\!2} k!z^k,\qquad
 C_{a,b}(z)=\sum_{k=1}^{b}\binom ak\binom bk k!z^k.
\]
Then the complete rank enumerators of extendible and nonextendible elements are, respectively,
\[
\boxed{E_{a,b}(z)=R_a(z)R_b(z)},\qquad
\boxed{N_{a,b}(z)=C_{a,b}(z)\big(C_{a,b}(z)+2\big)}.
\]
Consequently the complete element-rank polynomial is
\[
\boxed{F_{a,b}(z)=R_a(z)R_b(z)+C_{a,b}(z)^2+2C_{a,b}(z).}
\]
The nonextendible rank spectrum is **exactly** \(\{1,2,\ldots,2b\}\): every partial automorphism of rank greater than \(2b\) extends to a full graph automorphism, and the number of nonextendible elements at the sharp boundary is exactly
\[
\boxed{[z^{2b}]N_{a,b}(z)=\binom ab^{\!2}(b!)^2.}
\]
The balanced case \(a=b\) is different: every partial automorphism extends and the known homogeneous-graph formula specializes to \(F_{a,a}(z)=2R_a(z)^2-1\). This balanced case is included only to delimit the new asymmetric claim, not claimed as an independent result.

For example, when \((a,b)=(3,2)\),
\[
N_{3,2}(z)=12z+48z^2+72z^3+36z^4,
\]
\[
F_{3,2}(z)=1+25z+104z^2+168z^3+96z^4+12z^5.
\]

## Assumptions and scope

The graph is finite, undirected, loopless, and **vertex-induced** subgraph isomorphisms are required; arbitrary graph homomorphisms, non-induced subgraph isomorphisms, and non-injective partial transformations are not counted. The theorem assumes integers \(a>b\ge1\) and hence a uniquely degree-distinguished bipartition. The empty partial map is included once and is extendible, contributing the constant coefficient \(1\). The words *rank* and *extension* always mean domain cardinality and restriction of an actual global graph automorphism, not generator rank or extension to a larger graph. Every coefficient counts distinct partial maps rather than distinct ways to extend them. No analytic asymptotic is needed.

## Proof

**1. Classification of possible domains and images.** Let \(A\) and \(B\) be the two vertex classes. A nonempty induced subgraph on \(D\subseteq A\cup B\) is edgeless exactly when \(D\) lies wholly in one vertex class. Otherwise its induced subgraph is the connected complete bipartite graph on \(D\cap A\) and \(D\cap B\), both nonempty. An induced-subgraph isomorphism between two nonempty mixed induced subgraphs must either preserve or interchange their two unique bipartitions. This remains valid when both class sizes within the induced subgraph are one, because the unique bipartition into independent classes is defined up to interchange. Conversely, every class-preserving or class-interchanging pair of partial injections (with both source classes occupied in the mixed case) is an induced-subgraph isomorphism.

**2. Which maps extend.** A vertex of \(A\) has degree \(b\), and a vertex of \(B\) has degree \(a\). Since \(a>b\), every global automorphism preserves both vertex classes. Conversely, any pair of permutations of \(A\) and \(B\) is a global automorphism, and any partial injection within each class extends to a permutation of that class. Therefore the extendible partial automorphisms are exactly the class-preserving partial bijections. The number of partial injections of domain size \(k\) from one \(s\)-set into itself is \(\binom sk^2k!\), hence their rank polynomial is \(R_s(z)\). Their independent choices in \(A\) and \(B\) prove \(E_{a,b}=R_aR_b\).

**3. Unique classification of obstructions.** A nonextendible partial automorphism must interchange the vertex classes on every occupied portion of its domain. There are exactly three mutually disjoint types: (i) a nonempty partial injection \(A\to B\) with no domain points in \(B\); (ii) a nonempty partial injection \(B\to A\) with no domain points in \(A\); or (iii) the disjoint union of a nonempty injection \(A\to B\) and a nonempty injection \(B\to A\). These cases exhaust the edgeless and mixed-domain cases from Step 1, and the direction and components are uniquely recoverable from the map. For \(1\le k\le b\), each cross-class partial injection of rank \(k\) has \(\binom ak\binom bk k!\) choices. Thus the first two types contribute \(2C_{a,b}(z)\) and the third contributes \(C_{a,b}(z)^2\). This yields the displayed factorization \(N=C(C+2)\) and, by disjoint union, \(F=E+N\).

**4. Sharp boundary and no rank gaps.** The coefficient of \(z^k\) in \(C\) is strictly positive for each integer \(1\le k\le b\) and vanishes elsewhere. Therefore \(2C\) supplies all ranks \(1\) through \(b\). For \(b<k\le2b\), choose two integers \(i,j\) with \(1\le i,j\le b\) and \(i+j=k\); the product \(C^2\) gives a strictly positive contribution. Since \(\deg N=2b\), no higher nonextendible rank is possible. The leading coefficient comes solely from the product of the two leading coefficients of \(C\); each leading coefficient equals \(\binom ab b!\). This proves the sharp cutoff and its exact population.

**5. Balanced comparison.** If \(a=b\), the whole-graph automorphism group also interchanges \(A\) and \(B\). Every induced-subgraph partial automorphism from Step 1 is then a restriction of a side-preserving or side-exchanging permutation, so no nonextendible maps occur. Here \(C_{a,a}=R_a-1\), giving \(R_a^2+(R_a-1)^2+2(R_a-1)=2R_a^2-1\). This is a boundary comparison with the previously established homogeneous case, not a separate novelty assertion.

## Verification

The standalone Python 3 file `verify.py` implements direct enumeration of **all partial injections** on the underlying labeled vertex set (not just the three structural types), tests preservation of adjacency and nonadjacency for every pair in the domain, and tests whether each valid map preserves classes or, in the balanced case, exchanges them globally. It independently computes the three displayed generating polynomials from integer binomial coefficients, and checks the resulting coefficient vectors for \((a,b)=(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,2),(5,1)\). The test prints `PASS` after all identities hold. Some checks involve thousands of raw partial injections. The proof above, not the finite testing, establishes the result for all \(a>b\ge1\).

## Relationship to prior work

Chih and Plessas (2015, arXiv:1506.02093) introduce four graph-based inverse semigroups, including isomorphisms of vertex-induced subgraphs, and study their idempotent semilattices and ideals. Their definitions match the induced-subgraph object used here, but their structural classification does not give the asymmetric biclique rank-refined extension counts.

Jajcay, Jajcayová, Szakács and Szendrei (2018, arXiv:1809.04422) develop inverse monoids of partial graph automorphisms and characterize which inverse submonoids arise from graphs. Their rank-one/rank-two membership criterion is consistent with Step 1, but does not supply the present all-rank square-factorization or sharp obstruction threshold. Both public arXiv texts were materially inspected beyond abstracts.

The previously established rank spectra for **finite homogeneous graphs** include the balanced complete bipartite graphs \(K_{a,a}\), because these are complements of two equal cliques. The asymmetric graphs \(K_{a,b}\) with \(a>b\) are not homogeneous, and the new nonextendible polynomial cannot be deduced by simply substituting unequal clique sizes into that homogeneous classification. Published square-zero rank distributions for partial isometries of complete multipartite graphs concern only the subfamily satisfying \(f^2=0\), whereas the present theorem counts *all* partial automorphisms and distinguishes extendibility. The underlying rook counts are classical; no originality is claimed for their individual coefficients.

## Limitations

This is an exact theorem only for two nonempty classes, with the nontrivial new content for unequal class sizes. It does not classify extension obstructions for three or more vertex classes, general bipartite graphs, or arbitrary graph-metric partial isometries, nor does it claim a new general theorem about homogeneous graphs. The factorization is elementary once the natural bipartition classification has been established; broader formulas for partial isomorphism monoids or rook-polynomial constructions may already imply it, and complete historical priority is not certified. Direct testing is finite; no independent mathematical audit has been performed.

## References

1. T. Chih and D. Plessas, *Graphs and Their Associated Inverse Semigroups*, arXiv:1506.02093, first posted 2015-06-06, https://arxiv.org/abs/1506.02093 .
2. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first posted 2018-09-12, https://arxiv.org/abs/1809.04422 .
3. A. Gardiner, *Homogeneous graphs*, Journal of Combinatorial Theory Series B 20 (1976), 94–102 (classical finite homogeneous classification; referenced for context, not re-proved here).
4. *Rank spectra and Gaussian deficiency laws for finite homogeneous graph partial automorphisms* (published 2026-11-02; homogeneous rank census; equality-class overlap only).
5. *The complete square-zero rank distribution of multipartite partial-isometry monoids* (published 2026-10-26; covers square-zero subfamily, not the present unrestricted element census).
