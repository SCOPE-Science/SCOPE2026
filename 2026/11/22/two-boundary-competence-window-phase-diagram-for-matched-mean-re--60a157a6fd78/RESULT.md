# Two-boundary competence-window phase diagram for matched-mean residence clocks

## Finding

For any real shape \(k>1\), compare residence/exit times \(T_1\sim\operatorname{Exp}(1/\tau)\) and \(T_k\sim\operatorname{Gamma}(k,k/\tau)\), with the same mean \(\tau>0\). Consider a finite competence period from age \(\tau c\) to \(\tau(c+L)\), with \(c\ge0\) and \(L>0\), and define the change in the probability of exiting during that period:

\[
\Delta_k(c,L)=\Pr\{\tau c<T_k\le\tau(c+L)\}-\Pr\{\tau c<T_1\le\tau(c+L)\}.
\]

There is one critical normalized width \(\ell_k>0\). For every \(0<L<\ell_k\), there are exactly two simple positive onset thresholds \(c_-(L)<c_+(L)\), and \(\Delta_k\) is strictly negative, positive, and negative on the three successive onset intervals. At \(L=\ell_k\), onset zero is an equality, and there is precisely one further positive zero \(c_+(L)\), with \(\Delta_k(c,L)>0\) between them and negative afterward. For \(L>\ell_k\), exactly one positive zero \(c_+(L)\) exists; \(\Delta_k\) is positive for all \(0\le c<c_+(L)\) and negative for \(c>c_+(L)\). Every described equality is exact, and no other onset zeros exist.

Both threshold curves are strictly decreasing in \(L\). With the two distinct normalized residence-density crossings denoted \(0<\alpha_k<1<\beta_k\), their endpoint limits are

\[
\begin{aligned}
&\lim_{L\downarrow0}c_-(L)=\alpha_k,\qquad\lim_{L\uparrow\ell_k}c_-(L)=0,\\
&\lim_{L\downarrow0}c_+(L)=\beta_k,\qquad\lim_{L\to\infty}c_+(L)=\ell_k.
\end{aligned}
\]

The critical width is the unique solution \(\ell_k\in(\alpha_k,\beta_k)\) of

\[
P(k,k\ell_k)=1-e^{-\ell_k},
\]

where \(P\) is the regularized lower incomplete gamma function. As the number of Gamma stages grows,

\[
\ell_k=1+\frac{\Phi^{-1}(1-e^{-1})}{\sqrt{k}}+o(k^{-1/2}),\qquad
\Phi^{-1}(1-e^{-1})\simeq0.3374749637642.
\]

For integer \(k\), the Gamma clock is an \(k\)-stage Erlang model. The classification also holds for every noninteger real \(k>1\).

## Assumptions and scope

Exit times are nonnegative and exactly distributed according to the specified exponential and Gamma laws; their means match exactly. The competence interval is a fixed deterministic window, starts at nonnegative age and has positive finite width. Exiting within the competence window is the modeled event. No mortality, dispersal direction, successful settlement, larval behavior, post-exit survival, or hydrodynamic calibration is inferred. The theorem compares a clock distribution under changed variance, not identical full transport environments.

Scale invariance allows \(\tau=1\). Define the densities \(f_1(t)=e^{-t}\) and \(f_k(t)=k^k t^{k-1}e^{-kt}/\Gamma(k)\) for \(t>0\). Let \(F_1,F_k\) denote the cumulative distribution functions. Write

\[
H(t)=F_k(t)-F_1(t)=P(k,kt)-(1-e^{-t}),\qquad
\Delta_k(c,L)=H(c+L)-H(c).
\]

Every quantifier in the finding holds separately for each fixed real \(k>1\) and each specified \(L>0\).

## Proof

**Density crossing geometry.** The density ratio is

\[
R_k(t)=\frac{f_k(t)}{f_1(t)}=\frac{k^k}{\Gamma(k)}t^{k-1}e^{-(k-1)t}.
\]

Its logarithmic derivative equals \((k-1)(1/t-1)\). Thus \(R_k\) rises strictly on \((0,1)\), falls strictly on \((1,\infty)\), and tends to zero at each endpoint. Its maximum must exceed one: otherwise \(f_k\le f_1\) everywhere with strict inequality on a set of positive measure, contradicting their common total mass one. Consequently there are exactly two solutions of \(R_k(t)=1\), one in \((0,1)\) and the other in \((1,\infty)\); call them \(\alpha_k\) and \(\beta_k\). Their density difference \(H'(t)=f_k(t)-f_1(t)\) has strict signs \(-,+,-\) on the consecutive intervals.

**Cumulative crossing geometry.** Because \(H(0)=0\) and \(H(\infty)=0\), the derivative signs show that \(H(\alpha_k)<0\) and \(H(\beta_k)>0\); the latter follows also because \(H\) is strictly decreasing to zero after \(\beta_k\). Thus one and only one zero \(\ell_k\) lies in \((\alpha_k,\beta_k)\). In particular, \(H(t)<0\) for \(0<t<\ell_k\) and \(H(t)>0\) for \(t>\ell_k\). Strictly, \(H\) decreases on \((0,\alpha_k)\), increases on \((\alpha_k,\beta_k)\), and decreases on \((\beta_k,\infty)\).

**Lower threshold.** For every \(c\in(0,\alpha_k)\), the value \(H(c)<0\) is attained exactly once on the strictly increasing branch \((\alpha_k,\ell_k)\); denote the companion abscissa \(r_-(c)\). As \(c\) increases, \(H(c)\) strictly decreases and so does \(r_-(c)\). The companion distance \(L_-(c)=r_-(c)-c\) is therefore strictly decreasing and continuous. It tends to \(\ell_k\) as \(c\downarrow0\) and to zero as \(c\uparrow\alpha_k\). For \(0<L<\ell_k\), exactly one \(c_-(L)\) solves \(L=L_-(c)\); for larger widths none exists. Because \(H\) first declines and then increases above this matched height, the sign of \(H(c+L)-H(c)\) changes from negative to positive at the lower threshold. When \(L=\ell_k\), \(c=0\) is the limiting equality. For \(L>\ell_k\), \(H(L)>0=H(0)\).

**Upper threshold.** For every \(c\in(\ell_k,\beta_k)\), the value \(H(c)>0\) occurs exactly once on the strictly decreasing branch \((\beta_k,\infty)\); call the companion \(r_+(c)\). As \(c\) increases, \(H(c)\) increases and \(r_+(c)\) strictly decreases. Hence \(L_+(c)=r_+(c)-c\) is continuous and strictly decreasing from infinity (as \(c\downarrow\ell_k\)) to zero (as \(c\uparrow\beta_k\)). Each \(L>0\) therefore has exactly one upper threshold \(c_+(L)\), with positive difference to its left (after any lower threshold) and negative to its right. When \(c\ge\beta_k\), strict decrease of \(H\) forces \(\Delta_k<0\). For \(\alpha_k\le c\le\ell_k\), strict increase of \(H\) until its positive maximum, followed by a decline to a positive limit zero, forces \(\Delta_k>0\). These facts exhaust all \(c\ge0\). At the lower crossing \(H'(c)<0<H'(c+L)\), and at the upper crossing \(H'(c)>0>H'(c+L)\), so the onset zeros are simple. Monotonicity and endpoint limits of both curves follow directly from the inverse companion distances.

**Large-shape limit.** A Gamma variable of shape \(k\) and rate \(k\) has mean one and variance \(1/k\). For every fixed \(t<1\), its CDF tends to zero as \(k\to\infty\); for fixed \(t>1\), it tends to one. Comparing these limits to \(F_1(t)\) and using uniqueness of the crossing proves \(\ell_k\to1\). The Gamma central limit theorem gives, for fixed real \(z\),

\[
F_k(1+z/\sqrt{k})\longrightarrow\Phi(z),\qquad
F_1(1+z/\sqrt{k})\longrightarrow1-e^{-1}.
\]

The unique sign crossing and continuity permit squeezing its standardized location between any two numbers on opposite sides of \(\Phi^{-1}(1-e^{-1})\). This proves the stated expansion; it does not rely on a numerical fit.

## Verification

The accompanying `check_window.py` independently evaluates the densities and cumulative probabilities using SciPy, solves the density and cumulative crossings by scalar bracketing, and probes sign regions, all window regimes, root monotonicity, and the asymptotic scaling. It passed 59,007 diagnostic assertions for twelve real shapes \(1.05,1.2,1.5,2,2.5,3,4,5,10,15,30,100\), as well as larger shapes in the asymptotic check. The finite computations check implementation and examples only; the above analytical argument proves all real \(k>1\) and all \(c,L\) in the stated ranges.

For \(k=2\), \(\alpha_2\simeq0.3574029562\), \(\ell_2\simeq1.2564312086\), \(\beta_2\simeq2.1532923641\). At window width \(L=0.5\), the onset crossings are approximately \(0.1540548276\) and \(1.9254285952\). At \(L=1.5\) only the upper crossing, approximately \(1.5967399055\), remains.

## Relationship to prior work

Siegel et al. (2003) motivate distinguishing precompetence from competence periods when modeling marine larval transport, rather than specifying the present pair of mean-matched residence-time distributions. Cetina-Heredia and Connolly (2011) study reef residence times and predictors of mean retention under hydrodynamics; their reported mean alone does not determine a finite departure-window probability. Figueiredo, Baird and Connolly (2013) combine larval competence and reef flushing using a constant flushing rate, whereas the present comparison changes the entire residence-time law but retains its mean. The theorem is a theoretical matched-mean clock sensitivity result, not a rederivation of these ecological models. Comparable Gamma/exponential crossing identities and general stochastic-order methods may precede this application; historical priority is not independently settled.

## Limitations

The biological interpretation is explicitly limited to the chance of **exit** during an externally specified competence interval. Exiting when competent is not equivalent to settling successfully, local retention or self-recruitment. No empirical evidence justifies a Gamma rather than exponential residence law for a particular site. Real competence may be probabilistic and continuous rather than a fixed rectangular window, and residence times can depend on conditions and larval behavior. Near any equality boundary, an estimated sign can be numerically fragile. Literature comparisons could not rule out all older mathematical equivalents; a relevant ecological modeling article by Connolly and Baird (2010) was not available in full text for this comparison.

## References

1. Siegel, D. A., Kinlan, B. P., Gaylord, B., and Gaines, S. D. (2003), *Lagrangian descriptions of marine larval dispersion*, Marine Ecology Progress Series 260:83–96, published September 30, 2003. https://doi.org/10.3354/meps260083 . Full text: https://static1.squarespace.com/static/5f8727713ecbb72c5beec2b8/t/5f88b801bea5e90073be34a5/1602795524837/Siegel_et_al_2003_MEPS.pdf
2. Cetina-Heredia, P., and Connolly, S. R. (2011), *A simple approximation for larval retention around reefs*, Coral Reefs 30. https://doi.org/10.1007/s00338-011-0749-z . Full text: https://reefresilience.org/pdf/Cetina-Heredia_Connolly_2011.pdf
3. Figueiredo, J., Baird, A. H., and Connolly, S. R. (2013), *Synthesizing larval competence dynamics and reef-scale retention reveals a high potential for self-recruitment in corals*, Ecology 94(3):650–659. https://doi.org/10.1890/12-0767.1 . Full text: https://scholars.nova.edu/ws/portalfiles/portal/42840688/Synthesizing%20Larval%20Competence%20Dynamics%20and%20Reef-Scale%20Retention.pdf
4. Connolly, S. R., and Baird, A. H. (2010), *Estimating dispersal potential for marine larvae: dynamic models applied to scleractinian corals*, Ecology 91:3572–3583. https://doi.org/10.1890/10-0143.1 . Abstract available; full text not inspected.
