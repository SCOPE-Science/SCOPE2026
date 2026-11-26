# The square has Morse index two for random-direction width deviation of convex quadrilaterals

## Finding
For a planar convex quadrilateral \(Q\), let \(W_Q(\omega)\) be its width in a uniform random direction \(\omega\in S^1\). Define the scale-invariant squared coefficient of variation
\[\mathcal R(Q)=\frac{\mathbb E[W_Q^2]}{(\mathbb EW_Q)^2}-1.\]
The square is a **nondegenerate saddle with Morse index two** for this functional on the four-dimensional moduli of labeled strictly convex quadrilaterals modulo Euclidean similarities. In canonical coordinates described below its Hessian has exactly two negative and two positive eigenvalues, with **precisely the symmetry-breaking variations decreasing the functional to quadratic order**.

Take, in cyclic order, the vertices
\[(-1,0),\quad (x,b),\quad (1,0),\quad (y,-a),\qquad a,b>0,\]
with \((x,y,a,b)\) close to \((0,0,1,1)\), the square. With coordinate order \((x,y,a,b)\), the gradient at the square vanishes and the Hessian is
\[H=\begin{pmatrix}
0&\pi(2-\pi)/64&0&0\\
\pi(2-\pi)/64&0&0&0\\
0&0&\pi(6-\pi)/128&\pi(2+\pi)/128\\
0&0&\pi(2+\pi)/128&\pi(6-\pi)/128
\end{pmatrix}.\]
Its eigenvalues, counted with multiplicity, are
\[\frac\pi{16},\quad \frac{\pi(\pi-2)}{64},\quad-\frac{\pi(\pi-2)}{64},\quad-\frac{\pi(\pi-2)}{64}.\]
In particular \(\det H=\pi^4(\pi-2)^3/4194304>0\), although \(H\) is indefinite.

## Assumptions and scope
The quadrilaterals are Euclidean, labeled, nondegenerate and strictly convex. Similarities are quotiented out by sending one chosen diagonal's endpoints to \((-1,0)\) and \((1,0)\). The remaining four vertex coordinates are a genuine smooth local chart around the square; no angles are externally constrained. Expectation uses normalized uniform angular measure, and the full shape functional is invariant under similarity. The theorem concerns the local second variation, not the unknown global minimum for four-sided polygons.

## Proof
**(1) Exact width correlation.** Number the cyclic edge vectors \(e_1,e_2,e_3,e_4\) as
\[e_1=(1+x,b),\quad e_2=(1-x,-b),\quad e_3=(y-1,-a),\quad e_4=(-1-y,a).\]
For a direction \(\omega\) of unit length, Cauchy's projection identity for a convex polygon gives
\[W_Q(\omega)=\frac12\sum_{i=1}^4|e_i\cdot\omega|,\qquad \mathbb EW_Q=\frac{P}{\pi},\quad P=\sum_{i=1}^4\|e_i\|.\]
For arbitrary nonzero planar vectors \(e,f\), direct integration over the circle yields
\[K(e,f):=\mathbb E[|e\cdot\omega|\,|f\cdot\omega|]
=\frac1\pi\left(|\det(e,f)|+|e\cdot f|\arctan\frac{|e\cdot f|}{|\det(e,f)|}\right),\]
using its continuous limiting value \(K(e,f)=|e\cdot f|/2\) if \(\det(e,f)=0\). Consequently,
\[\mathbb EW_Q^2=\frac14\left(\sum_iK(e_i,e_i)+2\sum_{i<j}K(e_i,e_j)\right),\qquad \mathcal R(Q)=\frac{\pi^2\mathbb EW_Q^2}{P^2}-1.\]
This angular correlation agrees with the established projection-width moment kernel, but the full moduli-space second-variation analysis below is distinct.

**(2) Controlled expansion at the square.** Put \(h=(x,y,a-1,b-1)\). At \(h=0\), the opposite pairs \((e_1,e_3)\), \((e_2,e_4)\) are antiparallel with negative scalar product; the four adjacent edge pairs are perpendicular and have determinant \(-2\). Taylor expansion of the exact kernel gives, uniformly for small \(h\),
\[K(e_i,e_j)=\begin{cases}-\frac12(e_i\cdot e_j)+O(\|h\|^3),&\text{opposite pair},\\[3pt]
\frac1\pi\left(-\det(e_i,e_j)+\frac12(e_i\cdot e_j)^2\right)+O(\|h\|^3),&\text{adjacent pair}.
\end{cases}\]
These estimates follow from \(\arctan t=t+O(t^3)\) at perpendicularity and \(\arctan(1/t)=\pi/2-t+O(t^3)\) at parallelism. Terms with absolute values cancel through quadratic order; hence \(\mathcal R\) is twice continuously differentiable even at coincident edge directions. The diagonal terms are exactly \(K(e_i,e_i)=\|e_i\|^2/2\).

Writing \(\mathcal A=\{(1,2),(2,3),(3,4),(4,1)\}\) and \(\mathcal O=\{(1,3),(2,4)\}\), one obtains the explicit jet
\[\mathbb EW_Q^2=\frac14\left[\frac12\sum_i\|e_i\|^2-\sum_{(i,j)\in\mathcal O}e_i\cdot e_j+
\frac2\pi\sum_{(i,j)\in\mathcal A}\left(-\det(e_i,e_j)+\frac12(e_i\cdot e_j)^2\right)\right]+O(\|h\|^3).\]
Divide by \(P^2/\pi^2\), using the exact differentiable perimeter \(P=\sum\|e_i\|\). A direct second-order expansion yields \(\mathcal R(\mathrm{square})=\pi(\pi+2)/16-1\), zero first derivatives and the matrix \(H\) stated in the finding. The included symbolic checker independently differentiates this jet and tests its exact factorization.

**(3) Signature and geometric meaning.** Put \(u=a-1\), \(v=b-1\). Diagonalizing the quadratic form gives
\[\boxed{\mathcal R(Q)-\mathcal R(\mathrm{square})=
\frac\pi{64}(u+v)^2+\frac{\pi(\pi-2)}{256}(x-y)^2
-\frac{\pi(\pi-2)}{256}\left((x+y)^2+(u-v)^2\right)+O(\|h\|^3).}\]
Both positive and both negative coefficients are strictly nonzero because \(\pi>2\). The parallelogram submanifold in this chart is exactly \(x+y=0\), \(a=b\), and its tangent directions are precisely the positive eigenspace. The negative eigenspace is the complementary two-plane \(x=y\), \(u=-v\). Thus the Hessian is nondegenerate with Morse index two. Since \(\mathcal R(\mathrm{square})>0\) and its first derivative vanishes, the coefficient of variation \(\sqrt{\mathcal R}\) has Hessian \(H/(2\sqrt{\mathcal R(\mathrm{square})})\) and the same signature.

## Verification
The standalone `checker.py` reconstructs the full symbolic Hessian and its characteristic polynomial directly from the second-order correlation jet, with exact algebraic coefficients, then integrates the original vertex-defined directional width over the circle on a fine midpoint grid for independent finite-difference tests in positive, negative and mixed directions. The dependency is recorded in `requirements.txt`. Execute `python checker.py` after installing that dependency. The mathematical proof is analytic; midpoint quadrature supplies only corroboration, not a universal proof.

## Relationship to prior work
Akiyama and Kamae's *Width deviation of convex polygons* (public preprint January 18, 2022; subsequently in *Discrete & Computational Geometry*) defines the same coefficient of variation, derives a general edge-angle moment formula, identifies sharp minimizers for side counts not powers of two, and explicitly flags the unresolved four-gon case with a numerically favored asymmetric kite (Sections 1, 2, 6, 7). The correlation identity above is established background. The present finding is the exact **four-parameter Hessian and its Morse-index-two sign decomposition at the square**, which is not stated in the inspected source. In particular, simply knowing that the square is not globally minimizing does not establish that the square is a nondegenerate critical point, nor identify its exact local stable and unstable tangent spaces. This local structure does not settle global quadrilateral optimization.

## Limitations
The result is local near the square and does not identify a global minimizer or prove uniqueness of any distant kite. Hessian eigenvalues depend on the displayed canonical coordinate gauge; the signature and Morse index do not. The correlation kernel is not new, and the new status of the complete signature is a best-knowledge assessment, not independently established priority. No noisy measurement or statistical estimation theorem is claimed.

## References
- Shigeki Akiyama and Teturo Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1 (first posted January 18, 2022), especially Theorem 1 and Section 7. https://arxiv.org/abs/2201.06736
- S. Akiyama and T. Kamae, *Width Deviation of Convex Polygons*, *Discrete & Computational Geometry* 71 (2024), 1403–1428, DOI:10.1007/s00454-023-00545-6.
