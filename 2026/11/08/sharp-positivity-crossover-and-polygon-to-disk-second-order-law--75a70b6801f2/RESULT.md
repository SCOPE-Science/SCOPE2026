# Sharp positivity crossover and polygon-to-disk second-order law for affine least squares

## Finding
Let \(\Omega_n\) be the filled, circumradius-one regular \(n\)-gon, \(n\ge3\), with normalized area measure \(\mu_n\). Let \(P_n\) be the real \(L^2(\mu_n)\)-orthogonal projection onto \(\operatorname{span}_{\mathbb R}\{1,y_1,y_2\}\). Put
\[
q_n=\frac{2+\cos(2\pi/n)}{12},\qquad k_n=q_n^{-1},\qquad
D_n=\Omega_n\cap\{y:y_1<-q_n\},
\]
and let \(A_n=n\sin(2\pi/n)/2\) be polygon area. Define
\[
C_n=-\frac1{A_n}\int_{D_n}(1+k_n y_1)\,dy.
\]
Then the exact endpoint norm and the sharp loss of positivity are
\[
\|P_n\|_{L^\infty(\mu_n)\to L^\infty(\mu_n)}=1+2C_n,
\qquad
\inf_{0\le f\le1}\min_{x\in\Omega_n}(P_nf)(x)=-C_n.
\]
Precisely the vertices of \(\Omega_n\) are norming evaluation locations. At a vertex \(v\), the norming unit inputs, up to null sets, are the two signs \(\pm\operatorname{sgn}(1+k_n v\cdot y)\); the sharp positivity-loss input is \(\mathbf1_{\{1+k_n v\cdot y<0\}}\). For every \(n\), the cap integral above has the explicit finite algebraic-trigonometric shoelace formula described below.

The endpoint norm undergoes an exact side-number crossover:
\[
\boxed{\ \|P_n\|>2\quad(3\le n\le6),\qquad
\|P_n\|<2\quad(n\ge7).\ }
\]
For instance, \(\|P_3\|=19/8\), \(\|P_4\|=233/108\), and \(\|P_6\|=361/180\). Moreover, with \(\Lambda_\circ\) the corresponding filled-unit-disk affine projection norm,
\[
\Lambda_\circ=\frac{11\sqrt{15}}{8\pi}+\frac2\pi\arcsin(1/4),\qquad
\boxed{\ \lim_{n\to\infty}n^2\bigl(\|P_n\|-\Lambda_\circ\bigr)=\frac{5\pi\sqrt{15}}{12}>0.\ }
\]
The norm converges to its disk value from above at a precise second-order rate, even though the norm is already below \(2\) from the heptagon onward.

## Assumptions and scope
The measure is two-dimensional uniform **area**, not boundary arclength or uniform vertex measure. The polygon is filled, convex and regular, with vertices \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), \(0\le j<n\); geometric scaling leaves the operator norm unchanged. Functions and projection coefficients are real. The endpoint norm takes the essential supremum of inputs and the continuous maximum of outputs. Positivity defect is optimized over measurable inputs between zero and one; null-set changes do not affect the conclusion.

## Proof
### Kernel, endpoint norm and equality cases
Rotational symmetry gives \(\mathbb E_{\mu_n}y=0\) and \(\mathbb E_{\mu_n}(yy^{\mathsf T})=q_n I_2\). To calculate \(q_n\), triangulate the polygon into \(n\) congruent triangles \(\operatorname{conv}\{0,v_j,v_{j+1}\}\). For uniform barycentric coefficients \(s,t\) on the standard triangle, \(\mathbb E s^2=\mathbb E t^2=1/6\), \(\mathbb E st=1/12\), hence \(\mathbb E\|y\|^2=(2+\cos(2\pi/n))/6\). Thus the real reproducing kernel is
\[
K_n(x,y)=1+k_n x\cdot y.
\]
For a fixed \(x\), the norm of evaluation is \(F_n(x)=\mathbb E_{\mu_n}|K_n(x,Y)|\). This is convex in \(x\), and therefore reaches its maximum at some polygon vertex. At each vertex its negative-kernel mass is \(C_n\); rotational symmetry makes the vertex values equal, yielding \(\|P_n\|=1+2C_n\) because \(\int K_n(x,y)d\mu_n(y)=1\).

To show that no nonvertex is norming, observe that for any distinct vertices \(v,w\), both affine level lines \(v\cdot y=-q_n\) and \(w\cdot y=-q_n\) cross the polygon interior. These lines are distinct; consequently there is a set of positive area on which \(K_n(v,\cdot)\) and \(K_n(w,\cdot)\) have opposite signs. The absolute-value triangle inequality is then strict when averaging the two kernel rows with any nontrivial weights. Every nonvertex is a nontrivial convex combination of distinct vertices, giving a strict deficit. Sign rigidity away from the kernel's zero line gives the stated extremizing inputs. Replacing a sign input by the indicator of the negative kernel gives exactly the sharp loss of positivity.

### Exact finite expression
Construct \(D_n\) by clipping the ordered polygon vertices against \(y_1<-q_n\). Every crossing-edge intersection between \(a\) and \(b\) is
\[
p=a+\frac{-q_n-a_1}{b_1-a_1}(b-a).
\]
Let \(p_0,\dots,p_{r-1}\) denote the resulting counterclockwise cap-polygon vertices. Set \(\Delta_j=\det(p_j,p_{j+1})\), with cyclic indexing. Shoelace area and first-moment integration give
\[
\boxed{\ C_n=-\frac{1}{A_n}\left[
\frac12\sum_{j=0}^{r-1}\Delta_j+\frac{k_n}{6}
\sum_{j=0}^{r-1}\Delta_j(p_{j,1}+p_{j+1,1})\right].\ }
\]
The cap is nonempty for all \(n\ge3\). This is an exact finite expression involving only elementary trigonometric numbers and arithmetic, valid even when a clipping line meets a polygon vertex (duplicate points may be omitted). It is not a numerical quadrature approximation.

### Exact crossover at six sides
For \(3\le n\le11\), substitute the cap-polygon vertices into the preceding formula. The three rational cases stated above follow directly. In particular \(C_n>1/2\) for \(n=3,4,5,6\) and \(C_n<1/2\) for \(n=7,8,9,10,11\). The included `check_polygon.py` constructs **rational interval bounds** for every trigonometric coordinate using Machin's formula for \(\pi\), alternating arctangent sums, Taylor bounds, exact rational arithmetic and shoelace integration. Its strict inequalities certify these nine finite statements without using floating-point sampling.

For the remaining infinitely many \(n\), let \(B(k)\) be the negative-kernel mass over the uniform unit disk, with kernel \(1+ky_1\). Elementary one-variable integration gives, for \(k>1\),
\[
B(k)=-\frac12+\frac{k^{-1}\sqrt{1-k^{-2}}+\arcsin(k^{-1})}{\pi}
+\frac{2k}{3\pi}(1-k^{-2})^{3/2}.
\]
Because \(\Omega_n\subseteq\{\|y\|\le1\}\) and the negative-part integrand is nonnegative,
\[
C_n\le\frac{\pi}{A_n}B(k_n).
\]
As \(n\) increases, \(A_n=\pi\sin(2\pi/n)/(2\pi/n)\) strictly increases and \(k_n\) strictly decreases. Also \(B(k)\) increases with \(k\) because it integrates \((-1-ky_1)_+\) over negative \(y_1\). Hence for every \(n\ge11\),
\[
C_n\le\frac{\pi}{A_{11}} B(k_{11})<\frac12.
\]
The final strict inequality is proved by rational interval bounds in the same standalone checker, using the convergent positive series for \(\arcsin\) with a geometric remainder and a rational square-root enclosure. This proves the universal crossover.

### Sharp second-order polygon-to-disk convergence
Write \(h=\pi/n\), and let \(R_n(\theta)\) be the radial boundary of the polygon. On the angular cell around any facet normal, with offset \(\phi\in[-h,h]\),
\[
R_n(\theta)=\frac{\cos h}{\cos\phi}
=1-\frac{h^2-\phi^2}{2}+O(h^4)
\]
uniformly. The cell average of \((h^2-\phi^2)/2\) is \(h^2/3\). By Riemann sums, for each continuous angular function \(g\),
\[
\int_0^{2\pi}(1-R_n(\theta))g(\theta)d\theta
=\frac{h^2}{3}\int_0^{2\pi}g(\theta)d\theta+o(h^2).
\]
Furthermore \(k_n=4+8h^2/3+O(h^4)\) and \(A_n=\pi(1-2h^2/3+O(h^4))\). The negative-part integrand is uniformly Lipschitz; its derivative with respect to \(k\) exists away from a zero-area level line. Therefore the bulk parameter perturbation and the boundary-shell removal yield
\[
C_n=C_\circ+h^2\left(\frac83J-\frac13 H+\frac23C_\circ\right)+o(h^2),
\]
where the disk integrals are
\[
\begin{aligned}
C_\circ&=-\frac12+\frac{11\sqrt{15}}{16\pi}+\frac{\arcsin(1/4)}{\pi},\\
J&=\frac1\pi\int_{\|y\|\le1}(-y_1)\mathbf1_{\{y_1<-1/4\}}dy=\frac{5\sqrt{15}}{32\pi},\\
H&=\frac1\pi\int_0^{2\pi}(-1-4\cos\theta)_+d\theta
=\frac2\pi\bigl(\sqrt{15}-\arccos(1/4)\bigr).
\end{aligned}
\]
Using \(\arcsin(1/4)+\arccos(1/4)=\pi/2\), the bracket simplifies **exactly** to \(5\sqrt{15}/(24\pi)\). Since \(h=\pi/n\) and \(\|P_n\|=1+2C_n\), the second-order limit follows.

## Verification
Execute `python3 check_polygon.py` with the Python standard library. The script proves all nine finite cap comparisons with rational intervals, gives rigorous rational bounds for the disk comparison at \(n=11\), and prints `ALL_REGULAR_POLYGON_INTERVAL_CHECKS_PASSED`. The exact asymptotic constant follows from the displayed symbolic integral identities and uniform radial expansion, not from finite tests. Numerical illustrations are not used as proof.

## Relationship to prior work
Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first version May 13, 2010) establish general \(L^p\)-stability and near-best approximation results for least-squares projectors in positive-definite kernel spaces on manifolds. Their Theorem 5.1 does not give the filled-polygon affine projection norm, the six-to-seven-side threshold or the second-order coefficient. Established exact affine projector results on simplices determine the triangle case, and an exact filled-disk result determines the limiting constant; neither implies the polygonal crossing or its positive correction coefficient. Arclength projection on the perimeter of a regular polygon uses a different measure and has a different limiting constant. The general kernel identity and cap-clipping formula are elementary ingredients; the side-number classification and exact asymptotic coefficient are the conclusions being asserted here.

## Limitations
The result concerns real affine \(L^2\) projection on **uniform filled regular polygons**. No norm monotonicity in the number of sides is asserted. It does not cover general irregular polygons, polygonal boundary arclength, higher-degree polynomial spaces or complex-valued projection norms. An equivalent unindexed result in older approximation literature is a residual originality risk. The universal proof is analytical; the rational checker certifies only the finite sign tests explicitly delegated to it.

## References
- T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424, version 1 dated 2010-05-13, published in SIAM Journal on Mathematical Analysis 43 (2011), 662–684, DOI:10.1137/100795334.
- Published exact affine projection computations on simplices, filled Euclidean balls and uniform regular-polygon perimeters provide domain- or measure-specific comparators; none is needed as an unproved lemma here.
