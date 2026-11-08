# Sharp squared-chord boundary/interior ratio for Euclidean simplices and its dimension-four reversal

## Finding
For each integer \(d\ge2\), let \(T\subset\mathbb R^d\) be a nondegenerate Euclidean \(d\)-simplex. Let \(X,X'\) be independent volume-uniform points of \(T\), and \(Y,Y'\) independent points uniform with respect to \((d-1)\)-dimensional Hausdorff measure on \(\partial T\). Then
\[
\boxed{\frac{\mathbb E\|Y-Y'\|_2^2}{\mathbb E\|X-X'\|_2^2}>\frac{(d+1)(d+2)}{2d^2},\qquad
\inf_{T}\frac{\mathbb E\|Y-Y'\|_2^2}{\mathbb E\|X-X'\|_2^2}=\frac{(d+1)(d+2)}{2d^2}.}
\]
The infimum is over all nondegenerate Euclidean simplices in the given dimension. It is never attained. Consequently, every triangle and every tetrahedron has larger boundary than interior mean *squared* pair distance, with sharp universal factors \(3/2\) and \(10/9\), respectively. In every dimension \(d\ge4\) some nondegenerate simplices reverse the squared-distance comparison, while regular simplices still have larger boundary mean squared distance. The first reversal dimension among simplices is therefore four.

## Assumptions and scope
Use the ambient Euclidean norm and uniform volume and surface-area distributions, **not** uniform selection of a facet or a vertex. A simplex has vertices \(v_0,\ldots,v_d\), vertex centroid \(G=(d+1)^{-1}\sum_i v_i\), opposite-facet areas \(A_i>0\), facet-area weights \(w_i=A_i/\sum_j A_j\), and incenter \(I=\sum_iw_iv_i\). Define \(S=\sum_{i=0}^{d}\|v_i-G\|_2^2>0\). All expectations are over independent points sampled as just described. The result concerns the second power of distance; it does not assert the ordinary first-moment inequality in high dimension.

The exact intermediate identity, valid for every nondegenerate simplex, is
\[
\frac{\mathbb E\|Y-Y'\|_2^2}{\mathbb E\|X-X'\|_2^2}
=\frac{d+2}{d}-\frac{(d+1)(d+2)}{d^2}\frac{\|I-G\|_2^2}{S}.
\]

## Proof
**1. Uniform simplex moments.** For a point sampled uniformly inside a \(d\)-simplex, its \(d+1\) barycentric weights have the Dirichlet distribution with all parameters one. Their first moments are \(1/(d+1)\), and second products are \((1+\mathbf1_{i=j})/((d+1)(d+2))\). Centering vertices at \(G\) and summing gives
\[
\mathbb E\|X-G\|_2^2=\frac{S}{(d+1)(d+2)},\qquad
\mathbb E\|X-X'\|_2^2=\frac{2S}{(d+1)(d+2)}.
\]
On the facet opposite \(v_i\), uniform barycentric weights on the remaining \(d\) vertices are Dirichlet with \(d\) unit parameters. Because \(\sum_{j\ne i}(v_j-G)=-(v_i-G)\), the second-moment identity gives
\[
\mathbb E(\|Y-G\|_2^2\mid Y\text{ lies on facet }i)
=\frac{\sum_{j\ne i}\|v_j-G\|_2^2+\|v_i-G\|_2^2}{d(d+1)}
=\frac{S}{d(d+1)}.
\]
This value is independent of the facet. A facet's centroid is \(((d+1)G-v_i)/d\). Weighting these centroids by the *actual facet areas* yields
\[
\mathbb EY=G-\frac{I-G}{d},\qquad
\mathbb E\|Y-Y'\|_2^2=\frac{2S}{d(d+1)}-\frac{2\|I-G\|_2^2}{d^2}.
\]
Dividing by the interior expression proves the exact identity.

**2. Sharp universal inequality.** Let \(n_i\) be outward unit normals to the facets. The equilibrium identity \(\sum_i A_in_i=0\), obtained by applying the divergence theorem to constant vector fields, implies \(A_i<\sum_{j\ne i}A_j\) for every \(i\). Strictness follows because the outward normals of the remaining facets of a nondegenerate simplex cannot all coincide. Thus \(0<w_i<1/2\), \(\sum_iw_i=1\), and \(\sum_iw_i^2<1/2\). Writing \(z_i=v_i-G\) and using Cauchy–Schwarz,
\[
\frac{\|I-G\|_2^2}{S}
=\frac{\|\sum_i(w_i-1/(d+1))z_i\|_2^2}{\sum_i\|z_i\|_2^2}
\le\sum_i\left(w_i-\frac1{d+1}\right)^2
=\sum_iw_i^2-\frac1{d+1}
<\frac{d-1}{2(d+1)}.
\]
Substituting into the exact identity yields the stated strict bound.

**3. Sharpness in every dimension.** Fix \(d\ge2\) and \(t>0\), and let \(e_0,\ldots,e_{d-1}\) be the standard orthonormal basis. Define
\[
v_0=e_0,\quad v_1=e_0+t^2e_1,\quad v_2=-e_0,\quad
v_j=-e_0+t e_{j-1}\quad(3\le j\le d).
\]
These \(d+1\) points are affinely independent for every \(t>0\). Direct facet Gram determinants give, after removing the common factor \(1/(d-1)!\), the \(d+1\) facet areas
\[
\begin{aligned}
A_0&=t^{d-2}\sqrt{4+t^4},&A_1&=2t^{d-2},\\
A_2&=t^{d-1}\sqrt{t^2+4(d-2)},&A_j&=2t^{d-1}\quad(3\le j\le d).
\end{aligned}
\]
For \(d=2\), the final index range is empty and the same formulas apply. Therefore \((w_0,w_1,w_2,\ldots,w_d)\to(1/2,1/2,0,\ldots,0)\). Meanwhile \(v_0,v_1\to e_0\) and \(v_2,\ldots,v_d\to-e_0\), so
\[
G\to \frac{3-d}{d+1}e_0,\quad I\to e_0,\quad
S\to\frac{8(d-1)}{d+1},\quad
\frac{\|I-G\|_2^2}{S}\to\frac{d-1}{2(d+1)}.
\]
The ratio consequently tends to \((d+1)(d+2)/(2d^2)\), proving that no larger constant works. All finite-\(t\) examples remain full-dimensional and satisfy the bound strictly.

**4. The sharp dimensional transition.** The sharp factor is greater than one exactly for integer dimensions \(d=2,3\), while it is less than one for all integers \(d\ge4\). By the just-proved limit, for every \(d\ge4\) a sufficiently small *positive* \(t\) gives \(\mathbb E\|Y-Y'\|_2^2<\mathbb E\|X-X'\|_2^2\). For a regular simplex, \(w_i=1/(d+1)\), thus \(I=G\) and the ratio is \((d+2)/d>1\). This proves the stated reversal and shows the transition is sharp.

## Verification
Run `python3 verify.py` with Python 3 and NumPy. This separately computes facet areas by singular values, evaluates both independent-point moments from their Dirichlet pair-product sums, and compares them to the geometric formula. It samples nondegenerate simplices in dimensions \(2\) through \(8\), checks the explicit degenerating family in dimensions \(2\) through \(10\), and performs an independent finite Monte Carlo check for a four-dimensional example. The tested program prints `SIMPLEX_SURFACE_SECOND_MOMENT_OK 1204`, plus a numerical dimension-four ratio of approximately \(0.9685456401\) at \(t=0.01\), below one. Numerical checks are supplementary; the universal theorem, strictness and sharpness follow from the proof above.

## Relationship to prior work
The Zaporozhets–Tarasov program compares distance moments of independently sampled interior and boundary points. Tokmachev's 2026 paper proves convex-order domination for a mean-aligned planar class and for circumscribed polytopes whose incenter equals both interior and surface means. Shen (2026) proves the first-distance planar conjecture and gives three-dimensional nonsimplicial counterexamples. Lotnikov (2026) gives general projective-boundary moment identities and an exact second-moment formula involving the projected boundary centroid (particularly Sections 10.3–10.4 and Theorem 8). The present exact simplex identity is compatible with those general moment identities and is **not claimed independently of them**. The proposed contribution is the universal, dimension-wise **sharp ratio**, its nonattainment, explicit simultaneous extremizing degeneration, and the first counterexamples **among simplices** starting in dimension four. Lotnikov's general identity and the centered special case do not alone bound the surface mean displacement sharply by vertex variance, nor give the extremizing sequence. Earlier two-dimensional triangle second-moment comparisons are also not claimed as new. No available comparison identified the all-dimensional sharp factor or its dimension-four transition; specialist literature could still affect priority.

## Limitations
The ratio is specific to Euclidean squared distance, nondegenerate simplices, uniform volume, and genuine surface-area weighting. The bound is an infimum attained only in a degenerate limit, not by any simplex with positive volume. The limiting family does not furnish first-moment counterexamples or imply statements about all convex bodies in dimensions two or three. Historical novelty is not independently certified; unexamined literature may contain equivalent formulations. The standalone checks do not exhaust infinitely many dimensions or shapes.

## References
1. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869, first posted 2026-07-09, https://arxiv.org/abs/2607.08869.
2. E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470, first posted 2026-08-06, https://arxiv.org/abs/2608.06470.
3. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848, first posted 2026-08-14, https://arxiv.org/abs/2608.14848; particularly Sections 10.3–10.4 and Theorem 8.
