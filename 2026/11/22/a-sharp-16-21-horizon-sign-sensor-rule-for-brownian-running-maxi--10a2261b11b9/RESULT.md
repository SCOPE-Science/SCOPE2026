# A sharp 16/21-horizon sign-sensor rule for Brownian running maxima

## Finding

Let \((W_u)_{0\le u\le1}\) be standard Brownian motion with \(W_0=0\), and let \(M=\sup_{0\le u\le1}W_u\). Exactly one predetermined observation is available, consisting of the zero-threshold sign bit \(S_s=\operatorname{sgn}(W_s)\) for a freely chosen time \(0<s\le1\). Under squared error, optimize over **all measurable real-valued decoders of that bit** and all such observation times.

The exact optimal conditional-mean decoder at any \(s\) is
\[
\widehat M_s=\sqrt{\frac2\pi}+c(s)S_s,\qquad
c(s)=\frac{2\sqrt{s}+\sqrt{4-3s}-2}{\sqrt{2\pi}}.
\]
Its exact Bayes risk is
\[
R(s)=\mathbb E[(M-\widehat M_s)^2]
=1-\frac2\pi-\frac{(2\sqrt{s}+\sqrt{4-3s}-2)^2}{2\pi}.
\]
The **unique global optimum** over all fixed sign-measurement times and all decoders occurs at
\[
\boxed{s_*=\frac{16}{21}}.
\]
The corresponding sharp risk is
\[
\boxed{R_* = \frac{3\pi-26+4\sqrt{21}}{3\pi}}
=0.186219850260479\ldots.
\]
The terminal sign bit at \(s=1\) has risk \(1-5/(2\pi)=0.204225284540523\ldots\), so moving the one-bit sensor to \(16/21\) reduces the optimal squared error by \(8.816456943886\ldots\%\) relative to terminal-sign sensing. The optimum recovers \(48.75344443648\ldots\%\) of the prior variance \(1-2/\pi\). For horizon \(T>0\), Brownian scaling gives optimal sampling time \(16T/21\), optimal risk \(TR_*\), and decoder \(\sqrt T\,\widehat M_{s_*}\) applied to \(\operatorname{sgn}(W_{16T/21})\).

## Assumptions and scope

The observation time is chosen before observing any path information. The sensor transmits exactly the sign of the Brownian position relative to zero, without observation noise. Since \(s>0\), the sign has probabilities \(1/2\) and \(1/2\); its value at zero has probability zero. The decoder knows the selected time, uses only the one sign bit, and may output any real number. Risk is expectation under standard Wiener measure and squared loss. In particular, this is **not** an optimality claim among arbitrary one-bit thresholds, adaptive sampling times, or general binary encoders. The no-observation boundary \(s=0\), if added, has risk \(1-2/\pi\) and is strictly inferior.

## Proof

**1. Conditional projection.** The reflection principle gives \(M\overset d=|Z|\) for standard normal \(Z\), hence \(\mathbb EM=\sqrt{2/\pi}\) and \(\operatorname{Var}(M)=1-2/\pi\). As \(S_s\) is a fair symmetric sign, its two-point conditional-mean projection is \(\mathbb E[M\mid S_s]=\mathbb EM+\mathbb E[MS_s]S_s\). Its risk is the prior variance minus \(\mathbb E[MS_s]^2\). Thus it suffices to calculate \(c(s)=\mathbb E[MS_s]\) exactly.

**2. Brownian reflection and splitting at the sign site.** Put \(A=M_s/\sqrt{s}\) and \(D=(M_s-W_s)/\sqrt{s}\), where \(M_s=\max_{0\le u\le s}W_u\). The standard reflection-principle joint density, in the positive quadrant, is
\[
f_{A,D}(a,d)=2(a+d)\phi(a+d),\quad a,d\ge0,
\]
where \(\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}\). This density is exchangeable in \(a,d\), and \(S_s=\operatorname{sgn}(A-D)\). By exchangeability,
\[
\mathbb E[A\operatorname{sgn}(A-D)]
=\frac12\mathbb E|A-D|=\frac1{\sqrt{2\pi}},
\]
since \(A-D=W_s/\sqrt s\) is standard normal.

The future Brownian increments are independent of \((A,D)\), and their maximum over the remaining horizon is distributed as \(\sqrt{1-s}|Z'|\). Write \(r=\sqrt{(1-s)/s}\) and take \(Z'\) independent standard normal. The full maximum therefore satisfies, jointly with the observed sign,
\[
\frac M{\sqrt s}\ \overset d=\ A+(r|Z'|-D)_+.
\]
The expectation over the first coordinate of the joint density, weighted by the sign, gives the explicit kernel
\[
k(d)=\int_0^\infty 2(a+d)\phi(a+d)\operatorname{sgn}(a-d)\,da
=4\phi(2d)-2\phi(d).
\]
The expected future excess at drawdown \(d\) is
\[
h_r(d)=\mathbb E[(r|Z'|-d)_+]
=2r\phi(d/r)-2d\overline\Phi(d/r),
\]
where \(\overline\Phi\) is the standard normal upper-tail function, for \(r>0\). For \(r=0\), the excess is identically zero.

**3. Exact Gaussian integral.** For \(b>0\) and \(r>0\), direct integration and integration by parts give
\[
I_b:=\int_0^\infty\phi(bd)\phi(d/r)\,dd
=\frac{r}{2\sqrt{2\pi}\sqrt{1+b^2r^2}},
\]
\[
K_b:=\int_0^\infty d\phi(bd)\overline\Phi(d/r)\,dd
=\frac1{2b^2\sqrt{2\pi}}-\frac{I_b}{b^2r}.
\]
It follows that
\[
\begin{aligned}
\int_0^\infty k(d)h_r(d)\,dd
&=8rI_2-4rI_1-8K_2+4K_1\\
&=\frac{1+\sqrt{1+4r^2}-2\sqrt{1+r^2}}{\sqrt{2\pi}}.
\end{aligned}
\]
Adding the past maximum contribution and multiplying by \(\sqrt s\) gives
\[
\begin{aligned}
c(s)&=\frac{\sqrt s}{\sqrt{2\pi}}
\left[2+\sqrt{1+4(1-s)/s}-2\sqrt{1+(1-s)/s}\right]\\
&=\frac{2\sqrt s+\sqrt{4-3s}-2}{\sqrt{2\pi}}.
\end{aligned}
\]
This also holds at \(s=1\) by continuity, which directly recovers the familiar endpoint sign case.

**4. Sharp unique minimizer.** Let \(q(s)=2\sqrt s+\sqrt{4-3s}-2\). Its derivative in the open interval is
\[
q'(s)=\frac1{\sqrt s}-\frac3{2\sqrt{4-3s}}.
\]
All denominators are positive, and its sign is precisely the sign of \(16-21s\). Thus \(q\) strictly increases on \((0,16/21)\) and strictly decreases on \((16/21,1)\). As \(q(0+)=0\), \(q(1)=1\), and \(q(s)>0\) throughout \((0,1]\), maximizing \(q(s)^2\) has a **unique** solution \(s=16/21\). Substituting this value into the exact Bayes risk yields \(R_*=(3\pi-26+4\sqrt{21})/(3\pi)\). This proves the result for the entire continuum of times and every permitted decoder. Brownian scaling proves the \(T\)-horizon statement.

## Verification

Run `python verify.py` with Python 3.10 or later after installing the packages in `requirements.txt`. The standalone verifier checks the exact optimum and risk symbolically in SymPy, checks derivative signs, verifies normalization and Gaussian moments of the reflection density, and compares the closed covariance against independently evaluated one-dimensional Gaussian integrals using SciPy. It passed 27 assertions for this package, including nine observation times. The source proof above, not these finite numerical checks, establishes the universal Bayes-risk and uniqueness statements.

## Relationship to prior work

Bisewski, Crommelin and Mandjes (arXiv first public 18 May 2017, later journal 2018) analyze numerical estimation of **Brownian barrier-crossing probabilities** and their time-grid discretization bias. Their published threshold-dependent nonuniform sampling motivates sparse maximum sensing, but their target is a crossing probability rather than squared-error estimation of the **random maximum from one sign bit**. Their full preprint, including introductory comparison with supremum-discretization literature and principal results, was inspected.

Grill, Valko and Munos (arXiv first public 15 January 2019) analyze **adaptive full-valued function evaluations** to approximate a Brownian maximum and their sample complexity. Their full preprint does not provide a fixed single-bit Bayes-risk curve or a sharp one-sensor timing rule.

Riedel (arXiv first public 13 November 2019) derives conditional distributions and moments of Brownian paths **given the maximum, argmax and terminal value**; the full accessible manuscript was inspected. This is the reverse conditioning direction and does not imply the formula for \(\mathbb E[M\mid\operatorname{sgn}(W_s)]\) or its optimizing time without additional calculations.

A prior published exact result on maximum–endpoint covariance under reversal and global sign symmetries yields our \(s=1\) specialization (including odd terminal transforms), so **that endpoint case is prior art**, not the contribution. It makes no assertion for nonterminal sign observations or their global timing optimization. A related cyclic-bridge theorem concerns intermediate positions of a **zero-sum bridge**, not the maximum of free Brownian motion; its Brownian bridge specialization cannot dominate the present formula.

Aksenov and collaborators' 2019 work on optimal Brownian observation times concerns full-valued Gaussian filtering/state-estimation measurements, rather than a single sign to estimate a running maximum. Only metadata/summary-level material was accessible for that specific source, so residual historical-priority uncertainty is retained. An undiscovered previous derivation under Gaussian extrema or one-bit sensing terminology remains possible.

## Limitations

The measurement threshold is fixed at zero. The result does **not** optimize all binary encoders or all possible thresholds; neither adaptive observation times nor added measurement noise are covered. The stochastic process is scalar standard Brownian motion and the target is its running **maximum value**, not its maximizing time, level-crossing probability, path integral, or Brownian-bridge maximum. The only independent validation of this result is not yet performed; priority remains subject to broader historical scrutiny.

## References

1. K. Bisewski, D. Crommelin and M. Mandjes, *Controlling the time discretization bias for the supremum of Brownian motion*, arXiv:1705.06567v1 (first posted 18 May 2017), later *ACM Transactions on Modeling and Computer Simulation* 28 (2018), article 24, DOI:10.1145/3177775. https://arxiv.org/abs/1705.06567
2. J.-B. Grill, M. Valko and R. Munos, *Optimistic optimization of a Brownian*, arXiv:1901.04884v1 (first posted 15 January 2019), NeurIPS 2018. https://arxiv.org/abs/1901.04884
3. K. S. Riedel, *Mean and variance of Brownian motion with given final value, maximum and argmax*, arXiv:1911.05272v1 (first posted 13 November 2019), later *Stochastic Models* 37 (2021). https://arxiv.org/abs/1911.05272
4. *Reversal and sign symmetry force a half-variance maximum–endpoint law*, public research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-reversal-and-sign-symmetry-force-a-half-variance-maximum-endpoin--5e8da51794ea
5. *Cyclic-bridge maximum–position duality without sign symmetry*, public research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-cyclic-bridge-maximum-position-duality-without-sign-symmetry--43b9344c4101
6. Aksenov et al., *Optimal measurement times for a small number of measures of a Brownian motion over a finite period*, arXiv:1902.06126 (2019). https://arxiv.org/abs/1902.06126
