# Annihilator layers control symmetry and metric dimension in every finite chain-ring zero-divisor graph

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), nilpotency length \(\ell\ge2\), and residue field of order \(q\). For the standard zero-divisor graph \(\Gamma(R)\), the annihilator-equivalence classes are exactly the valuation layers \(V_i=\mathfrak m^i\setminus\mathfrak m^{i+1}\) for \(1\le i\le\ell-1\), with \(|V_i|=(q-1)q^{\ell-i-1}\), and vertices in \(V_i,V_j\) are adjacent exactly when \(i+j\ge\ell\). Consequently \(\operatorname{Aut}\Gamma(R)\cong\prod_{i=1}^{\ell-1}S_{(q-1)q^{\ell-i-1}}\), and both the determining number and metric dimension equal \(q^{\ell-1}-\ell\). In particular, the zero-divisor graph is determined up to isomorphism by \((q,\ell)\), although the ring need not be.

This gives a uniform graph-theoretic description of all finite commutative chain rings, rather than only the classical families \(\mathbb Z_{p^\ell}\) or truncated polynomial rings.

## Assumptions and scope

Let \(R\) be a finite commutative chain ring. Thus its ideals are linearly ordered, its unique maximal ideal is principal,
\[
\mathfrak m=(\pi),
\]
and for some \(\ell\ge2\),
\[
\mathfrak m^\ell=0,\qquad \mathfrak m^{\ell-1}\ne0.
\]
Write
\[
q=|R/\mathfrak m|.
\]
The nonzero zero-divisors are exactly \(\mathfrak m\setminus\{0\}\).

For \(1\le i\le\ell-1\), define the valuation layer
\[
V_i=\mathfrak m^i\setminus\mathfrak m^{i+1}.
\]
The graph \(\Gamma(R)\) is the Anderson--Livingston zero-divisor graph: its vertices are the nonzero zero-divisors and two distinct vertices are adjacent exactly when their product is zero.

The determining number is the minimum size of a vertex set whose pointwise stabilizer in the graph automorphism group is trivial. The metric dimension is the minimum size of a resolving set.

## Proof

Every nonzero element \(x\in R\) has a unique presentation
\[
x=u\pi^i
\]
with \(u\) a unit and \(0\le i\le\ell-1\). Therefore the nonzero zero-divisors are partitioned by the \(V_i\).

Because every quotient
\[
\mathfrak m^i/\mathfrak m^{i+1}
\]
is one-dimensional over \(R/\mathfrak m\), one has
\[
|\mathfrak m^i|=q^{\ell-i}.
\]
Hence
\[
|V_i|
=|\mathfrak m^i|-|\mathfrak m^{i+1}|
=(q-1)q^{\ell-i-1}.
\]

If \(x=u\pi^i\in V_i\) and \(y=v\pi^j\in V_j\), then \(uv\) is a unit, so
\[
xy=0
\quad\Longleftrightarrow\quad
\pi^{i+j}=0
\quad\Longleftrightarrow\quad
i+j\ge\ell.
\]
Thus adjacency depends only on the two valuation indices.

Moreover
\[
\operatorname{ann}(u\pi^i)=\mathfrak m^{\ell-i}.
\]
Hence two nonzero zero-divisors have the same annihilator exactly when they lie in the same \(V_i\). The annihilator-equivalence classes used in compressed zero-divisor graphs are therefore precisely the valuation layers.

For \(x\in V_i\), the neighbors are all elements in
\[
V_{\ell-i}\cup V_{\ell-i+1}\cup\cdots\cup V_{\ell-1},
\]
except that \(x\) itself must be removed when \(2i\ge\ell\). Since
\[
\left|\mathfrak m^{\ell-i}\right|=q^i,
\]
the degree is
\[
\deg(x)=
\begin{cases}
q^i-1,&2i<\ell,\\
q^i-2,&2i\ge\ell.
\end{cases}
\]
These values are strictly increasing with \(i\). Thus every automorphism preserves each \(V_i\) setwise.

Within one layer, all vertices have identical adjacency to vertices outside the layer; the induced graph on the layer is either empty or complete according as \(2i<\ell\) or \(2i\ge\ell\). Therefore every permutation of \(V_i\) is a graph automorphism, independently for each \(i\). Since the degree sequence forbids any mixing of distinct layers,
\[
\operatorname{Aut}\Gamma(R)
\cong
\prod_{i=1}^{\ell-1}\operatorname{Sym}(V_i)
\cong
\prod_{i=1}^{\ell-1}S_{(q-1)q^{\ell-i-1}}.
\]

A determining set must contain all but at most one vertex of every \(V_i\), because any two omitted vertices from the same layer can be transposed while fixing every other vertex. Conversely, retaining all but one vertex from each layer kills every factor of the displayed direct product. Therefore
\[
\operatorname{Det}\Gamma(R)
=
\sum_{i=1}^{\ell-1}(|V_i|-1)
=
(q^{\ell-1}-1)-(\ell-1)
=
q^{\ell-1}-\ell.
\]

The same twin-class argument gives the metric lower bound
\[
\dim_M\Gamma(R)\ge q^{\ell-1}-\ell.
\]
Let \(W\) contain all but one vertex from every \(V_i\). Vertices in \(W\) are distinguished from every other vertex by their own zero coordinate in their distance vectors. It remains only to distinguish the omitted representatives \(u_i\in V_i\).

If \(i<j\), choose a selected vertex
\[
w\in V_{\ell-j}.
\]
Such a selected vertex exists because
\[
|V_{\ell-j}|=(q-1)q^{j-1}\ge2
\]
for \(j\ge2\). Then
\[
(\ell-j)+j=\ell
\]
so \(w\) is adjacent to \(u_j\), whereas
\[
(\ell-j)+i<\ell
\]
so \(w\) is not adjacent to \(u_i\). The graph has diameter at most two, so the corresponding distances are \(1\) and \(2\). Hence \(W\) resolves every pair of omitted representatives.

For \(\ell=2\), \(\Gamma(R)\) is the complete graph on \(q-1\) vertices and the same formula gives metric dimension \(q-2\), with the standard value \(0\) for the one-vertex case. Thus in all cases
\[
\dim_M\Gamma(R)=q^{\ell-1}-\ell.
\]

All adjacency, layer sizes, and therefore the entire graph are determined by \((q,\ell)\). Hence any two finite commutative chain rings with the same residue-field size and length have isomorphic zero-divisor graphs. For example, \(\mathbb Z/8\mathbb Z\) and \(\mathbb F_2[x]/(x^3)\) are nonisomorphic rings of different characteristics, but their zero-divisor graphs are isomorphic.

## Verification

The accompanying `verify.py` constructs the abstract valuation-layer graph from \((q,\ell)\), checks the exact layer sizes and degree formulas, verifies the twin structure and strict degree separation, and tests the proposed resolving set.

For all tested instances with at most \(15\) graph vertices it exhaustively searches smaller resolving sets and confirms the exact metric dimension. Independently, it constructs zero-divisor graphs from multiplication in \(\mathbb Z/8\mathbb Z\), \(\mathbb Z/16\mathbb Z\), \(\mathbb F_2[x]/(x^3)\), and \(\mathbb F_2[x]/(x^4)\), and confirms that rings with the same \((q,\ell)\) have identical layer-degree-edge profiles.

Exact output:

```text
VERIFY_OK
abstract_cases=6
metric_dimension_exhaustive_for_all_cases_with_at_most_15_vertices
same_graph_profile=Z8_vs_F2[x]/(x^3)
same_graph_profile=Z16_vs_F2[x]/(x^4)
```

The computations are corroborative; the equalities for arbitrary finite chain rings follow from the symbolic valuation and twin-class arguments above.

## Relationship to prior work

Spiroff and Wickham introduced the annihilator-equivalence compression of zero-divisor graphs. In a chain ring their equivalence relation becomes exactly the valuation-layer partition proved above.

Later work on principal ideal rings studied spectra of zero-divisor graphs over finite chain rings, while work on determining number and metric dimension obtained formulas for \(\Gamma(\mathbb Z_n)\). Those results cover the special family \(\mathbb Z_{p^\ell}\), not arbitrary finite chain rings.

Recent papers make two further special cases explicit. One gives the valuation-layer structure for \(\mathbb F_p[x]/(x^c)\) in a spectral study; another computes an automorphism-group product for the nilradical graph of \(\mathbb Z_{p^k}\). These are consistent with the theorem here. The new statement is the uniform chain-ring synthesis: the annihilator compression, full automorphism group, determining number, metric dimension, and graph-isomorphism classification all follow solely from \((q,\ell)\), including equal-characteristic, mixed-characteristic, and nonisomorphic chain rings with the same parameters.

Targeted mathematical-record and literature searches for finite chain rings together with determining number, metric dimension, automorphism group, annihilator classes, and valuation layers found no source stating this combined general theorem.

## Limitations

The theorem assumes the ring is commutative and a chain ring. For a general finite local principal ideal ring that is not commutative, or for finite local rings whose ideal lattice is not a chain, annihilator classes can refine or interact with several incomparable directions and the proof does not apply.

The \(\mathbb Z_{p^\ell}\) special case of the determining/metric formulas is already covered by broader results for \(\mathbb Z_n\), and the automorphism product for that special family has also appeared separately. The originality claim is therefore specifically the extension and unification for arbitrary finite commutative chain rings.

A 2021 paper on spectra over finite chain rings was available during this run only through its abstract after open-access and institutional full-text attempts failed. Its stated scope is spectral, so it is not a decisive unresolved comparison, but the access limitation remains a literature risk.

## References

1. S. Spiroff and C. Wickham, “A Zero Divisor Graph Determined by Equivalence Classes of Zero Divisors,” *Communications in Algebra* 39 (2011), 2338–2348. DOI: 10.1080/00927872.2010.488675. arXiv:0801.0086; first public preprint 2007-12-29.
2. S. Rattanakangwanwong and Y. Meemark, “Eigenvalues of zero divisor graphs of principal ideal rings,” *Linear and Multilinear Algebra* 70 (2022), 6890–6905. DOI: 10.1080/03081087.2021.1917501. Published online 2021-04-26.
3. M. Sabeel K and K. Paramasivam, “On determining number and metric dimension of zero-divisor graphs,” arXiv:2308.00796, 2023.
4. B. A. Rather, “Spectral Properties of Zero-Divisor Graphs of Truncated Polynomial Rings,” arXiv:2604.03101, 2026.
5. K. Kiplagat, M. Mude, and G. Kayiita, “Automorphism of Zero Divisor Graphs of Nilradicals of Commutative Finite Local Rings,” *Journal of Advances in Mathematics and Computer Science* 41(2) (2026), 44–58. DOI: 10.9734/jamcs/2026/v41i22097.
