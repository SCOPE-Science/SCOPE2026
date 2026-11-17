# Maximum weighted-star degree controls sharp Euclidean distortion of poset transfer maps

## Finding
Let \(P\) be any nonempty finite poset of height at most two, \(A\) its minimal elements and \(B=P\setminus A\). For each \(b\in B\) fix \(t_b\in[0,1]\). Define
\[
W(P,\mathbf t)=\max_{a\in A}\sum_{b\in B:\,a<_P b}t_b^2,
\qquad
\Lambda(W)=\sqrt{\frac{2+W+\sqrt{W^2+4W}}2}.
\]
On the ordinary order polytope \(\mathcal O(P)\subseteq\mathbb R^P\), let the parametrized transfer map be
\[
(\Phi_{\mathbf t}(x))_a=x_a\ (a\in A),\qquad
(\Phi_{\mathbf t}(x))_b=x_b-t_b\max_{a<_P b}x_a\ (b\in B).
\]
Its image \(\mathcal C_{\mathbf t}(P)=\Phi_{\mathbf t}(\mathcal O(P))\) is a convex polytope. In the ordinary coordinatewise Euclidean metric, the exact optimal global Lipschitz constants of **both** this bijection and its inverse are
\[
\boxed{\operatorname{Lip}_2(\Phi_{\mathbf t})=\operatorname{Lip}_2(\Phi_{\mathbf t}^{-1})=\Lambda(W(P,\mathbf t)).}
\]
Thus the sharp two-sided Euclidean distortion of the entire continuous marked-poset interpolation depends on its comparability graph and all individual parameters only through one maximum weighted star sum. When \(t_b=1\) for all \(b\), the target is Stanley's chain polytope, \(W=\Delta\) is the maximum number of upper neighbours of a minimal element, and the sharp Lipschitz constant is \(\sqrt{(2+\Delta+\sqrt{\Delta^2+4\Delta})/2}\). Both constants are attained by sufficiently close distinct interior points, whenever \(W>0\); the zero-weight case is the identity map. The product of the sharp forward and inverse Lipschitz constants equals \((2+W+\sqrt{W^2+4W})/2\).

## Assumptions and scope
A height-at-most-two poset is a finite poset with no strict chain of length three. All comparabilities join \(A\) to \(B\); every element in \(B\) has at least one lower neighbour. Isolated elements lie in \(A\). The order polytope is \(\mathcal O(P)=\{x\in[0,1]^P:x_a\le x_b\text{ whenever }a<_P b\}\). Euclidean distances use the given coordinate realization, not a freely chosen affine normalization. A map's Lipschitz constant is the supremum over distinct points of its domain of the ratio of Euclidean output distance to Euclidean input distance. A maximum over \(a\in A\) is defined because \(P\) is nonempty. The theorem includes all zero weights and disconnected comparability graphs.

The image can equivalently be described without using the transfer map: its minimal coordinates satisfy \(0\le y_a\le1\); for each \(b\in B\) and \(a<_P b\), impose \((1-t_b)y_a\le y_b\) and \(y_b+t_by_a\le1\). These are all defining inequalities, with the implied bounds \(0\le y_b\le1\). The inverse is \(x_a=y_a\) and \(x_b=y_b+t_b\max_{a<_P b}y_a\).

## Proof
**1. Explicit bijective polytope model.** For \(x\in\mathcal O(P)\), put \(M_b=\max_{a<_P b}x_a\). The bounds \(M_b\le x_b\le1\) are equivalent to \((1-t_b)M_b\le y_b\le1-t_bM_b\), where \(y_b=x_b-t_bM_b\) and \(y_a=x_a\). Since \(t_b\in[0,1]\), the first inequality is equivalent to the family \((1-t_b)y_a\le y_b\); the second is equivalent to the family \(y_b+t_by_a\le1\). These linear inequalities show that the image is convex and yield the stated inverse for every point of the image.

**2. All local Jacobians.** On a full-dimensional chamber where every \(b\in B\) has a unique maximizing lower neighbour \(a(b)\), the Jacobian \(J\) has identity diagonal and one additional nonzero coefficient \(-t_b\) in row \(b\), column \(a(b)\). After grouping each minimal element with the upper elements choosing it, \(J\) is an orthogonal direct sum of weighted star matrices
\[
S(w)=\begin{pmatrix}1&0\\-w&I\end{pmatrix},
\qquad w=(t_b)_{a(b)=a}.
\]
For \(U=\|w\|_2^2\), \(S(w)^\top S(w)\) has eigenvalue \(1\) on the orthogonal complement of \(w\) in the leaf subspace, and two remaining eigenvalues are the roots of \(z^2-(2+U)z+1=0\). Hence \(\|S(w)\|_2=\Lambda(U)\). Its inverse \(S(w)^{-1}=S(-w)\) has the same singular values. Since \(U\le W(P,\mathbf t)\), every chamber has both Jacobian and inverse-Jacobian norm at most \(\Lambda(W)\).

**3. Sharp global constants.** The domain and target are convex polytopes, and the maps and inverse are continuous piecewise affine with finitely many chambers. Subdivide any chord at its finitely many chamber boundaries (or take a generic limiting chord). Integrating the local norm bound proves both global upper bounds. Choose \(a_*\in A\) realizing \(W\), give it a strictly larger coordinate than every other minimal element, and choose all upper coordinates strictly above all minimal ones but below one. This is an interior point of \(\mathcal O(P)\) lying in a chamber where every upper neighbour of \(a_*\) chooses \(a_*\). The corresponding star has \(U=W\). Its principal singular vectors give arbitrarily small interior chords attaining exactly \(\Lambda(W)\) for \(\Phi_{\mathbf t}\) and, by applying the inverse to small chords in its image chamber, for \(\Phi_{\mathbf t}^{-1}\). If \(W=0\), all the maps are identity. This proves sharpness, including the boundary parameter cases.

## Verification
The accompanying independent numerical checker (`checker.py`) enumerates all bipartite relation graphs in six size regimes (including all \(2^{12}\) graphs on three lower and four upper elements), assigns rational interpolation weights, reconstructs every possible parent-selection Jacobian, and independently evaluates its singular values and inverse singular values. It also tests randomly selected strictly feasible point pairs, both transfer identities, exact upper bounds, and local singular-vector witnesses. A separate 116-case star calculation checks the closed radical formula. The observed output was:

`TRANSFER_STABILITY_PASS graphs=4754 Jacobians=31079 interior_pairs=9508 sharp_witnesses=4732 weighted_stars=116`

Finite numerical tests support the proof but do not establish the general theorem. The analytic argument above covers arbitrary finite height-at-most-two posets and real parameters in the full closed unit interval.

## Relationship to prior work
Fang, Fourier, Litza and Pegel introduced the continuous family of marked poset polytopes and the parametrized transfer maps, including their inverse and piecewise-linear structure (arXiv:1712.01037, Section 2). Pegel and Sanyal studied broader piecewise-linear transfer homeomorphisms and anti-blocking images (arXiv:1911.12090). The present theorem does not claim a new transfer map, a new convex image, or a new Ehrhart equivalence. It identifies the optimal ordinary Euclidean **two-sided stability constants** for the arbitrary-weight height-two restriction, reducing their evaluation to one maximum weighted degree. These constants do not follow as stated from the cited map-construction and image-classification results. The related geometric study of minimum enclosing spheres for a complete two-level marked-poset family concerns a different metric invariant and does not supply the transfer-map operator norm.

## Limitations
The formula is proved only for posets of height at most two, for the displayed interpolation between ordinary order and marked-poset polytopes, for real parameters \(0\le t_b\le1\), and for standard coordinate Euclidean distance. For greater height, Jacobian blocks need not be disjoint weighted stars, and this formula is not asserted. The full historical novelty of the optimal constants remains subject to independent bibliographic examination. No independent mathematical audit has been performed.

## References
- X. Fang, G. Fourier, J.-P. Litza, C. Pegel, *A continuous family of marked poset polytopes*, arXiv:1712.01037, first publicly posted 2017-12-04, https://arxiv.org/abs/1712.01037 ; full-text Section 2: https://ar5iv.labs.arxiv.org/html/1712.01037 .
- C. Pegel, R. Sanyal, *On piecewise-linear homeomorphisms between distributive and anti-blocking polyhedra*, arXiv:1911.12090, first publicly posted 2019-11-27, https://arxiv.org/abs/1911.12090 .
- R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, https://doi.org/10.1007/BF02187680 .
