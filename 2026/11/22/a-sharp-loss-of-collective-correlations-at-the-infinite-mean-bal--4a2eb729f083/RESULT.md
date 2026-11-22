# A sharp loss of collective correlations at the infinite-mean ballistic resetting boundary

## Finding
Fix an integer \(N\ge2\). At the beginning of every excursion, all particles occupy \(L>0\) and sample independent speeds \(V_1,\ldots,V_N>0\) from the same continuous distribution \(F\). They move left without changing speed, and when the fastest particle first reaches zero, all particles immediately restart at \(L\) with fresh independent speeds. Define \(X_i(t)\) as particle \(i\)'s position, and \(A_t\) as the elapsed time since the most recent common restart.

**Theorem (joint decorrelation and sharp boundary).** Assume
\[
F(v)\sim c v^\alpha\quad(v\downarrow0),\qquad c>0,\quad\alpha>0,
\]
and write \(\gamma=N\alpha\). If \(0<\gamma\le1\), then
\[
\left(\frac{X_1(t)}L,\ldots,\frac{X_N(t)}L\right)
\ \Rightarrow\ (Y_1,\ldots,Y_N),\qquad
Y_i\overset{\mathrm{iid}}\sim\operatorname{Beta}(1,\alpha).
\]
Hence the limiting joint density on \((0,1)^N\) is \(\alpha^N\prod_i(1-y_i)^{\alpha-1}\), and every distinct-particle normalized positional covariance tends to zero. If in addition \(0<\gamma<1\), the stronger joint convergence holds:
\[
\left(\frac{A_t}{t},\frac{X_1(t)}L,\ldots,\frac{X_N(t)}L\right)
\ \Rightarrow\ (U,Y_1,\ldots,Y_N),\qquad
U\sim\operatorname{Beta}(1-\gamma,\gamma),
\]
with \(U,Y_1,\ldots,Y_N\) mutually independent. In particular, the common clock retains a macroscopic aging fraction but becomes asymptotically invisible to the spatial cloud.

For the exact speed CDF \(F(v)=v^\alpha\), \(0<v<1\), when \(\gamma>1\), the unique regenerative equilibrium exists and, for any distinct \(i,j\),
\[
\lim_{t\to\infty}\operatorname{Cov}\left(\frac{X_i(t)}L,\frac{X_j(t)}L\right)
=\left(\frac{\alpha}{1+\alpha}\right)^2
\frac{(\gamma-1)(\gamma+3)}{12\gamma^2}>0.
\]
The equality case \(\gamma=1\) belongs to the independent-cloud side. This is a correlation transition, **not** a claim that the infinite-mean system has a stationary probability on the augmented renewal-age state space.

## Assumptions and scope
Time is continuous. All sampled speeds are strictly positive and the speed CDF is continuous. Speeds are constant during excursions and are resampled independently across particles and across cycles. Common resets are instantaneous. The statement is for a fixed finite \(N\), fixed \(L\), and the limit \(t\to\infty\). The regular-variation hypothesis concerns the earliest slow-speed tail; no density or finite higher moments of \(V\) are needed. \(\operatorname{Beta}(a,b)\) means density \(y^{a-1}(1-y)^{b-1}/B(a,b)\) on \((0,1)\). The exact-covariance statement requires the **specified** unit-cutoff power-speed distribution; it is not asserted for arbitrary \(F\) when \(\gamma>1\).

## Proof
**1. Renewal tail and mean.** Each full excursion lasts \(T=L/M\), where \(M=\max_iV_i\). Therefore, exactly for all \(t>0\), \(\Pr(T>t)=F(L/t)^N\); its tail is \(c^N L^\gamma t^{-\gamma}(1+o(1))\). Thus \(\mathbb ET=\infty\) for \(\gamma\le1\) and \(\mathbb ET<\infty\) for \(\gamma>1\). By the infinite-mean nonarithmetic renewal theorem, when \(\mathbb ET=\infty\), \(A_t\to\infty\) in probability. For \(0<\gamma<1\), the Dynkin–Lamperti renewal theorem additionally yields \(A_t/t\Rightarrow\operatorname{Beta}(1-\gamma,\gamma)\). The interarrival law is nonarithmetic because \(F\) is continuous.

**2. An exact conditional product law.** Disintegrate at the last completed renewal time, and suppose \(A_t=a>0\). The new excursion's sampled speed vector is independent of all completed cycles; the only information about its speed vector supplied by the event of reaching age \(a\) is \(T>a\), equivalently \(V_i<L/a\) simultaneously for all \(i\). Consequently its conditional law is the product of \(N\) independent copies of \(V\) truncated above at \(L/a\). In particular, for every \(0\le z\le1\),
\[
\Pr\left(1-\frac{X_i(t)}L\le z\,\middle|\,A_t=a\right)
=\frac{F(zL/a)}{F(L/a)}.
\]
The event of a renewal exactly at the deterministic observation time has probability zero; it does not affect this disintegration.

**3. Universal independent cloud.** As \(a\to\infty\), regular variation gives \(F(zL/a)/F(L/a)\to z^\alpha\) for every \(0<z\le1\), with the endpoint limits also consistent. The continuous limiting CDF implies weak convergence of each truncated normalized displacement to \(\operatorname{Beta}(\alpha,1)\); the exact product law yields joint convergence to **independent** copies. Since \(A_t\to\infty\) in probability, bounded-test-function conditioning proves convergence of the unconditional joint cloud, after replacing displacement by position \(1-z\), to iid \(\operatorname{Beta}(1,\alpha)\). For \(0<\gamma<1\), the same conditional argument applies to any product of a bounded continuous test function of \(A_t/t\) and a bounded continuous test function of the cloud. Combining with the Dynkin–Lamperti age limit proves independence from the entire limiting spatial vector. Positions lie in \([0,L]\), so weak convergence also gives convergence of bounded moments, including cross-particle covariances.

**4. Positive covariance above the boundary for the exact power family.** Take \(F(v)=v^\alpha\) on \((0,1)\), with \(\gamma>1\). Then \(T\) is Pareto, \(\Pr(T>a)=1\) for \(0<a<L\) and \((L/a)^\gamma\) for \(a\ge L\), and \(\mathbb ET=L\gamma/(\gamma-1)\). The equilibrium age has density \(\Pr(T>a)/\mathbb ET\). Conditional on age \(a\), the normalized positions are independent, with common conditional mean
\[
m(a)=1-\frac{\alpha}{1+\alpha}\min\!\left(\frac aL,1\right).
\]
Put \(Z=\min(A/L,1)\) for an equilibrium age \(A\). Integrating the stated equilibrium age density yields
\[
\mathbb EZ=\frac{\gamma+1}{2\gamma},\qquad
\mathbb EZ^2=\frac{\gamma+2}{3\gamma},\qquad
\operatorname{Var}Z=\frac{(\gamma-1)(\gamma+3)}{12\gamma^2}.
\]
For distinct particles, conditional covariance is zero given \(A\), so total covariance is \(\operatorname{Var}(m(A))\), giving exactly the displayed strictly positive expression. The continuous nonlattice finite-mean renewal theorem supplies convergence to this equilibrium law. At \(\gamma=1\), part 3 applies because the renewal mean remains infinite, yielding zero limiting covariance. This completes the sharp classification for this family.

## Verification
The standalone `check.py` (Python standard library only) checks the exact mixed-moment factorization for the corresponding beta-mark limit, multiple independent integrations of the finite-mean covariance formula, and directly simulates 1,600 full finite-time renewal realizations at \(N=2\), \(\alpha=0.24\), \(t=10^6\), with a fixed random seed. It passed. Numerical tests support but do **not** prove convergence; the proof is the conditional truncation and renewal argument above. Run `python check.py` after extracting the embedded files.

## Relationship to prior work
Das, Majumdar and Pal (2026), arXiv:2611.16733, rigorously analyze the single ballistic particle's finite-mean uniform steady state and its relaxation, and explicitly identify multi-particle spatial correlations as a future direction. Biswas, Majumdar and Pal (2025), arXiv:2504.13501, study correlated multi-searcher first-passage/target-search optimization under a different target-and-reset geometry; their main derivations concern search completion time, not an infinite-mean shared-clock positional law. The age theorem is the classical Dynkin–Lamperti result; Blanchet, Glynn and Thorisson (2015) separately identify the limiting age-to-current-cycle fraction in infinite-mean renewal processes. The present assertion is the joint particle **independence** and explicit correlation boundary after combining the physical conditional-speed law with these renewal facts, not a claim to have discovered the underlying renewal theorem.

## Limitations
Only fixed finite \(N\) and instantaneous whole-population resets are treated. The universal independent spatial limit requires \(N\alpha\le1\); the explicit positive-covariance formula requires the exact unit-cutoff power law \(F(v)=v^\alpha\). No joint \(N,t\to\infty\) limit, no finite-time rate of decorrelation, and no stationary distribution on the full age-augmented state in the infinite-mean regime are established. Independent external audit and exhaustive discovery of all possibly equivalent literature are not claimed.

## References
1. R. Das, S. N. Majumdar, A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733, first posted 12 November 2026. https://arxiv.org/abs/2611.16733
2. A. Biswas, S. N. Majumdar, A. Pal, *Target Search Optimization by Threshold Resetting*, arXiv:2504.13501, first posted 18 April 2025. https://arxiv.org/abs/2504.13501
3. J. Blanchet, P. Glynn, H. Thorisson, *On the Limiting Ratio of Current Age to Total Life for Null Recurrent Renewal Processes*, arXiv:1503.08374, 2015. https://arxiv.org/abs/1503.08374
4. Dynkin–Lamperti renewal-age theorem; see the discussion and reference to Bingham, Goldie and Teugels (1987), Theorem 8.6.3, in reference 3.
