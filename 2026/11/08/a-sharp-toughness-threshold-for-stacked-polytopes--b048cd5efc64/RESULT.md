# A sharp toughness threshold for stacked polytopes

## Finding

Let \(P\) be a stacked convex polytope of dimension \(d\ge4\), formed from a simplex by successive stackings on exposed facets, and let \(G(P)\) be its vertex-edge graph. For a vertex subset \(S\), let \(\omega(G(P)-S)\) count the connected components of the graph induced by the vertices outside \(S\), taking this count to be zero if none remain.

**Facet-budget separator theorem.** For every nonempty \(S\subseteq V(G(P))\),
\[
\omega(G(P)-S)\le(d-1)|S|-(d-2).
\]
Consequently, every finite stacked \(d\)-polytope has graph toughness strictly larger than \(1/(d-1)\), where the toughness of a complete graph is conventionally infinite. This strict bound is best possible over the class:
\[
\inf\{\tau(G(P)):P\text{ is a stacked }d\text{-polytope}\}=\frac{1}{d-1}.
\]
The infimum is not attained. More precisely, there are explicit stacked polytopes \(P_N\) with
\[
\frac1{d-1}<\tau(G(P_N))\le\frac{N}{(d-1)N-(d-2)(d+1)},\qquad N\ge d+2.
\]

## Assumptions and scope

The polytope is convex and simplicial, and the stacking process always replaces one **currently exposed** simplex facet by the \(d\) new facets meeting the new vertex. The graph has edges between the new vertex and exactly the \(d\) vertices of the chosen facet, and no new edges between previous vertices. These statements follow from the combinatorial definition of a stacked convex polytope. The proof below is independent of any metric realization of its vertices. Toughness is
\[
\tau(G)=\min_{S:\,\omega(G-S)\ge2}\frac{|S|}{\omega(G-S)}
\]
for noncomplete graphs, and is infinite for complete graphs. Only dimensions \(d\ge4\) are claimed as the new sharp higher-dimensional regime; the argument also works in dimension three, which has separate classical planar constraints.

## Proof

Fix a nonempty set \(S\) of vertices of the final stacked polytope. Traverse one fixed stacking sequence from its original \(d\)-simplex. At each stage \(t\), write \(G_t\) for the current graph, \(\mathcal F_t\) for the set of exposed \(d\)-vertex facets, \(s_t=|S\cap V(G_t)|\), \(c_t=\omega(G_t-(S\cap V(G_t)))\), and
\[
a_t=\#\{F\in\mathcal F_t:F\subseteq S\}.
\]
Define the integer **facet budget** \(b_t=(d-1)s_t-c_t-a_t\).

We first show that \(b_t\) never decreases. When a vertex \(v\in S\) is stacked on an exposed facet \(F\), deletion of \(S\) also deletes \(v\), so \(c_t\) is unchanged, while \(s_t\) increases by one. The old facet is removed and \(d\) new facets appear. If \(F\subseteq S\), all \(d\) new facets are contained in \(S\), giving an increase of exactly \(d-1\) in \(a_t\). If \(F\not\subseteq S\), at most one new facet can be contained in \(S\), so the increase in \(a_t\) is at most one. In either case \(a_t-a_{t-1}\le d-1\), hence \(b_t\ge b_{t-1}\).

When \(v\notin S\), no new facet can be contained in \(S\). If \(F\subseteq S\), the new surviving vertex is isolated in \(G_t-S\): the number of components increases by one while \(a_t\) decreases by one. If \(F\not\subseteq S\), its surviving vertices are mutually adjacent, being vertices of a simplex facet, so the new vertex joins an existing component without merging distinct ones; both \(c_t\) and \(a_t\) stay unchanged. Thus \(b_t=b_{t-1}\) in either case.

Write \(s_0\) for the number of original simplex vertices in \(S\). If \(1\le s_0\le d-1\), the original surviving simplex vertices form one component and no facet is wholly deleted: \(c_0=1\), \(a_0=0\), so \(b_0=(d-1)s_0-1\ge d-2\). If \(s_0=d\), then \(c_0=1\) and \(a_0=1\), so \(b_0=d(d-1)-2\ge d-2\). If \(s_0=d+1\), then \(c_0=0\) and \(a_0=d+1\), giving \(b_0=(d+1)(d-2)\ge d-2\).

Finally, if \(s_0=0\), consider the first newly stacked vertex that belongs to \(S\), which must exist because \(S\ne\varnothing\). Before that step all existing vertices survive, so \(c=1\) and \(a=0\). Immediately after stacking that vertex, it is deleted, leaving \(c=1\) and \(a=0\), while \(s=1\); therefore \(b=d-2\). Monotonicity then gives \(b_{\mathrm{final}}\ge d-2\). In all cases, since \(a_{\mathrm{final}}\ge0\),
\[
(d-1)|S|-\omega(G(P)-S)=b_{\mathrm{final}}+a_{\mathrm{final}}\ge d-2.
\]
This proves the claimed component inequality.

For any separator \(S\) with \(\omega(G(P)-S)\ge2\), the bound yields \((d-1)|S|\ge\omega(G(P)-S)+(d-2)>\omega(G(P)-S)\), so the ratio defining toughness is strictly greater than \(1/(d-1)\). The graph is finite, hence its minimum over separators is strict. A simplex has infinite toughness by convention.

For sharpness, choose any stacked \(d\)-polytope \(Q_N\) with \(N\ge d+2\) vertices. Its number of facets is exactly
\[
F_N=(d+1)+(d-1)(N-d-1)=(d-1)N-(d-2)(d+1),
\]
because each stacking adds one vertex and replaces one facet by \(d\) facets. Stack once on **each original facet** of \(Q_N\), retaining the remaining original facets at every step, and call the resulting stacked polytope \(P_N\) (the Kleetope of \(Q_N\)). The \(F_N\) new vertices are pairwise nonadjacent and each is joined only to vertices of its corresponding original facet, as also recorded in Proposition 2.6 of Pineda-Villavicencio (2026). Deleting the \(N\) original vertices therefore leaves exactly \(F_N\) isolated vertices. Hence \(\tau(G(P_N))\le N/F_N\to1/(d-1)\), proving sharpness and nonattainment.

## Verification

The self-contained standard-library script `verify.py` reconstructs exposed facets and adjacency after each stacking, exhaustively checks all nonempty vertex cuts for multiple small stacked examples in dimensions four through six (and includes dimension three as a consistency test), and constructs Kleetopes to verify the independent-apex count and exact facet formula in dimensions three through six. It completed 35,816 complete cut checks and 32 exact Kleetope construction checks without failure. These finite tests are auxiliary; the monotone facet-budget proof covers arbitrary stacking sequences and all dimensions in the stated range.

## Relationship to prior work

Pineda-Villavicencio (2026, arXiv:2610.12836, submitted 2026-10-09) proved that for every dimension at least four and every prescribed connectivity at least the dimension, there exist simplicial polytopes of arbitrarily small graph toughness. That theorem uses Kleetope constructions and states their independence property in Proposition 2.6, but does not assert a universal positive toughness threshold for the **stacked** subclass. The present sharp lower bound therefore separates a natural geometrically restricted subclass from the larger class of simplicial polytopes.

Chen (2016) supplies the characterization of stacked polytopal graphs among \(d\)-trees and thus clarifies the significance of the exposed-facet restriction. Markenzon and Waga (2020) study toughness of planar Apollonian networks (dimension three) and their subclasses. Kabela (2017/2019) studies toughness thresholds **implying Hamiltonicity** in general \(k\)-trees, not a universal sharp lower bound for the higher-dimensional stacked-polytopal subclass. The cited results do not by themselves imply the facet-budget inequality. Priority beyond the inspected texts has not been independently confirmed.

## Limitations

The uniform threshold applies only to stacked polytopes and need not hold for arbitrary simplicial polytopes or arbitrary \(d\)-trees. The additive separator inequality need not be optimal for each fixed polytope or fixed number of vertices. The theorem finds the infimum of toughness across stacked polytopes, not an exact formula for the toughness of each finite example. The numerical verifier cannot certify infinitely many stacking sequences; the proof does that analytically. Historical priority and correctness have not undergone an independent audit.

## References

1. G. Pineda-Villavicencio, *Connectivity, toughness, and hamiltonicity of simplicial polytopes*, arXiv:2610.12836 (first submitted 2026-10-09), particularly Theorem 1.5 and Proposition 2.6. https://arxiv.org/abs/2610.12836
2. H. Chen, *Apollonian Ball Packings and Stacked Polytopes*, Discrete & Computational Geometry 55 (2016), 801–826, DOI:10.1007/s00454-016-9777-3, particularly Section 2.4. https://link.springer.com/article/10.1007/s00454-016-9777-3
3. L. Markenzon and C. F. E. M. Waga, *Toughness and Hamiltonicity in Random Apollonian Networks*, arXiv:2002.09244 (2020), particularly Sections 4 and 6. https://arxiv.org/abs/2002.09244
4. A. Kabela, *Long paths and toughness of k-trees and chordal planar graphs*, arXiv:1707.08026 (2017), later Discrete Mathematics 342 (2019), particularly Sections 1, 3, 5 and 6. https://arxiv.org/abs/1707.08026
