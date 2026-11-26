# All-orders endpoint expansion for the BCC Voronoi radial law

## Finding

Let \(L=\mathbb Z^3\cup(\mathbb Z^3+(1/2,1/2,1/2))\) and let \(X\) be uniform in its centered Euclidean Voronoi cell \(V\). Set \(R^2=5/16\), the maximum squared distance from \(0\) in \(V\). Luo's facet quadrature determines the radial distribution (see Relationship to prior work). Here we extract its **convergent all-orders endpoint expansion** by resolving the 24 extremal vertex caps. The resulting fixed-simplex representation, valid for \(0<\varepsilon<1/64\), is

\[
\mathbb P\bigl(R^2-\|X\|_2^2<\varepsilon\bigr)
=256\int_{\Delta}\left(\frac{2\varepsilon}{1+\sqrt{1-32\varepsilon H(a,b,c)}}\right)^3\,da\,db,
\]

where \(\Delta=\{(a,b):a\ge0,\ b\ge0,\ a+b\le1\}\), \(c=1-a-b\), and

\[
H(a,b,c)=a^2-a(b+c)+b^2+c^2.
\]

The resulting explicit coefficients are

\[
\begin{aligned}
\mathbb P\bigl(R^2-\|X\|_2^2<\varepsilon\bigr)
&=\sum_{m=0}^{\infty}C_m\varepsilon^{m+3}\\
&=128\varepsilon^3+1024\varepsilon^4+\frac{53248}{5}\varepsilon^5+O(\varepsilon^6),\\
C_m&=\frac{768\,8^m}{m+3}\binom{2m+2}{m}\int_{\Delta}H(a,b,1-a-b)^m\,da\,db.
\end{aligned}
\]

Every \(C_m\) is a strictly positive rational number. As a consequence, for independent uniform points \(X_1,\dots,X_N\in V\) and \(M_N=\max_{1\le j\le N}\|X_j\|_2^2\), the near-covering-radius sample extreme has the limiting law

\[
\lim_{N\to\infty}\mathbb P\bigl(N^{1/3}(R^2-M_N)>t\bigr)=\exp(-128t^3),\qquad t\ge0.
\]

The scaling is the *unscaled* BCC lattice of covolume \(1/2\). On the unit-covolume BCC lattice all squared lengths are multiplied by \(2^{2/3}\); the probability is unchanged after the same rescaling of the deficit.

## Assumptions and scope

All Euclidean norms are standard. The closed Voronoi cell includes its facets, which do not affect uniform-volume probabilities. All probability statements concern three dimensions and the fixed exact BCC lattice \(L\) above. \(\varepsilon\) is the **squared-distance deficit**, not the distance deficit. The stated upper endpoint \(1/64\) is an explicit sufficient range for the exact integral; no assertion that it is the largest possible range is made. The sampling limit assumes independent points from the same uniform-cell distribution.

## Proof

**1. The cell and its extremal vertices.** The relevant lattice bisectors give the closed polytope

\[
V=[-1/2,1/2]^3\cap\{x:\|x\|_1\le3/4\}.
\]

Indeed the bisectors of the six axial lattice vectors yield the cube inequalities, and those of the eight vectors \((\pm1/2,\pm1/2,\pm1/2)\) yield the \(\ell_1\) inequality. Conversely, for any \(z\in\mathbb Z^3\), the cube inequalities imply \(2x\cdot z\le\sum_i|z_i|\le\|z\|_2^2\). Every other lattice vector has coordinates \(s_i(n_i+1/2)\) with \(s_i\in\{-1,1\}\) and \(n_i\in\mathbb Z_{\ge0}\); then

\[
2x\cdot(s_i(n_i+1/2))_{i=1}^3
\le \|x\|_1+2\sum_i n_i|x_i|
\le 3/4+\sum_i n_i
\le\sum_i(n_i+1/2)^2.
\]

Thus no other lattice vector cuts the polytope. Its complete vertex set is the set of signed coordinate permutations of \((1/2,1/4,0)\), comprising exactly 24 vertices, each of squared norm \(R^2=5/16\). For the positive octant, the volume is \(2^{-3}\) times the probability-volume \(\bigl((3/2)^3-3(1/2)^3\bigr)/6=1/2\) in the unit cube under \(y_1+y_2+y_3\le3/2\). Therefore \(\operatorname{vol}(V)=1/2\).

**2. Global vertex localization.** For any \(x\in V\), write \(x=\sum_v\lambda_vv\), \(\lambda_v\ge0\), \(\sum_v\lambda_v=1\), over those 24 vertices. Since every vertex has squared norm \(R^2\),

\[
R^2-\|x\|_2^2=\sum_v\lambda_v\|v-x\|_2^2.
\]

Consequently, if the deficit is less than \(\varepsilon<1/64\), \(x\) belongs to an open ball of radius \(1/8\) about some vertex. The least squared separation between distinct vertices is \(1/8\), so these 24 open balls are disjoint. At \(v=(1/2,1/4,0)\), the only bounding facets meeting the vertex are

\[
x_1\le1/2,\qquad x_1+x_2+x_3\le3/4,\qquad x_1+x_2-x_3\le3/4.
\]

Every other supporting plane has Euclidean distance at least \(1/4\) from \(v\). Hence within the radius-\(1/8\) ball, membership in \(V\) is equivalent to these three halfspaces. Signed coordinate symmetries handle the other vertices.

**3. Exact vertex-cap integration.** Parametrize the resulting trihedral cone at \(v\) by

\[
x=(1/2-2p,\ 1/4+2p-2q-2r,\ 2r-2q),\qquad p,q,r\ge0.
\]

The absolute coordinate Jacobian is 16. The squared-distance deficit becomes the exact quadratic

\[
R^2-\|x\|_2^2=(p+q+r)-8\bigl(p^2-p(q+r)+q^2+r^2\bigr).
\]

Put \(p=ta,\ q=tb,\ r=tc\), with \(t\ge0\), \((a,b)\in\Delta\), \(c=1-a-b\). The Jacobian is \(t^2\,dt\,da\,db\), and the deficit is \(t-8H(a,b,c)t^2\). On \(\Delta\),

\[
1/10\le H\le1;
\]

the lower bound follows from \(b^2+c^2\ge(b+c)^2/2\), and the upper bound follows from convexity of \(H\) on the simplex and its value 1 at each vertex. For \(0<\varepsilon<1/64\), the smaller root of \(t-8Ht^2=\varepsilon\) is

\[
t_-(\varepsilon,H)=\frac{2\varepsilon}{1+\sqrt{1-32H\varepsilon}}.
\]

It satisfies \(t_-\le2\varepsilon<1/32\), so \(8Ht_-^2<1/128\): the entire initial cone segment \(0\le t<t_-\) lies in the radius-\(1/8\) ball. Conversely, a point in that ball with deficit less than \(\varepsilon\) cannot lie beyond the larger root \(t_+\), since \(t_+\ge1/16\) would give \(\|x-v\|_2^2=8Ht^2=t-(R^2-\|x\|_2^2)>3/64>1/64\), a contradiction. The quadratic is at least \(\varepsilon\) between its two roots. Thus precisely \(0\le t<t_-\) contributes inside each small vertex ball.

Integrating \(16t^2\,dt\,da\,db\) yields \(\frac{16}{3}\int_\Delta t_-^3\) of volume per vertex. Multiply by 24 vertices and divide by \(\operatorname{vol}(V)=1/2\) to obtain the stated exact probability integral.

**4. Positive rational series and sample extremes.** The root satisfies \(t_-=\varepsilon+8Ht_-^2\), so Lagrange inversion gives, for all \(m\ge0\),

\[
[\varepsilon^{m+3}]\,t_-^3=\frac{3}{m+3}\binom{2m+2}{m}(8H)^m.
\]

The expansion converges uniformly on \(\Delta\) whenever \(\varepsilon<1/64\), because \(32H\varepsilon<1/2\). Direct simplex integration gives \(\int_\Delta1=1/2\), \(\int_\Delta H=1/6\), \(\int_\Delta H^2=13/180\), proving the three displayed coefficients. Polynomial simplex integration produces rational coefficients; positivity follows from \(H\ge1/10\). Finally, set \(\varepsilon=tN^{-1/3}\) and use \((1-128t^3/N+o(N^{-1}))^N\to e^{-128t^3}\).

## Verification

The included `check_bcc_tail.py` requires only Python 3 and reproduces independent exact-rational checks of all 14 halfspaces and their triple intersections, the 24 vertices, their common squared radius and incident-facet count, the vertex separation, the volume calculation, the cone-coordinate identity, the coordinate Jacobian, and the first seven exact simplex moments and endpoint coefficients. It prints the explicit fractions and raises an exception if a check fails. The conceptual steps for all \(\varepsilon\) and all orders are the preceding analytic proof, not the finite checker.

To reproduce: run `python3 check_bcc_tail.py` from the package directory. The conclusion does not use floating-point integration or stochastic sampling. There is no claim that the checker proves independent novelty or global lattice optimality.

## Relationship to prior work

Luo's Proposition 2.3 and equations (2.8)–(2.9) supply an alternative, global representation of this same radial law. Write \(Q\) for the value of one of Luo's two quadratics at a uniform point of \([-1,1]^2\), using the square quadratic with probability \(1/4\) and the rhombus quadratic with probability \(3/4\). Let \(U\) have density \(3u^2\) on \([0,1]\), independent of \(Q\). Equation (2.9) and \(\operatorname{vol}(V)=1/2\) give
\[
\mathbb E\|X\|^p=2^{-p/3} E_p(A_{\rm bcc})=\mathbb E\bigl[(U\sqrt Q/2)^p\bigr].
\]
The even powers, together with total mass one, identify the squared-radius distribution by compact-support moment determinacy. Equivalently, one can integrate the radial variable directly in the facet pyramids of Proposition 2.3, obtaining \(\Pr(\|X\|^2>s)=\mathbb E[(1-(4s/Q)^{3/2})_+]\) for \(s\ge0\). The contribution here is not identification of the radial distribution from scratch, but a fixed-simplex cap representation adapted to the endpoint and the explicit positive rational coefficient formula there. In the facet quadrature the contributing part of the square shrinks with the deficit, so one cannot obtain those coefficients by simply taking Taylor coefficients of the unrestricted integrand. The sample extreme law is a consequence of the leading cap coefficient.

Bourne–Cagnetti–Roper studied lattice optimality, Barnes–Sloane addressed mean square distortion, and Bambah the covering radius. General Voronoi-cell geometry and the regular truncated-octahedral vertex configuration are not new.

A public result on the four-dimensional \(D_4\) Voronoi 24-cell has a related near-covering-radius analytic method but treats a different lattice, dimension, cell and local cone. Results on regular-simplex nearest-vertex error likewise do not yield the 3D BCC coefficients. These are not claims of first use of local cone expansions generally.

## Limitations

The fixed-simplex endpoint integral is proved for \(0<\varepsilon<1/64\); the largest validity interval for this representation is not asserted. This is an exact *fixed-cell* statement, not a new optimization theorem comparing lattices. The series is convergent for the stated interval, but its unscaled coefficients must be rescaled for other covolumes. No priority is asserted for the underlying radial distribution or for the general use of local cone expansions.

## References

- Senping Luo, *The BCC lattice is the optimal 3D lattice quantizer for all \(p\ge1\)*, arXiv:2611.09523v1, first submitted 6 November 2026, https://arxiv.org/html/2611.09523v1.
- David P. Bourne, Filippo Cagnetti and Steven M. Roper, *Optimality of the BCC lattice among 3D lattice quantizers*, arXiv:2610.39705v1, 29 October 2026, https://arxiv.org/abs/2610.39705.
- E. S. Barnes and N. J. A. Sloane, *The optimal lattice quantizer in three dimensions*, SIAM J. Algebraic Discrete Methods 4 (1983), 30–41, https://doi.org/10.1137/0604005.
- V. Lucarini, *Symmetry-Break in Voronoi Tessellations*, Symmetry 1 (2009), 21–54, https://doi.org/10.3390/sym1010021 (geometry of the BCC Voronoi cell).
