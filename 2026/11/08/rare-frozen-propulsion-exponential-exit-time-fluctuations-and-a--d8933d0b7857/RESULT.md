# Rare frozen propulsion, exponential exit-time fluctuations, and a restart reversal

## Finding

Fix \(D,L>0\) and \(0<x\leq L\). Consider a Brownian searcher in \([0,L]\), absorbed at \(0\) and normally reflected at \(L\), whose velocity \(V\) is sampled once per attempt from \(N(0,\sigma^2)\) and then held constant. Let \(T_\sigma\) be the first absorption time in an unreset attempt and \(M_j(\sigma)=\mathbb E[T_\sigma^j]\). For every \(\sigma\geq0\), these moments are finite. As \(\sigma\to\infty\),

\[
M_1(\sigma)\sim \frac{D^3}{\sigma^4L^2}\exp\!\left(\frac{\sigma^2L^2}{2D^2}\right),\qquad
M_2(\sigma)\sim \frac{D^6}{8\sigma^8L^4}\exp\!\left(\frac{2\sigma^2L^2}{D^2}\right),
\]

and hence

\[
\frac{M_2(\sigma)}{M_1(\sigma)^2}\sim\frac18\exp\!\left(\frac{\sigma^2L^2}{D^2}\right).
\]

In particular, the mean increases strictly with \(\sigma>0\), and the first two moments are increasingly dominated by rare strongly outward velocities. More precisely, under the probability law that weights a sampled velocity \(v\) by the conditional moment \(\mathbb E[T_\sigma^j\mid V=v]\) for \(j=1,2\),

\[
\frac{V-j\sigma^2L/D}{\sigma}\ \Longrightarrow\ N(0,1),\qquad \sigma\to\infty.
\]

Suppose independent Poisson resets of rate \(r\) restart the particle at \(x\), drawing fresh independent Brownian noise and a fresh \(N(0,\sigma^2)\) velocity. Denote the total expected absorption time by \(\mathcal T_\sigma(r)\). Then

\[
\mathcal T_\sigma'(0+)=M_1(\sigma)^2-\tfrac12M_2(\sigma)<0
\]

for every sufficiently large \(\sigma\), and a finite global minimizer with strictly positive reset rate exists for those \(\sigma\). Conversely, at zero propulsion variance,

\[
\mathcal T_0'(0+)=\frac{x(x-2L)(5x^2-10Lx+4L^2)}{24D^2}.
\]

Therefore for each \(x/L>1-1/\sqrt5\), the initial effect of resetting changes from detrimental at \(\sigma=0\) to beneficial for sufficiently large \(\sigma\). No uniqueness of the reversal threshold or of the optimum resetting rate is asserted.

## Assumptions and scope

For each independent attempt sample \(V\sim N(0,\sigma^2)\), a standard Brownian motion \(W\), and a path \(X\) solving the one-sided Skorokhod problem

\[
X_t=x+Vt+\sqrt{2D}\,W_t-K_t\in[0,L]
\]

up to the first contact with \(0\). Here \(K\) is continuous, nondecreasing, starts at zero, and can increase only when \(X=L\). A trajectory is terminated at \(T_\sigma=\inf\{t\geq0:X_t=0\}\). The constant velocity is a frozen-propulsion surrogate for very persistent active motion; it is not the full finite-persistence active Ornstein–Uhlenbeck process. The noise width \(\sigma\) is held fixed during each attempt and is resampled independently at each resetting event. Rates have units of inverse time, \(D\) length squared per time, and \(\sigma\) length per time. The case \(\sigma=0\) is ordinary reflected Brownian diffusion. All asymptotics hold with positive \(x,L,D\) fixed.

## Proof

**1. Conditional passage-time moments.** For a deterministic velocity \(v\in\mathbb R\), let \(m_j(z;v)=\mathbb E_z[T^j\mid V=v]\) and \(m_0\equiv1\). Standard killed-diffusion moment equations, or Dynkin's formula stopped at a bounded time followed by monotone convergence, give the unique finite solution to

\[
D m_j''(z;v)+v m_j'(z;v)=-j m_{j-1}(z;v),\quad m_j(0;v)=0,\quad m_j'(L;v)=0.
\]

Integrating the equation for its derivative against the integrating factor and then integrating from \(0\) to \(z\) gives, for \(j=1,2\),

\[
m_j(x;v)=\frac{j}{D}\int_0^x dz\int_z^Ldy\,e^{v(y-z)/D}m_{j-1}(y;v).
\]

Thus \(m_1(x;v)=D^{-1}\int_0^x dz\int_z^Ldy\,e^{v(y-z)/D}\) and

\[
m_2(x;v)=\frac2{D^2}\int_0^x dz\int_z^Ldy\int_0^y da\int_a^Ldb\,e^{v(y-z+b-a)/D}.
\]

These finite positive integrals establish the moment equations directly and are finite after Gaussian averaging. Using \(\mathbb E[e^{tV}]=e^{\sigma^2t^2/2}\), we obtain the exact formulas

\[
M_1(\sigma)=\frac1D\int_0^x dz\int_z^Ldy\,\exp\!\left(\frac{\sigma^2(y-z)^2}{2D^2}\right)
\]

and

\[
M_2(\sigma)=\frac2{D^2}\int_0^x dz\int_z^Ldy\int_0^y da\int_a^Ldb\,\exp\!\left(\frac{\sigma^2(y-z+b-a)^2}{2D^2}\right).
\]

Every integrand is nonnegative with bounded exponential argument, proving finiteness for each finite \(\sigma\). Positivity of \(y-z\) on a set of positive measure proves that \(M_1(\sigma)\) strictly increases for \(\sigma>0\). The same representation proves monotonicity for any replacement of the sampled velocity by a mean-preserving spread in convex order, with strictness whenever the spread increases the corresponding exponential moments.

**2. Corner Laplace asymptotics.** Set \(a_\sigma=\sigma^2/(2D^2)\). In the double integral \(h_1=y-z\leq L\), equality occurs only at the spatial corner \((z,y)=(0,L)\). Write \(s=z\), \(t=L-y\); locally \(h_1=L-s-t\), with \(s,t\geq0\). For \(\sigma\to\infty\), the unique maximum contributes the full integral to leading order. With \(\lambda_1=\sigma^2L/D^2\), dominated Laplace localization on the fixed compact integration polytope yields

\[
\int_0^x dz\int_z^Ldy\,e^{a_\sigma (y-z)^2}
\sim e^{a_\sigma L^2}\left(\int_0^\infty e^{-\lambda_1s}ds\right)^2
=e^{a_\sigma L^2}\lambda_1^{-2}.
\]

For the quadruple integral let \(h_2=y-z+b-a\leq2L\). Its unique maximum is \((z,y,a,b)=(0,L,0,L)\); writing the four nonnegative corner distances \(s_1=z,s_2=L-y,s_3=a,s_4=L-b\) gives \(h_2=2L-\sum_{i=1}^4s_i\). The local inequalities defining the nested integrals become inactive at this corner. With \(\lambda_2=2\sigma^2L/D^2\), the same argument yields

\[
\int_{\mathrm{nested}}e^{a_\sigma h_2^2}\,dz\,dy\,da\,db
\sim e^{4a_\sigma L^2}\lambda_2^{-4}.
\]

To justify these local calculations without assuming a formal saddle-point rule: for any fixed neighborhood of the unique maximizing corner, the compact complement has an exponentially smaller maximum. Inside the neighborhood, substitute the distances \(s_i=u_i/\lambda_j\). The exponent difference tends pointwise to \(-\sum_i u_i\), while for sufficiently small fixed neighborhood the inequality \((jL-\sum_i s_i)^2\leq(jL)^2-jL\sum_i s_i\) dominates the rescaled kernel by an integrable product exponential. Dominated convergence therefore proves both limits. Inserting prefactors \(1/D\) and \(2/D^2\) proves all displayed large-\(\sigma\) moment asymptotics.

**3. Velocity selection.** Let \(Q_{j,\sigma}\) be the probability measure with density proportional to \(m_j(x;v)e^{-v^2/(2\sigma^2)}\), for \(j=1,2\). In the spatial-integral representation, conditional on the spatial variables with sum \(h_j\), exponential tilting of the Gaussian makes

\[
V\mid h_j\ \sim\ N(\sigma^2h_j/D,\sigma^2).
\]

The normalized spatial weight is exactly proportional to \(\exp(\sigma^2h_j^2/(2D^2))\). The preceding corner localization gives \(jL-h_j=O_{Q_{j,\sigma}}(\sigma^{-2})\), since its rescaled corner distances have limiting independent mean-one exponential distributions. Consequently \(\sigma(h_j-jL)/D\to0\) in probability; the independent standard Gaussian residual remains, proving the two stated distributional limits by Slutsky's theorem.

**4. Resetting transition and existence of a positive optimum.** Let \(\Phi_\sigma(r)=\mathbb E[e^{-rT_\sigma}]\). An independent attempt succeeds before a Poisson reset with probability \(\Phi_\sigma(r)>0\). Conditioning on the earlier of absorption and reset and summing independent attempts gives

\[
\mathcal T_\sigma(r)=\frac{1-\Phi_\sigma(r)}{r\Phi_\sigma(r)},\qquad r>0.
\]

Its continuous extension at \(r=0\) equals \(M_1(\sigma)\). Taylor expansion of \(\Phi_\sigma(r)=1-rM_1+r^2M_2/2+o(r^2)\), justified by finite second moment, gives \(\mathcal T_\sigma'(0+)=M_1^2-M_2/2\). By Step 2, \(M_2/(2M_1^2)\to\infty\), so the derivative becomes negative at sufficiently large \(\sigma\).

To see that a global optimum is attained at a finite positive rate, it suffices to prove \(r\Phi_\sigma(r)\to0\) as \(r\to\infty\). For the reflected path up to absorption, the reflection regulator is at most \(|V|t+\sqrt{2D}\sup_{s\leq t}|W_s|\) by the Skorokhod representation, so absorption by time \(t\) requires

\[
2|V|t+2\sqrt{2D}\sup_{s\leq t}|W_s|\geq x.
\]

Gaussian-tail and Brownian-reflection bounds imply \(\mathbb P(T_\sigma\leq t)=O(e^{-c/t})+O(e^{-c/t^2})\) as \(t\downarrow0\), for constants depending on fixed parameters. Hence \(\mathbb E[T_\sigma^{-2}]<\infty\). The elementary inequality \(e^{-u}\leq C/u^2\) for \(u>0\) then gives \(r\Phi_\sigma(r)\leq C\mathbb E[T_\sigma^{-2}]/r\to0\). Thus \(\mathcal T_\sigma(r)\to\infty\) at large \(r\), while its initial derivative is negative. Continuity forces at least one finite global minimizer with \(r>0\).

**5. The sharp passive starting-position boundary.** At \(\sigma=0\), direct integration of the exact moment formulas gives

\[
M_1(0)=\frac{x(2L-x)}{2D},\qquad
M_2(0)=\frac{x(2L-x)(4L^2+2Lx-x^2)}{12D^2}.
\]

Subtracting \(M_2(0)/2\) from \(M_1(0)^2\) yields the displayed polynomial. Its sign on \(0<x\leq L\) is positive precisely for \(x/L>1-1/\sqrt5\), zero at equality, and negative below. Continuity in \(\sigma\) and the large-noise sign proved above establish a reset-response reversal for every strictly above-threshold starting point. The proof makes no monotonicity assertion about the reset derivative as a function of \(\sigma\), hence no claim of a unique noise threshold.

## Verification

The standalone `verify.py` independently evaluates the two exact spatial-integral representations by nested Gauss--Legendre quadrature using `numpy`. It compares zero-propulsion values with the explicit polynomial formulas for four geometric parameter choices, checks the passive restart slope, strict mean growth over a finite grid, the predicted restart sign reversal, and the monotone reduction of leading asymptotic relative errors at large propulsion width. Run `python verify.py`. These numerical tests are diagnostics, not a replacement for the compact-polytope Laplace proof or the all-parameter sign arguments.

## Relationship to prior work

Georgiou, Bressloff and Bertrand (2026) study the same absorbing/reflecting interval and position-plus-velocity resetting protocol in a full active Ornstein--Uhlenbeck particle, but their analytical results are perturbative in weak activity and for finite persistence. Their conclusion explicitly highlights strongly persistent activity and resetting protocols as further directions. The present theorem concerns a different, precisely defined *frozen Gaussian propulsion* model and proves high-width rare-velocity moment asymptotics, size-biased velocity laws, and a reset-onset reversal. It does not extend their finite-persistence theorem without additional uniform-limit analysis.

Montero, Masó-Puigdellosas and Villarroel (2017) examine randomly oriented monotone continuous-time random walks with resets and derive general survival and first-passage identities. These imply the renewal part in principle, but not the reflecting drift-diffusion moment integrals or Gaussian high-width corner asymptotics. Standard stochastic-restart theory also contains the universal first- and second-moment threshold; only its quantitative evaluation in this particular frozen-propulsion family is claimed here as new. Woillez, Kafri and Lecomte (2019) analyze persistent active escape using a large-deviation approximation for a different limit and confining potential.

## Limitations

This is a frozen-drift Brownian model, not a proof of uniform convergence from finite-persistence active Ornstein--Uhlenbeck dynamics. Only fresh independent velocity resampling at a reset is covered. The theorem does not calculate resetting cost, entropy production, finite-persistence corrections, uniqueness of a beneficial-reset noise boundary, or uniqueness of the optimal reset rate. Published-literature coverage outside the accessible sources and independent scientific validation remain possible limitations.

## References

1. D. K. Georgiou, P. C. Bressloff and T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein--Uhlenbeck particle*, arXiv:2609.21124v1 (first public September 17, 2026), https://arxiv.org/abs/2609.21124.
2. M. Montero, A. Masó-Puigdellosas and J. Villarroel, *Continuous-time random walks with reset events: Historical background and new perspectives*, arXiv:1706.04812v1 (2017), https://arxiv.org/abs/1706.04812.
3. J. Woillez, Y. Kafri and V. Lecomte, *Nonlocal stationary probability distributions and escape rates for an active Ornstein--Uhlenbeck particle*, arXiv:1912.04010 (2019), https://arxiv.org/abs/1912.04010.
4. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and applications*, arXiv:1910.07993 (2019), https://arxiv.org/abs/1910.07993.
