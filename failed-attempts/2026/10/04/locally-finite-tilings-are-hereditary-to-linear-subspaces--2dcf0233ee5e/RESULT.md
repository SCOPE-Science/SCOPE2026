# Locally finite tilings are hereditary to linear subspaces

## Finding
Let \(X\) be a real normed space admitting a locally finite tiling by bounded convex bodies. Then every linear subspace \(Y\subseteq X\), endowed with the norm inherited from \(X\), also admits a locally finite tiling by bounded convex bodies. The subspace need not be closed, complete, or separable.

## Assumptions and scope
A tiling is locally finite when every point has a neighbourhood meeting only finitely many tiles, and the tiles here are bounded convex bodies. The recent characterization of De Bernardi, del Río, Russo, and Somaglia says that a real normed space admits such a tiling if and only if it admits an equivalent norm that is \((VI)\)-polyhedral with property \((\Delta)\); equivalently, it admits an equivalent norm that is \((K)\)-polyhedral and LFC. We use the latter formulation.

For the present argument, \((K)\)-polyhedral means that the unit ball cuts every finite-dimensional subspace in a polytope. An LFC norm is locally determined by finitely many continuous linear functionals: near each unit vector there are finitely many functionals such that equality of their values forces equality of the norm.

## Proof
By the characterization above, choose on \(X\) an equivalent norm \(|||\cdot|||\) that is \((K)\)-polyhedral and LFC. Restrict it to \(Y\).

First, the restricted norm is \((K)\)-polyhedral. If \(E\subseteq Y\) is finite-dimensional, then \(E\) is also a finite-dimensional subspace of \(X\), and
\[
B_{(Y,|||\cdot|||)}\cap E=B_{(X,|||\cdot|||)}\cap E.
\]
The right-hand side is a polytope, hence so is the left-hand side.

Second, the restricted norm is LFC. Fix \(y\in Y\) with \(|||y|||=1\). Since \(|||\cdot|||\) is LFC on \(X\), there are a neighbourhood \(U\) of \(y\) in \(X\) and functionals \(f_1,\ldots,f_m\in X^*\) witnessing the local finite-coordinate condition. Then \(U\cap Y\) is a neighbourhood of \(y\) in \(Y\), and the restrictions \(f_1|_Y,\ldots,f_m|_Y\in Y^*\) have the same implication: whenever \(u,v\in U\cap Y\) satisfy \(f_j(u)=f_j(v)\) for every \(j\), one has \(|||u|||=|||v|||\). Thus the restriction is LFC.

Finally, because \(|||\cdot|||\) is equivalent to the original norm on \(X\), its restriction is equivalent to the inherited original norm on \(Y\). Applying the same tiling characterization to \(Y\) gives a locally finite tiling of \(Y\) by bounded convex bodies. The zero subspace is immediate.

## Verification
The argument uses only the cited characterization and two restriction facts. The \((K)\)-polyhedral check is exact on every finite-dimensional \(E\subseteq Y\). The LFC check is exact because continuous ambient functionals remain continuous after restriction and relative neighbourhoods have the form \(U\cap Y\). Equivalence constants for the ambient two norms restrict unchanged to \(Y\), so no completeness hypothesis is introduced.

No finite computation is being used as evidence for an infinite-dimensional assertion. The proof is uniform over all real normed spaces and all linear subspaces.

## Relationship to prior work
The 2026 paper proves the norm-theoretic characterization used above, but the inspected statement of its tiling theorem does not state this hereditary consequence. Fonf's 1990 characterization implies the separable Banach special case after restricting a polyhedral renorming. The point of the present statement is the unrestricted normed-space form: the same restriction argument works for arbitrary, possibly nonclosed and incomplete, subspaces because the recent characterization is formulated for normed spaces and uses the hereditary pair \((K)\)-polyhedral plus LFC.

Searches for the hereditary statement, its polyhedral/LFC formulation, and equivalent subspace formulations did not locate a published finding that states or implies the full arbitrary-normed-space claim. This is evidence of noncoverage, not a proof of absolute novelty.

## Limitations
The conclusion is existential. It does not assert that intersecting the original tiles of \(X\) with \(Y\) gives a tiling, nor does it preserve tile shapes, symmetry, diameters, or quantitative local-finiteness bounds. Nothing here concerns quotients or nonlinear subsets. The separable Banach special case is already implicit in Fonf's 1990 theorem; the claimed extension is the arbitrary normed-space hereditary principle enabled by the 2026 characterization.

## References
1. C. A. De Bernardi, H. del Río, T. Russo, J. Somaglia, “Polyhedral normed spaces: the structural theorem and locally finite tilings,” arXiv:2609.29279v1, first submitted 2026-09-24.
2. V. P. Fonf, “Three characterizations of polyhedral Banach spaces,” Ukrainian Mathematical Journal 42 (1990), DOI 10.1007/BF01056615.
3. C. A. De Bernardi, L. Veselý, “Tilings of Normed Spaces,” Canadian Journal of Mathematics 69 (2017), 321–337, DOI 10.4153/CJM-2015-057-3.
