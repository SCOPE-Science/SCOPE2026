# Unique optimal rotation for mean-square Euler stability under coordinate multiplicative noise

## Finding
Let \(a>0\), \(\omega\ge0\), \(\sigma>0\). Consider the planar Itô system
\[
\mathrm dX_t=(-aI_2+\omega J)X_t\,\mathrm dt+\sigma P X_t\,\mathrm dW_t,
\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad P=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
For constant-step Euler–Maruyama, let \(x=ah>0\), \(s=(\omega/a)^2\), and \(\tau=\sigma^2/a\). Define
\[
F_s(x)=\frac{2(2+s)-2(2+s)x+(1+s)x^2}{(1+s)[2-(1+s)x][4-4x+(1+s)x^2]}.
\]
Mean-square asymptotic stability for **every** deterministic initial vector occurs if and only if
\[
0<x<\frac{2}{1+s}\quad\text{and}\quad \tau F_s(x)<1.
\]
For every fixed \(s\ge0\), \(F_s\) increases strictly from \((2+s)/[4(1+s)]\) to \(+\infty\) on this interval. Thus a stable positive step exists exactly when \(\tau<4(1+s)/(2+s)\), and then the stable steps are exactly \(0<h<h_c(s)/a\), where \(h_c(s)\) denotes the unique root \(\tau F_s(h_c)=1\) in \((0,2/(1+s))\). (Here \(h_c\) is dimensionless.) No stability reentry is possible at larger steps.

**Unique optimal-rotation conclusion.** If \(2<\tau<4\), then positive stable steps exist precisely at frequencies satisfying
\[
s>s_0=\frac{2\tau-4}{4-\tau}.
\]
On that frequency range the sharp scaled step ceiling \(h_c(s)\) tends to zero at both ends and has exactly **one** global maximizer \(s_*(\tau)\in(s_0,\infty)\). It is the unique solution of the two equations
\[
\tau F_s(x)=1,\qquad \partial_sF_s(x)=0,
\]
with \(x>0\), \(s>s_0\) and \(0<x<2/(1+s)\). In particular, at \(\tau=3\) numerical solution yields \(s_*\approx5.0082572\), \(\omega_*/a\approx2.2379136\), and \(h_c(s_*)\approx0.04224749\). These decimal approximations are not used to establish uniqueness.

## Assumptions and scope
The driving Wiener increments are independent, centered, and have variance \(h\). A fresh increment is used at each Euler step. The stochastic differential equation is interpreted in the Itô sense. Stability means \(\lim_{n\to\infty}\mathbb E\|X_n\|_2^2=0\) for every fixed deterministic starting vector; it is not merely stability of the expected vector. The noise acts on the first coordinate only and is proportional to that coordinate. The continuous-time drift is a normal damped rotation; no assumption of simultaneous diagonalizability of drift and noise is made.

## Proof
**Covariance feedback reduction.** Set \(C=I_2+h(-aI_2+\omega J)=cI_2+dJ\) with \(c=1-x\) and \(d=\sqrt{s}\,x\). The covariance recursion is the positive linear map on symmetric matrices
\[
\mathcal T(V)=CVC^{\mathsf T}+h\sigma^2PVP.
\]
Its noise-free part \(\mathcal T_0(V)=CVC^{\mathsf T}\) has spectral radius \(q=c^2+d^2\). A necessary condition for mean-square stability is \(q<1\), equivalent to \(0<x<2/(1+s)\), because \(\mathcal T\ge\mathcal T_0\) on the positive-semidefinite cone. For \(q<1\), write \(\ell(V)=V_{11}\). The nonnegative resolvent is \((I-\mathcal T_0)^{-1}=\sum_{k\ge0}\mathcal T_0^k\). The rank-one positive perturbation has strength \(h\sigma^2 P\ell(V)\). The positive-resolvent or Perron–Frobenius criterion gives
\[
\rho(\mathcal T)<1\ \Longleftrightarrow\ h\sigma^2\,\ell((I-\mathcal T_0)^{-1}P)<1.
\]
Indeed the Sherman–Morrison inverse is positive if the right-hand inequality holds. A cone-Perron eigenmatrix of \(\mathcal T\) rules out stability if it fails: at equality the inverse is singular, and beyond equality spectral radius is nondecreasing under increasing positive feedback. This also treats \(d=0\), where direct diagonal covariance recursion gives the same criterion.

Since \(C^k=q^{k/2}\) times a rotation, \((C^k)_{11}=\mathrm{Re}(c+\mathrm id)^k\), and therefore
\[
\ell((I-\mathcal T_0)^{-1}P)
=\sum_{k=0}^{\infty}[\mathrm{Re}(c+\mathrm id)^k]^2
=\frac1{2(1-q)}+\frac12\mathrm{Re}\frac1{1-(c+\mathrm id)^2}.
\]
Exact rational simplification, using \(h\sigma^2=\tau x\), gives \(h\sigma^2\ell((I-\mathcal T_0)^{-1}P)=\tau F_s(x)\).

**Strict timestep monotonicity.** Set \(t=1-(1+s)x/2\), so \(0<t<1\). Then
\[
F_s(x)=\frac{s(s+1)+2st+2t^2}{4(1+s)t(s+t^2)}.
\]
Direct differentiation gives
\[
\frac{\partial F_s}{\partial x}
=\frac{s^3+s^2+(3s^2+s)t^2+4st^3+2t^4}{8t^2(s+t^2)^2}>0.
\]
The endpoint limits establish the unique positive timestep threshold and no-reentry statement. The limit at \(x=0\) also equals the continuous-time return-gain threshold, since
\[
\int_0^\infty e^{-2at}\cos^2(\omega t)\,\mathrm dt
=\frac{2+s}{4a(1+s)}.
\]

**Strict frequency-profile unimodality.** At any fixed \(0<x<2\), the sign of \(\partial_sF_s(x)\), wherever \(0\le s<2/x-1\), equals the sign of
\[
\begin{aligned}
G_x(s)={}&x^3[(x-1)^2+1]s^3
+x[3(x-1)^4-(x-1)^2+2]s^2\\
&+x(x-2)^2[3(x-1)^2+1]s
+(x-2)^3(x-1)^2.
\end{aligned}
\]
All coefficients of positive powers of \(s\) are positive, and the constant is nonpositive. Thus \(G_x\) increases strictly for \(s\ge0\), and \(F_s(x)\) has at most one stationary point as a function of \(s\), necessarily a strict minimum. At \(x=1\) the minimum is at \(s=0\); otherwise the derivative starts negative. The expression \(3u^2-u+2>0\) for \(u\ge0\) verifies the only nonobvious coefficient sign.

**Unique optimal frequency.** For \(2<\tau<4\), \(\tau F_s(0)<1\) holds exactly for \(s>s_0\). The uniquely defined \(h_c(s)\) depends continuously on \(s\). As \(s\downarrow s_0\), the strict increase in \(x\) forces \(h_c(s)\downarrow0\); as \(s\to\infty\), \(0<h_c(s)<2/(1+s)\to0\). A positive global maximum is therefore attained at a finite interior \(s_*\). At this maximum, \(\partial_sF_{s_*}(h_c(s_*))=0\). If there were two different maximizers \(s_1<s_2\) at the same maximal step \(x_*\), strict frequency-profile unimodality would give a point between them with \(F_s(x_*)<1/\tau\). Strict continuity in \(x\) would allow a slightly larger stable step at that intermediate frequency, a contradiction. Hence the maximizer is unique. Any admissible solution of the two stationary equations minimizes the entire fixed-\(x\) frequency profile, so it is itself a globally maximal step; consequently no second stationary pair exists. This also proves the stated two-equation characterization.

## Verification
The standalone \(verify.py\) performs exact symbolic checks of the resolvent identity, the two derivative numerator identities, and the covariance-map determinant identity. It also evaluates rational test cases of the sign criterion against the full three-dimensional covariance-update spectrum, and recomputes the \(\tau=3\) stationary pair numerically. All experiments serve as checks, not substitutes for the proof above. Run \(python verify.py\) with Python 3, SymPy, and NumPy installed; see \(verification_output.txt\).

## Relationship to prior work
Lang, Petersson and Thalhammer (2017, arXiv:1702.07700, especially Proposition 3.1, Corollary 3.1 and Theorem 3.1) establish general covariance spectral-radius criteria and sufficient bounds for numerical SDE stability. The general spectral criterion includes this finite-dimensional model implicitly, but does not state the present rational threshold or the unique rotation-frequency optimization. Song, Geng and Liu (2020, arXiv:2001.05203) prove small-step stability equivalences for broader stochastic systems, not an exact frequency-dependent optimization. Senosiain and Tocino (2023, DOI:10.1007/s11075-022-01478-6) investigate continuous-time mean-square destabilization, notably for nonnormal Jordan drifts; they do not calculate the present Euler discretization and unique optimal rotation. The standard deterministic Euler stability disk supplies only \(x<2/(1+s)\), not the rank-one noise feedback inequality. These distinctions concern implications of checked statements, not merely differing titles.

## Limitations
The model is two-dimensional, uses one rank-one diagonal multiplicative noise coefficient, and concerns constant-step explicit Euler–Maruyama. No claims are made for larger matrices, other noise geometries, nonlinear equations, almost-sure Lyapunov exponents, or relative finite-time accuracy. The no-reentry property alone is consistent with general Lyapunov monotonicity arguments for Euler–Maruyama; the specific closed threshold and the unique frequency optimizer constitute the quantitative classification. Historical priority requires independent review.

## References
- A. Lang, A. Petersson, A. Thalhammer, *Mean-square stability analysis of approximations of stochastic differential equations in infinite dimensions*, arXiv:1702.07700, first submitted 24 February 2017. https://arxiv.org/abs/1702.07700 ; https://doi.org/10.1007/s10543-017-0684-7 .
- M. Song, Y. Geng, M. Liu, *Stability equivalence among stochastic differential equations and stochastic differential equations with piecewise continuous arguments and corresponding Euler-Maruyama methods*, arXiv:2001.05203, first submitted 15 January 2020. https://arxiv.org/abs/2001.05203 .
- M. J. Senosiain, A. Tocino, *A survey of mean-square destabilization of multidimensional linear stochastic differential systems with non-normal drift*, *Numerical Algorithms* 93 (2023), 1543–1559. https://doi.org/10.1007/s11075-022-01478-6 .
- E. Buckwar, T. Sickenberger, *A comparative linear mean-square stability analysis of Maruyama- and Milstein-type methods*, arXiv:0912.1968 (2009). https://arxiv.org/abs/0912.1968 .
