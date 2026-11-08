# Exact geodesic transversal spectra and packing in crown graphs

## Finding

For every integer \(n\ge4\), the crown graph \(G_n=K_{n,n}-M_n\) has a complete structural description of its geodesic transversals and their inclusion-minimal members. Put \(V(G_n)=\{a_1,\ldots,a_n,b_1,\ldots,b_n\}\), with \(a_i b_j\) an edge precisely when \(i\ne j\). A *geodesic transversal* is a vertex set meeting every shortest path that is not a proper subpath of another shortest path.

The polynomial counting all geodesic transversals by cardinality is
\[
T_n(z)=(2z+z^2)^n+2nz^{n-1}(1+z)^{n-1}-nz^{2n-2}+\binom n2z^{2n-4}.
\]
The polynomial counting **inclusion-minimal** geodesic transversals is
\[
M_n(z)=2nz^{n-1}+(2^n-2n-2)z^n+\binom n2z^{2n-4}.
\]
Coefficients at equal powers are combined, notably for \(n=4\).

In particular, the minimum and maximum cardinalities of inclusion-minimal geodesic transversals are
\[
\operatorname{gt}(G_n)=n-1,\qquad
\operatorname{gt}^{+}(G_n)=\max\{n,2n-4\}.
\]
The exact attainable cardinalities are the support of \(M_n(z)\): \(\{3,4\}\) at \(n=4\), \(\{4,5,6\}\) at \(n=5\), and \(\{n-1,n,2n-4\}\) for \(n\ge6\). Thus the inclusion-minimal cardinality spectrum has arbitrarily long gaps. The geodesic-packing number is
\[
\operatorname{gpack}(G_n)=\left\lfloor\frac n2\right\rfloor,
\]
so the ratio \(\operatorname{gt}(G_n)/\operatorname{gpack}(G_n)\) tends to \(2\).

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted; all paths are simple. An unoriented geodesic is a shortest path between its endpoints. Maximality is under containment as a contiguous subpath, not by inclusion of its vertex set. A geodesic transversal meets the vertices of every maximal geodesic. An inclusion-minimal transversal ceases to be one after deletion of any chosen vertex. A geodesic packing is a collection of pairwise vertex-disjoint maximal geodesics. The statements concern every labeled crown graph \(G_n\) with integer \(n\ge4\); no assertion is made about weighted variants, other matching deletions, or other path conventions.

## Proof

**1. Exact maximal geodesics.** For distinct indices \(i,k\) in the same shore, \(d(a_i,a_k)=d(b_i,b_k)=2\). We have \(d(a_i,b_j)=1\) if \(i\ne j\), while \(d(a_i,b_i)=3\). The graph has diameter \(3\). Each length-two geodesic of the form \(a_i b_j a_k\), with \(i,j,k\) pairwise distinct, extends to the three-edge geodesic \(a_i b_j a_k b_i\); the symmetric assertion holds for geodesics beginning in the other shore. Each edge also extends to such a geodesic. Thus the **only** maximal geodesics, up to reversal, are
\[
a_i-b_j-a_k-b_i,\qquad i,j,k\text{ pairwise distinct}.
\]
There are exactly \(n(n-1)(n-2)\) of them.

**2. Exact hitting criterion.** For a candidate \(S\subseteq V(G_n)\), let \(R=\{i:a_i\notin S\}\), \(C=\{i:b_i\notin S\}\), and \(U=R\cap C\). A maximal geodesic disjoint from \(S\) exists if and only if there are pairwise distinct \(i,j,k\) with \(i\in U\), \(j\in C\setminus\{i\}\), and \(k\in R\setminus\{i\}\). Hence \(S\) is a transversal if and only if one of the following alternatives holds:

- \(U=\varnothing\) (each matched pair contains at least one selected vertex);
- \(U\ne\varnothing\) and \(|R|=1\) or \(|C|=1\);
- \(R=C=\{i,h\}\) for two distinct indices \(i,h\).

To establish necessity in the remaining case, suppose \(U\ne\varnothing\) and \(|R|,|C|\ge2\). Choose \(i\in U\). Since any choices \(j\in C\setminus\{i\}\) and \(k\in R\setminus\{i\}\) must then be equal, both nonempty sets must be the same singleton \(\{h\}\); thus \(R=C=\{i,h\}\). Conversely, each displayed alternative clearly precludes three distinct indices as above.

**3. All transversals.** The case \(U=\varnothing\) offers, independently for each index, a selection \(\{a_i\}\), \(\{b_i\}\), or \(\{a_i,b_i\}\), with weight \(2z+z^2\). If \(U\ne\varnothing\) and \(|R|=1\), the omitted index \(i\) lacks both \(a_i\) and \(b_i\), while all other \(a\)-vertices must be selected and the other \(b\)-vertices are arbitrary: weight \(nz^{n-1}(1+z)^{n-1}\). Interchanging shores contributes the same amount. The two counts overlap exactly on the \(n\) sets omitting one matched pair and selecting all other vertices, contributing \(nz^{2n-2}\). Finally, \(R=C=\{i,h\}\) contributes \(\binom n2z^{2n-4}\) with no overlap with the preceding cases. This proves \(T_n(z)\).

**4. Inclusion-minimal transversals.** In the first class \(U=\varnothing\), having a doubly selected matched pair prevents minimality: delete one vertex from that pair. A transversal containing exactly one vertex per pair is inclusion-minimal precisely when at least two selected vertices lie in each shore. Indeed, if one shore has at most one selected vertex, deleting a suitable selected vertex leaves all but one vertex of the other shore, still a transversal by Step 2. Conversely, when each shore contains at least two selected vertices, deleting any selected vertex creates a missing pair \(i\); both \(R\setminus\{i\}\) and \(C\setminus\{i\}\) are nonempty and disjoint, so Step 2 gives a disjoint maximal geodesic. There are \(2^n-2n-2\) such selections, all of size \(n\).

For the second class, minimality forces the opposite shore's optional vertices to be absent, leaving precisely \(\{a_j:j\ne i\}\) or \(\{b_j:j\ne i\}\), giving \(2n\) sets of size \(n-1\). They are minimal since deleting another selected vertex leaves two missing indices in that shore, and the entirely omitted opposite shore permits a disjoint maximal geodesic (there is a third distinct index because \(n\ge4\)). For the final class, \(S=\{a_j,b_j:j\notin\{i,h\}\}\). Removing any \(a_k\) produces a disjoint maximal geodesic with endpoint index \(i\), intermediate indices \(h\) and \(k\); removing \(b_k\) is symmetric. Thus all \(\binom n2\) such sets are minimal and have size \(2n-4\). The three descriptions are disjoint and exhaustive, proving \(M_n(z)\) and its spectrum.

**5. Geodesic packing.** Every maximal geodesic has four vertices, so vertex-disjoint maximal geodesics number at most \(\lfloor 2n/4\rfloor=\lfloor n/2\rfloor\). Set \(p=\lfloor n/2\rfloor\ge2\). Choose \(p\) endpoint indices \(I\) and \(p\) disjoint intermediate indices \(J\), possible because \(2p\le n\). Index these two sets as \(I=\{i_1,\ldots,i_p\}\), \(J=\{j_1,\ldots,j_p\}\). The paths \(a_{i_t}-b_{j_t}-a_{j_{t+1}}-b_{i_t}\), with the second subscript cyclic modulo \(p\), are maximal geodesics and are pairwise vertex-disjoint. This attains the upper bound.

## Verification

Run `python3 verify_crown_gt.py` using Python 3 without external dependencies. The script independently builds the crown graph, computes all-pairs distances by breadth-first search, enumerates short simple paths, checks geodesic maximality by both endpoint extensions, and directly tests every vertex subset for transversal and inclusion-minimal status. For every integer \(4\le n\le8\), it compares the exact coefficient histograms with the two formulas and checks an explicit optimal packing.

The executed program reported:

```
VERIFY_OK orders=4..8 maximal_geodesics=750 all_subsets=87296 transversals=13403 inclusion_minimal=566 independent_BFS=PASS all_polynomials=PASS minimal_families=PASS packing_construction=PASS
```

Examples: \(M_4(z)=8z^3+12z^4\), \(M_6(z)=12z^5+50z^6+15z^8\), and \(M_8(z)=16z^7+238z^8+28z^{12}\). The finite checks corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work

Manuel, Brešar, and Klavžar introduced the geodesic-transversal problem and established general complexity bounds and algorithms for trees and spread cactus graphs [1]. Peterin and Semanišin independently studied the equivalent *maximal shortest paths cover* invariant [2]. Manuel, Brešar, and Klavžar later developed the dual geodesic-packing problem and computed the transversal number in rook graphs [3]. Their related network study treats meshes, tree structures and particular chemical networks [4]. Those published results provide the definitions and context but, in the inspected material, do not furnish the crown-graph transversal characterization, both exact polynomials, or its inclusion-minimal spectrum. A published geodesic-*subpath counting* result for matching-deleted bicliques addresses counting paths rather than minimal vertex hitting sets; this invariant cannot directly yield the formulas above. Similar optimization parameters such as edge-metric dimension and strong geodetic number are not equivalent to covering every maximal geodesic.

## Limitations

No claim is made that a negative literature/database search proves absolute novelty. A previously unindexed result or an inaccessible exhaustive treatment could cover the theorem. The computational check is limited to \(n\le8\); the unrestricted conclusions rely on the explicit argument. Only ordinary unweighted graph geodesics, inclusion-minimal hitting sets, and vertex-disjoint geodesic packing are covered. Independent mathematical verification has not been performed.

## References

[1] P. Manuel, B. Brešar, and S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1 (20 January 2021), later Applied Mathematics and Computation 413 (2022), 126621. https://arxiv.org/abs/2101.08042

[2] I. Peterin and G. Semanišin, *On the Maximal Shortest Paths Cover Number*, Mathematics 9 (2021), 1592. https://doi.org/10.3390/math9141592

[3] P. Manuel, B. Brešar, and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325v1 (27 October 2022), later Applied Mathematics and Computation 459 (2023), 128277. https://arxiv.org/abs/2210.15325

[4] P. Manuel, B. Brešar, and S. Klavžar, *The geodesic transversal problem on some networks*, Computational and Applied Mathematics 42 (2023), article 59. https://doi.org/10.1007/s40314-023-02199-9
