# Two sharp area-growth exponents at quartic rigid isochronous centers

## Finding
Let \(F:\mathbb R^2\to\mathbb R\) be any nonzero real homogeneous polynomial of degree three, and consider the rigid polynomial flow
\[
\dot x=-y+xF(x,y),\qquad \dot y=x+yF(x,y).
\]
For \(\theta\in\mathbb R\), set \(A(\theta)=F(\cos\theta,\sin\theta)\), \(P(\theta)=3\int_0^\theta A(s)\,ds\), and \(M=\max_\theta P(\theta)\). The function \(P\) is \(2\pi\)-periodic. For any nonzero initial point \((r\cos\theta,r\sin\theta)\), define \(K=r^{-3}+P(\theta)\).

**Theorem.** The forward solution is complete and periodic of minimal period \(2\pi\) precisely when \(K>M\); for \(K\le M\), it escapes to infinity in a finite positive amount of **original physical time**. If \(\mathcal B\) is the union of the origin and all periodic initial conditions, the area of its intersection with the Euclidean disk of radius \(R\) is exactly
\[
V_F(R)=\frac12\int_0^{2\pi}\min\left\{R^2,\bigl(M-P(\theta)\bigr)^{-2/3}\right\}\,d\theta,
\]
with the integrand interpreted as \(R^2\) when \(P(\theta)=M\).

Every global maximum \(\theta_j\) of \(P\) has a contact order \(k_j\in\{2,4\}\) and a coefficient \(c_j>0\) defined by
\[
M-P(\theta_j+u)=c_j|u|^{k_j}+O(|u|^{k_j+1}).
\]
Write \(k_* =\max_j k_j\). Then
\[
\boxed{\displaystyle
V_F(R)\sim \frac{2k_*}{2k_*-3}
\left(\sum_{j:\,k_j=k_*}c_j^{-1/k_*}\right)
R^{2-3/k_*}\quad(R\to\infty).}
\]
Thus the only possible area-growth powers are \(1/2\) and \(5/4\), both occur, and \(\mathcal B\) has **infinite** planar Lebesgue measure for every nonzero homogeneous cubic \(F\).

On the critical boundary \(K=M\), let \(t_*\) be the first future time at which the angular coordinate reaches a global maximizer \(\theta_j\). Then
\[
\boxed{r(t)\sim c_j^{-1/3}(t_*-t)^{-k_j/3}}
\qquad(t\uparrow t_*),
\]
so the critical original-time escape powers are precisely \(2/3\) and \(4/3\). The contact order in this last formula is that of the **first encountered** maximum, which need not equal \(k_*\) if there are several global maxima.

## Assumptions and scope
The coefficients of the homogeneous cubic \(F(x,y)=a x^3+b x^2y+c xy^2+d y^3\) are arbitrary real numbers, not all zero. Initial points are in \(\mathbb R^2\). The angular coordinate is unwrapped when following a trajectory. Euclidean area is ordinary two-dimensional Lebesgue measure in the uncompactified plane. The result concerns the zero-linear-part subfamily of the nonlinear function in the rigid quartic system; it does not address general inhomogeneous rigid systems. The origin is the sole equilibrium and is included in \(\mathcal B\) without changing its area.

## Proof
**1. Exact radial dynamics and the periodic/escape alternative.** Because \(F\) is homogeneous of degree three, polar coordinates for a nonzero solution obey
\[
\dot\theta=1,\qquad \dot r=r^4 A(\theta),\qquad
\frac d{dt}r^{-3}=-3A(\theta).
\]
The cubic \(F\) is odd, so \(A(\theta+\pi)=-A(\theta)\). Hence its integral over one full turn is zero and \(P\) is periodic. Integrating the radial equation gives the exact identity
\[
r(t)^{-3}=K-P(\theta_0+t),\qquad K=r_0^{-3}+P(\theta_0).
\]
As long as the right-hand side is positive, this defines a unique positive classical solution. If \(K>M\), it is uniformly positive and returns to the same radial and angular position after every full turn. Since \(\dot\theta=1\), its minimal period is \(2\pi\). If \(K\le M\), then \(K>P(\theta_0)\), because \(r_0\) is finite. Along the next full turn the continuous periodic function \(P\) reaches \(M\ge K\). It therefore first attains \(K\) at a finite positive time \(t_*\le2\pi\); as \(t\uparrow t_*\), the radial denominator decreases to zero and \(r(t)\to\infty\). The polynomial vector field is locally Lipschitz on finite points, so this is a finite-time escape, not a finite-position breakdown.

**2. Exact area.** At a fixed angle \(\theta\), the condition \(K>M\) is \(r^{-3}>M-P(\theta)\). Since the nonnegative quantity on the right is zero precisely at global maxima of \(P\), the allowed radial section extends from zero to \((M-P(\theta))^{-1/3}\), with the natural infinite convention. Integrating the area element \(r\,dr\,d\theta\) over the disk gives the stated exact formula for \(V_F(R)\).

**3. Only quadratic and quartic maxima are possible.** The restriction of a homogeneous cubic to the unit circle is a trigonometric polynomial supported on the first and third Fourier harmonics. In particular,
\[
A^{(4)}+10A''+9A=0.
\]
If a nonzero solution of this fourth-order constant-coefficient ODE had a zero of order at least four, its first four initial derivatives would vanish and uniqueness would imply \(A\equiv0\), contradicting \(F\ne0\). Thus every zero of \(A\) has multiplicity at most three. At a local maximum \(\theta_j\) of nonconstant real-analytic \(P\), the first nonzero term of \(M-P(\theta_j+u)\) has **positive even** degree \(k_j\). Since \(P'=3A\), its order minus one is the odd multiplicity of a zero of \(A\). Consequently \(k_j\) is either two or four, and the coefficient \(c_j\) is positive. There are finitely many maxima because \(P\) is a nonconstant trigonometric polynomial.

**4. Sharp area asymptotics.** Choose pairwise disjoint neighborhoods of the global maxima. Away from them \(M-P\) is bounded below by a positive constant, so that region contributes \(O(1)\) to \(V_F(R)\). Near one maximum with order \(k\), write \(\Delta(u)=M-P(\theta_j+u)=c|u|^k(1+o(1))\). Substitute \(u=R^{-3/k}v\) into that neighborhood's contribution. The normalized integrand converges to \(\frac12\min\{1,c^{-2/3}|v|^{-2k/3}\}\). Since \(2k/3>1\), two-sided power bounds on \(\Delta(u)\) provide an integrable majorant. Dominated convergence yields the contribution
\[
R^{2-3/k}\left[\frac12\int_{-\infty}^\infty
\min\{1,c^{-2/3}|v|^{-2k/3}\}\,dv+o(1)\right]
=R^{2-3/k}\left[\frac{2k}{2k-3}c^{-1/k}+o(1)\right].
\]
Summing over the finitely many maxima and keeping those with greatest \(k\) proves the formula. The exponent is positive in either case, so the periodicity basin has infinite area.

**5. Critical physical-time escape.** If \(K=M\), the first hitting angle is a global maximum \(\theta_j\). Since \(\theta(t)=\theta_0+t\) and \(P\) is smooth, the expansion in part 3 gives \(r(t)^{-3}=c_j(t_*-t)^{k_j}(1+o(1))\). Taking a cube root proves the claimed critical rate.

**6. Both phases occur with explicit coefficients.** For \(F(x,y)=-y(x^2+y^2)\), the angular cubic is \(A(\theta)=-\sin\theta\), so \(P(\theta)=3(\cos\theta-1)\) has one quadratic maximum modulo a full turn and \(M-P(\theta)\sim\frac32\theta^2\). The result specializes to
\[
V_F(R)\sim4\sqrt{\frac23}\,R^{1/2}.
\]
For \(F(x,y)=-y^3\), \(A(\theta)=-\sin^3\theta\), and
\[
M-P(\theta)=2-3\cos\theta+\cos^3\theta
=(1-\cos\theta)^2(2+\cos\theta)
\sim\frac34\theta^4.
\]
Thus this distinct quartic-contact example satisfies
\[
V_F(R)\sim\frac85\left(\frac43\right)^{1/4}R^{5/4}.
\]
The examples also realize the two critical escape powers.

## Verification
The included standalone script `verify_quartic_rigid.py` uses exact rational arithmetic to check the flattened angular-potential factorization and independently evaluates truncated basin areas by logarithmically rescaled Simpson quadrature. It also checks the leading Taylor coefficients for the two explicit examples. Run `python3 verify_quartic_rigid.py` in an ordinary Python 3 environment; the script uses only the standard library. Its numerical checks are illustrative: the all-coefficient conclusions and the sharp constants follow from the analysis above, not from finite sampling.

## Relationship to prior work
Álvarez, Bravo and Calderón [1] study the encompassing quartic rigid family and state its polar reduction (their equation (1.4)), the isochronous center criterion (their Theorem 2.1), an explicit first integral in the homogeneous cubic case, and its compactified global-center geometry (their Theorem 3.5). **Those results are prior and are not claimed as new.** The present theorem concerns the uncompactified plane and adds the exact periodic/burst alternative in original time, the measured periodicity-basin formula, the complete two-exponent and sharp-constant area classification, and original-time critical escape exponents. These statements do not follow from topological phase-portrait classification without additional metric estimates.

Itikawa and Llibre [2] classified the possible Poincaré-disc phase portraits of precisely this homogeneous quartic family. That classification covers qualitative separatrix configurations, not the Euclidean area of the periodicity basin inside a growing disk or its contact-order constants. Llibre and Valls [3] also classify homogeneous uniform-isochronous phase portraits when the angular polynomial has simple zeroes, again in a topological rather than metric framework.

## Limitations
The theorem is not a new integrability criterion, global-center classification, or phase-portrait classification. It only covers nonzero **homogeneous cubic** radial nonlinearities with unit angular velocity. It does not give subleading terms or a classification of first-contact behavior at a nonglobal local maximum, which can occur for subcritical \(K<M\). A later or unindexed derivation of the same metric asymptotics could affect publication priority. The 2021/2022 related article [3] was inspected in accessible abstract and appendix material only, not its complete subscription-restricted main body. All claims here are mathematical arguments without an independent audit.

## References
1. M. J. Álvarez, J. L. Bravo, L. A. Calderón, *Quartic rigid systems in the plane and in the Poincaré sphere*, arXiv:2310.05509 (first publicly posted 2023-10-09); *Qualitative Theory of Dynamical Systems* 23, 226 (2024), doi:10.1007/s12346-024-01083-z. Open full text: https://link.springer.com/article/10.1007/s12346-024-01083-z .
2. J. Itikawa, J. Llibre, *Global phase portraits of uniform isochronous centers with quartic homogeneous polynomial nonlinearities*, *Discrete and Continuous Dynamical Systems - B* 21 (2016), 121–131, doi:10.3934/dcdsb.2016.21.121. Open article text: https://www.researchgate.net/publication/283758449_Global_phase_portraits_of_uniform_isochronous_centers_with_quartichomogeneous_polynomial_nonlinearities .
3. J. Llibre, C. Valls, *Phase Portraits of Uniform Isochronous Centers with Homogeneous Nonlinearities*, *Journal of Dynamical and Control Systems* 28 (2022), 319–332, doi:10.1007/s10883-021-09529-2. Accessible preview and appendix: https://link.springer.com/article/10.1007/s10883-021-09529-2 .
