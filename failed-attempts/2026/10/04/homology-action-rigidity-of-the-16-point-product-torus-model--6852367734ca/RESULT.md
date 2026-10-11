# Homology-action rigidity of the 16-point product torus model
## Finding
Let \(C\) be the four-point finite \(T_0\)-space with two minimal points and two maximal points, each minimal point below each maximal point. Let \(T^2_{0,0}=C\times C\). This is the standard 16-point product finite model of the torus.

There are exactly 8,042,896 continuous self-maps \(f:T^2_{0,0}\to T^2_{0,0}\). Relative to the two factor generators of \(H_1(T^2_{0,0};\mathbb Z)\cong\mathbb Z^2\), their induced homology maps comprise exactly 25 integer matrices. Exactly 32 self-maps have rank-two action. Those 32 maps are precisely the homeomorphisms, and the eight distinct rank-two matrices are exactly the signed permutation matrices.

Consequently the elementary shear
\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]
is not induced by any self-map of \(T^2_{0,0}\). Thus this cardinality-minimal finite torus model does not directly realize a Dehn-twist mapping class; realizing that mapping class requires changing the finite model, for example by refinement or enlargement.

## Assumptions and scope
The topology on a finite \(T_0\)-space is represented by its specialization poset, so continuous maps are exactly order-preserving maps. The claim concerns the specific product model \(T^2_{0,0}=C\times C\), not the other 16-point minimal torus model and not arbitrary refinements.

The source literature identifies \(T^2_{0,0}\) with the product of two four-point circle models and proves that it is a minimal finite model of the torus. Hence its first integral homology is \(\mathbb Z^2\).

## Proof
Label the points of \(C\) by \(0,1,2,3\), with \(0,1\) minimal, \(2,3\) maximal, and all four relations \(0<2\), \(0<3\), \(1<2\), \(1<3\). In \(C\times C\), use the two factor cycles
\[
z_1=[(0,0),(2,0)]-[(1,0),(2,0)]+[(1,0),(3,0)]-[(0,0),(3,0)]
\]
and
\[
z_2=[(0,0),(0,2)]-[(0,1),(0,2)]+[(0,1),(0,3)]-[(0,0),(0,3)].
\]
Let \(u\) be the integral 1-cocycle on \(C\) taking value \(1\) on the edge \(0<2\) and \(0\) on the other three edges. Pulling \(u\) back along the two coordinate projections gives cocycles \(\alpha,\beta\) on \(C\times C\). Direct evaluation gives
\[
\langle\alpha,z_1\rangle=1,\quad
\langle\alpha,z_2\rangle=0,\quad
\langle\beta,z_1\rangle=0,\quad
\langle\beta,z_2\rangle=1.
\]
Since the source model has torus homology, these cycles and cocycles are dual integral bases.

For each order-preserving self-map \(f\), the matrix of \(f_*\) is therefore obtained exactly by evaluating \(\alpha\) and \(\beta\) on \(f_\#z_1\) and \(f_\#z_2\). The attached verifier performs a complete backtracking enumeration. At every partially assigned map it intersects the codomain upper and lower sets forced by all already assigned comparable domain points; every surviving codomain image is then branched over. This partitions all order-preserving maps without omission or duplication.

The exhaustive output is \(8{,}042{,}896\) continuous self-maps and exactly \(25\) distinct induced matrices. Of the self-maps, \(32\) induce matrices of nonzero determinant, and these same \(32\) maps are exactly the bijective ones. Every bijective order-preserving self-map of a finite poset is an automorphism, because a positive power is the identity and hence its inverse is also order-preserving. The eight distinct invertible matrices are
\[
\left\{
\begin{pmatrix}\varepsilon&0\\0&\delta\end{pmatrix},
\begin{pmatrix}0&\varepsilon\\\delta&0\end{pmatrix}
:\ \varepsilon,\delta\in\{-1,1\}
\right\}.
\]
These are precisely the signed permutation matrices. The shear matrix above is absent from the complete list.

## Verification
Run `python3 verify.py`. It reconstructs the poset, checks that the displayed cycles are cycles, checks that the two displayed cochains are cocycles and pair dually with the cycles, exhaustively enumerates all order-preserving self-maps, recomputes every induced matrix, checks the complete 25-matrix multiplicity table, verifies that exactly 32 maps are bijective and exactly 32 have rank-two homology action, and confirms that the rank-two matrices are precisely the signed permutation matrices.

Expected terminal lines include `VERIFY_OK`, `continuous_self_maps=8042896`, `induced_H1_matrices=25`, `rank2_maps=32`, and `dehn_twist_matrix_present=false`.

## Relationship to prior work
Barmak's 2011 monograph develops finite-space products and minimal finite models and is the earlier public source associated with the product torus model. Cianci and Ottina's 2015 preprint identifies \(T^2_{0,0}\) as \(C\times C\), proves the 16-point lower bound for finite torus models, and proves that there are exactly two 16-point minimal torus models. Their result supplies the minimal-model context; the exact endomorphism census and the image of the self-map monoid on integral first homology are not stated there.

Targeted searches for the model name, self-map monoid, exact count, homology action, signed permutation matrices, and Dehn-twist realization did not locate a prior statement of this classification. Database noncoverage is not a proof of novelty, so an obscure equivalent computation remains a residual risk.

## Limitations
The result is specific to \(T^2_{0,0}\); it does not classify self-maps of the second 16-point minimal torus model. It does not say that a Dehn twist cannot be represented after subdividing, refining, or enlarging the finite model. The exact census is computer-assisted, although the search is finite, deterministic, exhaustive, and replayable from the included verifier.

## References
Jonathan A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011. DOI: `10.1007/978-3-642-22003-6`.

Nicolás Cianci and Miguel Ottina, *Poset splitting and minimality of finite models*, arXiv:`1512.06088v1`, submitted 18 December 2015.
