# A third-jump-moment threshold and covariance twins with opposite time arrows in reset transport

## Finding

Let a stationary nonnegative jump-transport particle receive independent Poisson jumps of iid size \(J>0\) at rate \(\lambda>0\), and undergo independent proportional Poisson resets \(X\mapsto cX\) at rate \(q>0\), where \(0\le c<1\). Assume \(\mathbb E J^3<\infty\), and write \(r=\lambda/q\), \(m_j=\mathbb E[J^j]\), \(u=m_2/m_1^2\), and \(v=m_3/m_1^3\). For the centered stationary process \(Y_t=X_t-\mathbb E X_0\), define the chronological third-order contrast
\[
\mathcal A_c(t)=\mathbb E[Y_0^2Y_t]-\mathbb E[Y_0Y_t^2],\qquad t>0.
\]
For every \(0<c<1\), the exact all-lag law is
\[
\boxed{\mathcal A_c(t)=\frac{r m_1^3[(v+ru)c(1+c)-2r(u+r)]}{c(1+c)(1-c^3)}\left(e^{-q(1-c)t}-e^{-q(1-c^2)t}\right).}
\]
At \(c=0\), its continuous extension is \(\mathcal A_0(t)=-2qr^2m_1^3(u+r)t e^{-qt}<0\).

The sign is constant across every positive lag and has a sharp complete classification. If \(r\ge\sqrt v\), it is strictly negative for all \(0\le c<1\). If \(0<r<\sqrt v\), it is strictly negative below, exactly zero at, and strictly positive above the unique contraction
\[
\boxed{c_* =\frac{\sqrt{1+8r(u+r)/(v+ru)}-1}{2}\in(0,1).}
\]
In particular, the existence of a sign reversal as contraction varies is determined by the third raw jump moment relative to its mean, with no dependence on the second raw moment.

Two explicit strictly positive burst laws give **opposite chronological arrows but identical stationary means and entire second-order covariance functions**. Keep \(r=9/4\), \(c=49/50\), \(q>0\) arbitrary. For law A, \(J=1/5\) with probability \(25/41\), or \(J=9/4\) with probability \(16/41\). For law B, \(J=1/2\) with probability \(4/5\), or \(J=3\) with probability \(1/5\). Both have \(m_1=1\) and \(m_2=2\), but their third moments are \(89/20\) and \(11/2\), respectively. The sign numerator in the boxed formula is strictly negative for A and strictly positive for B at this same contraction, for every lag \(t>0\). The two stationary covariance functions coincide exactly:
\[
\operatorname{Cov}(X_0,X_t)=\frac{r(m_2+r m_1^2)}{1-c^2}e^{-q(1-c)t}.
\]

## Assumptions and scope

The two Poisson clocks and all nonnegative iid jump marks are mutually independent. The process is defined by an upward jump \(X\mapsto X+J\) at each input event and a multiplicative collapse \(X\mapsto cX\) at each reset event. At \(c=0\), complete resets are permitted. The invariant distribution exists uniquely for each \(c<1\): contraction at independent reset times and finite logarithmic input moment give the standard perpetuity construction. The stated finite third moment ensures all displayed moments are finite. The stationary process is taken in two-sided equilibrium; no assertion is made for nonstationary preparations. All times and rates are physical continuous-time variables. The zero at \(c=c_*\) means vanishing of this particular third-degree statistic, not detailed balance or reversibility.

## Proof

**Step 1: invariant cumulants.** Let \(S\) be the compound-Poisson influx accumulated over an independent \(\operatorname{Exp}(q)\) interval. Writing \(M_J(z)=\mathbb E e^{zJ}\) as a formal power series to degree three (no positive exponential moment is required), its cumulant series is
\[
\log\mathbb E e^{zS}=-\log\big(1-r(M_J(z)-1)\big).
\]
Thus its first three cumulants are \(r m_1\), \(r m_2+r^2m_1^2\), and \(r m_3+3r^2m_1m_2+2r^3m_1^3\). The stationary series \(X\stackrel d=\sum_{j\ge0}c^jS_j\), with independent copies \(S_j\), yields
\[
\bar x=\frac{r m_1}{1-c},\quad V=\operatorname{Var}(X)=\frac{r m_2+r^2m_1^2}{1-c^2},\quad T=\mathbb E[(X-\bar x)^3]=\frac{r m_3+3r^2m_1m_2+2r^3m_1^3}{1-c^3}.
\]
These identities also follow from the generator on powers through degree three.

**Step 2: conditional polynomial relaxation.** The generator is
\[
\mathcal L f(x)=\lambda\mathbb E[f(x+J)-f(x)]+q[f(cx)-f(x)].
\]
For \(y=x-\bar x\), let \(a_1=q(1-c)\) and \(a_2=q(1-c^2)\). Direct expansion gives \(\mathcal Ly=-a_1y\) and
\[
\mathcal L(y^2-V)=-a_2(y^2-V)+2\lambda m_1(1-c)y.
\]
For \(0<c<1\), integrating the two triangular linear equations gives
\[
P_t y=e^{-a_1t}y,\qquad
P_t(y^2-V)=e^{-a_2t}(y^2-V)+\frac{2r m_1}{c}(e^{-a_1t}-e^{-a_2t})y.
\]
Stationary expectation of the products with \(Y_0\) and \(Y_0^2\) yields
\[
\mathcal A_c(t)=\left(T-\frac{2r m_1}{c}V\right)(e^{-a_1t}-e^{-a_2t}).
\]
Substitution of Step 1 and cancellation of the common factor \(1-c\) yield the first boxed identity. At \(c=0\), the relaxation eigenvalues coincide; integrating the triangular equations gives the stated \(-2qr^2m_1^3(u+r)t e^{-qt}\) limit.

**Step 3: global sign and sharp threshold.** For \(0<c<1\) and \(t>0\), every factor outside \(H(c)=(v+ru)c(1+c)-2r(u+r)\) is strictly positive. The polynomial \(H\) is strictly increasing on \([0,1]\), with \(H(0)=-2r(u+r)<0\) and \(H(1)=2(v-r^2)\). Therefore an interior zero exists exactly when \(r<\sqrt v\), and is unique with the displayed root. At the boundary \(r=\sqrt v\), the only formal root is the excluded limit \(c=1\). The endpoint \(c=0\) has strictly negative contrast.

**Step 4: covariance twins.** The same first-degree relaxation proves the displayed covariance identity. The two explicit two-point laws each have \(m_1=1\) and \(m_2=2\); their third moments are \(89/20\) and \(11/2\). At the specified parameters, \(r^2=81/16\) lies strictly between these third moments, and the exact sign numerator at \(c=49/50\) is negative for A and positive for B (checked as exact rationals by the included script). This gives opposite signs simultaneously for all positive lags while preserving the complete second-order covariance.

## Verification

Run `python checker.py` with Python 3; only the standard library is required. It reconstructs raw invariant moments by the generator recurrence, independently factors the chronological contrast, and checks the explicit two-point laws with exact rational arithmetic. It runs 64 further exact moment-factor comparisons across jump distributions, rate ratios and contraction factors, checks all three witness lags, verifies the complete-reset sign, and validates the critical-root dichotomy. The checker tests finite polynomial identities; the proof above establishes the statements for all permissible distributions and all positive lags, not the finite cases alone.

## Relationship to prior work

Palmowski and Vlasiou (arXiv:2611.14692v1, first posted November 10, 2026), Sections 2.3–2.7, establish stationary perpetuities, transforms and moment recursions for general Lévy inflow with affine resetting; their finite-activity formula includes the underlying jump model. Assefa, Keller-Ressel and Palmowski (arXiv:2610.01363v1, first posted October 1, 2026), Theorem 3.11 and Corollary 3.12, already provide a general matrix-exponential procedure for computing cross-moments of polynomial processes with affine resets. **Neither the stationary-moment machinery nor the general cross-moment calculability is claimed as new.** The new statement here is the exact all-lag third-order sign classification, cancellation of the second jump moment from the existence criterion, and explicit strictly-positive burst laws with identical full covariance but opposite temporal asymmetry. The general cross-moment theorem formally supplies the machinery from which these consequences can be derived; priority of this specific qualitative corollary needs independent assessment.

## Limitations

The model assumes linear proportional resets, independent homogeneous Poisson clocks, iid positive kicks, stationarity and a finite third jump moment. The contrast may vanish at its threshold without eliminating other forms of time irreversibility; no claim of complete detailed balance is made. Matching complete second-order covariance does not imply agreement of higher-order moments or path laws. The cited general polynomial-process theory is broad enough to calculate the present cross moments and represents a real originality-priority risk. No physical entropy-production identity is asserted. No independent scientific audit has been performed.

## References

1. Z. Palmowski and M. Vlasiou, *Steady-state of Lévy process with general resetting: unreflected and reflected cases*, arXiv:2611.14692v1, November 10, 2026, https://arxiv.org/html/2611.14692v1.
2. J. Assefa, M. Keller-Ressel and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363v1, October 1, 2026, https://arxiv.org/html/2610.01363v1.
3. O. Boxma, D. Perry, W. Stadje and S. Zacks, *A Markovian growth-collapse model*, *Advances in Applied Probability* 38 (2006), 221–243, https://doi.org/10.1239/aap/1143936148.
