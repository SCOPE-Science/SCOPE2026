# An opposing-tail covariance transition in a synchronously reset Brownian gas

## Finding

Consider \(N\ge2\) Brownian particles on \(\mathbb R\), each with generator \(D\partial_{xx}\), sharing one Poisson clock of rate \(r>0\). Every clock ring resets *all* particles to zero; between rings their Brownian motions are independent. Observe the unique stationary law. For \(a>0\), let \(C_+(a)=\#\{i:X_i>a\}\), \(C_-(a)=\#\{i:X_i<-a\}\), and \(b=a\sqrt{r/D}>0\). Write

\[
q_b(t)=\frac12\operatorname{erfc}\!\left(\frac{b}{2\sqrt t}\right),\quad
p_b=\frac12e^{-b},\quad
J(b)=\int_0^\infty e^{-t}q_b(t)^2\,dt.
\]

Then \(J(b)>p_b^2\), and the *exact* finite-population covariance and its critical population are

\[
\operatorname{Cov}(C_+,C_-)=N\big[(N-1)J(b)-Np_b^2\big],\qquad
N_{\mathrm{crit}}(b)=\frac{J(b)}{J(b)-p_b^2}>1.
\]

For each fixed \(b>0\), the covariance is strictly positive exactly for integers \(N>N_{\mathrm{crit}}(b)\), zero at equality if the threshold is an integer, and negative for \(N<N_{\mathrm{crit}}(b)\). The function has the sharp endpoint laws

\[
N_{\mathrm{crit}}(b)\sim\frac{\pi}{2b^2\log(1/b)}\quad(b\downarrow0),
\]
\[
N_{\mathrm{crit}}(b)-1\sim
\frac{2^{3/4}\sqrt\pi}{4}\,\sqrt b\,e^{-(2-\sqrt2)b}\quad(b\to\infty).
\]

In particular every fixed population \(N\ge2\) has negative covariance for all sufficiently small positive \(a\) and positive covariance for all sufficiently large \(a\). **No uniqueness of the crossover in \(a\) is asserted.**

More sharply, for any fixed \(c>0\), choose the mesoscopic observation level \(b_N=\sqrt{c/(N\log N)}\). Then

\[
\boxed{\lim_{N\to\infty}\frac1N\operatorname{Cov}\big(C_+(b_N),C_-(b_N)\big)=\frac{c-\pi}{4\pi}.}
\]

Here the argument \(b_N\) of \(C_\pm\) is the dimensionless level, so the physical threshold is \(a_N=\sqrt{D/r}\,b_N\). Thus the sign crosses at the universal *critical mesoscopic constant* \(c=\pi\): it is ultimately negative for \(0<c<\pi\) and ultimately positive for \(c>\pi\). No sign is claimed at \(c=\pi\) from the displayed leading-order limit.

## Assumptions and scope

The particle noises are independent conditioned on the common clock, and all particles reset simultaneously and instantaneously to the same location. The law is stationary at the observation time (equivalently, the time elapsed since the last clock ring is exponential with parameter \(r\)). Counts refer to two disjoint, unbounded, opposite tails, and the covariance is over both Brownian noise and the common resetting clock. The theorem requires integer \(N\ge2\), finite \(D,r>0\), and \(a>0\). At \(a=0\), \(C_++C_-=N\) almost surely and the covariance is exactly \(-N/4\), which is consistent with the singular small-level regime but outside the displayed critical-population definition.

## Proof

**1. Conditional count law.** Let \(S\sim\mathrm{Exp}(r)\) be the common stationary reset age, and set \(T=rS\sim\mathrm{Exp}(1)\). Given \(T=t\), every normalized particle position \(Y_i=\sqrt{r/D}\,X_i\) is independent \(\mathcal N(0,2t)\). Hence the triple of counts in the right tail, left tail, and remaining region is multinomial with cell probabilities \((q_b(t),q_b(t),1-2q_b(t))\). In particular, conditional on \(T=t\),

\[
\mathbb E[C_+\mid T]=Nq_b(T),\qquad
\mathbb E[C_+C_-\mid T]=N(N-1)q_b(T)^2.
\]

The one-particle stationary law has density \(e^{-|y|}/2\) in these dimensionless coordinates, by the exponential-age Gaussian integral \(\int_0^\infty e^{-t}(4\pi t)^{-1/2}e^{-y^2/(4t)}dt=e^{-|y|}/2\). Thus \(\mathbb E q_b(T)=p_b=e^{-b}/2\). Taking expectations of the conditional identities yields the covariance formula. Since \(q_b(t)\) is a strictly increasing nonconstant function of \(t>0\), \(J(b)-p_b^2=\operatorname{Var}(q_b(T))>0\); the finite-population threshold and its sign criteria follow by algebra.

**2. Alternative exact integral.** The pair \((Y_1,Y_2)\) has joint density

\[
f(y_1,y_2)=\int_0^\infty\frac{e^{-t-(y_1^2+y_2^2)/(4t)}}{4\pi t}\,dt
=\frac{1}{2\pi}K_0\!\left(\sqrt{y_1^2+y_2^2}\right),
\]

where \(K_\nu\) is the modified Bessel function of the second kind. By integrating over \([b,\infty)^2\) in the first quadrant using polar coordinates and \(\int_x^\infty uK_0(u)du=xK_1(x)\), we obtain

\[
J(b)=\frac1\pi\int_0^{\pi/4}\frac b{\sin\theta}
K_1\!\left(\frac b{\sin\theta}\right)d\theta.
\]

This independent single-integral representation also supports numerical verification.

**3. Small-level logarithm.** Write \(\delta_b(t)=q_b(t)-1/2\). On \(t\ge b^2\), the uniform Taylor estimate for the complementary error function gives

\[
\delta_b(t)=-\frac b{2\sqrt{\pi t}}+O\!\left(\frac{b^3}{t^{3/2}}\right).
\]

On \(0<t<b^2\), \(|\delta_b(t)|\le1/2\). Splitting the exponential-age integral at \(b^2\) and at 1, squaring the Taylor estimate on the middle interval, and bounding the two remainders gives

\[
\mathbb E[\delta_b(T)^2]=\frac{b^2}{4\pi}\int_{b^2}^1\frac{dt}{t}+O(b^2)
=\frac{b^2}{2\pi}\log(1/b)+O(b^2).
\]

The squared mean \((\mathbb E\delta_b(T))^2=(p_b-1/2)^2=O(b^2)\). Consequently,

\[
J(b)-p_b^2=\frac{b^2}{2\pi}\log(1/b)+O(b^2).
\]

As \(J(b)\to1/4\), the stated small-level threshold follows.

**4. Remote-tail corner asymptotic.** From the two-dimensional density,

\[
J(b)=\frac1{2\pi}\int_b^\infty\!\int_b^\infty
K_0(\sqrt{x^2+y^2})\,dx\,dy.
\]

Put \(x=b+s\), \(y=b+t\) with \(s,t\ge0\). The expansion \(\sqrt{(b+s)^2+(b+t)^2}=\sqrt2b+(s+t)/\sqrt2+o(1)\) holds for each fixed \(s,t\), while convexity gives the global lower bound \(\sqrt{(b+s)^2+(b+t)^2}\ge\sqrt2b+(s+t)/\sqrt2\). Together with \(K_0(z)\sim\sqrt{\pi/(2z)}e^{-z}\) and standard monotone Bessel bounds, dominated convergence shows that the ratio of this double integral to \(K_0(\sqrt2b)\) tends to \(\int_0^\infty\!\int_0^\infty e^{-(s+t)/\sqrt2}dsdt=2\). Hence

\[
J(b)\sim\frac1\pi K_0(\sqrt2 b)
\sim\frac{2^{-3/4}}{\sqrt\pi}\,b^{-1/2}e^{-\sqrt2b}.
\]

Since \(p_b^2=e^{-2b}/4\), we have \(p_b^2/J(b)\to0\) and \(N_{\mathrm{crit}}(b)-1\sim p_b^2/J(b)\), giving the displayed large-level coefficient.

**5. Mesoscopic scaling.** With \(b_N=\sqrt{c/(N\log N)}\), one has \(\log(1/b_N)\sim(\log N)/2\). Step 3 therefore yields \(N\operatorname{Var}(q_{b_N}(T))\to c/(4\pi)\). Moreover \(p_{b_N}^2\to1/4\). Rewrite the exact covariance as

\[
\frac1N\operatorname{Cov}(C_+,C_-)
=(N-1)\operatorname{Var}(q_{b_N}(T))-p_{b_N}^2.
\]

The limiting value is \((c-\pi)/(4\pi)\), completing the proof.

## Verification

A deterministic checker named `check.py` evaluates \(J(b)\) independently as an exponential-age integral and a Bessel polar integral, checks representative positive/negative finite-population covariances, compares both endpoint asymptotics, and tests signs within the mesoscopic window. Run `python check.py` with SciPy installed. The executed package passed 42 assertions. Numerical quadrature is supplementary only: the all-\(N\) covariance identity and both limits follow from the analytic proof above.

## Relationship to prior work

Biroli, Larralde, Majumdar and Schehr (arXiv:2211.00563, initially public 2022-11-01) give the common-reset Brownian joint position distribution and single symmetric-interval full counting statistics; that distribution is the necessary starting point of Step 1, **not** a new contribution here. Their supplemental counting calculation concerns one symmetric interval rather than the cross-covariance of two separated opposite tails. Biroli, Larralde, Majumdar and Schehr (arXiv:2307.15351) establish a broader conditional-independence framework and many order/sum statistics; their framework also covers the conditioning step here. The separate contribution assessed is the exact *sign competition between disjoint-tail exclusion and shared-age fluctuation*, especially its logarithmically corrected critical population and universal \(N\log N\) window. A general joint distribution permits this result to be derived, so priority depends on whether an equivalent sign/asymptotic statement has appeared elsewhere.

## Limitations

No uniqueness or monotonicity of a critical distance at fixed population is established. This is an equal-diffusivity, single common-clock, stationary result and does not cover partial resets, individual reset clocks, finite observation times, or different target regions. No result at the critical mesoscopic constant \(c=\pi\) beyond the vanishing leading covariance is asserted. Numerical tests do not constitute proof. The publication-priority status remains subject to broader specialist literature review and independent audit.

## References

1. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first posted 2022-11-01), especially main Eq. (4) and Supplementary Section IV. https://arxiv.org/abs/2211.00563
2. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351 (first posted 2023-07-28), especially Sections I and IV.A. https://arxiv.org/abs/2307.15351
3. M. Biroli, S. N. Majumdar, and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (2023); a different many-searcher first-passage problem. https://arxiv.org/abs/2303.18012
