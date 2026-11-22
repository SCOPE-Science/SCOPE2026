# A sharp mean–cap phase diagram for Haldane substrate-inhibited growth

## Finding

Consider an externally imposed, measurable substrate concentration whose time distribution is an arbitrary Borel probability law \(P\) on \([0,B]\), with fixed mean \(m\). Under the Haldane–Andrews instantaneous growth law
\[
 f(s)=\frac{\mu s}{K+s+s^2/I},\qquad K,I,\mu>0,
\]
the maximum and minimum of \(\mathbb E_P[f(S)]\) have exact, unique optimizing laws, including a sharp boundary at which fixed-mean substrate variability first becomes beneficial.

Set \(M=\sqrt{KI}\). Let \(R>M\) be the unique positive root of
\[
R^3-3KI R-KI^2=0.
\]
For \(B\le R\), the maximizing law is uniquely the constant law \(S=m\). For \(B>R\), define
\[
a_B=\frac{I}{B}\left[K+\sqrt{K^2+KB(1+B/I)}\right].
\]
Then \(M<a_B<R<B\). If \(0\le m\le a_B\), the unique maximizing law remains \(S=m\); if \(a_B<m<B\), the unique maximizing law assigns weights \((B-m)/(B-a_B)\) and \((m-a_B)/(B-a_B)\) to \(a_B\) and \(B\), respectively. At \(m=B\), the only law is constant. Consequently the maximum is
\[
 U_B(m)=\begin{cases}
 f(m),&B\le R\ \text{or}\ m\le a_B,\\
 \dfrac{(B-m)f(a_B)+(m-a_B)f(B)}{B-a_B},& B>R,\ a_B<m\le B.
 \end{cases}
\]
For every \(B>0\) and \(0\le m\le B\), the minimum is \(m f(B)/B\), uniquely attained (for \(0<m<B\)) by the law on \(\{0,B\}\) with weights \(1-m/B\) and \(m/B\).

For a prescribed mean \(m>M\), define the critical cap
\[
 B_c(m)=\frac{KI(I+2m)}{m^2-KI}.
\]
If \(M<m<R\), a nonconstant input strictly beats constant \(m\) if and only if \(B>B_c(m)\); if \(m\ge R\), it does so for every \(B>m\). If \(m\le M\), constant input is best for every finite cap \(B\ge m\). These conditions classify *all* admissible distributions, not just equal-duration two-level inputs.

There is a singular unbounded-cap limit: when \(m>M\), over laws on \([0,\infty)\) with finite mean \(m\), the supremum is \(f(M)\) but is unattained. The finite-cap maximizers approach it as \(B\to\infty\), with their high-concentration weight tending to zero. For \(m\le M\), the constant law uniquely maximizes even without a cap. For \(m>0\) and no cap, the infimum zero is likewise unattained.

## Assumptions and scope

The result concerns nonnegative externally specified substrate *concentrations*, whose time fractions (or stationary one-time law) can be chosen freely subject only to a prescribed mean and, for the finite-cap theorem, a hard upper bound. The response is instantaneous Haldane–Andrews growth. There is no coupling to uptake, dilution, biomass feedback, acclimation, feed-rate bounds, or substrate mass conservation within a reactor. In the elementary linear biomass model \(\dot X=(f(S(t))-d)X\), the time-mean \(f(S)\) gives the logarithmic growth exponent up to the constant loss \(d\), when the driving environment has well-defined long-run occupation fractions.

The zero-mean and full-cap endpoints have only one feasible law. The optimizer statements otherwise quantify over **every** Borel probability measure on \([0,B]\), including continuous, discrete, and mixed laws. No assertion is made that an arbitrary optimum occupation law can be implemented in a physical chemostat.

## Proof

Write \(c=1/I\) and \(D(s)=K+s+cs^2\). The positive multiplier \(\mu\) does not change any optimizer and is suppressed in the algebra below. Direct differentiation yields
\[
 f'(s)=\frac{K-cs^2}{D(s)^2},\qquad
 f''(s)=\frac{2(c^2s^3-3Kcs-K)}{D(s)^3}.
\]
The cubic \(h(s)=c^2s^3-3Kcs-K\) decreases on \((0,M)\), increases on \((M,\infty)\), is negative at \(M\), and tends to infinity. Thus \(R\) exists uniquely, \(f\) is strictly concave on \((0,R)\), and strictly convex on \((R,\infty)\). For \(B\le R\), strict Jensen immediately gives the unique upper optimizer.

For \(B>R\), seek a line tangent to \(f\) at \(a\) and passing through \((B,f(B))\). The secant identity
\[
\frac{f(B)-f(a)}{B-a}=\frac{K-caB}{D(a)D(B)}
\]
reduces this tangency equation, after removing the root \(a=B\), to
\[
 Bc(ca^2-K)=K(1+2ca).
\]
It has the unique positive solution \(a=a_B\) displayed above with \(a>M\). The right-hand expression \(B=K(1+2ca)/[c(ca^2-K)]\) decreases strictly from infinity to zero as \(a\) increases from \(M\); at \(a=R\), it equals \(R\), precisely because \(h(R)=0\). Therefore \(M<a_B<R<B\).

Let \(\ell(s)=f(a)+f'(a)(s-a)\). The exact factorization
\[
\ell(s)-f(s)=\frac{-c f'(a)(s-a)^2(B-s)}{D(s)}\ge0
\qquad (0\le s\le B)
\]
follows from the tangency identity. Its inequality is strict except at \(s=a,B\), because \(f'(a)<0\). The piecewise function \(C(s)=f(s)\) on \([0,a]\) and \(C(s)=\ell(s)\) on \([a,B]\) is concave: \(f\) is strictly concave to \(a\), and its derivative agrees with the chord slope at \(a\). Also \(C\ge f\). Thus
\[
\mathbb E f(S)\le\mathbb E C(S)\le C(\mathbb E S)=C(m).
\]
If \(m\le a\), equality forces the constant law (including \(m=a\)); if \(a<m<B\), equality forces support on the two contact points \(a,B\), and the mean uniquely determines their weights. These laws attain \(C(m)\), proving the global maximum and uniqueness.

Since \(s/D(s)\ge (s/B)/D(B)\) for \(0\le s\le B\), with equality only when \(s=0\) or \(B\), integration gives \(\mathbb E f(S)\ge (m/B)f(B)\), with the asserted unique minimizing law.

For a fixed \(m\in(M,R)\), tangency is located at the mean exactly when \(B=B_c(m)\), by solving the displayed tangency equation for \(B\). Monotonicity of \(a_B\) shows \(m>a_B\) precisely for \(B>B_c(m)\), giving the sharp beneficial-fluctuation condition; for \(m\ge R\) and \(B>m\), necessarily \(a_B<m\). When \(m\le M\), the tangent at \(m\) is a global majorant even on the unbounded half-line, as follows from the identity
\[
 \left[f(m)+f'(m)(s-m)\right]-f(s)
 =\frac{(s-m)^2\left[K+2Kcm+cs(K-cm^2)\right]}{D(m)^2D(s)}\ge0.
\]
It is strict for \(s\ne m\), proving unbounded-cap uniqueness. When \(m>M\), the pointwise global maximum \(f(M)\) cannot be attained by any nonconstant law having mean \(m\). Yet the finite-cap mixture has \(a_B\downarrow M\) and upper-point weight \((m-a_B)/(B-a_B)\to0\), so its expected response tends to \(f(M)\). Finally, the lower two-point law on \(\{0,B\}\) has expectation \(mf(B)/B\to0\), and zero expectation is impossible at positive mean.

## Verification

The accompanying dependency-free `checker.py` tests the tangency and supporting-line identities with exact rational arithmetic, exercises multiple kinetic parameters and cap/mean grids, and checks the sharp threshold, limiting behavior and comparisons with thousands of two-point competitors. Its execution returned `PASS: 59170 deterministic assertions`. The proof above, not finite sampling, certifies every Borel law and the infinite-domain statements.

For example, with \(K=I=\mu=1\), the inflection boundary is \(R=2\cos(\pi/9)\approx1.879385\). At mean \(m=3/2\), the exact critical concentration cap is \(B_c=16/5=3.2\); below or at that cap there is no benefit from variability, but above it there is. At \(m=3\) and \(B=5\), constant feed gives \(3/13\approx0.230769\) while the unique two-level optimum is approximately \(0.250226\), an improvement of approximately \(8.43\%\).

## Relationship to prior work

The Haldane–Andrews response and its inhibitory peak are classical (Andrews 1968). Bumbak et al. (2011) discuss experimentally motivated pulsed substrate delivery and toxicity limits in cultivation. Rapaport, Haidar and Harmand (arXiv 2012) study nonlinear chemostat equilibria, buffers and stability using Haldane kinetics, not distribution-free maximum average response under an externally fixed substrate mean and concentration cap. Bayen, Rapaport and Tani (2020) study optimal **dilution-rate controls for coupled periodic chemostat states**; their conclusions about periodic operation do not imply the exogenous concentration-law optimum here, nor does this theorem imply a physically feasible chemostat improvement.

General fixed-mean concavification is a standard convex-analysis principle; the claimed contribution is specifically the explicit Haldane tangency law, its sharp three-regime mean–cap phase diagram and uniqueness and nonattainment boundaries. That contribution is not a claim that the concavification principle itself is new.

## Limitations

The controlled substrate distributions need not be attainable with mass balance, mixing delays, state constraints, actuator limits, or physiologic memory. The theorem concerns average instantaneous specific growth, not volumetric product yield, equilibrium stability, washout risk, or empirical optimal feeding. No independent scientific audit has been performed. Historical priority is provisional: the 1968 original and some periodic-control papers were not read in full, and equivalent specialized concavification formulas may exist outside inspected material.

## References

- Andrews, J. F. (1968), *A mathematical model for the continuous culture of microorganisms utilizing inhibitory substrates*, Biotechnology and Bioengineering 10, 707–723, DOI:10.1002/bit.260100602.
- Bumbak, F., Cook, S., Zachleder, V., Hauser, S., Kovar, K. (2011), *Best practices in heterotrophic high-cell-density microalgal processes*, Applied Microbiology and Biotechnology, DOI:10.1007/s00253-011-3311-6, https://pmc.ncbi.nlm.nih.gov/articles/PMC3114082/ .
- Rapaport, A., Haidar, I., Harmand, J. (2012), *The buffered chemostat with non-monotonic response functions*, arXiv:1212.4252, https://arxiv.org/abs/1212.4252 .
- Bayen, T., Rapaport, A., Tani, F.-Z. (2020), *Improvement of performances of the chemostat used for continuous biological water treatment with periodic controls*, Automatica 121, 109199, DOI:10.1016/j.automatica.2020.109199.
