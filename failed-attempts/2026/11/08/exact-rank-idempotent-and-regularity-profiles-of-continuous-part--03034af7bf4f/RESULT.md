# Exact rank, idempotent and regularity profiles of continuous partial maps on finite stars

## Finding
For every integer \(n\ge1\), let \(\Gamma_n=K_{1,n}\) have center \(0\) and leaves \(1,\ldots,n\). Let \(M_n=\operatorname{MR}(\Gamma_n)\) be the monoid of partial maps of its vertices for which the full inverse image of each vertex or edge is empty, a singleton, or an edge. The rank \(\rho(f)\) of a partial map is the cardinality of its image. Put \(\binom ab=0\) unless \(0\le b\le a\), and put \((a)_{\underline b}=a!/(a-b)!\) for \(0\le b\le a\), and zero otherwise.

For each \(0\le k\le n+1\), the total number of rank-\(k\) maps is
\[
R_{n,k}=\binom nk(n+1)_{\underline k}+n^2\binom{n-1}{k-1}(n-1)_{\underline{k-1}}+\binom n{k-1}n_{\underline{k-1}}+2n\,[k=1]+n^2\,[k=2].
\]
The number of rank-\(k\) idempotents is
\[
E_{n,k}=(k+1)\binom nk+\binom n{k-1}+n\,[k=1],
\]
so the total number of idempotents is
\[
\sum_kE_{n,k}=2^{n+1}+n2^{n-1}+n.
\]
The number of nonregular elements of rank \(k\) is exactly
\[
B_{n,k}=\begin{cases}\binom n{k-1}(n)_{\underline k},&2\le k\le n,\\0,&\text{otherwise}.\end{cases}
\]
An element is nonregular if and only if it is injective, its image consists solely of leaves, and its domain contains both the center and at least one leaf. Thus \(R_{n,k}-B_{n,k}\) is the exact number of regular elements of rank \(k\). Here regular means that some \(g\in M_n\) satisfies \(fgf=f\), with partial-map composition.

## Assumptions and scope
A face of \(\Gamma_n\) means one vertex or an edge \(\{0,i\}\). The empty set is also allowed as a preimage. A partial function is represented with undefined values outside its domain. Rank zero is the empty map. The proof holds for all positive \(n\), including the exceptional case \(n=1\) in which the star is the complete graph \(K_2\). No graph-theoretic forward-homomorphism condition is imposed; the condition here is inverse-image continuity.

## Proof
Write \(H=f^{-1}(\{0\})\), and for each leaf \(i\) write \(F_i=f^{-1}(\{i\})\). Inverse-image continuity says each nonempty \(H\), \(F_i\), and \(H\cup F_i\) is a face; the fibers are pairwise disjoint.

**Complete case analysis.** If \(H=\varnothing\), either all occupied fibers \(F_i\) are singletons, giving an arbitrary injection from a subset of the \(n+1\) source vertices into the \(n\) target leaves, or exactly one occupied fiber is the edge \(\{0,j\}\), and every other occupied fiber is a singleton of a different source leaf. There cannot be two doubled fibers since each would contain \(0\). For rank \(k\), the first type has \(\binom nk(n+1)_{\underline k}\) choices: choose \(k\) target leaves and inject their preimages into the \(n+1\) sources. The second has \(n\) choices for \(j\), \(n\) choices for the target of its doubled fiber, and \(\binom{n-1}{k-1}(n-1)_{\underline{k-1}}\) choices for the remaining leaf-to-leaf injection.

If \(H\neq\varnothing\), there are precisely three possibilities. If \(H=\{0\}\), the other nonempty fibers are singletons of distinct leaves, with \(\binom n{k-1}n_{\underline{k-1}}\) choices at rank \(k\). If \(H=\{j\}\) for a leaf \(j\), there may be no further occupied fiber (\(n\) rank-one maps), or precisely one further fiber \(F_i=\{0\}\), with \(n^2\) rank-two maps. Finally, if \(H=\{0,j\}\), there can be no other occupied fiber, giving \(n\) rank-one maps. The cases are mutually exclusive and exhaustive. Their sum is \(R_{n,k}\), with the empty map counted by the first case.

**Idempotents.** A partial transformation \(f\) is idempotent exactly when it fixes every point in its image. If \(0\) is absent from the image, select \(k\) image leaves. They must be fixed, and the source center is either undefined or may map to any one of those \(k\) leaves: \((k+1)\binom nk\) choices. If \(0\) is in the image, its preimage must contain \(0\). When it is the singleton \(\{0\}\), select and fix \(k-1\) leaves, giving \(\binom n{k-1}\) choices. When it is an edge \(\{0,j\}\), the map has rank one, with \(n\) choices for \(j\). Summation gives the stated idempotent profile and total, using \(\sum_k k\binom nk=n2^{n-1}\).

**Regularity.** If \(fgf=f\), the restriction of \(g\) to the image of \(f\) selects one source representative from each fiber of \(f\). Conversely, a continuous partial section \(g\) on that image implies \(fgf=f\). Restricting a continuous map preserves inverse-image continuity, so existence of any generalized inverse is equivalent to existence of such a section.

In every case except one, a continuous section can be chosen: when \(H=\varnothing\) and all fibers are singletons and the source center is absent, the unique representatives are source leaves; when the source center is present but the image is a singleton, the one-point section is continuous; in the doubled-fiber case, choose the leaf (rather than \(0\)) from the doubled fiber, so again all selected representatives are leaves. When \(H=\{0\}\), the section fixes the center and maps each target leaf to its distinct source leaf, preserving edges under inverse images. When \(H\) is a singleton leaf, its rank is at most two; if two, the selected representatives of the center and one target leaf are respectively a leaf and the source center, which form an edge. When \(H=\{0,j\}\), the rank is one and any section is continuous.

The excluded case is a single-fiber/injective map \(f\) whose center \(0\) is in the domain and whose leaf-only image has size at least two. Here the unique section would send two distinct target leaves to the source center and one of its leaves. The full inverse image of that source edge under the section would contain those two distinct, nonadjacent target leaves, so the section is not continuous. No other generalized inverse can exist. For rank \(k\), select \(k-1\) source leaves alongside \(0\), then inject the \(k\) chosen source vertices into the target leaves: \(\binom n{k-1}(n)_{\underline k}\). This proves both the criterion and \(B_{n,k}\).

## Verification
Run \(\texttt{python3 star\_mr\_verify.py}\) with Python 3 and no external packages. The program independently enumerates all partial vertex maps for stars with \(1\le n\le5\), tests each source simplex preimage against the face list, counts ranks and idempotents, and searches all fiberwise sections for regularity; it compares every rank with the displayed formulas. The observed monoid orders are \(9,36,185,1278,10857\); all \(12{,}365\) directly enumerated valid maps and \(25\) rank strata agree. Verification output is in \(\texttt{verification\_output.txt}\). The finite checks support but do not replace the unrestricted proof.

## Relationship to prior work
Margolis and Rhodes introduced the inverse-image continuous map monoid and its general singular/injective decomposition in their 2020 preprint and 2021 journal article. Their September 2026 paper develops the ideal structure and explicit enumerations for paths and cycles, and proves that \(\operatorname{MR}(\Gamma)\) is regular only for empty or complete graphs. The present result is the exact rankwise, idempotent and regular/nonregular distribution for the branching family of stars; it does not claim to introduce the monoid, its abstract continuity criterion or the general nonregularity theorem. Dimitrova, Fernandes and Koppitz study a different collection of *forward-edge-preserving* partial endomorphism monoids of stars (2024), not these inverse-image continuous maps. Their cardinality formulas therefore do not imply the displayed profiles.

## Limitations
The graph family is exactly the star \(K_{1,n}\), not arbitrary trees or complete bipartite graphs. No claim is made about Krohn–Rhodes complexity or minimal generating ranks. The general partial-map decomposition and the qualitative statement that the star monoid is not regular for \(n\ge2\) are prior results. The formula-level priority assessment is based on accessible literature; unnoticed earlier enumerations under different terminology remain a possibility. All publication and scientific review statuses are non-independent.

## References
1. S. Margolis and J. Rhodes, *The Margolis-Rhodes Monoid of a Graph*, arXiv:2609.39370v1 (first posted 2026-09-30), https://arxiv.org/abs/2609.39370 .
2. S. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606 (first posted 2020-05-06), https://arxiv.org/abs/2005.02606 .
3. I. Dimitrova, V. H. Fernandes and J. Koppitz, *On partial endomorphisms of a star graph*, arXiv:2401.11741 (first posted 2024-01-22), https://arxiv.org/abs/2401.11741 .
4. S. Margolis and J. Rhodes, *Degree 2 transformation semigroups as continuous maps on graphs: Complexity and examples*, International Journal of Algebra and Computation 33 (2023), 289–316, https://doi.org/10.1142/S0218196723500157 .
