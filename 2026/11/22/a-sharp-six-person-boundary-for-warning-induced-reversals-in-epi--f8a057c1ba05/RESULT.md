# A sharp six-person boundary for warning-induced reversals in epidemic size

## Finding

A warning mechanism triggered by *all* of several newly infected sentinels can make the expected **final** epidemic size decrease as the baseline biological transmissibility increases. In the defined two-generation contact-and-warning network, this happens if and only if

\[
m\bigl[k-(k+2)\bar r\bigr]>k+1,
\qquad \bar r=\frac1m\sum_{i=1}^{m}r_i.
\]

Here \(k\ge1\) is the number of warning sentinels, \(m\ge1\) is the number of terminal individuals and \(r_i\in[0,1]\) is the residual biological transmission multiplier when terminal \(i\) receives the warning. Whenever the inequality holds, the expected size has **exactly one strict interior maximum** and decreases strictly thereafter. Otherwise it increases strictly with transmissibility. The threshold is unchanged if target protection is heterogeneous but has the same arithmetic mean.

Within this precise family, six individuals are necessary and sufficient for an interior reversal. The six-person perfect-warning witnesses have \((k,m)=(1,3)\) or \((2,2)\). This minimality is *not* a statement about arbitrary epidemic networks.

## Assumptions and scope

Define a finite directed two-layer network with \(n=k+m+2\) distinct individuals: one source \(s\), one mediator \(a\), \(k\) sentinels \(w_1,\ldots,w_k\) and \(m\) terminals \(v_1,\ldots,v_m\). The directed biological arcs are \(s\to a\), \(s\to w_j\) for each \(j\), and \(a\to v_i\) for each \(i\). The social layer sends a deterministic warning from the sentinel group to every terminal only when all \(k\) sentinels have become infected. There are no other contacts.

At time zero only \(s\) is infectious. In the first step, the source independently infects the mediator and each sentinel, each with probability \(p\in[0,1]\). The source is then removed. At the next step, before any mediator-to-terminal transmissions, each terminal receives the warning exactly when every sentinel was infected. If \(a\) was infected, each terminal is infected independently with conditional probability \(p\) when not warned and \(p r_i\) when warned, with fixed \(0\le r_i\le1\); otherwise no terminal can be infected. The mediator and sentinels are removed after this step. All infected individuals, including the initial source and infected warning sentinels, are counted in final size \(X\). The model has no further generations and no reinfection.

The warning is a deliberately idealized unanimous confirmation rule. The biological and social layers have different specified arc dynamics. This model is not assumed to be a literal specialization of other threshold- or prevalence-based awareness processes.

## Proof

**1. Exact expectation.** Let \(A\) be the indicator that the mediator is infected in the first step; let \(W_j\) indicate whether sentinel \(j\) is infected. These \(k+1\) Bernoulli indicators are independent with success probability \(p\). Put \(H=\prod_{j=1}^k W_j\); then \(H=1\) if and only if the warning is activated, and \(\mathbb E H=p^k\). Moreover \(A\) and \(H\) are independent. If \(C_i\) denotes infection of terminal \(i\), conditioning on the first-step outcomes gives

\[
\Pr(C_i=1\mid A,H)=A p\bigl[1-(1-r_i)H\bigr].
\]

It follows that \(\mathbb E C_i=p^2[1-(1-r_i)p^k]\). Since \(X=1+A+\sum_j W_j+\sum_i C_i\), linearity of expectation yields the **exact finite** identity

\[
E(p):=\mathbb E X
=1+(k+1)p+mp^2-p^{k+2}\sum_{i=1}^{m}(1-r_i)
=1+(k+1)p+mp^2-m(1-\bar r)p^{k+2}.
\]

No independence of the terminal indicators is needed to sum their means. In particular, replacing the heterogeneous list by its mean leaves this *expectation* unchanged, although it need not preserve the distribution or variance.

**2. Sharp all-parameter criterion.** Write \(h=1-\bar r\), so \(0\le h\le1\). Differentiation gives

\[
E'(p)=(k+1)+2mp-(k+2)mh p^{k+1},
\qquad E''(p)=2m-(k+1)(k+2)mh p^k.
\]

If \(h=0\), the derivative is strictly positive. Otherwise \(E''\) is strictly decreasing on \((0,1)\), and thus \(E'\) first increases and then decreases (or is monotone on this interval). Consequently the minimum of \(E'\) over \([0,1]\) is at an endpoint, and since \(E'(0)=k+1>0\), a negative derivative occurs at some interior point if and only if \(E'(1)<0\). The latter is exactly

\[
(k+1)-m\bigl[k-(k+2)\bar r\bigr]<0.
\]

In that case, \(E'\) has exactly one zero \(p_*\in(0,1)\): it cannot vanish while increasing from its positive initial value, and is strictly decreasing after its only possible turning point. Therefore \(E\) strictly increases before \(p_*\) and strictly decreases afterwards. The maximizing \(p_*\) is the unique solution in \((0,1)\) to

\[
(k+2)m(1-\bar r)p_*^{k+1}-2mp_*=k+1.
\]

If the displayed strict inequality fails, both endpoint values of \(E'\) are nonnegative, and its unimodal shape forces \(E'(p)>0\) for all \(0\le p<1\); the expected size is strictly increasing, even when its derivative vanishes at \(p=1\).

Equivalently, for \(\bar r<k/(k+2)\) an interior reversal occurs exactly when \(m>(k+1)/(k-(k+2)\bar r)\); for larger \(\bar r\) no number of terminals in this family suffices. In the large-terminal limit the residual-multiplier threshold approaches \(k/(k+2)\).

**3. Sharp minimum within the family.** An interior reversal is easiest when all \(r_i=0\), in which case it requires \(mk>k+1\), equivalently \(m>1+1/k\). For \(k=1\), the smallest integer \(m\) is three; for every \(k\ge2\), the smallest is two. Since total population is \(n=k+m+2\), the minimum is \(n=6\), attained exactly by \((k,m)=(1,3)\) and \((2,2)\). Increasing a residual multiplier can only weaken the negative derivative term, so no protection choices allow a smaller population to reverse.

For illustration, with \(k=1\), \(m=3\), and all \(r_i=0\),

\[
E(p)=1+2p+3p^2-3p^3,
\quad p_*=(1+\sqrt3)/3=0.9106836025\ldots,
\]

and \(E(p_*)>E(1)=3\). A distinct six-person configuration, \(k=m=2\) with perfect warning, has \(E(p)=1+3p+2p^2-2p^4\) and a unique maximum at \(p_*\approx0.9466445982\).

## Verification

The companion `CHECKER.py` runs with standard Python 3. It independently enumerates first-generation mediator/sentinel outcomes and every possible terminal infection pattern using exact rational probabilities, then compares the resulting full-state expected final size to the formula. It also performs rational-grid derivative-sign and family-minimality checks. On the saved standalone code, **58,578 exact-rational assertions passed**. These finite checks are diagnostic; the preceding conditioning and derivative arguments prove the all-integer, all-parameter statements without extrapolating from enumeration.

## Relationship to prior work

Van Wesemael, Rocha and Baetens (arXiv:2404.16466; first public 2024-04-25) already reported that increasing transmission can decrease epidemic extent when awareness cascades interact with infection on multiplex networks (especially their Section 3.2.2). The qualitative phenomenon is **not claimed as new** here. Their process uses threshold-based awareness and numerically studied network ensembles; the exact fixed two-generation unanimous-sentinel family, heterogeneous-target mean reduction, necessary-and-sufficient inequality and six-person family-specific minimum are not statements established in the inspected text.

Granell, Gomez and Arenas (arXiv:1405.4480) analyze epidemic–awareness competition and its metacritical threshold in multiplex networks. Kan and Zhang (arXiv:1502.00392) derive invasion thresholds from Markovian awareness–epidemic dynamics. Feng and colleagues (arXiv:2406.03763) study information-dissemination nodes and epidemic invasion thresholds. These are closely relevant mechanisms but their invasion-threshold or mean-field comparisons do not imply the finite uniform-transmission **final-size** derivative classification above. No assertion of complete global literature priority follows from these comparisons.

## Limitations

This is a stylized two-round model with one initially infected source, deterministic social alert delivery conditional on unanimous sentinel infection, no warning delays, prescribed directionality, and no further transmission generations. The alert rule is intentionally different from ordinary local-awareness dynamics. The six-person minimality refers **only to the specified one-mediator/unanimous-sentinel/fan family**, not to all multiplex networks. The mean-only heterogeneity invariance is not a distributional equivalence. The result does not show that real epidemics shrink as biological transmissibility increases, and it gives no clinical policy guidance or validated control recommendation. Historical priority beyond inspected sources is not independently certified.

## References

1. T. Van Wesemael, L. E. C. Rocha and J. M. Baetens, *Epidemic risk perception and social interactions lead to awareness cascades on multiplex networks*, arXiv:2404.16466 (first posted 2024-04-25), https://arxiv.org/abs/2404.16466; Journal of Physics: Complexity (2025), https://doi.org/10.1088/2632-072X/adb897.
2. C. Granell, S. Gomez and A. Arenas, *Competing spreading processes on multiplex networks: awareness and epidemics*, arXiv:1405.4480 (2014), https://arxiv.org/abs/1405.4480.
3. J.-Q. Kan and H.-F. Zhang, *Effects of awareness diffusion and self-initiated awareness behavior on epidemic spreading*, arXiv:1502.00392 (2015), https://arxiv.org/abs/1502.00392.
4. M. Feng, X. Li, Y. Li and Q. Li, *The impact of nodes of information dissemination on epidemic spreading in dynamic multiplex networks*, arXiv:2406.03763 (first posted 2024-06-06), https://arxiv.org/abs/2406.03763.
