# A sharp covariance-sign transition in trapezoidal rational-linear-precision prismatoids

## Finding
Let \(a,b,d>0\), \(0\le t\le1\), and
\[
T_{a,b,d}=\{(u,v):0\le v\le b,\ 0\le u\le a+d(b-v)\}.
\]
Define the standard-coordinate homothetic prismatoid
\[
P_{a,b,d;t}=\operatorname{conv}\bigl((T_{a,b,d},0),\ (tT_{a,b,d},1)\bigr)\subset\mathbb R^3.
\]
If \((X,Y,Z)\) is uniform with respect to three-dimensional volume on this body, set \(r=a/(bd)>0\). Define
\[
\rho(r)=\frac{6r^2+6r+1}{4(3r+1)(3r^2+3r+1)},\qquad
q(t)=\frac{(1-t)^2(t^4+4t^3+10t^2+4t+1)}{16(t^2+t+1)(t^4+t^3+t^2+t+1)}.
\]
Let \(r_*\) be the **unique positive** root of
\[
3r^3-4r^2-6r-1=0,\qquad r_*=2.27628825832698\ldots.
\]
Then the exact sign of the standard-coordinate mixed moment is
\[
\boxed{\operatorname{sgn}\operatorname{Cov}(X,Y)=\operatorname{sgn}(q(t)-\rho(r)).}
\]
The complete sharp phase diagram is:

1. If \(0<r<r_*\), the covariance is strictly negative for every \(0\le t\le1\).
2. If \(r=r_*\), it vanishes exactly at \(t=0\) and is negative for every \(0<t\le1\).
3. If \(r>r_*\), there is a unique \(t_*(r)\in(0,1)\), determined by \(q(t_*(r))=\rho(r)\); the covariance is positive below it, zero at it, and negative above it. Moreover \(t_*(r)\) is strictly increasing, tends to zero as \(r\downarrow r_*\), and satisfies the sharp large-aspect law
\[
\boxed{\lim_{r\to\infty}\sqrt r\,(1-t_*(r))=\sqrt2.}
\]

Thus a homothetic narrowing of the top trapezoid creates a unique *positive-to-negative coordinate covariance crossing* with no intervening combinatorial transition for \(0<t<1\). In the original integral-parameter family, \(a=12,b=4,d=1\) gives positive covariance \(33893/864360\) at \(t=1/4\), but negative covariance \(-4579/24010\) at \(t=1/2\); in both cases top and bottom are genuine trapezoids with integer parameters.

## Assumptions and scope
The coordinates are the distinguished trapezoid coordinates of the source construction; no invariance under arbitrary affine changes of coordinate is asserted. The body has height one. The range \(0<t<1\) comprises full-dimensional eight-vertex, six-facet frusta, with the same combinatorial type; \(t=0\) is the limiting trapezoidal pyramid and \(t=1\) is the prism. All statements concern **uniform Euclidean volume** inside the body, not the uniform vertex or surface-area distributions. Positive \(a,b,d\) makes the base a genuine nonrectangular trapezoid. The real-parameter geometric family extends the integer-lattice subfamily obtained by restricting \(a,b,d\) and \(ta,tb\) to integers. The lead source has primary MSC2020 52B20 and was first publicly released on 2021-09-16.

## Proof
**1. Exact independent-slice representation.** At height \(z\in[0,1]\), the section is \(s(z)T_{a,b,d}\) where \(s(z)=1-(1-t)z\). Its area is \(s(z)^2\operatorname{area}(T_{a,b,d})\). For \(t<1\), let \(S=s(Z)\). Then \(S\) has density \(3s^2/(1-t^3)\) on \([t,1]\), and \((X,Y)\) has exactly the distribution of \(S(U,V)\) with \(S\) independent of a uniform \((U,V)\in T_{a,b,d}\). At \(t=1\), \(S=1\) almost surely. For integers \(j\ge0\),
\[
\mathbb E[S^j]=\frac{3(1-t^{j+3})}{(j+3)(1-t^3)}\quad(t<1).
\]

**2. Base trapezoid's exact cross-moment.** Write \(w(v)=a+d(b-v)\). The area is \(b(2a+bd)/2\). Direct integration over \(0\le v\le b\), \(0\le u\le w(v)\) yields
\[
\mu_U=\frac{3a^2+3abd+b^2d^2}{3(2a+bd)},\quad
\mu_V=\frac{b(3a+bd)}{3(2a+bd)},
\]
\[
\operatorname{Cov}(U,V)=-\frac{b^2d(6a^2+6abd+b^2d^2)}{36(2a+bd)^2}<0.
\]
Consequently \(-\operatorname{Cov}(U,V)/(\mu_U\mu_V)=\rho(r)\).

**3. The two competing sources of covariance.** Independence and conditioning give
\[
\begin{aligned}
\operatorname{Cov}(X,Y)
&=\mathbb E[S^2]\operatorname{Cov}(U,V)
   +\operatorname{Var}(S)\mu_U\mu_V\\
&=\mathbb E[S^2]\mu_U\mu_V\left(\frac{\operatorname{Var}(S)}{\mathbb E[S^2]}-\rho(r)\right).
\end{aligned}
\]
The prefactor is positive. Substitution of the two slice moments and polynomial cancellation gives precisely \(q(t)\). In particular \(q(0)=1/16\), \(q(1)=0\), and
\[
q'(t)=\frac{15t^2(t-1)(t+1)(t^2+1)(3t^2+4t+3)}{16(t^2+t+1)^2(t^4+t^3+t^2+t+1)^2}<0
\qquad(0<t<1).
\]
This proves the exact sign identity and uniqueness of a taper crossing whenever \(0<\rho(r)<1/16\).

**4. The unique aspect threshold and its asymptotics.** Direct subtraction yields
\[
\frac1{16}-\rho(r)=\frac{3(3r^3-4r^2-6r-1)}{16(3r+1)(3r^2+3r+1)}.
\]
The cubic has exactly one positive zero (one sign change and opposite endpoint signs). Moreover
\[
\rho'(r)=-\frac{3r(18r^3+36r^2+21r+4)}{4(3r+1)^2(3r^2+3r+1)^2}<0.
\]
Thus \(\rho(r)\) decreases strictly, and so the unique solution of \(q(t_*)=\rho(r)\) increases strictly with \(r>r_*\). Finally
\[
\rho(r)=\frac1{6r}+O(r^{-2}),\qquad
q(t)=\frac{(1-t)^2}{12}+O((1-t)^3)\quad(t\uparrow1).
\]
The equality \(q(t_*)=\rho(r)\) forces \(t_*\uparrow1\) and yields the asserted \(\sqrt2\) limit. At \(t=1\), the covariance equals the strictly negative base covariance, proving the boundary case.

## Verification
Run `python3 verify.py` (requires `sympy`, `numpy`, `scipy`). It symbolically recomputes all trapezoid integrals, the taper ratio, the derivative factorization, and the aspect cubic. Independently, it triangulates the entire three-dimensional convex hull, integrates first and mixed second moments exactly over its tetrahedra using rational arithmetic, and compares with the formula for 96 choices of integer trapezoid parameters and rational tapers, including the pyramid and prism endpoints. These finite checks support reproducibility but do not replace the all-parameter symbolic proof.

## Relationship to prior work
Davies, Duarte, Portakal and Sorea introduce the trapezoidal six-facet prismatoids and establish rational linear precision via Horn pairs. Their Section 3.2 studies the face structure, facet-distance functions and algebraic-statistical parametrization; it supplies the distinguished coordinates but no uniform-volume covariance sign law. Earlier geometric investigations of the same prismatoids determine Euclidean inballs and contact facets, not volume cross-moments. Results on homothetic frusta involving Santaló products, reflected mixed volumes, and random directional mean width concern other functionals; their inspected full statements do not imply the sign classification here. Standard conditional-covariance identities are used as ingredients, not claimed as new. The contribution is the exact aspect threshold, single-crossing phase classification, and asymptotic taper law on this canonical nonrectangular family.

## Limitations
This theorem treats a homothetic subfamily, not arbitrary pairs of trapezoidal top and bottom faces. It does not determine the full covariance spectrum or the affine-invariant isotropic constant. Coordinate covariance is not invariant under rotations or shears. The strict crossing is asserted only in the stated canonical coordinates, under uniform interior-volume sampling. Previously unindexed or differently formulated moment results could affect historical priority; no independent audit has been performed.

## References
1. I. Davies, E. Duarte, I. Portakal and M.-Ş. Sorea, *Families of polytopes with rational linear precision in higher dimensions*, arXiv:2109.08151v1, first posted 2021-09-16; Section 3.2 and Figure 2, https://arxiv.org/abs/2109.08151 .
2. *Three barriers determine the Euclidean inradius of rational-linear-precision prismatoids*, published mathematical finding (2026), concerning the inscribed-ball problem in the same six-facet model.
3. *Taper-response tomography for homothetic convex frusta*, published mathematical finding (2026), concerning the distribution of random-direction widths under tapering.
