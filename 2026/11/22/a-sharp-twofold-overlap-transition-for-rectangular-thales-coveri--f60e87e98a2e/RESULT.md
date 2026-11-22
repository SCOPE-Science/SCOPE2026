# A sharp twofold-overlap transition for rectangular Thales coverings

## Finding
Let \(P=[-a,a]\times[-b,b]\) with \(a,b>0\), and let \(D_{\varepsilon,\eta}\) be the Euclidean closed disk having diameter from \((0,0)\) to \((\varepsilon a,\eta b)\), where \(\varepsilon,\eta\in\{-1,1\}\). For a uniformly area-sampled \(X\in P\), let \(N(X)\) count the four disks containing \(X\). Almost every point belongs to exactly one or exactly two disks, and every point of \(P\) belongs to at least one.

Put \(\lambda=\max(a,b)/\min(a,b)\ge1\) and \(q(\lambda)=\Pr\{N(X)=2\}\). The complete closed formula is
\[
q(\lambda)=\frac{\pi}{8}(\lambda+\lambda^{-1})-\frac12-\frac{\Phi(\lambda)}{4\lambda},
\]
where
\[
\Phi(\lambda)=\begin{cases}
0,&1\le\lambda\le2\sqrt2,\\
(\lambda^2+1)\arctan\!\left(\frac{\sqrt{\lambda^2-8}}3\right)-3\sqrt{\lambda^2-8},&\lambda>2\sqrt2.
\end{cases}
\]
Consequently \(q(1)=\pi/4-1/2\), the function \(q\) is strictly increasing on \([1,\infty)\), and
\[
q(\lambda)=1-\frac{3}{2\lambda^2}+O(\lambda^{-4})\qquad (\lambda\to\infty).
\]
There is a genuine shape transition at \(\lambda_0=2\sqrt2\): \(q\) is \(C^1\) but not \(C^2\) there. Specifically, as \(\lambda\downarrow\lambda_0\) from above,
\[
q(\lambda)=\frac\pi8(\lambda+\lambda^{-1})-\frac12
-\frac{2^{5/4}}9(\lambda-2\sqrt2)^{3/2}+O((\lambda-2\sqrt2)^{5/2}).
\]
The expected number of disks covering a uniform point is exactly \(1+q(\lambda)\).

## Assumptions and scope
The center must be the center of the axis-parallel rectangle. The four closed disks have *exactly* the four diameters indicated; neither disk radii nor locations may be optimized. Area probabilities use ordinary planar Lebesgue measure divided by \(4ab\). Boundary or origin contacts are not assigned an almost-everywhere multiplicity. The parameter \(\lambda\) ranges over all finite \(\lambda\ge1\), including the square and the transition.

## Proof
For \(x=(u,v)\), completion of the square gives the exact membership rule
\[
x\in D_{\varepsilon,\eta}\quad\Longleftrightarrow\quad
u^2+v^2\le\varepsilon au+\eta bv.
\]
In the first quadrant put \(A=au\), \(B=bv\), \(S=u^2+v^2\). The four right-hand sides are \(A+B,A-B,-A+B,-A-B\). Since \(0\le u\le a\) and \(0\le v\le b\), \(S\le A+B\); for any nonzero point, \(S>0\). Thus there is at least one covering disk and at most two (outside measure-zero ties). Exactly two means \(S\le|A-B|\). The two disjoint open-area lobes in the positive quadrant are \(u^2+v^2+bv\le au\) and \(u^2+v^2+au\le bv\). They are exchanged by swapping \(a,b\) and \(u,v\).

The area of the first lobe is
\[
F(a,b)=\int_0^a\min\!\left\{b,\frac{\sqrt{b^2+4u(a-u)}-b}{2}\right\}\,du.
\]
Without the cap at \(b\), this integral is
\[
F_0(a,b)=\frac{(a^2+b^2)\arctan(a/b)-ab}{4}.
\]
The cap activates precisely when \(a>\sqrt8\,b\), in the interval \(\frac{a-T}2<u<\frac{a+T}2\), where \(T=\sqrt{a^2-8b^2}\). The amount to subtract is
\[
\frac14\left[(a^2+b^2)\arctan(T/(3b))-3bT\right].
\]
By four-quadrant symmetry, the exactly-two area is \(4(F(a,b)+F(b,a))\). Using \(\arctan(a/b)+\arctan(b/a)=\pi/2\), division by \(4ab\) yields the displayed formula.

For \(1<\lambda\le2\sqrt2\), differentiating gives \(q'(\lambda)=\frac\pi8(1-\lambda^{-2})>0\). Above the transition, write \(T=\sqrt{\lambda^2-8}>0\). Direct differentiation and the arctangent complement identity yield
\[
q'(\lambda)=\frac{(T^2+7)\arctan(3/T)-3T}{4\lambda^2}.
\]
Since \(\arctan(3/T)=T\int_0^3(T^2+s^2)^{-1}\,ds\), strict Jensen convexity of \(z\mapsto(T^2+z)^{-1}\), together with \(\frac13\int_0^3s^2\,ds=3\), gives
\[
\int_0^3\frac{ds}{T^2+s^2}>\frac3{T^2+3}.
\]
Therefore the numerator exceeds \(T[3(T^2+7)/(T^2+3)-3]=12T/(T^2+3)>0\). Continuity covers the transition and strict increase from the square.

Finally, \(\Phi(\lambda)=(2/9)(\lambda^2-8)^{3/2}+O((\lambda^2-8)^{5/2})\) at the threshold, giving the nonzero \(3/2\)-power term above. For the long-rectangle limit, set
\[
G(t)=\int_0^1\min\left\{1,\frac{\sqrt{1+4t^2x(1-x)}-1}{2}\right\}\,dx,
\]
so that \(q(\lambda)=G(\lambda)+G(\lambda^{-1})\). A Taylor expansion gives \(G(\lambda^{-1})=1/(6\lambda^2)+O(\lambda^{-4})\). For \(G(\lambda)\), only intervals of width \(O(\lambda^{-2})\) near both endpoints contribute to the uncovered part. Substituting \(x=z/\lambda^2\) at each endpoint, and expanding the smooth factors, gives
\[
1-G(\lambda)=\lambda^{-2}\int_0^2[3-\sqrt{1+4z}]\,dz+O(\lambda^{-4})
=\frac5{3\lambda^2}+O(\lambda^{-4}).
\]
The two expansions imply the asserted coefficient \(3/2\). The mean multiplicity identity follows because the multiplicity is one or two almost everywhere.

## Verification
The independently computed one-dimensional integral and a direct test of all four disk inequalities on rectangular grids agree with the closed formula for eight aspect ratios, including \(2\sqrt2\) and values on both sides. The standalone `verify.py` makes those computations, checks 999 monotonicity samples, and checks the leading asymptotic coefficient. These finite checks are corroboration only: the mathematical proof is the exact geometric integration and analytic inequalities above.

## Relationship to prior work
Pavlík (2026, first posted 10 November) proves the general coverage of polytopes by vertex-to-point diameter balls (Theorem 5.1), but does not quantify overlap-area distributions of nonregular rectangles. An accessible published record on regular-polygon diameter disks determines full multiplicity area spectra for *regular* polygons, including our isolated square endpoint; that theorem does not imply the unequal-side branch, its \(2\sqrt2\) transition, or monotonicity. The separately published rectangle disk-covering optimization problem permits adjustable disk locations and sizes, whereas the present four disk diameters are prescribed. The formula uses classical circular-segment integration, whose constituent integrals are not claimed as original.

## Limitations
No claim is made for centers displaced from the rectangle center, parallelograms with nonorthogonal sides, dimension above two, or arbitrary polygons. The proof gives exact planar Lebesgue area, not the area of overlap *outside* the rectangle. Priority beyond the specifically inspected sources remains subject to independent verification.

## References
1. J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, first posted 2026-11-10; theorem 5.1. https://arxiv.org/abs/2611.14277
2. *Exact multiplicity spectrum of vertex-to-center diameter disks of regular polygons*, published-finding corpus mathematical record, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-multiplicity-spectrum-of-vertex-to-center-diameter-disks-o--1b3f060ecc28
3. *Worst-Case Optimal Covering of Rectangles by Disks*, Discrete & Computational Geometry (2023), doi:10.1007/s00454-023-00582-1. https://doi.org/10.1007/s00454-023-00582-1
