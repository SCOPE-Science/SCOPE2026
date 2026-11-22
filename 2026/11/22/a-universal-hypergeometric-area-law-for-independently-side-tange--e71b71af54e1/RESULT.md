# A universal hypergeometric area law for independently side-tangent triangle inellipses

## Finding
Fix a nondegenerate Euclidean triangle \(T\), choose two of its sides sharing a vertex, and choose one point independently and uniformly by length in the relative interior of each chosen side. There is a unique ellipse tangent to all three sides with those two contact points. Write \(A\) for the area of this ellipse divided by the area of \(T\). Then the entire law of \(A\) is independent of triangle shape and of the chosen adjacent sides. Its exact moment transform, for every real \(s\ge0\), is
\[
\mathbb E[A^s]=\pi^s B(1+s/2,1+s)^2\,{}_3F_2\!\left(\begin{matrix}3s/2,1+s/2,1+s/2\\2+3s/2,2+3s/2\end{matrix};1\right).
\]
In particular \(\mathbb E[A]=0.33817308452717244\ldots\) and \(\mathbb E[A^2]=0.14348892714188599\ldots\). The maximum possible ratio is \(a_*=\pi/(3\sqrt3)\). It is uniquely attained by the Steiner inellipse, whose three contacts are midpoints. The near-maximum probability has the sharp linear law
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr(A>a_*-\varepsilon)}{\varepsilon}=\frac94.
\]
This is a distribution for *independent uniformly sampled contacts* on two fixed sides, not a distribution for ellipses sampled with centers uniform in the medial triangle.

## Assumptions and scope
All triangles are nondegenerate and Euclidean. Uniformity means normalized one-dimensional arclength along each selected side, independently. Ellipses are closed, nondegenerate and tangent to all three sides; the random contacts have probability one of lying in the side interiors. The quotient of ellipse area by parent triangle area removes scale. The Gauss hypergeometric notation \({}_3F_2\) is defined by its convergent generalized hypergeometric series, and \(B\) denotes the Euler beta function. The moment formula is asserted for \(s\ge0\); no unsupported negative-moment integrability statement is needed.

## Proof
**1. Exact geometric parameterization.** By an invertible affine map, reduce to the right triangle with vertices \((0,0),(1,0),(0,1)\). A uniform arclength fraction along a side remains uniform after this map. Write the two independent side-contact fractions as \(t,w\in(0,1)\), and set \(H=t+w-tw\). The classical inellipse parametrization gives the center \((u,v)=(t/(2H),w/(2H))\). Existence and uniqueness can also be seen directly. For an ellipse \(E=(u,v)+Q^{1/2}\overline B_2\) to be tangent to the three lines \(x=0\), \(y=0\), and \(1-x-y=0\) while remaining inside their positive halfplanes, it is necessary and sufficient that
\[
Q_{11}=u^2,\quad Q_{22}=v^2,\quad Q_{12}=\tfrac12[(1-u-v)^2-u^2-v^2].
\]
The displayed center belongs to the open medial triangle and makes this matrix positive definite, which proves that the ellipse is uniquely specified by its center. Its side contacts are exactly \((t,0)\) and \((0,w)\): for instance the tangency on \(x=0\) has \(y=v-Q_{12}/u=w\), and the other contact follows symmetrically.

**2. Heron identity and exact area map.** Put \(z=1-u-v\). Direct determinant expansion followed by Heron's formula for a triangle of side lengths \(u,v,z\) gives
\[
\det Q=u^2v^2-\tfrac14(z^2-u^2-v^2)^2=4\Delta(u,v,z)^2.
\]
Here \(u,v,z<1/2\), so they satisfy the strict triangle inequalities. With \(p=1-2u\), \(q=1-2v\), \(r=1-2z\), one has \(p+q+r=1\) and \(\Delta(u,v,z)^2=pqr/16\). The ellipse area is \(\pi\sqrt{\det Q}\), whereas the normalized reference triangle has area \(1/2\). Thus \(A=\pi\sqrt{pqr}\). Substitution of the contact center gives
\[
p=\frac{w(1-t)}H,\quad q=\frac{t(1-w)}H,\quad r=\frac{tw}H,\quad
A(t,w)=\frac{\pi tw\sqrt{(1-t)(1-w)}}{(t+w-tw)^{3/2}}.
\]
This identity is exact throughout the open unit square. Because the derivation commutes with affine maps, the law is independent of the shape of \(T\).

**3. All nonnegative moments.** Set \(x=1-t\), \(y=1-w\). Since \(x,y\) remain independent uniform variables,
\[
\mathbb E[A^s]/\pi^s=\int_0^1\!\int_0^1\frac{x^{s/2}(1-x)^s y^{s/2}(1-y)^s}{(1-xy)^{3s/2}}\,dx\,dy.
\]
For \(s\ge0\), the binomial series \((1-xy)^{-3s/2}=\sum_{k\ge0}(3s/2)_k(xy)^k/k!\) has nonnegative terms (the \(s=0\) case is the constant series), so monotone convergence permits termwise integration. Each factor is \(B(1+s/2+k,1+s)\). Using beta-to-Pochhammer identities yields exactly the stated \({}_3F_2\) transform; the series converges at one because its parameter excess is \(2+s/2>0\). Since \(A\) is compactly supported, these integer moments determine its probability law uniquely. The first two numerical constants follow by this absolutely convergent series, with independent quadrature checks.

**4. Sharp upper endpoint.** The variables \(p,q,r\) are positive with sum one. AM–GM gives \(pqr\le1/27\), equality only at \(p=q=r=1/3\), corresponding uniquely to \(t=w=1/2\). Differentiating the explicit expression for \(A(t,w)\) at this point yields gradient zero and negative Hessian
\[
-D^2A(1/2,1/2)=\frac{8\sqrt3\pi}{27}\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
\sqrt{\det(-D^2A)}=\frac{8\pi}{9}.
\]
Consequently the set \(A>a_*-\varepsilon\) is a smooth shrinking ellipse to quadratic order. Its area, which is its probability under the uniform \((t,w)\) law, equals \(2\pi\varepsilon/(8\pi/9)+o(\varepsilon)=(9/4)\varepsilon+o(\varepsilon)\). Compactness and uniqueness of the maximizer exclude competing near-optimal regions elsewhere in the closed parameter square; the continuous area map extends by zero at the relevant boundary limits.

## Verification
The accompanying `check_random_inellipse.py` uses only the Python standard library. It checks 20,000 independently sampled geometric area and covariance identities, numerical quadrature on a \(680\times680\) midpoint grid for three moments against independently summed hypergeometric series, the maximum, and Hessian entries. Execute `python check_random_inellipse.py` in the directory containing the extracted file. These finite checks supplement and do not establish the analytic theorem.

## Relationship to prior work
The existence and one-to-one contact parameterization of triangle inellipses is classical and explicitly given by A. Horwitz, *Dynamics of ellipses inscribed in triangles*, arXiv:1504.05141 (2015). The Steiner inellipse and its maximal area are classical. Those results are used as input and are not claimed as new. The new claim here is the complete shape-independent pushforward probability law under *independent uniformly sampled side contacts*, its exact all-moment hypergeometric transform, and the sharp near-optimum coefficient. In contrast, uniform selection of an inellipse's center in the medial triangle induces a different area law, equivalent to an elementary broken-stick construction; it is not the sampling measure studied here. General published results on other random triangles and conic optimization do not supply the specified pushforward measure and distribution.

## Limitations
The sampling model is essential. A center-uniform inellipse, a Euclidean-uniform contact point on the third side, or tangent points sampled with dependence gives a different law. All assertions concern area rather than eccentricity, focal geometry, or randomly oriented side selections with other weights. The moment expression is an exact convergent special-function representation rather than an elementary closed-form CDF. Novelty is assessed against the examined literature but not independently certified.

## References
1. A. Horwitz, *Dynamics of ellipses inscribed in triangles*, arXiv:1504.05141v1 (first public 2015-04-20), https://arxiv.org/abs/1504.05141 .
2. A. Horwitz, *The locus of centers of ellipses inscribed in quadrilaterals*, arXiv:math/0312403v1 (2003), https://arxiv.org/abs/math/0312403 .
3. Classical Steiner inellipse facts and area ratio, https://mathworld.wolfram.com/SteinerInellipse.html .
4. E. W. Weisstein, *Broken Stick Problem*, https://mathworld.wolfram.com/BrokenStickProblem.html (background on the distinct center-uniform sampling analogy).
