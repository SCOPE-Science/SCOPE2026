# Four-observable global reconstruction and sharp logarithmic conditioning in a quadratic switching center

## Finding

For Tang's normalized piecewise quadratic global-center family, the two half-orbit enclosed Euclidean areas and two original-time residence durations measured on **one** periodic orbit determine all three positive coefficients and the crossing amplitude. Every positive quadruple of observations is realizable exactly once. The inverse has a sharp global multiplicative-error condition number \(6\) in maximum logarithmic norm; no three of the four observation channels suffice for global identification without supplementary information.

Write \(G_+,G_->0\) for upper- and lower-half enclosed areas, and \(T_+,T_->0\) for the corresponding physical-time flight durations. Let \(B\) denote Euler's beta function and
\[
P=(3/2)^{1/3}B(1/2,4/3),\qquad Q=(2/3)^{2/3}B(1/2,1/3),\qquad P/Q=3/5.
\]
The full reconstruction is
\[
\boxed{r=\sqrt{\frac{5G_-}{3T_-}},\qquad \beta=\frac{G_+T_-}{G_-T_+},\qquad
\gamma=\frac{P^3r^5}{G_-^3},\qquad \alpha=\frac{\beta P^3r^5}{G_+^3}.}
\]
These equations define a real-analytic inverse on the entire positive measurement orthant.

## Assumptions and scope

Consider the planar physical-time differential equation, with upper and lower vector fields joined across \(y=0\),
\[
(\dot x,\dot y)=\begin{cases}(-\alpha y^2,\,\beta x),&y\geq0,\\(\gamma y^2,\,x),&y<0,\end{cases}
\qquad \alpha,\beta,\gamma>0.
\]
At a nonzero point of the switching line, the normal velocity on both sides has the same sign, so the crossing orbit is unambiguous. For every \(r>0\), the orbit through \((r,0)\) crosses the upper half-plane toward \((-r,0)\), and returns through the lower half-plane. The four observations are ordered \((G_+,G_-,T_+,T_-)\). Each area is the positive ordinary Euclidean area bounded by its half-orbit and the corresponding switching-line segment; each duration is measured in the time of the displayed equation. The coordinate and physical-time normalizations are essential to the inverse claim.

## Proof

**Existence and exact graph equations.** Dividing the two components in each open half-plane and integrating gives, for \(-r\leq x\leq r\),
\[
y_+(x)=\left(\frac{3\beta}{2\alpha}\right)^{1/3}(r^2-x^2)^{1/3},\qquad
 y_-(x)=-\left(\frac3{2\gamma}\right)^{1/3}(r^2-x^2)^{1/3}.
\]
Both branches are regular away from their two switching endpoints. At those endpoints the nonzero normal velocity yields a transverse crossing. Their union is a simple periodic oval, traversed in the indicated directions. This construction holds for all positive parameters and every \(r>0\), not merely asymptotically.

**Area and flight-time quadratures.** The identity
\[
\int_{-r}^{r}(r^2-x^2)^s\,dx=r^{2s+1}B(1/2,s+1),\qquad s>-1,
\]
follows by putting \(x=r\sqrt u\) on the positive half-interval. Integrating the graph heights for the areas and using \(dt=|dx|/|\dot x|\) separately on each half-orbit, with exponents \(s=1/3\) and \(s=-2/3\), yields
\[
\begin{aligned}
G_+&=P(\beta/\alpha)^{1/3}r^{5/3},&\quad
G_-&=P\gamma^{-1/3}r^{5/3},\\
T_+&=Q\alpha^{-1/3}\beta^{-2/3}r^{-1/3},&
T_-&=Q\gamma^{-1/3}r^{-1/3}.
\end{aligned}
\]
The beta recurrence \(B(a,b+1)=bB(a,b)/(a+b)\) gives \(P/Q=3/5\); therefore
\[
\frac{G_-}{T_-}=\frac35r^2,\qquad
\frac{G_+}{T_+}=\frac35\beta r^2.
\]
These identities immediately recover \(r\) and \(\beta\), and either area then recovers its corresponding stiffness coefficient, giving exactly the four displayed inverse equations. Substitution into the original four forward equations proves both compositions are identity maps on the positive orthant. All functions are analytic there, so the observation map is a global analytic diffeomorphism.

**Minimality of four separate channels.** Fix any three of the four positive measurements and vary the fourth over any positive interval. The global inverse produces different positive parameter/amplitude quadruples with exactly those three fixed measurements. Hence no subset of three observables is globally identifying for the four unrestricted unknowns. This is a statement about selection from these four channels, not an assertion about arbitrary nonlinear single-scalar measurements.

**Sharp logarithmic conditioning.** Set \(p=(\log\alpha,\log\beta,\log\gamma,\log r)\) and \(d=(\log G_+,\log G_-,\log T_+,\log T_-)\). The forward log map is affine \(d=Mp+k\), with
\[
M=\frac13\begin{pmatrix}-1&1&0&5\\0&0&-1&5\\-1&-2&0&-1\\0&0&-1&-1\end{pmatrix},
\qquad \det M=-2/9.
\]
Its inverse coefficient matrix is
\[
M^{-1}=\begin{pmatrix}
-2&3/2&-1&-3/2\\
1&-1&-1&1\\
0&-1/2&0&-5/2\\
0&1/2&0&-1/2
\end{pmatrix}.
\]
The row absolute sums of \(M^{-1}\) are exactly \((6,4,3,1)\), so \(\|M^{-1}\|_{\infty\to\infty}=6\); those of \(M\) give \(\|M\|_{\infty\to\infty}=7/3\). If each observed channel is perturbed multiplicatively by at most \(e^{\pm\varepsilon}\), then the reconstruction obeys
\[
\left|\log\frac{\widetilde\alpha}{\alpha}\right|\leq6\varepsilon,\qquad
\left|\log\frac{\widetilde\beta}{\beta}\right|\leq4\varepsilon,\qquad
\left|\log\frac{\widetilde\gamma}{\gamma}\right|\leq3\varepsilon,\qquad
\left|\log\frac{\widetilde r}{r}\right|\leq\varepsilon.
\]
Every bound is sharp: for any chosen row of \(M^{-1}\), choose the four measurement log perturbations to have signs agreeing with that row. The observations remain strictly positive and, by global surjectivity, physically realizable. The corresponding log-parameter error attains that row sum for every \(\varepsilon>0\). These are exact, global bounds rather than linearized or asymptotic estimates.

## Verification

The accompanying standard-library script `check_inverse.py` evaluates the beta-function normalization, both compositions of the forward and inverse maps on 2000 randomly seeded positive instances and both area-to-time identities. Its successful output is `PIECEWISE_CENTER_FOUR_MEASUREMENT_INVERSE_OK`. The analytic proof, especially the exact beta integral and logarithmic matrix, is independent of finite testing. A separate symbolic matrix inversion confirmed the determinant and four inverse row sums; direct numerical quadrature checked a nonsymmetric example.

## Relationship to prior work

Tang established the global-center criterion and derived its invariant curves and physical-period formulas, including the beta-function scaling. Those equations supply the starting phase portrait and are not claimed as new here. The present claim instead concerns **four-channel observation identifiability from a single orbit, its globally onto inverse, minimal channel count, and sharp parameter-independent multiplicative conditioning**. A subsequent center-classification study by Chen, Llibre and Tang concerns broader piecewise quasi-homogeneous systems; its accessible abstract describes center criteria and monotonicity, not this inverse theorem. The complete text of that second study was not accessible, so its coverage is an explicit priority uncertainty. Closely related studies of other center models and period annuli do not imply injectivity or the condition-number bound for the stated normalized family.

## Limitations

The result assumes exactly the displayed positive three-coefficient normalization, a known switching axis, an orbit identified by its positive section crossing, and exact positive noiseless measurements for exact identification. Only multiplicative perturbations are controlled; additive noise near small areas or times is not uniformly conditioned. The theorem does not identify arbitrary more-general switching vector fields, infer the switching line from data, or claim novelty for the underlying beta integrals. The checked sources do not rule out unindexed equivalent inverse results, and a relevant 2019 full text remained inaccessible. Independent mathematical validation has not been performed.

## References

- Y. Tang, *Global dynamics and unfolding of planar piecewise smooth quadratic quasi-homogeneous differential systems*, arXiv:1708.03444v1, first posted 11 August 2017; published as *Global dynamics and bifurcation of planar piecewise smooth quadratic quasi-homogeneous differential systems*, Discrete and Continuous Dynamical Systems **38** (2018), 2029–2046, DOI:10.3934/dcds.2018082.
- J. Chen, J. Llibre, and Y. Tang, *Centers of discontinuous piecewise smooth quasi-homogeneous polynomial differential systems*, Discrete and Continuous Dynamical Systems B (2019), DOI:10.3934/dcdsb.2019150. Abstract/metadata inspected; full text inaccessible.
