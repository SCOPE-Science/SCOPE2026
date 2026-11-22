# Exact boundary-anchored contrast quadrature for the exponential kernel and its long-correlation noise crossover

## Finding
Let \(X\) be a centered, real, stationary Gaussian process on \([0,1]\) with covariance \(K(s,t)=\exp(-|s-t|/\ell)\), where \(\ell>0\). To estimate \(J=\int_0^1X(s)\,ds\), observe a **single contrast**
\[
Y_{u,v}=X(v)-X(u)+\varepsilon,\qquad 0\le u<v\le1,
\]
where \(\varepsilon\sim N(0,\eta)\) is independent and \(\eta\ge0\). The Bayes estimator is the conditional mean, and the design maximizes the reduction in posterior mean-square error.

**Theorem.** For every \(\ell>0\) and \(\eta\ge0\), the only globally optimal unordered two-location designs are
\[
\{0,d_*\}\quad\text{and}\quad\{1-d_*,1\},
\]
where \(0<d_*<1/2\). Put \(q=e^{-1/\ell}\) and \(r_*=e^{-d_*/\ell}\). Then \(r_*\) is the **unique** root in \((\sqrt q,1)\) of
\[
r(r-q)(1-r+\eta)=q(1-r)\{2(1-r)+\eta\}.
\]
Equivalently it is the sole root of
\[
\frac{1}{1-r}-\frac{1}{2(1-r)+\eta}=\frac{q}{r(r-q)}.
\]
The optimal gap \(d_*\) increases strictly with \(\eta\). At zero noise,
\[
r_*(\ell,0)=\frac{\sqrt{q^2+8q}-q}{2}.
\]
At fixed \(\ell\), as \(\eta\to\infty\),
\[
d_*(\ell,\eta)=\frac12-\frac{\ell(1-e^{-1/(2\ell)})^2}{2\eta}+O_\ell(\eta^{-2}).
\]
In the long-correlation joint limit \(\ell\to\infty\) with \(\eta=\kappa/\ell\) for fixed \(\kappa\ge0\),
\[
d_*(\ell,\kappa/\ell)\longrightarrow
D(\kappa):=\frac{1-2\kappa+\sqrt{1+8\kappa+4\kappa^2}}6,
\qquad D(0)=\frac13,\quad \lim_{\kappa\to\infty}D(\kappa)=\frac12.
\]
The maximally explained variance satisfies
\[
\max_{u<v}\operatorname{Var}(\mathbb E[J\mid Y_{u,v}])=
\frac{d_*^2(1-d_*)^2}{\ell(2d_*+\kappa)}+O_\kappa(\ell^{-2})
\]
when \(\eta=\kappa/\ell\), interpreting \(d_*=d_*(\ell,\kappa/\ell)\) in the displayed expression. In particular, for \(\kappa=0\), the leading coefficient is \(2/(27\ell)\). In contrast, the full-span observation \(X(1)-X(0)\) explains **zero** variance for this symmetric integral.

## Assumptions and scope
The process has known zero mean and unit marginal variance; the domain and integration measure are respectively \([0,1]\) and Lebesgue measure. The observation is one scalar Gaussian difference, **not** two individually available point measurements. Noise has fixed absolute variance \(\eta\) independent of the chosen gap and positions. This is one-shot nonadaptive design. Both reflection-related minimizers are allowed; reversing the sign of the recorded contrast changes no information. At coincident locations the contrast is zero, so the design uses \(u<v\).

## Proof
1. **Exact risk.** Write \(m(t)=\operatorname{Cov}(J,X(t))\). Direct integration gives
   \[
   m(t)=\ell(2-e^{-t/\ell}-e^{-(1-t)/\ell}),\qquad
   \operatorname{Var}(J)=2\ell[1-\ell(1-e^{-1/\ell})].
   \]
   The contrast variance is \(V(u,v)=2(1-e^{-(v-u)/\ell})+\eta\), and its covariance with \(J\) is \(m(v)-m(u)\). Gaussian conditioning therefore gives
   \[
   R(u,v)=\operatorname{Var}(J)-\frac{[m(v)-m(u)]^2}{V(u,v)}.
   \]
   The expression is valid for \(\eta=0\) as long as \(u<v\).
2. **Global endpoint reduction.** Since
   \(m''(t)=-[e^{-t/\ell}+e^{-(1-t)/\ell}]/\ell<0\), the function
   \(u\mapsto m(u+d)-m(u)\) is strictly decreasing for every fixed \(0<d<1\). By reflection, its values at \(u=0\) and \(u=1-d\) are opposite. Since \(V\) depends only on \(d=v-u\), maximum squared covariance at fixed gap is attained **only** by the reflected endpoint-anchored pairs. The resulting covariance magnitude is
   \[
   C(d)=m(d)-m(0)=\ell(1-e^{-d/\ell})(1-e^{-(1-d)/\ell}),
   \]
   symmetric under \(d\leftrightarrow1-d\). The denominator \(2(1-e^{-d/\ell})+\eta\) is strictly increasing in \(d\), so any \(d>1/2\) is strictly inferior to \(1-d<1/2\); \(d=1\) gives zero information.
3. **Unique global gap.** For \(d\in(0,1/2)\), put \(r=e^{-d/\ell}\) and \(q=e^{-1/\ell}\), so \(\sqrt q<r<1\). The information objective is
   \[
   I(r)=\ell^2\frac{(1-r)^2(1-q/r)^2}{2(1-r)+\eta}.
   \]
   Its logarithmic derivative vanishes precisely when
   \[
   F_\eta(r):=\frac{1}{1-r}-\frac{1}{2(1-r)+\eta}
                   -\frac{q}{r(r-q)}=0.
   \]
   The first two terms have derivative
   \(1/(1-r)^2-2/[2(1-r)+\eta]^2>0\); the final subtracted term also has strictly positive derivative. Thus \(F_\eta\) is strictly increasing. At \(r=\sqrt q\), it is negative; as \(r\uparrow1\), it tends to \(+\infty\). There is exactly one stationary point. The information tends to zero as \(d\downarrow0\) and decreases at \(d=1/2\), so the stationary point is the unique maximizer in the reduced interval. The two reflection-related designs are consequently the only global optimizers.
4. **Noise monotonicity and limits.** \(\partial_\eta F_\eta(r)=1/[2(1-r)+\eta]^2>0\); implicit differentiation and strict \(\partial_rF_\eta>0\) yield \(dr_*/d\eta<0\), so \(dd_*/d\eta>0\). At \(\eta=0\), the stationary equation reduces to \(r^2+qr-2q=0\), giving the positive root in the theorem. At fixed \(\ell\), expansion about \(d=1/2\) uses \(C'(1/2)=0\), \(C''(1/2)=-2e^{-1/(2\ell)}/\ell\), and \(V'(1/2)=2e^{-1/(2\ell)}/\ell\), giving the stated \(1/\eta\) displacement.
5. **Long-correlation crossover.** Uniformly on compact interior ranges of \(d\), for \(\eta=\kappa/\ell\),
   \[
   C(d)=\frac{d(1-d)}{\ell}+O(\ell^{-2}),\qquad
   V(d)=\frac{2d+\kappa}{\ell}+O(\ell^{-2}).
   \]
   The limiting objective is \(\ell^{-1}d^2(1-d)^2/(2d+\kappa)\). Its unique interior stationary point satisfies
   \[
   d-3d^2+\kappa(1-2d)=0,
   \]
   with the displayed positive root \(D(\kappa)\). Root convergence follows alternatively by expansion of the exact stationary equation, including \(\kappa=0\), and strict uniqueness. The information expansion follows by substitution. At \(\kappa=0,d=1/3\), the constant is \(2/27\). Finally, \(m(1)=m(0)\) implies the full-span contrast has zero covariance with \(J\), and joint Gaussianity makes it independent of \(J\).

## Verification
Run `python3 verify.py` from the extracted package. The script uses only the standard library, checks exact-formula identities against independent numerical kernel integrals, a finite global grid over arbitrary pairs, zero-noise roots, noise monotonicity, large-noise behavior, and the long-correlation crossover. Its deterministic execution returned `PASS 20666 supplementary exact-formula, optimality-grid, integral and scaling checks`. These finite tests do **not** certify the continuum optimization; steps 1–5 above provide the proof.

For example, when \(\ell=1\), the optimal half-gap is \(d_*(1,0)\approx0.366257\) without noise and \(d_*(1,1)\approx0.453519\) at noise variance one. All parameters are dimensionless after normalizing the observation interval to length one and the pointwise prior variance to one.

## Relationship to prior work
Gaussian-process conditioning on linear functionals and posterior integral variance are established methods; the covariance-to-risk identity is not new. Wu, Aoi and Pillow (2017) discuss derivative-enhanced Bayesian quadrature. Karvonen, Kanagawa and Särkkä (2018) analyze weights and optimality for point-value Bayesian quadrature and discuss derivative information. Longi et al. (2020) optimize sensor locations for **line-integral** observations, with general Gaussian linear-operator tools. Pronzato and Zhigljavsky (2020) develop kernel-energy and design links. These sources motivate the present question, but their examined statements do not provide the globally optimal **single two-point contrast** for the exponential kernel or the explicit \(\eta\ell\) crossover. Individually observing \(X(u)\) and \(X(v)\) is a strictly different information experiment from receiving only their noisy difference. Earlier optimal exponential-kernel point-sampling designs similarly do not imply this one-contrast placement theorem. Literature priority beyond the inspected sources is not established.

## Limitations
This is a prior-model Bayes-design theorem, not a worst-case quadrature guarantee. It assumes the exact stationary exponential covariance, known correlation length, symmetric integration weight, a known zero mean, and fixed independent Gaussian contrast-noise variance. It does not cover nonstationary OU initializations, general kernels or weights, individually recorded endpoint values, variable gap-dependent sensing cost, multiple contrasts, adaptive selection, or unknown nuisance offsets in the target. The result is not independently audited; the original-source search was bounded and does not prove literature uniqueness.

## References
- A. Wu, M. C. Aoi, and J. W. Pillow (2017), *Exploiting gradients and Hessians in Bayesian optimization and Bayesian quadrature*, arXiv:1704.00060, v1 2017-03-31. https://arxiv.org/abs/1704.00060
- T. Karvonen, M. Kanagawa, and S. Särkkä (2018), *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, v1 2018-12-20. https://arxiv.org/abs/1812.08509
- K. Longi et al. (2020), *Sensor Placement for Spatial Gaussian Processes with Integral Observations*, PMLR 124:1009–1018. https://proceedings.mlr.press/v124/longi20a.html
- L. Pronzato and A. Zhigljavsky (2020), *Bayesian quadrature, energy minimization, and space-filling design*, SIAM/ASA Journal on Uncertainty Quantification 8, 959–1011. https://doi.org/10.1137/18M1210332
- T. Traverso et al. (2023), *Data-driven modeling for drop size distributions*, Physical Review Fluids 8, 104302. https://doi.org/10.1103/PhysRevFluids.8.104302
