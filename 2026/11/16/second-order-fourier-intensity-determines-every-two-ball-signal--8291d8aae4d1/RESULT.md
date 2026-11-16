# Second-order Fourier intensity determines every two-ball signal in higher dimensions

## Finding
For a unit-density sum of two Euclidean ball indicators in every \(\mathbb R^d\), \(d\ge2\), the Fourier intensity at frequency zero and its full Hessian determine both radii and the center separation up to its unavoidable sign. Consequently they determine the complete signal up to translation and reflection. **Only a second-order Taylor jet is needed**, even when the balls overlap. No finite positive radii or center separations are excluded.

## Assumptions and scope
Fix an integer \(d\ge2\), let \(B(c,r)=\{x\in\mathbb R^d:|x-c|<r\}\), and take \(f(x)=\mathbf1_{B(c_1,r_1)}(x)+\mathbf1_{B(c_2,r_2)}(x)\), with \(r_1,r_2>0\) and arbitrary centers. This is a **sum of indicators**, rather than the indicator of a union when the balls overlap. For disjoint balls the two coincide. Use \(\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-i\xi\cdot x}\,dx\); let \(I(\xi)=|\widehat f(\xi)|^2\). Set \(\omega_d=\pi^{d/2}/\Gamma(1+d/2)\), \(V_j=\omega_dr_j^d\), and \(S=V_1+V_2\). All derivatives are ordinary real-frequency derivatives at \(\xi=0\).

Define the observed real symmetric matrix
\[\Sigma=-\frac{\nabla^2 I(0)}{2I(0)}.\]
Then the radii and displacement are reconstructed exactly as follows:
\[S=\sqrt{I(0)},\qquad a=\lambda_{\min}(\Sigma),\qquad V_1+V_2=S,\]
\[V_1^{1+2/d}+V_2^{1+2/d}=\omega_d^{2/d}S(d+2)a,\]
\[\lvert c_1-c_2\rvert=\frac{S}{\sqrt{V_1V_2}}\sqrt{\lambda_{\max}(\Sigma)-a}.\]
The two-volume equations have exactly one unordered positive solution for data arising from this model. If \(\lambda_{\max}(\Sigma)>a\), the eigenspace for the largest eigenvalue supplies the unoriented displacement direction; if equality holds, the centers coincide.

## Proof
**1. Intensity Hessian is covariance.** Write \(p(x)=f(x)/S\), a probability density, and let \(X,Y\) be independent with density \(p\). Since \(I(\xi)=S^2\mathbb E[e^{-i\xi\cdot(X-Y)}]\), dominated differentiation (compact support) gives \(I(0)=S^2\) and
\[\partial_{jk}I(0)=-S^2\mathbb E[(X_j-Y_j)(X_k-Y_k)]=-2S^2\operatorname{Cov}(X)_{jk}.\]
Thus \(\Sigma=\operatorname{Cov}(X)\). All odd-order derivatives of \(I\) at zero vanish because \(I(-\xi)=I(\xi)\).

**2. Exact rank-one covariance decomposition.** Conditional on choosing ball \(j\), the point is uniformly distributed on that ball, with mean \(c_j\) and covariance \(r_j^2I_d/(d+2)\). The mixing weights are \(V_j/S\). The law of total covariance yields
\[\Sigma=aI_d+\frac{V_1V_2}{S^2}vv^T,\qquad v=c_1-c_2,\quad a=\frac{V_1r_1^2+V_2r_2^2}{S(d+2)}.\]
Because \(d\ge2\), the rank-one positive-semidefinite correction has a zero eigenvalue in a transverse direction, so \(a\) is precisely the smallest eigenvalue; the unique nontrivial eigenvalue difference is \(\Delta=V_1V_2|v|^2/S^2\). Its top eigendirection is \(\mathbb Rv\) when \(v\ne0\). These statements include coincident centers by setting \(\Delta=0\).

**3. Unique recovery of both radii.** Define \(q=1+2/d>1\) and \(M=S\). Since \(r_j^d=V_j/\omega_d\), the displayed formula for \(a\) gives
\[V_1^q+V_2^q=\omega_d^{2/d}S(d+2)a.\]
On the fixed-sum segment \(V_1+V_2=M\), the function \(t\mapsto t^q+(M-t)^q\) is strictly decreasing on \((0,M/2)\), strictly increasing on \((M/2,M)\), and invariant under \(t\mapsto M-t\): its derivative is \(q(t^{q-1}-(M-t)^{q-1})\). Hence any admissible value gives exactly one unordered pair \(\{V_1,V_2\}\). The radii follow as \(r_j=(V_j/\omega_d)^{1/d}\).

**4. Unique geometry modulo Fourier symmetries.** Given the radii, the spectral gap \(\Delta\) fixes \(|v|\), and the top eigenspace fixes \(v\) up to sign. A common translation fixes one center; changing the sign of \(v\) is realized by a central reflection. If the two recovered radii are interchanged relative to a fixed pair of center positions, reflecting about their midpoint exchanges the positions. Thus all remaining choices represent the same signal modulo translation and reflection.

**5. Sharp jet order.** Since \(I\) is even, every first derivative at zero vanishes. The value \(I(0)=\omega_d^2(r_1^d+r_2^d)^2\) has infinitely many different positive unordered-radius representations; choose their centers sufficiently far apart if disjoint balls are required. Neither an order-zero nor an order-one jet therefore suffices on this class, whereas the full order-two jet does.

## Verification
The covariance identity follows from differentiation under a compactly supported double integral, not from a finite experiment. As a check in dimension two, radii \(1\) and \(2\) and center separation \(5\) give \(S=5\pi\), \(a=17/20\), and covariance eigenvalues \(17/20\) and \(97/20\). The inversion equations recover volumes \(\pi,4\pi\) and separation \(5\) exactly. All boundary cases \(r_1=r_2\), \(c_1=c_2\), touching balls and overlapping sums are covered by the proof.

## Relationship to prior work
Xia and Xu's *Fourier Phase Retrieval for Finite Unions of Intervals* (first posted 2026-06-18) studies one-dimensional union-of-interval indicators and their full Fourier magnitudes. The present statement is higher-dimensional, restricted to two Euclidean balls, but needs only the intensity's zero-frequency second jet. The general survey by Grohs, Koppensteiner and Rathmair discusses Fourier phase-retrieval uniqueness; it does not, in the accessible abstract, assert this reconstruction. Covariogram literature on nonconvex sets concerns reconstruction from complete autocorrelation, not this second-jet criterion. A published exact finite-jet theorem for two intervals is one-dimensional and requires a fourth-order jet; it does not imply the anisotropic higher-dimensional result.

## Limitations
The two components must be full Euclidean balls with known common unit density; freely weighted balls, general ellipsoids, three or more balls and unknown background are outside this result. Exact derivatives are assumed; stability and noise amplification are not established. Only translations and central reflection are declared unobservable. The historical literature comparison is provisional: a plausible full June 2026 manuscript and older geometric inverse-scattering works could not be read in full, so publication priority remains subject to deeper primary-source review.

## References
1. Y. Xia and Z. Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first posted 2026-06-18, https://arxiv.org/abs/2606.19855 .
2. P. Grohs, S. Koppensteiner, M. Rathmair, *Phase Retrieval: Uniqueness and Stability*, SIAM Review 62 (2020), 301–350, https://doi.org/10.1137/19M1256865 .
3. C. Benassi, G. Bianchi, G. D'Ercole, *Covariogram of Non-Convex Sets*, Mathematika 56 (2010), 267–284, https://doi.org/10.1112/S0025579310000549 .
4. A. Charalambopoulos, G. Dassios, M. Hadjinicolaou, *An Analytic Solution for Low-Frequency Scattering by Two Soft Spheres*, SIAM J. Appl. Math. 58 (1998), 370–386, https://doi.org/10.1137/S0036139996304081 (a physically different boundary-scattering problem).
