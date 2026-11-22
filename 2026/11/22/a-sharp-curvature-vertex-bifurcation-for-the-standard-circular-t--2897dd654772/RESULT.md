# A sharp curvature-vertex bifurcation for the standard circular trefoil

## Finding
For every real \(R>1\), consider the embedded circular-torus trefoil
\[
X_R(t)=\bigl((R+\cos3t)\cos2t,\ (R+\cos3t)\sin2t,\ \sin3t\bigr),\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
The minor radius is one, the major radius is \(R\), and the aspect ratio is \(\lambda=1/R\). Let \(\kappa_R(t)=\|X_R'(t)\times X_R''(t)\|/\|X_R'(t)\|^3\) be its nonnegative Euclidean curvature. Count *strict local extrema* of curvature, including the possible zero-curvature minimum at an inflection, whether or not curvature is differentiable there.

Define \(R_*\) as the unique real root greater than one of
\[
20R^3-156R^2-417R-484=0.
\]
Numerically \(R_*=10.1012691095328\ldots\) and \(\lambda_*=1/R_*=0.0989974615226\ldots\). There is an exact, sharp transition:

* If \(1<R<R_*\), curvature has precisely twelve strict local extrema: six maxima and six minima. The minima are at \(\cos3t=1\) (three points) and \(\cos3t=-1\) (three points); at \(R=13/4\) the latter three are strict but nondifferentiable zero-curvature minima. All six maxima have \(\cos3t=c_R\), where \(c_R\in(-1,1)\) is the unique zero of the explicit quintic \(F_R\) below.
* If \(R=R_*\), there are exactly six strict local extrema: three ordinary minima at \(\cos3t=-1\) and three quartically flat maxima at \(\cos3t=1\).
* If \(R>R_*\), there are exactly six ordinary strict extrema: three maxima at \(\cos3t=1\) and three minima at \(\cos3t=-1\).

Equivalently, increasing the minor-to-major aspect ratio through \(\lambda_*\) creates three additional curvature minima and splits each of three pre-existing maxima into a pair of maxima. The inflection threshold \(\lambda_{\mathrm{inf}}=4/13\) is different from this vertex threshold.

The transition has a sharp local scale. Let
\[
F_R(c)=80c^5-464Rc^4-(1792R^2+864)c^3-(1792R^3+5508R)c^2
 -(464R^4+5508R^2+5508)c+80R^5-864R^3-3321R,
\]
\[
P=-\frac{\partial_R F_{R_*}(1)}{\partial_c F_{R_*}(1)}>0.
\]
For \(R=R_*-\delta\) with \(\delta\downarrow0\), the six interior maxima occur in pairs around \(t_k=2\pi k/3\), \(k=0,1,2\), at
\[
t=t_k\pm\frac{\sqrt{2P}}3\sqrt{\delta}+O(\delta^{3/2}),
\qquad \frac{\sqrt{2P}}3=0.1707184632790\ldots.
\]
At \(R=R_*\), the curvature decrease away from \(t_k\) is a strictly positive multiple of \((t-t_k)^4+O((t-t_k)^6)\). This is a curvature-vertex bifurcation, not a change of knot type or an inflection creation.

## Assumptions and scope
All parameters and inequalities are real. The torus is an embedded ring torus because \(R>1\); the curve is a smooth embedded closed trefoil with nonvanishing velocity. Curvature is nonnegative; the word *extremum* refers to strict topological extrema of \(\kappa_R\) along the parameter circle. The unit minor radius fixes scale without loss of generality for curvature-extremum positions and counts. The claim concerns exactly this standard \((2,3)\) embedding, not arbitrary deformations or other torus-knot types.

## Proof
Put \(c=\cos3t\), \(s=\sin3t\), \(u=R+c\), and \(V=4u^2+9\). In the moving orthonormal cylindrical frame, the velocity and acceleration have components
\[
X_R'=(-3s,\ 2u,\ 3c),\qquad
X_R''=(-9c-4u,\ -12s,\ -9s).
\]
Consequently \(\|X_R'\|^2=V>0\), and the squared cross product is
\[
N=V\bigl((9c+4u)^2+225(1-c^2)\bigr)-144u^2(1-c^2).
\]
Thus \(\kappa_R(t)^2=K_R(c)=N/V^3\). Direct differentiation (expanding the displayed polynomials) gives the exact identity
\[
\frac{\partial K_R}{\partial c}=\frac{8F_R(c)}{V^4}.
\]
There is no hidden critical-point source: \(dc/dt=-3\sin3t\). Also \(N>0\) for \(-1<c<1\), because the radial component of \(X_R'\times X_R''\) equals \(18s(c-R)\neq0\). At \(c=\pm1\), \(N\) can vanish only when \(c=-1,R=13/4\), by the remaining cross-product components. That exceptional curvature zero is a strict minimum by \(\partial_c K_R(-1)>0\), and is allowed in the statement.

It remains to count roots of \(F_R\) on \((-1,1)\) **for every** \(R>1\), rather than merely sample parameter values. Write \(z=R-1>0\), \(y=(1+c)/(1-c)>0\). The degree-five polynomial
\[
G_z(y)=(1+y)^5F_{1+z}\left(\frac{y-1}{y+1}\right)
=\sum_{j=0}^5g_j(z)y^j
\]
has the following exact coefficients (in ascending powers of \(z\)):
\[
\begin{aligned}
g_0&=2187-405z+2916z^2+864z^4+80z^5,\\
g_1&=5751-2025z+8748z^2+3456z^3+3392z^4+400z^5,\\
g_2&=-10530-15714z+5832z^2+6656z^3+4928z^4+800z^5,\\
g_3&=-44226-52866z-20168z^2-768z^3+3072z^4+800z^5,\\
g_4&=-58617-72089z-37420z^2-7680z^3+608z^4+400z^5,\\
g_5&=-25925-33317z-17252z^2-3712z^3-64z^4+80z^5.
\end{aligned}
\]
The first two are positive for every \(z\ge0\), since their quadratic truncations have negative discriminants and all omitted terms are nonnegative. In each of \(g_2,g_3,g_4,g_5\), the coefficients in increasing powers of \(z\) change sign exactly once, from negative to positive. Descartes' rule, together with the values at zero and infinity, proves each has **exactly one** positive zero. Evaluating at rational endpoints gives mutually disjoint intervals for the zero, expressed in \(R=1+z\):
\[
\begin{array}{c|cccc}
 j&2&3&4&5\\\hline
R\text{ interval}&(2,5/2)&(3,4)&(6,7)&(10,11).
\end{array}
\]
Hence as \(R\) increases the signs of \((g_0,\ldots,g_5)\) are always a positive initial segment followed by a negative terminal segment, until \(g_5\) becomes nonnegative. Descartes' rule in \(y>0\) now gives exactly one root in \(-1<c<1\) while \(g_5<0\), and none once \(g_5\ge0\). Moreover,
\[
F_R(1)=(4R^2+8R+13)(20R^3-156R^2-417R-484),
\]
while \(F_R(-1)>0\) for \(R>1\). Therefore the unique interior root, when present, is crossed from positive to negative. The root of the cubic is unique in \((10,11)\), establishing the asserted count and the exact threshold.

For \(1<R<R_*\), the function \(K_R\) increases on \((-1,c_R)\) and decreases on \((c_R,1)\). Thus the three points with \(c=-1\) and three with \(c=1\) are minima, and the six preimages of \(c=c_R\) are maxima. For \(R>R_*\), \(K_R\) increases throughout \((-1,1)\), giving three minima at \(c=-1\) and three maxima at \(c=1\). At equality, \(F_{R_*}(1)=0\) and \(\partial_cF_{R_*}(1)<0\): the expansion \(c=1-\tfrac92(t-t_k)^2+O((t-t_k)^4)\) gives a negative fourth-order term in \(K_{R_*}(t)-K_{R_*}(t_k)\); since curvature is positive there, the curvature maximum is quartically flat.

Finally, \(\partial_R F_{R_*}(1)>0\) and \(\partial_cF_{R_*}(1)<0\). The implicit-function theorem yields \(c_{R_*-\delta}=1-P\delta+O(\delta^2)\), where \(P>0\) is defined above. Substituting \(\cos3t=c_{R_*-\delta}\) and expanding the inverse cosine proves the two-branch square-root splitting with the indicated coefficient.

## Verification
The standalone standard-library script `check_trefoil_curvature.py` checks the squared-curvature formula against the three-dimensional velocity/acceleration cross product; compares the analytic derivative with finite differences; verifies the Möbius polynomial transform at exact rational test inputs; checks all coefficient-root bracketing signs; isolates the cubic threshold; tests the root-count regimes and the local square-root coefficient; and confirms the exceptional inflection identity at \(R=13/4\). It prints `TREFOIL_CURVATURE_VERTEX_BIFURCATION_CHECKS_OK` when all assertions hold. All global root-count and asymptotic claims rest on the preceding exact sign proof and expansions, not on finite sampling.

## Relationship to prior work
Oberti and Ricca (2016) study this standard torus-knot parametrization, analyze its curvature and inflection points, and prove the distinct inflection aspect ratio \(\lambda=4/13\) for the trefoil. Their Figure 3 displays two curvature peaks for several sample aspect ratios, but the inspected Sections 2–6 do not give the exact \(\lambda_*\) at which that peak pair disappears, an all-ratio curvature-extremum count, or the square-root collision law. The present theorem fixes the geometry and studies exactly that local-vertex transition; it does not reassert their inflection theorem or total-curvature analysis.

Starostin and van der Heijden (2014) study nonlinear, contact-constrained elastic-knot equilibria and their curvature profiles. Their varying equilibrium shapes are not the fixed circular-torus trefoil family analyzed here, and their numerical ropelength bifurcations do not imply the stated cubic threshold. This result is independent of topological knot classification and is about Euclidean curvature geometry of one canonical embedding.

## Limitations
The classification is restricted to the standard \((2,3)\) circular ring-torus parametrization with unit tube radius and \(R>1\). It gives no corresponding classification for other winding numbers, noncircular tori, or elastically relaxed knots. The root-count theorem is analytic, while the numerical values are only approximations. The known earlier curvature plots reduce the historical-priority margin: the assertion of unreported exact sharpness is based on inspected accessible texts and targeted searches, not on exhaustive universal priority proof. Independent assessment has not been performed.

## References
1. C. Oberti and R. L. Ricca, *On torus knots and unknots*, Journal of Knot Theory and Its Ramifications **25** (2016), 1650036, DOI: 10.1142/S021821651650036X. Publicly published April 28, 2016. Author-accessible full text: https://www.renzoricca.com/wp-content/uploads/2022/08/63-2016-Oberti-Ricca.pdf.
2. E. L. Starostin and G. H. M. van der Heijden, *Tightening elastic (n, 2)-torus knots*, Journal of Physics: Conference Series **544** (2014), 012007, DOI: 10.1088/1742-6596/544/1/012007. Author-shared text: https://www.researchgate.net/publication/267201478_Tightening_elastic_n_2-torus_knots.
