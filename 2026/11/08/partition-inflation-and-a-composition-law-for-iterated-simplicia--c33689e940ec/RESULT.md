# Partition inflation and a composition law for iterated simplicial doubles

## Finding
For every finite abstract simplicial complex \(X\) and integers \(r,s\ge 2\), define \(D_t(X)\) to have a vertex for every \(t\)-element face of \(X\), and a face for each family of pairwise disjoint \(t\)-element faces whose union is a face of \(X\). The **composition law** is a natural simplicial isomorphism
\[
D_r(D_s(X))\ \cong\ (D_{rs}(X))^{[c]},\qquad c=\frac{(rs)!}{r!(s!)^r},
\]
where \(K^{[c]}\) denotes the uniform vertex inflation of \(K\): every vertex is replaced by \(c\) mutually incompatible labels, and a selection of labels is a simplex precisely when its distinct underlying vertices form a simplex. Each label here is an unordered partition of its underlying \(rs\)-element face into \(r\) blocks of size \(s\).

When \(K=D_{rs}(X)\) is nonempty and connected, the classical vertex-inflation splitting gives the explicit integral homotopy formula
\[
D_r(D_s(X))\simeq K\ \vee\ \bigvee_{\substack{F\in K\\F\ne\varnothing}}\ \bigvee^{(c-1)^{|F|}}\Sigma^{|F|}D_{rs}(\operatorname{lk}_X(U_F)),\qquad U_F=\bigcup_{\sigma\in F}\sigma.
\]
In this formula \(F\) ranges over nonempty faces of \(K\), and \(|F|\) counts their constituent \(rs\)-faces. For a maximal face, the suspended complex containing only the empty simplex is interpreted as \(S^{|F|-1}\). For disconnected \(K\), apply the formula independently on connected components; if \(K\) has no vertices both complexes have empty geometric realization.

This construction is generally **not commutative in its two subdivision parameters**. On the full simplex with six vertices, \(D_2(D_3(X))\) is ten isolated points and \(D_3(D_2(X))\) is fifteen isolated points, so even their reduced integral zeroth homology groups differ.

## Assumptions and scope
A finite simplicial complex includes the empty face; every face mentioned in \(D_t\) has exactly \(t\) vertices. Vertex inflation prohibits selecting two distinct labels over the same original vertex. All geometric realizations and suspensions use standard unbased simplicial conventions; the wedge formula is understood up to homotopy and is not claimed to be a canonical equivariant splitting. In the connected case a base point may be selected without changing the displayed homotopy type. The natural simplicial isomorphism itself does not require connectedness, shellability, purity or torsion-free homology.

## Proof
**1. Vertex identification.** A vertex of \(D_r(D_s(X))\) is a family of \(r\) different vertices of \(D_s(X)\) forming a simplex in \(D_s(X)\). Its members are therefore \(r\) pairwise disjoint \(s\)-element faces of \(X\) whose union \(U\) is a face of \(X\), with \(|U|=rs\). Such data are exactly a vertex \(U\) of \(D_{rs}(X)\), together with an unordered partition of \(U\) into \(r\) size-\(s\) blocks. The number of these partitions is the constant \(c=(rs)!/(r!(s!)^r)\), independent of \(U\).

**2. Face criterion.** Consider any finite selection of these partition-labelled vertices. It is a face in \(D_r(D_s(X))\) if and only if all its constituent \(s\)-blocks are pairwise disjoint and their joint union is a face of \(X\). Equivalently, its underlying \(rs\)-sets are pairwise disjoint and jointly a face of \(X\); in particular no two selected labels lie over the same \(rs\)-set. This is exactly the definition of the corresponding simplex in the uniform inflation of \(D_{rs}(X)\). The correspondence and its inverse preserve all faces and commute with injections of simplicial complexes. This proves the composition law.

**3. Links.** If \(F\) is a face of \(K=D_{rs}(X)\), its vertices are disjoint \(rs\)-element subsets and their union \(U_F\) is a face in \(X\). A vertex \(W\) lies in \(\operatorname{lk}_K(F)\) exactly when \(W\) is an \(rs\)-element face disjoint from \(U_F\) with \(W\cup U_F\) a face of \(X\). The same condition for every family of such vertices proves an isomorphism \(\operatorname{lk}_K(F)\cong D_{rs}(\operatorname{lk}_X(U_F))\).

**4. Homotopy formula.** The vertex-inflation splitting theorem of Björner, Wachs and Welker (their poset-fiber theorem and simplicial-inflation corollary) states, for a connected base complex \(K\) and a positive number of copies \(m_v\) at each vertex, that its inflation is homotopy equivalent to the wedge of \(K\) and, over every nonempty face \(F\), \(\prod_{v\in F}(m_v-1)\) copies of \(\Sigma^{|F|}\operatorname{lk}_K(F)\). Apply this established theorem with all \(m_v=c\), and replace the links by the isomorphisms in Step 3. The conclusion is integral, not a rational or finite-range calculation. Connected components of an inflation do not mix when base components are disjoint, giving the stated disconnected-case reduction.

**5. Noncommutativity and natural scale.** For \(X\) the full simplex on six vertices and \(rs=6\), the base \(D_6(X)\) has one vertex. The partition counts are \(6!/(2!(3!)^2)=10\) for \((r,s)=(2,3)\) and \(6!/(3!(2!)^3)=15\) for \((r,s)=(3,2)\). Their inflated complexes therefore consist respectively of ten and fifteen isolated points. This verifies the asserted distinct integral reduced zeroth-homology ranks \(9\) and \(14\), not merely a numerical difference in vertex counts.

## Verification
The accompanying standalone `verify_iterated.py` constructs \(D_r(D_s(X))\) from its two defining applications, separately constructs \(D_{rs}(X)\), and enumerates unordered equipartitions for its predicted inflation. All tested complexes have dimension at most one in these parameter ranges, so checking all vertices and edges compares their entire face sets for full simplices of sizes four through nine with \((r,s)=(2,2)\), sizes six through nine with both \((2,3)\) and \((3,2)\), and a two-facet complex; it checks the connected nine-vertex example independently by graph cycle rank. All tests passed; see `verification_output.txt`. These finite checks corroborate but do not establish the unrestricted composition law, which follows from Steps 1–2, nor the homotopy splitting, which follows from the cited published theorem.

For the full simplex on nine vertices and \(r=s=2\), the base \(D_4(X)\) is the connected Kneser graph \(KG(9,4)\) with \(126\) vertices and \(315\) edges. Its inflation has \(378\) vertices and \(2835\) edges, so
\[D_2(D_2(X))\simeq\bigvee^{2835-378+1}S^1=\bigvee^{2458}S^1.\]
The splitting independently accounts for these \(2458\) circles as \(190\) from the original Kneser graph, \(1008\) from inflated vertices, and \(1260\) from inflated edges.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced and investigated the simplicial \(r\)-tupling construction in *The double of a simplicial complex* (arXiv:2506.10436v1, first public June 12, 2025). Their article focuses on connectivity, weak Cohen–Macaulay properties, destabilization and related complexes. The two-stage composition, its exact partition-inflation identification and the asymmetric order-of-operations consequence are not stated in the inspected primary text.

Björner, Wachs and Welker's *Poset fiber theorems* (Trans. Amer. Math. Soc., 2005, Section 6) already contains the general vertex-inflation homotopy splitting; that general theorem is used and expressly **not claimed as new**. The additional contribution here is the natural identification of two applications of the 2025 construction with that classical operation and its explicit \(rs\)-link formula. The literature may contain unindexed equivalent descriptions of compositions of matching or disjoint-face constructions.

## Limitations
The homotopy wedge formula is inherited from an established inflation theorem, not an independently novel general splitting. It requires the specified connectedness treatment, though the underlying simplicial composition law has none. It does not give canonical equivariant or multiplicative cohomology decompositions, and some applications may reduce to previously known examples. It does not assert all new summands are spheres for general \(X\). Independent mathematical audit has not been performed.

## References
1. K. Lesh, B. Schreiner, N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1 (2025-06-12), Definition 2.1 and Sections 2–4; later v2 2026-10-27.
2. A. Björner, M. Wachs, V. Welker, *Poset fiber theorems*, Transactions of the American Mathematical Society 357 (2005), 1877–1899, Section 6 (vertex inflation splitting, Theorem 6.2 and corollaries).
