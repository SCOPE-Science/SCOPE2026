# A sharp dimension-seven threshold for the quartic time arrow of trapped run-and-tumble motion

## Finding

A stationary coordinate of a harmonically confined isotropic run-and-tumble particle can exhibit an orientation-dependent *arrow of time* in its fourth-order two-time moments, even though its ordinary stationary autocovariance is invariant under reversal of the observation order. Precisely, let
\[
\mathcal A_d(t)=\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3].
\]
At the natural rate resonance \(\gamma=2a\), where the rate of complete isotropic directional redraws equals twice the trap relaxation rate, set \(s=at\). Then for every \(d\ge1\), \(D\ge0\), and \(t\ge0\),
\[
\boxed{\mathcal A_d(t)=\left(\frac va\right)^4\frac{e^{-4s}}{15d^2(d+2)}F_d(s)},
\]
where
\[
F_d(s)=2(d-7)e^{3s}-3(7d-19)e^{2s}
 +\bigl[30(d-1)s+6(d-7)\bigr]e^s+13d-1.
\]
The formula is *exactly independent* of the independent thermal diffusivity \(D\). Moreover, for every positive lag,
\[
\begin{cases}
\mathcal A_d(t)<0,&1\le d\le7,\\
\mathcal A_d(t)<0\quad(0<t<t_d),\quad \mathcal A_d(t_d)=0,\quad\mathcal A_d(t)>0\quad(t>t_d),&d\ge8,
\end{cases}
\]
with a **unique** crossing \(t_d\) in each dimension \(d\ge8\).

For an arbitrary positive dimensionless redraw rate \(r=\gamma/a\), the short-lag coefficient is
\[
\left(\frac av\right)^4\mathcal A_d(t)
=-\frac{6r(d+r+1)}{d^2(d+2)(r+1)(r+2)(r+3)}s^3+O(s^4).
\]
For \(r>1\), the nonresonant large-lag expansion reads
\[
\left(\frac av\right)^4\mathcal A_d(t)
=\frac{6r(rd-4r-6)}{d^2(d+2)(r-1)(r+1)^2(r+2)(r+3)}e^{-s}+o(e^{-s}).
\]
Consequently, if \(r>1\) and \(d>4+6/r\), the time arrow necessarily changes sign at least once. The *exactly once* conclusion is proved at \(r=2\), not for all rates. At a zero leading large-lag coefficient no next-order sign is claimed by this expansion alone.

## Assumptions and scope

Let \(d\) be an integer at least one. Let \(U_t\in S^{d-1}\) be the right-continuous stationary Markov process which holds its current direction between the events of a rate-\(\gamma>0\) Poisson process and at each event redraws independently from the uniform distribution on \(S^{d-1}\). A redraw may select the previous direction when \(d=1\), so the physical sign-switch rate is \(\gamma/2\). Denote the projection of \(U_t\) onto one fixed axis by \(u_t\). Its invariant moments are
\[
\mathbb E[u_t^2]=\frac1d,\qquad
\mathbb E[u_t^4]=\frac3{d(d+2)}.
\]
Let \(B_t\) be a standard one-dimensional Brownian motion independent of \(U\), and let \(X\) solve in its unique stationary law
\[
dX_t=(-aX_t+vu_t)\,dt+\sqrt{2D}\,dB_t,
\qquad a,v,\gamma>0,\quad D\ge0.
\]
The stationary causal construction \(X_t=v\int_{-\infty}^{t}e^{-a(t-q)}u_q\,dq+\sqrt{2D}\int_{-\infty}^{t}e^{-a(t-q)}\,dB_q\) fixes all initial-state assumptions. The position is centered and has moments of every finite order. All expectations below are in this stationary law. Time \(t>0\) is a forward lag, and the sign convention is \(\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3]\).

The result is an exact single-coordinate, high-dimensional active-particle statement; it does not quantify trajectory-level entropy production, prove microscopic irreversibility is absent when the statistic vanishes, or apply to orientational rotational diffusion, anisotropic redraws, nonharmonic traps or finite-duration tumble states without further arguments.

## Proof

**1. Reduction and stationary moments.** By the stationary convolution and linearity, write \(X=Y+Z\) with independent \(Y\) (the active coordinate, \(D=0\)) and centered stationary Gaussian Ornstein–Uhlenbeck \(Z\). Since \(\mathbb E[Y^2]\) is time-independent and \(\operatorname{Cov}(Z_0,Z_t)=\operatorname{Cov}(Z_t,Z_0)\), Wick expansion of both fourth mixed moments has identical cross terms, while \(\mathbb E[Z_0^3Z_t]=\mathbb E[Z_0Z_t^3]\). Therefore \(\mathcal A_d^X=\mathcal A_d^Y\) for all \(D\ge0\), proving exact thermal-noise invariance.

Scale \(x=aY/v\) and \(s=at\), and set \(r=\gamma/a\). Its generator on polynomial observables is
\[
L f(x,u)=(-x+u)\partial_x f(x,u)
+r\bigl[\langle f(x,w)\rangle_{w\in S^{d-1}}-f(x,u)\bigr].
\]
Writing \(M_{ij}=\mathbb E[x^iu^j]\), stationary generator identities, with \(m_2=1/d\) and \(m_4=3/[d(d+2)]\), yield
\[
\begin{aligned}
M_{11}&=\frac{m_2}{1+r},&M_{20}&=M_{11},\\
M_{13}&=\frac{m_4}{1+r},&M_{22}&=\frac{2M_{13}+r m_2M_{20}}{2+r},\\
M_{31}&=\frac{3M_{22}}{3+r},&M_{40}&=M_{31}.
\end{aligned}
\]
These follow from \(\mathbb E[L(xu)]=\mathbb E[L(x^2)]=\mathbb E[L(xu^3)]=\mathbb E[L(x^2u^2)]=\mathbb E[L(x^3u)]=\mathbb E[L(x^4)]=0\), respectively. The equations are triangular, so no unproved closure assumption is required.

**2. Exact two-time hierarchy.** For fixed stationary \(x_0\), define
\[
\begin{aligned}
h_0&=\mathbb E[x_0x_s],&h_u&=\mathbb E[x_0u_s],\\
h_1&=\mathbb E[x_0x_s^3],&h_2&=\mathbb E[x_0x_s^2u_s],\\
h_3&=\mathbb E[x_0x_su_s^2],&h_4&=\mathbb E[x_0u_s^3].
\end{aligned}
\]
The time-forward generator, including the isotropic redraw of \(u^2\), gives the exact finite triangular-forced system
\[
\begin{aligned}
h_0'&=-h_0+h_u, &h_u'&=-rh_u,\\
h_1'&=-3h_1+3h_2,&h_2'&=-(2+r)h_2+2h_3,\\
h_3'&=-(1+r)h_3+h_4+\tfrac r d h_0,&h_4'&=-rh_4.
\end{aligned}
\]
Its initial data are \((h_0,h_u,h_1,h_2,h_3,h_4)|_{s=0}=(M_{20},M_{11},M_{40},M_{31},M_{22},M_{13})\). In the opposite order, conditioning on the present \((x_0,u_0)\) and using \(\mathbb E[u_s\mid u_0]=e^{-rs}u_0\),
\[
\mathbb E[x_0^3x_s]=M_{40}e^{-s}
+M_{31}\frac{e^{-s}-e^{-rs}}{r-1}\qquad(r\ne1),
\]
with its continuous \(r=1\) limit. Hence the difference is obtained without a closure at any higher order by subtracting the solution \(h_1(s)\) of the displayed six equations.

At \(r=2\) the initial values reduce to
\[
M_{20}=M_{11}=\frac1{3d},\quad
M_{13}=\frac1{d(d+2)},\quad
M_{22}=\frac{2d+1}{3d^2(d+2)},\quad
M_{31}=M_{40}=\frac{2d+1}{5d^2(d+2)}.
\]
Solving successively for \(h_u,h_0,h_4,h_3,h_2,h_1\) by integrating factors and subtracting the preceding expression gives exactly the stated exponential-polynomial \(e^{-4s}F_d(s)/[15d^2(d+2)]\). This step can be verified independently by substituting that expression and the explicit initial values into the six constant-coefficient equations; `verify.py` performs an independent fourth-order Runge–Kutta integration of precisely this system at multiple lags and dimensions. The rational identities for the stationary moments also have exact independent checks.

**3. Sign and uniqueness at \(r=2\).** Direct differentiation gives
\[
F_d(0)=F_d'(0)=F_d''(0)=0,\qquad F_d'''(0)=-18(d+3)<0.
\]
For \(s\ge0\), define the sign-equivalent third-derivative function
\[
H_d(s)=e^{-s}F_d'''(s)
=54(d-7)e^{2s}-24(7d-19)e^s+30(d-1)s+96d-132.
\]
At the endpoints,
\[
H_1(s)=-36(9e^{2s}-8e^s+1)<0,\qquad
H_7(s)=180(s+3-4e^s)<0
\]
for all \(s\ge0\). The first inequality follows from \(9y^2-8y+1>0\) for \(y\ge1\); the second from \(e^s\ge1+s\). Since \(H_d(s)\) is affine in \(d\), it is negative for every real \(1\le d\le7\), and consequently \(F_d'''<0\). Triple integration with the three zero initial values makes \(F_d(s)<0\) for all \(s>0\).

For each \(d\ge8\), differentiate once more:
\[
H_d'(s)=108(d-7)e^{2s}-24(7d-19)e^s+30(d-1).
\]
As a function of \(y=e^s\ge1\), the right-hand side is an upward-opening quadratic, negative at \(y=1\), where it is \(-30(d+11)\), and positive for sufficiently large \(y\). Its two roots have opposite ordering about \(1\), with exactly one in \((1,\infty)\), so \(H_d\) first strictly decreases and then strictly increases. Since \(H_d(0)=-18(d+3)<0\) and \(H_d(s)\to\infty\), it crosses zero exactly once, from negative to positive. Now the same one-sign-change argument can be applied successively to \(F_d''\), \(F_d'\) and \(F_d\): each starts at zero (except the negative initial value of the preceding third derivative), is initially decreasing and eventually grows without bound, hence has one positive zero after its predecessor's zero. Finally \(F_d(s)\to+\infty\) because its leading term is \(2(d-7)e^{3s}\). It follows that \(F_d\) has exactly one strictly positive zero, negative before and positive after. Because all other factors multiplying \(F_d\) are positive, the theorem follows.

**4. General redraw-rate boundaries.** The stationary fourth-arrow has its first three Taylor coefficients (orders zero, one and two) equal to zero. Apply the exact matrix generator of Step 2 three times at the initial data of Step 1. Its third derivative is \(-36r(d+r+1)/[d^2(d+2)(r+1)(r+2)(r+3)]\), giving the stated coefficient of \(s^3\). For \(r>1\), all the other forcing exponentials decay strictly faster than \(e^{-s}\) (possible coincident faster exponents merely add polynomial factors). Extracting the \(e^{-s}\) eigenmode of the triangular hierarchy, or equivalently solving the coefficient recursions for \(h_0,h_3,h_2,h_1\), gives
\[
\lim_{s\to\infty}e^s\left(\frac av\right)^4\mathcal A_d(s/a)=
\frac{6r(rd-4r-6)}{d^2(d+2)(r-1)(r+1)^2(r+2)(r+3)}.
\]
This proves the additional sufficient criterion for at least one crossing by continuity. When its coefficient vanishes, the displayed limit is zero but does not determine the eventual sign.

## Verification

The supplied `verify.py` uses only Python's standard library. Its direct execution gives `PASS 435 deterministic checks`. These include exact rational stationary balances and third-derivative coefficients; independent numerical integration of the generator's six-dimensional conditional-moment system against the closed formula; root-sign brackets for dimensions \(8,9,10,12,20,50\); independent extraction of the long-lag mode coefficient over five positive rate ratios; and explicit Gaussian-noise cancellation checks. Representative dimensionless roots \(s_d=at_d\) are approximately \(3.845481152\) at \(d=8\), \(3.224418129\) at \(d=9\), and \(2.893527361\) at \(d=10\). These finite numerical tests corroborate but do not replace the analytical proof of exact uniqueness for all integer dimensions.

Reproduce with `python3 verify.py`; no network, external data, or third-party packages are necessary. The code and proof refer to the same single-coordinate model, stationary law and sign convention.

## Relationship to prior work

Guéneau, Majumdar and Schehr (first public February 9, 2026, arXiv:2602.08436) establish the stationary position distributions for isotropically trapped run-and-tumble particles in arbitrary dimension, including their Gaussian thermal convolution; they do not state the mixed two-lag fourth-order arrow or its dimension-seven sign threshold. Sun, Ye and Podgornik (arXiv:2409.00578) and Frydel's oscillator-moment analyses supply general moment-calculation methodology. Sun, Ye and Chen (arXiv:2610.24961, first posted October 18, 2026) develop a related, more general conditional moment construction; their specific solutions concern single-time conditional distributions and do not give the present unique lag-reversal theorem. Garcia-Millan and Pruessner (2021) investigate one-dimensional harmonic RTP field theory and entropy production, including lower-order time correlations, not this high-dimensional quartic criterion. General active-matter irreversibility is well-established; this does not claim its discovery. The distinction is the exact dimension threshold, uniqueness in lag at a rate resonance, and invariance under independent thermal noise.

The comparison is at the level of actual claims and formulas, not just titles: stationary one-time distributions do not imply the two-time arrow without a transition law, while general moment recursions provide a route to compute it but do not explicitly settle its sign/number of zeros across dimensions. This is a specific publication-priority assessment, not a uniqueness guarantee.

## Limitations

The theorem assumes complete independent isotropic direction redraws, not persistent rotational diffusion, partial turns or a finite-duration tumble state. The exact one-crossing conclusion holds at \(\gamma=2a\) only. The arbitrary-rate large-lag asymptotic requires \(\gamma>a\), and a zero leading coefficient is not a resolved next-order asymptotic. High spatial dimension is a mathematical regime and may not describe a literal microscopic swimmer. The observable is a temporal asymmetry witness, not an entropy-production estimator. Previous literature offers general moment machinery; the residual originality risk is that a specialized unindexed result might already state an equivalent sign classification. No independent audit has been performed.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (first public 2026-02-09), later *Physical Review E* 114, 014144 (2026). https://arxiv.org/abs/2602.08436
2. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1 (2026-10-18). https://arxiv.org/abs/2610.24961
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1 (2024-09-01). https://arxiv.org/abs/2409.00578
4. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, *J. Stat. Mech.* 2021, 063203. https://doi.org/10.1088/1742-5468/ac014d
5. M. Demaerel and C. Maes, *Active processes in one dimension*, arXiv:1801.01894 (2018). https://arxiv.org/abs/1801.01894
