# Universal distant-tracer cumulants in a globally reset random average process

## Finding

Consider the continuous-time random average process (RAP) defined below, with simultaneous Poisson resetting of every particle to its initial lattice position. Put \(v=h\mu(p-q)\), and let \(Q_s\) be the one-tracer displacement law of the **reset-free** RAP at age \(s\). Although \(Q_s\) is not generally available in closed form, the entire limiting joint law of any fixed number of widely separated reset tracers is explicit in terms of its one-tracer laws:

\[
\mathcal L\bigl(Z_{i_1}(t),\ldots,Z_{i_n}(t)\bigr)
\ \xrightarrow[\min_{a\ne b}|i_a-i_b|\to\infty]{\text{weakly and in all moments}}\
 e^{-rt}Q_t^{\otimes n}+\int_0^t re^{-rs}Q_s^{\otimes n}\,ds.
\]

For the stationary state, replace the right side by \(\int_0^\infty re^{-rs}Q_s^{\otimes n}\,ds\). In particular, for every fixed integer \(n\ge2\), the connected correlation with **one insertion at each distinct tracer** has the exact universal stationary plateau

\[
\boxed{\lim_{\min_{a\ne b}|i_a-i_b|\to\infty}
\operatorname{cum}(Z_{i_1}^*,\ldots,Z_{i_n}^*)
=(n-1)!\left(\frac{v}{r}\right)^n.}
\]

The third- and fourth-order plateaus are respectively \(2(v/r)^3\) and \(6(v/r)^4\). They are independent of the full jump-fraction distribution beyond its mean \(\mu\). They vanish at zero bias and are nonzero at every order when \(v\ne0\).

At finite observation time \(t\), let \(S\sim\mathrm{Exp}(r)\) and \(A_t=\min(S,t)\). The corresponding connected plateau is exactly \(v^n\kappa_n(A_t)\), where \(\kappa_n\) denotes the ordinary univariate cumulant and

\[
\mathbb E[A_t^k]=\frac{k!}{r^k}
\left[1-e^{-rt}\sum_{j=0}^{k-1}\frac{(rt)^j}{j!}\right],\qquad k\ge1.
\]

Thus a whole hierarchy of spatially nondecaying connected correlations is fixed by the single shared resetting clock, even though the reset-free tracer's higher moments need not be known explicitly.

## Assumptions and scope

Particles are labeled by \(i\in\mathbb Z\), initially at \(X_i(0)=hi\) with \(h>0\), and their order is preserved. Independently at every label, at rate \(p\ge0\) the position is replaced by \((1-\eta)X_i+\eta X_{i+1}\), and at rate \(q\ge0\) it is replaced by \((1-\eta)X_i+\eta X_{i-1}\). Assume \(p+q<\infty\). Each update samples a fresh independent \(\eta\in[0,1)\) from a common distribution of mean \(\mu\). Independently, a single rate-\(r>0\) clock simultaneously resets all sites to \(hi\). Denote displacement by \(Z_i(t)=X_i(t)-hi\), and its stationary version by \(Z_i^*\). At finite time the process starts from the deterministic lattice. There is no finite-ring approximation in the theorem.

Limits take a **fixed** number \(n\) of distinct labels whose minimum pairwise distance diverges, at a fixed time \(t\), or in the stationary law. They do not assert uniformity as \(n\) or \(t\) grows with separation. The theorem includes the unbiased case \(p=q\), for which the stated connected plateaus are zero; it excludes \(r=0\).

## Proof

**1. The backward graphical representation and polynomial moment control.** For the reset-free system, the affine averaging rules imply that, conditional on the independent Poisson clocks and their fraction marks \(\mathcal E\), \(X_i(s)\) is a convex combination of initial lattice positions. Equivalently, run a backward ancestor from site \(i\), choosing at each encountered right/left update the neighboring ancestral site with probability \(\eta\), otherwise retaining the current ancestral site. If \(Y_s\) is the resulting ancestor label, then

\[
Z_i^{(0)}(s)=h\,\mathbb E[Y_s-i\mid\mathcal E].
\]

After averaging over the marked clock environment, the single ancestor has nearest-neighbor jump rates \(p\mu\) to the right and \(q\mu\) to the left. Its total jump count \(N_s\) is Poisson with mean \(\lambda s\), where \(\lambda=\mu(p+q)\). Consequently

\[
\mathbb E[Z_i^{(0)}(s)]=h\mu(p-q)s=vs,
\qquad
\mathbb E|Z_i^{(0)}(s)|^m\le h^m\mathbb E[N_s^m]
\]

for every integer \(m\ge1\). The upper bound is a polynomial in \(s\) of degree \(m\), so it remains integrable under an independent exponential reset age for every \(r>0\); no restriction of the form \(r>m\lambda\) is required.

**2. Locality of separated tracers.** Stop a backward ancestor upon its first exit from the label interval \([i-R,i+R]\), and use that stopped ancestor to define \(Z_i^{(0,R)}(s)\). It depends only on clock marks whose site labels lie in this interval. Exiting needs at least \(R+1\) ancestor jumps. Jensen's inequality therefore gives

\[
\mathbb E|Z_i^{(0)}(s)-Z_i^{(0,R)}(s)|^m
\le h^m\mathbb E\bigl[N_s^m\mathbf1_{\{N_s\ge R+1\}}\bigr]\longrightarrow0
\quad(R\to\infty).
\]

For fixed \(R\), any truncated tracers with pairwise label separation exceeding \(2R+1\) depend on disjoint marked Poisson environments and are independent. The polynomial moment bounds and the displayed approximation pass this factorization to the full tracers as the minimum separation tends to infinity. Thus, at each deterministic reset-free age \(s\), their joint distribution converges to \(Q_s^{\otimes n}\), with convergence of every fixed mixed moment. This proves a stronger property than vanishing pair covariances: all finite collections become jointly independent at fixed age.

**3. A common random age is the only surviving long-range dependence.** At time \(t\), the time since the last simultaneous reset has the law of \(A_t=\min(S,t)\), with an atom \(e^{-rt}\) at \(t\) and density \(re^{-rs}\) on \((0,t)\). Conditional on that age, the system has precisely the reset-free law at that elapsed time, with fresh independent clocks. The conditional product limit of Step 2 yields the stated finite-time mixture. In the stationary regime the age is \(S\sim\mathrm{Exp}(r)\), yielding the stationary mixture. Passing mixed moments through either mixture is justified by the polynomial bounds in Step 1, Hölder's inequality, and exponential integrability of every polynomial.

**4. Connected correlations.** For any subset \(B\) of the distinct indices, the limiting expectation of the product \(\prod_{j\in B}Z_{i_j}\) is \(\mathbb E[(vA_t)^{|B|}]\): condition on the common age and use independence and the mean \(vs\). A joint cumulant is the universal partition polynomial in such subset moments. Therefore it converges to the cumulant of \(n\) copies of the same scalar \(vA_t\), namely \(v^n\kappa_n(A_t)\). Stationarily, the cumulant generating function of \(vS\) near zero is

\[
-\log(1-vz/r)=\sum_{n\ge1}\frac1n(vz/r)^n,
\]

and its \(n\)-th derivative at zero is \((n-1)!(v/r)^n\). The finite-time age-moment formula follows from \(\mathbb E[A_t^k]=k\int_0^t s^{k-1}e^{-rs}\,ds\). This completes the proof.

## Verification

The standalone `checker.py` performs exact symbolic checks of the reset-age cumulant recursion through order ten, its infinite-time coefficients, the finite-time second- and third-order polynomial formulas, and the Poisson moment recursion supporting the locality bound. Finite numerical Poisson-tail checks test only the localization estimate at selected parameters; they are not substitutes for the all-time all-order argument above.

In particular, the finite-time second plateau is

\[
\frac{v^2}{r^2}\left[1-2rt\,e^{-rt}-e^{-2rt}\right],
\]

which coincides with the far-separation term in Eq. (42) of Santra--Singh after setting \(h=1\). The third plateau is

\[
\frac{v^3}{r^3}\left[2-3(rt)^2e^{-rt}-6(rt)e^{-2rt}-2e^{-3rt}\right].
\]

## Relationship to prior work

Santra and Singh [1] define the globally reset RAP and compute its mean, stationary two-tracer correlation, and unequal-time two-point functions. Their Eq. (42) supplies precisely the second-order finite-time plateau above, and Eq. (44) the stationary value \(v^2/r^2\) at unit lattice spacing; neither provides a connected \(n\)-tracer result for \(n\ge3\), a spatial conditional-product theorem, or the all-order hierarchy. Their conclusion explicitly identifies higher moments as an open direction. Rajesh and Majumdar [2] analyze reset-free RAP tracer correlations, principally second-order quantities. Biroli et al. [3] provide a joint-law renewal mixture for **independent Brownian** particles under common resetting; their independent-particle factorization is not applicable to interacting RAP tracers before the locality argument in Step 2.

The present statement adds an interacting-system spatial mixing proof plus the exact nonlinear multi-tracer plateaus, not a new derivation of the known \(n=2\) plateau. The renewal principle and the second-order formula are established inputs; an unindexed general theorem giving an equivalent higher-order conclusion would affect publication priority.

## Limitations

The conclusion concerns infinitely separated, distinctly labeled tracers in a fixed-order limit; it supplies neither the finite-distance higher cumulants nor the explicit one-tracer law \(Q_s\). In particular, it does not solve the single-tracer higher-moment problem identified in [1], and it makes no claim of uniformity in cumulant order. A finite number of particles, local rather than global reset clocks, non-Poisson resetting, random reset configurations, or spatially varying jump rules require separate arguments. Symbolic and finite numerical checks corroborate identities, not the infinite-system convergence proof. Independent publication-priority verification has not been performed.

## References

[1] S. Santra and P. Singh, *Exact fluctuation and long-range correlations in a single-file model under resetting*, arXiv:2311.04097v1 (first public 2023-11-07); Phys. Rev. E **109**, 034123 (2024). https://arxiv.org/abs/2311.04097

[2] R. Rajesh and S. N. Majumdar, *Exact Tagged Particle Correlations in the Random Average Process*, arXiv:cond-mat/0104430 (2001); Phys. Rev. E **64**, 036103 (2001). https://arxiv.org/abs/cond-mat/0104430

[3] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first public 2022-11-01); Phys. Rev. Lett. **130**, 207101 (2023). https://arxiv.org/abs/2211.00563
