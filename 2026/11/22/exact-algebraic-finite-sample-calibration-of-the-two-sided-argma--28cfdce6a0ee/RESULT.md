# Exact algebraic finite-sample calibration of the two-sided argmax-standardized Kolmogorov–Smirnov statistic

## Finding
For every integer \(n\ge1\) and every fully specified continuous null distribution, the exact null cumulative distribution function of Ferger's two-sided maximizing-location-standardized Kolmogorov–Smirnov statistic is given by a **finite, constructive piecewise-algebraic formula**. In particular, no numerical integration or simulation is required to evaluate the CDF at any nonnegative rational threshold. The formula conditions on the winning order statistic, decomposes its remaining admissible order-statistic region into affine bins, and integrates rational polynomials over endpoints involving only quadratic radicals.

At the dimensionless threshold \(t=2\), two nontrivial exact values are
\[
\Pr\{V_2^*\le2\}=\frac{43}{25}-\frac{2\sqrt5}{5},\qquad
\Pr\{V_3^*\le2\}=-\frac{8099}{3375}+\frac{376\sqrt{11}}{375}.
\]
The exact \(95\%\) null quantile for \(n=3\) lies strictly between \(2.2981\) and \(2.2982\), as shown by strict algebraic comparisons of the CDF with \(19/20\). This supplies an exact finite-threshold calibration for the previously asymptotically calibrated two-sided statistic.

## Assumptions and scope
Let \(X_1,\ldots,X_n\) be independent samples from a *fully specified, continuous* null CDF \(F_0\), and put \(U_i=F_0(X_i)\). Then the \(U_i\) are independent uniform variables on \((0,1)\), with order statistics \(U_{(1)}<\cdots<U_{(n)}\) almost surely. Define
\[
 d_i^+=\frac{i}{n}-U_{(i)},\quad d_i^-=U_{(i)}-\frac{i-1}{n},\quad d_i=\max\{d_i^+,d_i^-\},\quad K_n=\max_{1\le i\le n}d_i.
\]
Let \(R\) be the index of the maximum \(d_i\) (arbitrary deterministic tie-breaking is harmless off a null set) and set
\[
 V_n^*=\frac{K_n}{\sqrt{U_{(R)}(1-U_{(R)})}}.
\]
This is the two-sided statistic in Ferger (2022/2023), not the maximum of two individually studentized one-sided statistics. All exact statements concern fixed finite \(n\), an independent sample and a specified continuous null; no nuisance parameters are estimated.

For \(j=1,\ldots,n\) and a sign \(s\in\{+,-\}\), put
\[
 c_j=\frac{2j-1}{2n},\quad
 k_{j,+}(u)=\frac jn-u,\qquad k_{j,-}(u)=u-\frac{j-1}{n},
\]
with sign domains \(D_{j,+}=(0,c_j)\) and \(D_{j,-}=(c_j,1)\). For fixed \(u\) in the appropriate domain write \(k=k_{j,s}(u)\) and
\[
 A_i(u)=\frac in-k,\qquad B_i(u)=\frac{i-1}{n}+k\quad(i\ne j).
\]
Let \(L_{j,s}(u)\) be the Lebesgue volume of all \(0<y_1<\cdots<y_{j-1}<u\) satisfying \(A_i(u)\le y_i\le B_i(u)\) for \(i<j\), and \(R_{j,s}(u)\) the volume of all \(u<y_{j+1}<\cdots<y_n<1\) satisfying the analogous constraints for \(i>j\). An empty family has volume \(1\). These quantities are **volumes**, not conditional probabilities.

## Proof
**1. Exact disjoint winner decomposition.** The joint density of the ordered uniform sample is \(n!\) on the open ordering simplex. Except on finitely many probability-zero hyperplanes, one of the \(2n\) affine deviations \(d_i^+,d_i^-\) is uniquely maximal. Its label is \((j,s)\). Conditional on \(U_{(j)}=u\), its value is \(k=k_{j,s}(u)\); the condition that this deviation is maximal is equivalent to (a) \(u\in D_{j,s}\) and (b) for every \(i\ne j\), both \(d_i^+\le k\) and \(d_i^-\le k\), or equivalently \(A_i(u)\le U_{(i)}\le B_i(u)\). Because the ordering constraints split at \(u\), the remaining simplex volume factors as \(L_{j,s}(u)R_{j,s}(u)\). Consequently, for all \(t\ge0\),
\[
 H_n(t):=\Pr(V_n^*\le t)=n!\sum_{j=1}^n\sum_{s\in\{+,-\}}\int_{D_{j,s}\cap\{k_{j,s}(u)\le t\sqrt{u(1-u)}\}}L_{j,s}(u)R_{j,s}(u)\,du. \tag{1}
\]
Every point of the ordering simplex outside a measure-zero set belongs to exactly one term; there is no double counting and no asymptotic approximation.

**2. Exact radical integration endpoints.** For \(a\in[0,1]\) and \(t>0\), define
\[
 \rho_\pm(a,t)=\frac{2a+t^2\pm t\sqrt{t^2+4a(1-a)}}{2(1+t^2)}.
\]
For \(s=+\) take \(a=j/n\); for \(s=-\) take \(a=(j-1)/n\). In both cases the inequality in (1) is exactly
\[
 \rho_-(a,t)\le u\le\rho_+(a,t),
\]
by solving \((u-a)^2\le t^2u(1-u)\). Therefore each sign domain contributes its intersection with one explicit radical interval.

**3. Exact rational-polynomial simplex volumes.** On each side of the fixed winning point, collect the affine lines \(0,1,u,A_i(u),B_i(u)\). Insert every rational crossing of two distinct lines in \((0,1)\), along with \(0,1,c_j\). These finitely many rational breakpoints partition each sign domain into chambers on which the order of all lines is constant. Intersect the lines with the relevant side \([0,u]\) or \([u,1]\), yielding sorted bin endpoints \(z_0(u)<\cdots<z_h(u)\) that are affine in \(u\) with rational coefficients. For each bin, the set of order-statistic indices allowed to occupy its interior is constant throughout the chamber.

The volume of a simplex of \(m\) ordered observations with individual admissible intervals is computed by the following finite bin-count recurrence. Put \(P_0(0)=1\), \(P_0(c)=0\) for \(c>0\). If a current bin of width \(\delta=z_{h+1}-z_h\) can accommodate each of the next \(r\) consecutive order-statistic indices \(c+1,\ldots,c+r\), update
\[
 P_{h+1}(c+r)\mathrel{+}=P_h(c)\frac{\delta^r}{r!},\qquad 0\le c+r\le m.
\]
The case \(r=0\) is always admissible. The factor \(\delta^r/r!\) is the exact ordered-simplex volume of \(r\) observations in one bin. Enumerating the successive counts gives a bijection with every admissible configuration of ordered observations, so the final coefficient \(P_h(m)\) is the desired volume, **not** an approximation. Because all bin widths are rational-affine in \(u\), this recurrence proves that both \(L_{j,s}(u)\) and \(R_{j,s}(u)\) are rational polynomials on each rational chamber. Their product has degree at most \(n-1\).

**4. Terminating exact CDF algorithm and piecewise algebraicity.** Intersect each rational chamber with the radical interval from step 2, integrate its resulting rational polynomial exactly using an antiderivative, and sum the contributions with multiplier \(n!\). All comparisons and operations can be made in real algebraic number fields for rational \(t\). Since only finitely many chambers and radical intersections occur, (1) is a finite algebraic formula for every rational threshold. For arbitrary real \(t>0\), the same formulas produce finitely many algebraic-function branches in \(t\), with changes only where a radical endpoint crosses a rational chamber boundary. Thus the full CDF is piecewise algebraic. No indefinite integrations, convergence assumptions or finite-simulation extrapolation remain.

**5. Exact consequences.** When \(n=1\), direct evaluation gives \(H_1(t)=0\) for \(0\le t\le1\), and \(H_1(t)=1-2/(1+t^2)\) for \(t>1\). Executing steps 1–4 for \(n=2,3\) at \(t=2\) gives the radical expressions in the Finding section. For \(n=3\), exact signs of \(H_3(22981/10000)-19/20\) and \(H_3(22982/10000)-19/20\) are respectively negative and positive; the claimed quantile enclosure follows from the CDF and continuity of its distribution.

## Verification
The accompanying `exact_ks_argmax.py` implements the chamber construction, ordered-bin recurrence, exact symbolic polynomial integration, and **exact algebraic sign comparisons** (SymPy). `verification_checks.py` performs 120 assertions: the hand-derived \(n=1\) law, exact \(t=2\) radical identities at \(n=1,2,3,4\), algebraically certified \(95\%\) quantile bracketing, CDF bounds and monotonicity, and seeded direct-sample simulations at \(n=1,\ldots,6\) and three thresholds. All assertions passed when run with Python 3, SymPy and NumPy. The simulations are diagnostic only; the finite partition proof above establishes the theorem for every integer \(n\).

For reproducibility, install SymPy and NumPy, place the scripts in the same directory, and run `python3 verification_checks.py`; `python3 exact_ks_argmax.py 3 2` prints the exact \(n=3\) expression. The code does not access a network and does not load source papers or private files.

## Relationship to prior work
Dietmar Ferger, *Exact and asymptotic goodness-of-fit tests based on the maximum and its location of the empirical process*, arXiv:2207.07947v1 (2022), introduced this statistic. Section 2, Theorem 2.1, supplies a finite-sample CDF for the **one-sided** variant, and Theorem 2.3 supplies an **asymptotic** two-sided law. The paper explicitly notes that the exact finite-sample law for the two-sided statistic was not known. The present result closes that precise finite-sample gap; it does **not** misidentify the two-sided statistic with the maximum of the two one-sided, separately standardized statistics.

Steck's classical rectangle-probability techniques for uniform order statistics are credited as a generic predecessor for deterministic rank bands; they do not, by themselves, give the present statistic's winner-conditioned radical integration and exact full CDF. Earlier analysis of this specific statistic established a fixed-sample inverse-square far-tail coefficient only, not its full finite-threshold CDF or critical-value enclosure. Such a tail theorem neither implies nor is needed by the exact formula here. Ferger's 2018 reflected-Brownian-bridge result concerns a limiting stochastic process, not the finite-\(n\) law computed here.

## Limitations
The exact symbolic algorithm can have substantial combinatorial and expression-size cost as \(n\) grows; no polynomial-time complexity or large-sample numerical efficiency is claimed. The theorem applies only under a fully specified continuous simple null, not after estimating \(F_0\), and does not assess power or finite-sample behavior under alternatives. A numerical implementation using floating-point arithmetic instead of the included exact comparisons need not certify endpoints. Independent mathematical verification and exhaustive historical-priority review have not been performed.

## References
1. D. Ferger, *Exact and asymptotic goodness-of-fit tests based on the maximum and its location of the empirical process*, arXiv:2207.07947v1, first public 2022-07-16, https://arxiv.org/abs/2207.07947 and https://arxiv.org/pdf/2207.07947 . Journal publication: *Brazilian Journal of Probability and Statistics* **37** (2023), 140–154, https://doi.org/10.1214/23-BJPS564 .
2. G. P. Steck, *Rectangle probabilities for uniform order statistics and the probability that the empirical distribution function lies between two distribution functions*, *Annals of Mathematical Statistics* **42** (1971), 1–11, https://www.jstor.org/stable/2958458 .
3. D. Ferger, *On the supremum of a Brownian bridge standardized by its maximizing point with applications to statistics*, *Statistics & Probability Letters* **134** (2018), 63–69, https://doi.org/10.1016/j.spl.2017.10.008 .
