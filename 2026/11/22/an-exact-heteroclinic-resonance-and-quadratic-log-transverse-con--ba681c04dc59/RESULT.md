# An exact heteroclinic resonance and quadratic-log transverse contraction in a Leslie–Gower map

## Finding

Consider the partially saturated two-species Leslie–Gower map
\[
T_p(x,y)=\left(\frac{p x}{a+x+c y},\frac{B y}{d x+y}\right)
\]
for strictly positive \(a,B,c,d,p\), on the strictly positive quadrant. Assume \(cd>1\) and \(p>a\), so the two axial equilibria are \(E_x=(p-a,0)\) and \(E_y=(0,B)\). Set
\[
D=B(cd-1)+ad,\qquad X=\frac{aB}{D},\qquad
\lambda=\frac{ad}{D}\in(0,1),\qquad
\kappa=\frac{ad}{B(a+cB)}.
\]
**Theorem.** The straight segment joining \(E_x\) to \(E_y\) is invariant if and only if
\[
p=a+X=a+\frac{aB}{B(cd-1)+ad}.
\]
At this unique positive parameter resonance the segment
\[
S=\left\{(x,y):x/X+y/B=1,\quad 0\le x\le X\right\}
\]
is an exact heteroclinic connection from \(E_x=(X,0)\) to \(E_y=(0,B)\). Each interior orbit has the explicit two-sided formula
\[
x_n=\frac{X}{1+(X/x_0-1)\lambda^{-n}},\qquad
 y_n=B(1-x_n/X),\qquad n\in\mathbb Z.
\]
Moreover every initial point \((x_0,y_0)\in(0,\infty)^2\), including points off \(S\), converges to \(E_y\), and has a finite, strictly positive axial amplitude
\[
A=\lim_{n\to\infty}\frac{x_n}{\lambda^n}\in(0,\infty).
\]
Write \(H_n=x_n/X+y_n/B-1\). For every initial point **off** \(S\), there is a finite nonzero signed constant \(C_H\) such that
\[
H_n=C_H(\kappa A)^n\lambda^{n(n-1)/2}(1+o(1)),
\qquad n\to\infty.
\]
In particular the exact universal quadratic-logarithmic contraction exponent is
\[
\boxed{\lim_{n\to\infty}\frac{\log|H_n|}{n^2}
=\frac12\log\lambda<0.}
\]
For all sufficiently large \(n\), the orthogonal projection of \((x_n,y_n)\) onto the supporting affine line of \(S\) belongs to \(S\). Thus the same limit holds with \(\log\operatorname{dist}(T_p^n(x_0,y_0),S)\) in place of \(\log|H_n|\), whereas the population coordinate \(x_n\) decreases only geometrically at rate \(\lambda\). On \(S\) the defect and distance are identically zero, so their logarithms are not asserted there.

## Assumptions and scope

The conclusion concerns arbitrary fixed real positive \(a,B,c,d\) with \(cd>1\) and the unique corresponding resonant \(p\), with all strictly positive initial conditions. The map extends continuously to the two stated axial equilibria, but not to the origin. The exact segment orbit is defined for all integer \(n\) in the open segment. No rate is claimed for nonresonant parameters, where the segment fails to be invariant. The discrete-time convergence is measured in iterations, not interpolated physical time.

## Proof

**1. Necessity of the resonance.** If the segment connecting \((p-a,0)\) and \((0,B)\) is forward invariant, its tangent at \(E_y\) is \(v=(1,-B/(p-a))\). The Jacobian at \(E_y\) is
\[
DT_p(E_y)=\begin{pmatrix}p/(a+cB)&0\\-d&0\end{pmatrix}.
\]
Since the segment is preserved and the first coordinate derivative is strictly positive, the tangent must be an eigenvector with eigenvalue \(p/(a+cB)\). Therefore
\[
d(p-a)(a+cB)=Bp.
\]
Equivalently, \((p-a)[ad+B(cd-1)]=aB\); this uniquely forces \(p=a+X\). There is no other straight segment between these two equilibria.

**2. Exact invariant polynomial and the heteroclinic parametrization.** At this resonance put \(U=a+x+cy\), \(V=dx+y\), \(H=x/X+y/B-1\). Direct expansion using \(p/X=1+a/X\) and \(a/X=cd-1+ad/B\) gives the exact identity
\[
H(T_p(x,y))=\frac{ad x}{UV}\,H(x,y).
\]
Both denominators are positive throughout the positive quadrant. Hence \(H=0\) is invariant, and its nonnegative segment maps into itself. On this segment the first-coordinate equation is a fractional linear map with fixed points \(0,X\), and direct algebra gives
\[
\frac{1}{x_{n+1}}-\frac1X
=\lambda^{-1}\left(\frac1{x_n}-\frac1X\right).
\]
Iteration in both time directions yields the displayed formula. Because \(0<\lambda<1\), its backward and forward limits are respectively \(E_x\) and \(E_y\), establishing the heteroclinic orbit.

**3. Global attraction and the positive axial amplitude.** At the resonance,
\[
\frac{p}{a+cB}=\lambda<1,
\qquad
\frac{B}{dX}=\lambda^{-1}>1.
\]
Thus the hypotheses of McArdle (2017, Manuscript 2), Theorem 6(b), also published in Kulenović–McArdle (2019), hold in the branch where \(E_y\) attracts the full strictly positive quadrant. That global convergence is a **previously established result**, used here rather than newly reproved. Their Lemma 4(b), or the displayed Jacobian, gives eigenvalues \(0,\lambda\) at \(E_y\). Smooth local contraction implies that for any fixed \(\theta\in(\lambda,1)\), the converging orbit satisfies \(|x_n|+|y_n-B|=O(\theta^n)\). (Choose an equivalent norm with derivative norm below \(\theta\), then apply a local contraction estimate after the orbit enters that neighborhood.) Since \(x_n>0\) for every finite \(n\),
\[
\frac{x_{n+1}/\lambda^{n+1}}{x_n/\lambda^n}
=\frac{a+cB}{a+x_n+cy_n}=1+O(\theta^n).
\]
The infinite product of these strictly positive factors converges to a strictly positive finite number. Hence \(x_n=A\lambda^n(1+O(\theta^n))\) for some \(A>0\).

**4. Exact transverse product and sharp logarithmic exponent.** Define \(K_n=ad x_n/[(a+x_n+cy_n)(dx_n+y_n)]\). The exact identity from Step 2 gives \(H_{n+1}=K_nH_n\). Since \(x_n=A\lambda^n(1+O(\theta^n))\), and \(y_n=B+O(\theta^n)\),
\[
K_n=\kappa A\lambda^n(1+O(\theta^n)).
\]
For \(H_0\ne0\), all \(H_n\ne0\), and the convergent nonzero infinite product
\[
C_H=H_0\prod_{j=0}^{\infty}\frac{K_j}{\kappa A\lambda^j}
\]
is well-defined. Multiplying \(H_{n+1}=K_nH_n\) yields
\[
\log|H_n|=\frac{n(n-1)}2\log\lambda
+n\log(\kappa A)+\log|C_H|+o(1).
\]
This proves the stated sharp universal quadratic-log exponent and the full asymptotic equivalence. The Euclidean distance to the *supporting line* is \(|H_n|/(X^{-2}+B^{-2})^{1/2}\). Since \(H_n=o(x_n)\) and \(x_n\to0\) with \(x_n>0\), the orthogonal projection onto that line has first coordinate \(x_n+O(H_n)=x_n(1+o(1))\in(0,X)\) for all sufficiently large \(n\). It therefore lies on the segment \(S\), proving the final distance statement.

## Verification

The accompanying standalone standard-library Python program `CHECK.py` checks the defining parameter identities over several exact rational families; it verifies the cofactor equality, invariant-segment formula, converse tangent criterion and sign-preservation with rational arithmetic. It also numerically tracks the accumulated logarithmic defect for an explicitly given positive orbit to test the predicted quadratic-log limit without subtracting nearly equal floating-point populations. The printed success marker is `LESLIE_HETEROCLINIC_CHECK_OK` when the tests pass. The all-parameter proof is the algebra and contraction argument above; finite tests are diagnostics, not a substitute.

One exactly rational example is \((a,B,c,d)=(1,3,2,2)\), with \(D=11\), \(X=3/11\), \(p=14/11\), \(\lambda=2/11\), and \(\kappa=2/21\).

## Relationship to prior work

McArdle (2017), Manuscript 2, Section 2.4 and Theorem 6(b), reprinted in Kulenović and McArdle (2019), Section 4 and Theorem 6(b), establish global attraction to the axial equilibrium for a **strictly larger parameter region** and derive the axial eigenvalues in Lemma 4; those results are used and not claimed as new. Their explicit solution for system (4) and invariant rays belong to a different, homogeneous model. They state in their Section 4/conclusion that they had no explicit full solution for system (5). The present statement identifies a sharp, nonhomogeneous heteroclinic-line resonance, provides its complete orbit parametrization, and quantitatively characterizes the transverse approach of *every* positive orbit at that resonance.

Kalabušić, Kulenović and Pilav (2011) analyze a related **but algebraically different** rational competitive map with additive input in the first numerator and no first-coordinate self-density in that denominator. Its global manifold formulas do not imply this particular segment identity, resonance, or \(n^2\)-scale defect law. Yeganeh and Baigent (2024) study carrying simplices for a fully saturated Leslie–Gower model with positive baseline terms in **both** denominators, so their invariant-boundary results do not directly cover the partially saturated map or its nonstationary segment. Other published work on critical rates in Ricker or modified Leslie–Gower maps provides analogies, not a reduction or the same conclusion for the present map.

## Limitations

The earlier dissertation/global-basin theorem (publicly archived in 2017 and published in 2019) is essential to the global component. The new exact solution is only for the invariant segment, **not** for arbitrary points in the full plane. The quadratic-log exponent concerns approach to that segment at a special parameter resonance and is not a convergence rate for the Euclidean distance to the endpoint equilibrium. While the primary full text and close literature were compared, an unindexed equivalent formula cannot be categorically ruled out. No independent mathematical audit has been performed.

## References

1. D. T. McArdle, *Global Dynamics and Boundedness of Discrete Population Models*, 2017 University of Rhode Island open-access dissertation, Manuscript 2, first publicly downloadable by April 26, 2017 according to the URI repository. https://digitalcommons.uri.edu/oa_diss/593/ (Manuscript 2 full text also at https://david-mcardle-scholar.media.uconn.edu/wp-content/uploads/sites/3525/2022/05/PhD_Thesis__McArdle__2017-1.pdf).
2. M. R. S. Kulenović and D. T. McArdle, "Global Dynamics of Leslie-Gower Competitive Systems in the Plane," *Mathematics* 7 (2019), article 76, first published January 12, 2019. https://doi.org/10.3390/math7010076. Full text: https://www.mdpi.com/2227-7390/7/1/76.
3. S. Kalabušić, M. R. S. Kulenović and E. Pilav, "Dynamics of a two-dimensional system of rational difference equations of Leslie–Gower type," *Advances in Difference Equations* 2011, article 29 (2011), https://doi.org/10.1186/1687-1847-2011-29.
4. H. N. Yeganeh and S. Baigent, "Convexity of non-compact carrying simplices in logarithmic coordinates," *Journal of Difference Equations and Applications* 30 (2024), 1671–1691. https://doi.org/10.1080/10236198.2024.2369215.
5. AMS, *Mathematics Subject Classification 2020*, entry 37C29 (homoclinic and heteroclinic orbits for dynamical systems), https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=37C25.
