# The fifth short-chord coefficient detects curvature oscillation on convex ovals

## Finding
For two independent uniformly arclength-distributed points \(X,Y\) on a smooth, strictly convex closed plane curve, the small Euclidean separation probability through order five is
\[
\Pr(\|X-Y\|\le r)=\frac{2r}{L}+\frac{r^3}{12L^2}\int_0^L\kappa^2\,ds+\frac{r^5}{L^2}\left(\frac3{320}\int_0^L\kappa^4\,ds-\frac1{360}\int_0^L(\kappa')^2\,ds\right)+O_\Gamma(r^7).
\]
The fifth coefficient combines fourth curvature energy and a **negative curvature-gradient energy**. In particular, it is unbounded below for strictly convex ovals of fixed perimeter, fixed upper and lower curvature bounds, and identical cubic coefficients.

## Assumptions and scope
The curve \(\Gamma=\gamma(\mathbb R/L\mathbb Z)\subset\mathbb R^2\) is \(C^\infty\), simple, closed, positively oriented, unit-speed, and has strictly positive signed curvature \(\kappa(s)\). The two samples are independent and each has normalized arclength law. All error bounds are as \(r\downarrow0\) for a **fixed curve**; no uniform error estimate over the oscillatory family is asserted. Chord distance is the ambient Euclidean distance, not intrinsic geodesic distance.

## Proof
For \(m\in\mathbb R/L\mathbb Z\) and small positive arc gap \(h\), set \(C(m,h)=\|\gamma(m+h/2)-\gamma(m-h/2)\|\). Writing \(T=\gamma'\) and \(N\) for the positive Frenet normal, the identities \(T'=\kappa N\), \(N'=-\kappa T\) yield
\[
\gamma'''=-\kappa^2T+\kappa'N,\qquad
\langle T,\gamma'''''\rangle=\kappa^4-3(\kappa')^2-4\kappa\kappa''.
\]
Taylor expansion of the *centered* secant, followed by squaring and taking the positive square root, gives uniformly in \(m\)
\[
C(m,h)=h-\frac{\kappa^2h^3}{24}+\left(\frac{\kappa^4}{1920}-\frac{(\kappa')^2}{1440}-\frac{\kappa\kappa''}{480}\right)h^5+O_\Gamma(h^7).
\]
The symmetry \(h\mapsto-h\) and smoothness supply the stated odd-order remainder. Since \(\partial_hC(m,0+)=1\), each sufficiently small \(r>0\) has a unique positive local arc gap \(H(m,r)\) with \(C(m,H)=r\). Direct substitution and coefficient comparison give
\[
H(m,r)=r+\frac{\kappa^2r^3}{24}+\left(\frac{3\kappa^4}{640}+\frac{(\kappa')^2}{1440}+\frac{\kappa\kappa''}{480}\right)r^5+O_\Gamma(r^7).
\]
Compactness and injectivity of the simple closed embedding ensure that, for all sufficiently small \(r\), only neighboring arclength parameters contribute to the event \(\|X-Y\|\le r\). With midpoint \(m=(s+t)/2\) and signed difference \(h=t-s\), the coordinate Jacobian is one, so the event has exactly the normalized measure
\[
F_\Gamma(r)=\frac{2}{L^2}\int_0^L H(m,r)\,dm.
\]
Substituting the expansion and using periodic integration by parts \(\int_0^L\kappa\kappa''\,ds=-\int_0^L(\kappa')^2\,ds\) proves the displayed formula, including the fifth coefficient and \(O_\Gamma(r^7)\) remainder.

For the counterfamily, set \(L=2\pi\), \(0<\varepsilon<1\), and for each integer \(n\ge2\), define
\[
\theta_n(s)=s+\frac{\varepsilon}{n}\sin(ns),\qquad
\gamma_n(s)=\int_0^s (\cos\theta_n(u),\sin\theta_n(u))\,du.
\]
The tangent angle increases strictly because \(\theta_n'(s)=1+\varepsilon\cos(ns)>0\). Moreover \(\theta_n(s+2\pi/n)=\theta_n(s)+2\pi/n\), so the \(n\) translated tangent increments are rotated copies and sum to zero. Hence \(\gamma_n(2\pi)=\gamma_n(0)\) and its turning number is one. An embedded smooth strictly convex oval results. Its curvature is exactly \(1+\varepsilon\cos(ns)\); thus its perimeter, pinching interval \([1-\varepsilon,1+\varepsilon]\), and squared-curvature integral \(2\pi(1+\varepsilon^2/2)\) are all independent of \(n\). Meanwhile
\[
\int_0^{2\pi}\kappa_n^4\,ds=2\pi\left(1+3\varepsilon^2+\frac{3\varepsilon^4}{8}\right),\quad
\int_0^{2\pi}(\kappa_n')^2\,ds=\pi\varepsilon^2 n^2.
\]
The fifth coefficient therefore equals
\[
c_5(n)=\frac1{2\pi}\left[\frac3{320}\left(1+3\varepsilon^2+\frac{3\varepsilon^4}{8}\right)-\frac{\varepsilon^2n^2}{720}\right],
\]
which tends to negative infinity with \(n\) and establishes the claimed separation between lower-order and fifth-order chord data.

## Verification
Run `python verify_chord.py` using Python 3 with NumPy. The verifier integrates actual secant vectors using Gauss–Legendre quadrature, inverts the chord relation independently by bisection, and integrates over midpoints for curves with harmonics \(n=2,4,12\) and a circle control. It checks 12 small-radius probabilities, the exact circle arcsine law, equal cubic coefficients, and opposite signs of fifth coefficients. Successful output begins `VERIFY_CHORD_OK`. These finite computations are checks, not proofs of the general or unbounded assertions.

## Relationship to prior work
The local intersection of an embedded manifold with an ambient Euclidean ball is a classical integral-invariant observable. Álvarez-Vizoso, Kirby and Peterson, *Integral Invariants from Covariance Analysis of Embedded Riemannian Manifolds* (2018), treat the first nontrivial curvature correction for such local volumes (not the displayed fifth global probability coefficient). Álvarez-Vizoso and collaborators, *Geometry of Curves in \(\mathbb R^n\), Singular Value Decomposition, and Hankel Determinants* (2015), study Frenet information recovered from local ball covariance, not the two-point fifth coefficient. The Four Vertex Theorem and its converse concern existence and restrictions on convex curvature functions; they do not imply the coefficient or the explicit oscillatory obstruction. The novelty claim is limited to the **specific fifth-order chord law together with its fixed-low-order unbounded-negative counterfamily**, not the already familiar cubic curvature-energy correction or the general idea of Taylor-expanding short secants.

## Limitations
No inverse theorem for full chord distributions is claimed; identical first and third coefficients do not imply identical full laws. The family has no uniform \(C^k\) bounds for \(k\ge3\), so the \(O_\Gamma(r^7)\) remainder depends on \(n\). Independent historical-priority assessment and independent validation have not been performed. Higher-order local integral-invariant expansions might yield equivalent formulas elsewhere.

## References
1. D. DeTurck, H. Gluck, D. Pomerleano, and D. S. Vick, *The Four Vertex Theorem and its Converse*, arXiv:math/0609268v1 (first publicly posted 2006-09-10), https://arxiv.org/abs/math/0609268.
2. J. Álvarez-Vizoso, R. Arn, B. Draper, M. Kirby, and C. Peterson, *Geometry of Curves in \(\mathbb R^n\), Singular Value Decomposition, and Hankel Determinants*, arXiv:1511.05008v1 (2015-11-16), https://arxiv.org/abs/1511.05008.
3. J. Álvarez-Vizoso, M. Kirby, and C. Peterson, *Integral Invariants from Covariance Analysis of Embedded Riemannian Manifolds*, arXiv:1804.10425v1 (2018-04-27), https://arxiv.org/abs/1804.10425.
