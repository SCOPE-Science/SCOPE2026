# Sharp three-atom bistability for unbiased multiplicative gradient clipping

## Finding

Fix a clipping level \(c>0\) and let \(C_c(t)=\max\{-c,\min\{t,c\}\}\). For a scalar multiplicative oracle \(g(x,A)=Ax\), put \(H_c(x)=\mathbb E[C_c(Ax)]\). Assume \(\mu=\mathbb E A>0\) and \(S=\mathbb E\operatorname{sgn}(A)>0\); thus the true objective \(f(x)=\mu x^2/2\) is strongly convex, and the clipped mean gradient points inward both near zero and sufficiently far from zero.

**Sharp support classification.** If \(A\) is supported on at most two nonzero values, \(H_c(x)>0\) for every \(x>0\). For exactly three nonzero values with distinct absolute magnitudes \(a_1>a_2>a_3>0\), probabilities \(p_1,p_2,p_3>0\), and signs \(s_i\in\{-1,+1\}\), additional nonzero zeros occur only with sign pattern \((s_1,s_2,s_3)=(+1,-1,+1)\). In that pattern, \(H_c\) has exactly two *simple* positive zeros if and only if
\[
p_2>p_1+p_3\frac{a_3}{a_2}.
\]
They are
\[
r_1=\frac{cp_1}{p_2a_2-p_3a_3},\qquad r_2=\frac{c(p_2-p_1)}{p_3a_3},
\qquad \frac c{a_1}<r_1<\frac c{a_2}<r_2<\frac c{a_3}.
\]
The mean descent flow has an attracting zero, repelling \(\pm r_1\), and attracting \(\pm r_2\). At equality there is one additional touching zero at \(\pm c/a_2\), with no negative-drift interval; below equality the origin is the only zero. This proves minimality of three oracle atoms for such nonoptimal attracting equilibria under \(\mu,S>0\).

**An exact instance and stochastic consequence.** Take
\[
\Pr(A=12)=\tfrac15,\qquad \Pr(A=-3)=\tfrac25,\qquad
\Pr(A=\tfrac12)=\tfrac25.
\]
Then \(\mu=7/5\), \(S=1/5\), and \(H_c\) has precisely five zeros \(0,\ \pm c/5,\ \pm c\). The expected-gradient recursion \(x_{k+1}=x_k-\eta H_c(x_k)\) with \(0<\eta\le5/7\) converges to zero if \(|x_0|<c/5\), to \(c\) if \(x_0>c/5\), and to \(-c\) if \(x_0<-c/5\); \(\pm c/5\) are fixed unstable separators.

More strongly, consider *actual* independent-sample clipped SGD \(X_{n+1}=X_n-\eta_n C_c(A_nX_n)\) with \(X_0=c\) and \(\eta_n=1/[4(n+1)]\). Then
\[
\Pr\bigl(\lim_{n\to\infty}X_n=c\bigr)\ \ge\ 1-\frac{\pi^2}{24}\ >\ 0.58,
\]
although the unique minimizer of \(f(x)=7x^2/10\) is zero. For the identical oracle and stepsizes, ordinary **unclipped** SGD converges to zero almost surely from every deterministic start.

## Assumptions and scope

The oracle values \(A_n\) are independent and identically distributed; \(c>0\) is fixed, and clipping is applied separately to each sampled scalar gradient, *before* averaging. The support classification assumes at most three nonzero oracle values and strictly distinct magnitudes in the three-atom case. No individual sampled quadratic is assumed convex: in the concrete instance one sampled curvature is negative, whereas the expected objective is globally strongly convex. The far-field sign condition \(S>0\) and the near-zero curvature condition \(\mu>0\) are essential to the sharp minimal-support statement. The stochastic probability statement concerns the concrete three-atom distribution and specified decreasing stepsizes, not general distributions or arbitrary steps.

## Proof

**1. Exact sign classification.** By oddness it suffices to study \(x>0\). With \(b_i=c/a_i\) and \(b_1<b_2<b_3\), the field \(H_c\) is linear between adjacent breakpoints and has values
\[
H_c(b_1)=\mu b_1>0,\qquad
H_c(b_2)=c\bigl(s_1p_1+s_2p_2+s_3p_3a_3/a_2\bigr),\qquad
H_c(b_3)=cS>0.
\]
It is strictly positive before \(b_1\) and constant positive after \(b_3\). For two atoms, only one interior breakpoint exists, so linear interpolation between positive endpoint values excludes any nonzero zero. For three atoms, a negative interval is possible exactly when \(H_c(b_2)<0\). If \(s_1=-1\), then \(\mu>0\) gives \(s_2p_2+s_3p_3a_3/a_2>p_1a_1/a_2>p_1\), so \(H_c(b_2)>0\). If \(s_3=-1\), then \(S>0\) implies \(s_1p_1+s_2p_2>p_3\), again forcing \(H_c(b_2)>0\). The only remaining way to make the middle value negative is the pattern \((+,-,+)\), when \(H_c(b_2)/c=p_1-p_2+p_3a_3/a_2\). Its negative sign is the displayed strict condition. On \((b_1,b_2)\), \(H_c(x)=cp_1+(-p_2a_2+p_3a_3)x\), and on \((b_2,b_3)\), \(H_c(x)=c(p_1-p_2)+p_3a_3x\). Solving these two affine equations gives \(r_1,r_2\) and strict locations; the signs alternate \(+,-,+\). At equality the middle breakpoint is the sole additional positive zero and merely touches zero; in all other cases the field is strictly positive for \(x>0\). Mirror by oddness.

**2. Exact concrete mean field and basins.** For \(r=|x|\), one obtains \(H_c(x)=\operatorname{sgn}(x)h_c(r)\), with \(h_c(0)=0\) and
\[
h_c(r)=\begin{cases}
7r/5,&0\le r\le c/12,\\
c/5-r,&c/12\le r\le c/3,\\
(r-c)/5,&c/3\le r\le2c,\\
c/5,&r\ge2c.
\end{cases}
\]
The roots are therefore \(0,c/5,c\) on the nonnegative ray. If \(0<\eta\le5/7\), then \(0\le x-\eta H_c(x)<x\) for \(0<x<c/5\). For \(c/5<x<c\), \(x<x-\eta H_c(x)\le c\). For \(x>c\), \(c\le x-\eta H_c(x)<x\). These inequalities follow directly from the affine branches, with \(H_c(x)\le(7/5)x\) near zero and \(|H_c(x)|\le|x-c|/5\) between \(c/3\) and \(2c\); beyond \(2c\), \(H_c=c/5\) and the step cannot cross \(c\). Consequently every non-fixed positive orbit is monotone, bounded, and converges to the only zero in its invariant interval. Oddness proves the negative half-line. The slopes at the zeros are \(7/5,-1,1/5\), proving the stability assertions.

**3. Genuine stochastic attraction to the wrong point.** Let \(Y_n=X_n-c\) and \(\tau=\inf\{n\ge0:|Y_n|\ge c/2\}\). For \(n<\tau\), the iterate lies in \((c/2,3c/2)\subset(c/3,2c)\), and hence the conditional mean clipped gradient is exactly \(\mathbb E[C_c(A_nX_n)\mid\mathcal F_n]=Y_n/5\). Every realized clipped gradient has magnitude at most \(c\). Therefore
\[
\mathbb E[Y_{(n+1)\wedge\tau}^2\mid\mathcal F_n]
\le Y_{n\wedge\tau}^2-\frac{2\eta_n}{5}Y_n^2\mathbf1_{\{n<\tau\}}+c^2\eta_n^2\mathbf1_{\{n<\tau\}}.
\]
Telescoping gives \(\mathbb E[Y_{n\wedge\tau}^2]\le c^2\sum_{k\ge0}\eta_k^2=c^2\pi^2/96\). Since \(|Y_\tau|\ge c/2\) on a finite exit, \(\Pr(\tau<\infty)\le4(\pi^2/96)=\pi^2/24\). Moreover \(Y_{n\wedge\tau}^2+c^2\sum_{k\ge n}\eta_k^2\) is a nonnegative supermartingale and therefore converges almost surely. Summing the negative drift term shows \(\sum_{n\ge0}\eta_nY_n^2\mathbf1_{\{n<\tau\}}<\infty\) almost surely. On \(\{\tau=\infty\}\), the squared error has a limit while \(\sum_n\eta_n=\infty\), so that limit must be zero: \(X_n\to c\). This proves the stated positive probability.

**4. Unclipped contrast.** Without clipping, \(X_{n+1}=(1-\eta_nA_n)X_n\). Here \(\mathbb EA=7/5\) and \(\mathbb EA^2=65/2\). For all sufficiently large \(n\),
\[
\mathbb E[X_{n+1}^2\mid\mathcal F_n]
=\left(1-\frac{14}{5}\eta_n+\frac{65}{2}\eta_n^2\right)X_n^2
\le\left(1-\frac75\eta_n\right)X_n^2.
\]
Since \(\sum_n\eta_n=\infty\), this implies \(\mathbb E X_n^2\to0\); the nonnegative squared-error supermartingale then converges to zero almost surely.

## Verification

The standalone \(\texttt{verify.py}\) uses exact rational arithmetic to check the piecewise field values, the five-zero classification for the explicit instance, hundreds of three-atom sign/probability configurations under the stated balance conditions, the predicted root formulas, and a dense finite rational set of one-step invariance inequalities. Run \(\texttt{python3 verify.py}\) with Python 3 and no external packages. These checks are supplementary: the universal support classification and almost-sure stochastic assertions follow from the preceding proofs, not from finite testing.

## Relationship to prior work

Nekrasova et al. (2026, arXiv:2610.28107), Appendix H.5, Proposition H.6, use a **two-atom** signed-multiplicative oracle with a negative clipped drift at large positive states, leading to escape/divergence. Their Appendix H.4 analyzes a distinct **additive-noise** example with a unique shifted attracting point. Neither stated construction enforces both \(\mu>0\) and \(S>0\) while producing multiple nonzero attracting basins. Koloskova, Hendrikx and Stich (2023, arXiv:2305.01588), Section 3.1 and Appendix C.5, prove unavoidable clipping bias using additive Bernoulli shifts; this does not imply the sharp number of multiplicative curvature atoms, the five-zero mean-field topology, or a positive-probability wrong-limit event with Robbins–Monro steps. Faw et al. (2023, arXiv:2302.06570) provide the earlier two-point oracle discussed and reproduced by Nekrasova et al.; the present positive-far-field classification is outside that two-point example. No exhaustive priority guarantee is claimed.

## Limitations

The scalar setting is exact and does not establish an optimization failure under componentwise convexity, sign-consistent individual gradients, a vanishing clipping bias schedule, or assumptions excluding strong multiplicative noise. The deterministic basin description concerns the **expected-gradient map**, not almost-sure trajectories. The stochastic theorem establishes a strictly positive lower bound on convergence to a wrong limit, not an exact probability or behavior on the complementary event. The classification fixes distinct absolute curvatures in its three-point form; degenerate equal magnitudes can first be merged and are not asserted to create new attractors. Independent validation has not been performed.

## References

1. A. Nekrasova, M. Sidorov, S. Chezhegov, A. Gasnikov, M. Preobrazhenskaia, I. Preobrazhensky and E. Gorbunov, *Weak-\(L^\alpha\) Noise, Strong Guarantees: Gradient Clipping under Affine Heavy Tails*, arXiv:2610.28107, first public 2026-10-20, especially Appendix H.4–H.5. https://arxiv.org/abs/2610.28107
2. A. Koloskova, H. Hendrikx and S. U. Stich, *Revisiting Gradient Clipping: Stochastic bias and tight convergence guarantees*, ICML/PMLR 2023, arXiv:2305.01588, Sections 3.1 and C.5. https://arxiv.org/html/2305.01588v2
3. M. Faw, L. Rout, C. Caramanis and S. Shakkottai, *Beyond Uniform Smoothness: A Stopped Analysis of Adaptive SGD*, arXiv:2302.06570, 2023; multiplicative example described in Reference 1, Appendix H.5. https://arxiv.org/abs/2302.06570
