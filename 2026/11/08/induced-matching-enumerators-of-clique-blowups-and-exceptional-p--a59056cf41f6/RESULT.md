# Induced-matching enumerators of clique blowups and exceptional purity on cyclic bases

## Finding

Let \(G\) be any finite simple graph and let \(m\ge2\) be an integer. Its uniform clique blowup is \(H=G[K_m]\), with fiber \(\{v\}\times[m]\) over each vertex of \(G\); two different fibers are completely joined precisely when the corresponding base vertices are adjacent. An **induced matching** is a set of disjoint edges with no additional edges among its endpoints. An induced matching is **inclusion-maximal** if no other edge can be adjoined while retaining this property.

Put \(a=\binom m2\) and \(b=m^2\). A **dissociation set** \(S\subseteq V(G)\) is a vertex set for which \(G[S]\) has maximum degree at most one; let \(c_1(S)\) count its isolated vertices and \(c_2(S)\) count its two-vertex components. The number of induced matchings of each size in \(G[K_m]\) is encoded exactly by
\[
I_{G[K_m]}(z)=
\sum_{\substack{S\subseteq V(G)\\ \Delta(G[S])\le1}}
a^{c_1(S)}b^{c_2(S)}z^{c_1(S)+c_2(S)}.
\]
The empty set contributes \(1\). The polynomial counting **inclusion-maximal** induced matchings is
\[
M_{G[K_m]}(z)=
\sum_{\substack{S\subseteq V(G)\\\Delta(G[S])\le1\\N_G[S]=V(G)}}
a^{c_1(S)}b^{c_2(S)}z^{c_1(S)+c_2(S)}.
\]
Here \(N_G[S]\) is the closed neighborhood of \(S\). Both formulas count *labelled matchings*, not just their isomorphism types.

For \(G=C_n\), \(n\ge3\), the maximal polynomial has the finite closed form
\[
\boxed{
M_{C_n[K_m]}(z)=
\sum_{k=\lceil n/4\rceil}^{\lfloor n/2\rfloor}
\frac{n}{k}
\sum_{p=\max(0,n-3k)}^{\min(k,n-2k)}
\binom{k}{p}\binom{k}{n-2k-p}
a^{k-p}b^p z^k.
}
\]
In particular, every integer \(k\) with \(\lceil n/4\rceil\le k\le\lfloor n/2\rfloor\) occurs as the cardinality of an inclusion-maximal induced matching. The induced-matching simplicial complex (whose vertices are the edges of \(H\)) is **pure**, equivalently \(H\) is well-indumatched, exactly for \(n\in\{3,5\}\). This assertion holds for every \(m\ge2\).

## Assumptions and scope

All graphs are finite, simple, and undirected, and all subsets, edges, and matchings are labelled. Isolated base vertices are allowed in the general polynomial identities. Throughout, \(m\ge2\); for \(m=1\) the ability to adjoin an internal edge in an undominated fiber fails and the maximality characterization changes. Cycles have \(n\ge3\). The empty matching is included in the all-matchings polynomial; if \(G\) has no vertices then the empty matching is the unique maximal matching as well.

For the cycle count, a cyclic binary word of length \(n\) is indexed by the actual labelled vertices \(0,\ldots,n-1\), including the \(n=3\) triangle. A run is a maximal cyclic consecutive block. An occupied fiber is represented by a one; an unoccupied fiber by a zero.

## Proof

**1. Projection and a weight-preserving bijection.** Given an induced matching \(Q\) in \(H=G[K_m]\), let \(S\) be the set of base vertices whose fibers contain endpoints of edges of \(Q\). If an edge of \(Q\) has endpoints in a single fiber over \(v\), that fiber contains exactly two endpoints and contributes an isolated vertex \(v\) to \(G[S]\): any adjacent occupied base vertex would introduce a forbidden cross-edge between endpoints. If an edge of \(Q\) crosses the adjacent fibers over \(u,v\), these are the only occupied neighbors of one another in \(G[S]\), since any further occupied neighbor would create a forbidden cross-edge. No fiber can meet two different matching edges because its vertices are pairwise adjacent. Thus \(G[S]\) is a disjoint union of isolated vertices and edges; each isolated vertex corresponds to one internal matching edge, and each base edge corresponds to one cross-fiber matching edge.

Conversely, for every dissociation set \(S\), choose one of the \(a=\binom m2\) internal edges in each isolated fiber and one of the \(b=m^2\) cross-fiber edges for each two-vertex component of \(G[S]\). These chosen edges form an induced matching, and the construction is inverse to projection. Exactly \(c_1(S)+c_2(S)\) edges are selected, proving the first polynomial.

**2. Maximality is exactly domination of support.** Let \(S\) be the occupied base support. If some \(v\notin N_G[S]\), the whole fiber over \(v\) has no edges to the endpoints of the matching. Since \(m\ge2\), an internal edge in that fiber can be adjoined, so the matching was not maximal. Conversely, if \(N_G[S]=V(G)\), every as-yet-unused edge has an endpoint in a fiber over a vertex of \(N_G[S]\). If its fiber is occupied, this endpoint is adjacent to an endpoint already selected unless it is literally a previously selected endpoint (then the edge is unusable). If its fiber is unoccupied but adjacent to an occupied fiber, it is adjacent to an endpoint in that neighboring occupied fiber. Therefore no new edge can be adjoined. This proves the second polynomial, including graphs with isolated vertices.

**3. Cyclic admissibility.** A binary cyclic support is dissociated if and only if it has no three consecutive ones: a vertex in the center of \(111\) would have two neighbors in the support. The support dominates the cycle if and only if it has no three consecutive zeros: the center of \(000\) would be outside the closed neighborhood. Therefore the supports of maximal induced matchings on \(C_n[K_m]\) are exactly the cyclic words avoiding both \(000\) and \(111\). They are nonconstant, have exactly \(k\ge1\) one-runs and \(k\) zero-runs, and each run has length either one or two.

Each one-run of length one contributes an internal edge with weight \(az\); each one-run of length two contributes a cross-fiber edge with weight \(bz\). A zero-run contributes weight \(1\). Let \(p\) be the number of length-two one-runs and \(q\) the number of length-two zero-runs. With \(k\) alternating pairs of runs, the number of vertices is \(n=2k+p+q\), so \(q=n-2k-p\). The admissible conditions \(0\le p,q\le k\) are equivalent to the bounds in the stated inner sum.

For a fixed \(k,p,q\), there are \(\binom{k}{p}\binom{k}{q}\) ordered choices for the types of the \(k\) one-runs and \(k\) zero-runs. Select a distinguished first one-run and its initial labelled cycle vertex, giving \(n\) choices; each finished labelled word with \(k\) one-runs has been counted exactly \(k\) times. Thus the number of labelled supports is \((n/k)\binom{k}{p}\binom{k}{q}\). The weights give the closed polynomial.

Since \(2k\le n\le4k\), only \(\lceil n/4\rceil\le k\le\lfloor n/2\rfloor\) occur. Conversely for every integer in this interval, distribute the nonnegative integer \(n-2k\le2k\) among the \(2k\) runs, increasing each from length one to length two as necessary, producing an admissible word. All fiber-edge weights are strictly positive because \(m\ge2\); hence every such \(k\) genuinely occurs.

**4. Purity.** Facets of the induced-matching complex are maximal induced matchings, so purity means that the interval of possible facet sizes contains one integer. It has one integer precisely when \(\lceil n/4\rceil=\lfloor n/2\rfloor\). Directly \(n=3\) and \(n=5\) satisfy this equality, whereas \(n=4\) and every \(n\ge6\) do not (for \(n\ge6\), \(\lceil n/4\rceil\le\lfloor n/2\rfloor-1\)). This proves the characterization.

For instance, taking \(m=2\), the first maximal polynomials are \(M_{C_3[K_2]}=15z\), \(M_{C_4[K_2]}=16z+2z^2\), \(M_{C_5[K_2]}=25z^2\), \(M_{C_6[K_2]}=99z^2+2z^3\), making the nonmonotone purity boundary explicit.

## Verification

Run `python3 verify.py` using the accompanying standalone Python 3 file. It builds the product graph directly, independently enumerates every induced matching by its actual edge-compatibility relation, tests inclusion maximality against every unused graph edge, and compares the resulting all-set and maximal-set distributions with the support formulas. It tests all labelled base graphs on one through four vertices, each at clique sizes two and three, plus cyclic bases of lengths three through nine at the feasible tested clique sizes. Independently, a four-state trace transfer enumerator and the binomial formula are compared for all \(3\le n\le64\) and \(2\le m\le8\).

Observed successful output:
`VERIFY_OK base_profiles=150 cycle_profiles=11 independent_edge_matchings=14589 transfer_formula_cases=434 direct_all_and_maximal=PASS maximal_spectrum=PASS`.

These tests check only finite parameters. The general identities, cycle formula, support spectrum, and purity boundary are proved in the preceding arguments, not inferred from finite enumeration.

## Relationship to prior work

Brešar, Dravec, Hedžet, and Samadi (arXiv:2406.04020, first public June 6, 2024) give the scalar lexicographic-product identity \(\nu_I(G\circ H)=\alpha(G)\nu_I(H)\), including a structural proof based on projecting induced matchings to the base. For \(H=K_m\), their result yields the **maximum** induced matching size, which in this setting is \(\alpha(G)\). The present contribution is not that known extremal identity: it concerns *every* induced matching and *every* inclusion-maximal induced matching, with an exact weighted support bijection and the full cyclic facet-count distribution and purity criterion. Their projection reasoning provides an important precursor and could potentially be extended to recover portions of the argument.

Yuan, Yang, Zheng, and Gong (arXiv:2410.11288, first public October 15, 2024) study sharp global upper bounds on the number of maximal and maximum induced matchings in connected graphs; they do not give these cycle-clique-blowup coefficient formulas. Orlovich and Zverovich (DIMACS TR 2004-26) study the minimum/maximum cardinalities among maximal induced matchings in broad graph classes, not the present exact labelled distributions.

## Limitations

The results concern uniform clique blowups with \(m\ge2\); they do not purport to enumerate arbitrary \(G[H]\) when \(H\) is not complete. The class of all induced matchings is naturally hereditary, but the **support** family corresponding to maximal matchings is domination-restricted and is not hereditary. The structural bijection is elementary and some aspects may be implicit in previous lexicographic-product proofs; an unindexed prior equivalent all-configuration enumeration remains possible. The novelty and significance emphasized here are the explicit maximal-support characterization, complete cycle formula, sharp spectrum, and exceptional purity classification. No independent mathematical audit or external verification has been performed.

## References

- Boštjan Brešar, Tanja Dravec, Jaka Hedžet, and Babak Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first posted 2024-06-06). https://arxiv.org/abs/2406.04020.
- Bo-Jun Yuan, Zhao-Yu Yang, Lu Zheng, and Shi-Cai Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288 (first posted 2024-10-15). https://arxiv.org/abs/2410.11288.
- Yury L. Orlovich and Igor E. Zverovich, *Maximal induced matchings of minimum/maximum size*, DIMACS Technical Report 2004-26, abstract https://archive.dimacs.rutgers.edu/TechnicalReports/abstracts/2004/2004-26.html.
