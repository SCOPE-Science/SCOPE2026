# Quartic Bernstein circle covariance preservation: exactly two distinct sampling grids

## Finding
Let \(0=\theta_0<\theta_1<\theta_2<\theta_3<\theta_4=\pi\) be five **distinct**, ordered sampling sites. On the geodesic interval of the unit circle define the degree-four Bernstein sampling operator
\[
(T_{\boldsymbol\theta}f)(\pi u)=\sum_{j=0}^4\binom4j u^j(1-u)^{4-j}f(\theta_j),\qquad 0\le u\le1.
\]
The operator maps **every** continuous positive-definite isotropic circle kernel to another positive-definite isotropic circle kernel if and only if the sampling grid is one of precisely two grids:
\[
\boxed{(\theta_0,\ldots,\theta_4)\in\left\{
(0,\pi/4,\pi/2,3\pi/4,\pi),
(0,\pi/3,\pi/2,2\pi/3,\pi)
\right\}.}
\]
Thus the uniform quartic grid is not unique, but all other distinct node configurations fail cone preservation. The classification is for the **entire** positive-definite cone, not only for a selected test covariance.

## Assumptions and scope
A real continuous \(f:[0,\pi]\to\mathbb R\) is positive definite if \((x,y)\mapsto f(d_{\mathbb S^1}(x,y))\) is positive semidefinite on all finite configurations of circle points. Equivalently its even \(2\pi\)-periodic extension has an absolutely uniformly convergent cosine series
\[
f(t)=b_0/2+\sum_{m\ge1}b_m\cos(mt),\qquad b_m\ge0,\quad \sum_{m\ge0}b_m<\infty.
\]
The nodes are strictly increasing and include the fixed endpoints. No shape or smoothness assumptions beyond continuity and positive definiteness are imposed on the input. Positive definiteness is semidefiniteness, not strict definiteness.

For any real polynomial \(P\) of degree at most four, write
\[
C_k(P)=2\int_0^1P(u)\cos(k\pi u)\,du,\qquad k\ge0.
\]
By integrating each Bernstein basis polynomial, \(C_0(P)=\frac25\sum_{j=0}^4s_j\) for a quartic Bernstein polynomial with node values \(s_j\). Repeated integration by parts gives, for \(k\ge1\),
\[
C_k(P)=\frac{2\big((-1)^kP'(1)-P'(0)\big)}{(\pi k)^2}
-\frac{2\big((-1)^kP^{(3)}(1)-P^{(3)}(0)\big)}{(\pi k)^4}.
\tag{1}
\]
The summability \(C_k(P)=O(k^{-2})\) makes the coefficient positivity criterion exact for each output polynomial.

## Proof
**1. Every admissible grid is reflection symmetric.** For each odd input frequency \(m=2r+1\), the samples at the endpoints are \(1,-1\). The zeroth cosine coefficient of the output is consequently
\[
C_0\big(T_{\boldsymbol\theta}\cos((2r+1)\,\cdot)\big)
=\frac25F(r),\qquad
F(r)=\sum_{j=1}^3\cos((2r+1)\theta_j).
\]
Cone preservation demands \(F(r)\ge0\) for every nonnegative integer \(r\). Since all three interior angles are strictly between zero and \(\pi\), the Cesàro mean of each sequence \(\cos((2r+1)\theta_j)\) is zero, so the Cesàro mean of \(F\) is zero. Moreover \(0\le F(r)\le3\), whence \(0\le F(r)^2\le3F(r)\); the mean of \(F^2\) is also zero.

To rigorously pass from zero mean square to pointwise vanishing, express \(F(r)\) as a *finite* sum \(\sum_{\lambda}a_\lambda\lambda^r\) over distinct unit-modulus frequencies \(\lambda\), after collecting any repeated frequencies. Orthogonality of exponentials in Cesàro mean yields
\[
\lim_{R\to\infty}\frac1R\sum_{r=0}^{R-1}|F(r)|^2=\sum_\lambda|a_\lambda|^2.
\]
All these coefficients vanish, so \(F(r)=0\) for every \(r\). In particular \(F(0)=F(1)=0\). With \(x_j=\cos\theta_j\), the identities \(\sum_jx_j=0\) and \(\sum_j(4x_j^3-3x_j)=0\) give \(\sum_jx_j^3=0\). The identity \(\sum_jx_j^3=3x_1x_2x_3\) when \(\sum_jx_j=0\) forces one \(x_j=0\). Since \(x_1>x_2>x_3\) and the other two sum to zero, the zero is the middle value. Consequently
\[
\theta_2=\pi/2,\qquad \theta_3=\pi-\theta_1.
\]
Write \(a=\theta_1\), with \(0<a<\pi/2\).

**2. Even-frequency mean forces a finite cyclic orbit.** For the symmetric grid \((0,a,\pi/2,\pi-a,\pi)\) and each \(m=4r+2\), the five samples of \(\cos(mt)\) equal \((1,c,-1,c,1)\), where \(c=\cos((4r+2)a)\). Their zeroth coefficient is \(\frac25(1+2c)\). Hence the necessary condition is
\[
\cos((2r+1)\,2a)\ge-\frac12\qquad\text{for every }r\ge0.\tag{2}
\]
Let \(z=e^{2ia}\). If \(z\) has infinite order, its odd positive powers are dense on the unit circle, contradicting (2). Suppose \(z\) has finite order \(L\). If \(L\) is odd, its odd powers exhaust the roots of unity of order \(L\); their smallest real part is \(-\cos(\pi/L)\), below \(-1/2\) for all odd \(L\ge5\). Order one is excluded because \(0<2a<\pi\). If \(L\equiv2\pmod4\), one odd power equals \(-1\), again impossible. If \(4\mid L\) and \(L\ge8\), the odd power with exponent \(L/2-1\) has real part \(-\cos(2\pi/L)<-1/2\). Thus necessarily \(L\in\{3,4\}\). As \(0<2a<\pi\), order three gives \(a=\pi/3\), and order four gives \(a=\pi/4\). This proves necessity.

**3. Both surviving grids preserve every cosine generator.** Fix either \(a=\pi/4\) or \(a=\pi/3\). For odd \(m\), put \(c=\cos(ma)\). The node samples are \((1,c,0,-c,-1)\). Their Bernstein polynomial is antisymmetric about \(u=1/2\); hence its zeroth and positive even cosine coefficients vanish. Formula (1) gives, for every odd \(k\ge1\),
\[
C_k=\frac{16}{(\pi k)^4}\left[(1-c)(\pi k)^2-6+12c\right].\tag{3}
\]
For \(k=1\) the bracket increases in \(c\in[-1,1]\); its minimum is \(2\pi^2-18>0\). For odd \(k\ge3\), it decreases in \(c\), with minimum \(6>0\). Hence (3) is positive.

For even \(m\), set \(c=\cos(ma)\), \(d=\cos(m\pi/2)\in\{-1,1\}\). The samples are \((1,c,d,c,1)\), so all odd cosine coefficients vanish and
\[
C_0=\frac25(2+2c+d),\qquad
C_k=\frac{16}{(\pi k)^4}\left[(1-c)(\pi k)^2+24c-18d-6\right]\quad(k\ge2\text{ even}).\tag{4}
\]
For even \(k\ge2\), \((\pi k)^2>24\), so the bracket in (4) is minimized at \(c=1\), where it equals \(18(1-d)\ge0\). To check \(C_0\), note that when \(m\equiv0\pmod4\), \(d=1\) gives \(C_0\ge0\). When \(m\equiv2\pmod4\), \(d=-1\) and the remaining condition is (2), which holds for either chosen \(a\): the odd powers of \(e^{2ia}\) have real parts in \(\{0\}\) for order four and in \(\{1,-1/2\}\) for order three. The constant input \(m=0\) is fixed by the operator.

Therefore all cosine coefficients of every sampled cosine generator are nonnegative. Since the operator has norm at most one in the uniform norm (its weights are nonnegative and sum to one), it sends uniformly convergent nonnegative cosine mixtures to the corresponding uniformly convergent mixtures of output polynomials. Termwise integration preserves coefficient nonnegativity; the output polynomial has summable cosine coefficients. The Fourier characterization proves positive definiteness for every positive-definite input. This completes sufficiency and the theorem.

## Verification
Run `python3 CHECK.py` using Python 3 and SymPy. The checker reconstructs both quartic Bernstein polynomials from their five node values and verifies the exact endpoint-derivative and mean identities used in (1), (3), and (4). It also checks roots of unity for finite orders up to 300 and 15,000 finite input/output frequency cases at the two classified grids. Executed results: `symbolic_coefficients_verified`, `root_of_unity_orders_checked`, `finite_mode_pairs_checked 15000`. Finite cases are supplementary; the density, harmonic-mean, coefficient inequalities and root-order argument in the proof cover infinitely many frequencies.

## Relationship to prior work
Otten, Nguyen and Watts [1] establish preservation for the *uniform* Bernstein grid in every degree; their full paper fixes the nodes at \(j\pi/n\) throughout. The present classification is for all strictly ordered quartic grids, and finds exactly one additional nonuniform survivor. A published classification [2] determines all endpoint-fixed grids in degrees two and three, with a one-parameter family at degree three, but explicitly does not classify degree four or higher. Checking a single generator \(f(t)=\cos t\) does not imply simultaneous preservation for *every* positive-definite kernel: the arithmetic restrictions here arise from arbitrarily high even input frequencies. No global publication-priority claim is made.

## Limitations
The claim concerns only degree four, strictly increasing nodes, fixed endpoints and the ordinary Bernstein polynomial basis. Degenerate repeated-node grids, higher degrees, other approximation bases, higher-dimensional spheres, and preservation of *strict* positive definiteness are not classified. The literature comparisons may miss older differently indexed results; no independent mathematical audit has been performed.

## References
[1] M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836, first public 2026-08-05, https://arxiv.org/abs/2608.04836 (public full text: https://www.researchgate.net/publication/411739385_Preservation_of_Positive-Definiteness_by_Bernstein_Operators_on_the_Circle).

[2] *Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle*, publicly accessible theorem and proof, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-quadratic-rigidity-and-cubic-node-freedom-for-positive-definite--b87f6c90a4aa/RESULT.md.

[3] J. M. Aldaz, O. Kounchev, H. Render, *Shape Preserving Properties of Generalized Bernstein Operators on Extended Chebyshev Spaces*, arXiv:0805.1614 (2008), https://arxiv.org/abs/0805.1614 (different reproduction and shape-preservation setting).
