# A universal reset-rate floor and a center-to-shell transition for Student-type harmonic steady states

## Finding

A harmonic diffusion with independent complete Poisson resets can have the genuinely heavy-tailed, centered Pearson--VII stationary density
\[
p_a(x)=\frac{\Gamma(\nu)}{\pi^{d/2}a^d\Gamma(\nu-d/2)}\left(1+\frac{\|x\|^2}{a^2}\right)^{-\nu},\qquad \nu>\frac d2.
\]
The set of feasible reset rates is an exact half-line. Write
\[
\lambda=\frac{D}{\kappa a^2},\quad \lambda_c=\frac1{2\nu+d+2},\quad b=2\nu+2-d>0.
\]
Then a probability law for the reset position producing exactly \(p_a\) exists **if and only if**
\[
r\ge r_{\min}(a):=\kappa\begin{cases}
d(1-2\nu\lambda),&0<\lambda\le\lambda_c,\\
d-2\nu+\dfrac{\nu(1+b\lambda)^2}{4(\nu+1)\lambda},&\lambda>\lambda_c.
\end{cases}
\]
The source is unique. At the boundary \(r=r_{\min}(a)\), it vanishes quadratically at the origin if \(\lambda<\lambda_c\), quartically at the origin if \(\lambda=\lambda_c\), and quadratically in radial distance on a nonzero-radius sphere if \(\lambda>\lambda_c\). For strictly larger \(r\), its density is strictly positive.

If the scale \(a\) may be selected, there is a second **sharp global feasibility limit**:
\[
\min_{a>0}r_{\min}(a)=\frac{\kappa d}{\nu+1},\quad
 a_{\rm opt}^2=\frac{D(2\nu+2-d)}{\kappa},\quad
 \|x\|_{\rm zero}=\sqrt{\frac{dD}{\kappa}}
\]
with a unique optimal scale. The zero-sphere radius is independent of the heavy-tail exponent. No reset distribution or target scale in this Pearson--VII family can attain a rate below the displayed global limit.

## Assumptions and scope

Fix an integer \(d\ge1\), \(\kappa,D,a,r>0\), and \(\nu>d/2\). Between resets the entire position vector follows
\[
dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t.
\]
At times of an independent Poisson process of rate \(r\), replace the entire position by a fresh draw from a fixed Borel probability law \(q\), independent of the trajectory and previous reset draws. No moment assumption is made on the reset law. The stationary statement concerns the one-time law, not Gaussianity of sample paths or detailed balance.

Set \(s(x)=(1+\|x\|^2/a^2)^{-1}\in(0,1]\). Denote the OU forward generator by \(L^*p=\kappa\nabla\cdot(xp)+D\Delta p\).

## Proof

**1. The uniquely forced source.** Every stationary target density \(p\) satisfies the distributional equation \(0=L^*p-rp+rq\). Thus any source for \(p_a\) must be absolutely continuous, with density
\[
q_r(x)=p_a(x)\left[1-\frac{\kappa}{r}f(s(x))\right],\qquad
f(s)=d-2\nu+2\nu(1+b\lambda)s-4\lambda\nu(\nu+1)s^2.
\]
Indeed, differentiation using \(z=\|x\|^2/a^2\) gives
\[
\frac{\nabla\cdot(xp_a)}{p_a}=d-\frac{2\nu z}{1+z},\qquad
\frac{\Delta p_a}{p_a}=-\frac{2\nu d}{a^2(1+z)}+\frac{4\nu(\nu+1)z}{a^2(1+z)^2},
\]
which yields \(L^*p_a/(\kappa p_a)=f(s)\). There can be no other resetting law, including singular alternatives.

**2. Source normalization without moments.** The density \(p_a\) is integrable because \(\nu>d/2\). The radial surface flux of \(\kappa xp_a+D\nabla p_a\) at radius \(R\) is of order \(R^{d-2\nu}\), hence vanishes at infinity; it also vanishes at the origin. Consequently \(\int_{\mathbb R^d}L^*p_a\,dx=0\), so \(\int q_r\,dx=1\) for every real \(r>0\) for which the formula defines a nonnegative density. Equivalently, under \(p_a\), \(s(X)\) has Beta parameters \(\nu-d/2,d/2\), and substitution of its first two moments gives \(\mathbb E[f(s(X))]=0\). This remains valid for targets with infinite second moment.

**3. Exact rate and zero-set classification.** Since \(p_a>0\), nonnegativity of \(q_r\) is equivalent to \(r/\kappa\ge\sup_{0<s\le1} f(s)\). The polynomial \(f\) is strictly concave; its vertex is
\[
s_* =\frac{1+b\lambda}{4\lambda(\nu+1)}>0.
\]
For \(\lambda\le\lambda_c\), one has \(s_*\ge1\) and the maximum occurs at \(s=1\), giving \(f(1)=d(1-2\nu\lambda)\). For \(\lambda>\lambda_c\), \(0<s_*<1\) and the maximum occurs at \(s_*\), giving \(f(s_*)=d-2\nu+\nu(1+b\lambda)^2/[4\lambda(\nu+1)]\). These maxima are strictly positive: the continuous nonconstant function \(f(s(X))\) has mean zero and full support in \(s\in(0,1)\).

At the rate equality, the exact positive factor is proportional to \(f(s_*)-f(s)\). If \(\lambda<\lambda_c\), \(f'(1)>0\) and \(1-s\sim\|x\|^2/a^2\), so \(q_r/p_a\) has a quadratic zero at \(x=0\). When \(\lambda=\lambda_c\), \(f'(1)=0\), and \(f(1)-f(s)=4\lambda\nu(\nu+1)(1-s)^2\), yielding a quartic zero at the origin. For \(\lambda>\lambda_c\), \(f(s_*)-f(s)=4\lambda\nu(\nu+1)(s-s_*)^2\), yielding a quadratic radial zero on the sphere
\[
\|x\|=a\sqrt{\frac{4\lambda(\nu+1)}{1+b\lambda}-1}.
\]
For \(r>r_{\min}(a)\), strict positivity follows immediately.

**4. Global optimization over target scales.** The first branch of \(r_{\min}(a)/\kappa\) is strictly decreasing in \(\lambda\). On the second branch,
\[
\frac{d}{d\lambda}\left(\frac{r_{\min}}{\kappa}\right)
=\frac{\nu}{4(\nu+1)}\left(b^2-\frac1{\lambda^2}\right).
\]
Since \(1/b>\lambda_c\), its unique global minimizer is \(\lambda_*=1/b\). At this point the maximum equals \(d/(\nu+1)\), the physical target width is \(a^2=Db/\kappa\), and the zero sphere has squared radius
\[
 a^2\left(\frac1{s_*}-1\right)=\frac{dD}{\kappa}.
\]
In particular, this radius is independent of \(\nu\). This proves the global attainability statement and the uniqueness of the minimizing scale.

**5. Stationarity and uniqueness.** For every nonnegative normalized \(q_r\), the reset process has invariant distribution \(\pi=r\int_0^\infty e^{-rt}q_rP_t\,dt\), where \(P_t\) is the OU Markov semigroup. It is invariant by the renewal construction; the preceding differential identity shows \(p_a\) is invariant. Two processes coupled to use the same first reset time, draw and subsequent Brownian path agree after that reset, so the invariant probability is unique and convergence is at least as fast as \(e^{-rt}\) in total variation. Conversely, if the forced source is negative anywhere, no positive measure can produce this target. The target tail is polynomial for every \(\nu>d/2\), including \(d/2<\nu\le(d+2)/2\), when its second moment is infinite.

## Verification

The standalone `CHECK.py` independently differentiates the target, checks the Beta normalization identity, reduces the concave-quadratic maximum, tests the critical quartic zero and the unique global shape optimum, and evaluates 1,875 exact-rational radial inequalities for representative parameter sets. Its asserted results match the displayed analytic proof. The finite checks are reproducibility support, not a substitute for the all-dimension statements.

## Relationship to prior work

Olsen, *Steady-state moments under resetting to a distribution* (arXiv:2310.04840, 2023), supplies the forward renewal framework and arbitrary-order stationary moments for harmonic diffusion with distributed resets; these are antecedents, not new claims. The related Gaussian inverse problem was also solved in *Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets* (published-finding corpus finding `08050fc52754`, 2026). The present theorem concerns a different prescribed, non-Gaussian heavy-tailed law, including the infinite-variance regime, and establishes the **explicit family-wide fixed-scale and optimized-scale attainability boundaries and center-to-sphere transition**. Neither cited antecedent directly states those Pearson--VII boundaries. Trajanovski et al. (arXiv:2301.12304, 2023) study OU resetting and comb geometry, but not this inverse heavy-tailed reset-source classification.

## Limitations

This result assumes complete state-independent Poisson resets, isotropic OU drift and diffusion, and the exact Pearson--VII target family. It does not optimize a physical reset-energy cost, establish finite-sample inference, or classify arbitrary nonradial heavy-tailed targets. The inverse forward equation is standard; the claimed addition is the exact sharp parameter, zero-set, and global scale classification. Broader unpublished or implicit results may affect publication priority. Independent scientific audit has not been performed.

## References

- K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first public version 7 October 2023), https://arxiv.org/abs/2310.04840.
- Ž. Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: Particle dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304 (2023), https://arxiv.org/abs/2301.12304.
- *Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets*, published-finding corpus finding `08050fc52754` (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-gaussian-stationary-state-engineering-by-non-gaussian-stoc--08050fc52754.
