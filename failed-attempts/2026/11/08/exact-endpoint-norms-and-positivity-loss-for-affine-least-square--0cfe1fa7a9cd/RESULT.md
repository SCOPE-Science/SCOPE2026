# Exact endpoint norms and positivity loss for affine least squares on Euclidean balls

## Finding
For every integer \(d\ge1\), let \(\mu_d\) be normalized uniform volume measure on the closed Euclidean unit ball \(B^d\subset\mathbb R^d\), and let \(P_d:L^2(\mu_d)\to\mathcal P_1\) be the orthogonal projection onto the real affine functions. Put
\[
a_d=\frac1{d+2},\qquad c_d=\frac{\Gamma(d/2+1)}{\sqrt\pi\,\Gamma((d+1)/2)},
\]
and define the unregularized incomplete beta function \(B_z(p,q)=\int_0^z t^{p-1}(1-t)^{q-1}\,dt\). The sharp positivity defect is
\[
C_d=c_d\left[\frac{d+2}{d+1}(1-a_d^2)^{(d+1)/2}-\frac12 B_{1-a_d^2}\left(\frac{d+1}{2},\frac12\right)\right].
\]
Then
\[
\boxed{\|P_d\|_{L^\infty(\mu_d)\to L^\infty(\mu_d)}=1+2C_d,\qquad \inf_{0\le f\le1}\min_{x\in B^d}(P_df)(x)=-C_d.}
\]
The first infimum is over all essentially bounded measurable real inputs satisfying the displayed bounds. Precisely the boundary sphere consists of norming evaluation locations. At any unit vector \(u\), the negative excursion is attained by \(f_u(y)=\mathbf1_{\{u\cdot y<-a_d\}}\); the operator norm is attained by \(g_u(y)=\operatorname{sgn}(1+(d+2)u\cdot y)\). These sign patterns, up to measure-zero changes, and global sign for \(g_u\), give the complete equality classifications at a fixed boundary evaluation point. Moreover
\[
\lim_{d\to\infty}\frac{\|P_d\|}{\sqrt d}=\sqrt{\frac2\pi},\qquad \lim_{d\to\infty}\frac{C_d}{\sqrt d}=\frac1{\sqrt{2\pi}}.
\]
For example, \(C_1=1/3\) and \(C_3=64/125\).

## Assumptions and scope
The domain is the full solid unit ball, not its surface; the measure is normalized Lebesgue volume. The projection acts on real functions and reproduces every affine function. It is evaluated on the closed ball using its unique continuous affine representative; since the ball has full-volume interior, the output's essential supremum is the supremum of that representative. Affine changes of variables yield the same norm and defect on any nondegenerate ellipsoid equipped with uniform volume. No constraint is imposed on input continuity; continuous bounded approximations to the sharp sign indicators recover the same sharp operator constants as suprema.

## Proof
Symmetry of uniform volume gives \(\mathbb EY=0\) and \(\mathbb E Y_iY_j=\delta_{ij}/(d+2)\). Thus the affine reproducing kernel is exactly
\[
K_d(x,y)=1+(d+2)x\cdot y,\quad (P_df)(x)=\int_{B^d}K_d(x,y)f(y)\,d\mu_d(y),\quad \int K_d(x,y)\,d\mu_d(y)=1.
\]
For fixed \(x\), the norm of evaluation is \(L(x)=\mathbb E|K_d(x,Y)|\), and the smallest projection of an input \(0\le f\le1\) is \(-\mathbb E(K_d(x,Y))_-\), where \(z_-=\max\{0,-z\}\). Because the kernel integrates to one, \(L(x)=1+2\mathbb E(K_d(x,Y))_-\). Rotational invariance makes \(L(x)=\mathbb E|1+(d+2)sY_1|\) for \(s=\|x\|\). As a function of \(s\ge0\) this is convex and nondecreasing: the average of the two absolute values at \(\pm Y_1\) is \(\max\{1,(d+2)s|Y_1|\}\). It is strictly increasing for every \(s>1/(d+2)\), since the marginal density is positive on the full interval \((-1,1)\). Hence precisely the sphere \(s=1\) maximizes evaluation. The signs of the kernel give the equality functions stated above, and the negative kernel has positive measure for every boundary point.

A slice-volume calculation gives the exact one-dimensional marginal density
\[
\mathbb P(Y_1\in dt)=c_d(1-t^2)^{(d-1)/2}\mathbf1_{[-1,1]}(t)\,dt.
\]
At \(x=u\) the negative part of \(K_d\) lies on \(Y_1<-a_d\), and reflection yields
\[
C_d=(d+2)c_d\int_{a_d}^1(t-a_d)(1-t^2)^{(d-1)/2}\,dt.
\]
The two pieces are computed by substitution:
\[
\int_{a_d}^1t(1-t^2)^{(d-1)/2}dt=\frac{(1-a_d^2)^{(d+1)/2}}{d+1},
\]
\[
\int_{a_d}^1(1-t^2)^{(d-1)/2}dt=\frac12 B_{1-a_d^2}\left(\frac{d+1}{2},\frac12\right).
\]
Using \((d+2)a_d=1\) proves the displayed exact formula, the endpoint norm, the defect, and equality classification. The cases \(d=1,3\) are direct polynomial integrations.

For the asymptotic, if \(G_1,\ldots,G_{d+2}\) are independent standard Gaussians, a coordinate of a uniform point on the sphere \(S^{d+1}\) has law \(G_1/(\sum_{j=1}^{d+2}G_j^2)^{1/2}\); its first coordinate has the same law as \(Y_1\) by the preceding beta density. The strong law gives \(\sqrt{d+2}Y_1\) converging in distribution to a standard Gaussian. In addition \(\mathbb E[(d+2)Y_1]^2=d+2\), so \((1+(d+2)Y_1)/\sqrt d\) has bounded second moments and is uniformly integrable. Thus
\[
\frac{\|P_d\|}{\sqrt d}=\mathbb E\left|\frac{1+(d+2)Y_1}{\sqrt d}\right|\longrightarrow \mathbb E|G_1|=\sqrt{2/\pi}.
\]
The defect limit follows from \(2C_d=\|P_d\|-1\). This proves every dimension claim without an experimental extrapolation.

## Verification
The standalone `verify.py` evaluates the beta expression independently against direct one-dimensional quadrature in dimensions \(1,2,3,4,5,6,8,10,15,20,30,100,1000\), checks the exactly integrable \(d=1\) value, and checks the Gaussian leading scale at several larger dimensions. It returned `BETA_INTEGRAL_AND_GAUSSIAN_SCALING_OK`. These finite tests check normalization and arithmetic; the exact equality and all-dimensional statements follow from the analytic proof above.

## Relationship to prior work
The continuous projector in this result is not hyperinterpolation. Wade's *On hyperinterpolation on the unit ball* (arXiv:1209.4328v1, first posted 2012-09-19) analyzes cubature-sampled polynomial projections; Theorem 3.1 of its accessible full text gives polynomial-degree growth estimates rather than the exact degree-one continuous endpoint norm and nonnegative-input sharp deficit considered here. The same paper provides relevant orthogonal-kernel foundations and the approximation-theory motivation.

An earlier published exact result, *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, solves the corresponding simplex problem and obtains a quantity of linear order in dimension, in contrast with the square-root growth proved here for the ball. Its reproducing-kernel and extremizing-shape methods are related, but its Dirichlet simplex-coordinate distribution is different from the ball's beta marginal; the constants do not imply one another.

The literature on orthogonal projection stability, including de Boor's spline estimates and Crouzeix–Thomée's finite-element estimates, concerns related operators but does not by its stated bounds determine the particular ball endpoint norm. A general radial-measure optimization result maximizes a related affine projection norm over *all* rotationally invariant measures of prescribed variance; such an envelope does not determine the exact norm for the fixed uniform-volume measure. These distinctions concern actual mathematical implications, not merely the wording of titles.

## Limitations
This is a degree-one and uniform-volume statement. It does not determine higher polynomial-degree projection constants, discretized hyperinterpolation constants, or projection norms for arbitrary convex bodies. The asymptotic is a leading-order result only. The beta integral is elementary once the exact kernel is identified, and an equivalent explicit norm may exist in classical multivariate orthogonal-polynomial or approximation tables not found in the sources inspected. No independent validation or priority guarantee is asserted.

## References
1. Jeremy Wade, *On hyperinterpolation on the unit ball*, arXiv:1209.4328v1, first submitted 2012-09-19, https://arxiv.org/abs/1209.4328 (full-text §2 and Theorem 3.1 inspected).
2. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 (full RESULT.md inspected).
3. Carl de Boor, *A Bound on the L-Infinity-Norm of L2-Approximation by Splines in Terms of a Global Mesh Ratio*, Mathematics of Computation 30 (1976), 765–771, DOI: 10.1090/S0025-5718-1976-0425432-1 (bibliographic comparison only).
4. Michel Crouzeix and Vidar Thomée, *The Stability in Lp and W1p of the L2-Projection onto Finite Element Function Spaces*, Mathematics of Computation 48 (1987), 521–532, DOI: 10.1090/S0025-5718-1987-0878688-2 (bibliographic comparison only).
