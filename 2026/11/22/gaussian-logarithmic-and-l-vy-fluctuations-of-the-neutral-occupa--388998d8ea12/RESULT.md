# Gaussian, logarithmic, and Lévy fluctuations of the neutral-occupation Poisson family

## Finding
Let \(0<\alpha<1\), \(r=1/\alpha>1\), and \(\beta>0\). Let \(N_\beta\) be a Poisson random measure on \((0,\infty)^2\) with intensity
\[
\beta\frac{dv}{v}\,r(1+w)^{-r-1}\,dw.
\]
Define the increasing additive process, with its almost-surely convergent Poisson integral,
\[
Z_\beta(t)=\frac{r-1}{\beta}\int_{(0,t^\alpha]\times(0,\infty)}vw\,N_\beta(dv,dw),\qquad t\ge0.
\]
Then \(\mathbb EZ_\beta(t)=t^\alpha\). For each fixed \(T>0\), as \(\beta\to\infty\) the following weak limits hold in \(D([0,T])\) with the Skorokhod \(J_1\) topology:

**Finite-second-moment regime \(0<\alpha<1/2\) (\(r>2\)).**
\[
\sqrt\beta\bigl(Z_\beta(t)-t^\alpha\bigr)
\ \Longrightarrow\ \sqrt{\frac{r-1}{r-2}}\,B(t^{2\alpha}).
\]

**Critical regime \(\alpha=1/2\) (\(r=2\)).**
\[
\sqrt{\frac\beta{\log\beta}}\bigl(Z_\beta(t)-\sqrt t\bigr)
\ \Longrightarrow\ \frac1{\sqrt2}\,B(t).
\]

**Infinite-second-moment regime \(1/2<\alpha<1\) (\(1<r<2\)).**
\[
\beta^{1-1/r}\bigl(Z_\beta(t)-t^\alpha\bigr)
\ \Longrightarrow\ (r-1)L_r(t),
\]
where \(B\) is standard Brownian motion and \(L_r\) is the mean-zero, spectrally positive, strictly \(r\)-stable Lévy process with Lévy measure
\[
\mathbf1_{\{y>0\}}\,dt\,y^{-r-1}\,dy
\]
and characteristic exponent
\[
\mathbb E e^{iuL_r(t)}=\exp\!\left[t\int_0^\infty(e^{iuy}-1-iuy)y^{-r-1}\,dy\right]
=\exp\bigl[t\Gamma(-r)(-iu)^r\bigr].
\]
In particular, the centered limit has **stationary increments in physical time** for \(\alpha\ge1/2\), but the Gaussian clock is \(t^{2\alpha}\) for \(\alpha<1/2\). The complete transition, its logarithmic normalization, and its universal stable clock arise in the high-intensity limit of the explicit neutral-occupation additive process in Wang's 2026 intermittent-map theorem.

## Assumptions and scope
The statement concerns the *Poisson limiting process family* \(Z_\beta\), not a joint limit in which an intermittent-map observation horizon and the intensity simultaneously vary. The Poisson random measure has infinitely many points near \(v=0\); nonetheless its integral exists because \(\mathbb EW=1/(r-1)<\infty\). All limits hold for fixed \(\alpha\) and fixed finite \(T\), from \(t=0\) to \(T\). At \(\beta=1\) logarithmic normalization is not used, only \(\beta\to\infty\).

The parameter corresponds to the random- or single-map neutral occupation law in [1]: \(\beta=\ell\bar c/\alpha\), after changing the original Poisson time \(s\) to \(v=s^\alpha\). The cited source proves the finite-intensity occupation limit and the unscaled deterministic endpoint, not the fluctuation theorem above.

## Proof
**1. First moments and independent increments.** The mark \(W\) has density \(r(1+w)^{-r-1}\) and tail \(\mathbb P(W>w)=(1+w)^{-r}\), whence \(\mathbb EW=1/(r-1)\). Campbell's formula yields \(\mathbb EZ_\beta(t)=(r-1)\int_0^{t^\alpha}\mathbb EW\,dv=t^\alpha\). Disjoint physical-time intervals correspond to disjoint \(v\)-intervals and therefore have independent increments. Centered processes are càdlàg martingales on each bounded interval; their jumps are nonnegative although their centering drifts down.

**2. Gaussian regime.** If \(r>2\), then \(\mathbb EW^2=2/((r-1)(r-2))\). The deterministic predictable quadratic variation of \(\sqrt\beta(Z_\beta-t^\alpha)\) on \([0,t]\) is exactly
\[
(r-1)^2\int_0^{t^\alpha}v\,\mathbb EW^2\,dv
=\frac{r-1}{r-2}t^{2\alpha}.
\]
For each \(\varepsilon>0\), the Lindeberg integral is bounded by a constant times \(\int_0^{T^\alpha}v\,\mathbb E[W^2\mathbf1_{\{W>\varepsilon\sqrt\beta/((r-1)v)\}}]dv\), which tends to zero by dominated convergence and \(\mathbb EW^2<\infty\). The martingale functional central limit theorem gives the stated Brownian time-change in \(J_1\).

**3. Logarithmic boundary.** Take \(r=2\), \(V=\sqrt T\), and \(b_\beta=\sqrt{\beta\log\beta}\). By the exact tail-integration identity
\[
\mathbb E[W^2\mathbf1_{\{W\le u\}}]
=2\left[\log(1+u)+\frac1{1+u}-1\right]-\frac{u^2}{(1+u)^2}
=2\log u+O(1)\quad (u\to\infty),
\]
the predictable quadratic variation, restricted to jumps \(vw\le b_\beta\), of \(\sqrt{\beta/\log\beta}(Z_\beta-\mathbb EZ_\beta)\) converges uniformly on \([0,T]\) to \(t/2\): explicitly it equals
\[
\frac1{\log\beta}\int_0^{\sqrt t}
v\,\mathbb E[W^2\mathbf1_{\{W\le b_\beta/v\}}]dv
=\frac{t\log b_\beta}{\log\beta}+O_T((\log\beta)^{-1})\to\frac t2.
\]
For every \(\varepsilon>0\), the intensity of jumps satisfying \(vw>\varepsilon b_\beta\) on the whole time interval is at most \(\beta V^2/(2\varepsilon^2 b_\beta^2)=O_T((\log\beta)^{-1})\). Their mean contribution in the displayed normalization is at most \(O_T((\log\beta)^{-1})\), obtained from the tail bound \(\mathbb E[W\mathbf1_{\{W>u\}}]=O(u^{-1})\). Thus after removing asymptotically absent large jumps and their negligible compensator, the truncated compensated martingale has the stated quadratic variation and the Lindeberg condition; its functional limit is \(B(t)/\sqrt2\). To see Lindeberg directly, fix \(0<\varepsilon<1\): the variance contribution from marks between \(\varepsilon b_\beta\) and \(b_\beta\) is \(O_T(\log(1/\varepsilon)/\log\beta)\). The monotone tightness of the quadratic-variation clocks and the vanishing maximal jumps complete the \(J_1\) argument.

**4. Stable regime and the exact physical-time density.** Let \(1<r<2\) and consider the centered process divided by \(r-1\). Its positive jump at physical time \(t\) has size \(y=\beta^{-1/r}t^\alpha W\). Changing variables in the defining Poisson intensity gives the **exact** time/size Lévy density
\[
\nu_{\beta}(dt,dy)
=\frac{dt\,dy}{y^{r+1}}
\left(1+\frac{t^\alpha}{\beta^{1/r}y}\right)^{-r-1},\qquad t,y>0.
\]
This identity uses \(r\alpha=1\), rather than an asymptotic approximation. On every rectangle bounded away from \(y=0\), the density converges to \(dt\,y^{-r-1}dy\), and for all \(\beta,t,y\) it is dominated by that limit. For \(\varepsilon>0\), big-jump point processes and their centered cumulative sums therefore converge on \([0,T]\) in \(J_1\), by Poisson point-process convergence. For small jumps the centered martingales satisfy uniformly
\[
\mathbb E\sup_{t\le T}\left|M_{\beta,\le\varepsilon}(t)\right|^2
\le4T\int_0^\varepsilon y^2y^{-r-1}dy
=\frac{4T}{2-r}\varepsilon^{2-r},
\]
by Doob's inequality, and the same holds for the limiting compensated stable small jumps. Letting \(\varepsilon\downarrow0\) completes the converging-together argument for the full centered processes. The limiting compensated Poisson integral is the specified mean-zero \(r\)-stable Lévy motion. Its intensity is independent of \(t\), proving stationary increments and identifying the exact normalization.

## Verification
The standalone `check_fluctuations.py` checks finite-second-moment means and quadratic variations for multiple parameters, the critical truncated-second-moment identity, and 216 exact-formula-to-Jacobian numerical comparisons for the stable Lévy kernel. It passed 271 checks with the dependencies identified in the file. These finite arithmetic checks do **not** establish process-level weak convergence; that follows from the proofs above. Reproduce with `python check_fluctuations.py` using Python 3 and SciPy.

## Relationship to prior work
Wang [1], Theorem 1.4 and its proof, constructs precisely the additive Poisson family after the time substitution \(v=s^\alpha\), and states \(Z_\infty(t)=t^\alpha\); it does not give these three centered functional high-intensity limits or the exact physical-time stable Lévy kernel. Pitman and You [2], Section 4, establish the general scale-invariant hold-jump construction of self-similar additive processes; the general representation underlies the process but does not state the sharp three-regime fluctuation classification for Wang's Lomax marks. Sera [3] concerns infinite-ergodic occupation functional limits in a different fixed-process asymptotic and does not compute this particular high-intensity family. The proof uses classical martingale functional central-limit and Poisson-jump convergence tools, not a new general limit theorem for arbitrary Poisson integrals.

## Limitations
These are **iterated-limit-level** statements about the exact Poisson family, not justified by Wang's finite-intensity convergence uniformly as \(\beta\to\infty\). No interchange with the original map observation horizon is claimed. The structural result is model-specific and the general probability limit methods are standard. Historical priority for an equivalent already-worked-out specialized self-similar additive process is not independently certified. Both fluctuation scale and limiting process change when \(\alpha\) crosses \(1/2\); no joint near-critical \(\alpha=\alpha_\beta\) asymptotic is asserted.

## References
[1] Q. Wang, *Strong Borel–Cantelli laws and clusters of visits for random intermittent maps*, arXiv:2611.03010 (2026), Theorem 1.4, especially equation (2), the commentary after (3), and Section 8.8. Preprint version 4 publicly dated 2026-10-25 at https://zenodo.org/records/23633079 ; https://arxiv.org/abs/2611.03010 .

[2] J. Pitman and Z. You, *The range of a self-similar additive gamma process is a scale invariant Poisson point process*, arXiv:2111.09409 (2021/2022), Section 4 (scale-invariant hold-jump construction); https://arxiv.org/abs/2111.09409 .

[3] T. Sera, *Functional limit theorem for occupation time processes of intermittent maps*, Nonlinearity 33 (2020), 1183–1217; https://arxiv.org/abs/1810.04571 .
