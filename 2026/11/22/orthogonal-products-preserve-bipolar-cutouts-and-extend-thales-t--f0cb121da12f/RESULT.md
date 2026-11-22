# Orthogonal products preserve bipolar cutouts and extend Thales tilings to arbitrary dimensions

## Finding
Let \(P_i\subset\mathbb R^{d_i}\), \(1\le i\le m\), be full-dimensional convex polytopes in mutually orthogonal Euclidean factors, and put \(P=\prod_{i=1}^mP_i\). For \(B=(B_i)\in\operatorname{int}P\), let \(x_G(B)\) be the orthogonal projection of \(B\) onto the affine hull of the nonempty face \(G\), and define the orthogonal cutout at a vertex \(v\) by
\[
C_v(P,B)=\operatorname{conv}\{x_G(B):G\text{ a nonempty face of }P,\ v\in G\}.
\]
Call a convex polytope with two specified opposite vertices *orthogonally bipolar* when it satisfies the facet, face-intersection and atomic perpendicularity conditions of Pavlík (Definition 3.1, arXiv:2611.14277). Define the orthogonal kernel
\[
\operatorname{ker}_{\perp}(P)=\{B\in\operatorname{int}P:x_G(B)\in\operatorname{relint}G\text{ for every nonempty face }G\}.
\]
Then:

1. **Product closure:** Every Euclidean orthogonal Cartesian product of orthogonally bipolar polytopes, with the tuples of their south and north poles as the two poles, is orthogonally bipolar.
2. **Exact factorization:**
\[
\operatorname{ker}_{\perp}(P)=\prod_{i=1}^m\operatorname{ker}_{\perp}(P_i),\qquad
C_{(v_1,\ldots,v_m)}(P,B)=\prod_{i=1}^m C_{v_i}(P_i,B_i).
\]
3. **Higher-dimensional Thales tilings:** If every \(d_i\le3\) and \(B_i\in\operatorname{ker}_{\perp}(P_i)\), then every cutout of \(P\) is orthogonally bipolar and
\[
C_v(P,B)=P\cap\bigl(B+N_P(v)\bigr)
\]
for every vertex \(v\), where \(N_P(v)=\{z:\langle z,v-w\rangle\ge0\text{ for all }w\in P\}\) is the outer normal cone. These cutouts form a face-to-face partition of \(P\), in arbitrarily large dimensions. In particular, the higher-dimensional implication of Pavlík's Conjecture 6.8 holds for all such orthogonal products. The family includes products of arbitrary triangles, not merely boxes or simplices.

## Assumptions and scope
All products use the product inner product, and all factors are full-dimensional, with dimensions one, two or three only in assertion 3. The closure assertion 1 holds in every finite list of positive factor dimensions. A product with a factor having empty orthogonal kernel has empty orthogonal kernel, so assertion 3 makes no claim for it. The point \(B\) is in the strict interior; every face includes the whole polytope itself. No claim is made about a general indecomposable polytope of dimension at least four.

## Proof
**Product closure.** It suffices to consider two orthogonally bipolar polytopes \(W_1,W_2\) with south poles \(\sigma_1,\sigma_2\), north poles \(\nu_1,\nu_2\), and vertex lattices \(L_1,L_2\). The facets of their Cartesian product are exactly \(F_1\times W_2\) and \(W_1\times F_2\). Each contains exactly one of \(\sigma=(\sigma_1,\sigma_2)\), \(\nu=(\nu_1,\nu_2)\), proving condition (O1).

Every south face of the product is \(S_1\times S_2\) with each \(S_i\) a south face of its factor; likewise every north face is \(T_1\times T_2\). Such a north face meets \(S_1\times S_2\) precisely when each \(T_i\cap S_i\ne\varnothing\). If two north faces meet the south face, their intersection also meets it because each factor satisfies Pavlík's (O2); the dual condition is proved identically. This proves (O2), including nonempty intersection of the relevant faces.

The vertex order defined by containment in all north faces factors coordinatewise: \((x_1,x_2)\le(y_1,y_2)\) exactly if \(x_i\le y_i\) in both \(L_i\). Its atoms are \((a_1,\sigma_2)\), for an atom \(a_1\) of \(L_1\), and \((\sigma_1,a_2)\), for an atom \(a_2\) of \(L_2\). For the first type,
\[
[\sigma,(a_1,\sigma_2)]=[\sigma_1,a_1]\times\{\sigma_2\},\quad
[(a_1,\sigma_2),\nu]=[a_1,\nu_1]\times W_2.
\]
The first face has direction space \(U_{[\sigma_1,a_1]}\times\{0\}\); the second has \(U_{[a_1,\nu_1]}\times U_{W_2}\). They are perpendicular by (O3) for \(W_1\). The other atom type is symmetric. Thus (O3) holds, proving orthogonally bipolar product closure. Induction handles \(m\) factors.

**Kernel and cutouts.** Every nonempty face of \(P\) is uniquely a product \(G=\prod_iG_i\) of nonempty faces. Orthogonal projection onto its affine hull separates:
\[
x_G(B)=\bigl(x_{G_1}(B_1),\ldots,x_{G_m}(B_m)\bigr),
\qquad \operatorname{relint}G=\prod_i\operatorname{relint}G_i.
\]
These identities imply the kernel factorization in both directions (in the converse direction select \(G_j=P_j\) for all indices except the factor being tested). The faces through \(v=(v_i)\) are precisely products of factor faces through the respective \(v_i\), so their projection set is a Cartesian product of finite sets. The identity \(\operatorname{conv}(A_1\times\cdots\times A_m)=\prod_i\operatorname{conv} A_i\) gives exact cutout factorization, with no kernel hypothesis required.

**Tilings.** For each factor dimension at most three, Pavlík's two/three-dimensional orthogonal-cutout theorem (Theorem 6.6 and Remark 6.9) says that \(B_i\) in its orthogonal kernel implies every factor cutout is orthogonally bipolar and agrees with \(P_i\cap(B_i+N_{P_i}(v_i))\) (Lemma 6.3). Product closure and cutout factorization give the first conclusion. Normal cones factor as \(N_P(v)=\prod_iN_{P_i}(v_i)\), hence
\[
\prod_i C_{v_i}(P_i,B_i)
=\prod_i\bigl[P_i\cap(B_i+N_{P_i}(v_i))\bigr]
=P\cap\bigl(B+N_P(v)\bigr).
\]
The normal cones at the vertices form a complete fan. Their translated intersections with \(P\) cover \(P\), have disjoint interiors and meet along common faces (the latter is Proposition 6.4 in the motivating work, and also follows directly from the normal-fan support inequalities). The face-to-face conclusion follows.

## Verification
A standalone rational-arithmetic checker, `check_product.py`, constructs two noncongruent triangles with vertices \((0,0),(4,0),(0,3)\) and \((0,0),(5,0),(0,4)\), taking the interior point \((1,1)\) in both. All six planar vertex cutouts have four distinct vertices, and the nine four-dimensional product cutouts have sixteen distinct vertices each. It tests their exact Thales sphere equations at all 144 product vertices and confirms that at least one such four-dimensional cell is not an orthogonal rectangular box (two edges from its south pole have nonzero inner product). Run `python check_product.py` with Python 3; no nonstandard modules are required. These computations illustrate the theorem and do not prove its universal scope, which follows from the product arguments above.

## Relationship to prior work
Jan Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1 (10 November 2026), introduces the orthogonally bipolar conditions, identifies cutouts with translated normal-fan cells when admissible, proves the dimension-three tiling theorem, and proposes Conjecture 6.8 in higher dimensions. The companion paper *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1 (10 November 2026), develops the vertex-lattice/interval description and the combinatorial cubical subdivision; it already describes cubical decompositions of simplices. The present contribution is a closure principle for the *metric orthogonality* conditions and the corresponding exact product factorization, yielding a broad family of higher-dimensional cases of the conjectured implication. It does not claim the older dimensional results, general fan tiling, or combinatorial products as new. It is distinct from the already recorded right-simplex cutout family: a product of two triangles is a four-polytope with nine vertices, not a simplex.

## Limitations
The extension uses orthogonality of the product factors; it is not invariant under general shear or arbitrary affine products. Only sufficient conditions for the conjecture on decomposable polytopes are obtained; the indecomposable dimension-four case remains unresolved. The proof is elementary in its use of product face theory and relies on the published dimension-at-most-three cutout theorem for the final application. The literature comparison covers relevant primary statements and targeted searches, not every historical use of other terminology; an unlocated earlier product-closure observation remains a priority risk. No independent audit has been performed.

## References
- J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, submitted 10 November 2026. https://arxiv.org/abs/2611.14277
- J. Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1, submitted 10 November 2026. https://arxiv.org/abs/2611.13896
- V. Buchstaber and T. Panov, *Toric Topology*, cubical subdivision construction, as cited in the companion paper.
