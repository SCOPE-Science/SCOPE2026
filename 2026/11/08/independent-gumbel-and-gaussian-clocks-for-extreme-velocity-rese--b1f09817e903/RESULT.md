# Independent Gumbel and Gaussian clocks for extreme velocity-reset Brownian flights

## Finding

Consider a particle whose **velocity alone** is reset to zero at Poisson times, while its position is continuous and never reset. Let \(D,r>0\). With the definitions in the next section, set
\[
 k=\left(\frac{9}{4Dr}\right)^{1/4},\qquad
 c=\frac{4r}{3}k,\qquad A=\sqrt{\frac32},\qquad
 b_t=\log(Art).
\]
For the largest absolute **completed-flight displacement** \(M_t\), and the reset-free duration \(L_t^*\) of that record flight, the joint limit is
\[
 \boxed{\left(c\sqrt{M_t}-b_t,\;\frac{4rL_t^*-3b_t}{\sqrt{3b_t}}\right)
 \ \Longrightarrow\ (G,Z),}
\]
where \(\Pr(G\le y)=\exp(-e^{-y})\), \(Z\) has standard normal law, and \(G\) and \(Z\) are independent. Thus the record flight has displacement of order \((\log t)^2\) and duration \(3\log t/(4r)\) with fluctuations of order \(\sqrt{\log t}/r\). Neither the Gaussian limit nor its duration normalization involves \(D\).

An intermediate, more local joint result is the conditional-duration theorem for a single flight. For \(J\) and \(L\) defined below, put \(\ell_x=k\sqrt x\). Then
\[
 \Pr(|J|>x)\sim A e^{-c\sqrt x},\qquad
 \mathcal L\left(\left.\frac{L-\ell_x}{\sqrt{\ell_x/(4r)}}\ \right|\ |J|>x\right)
 \Longrightarrow N(0,1)\quad(x\to\infty).
\]
The one-flight area density and its leading tail are known from Meerson's 2019 calculation; the contributions here are the conditional duration limit and the **joint marked extreme law over physical observation time**, with its explicit centering and asymptotic independence.

## Assumptions and scope

Let \(B_t\) be standard one-dimensional Brownian motion, independent of a rate-\(r\) Poisson clock with jump times \(0=S_0<S_1<S_2<\cdots\). On each interval \([S_{i-1},S_i)\), velocity evolves according to \(dV_s=\sqrt{2D}\,dB_s\), restarted at \(V_{S_{i-1}}=0\), and position follows \(dX_s=V_s\,ds\) without positional resets. This is the frictionless, zero-drift, zero-reset-velocity specialization of velocity-only resetting. Define
\[
 L_i=S_i-S_{i-1},\qquad
 J_i=X_{S_i}-X_{S_{i-1}}=\sqrt{2D}\int_0^{L_i} B_u^{(i)}\,du.
\]
The pairs \((L_i,J_i)\) are independent and identically distributed, \(L_i\sim\mathrm{Exp}(r)\), and
\[
 J_i\mid L_i=\ell\ \sim N\!\left(0,\frac{2D}{3}\ell^3\right).
\]
For \(t>0\) let \(N_t=\max\{i:S_i\le t\}\), \(M_t=\max_{1\le i\le N_t}|J_i|\), and let \(I_t\) be the almost surely unique index attaining the maximum, with \(L_t^*=L_{I_t}\). On the event \(N_t=0\), of probability \(e^{-rt}\), set \(M_t=L_t^*=0\). The statement concerns **end-to-end cycle displacements**, not the largest instantaneous position and not the maximum within a cycle. All limits are as \(t\to\infty\) with \(D,r\) fixed, or as \(x\to\infty\) for one cycle.

## Proof

**1. One-cycle law and saddle.** Brownian integration gives \(\operatorname{Var}(\int_0^\ell B_s\,ds)=\ell^3/3\), hence for \(x>0\)
\[
 p(x)=\Pr(|J|>x)
 =\int_0^\infty r e^{-r\ell}
 \operatorname{erfc}\!\left(\frac{x}{\sqrt{4D\ell^3/3}}\right)d\ell.
\]
Introduce \(f_x(\ell)=r\ell+3x^2/(4D\ell^3)\). Its unique minimizer and curvature are
\[
 \ell_x=k\sqrt x,\quad f_x(\ell_x)=c\sqrt x,\quad
 f_x''(\ell_x)=\frac{4r}{\ell_x}.
\]
The Gaussian survival (Mills) expansion, uniformly in a relatively shrinking neighborhood of \(\ell_x\), yields
\[
 r e^{-r\ell}\operatorname{erfc}\!\left(\frac{x}{\sqrt{4D\ell^3/3}}\right)
 =\frac{r\sqrt{4D/3}\,\ell^{3/2}}{\sqrt\pi\,x}
 e^{-f_x(\ell)}(1+o(1)).
\]
Set \(w_x=\sqrt{\ell_x/(4r)}\). For every fixed \(z\), Taylor's formula gives \(f_x(\ell_x+w_xz)-f_x(\ell_x)\to z^2/2\), and the prefactor ratio to its value at \(\ell_x\) tends to one. Laplace's method, with tightness obtained from the strict growth of \(f_x\) away from its unique minimum and the elementary Gaussian-tail bound, gives
\[
 p(x)\sim \frac{r\sqrt{4D/3}\,\ell_x^{3/2}}{\sqrt\pi\,x}
 \sqrt{\frac{2\pi\ell_x}{4r}} e^{-c\sqrt x}
 =\sqrt{\frac32}\,e^{-c\sqrt x}.
\]
The same normalized integral restricted to \(\ell\le\ell_x+z w_x\) tends to \(\Phi(z)\), proving the conditional Gaussian assertion. The exponent and leading prefactor agree with the existing mortal-Brownian-area calculation; only the restriction by lifetime is used to produce the additional conditional limit here.

**2. A marked extreme point process for a deterministic sample.** For deterministic \(n\to\infty\), let
\[
 Y_i=c\sqrt{|J_i|},\quad b_n=\log(An),\quad
 Z_{i,n}=\frac{4rL_i-3b_n}{\sqrt{3b_n}}.
\]
The preceding asymptotics imply for every fixed \(y,z\in\mathbb R\)
\[
 n\Pr(Y_i>b_n+y,\ Z_{i,n}\le z)\longrightarrow e^{-y}\Phi(z).
\]
Indeed set \(x_n(y)=((b_n+y)/c)^2\). Then \(\ell_{x_n(y)}=3(b_n+y)/(4r)\), while \(w_{x_n(y)}=\sqrt{3(b_n+y)}/(4r)\); consequently the conditional normal scaling of \(L_i\) coincides with \(Z_{i,n}\), up to an \(o(1)\) shift and multiplicative error. The unmarked exceedance has limit \(n\Pr(Y_i>b_n+y)\to e^{-y}\). This identifies, on any upper-truncated region, the limiting independent Poisson point process of pairs \((Y_i-b_n,Z_{i,n})\) with intensity \(e^{-y}\,dy\,\varphi(z)\,dz\). To see this without requiring a general theorem, use independence of the \(n\) pairs to evaluate generating functions of counts in disjoint rectangles: each has probability \(O(1/n)\), so the multinomial generating function tends to the product of Poisson generating functions. Approximation by rectangles and the exponential upper-tail bound give the asserted point process convergence. Its largest \(y\)-coordinate is Gumbel and its associated independent normal mark is standard Gaussian. The continuous joint law rules out ties.

**3. Transfer to observation time.** The number of completed flights is \(N_t\sim\mathrm{Poisson}(rt)\), although it is correlated with the \(L_i\) marks. For fixed \(\varepsilon\in(0,1)\), set \(n_-(t)=\lfloor (1-\varepsilon)rt\rfloor\), \(n_+(t)=\lceil(1+\varepsilon)rt\rceil\). By the Poisson law of large numbers, \(\Pr(n_-\le N_t\le n_+)\to1\). For the *infinite iid ordered sequence of pairs* \((L_i,J_i)\), the continuous exchangeable values \(|J_i|\) have a unique maximum among the first \(n_+\), whose maximizing index is uniform on \(\{1,\ldots,n_+\}\). Therefore the probability that the maxima and attached marks of the first \(n_-\) and first \(n_+\) differ equals \((n_+-n_-)/n_+\), tending to \(2\varepsilon/(1+\varepsilon)\). On the event \(n_-\le N_t\le n_+\) and equality of these two records, the record from the random count \(N_t\) is the same marked pair. Letting first \(t\to\infty\) then \(\varepsilon\downarrow0\) proves a vanishing coupling discrepancy. Replacing \(b_{n_-}\) by \(b_t=\log(Art)\) changes the Gumbel coordinate by \(\log(1-\varepsilon)+o(1)\) and the standardized mark by \(O(\varepsilon\sqrt{\log t})\) if \(\varepsilon\) were fixed; to avoid this nonuniformity, take \(\varepsilon_t=(rt)^{-1/4}\), for which Poisson concentration still yields \(\Pr(n_-\le N_t\le n_+)\to1\), the discrepancy probability is \(O(\varepsilon_t)\to0\), and \(b_{n_-}-b_t=O(\varepsilon_t)=o(1/\sqrt{b_t})\). The jointly normalized records therefore have the claimed limit.

**4. Scale comparison.** An iid completed-flight increment has \(\mathbb E[J_i]=0\) and \(\mathbb E[J_i^2]=(2D/3)\mathbb E[L_i^3]=4D/r^3\). By renewal-reward variance scaling (or the existing velocity-reset model's moment calculation), \(\operatorname{Var}(X_t)\sim4Dt/r^2\). In contrast, the largest completed-flight absolute increment has \(M_t=(b_t+O_{\Pr}(1))^2/c^2\), with its duration as stated; the distinction is between a bulk diffusive scale and extreme completed-flight scale, not a claim about the maximum of the full position trajectory.

## Verification

Run `python verify.py` with Python 3 and the `sympy` and `scipy` packages. The checker symbolically verifies the saddle, curvature, rate, prefactor and Gaussian length normalization; it evaluates the exact one-flight integral for several diffusivities, rates and thresholds, checks the normal conditional-length approximation, and checks finite-sample Gumbel exceedance intensities. These numerical computations are **diagnostics**, not proofs of the limits. The proof is the saddle analysis, rare marked multinomial limit and random-count coupling above.

## Relationship to prior work

Olsen and Löwen, *Dynamics of inertial particles under velocity resetting* (arXiv:2401.12685, first publicly posted January 23, 2024), give the specific velocity-only resetting model and describe its typical transport and propagator moments; their paper does not formulate completed-flight extreme-duration limits. Meerson, *Mortal Brownian motion: three short stories* (arXiv:1903.03963), derives the exact area-at-exponential-death density and its tail including the leading prefactor, which are treated here as **known** and used as an input, not claimed new. Smith and Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting* (arXiv:2202.03546), analyze long-time distributions of sums of these areas, including an optimal single-long-cycle mechanism, but do not state the independent joint Gumbel/normal law for the largest individual area and its duration. Singh and Pal, *Extremal statistics for stochastic resetting systems* (arXiv:2102.07111), study the maximum **position** and when it is attained in systems including position-reset random acceleration; these are different observables and dynamics from the velocity-only-reset **end-to-end flight displacement** and its **duration** here. Hartmann, Majumdar and Schehr, *The distribution of the maximum of independent resetting Brownian motions* (arXiv:2309.17432), likewise concern maxima of resetting trajectories, rather than these marked increments.

## Limitations

The result assumes independent Poisson velocity resets, Brownian acceleration without friction or drift, unaltered position at resets, and fixed strictly positive \(D,r\). The maximum is over *completed-flight displacement magnitudes*, not partial-flight extrema, instantaneous absolute position, or the entire net displacement. Only weak limiting laws are asserted: no finite-time error bounds, estimation guarantees, or universal result for non-exponential reset intervals is proved. The Gumbel marginal follows established iid extreme-value methods once the already-known area tail is inserted; novelty is claimed for the fully normalized **joint** marked limit and its transfer to the physical renewal clock. A broader unindexed marked-renewal theorem might imply this specialization and requires independent priority assessment.

## References

1. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (2024), https://arxiv.org/abs/2401.12685 .
2. B. Meerson, *Mortal Brownian motion: three short stories*, arXiv:1903.03963 (2019), https://arxiv.org/abs/1903.03963 .
3. N. R. Smith and S. N. Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting*, arXiv:2202.03546 (2022), https://arxiv.org/abs/2202.03546 .
4. P. Singh and A. Pal, *Extremal statistics for stochastic resetting systems*, arXiv:2102.07111 (2021), https://arxiv.org/abs/2102.07111 .
5. A. K. Hartmann, S. N. Majumdar and G. Schehr, *The distribution of the maximum of independent resetting Brownian motions*, arXiv:2309.17432 (2023), https://arxiv.org/abs/2309.17432 .
