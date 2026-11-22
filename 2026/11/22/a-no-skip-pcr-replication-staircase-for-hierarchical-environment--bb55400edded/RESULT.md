# A no-skip PCR replication staircase for hierarchical environmental-DNA sampling

## Finding

In a two-stage environmental-DNA (eDNA) detection experiment with a positive field-sample acquisition cost, the optimal number of PCR replicates per independent field sample, when judged by the exponential rate of missed detection **per unit expenditure**, increases through *every* integer without skipping as field-DNA availability increases. The thresholds have an explicit geometric-over-linear asymptotic. Near certain field capture, the continuously relaxed optimal replicate count obeys a logarithmic law with a negative log-log correction.

Specifically, write \(a,b>0\) for the fixed per-field-sample and per-PCR costs, \(0<p,q<1\) for field DNA capture and conditional PCR success probabilities, \(r=1-q\), and \(c=-\log r\). For each integer \(m\ge1\), let
\[
 H_m(p)=-\log\bigl(1-p+p r^m\bigr),\qquad E_m(p)=\frac{H_m(p)}{a+bm}.
\]
Let \(m_0\) be the **largest** integer maximizing \((1-r^m)/(a+bm)\). Then there are unique numbers \(p_m\in(0,1)\) for all integers \(m\ge m_0\) such that \(E_m(p_m)=E_{m+1}(p_m)\), and
\[
0<p_{m_0}<p_{m_0+1}<\cdots<1,\qquad\lim_{m\to\infty}p_m=1.
\]
The unique optimal PCR count is \(m_0\) when \(0<p<p_{m_0}\), and it is \(m\) when \(p_{m-1}<p<p_m\), for \(m>m_0\). Exactly two *adjacent* counts \(m,m+1\) tie at \(p=p_m\). Thus no intermediate count is bypassed. The large-count switching boundary satisfies
\[
1-p_m\sim\frac{a}{b}\frac{c r^{m+1}}{(1-r)m} \quad (m\to\infty).
\]
If real-valued \(m>0\) is allowed in the exponent-per-cost formula, its unique maximizer \(m_c(p)>0\) is strictly increasing with \(p\), and, as \(p\uparrow1\),
\[
c m_c(p)=L-\log L+\log(ca/b)+o(1),\qquad L=\log\frac1{1-p}.
\]
This continuous optimum need not be an admissible integer PCR count. A corresponding integer optimum is within one integer of \(m_c(p)\), subject to the lower bound \(m\ge1\). For \(p=1\), no finite replicate count maximizes \(E_m\): it increases strictly toward \(c/b\).

## Assumptions and scope

A target species is known to occupy the surveyed site. Each separately collected field sample has probability \(p\) of containing amplifiable target DNA, independently of other field samples. Conditional on capture in a particular sample, each of its \(m\) PCR replicates detects it independently with common probability \(q\). Conditional on absence of target DNA, every replicate is negative: **false positives are excluded**. A sample costs \(a+bm\), with \(a>0\) the collection/extraction cost and \(b>0\) the marginal PCR cost. Counts \(m\) are positive integers for the operational staircase; the real-valued extension is purely a smooth optimization benchmark.

The objective is the **miss-detection exponent per expenditure**, \(E_m(p)\), not occupancy-estimator variance, posterior classification loss, a finite-integer-budget optimizer, or a requirement to obtain two or more positive PCRs. With \(n\) independent samples each processed at the same count \(m\), the probability of no positive PCR anywhere is exactly \(\exp[-nH_m(p)]\), and the incurred cost is \(n(a+bm)\). Consequently, \(E_m\) is exactly the negative log failure probability divided by cost for every \(n\ge1\). For a fixed budget allowing real-valued sample count \(n=B/(a+bm)\), maximizing detection is equivalent to maximizing \(E_m\). With integer sample counts and an arbitrary finite budget, floor effects are outside this theorem.

## Proof

**1. Detection law.** Conditional on availability, all \(m\) PCRs miss with probability \(r^m\); without captured DNA they all miss. Thus a sample misses with probability \(1-p+p r^m\), and independent samples yield the stated exponent.

**2. Strict single-peakedness.** Set \(y=cm\), \(\alpha=ca/b\), and
\[
\psi_p(y)=-\log(1-p+p e^{-y}).
\]
For \(y>0\), \(\psi_p(0)=0\), \(\psi_p'>0\), and \(\psi_p''=-p(1-p)e^{-y}/(1-p+p e^{-y})^2<0\). The relaxed objective, up to the positive constant \(c/b\), is \(\psi_p(y)/(\alpha+y)\). Its derivative has the sign of \(K(y)=(\alpha+y)\psi_p'(y)-\psi_p(y)\). Because \(K(0)=\alpha p>0\), \(K'(y)=(\alpha+y)\psi_p''(y)<0\), and \(K(y)\to\log(1-p)<0\) as \(y\to\infty\), it has exactly one zero. The objective strictly increases before this zero and strictly decreases after it. Therefore its integer maximizers are one index or two adjacent indices. Also, three adjacent indices cannot tie, as that would make the strictly concave \(\psi_p\) collinear at three integer-spaced arguments.

**3. Single crossings for adjacent counts.** Put \(v_m=1-r^m\) and \(F(x)=-\log(1-x)\). For \(m\ge1\),
\[
\frac{E_{m+1}(p)}{E_m(p)}=\frac{a+bm}{a+b(m+1)}\frac{F(v_{m+1}p)}{F(v_m p)}.
\]
The last ratio is strictly increasing in \(p\), because the logarithmic elasticity of \(F\) is \(xF'(x)/F(x)=(e^z-1)/z\), with \(z=-\log(1-x)>0\), and this is strictly increasing in \(z\). Hence adjacent rankings cross at most once, from \(m\) to \(m+1\) as \(p\) rises.

As \(p\downarrow0\), \(E_m(p)/p\to v_m/(a+bm)\). This last sequence is the restriction of a strictly single-peaked continuous curve, by the preceding derivative calculation applied to \(v(y)=1-e^{-y}\). Its largest maximizing index \(m_0\) exists and is finite. For every \(m\ge m_0\), the small-\(p\) ratio \(E_{m+1}/E_m\) is strictly below one, whereas for \(p\uparrow1\), \(H_m(p)\to cm\), and \(cm/(a+bm)\) is strictly increasing in \(m\) because \(a>0\). Therefore each \(p_m\) exists uniquely in \((0,1)\). All indices below \(m_0\) lose to \(m_0\) at positive \(p\), because their adjacent ratio starts at least one and subsequently increases.

If \(p_{m+1}<p_m\), choosing \(p\) strictly between them would give \(E_m>E_{m+1}<E_{m+2}\), contrary to the strictly single-peaked sequence. Equality would force three adjacent ties, already excluded. Thus \(p_{m+1}>p_m\), and the complete optimal-index staircase follows. For any fixed \(p<1\), \(H_m(p)\) is bounded as \(m\to\infty\), so \(E_m(p)\to0\), forcing \(p_m\to1\).

**4. Switch asymptotic.** Write \(A=a/b\) and \(\delta=1-p\). The equality between \(m\) and \(m+1\) is
\[
D_m(\delta)=(A+m+1)H_m(1-\delta)-(A+m)H_{m+1}(1-\delta)=0.
\]
At \(\delta=0\), \(D_m(0)=-cA\). For any fixed \(k>0\), substitute \(\delta=k r^m/m\). From
\[
H_m(1-\delta)=cm-\log(1+\delta(r^{-m}-1)),
\]
we obtain \(H_m=cm-k/m+O(m^{-2})\) and \(H_{m+1}=c(m+1)-k/(rm)+O(m^{-2})\), hence
\[
D_m(k r^m/m)=-cA+k(r^{-1}-1)+O(m^{-1}).
\]
For every fixed \(k\) on either side of \(cA/(r^{-1}-1)\), these expressions have opposite signs for all large \(m\). The already-proved uniqueness of the adjacent crossing brackets the unique \(\delta_m=1-p_m\) between the two test scales, giving \(\delta_m\sim cA r^m/[(r^{-1}-1)m]\), equivalently the asserted formula.

**5. Monotonicity and log-log law for the relaxed count.** The unique root can be expressed as \(R(y,p)=\alpha\), where \(R(y,p)=\psi_p(y)/\psi_p'(y)-y\). Its derivative \(R_y=-\psi_p\psi_p''/(\psi_p')^2\) is strictly positive. With \(\epsilon=(1-p)/p\), direct differentiation gives
\[
\partial_\epsilon R=e^y\{\psi_p(y)-p(1-e^{-y})\}>0,
\]
since \(-\log(1-x)>x\) for \(0<x<1\). Hence increasing \(p\) increases the root \(y=cm_c(p)\). At any fixed \(y\) the derivative sign tends to positive as \(p\uparrow1\), implying \(cm_c(p)\to\infty\). Let \(L_\epsilon=\log(1/\epsilon)\) and evaluate the derivative numerator at \(y=L_\epsilon-\log L_\epsilon+t\) for each fixed \(t\). Using \(\epsilon e^y=e^t/L_\epsilon\), its value tends to \(\alpha-e^t\). Strict monotonicity of the derivative numerator and bracketing with \(t=\log\alpha\pm\eta\) prove \(y=L_\epsilon-\log L_\epsilon+\log\alpha+o(1)\). Because \(L_\epsilon=L+o(1)\), the announced expression follows.

## Verification

Run `python3 check.py` using only the Python standard library. The checker evaluates the detection formula, monotonic ranking transitions, a sample of exact-cost integer maxima, the relaxed stationary equation, and the threshold asymptotic at finite test indices. These finite diagnostics test examples and consistency; the quantifiers for all admissible parameters and all integer counts are established by the preceding analytic proof, **not** by enumeration.

For \(a=b=1\), \(q=1/2\), the low-availability limit has a tie between one and two PCRs, so \(m_0=2\), and every \(p>0\) sufficiently small favors two. The first three positive transition values are approximately \(p_2=0.835996736446\), \(p_3=0.955100082793\), and \(p_4=0.984953065849\).

## Relationship to prior work

The hierarchical eDNA observation model, separating field DNA availability from PCR amplification, is established by Schmidt et al. (2013) and used explicitly by Willoughby et al. (2016) and Lugg et al. (2018). Moore et al. (2014) and Smart et al. (2016) address fixed-cost decisions about field visits and sampling intensity, but optimize different stochastic detection models and cost levels. Lugg et al. account for a prescribed number of PCR repeats per sample and optimize ecological site replication, rather than optimizing the PCR-repeat count itself. The result here applies an independent Bernoulli-availability and conditional-PCR mechanism to optimize a laboratory replicate count with explicit cost, and yields the ordered integer phase diagram and its sharp accumulation rate. These are claim-level distinctions, not assertions that earlier research has no transferable methods. The analysis does not establish absolute historical priority across uninspected work.

## Limitations

Only true-positive recovery is modeled: correlated samples, contamination/false-positive PCRs, inhibitory effects, finite reagent capacity, imperfect prior calibration, nonconstant test sensitivity with replicate count, integer sample-budget floors, and objectives based on estimating occupancy or controlling posterior errors are outside scope. The divergence near \(p=1\) assumes the field sample's conditional PCR attempts are fully independent even at very large \(m\); practical replication limits can remove it. An exact mathematical cost-efficiency theorem is not a validated operational protocol.

## References

- Schmidt, B. R., Kéry, M., Ursenbacher, S., Hyman, O. J., and Collins, J. P. (2013). *Site occupancy models in the analysis of environmental DNA presence/absence surveys*. First online 2013-03-28. https://doi.org/10.1111/2041-210X.12052
- Moore, A. L., McCarthy, M. A., Parris, K. M., and Moore, J. L. (2014). *The optimal number of surveys when detectability varies*. Published 2014-12-19. https://doi.org/10.1371/journal.pone.0115345
- Willoughby, J. R., et al. (2016). *The importance of including imperfect detection models in eDNA experimental design*. First online 2016-04-01. https://doi.org/10.1111/1755-0998.12531
- Smart, A. S., et al. (2016). *Assessing the cost-efficiency of environmental DNA sampling*. First online 2016-05-29. https://doi.org/10.1111/2041-210X.12598
- Lugg, W. H., et al. (2018). *Optimal survey designs for environmental DNA sampling*. First online 2017-12-05. https://doi.org/10.1111/2041-210X.12951
