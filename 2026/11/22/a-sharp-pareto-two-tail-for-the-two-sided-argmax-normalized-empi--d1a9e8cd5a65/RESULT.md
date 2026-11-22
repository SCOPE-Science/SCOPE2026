# A sharp Pareto-two tail for the two-sided argmax-normalized empirical-distribution test

## Finding
For every fixed integer \(n\ge2\), under a completely specified continuous null distribution, the two-sided location-normalized Kolmogorov--Smirnov statistic introduced by Ferger has the sharp survival law
\[
\Pr\{V_n^*>t\}=\frac{2(n-1)!}{n^n}\,t^{-2}+O_n(t^{-4}),\qquad t\longrightarrow\infty.
\]
In particular, for every real \(q>0\),
\[
\mathbb E[(V_n^*)^q]<\infty\quad\Longleftrightarrow\quad q<2,
\]
and the truncated second moment has an exact logarithmic coefficient:
\[
\mathbb E\!\left[(V_n^*)^2\mathbf1_{\{V_n^*\le t\}}\right]
=\frac{4(n-1)!}{n^n}\log t+O_n(1).
\]
This is a fixed-sample result, not a simultaneous sample-size-and-threshold limit. The heavy-tail coefficient decreases as \(2\sqrt{2\pi/n}\,e^{-n}(1+O(1/n))\) when \(n\to\infty\).

## Assumptions and scope
Let \(X_1,\ldots,X_n\) be iid from a specified continuous CDF \(F_0\). Set \(U_i=F_0(X_i)\), and let \(0<U_{(1)}<\cdots<U_{(n)}<1\) be their order statistics, almost surely. Define
\[
 d_i=\max\!\left\{\frac{i}{n}-U_{(i)},\;U_{(i)}-\frac{i-1}{n}\right\},\quad
 R=\arg\max_{1\le i\le n}d_i,\quad
 V_n^*=\frac{d_R}{\sqrt{U_{(R)}(1-U_{(R)})}}.
\]
A deterministic smallest-index tie convention makes \(R\) well-defined; ties have probability zero. This matches the two-sided statistic in Ferger's equations (20)--(23), after the probability-integral transform. All moment statements concern the nonnegative statistic \(V_n^*\), not the unweighted Kolmogorov--Smirnov statistic.

## Proof
**1. Localization.** Since \(0\le d_i\le1\), the event \(V_n^*>t\), for \(t>2\), forces \(U_{(R)}(1-U_{(R)})<t^{-2}\), hence
\[
 U_{(R)}<2t^{-2}\quad\text{or}\quad U_{(R)}>1-2t^{-2}.
\]
If the first alternative occurs with \(R\ge2\), at least two independent uniform sample points fall in \([0,2t^{-2}]\). If the second occurs with \(R\le n-1\), at least two fall in \([1-2t^{-2},1]\). The combined probability of these noncorner events is \(O_n(t^{-4})\) by the binomial second-factorial-moment bound. Thus only \(R=1\) at the lower endpoint and \(R=n\) at the upper endpoint can contribute at order \(t^{-2}\).

**2. Exact lower-corner volume.** Put \(u=U_{(1)}\), and restrict \(0<u<1/(2n)\). Here \(d_1=1/n-u\). The event \(R=1\), up to zero-probability equalities, is equivalent to the simultaneous interval constraints
\[
 \frac{i-1}{n}+u<U_{(i)}<\frac{i}{n}-u,\qquad i=2,\ldots,n.
\]
These \(n-1\) intervals are ordered, mutually disjoint and each of length \(1/n-2u\). As the joint density of the uniform order statistics on their simplex is \(n!\), their exact volume at the lower corner is \(n!(1/n-2u)^{n-1}\,du\).

For all sufficiently large \(t\), the inequality \((1/n-u)/\sqrt{u(1-u)}>t\), for \(0<u<1/(2n)\), is equivalent to \(0<u<a_n(t)\), where the stable positive formula for the smaller quadratic root is
\[
 a_n(t)=\frac{2/n^2}{t^2+2/n+t\sqrt{t^2+4(n-1)/n^2}}.
\]
Therefore the exact contribution of the lower corner is
\[
 L_n(t)=n!\int_0^{a_n(t)}\left(\frac1n-2u\right)^{n-1}\,du
 =\frac{(n-1)!}{2}\left[n^{-n}-\left(\frac1n-2a_n(t)\right)^n\right].
\]
Reflection \(U_{(i)}\mapsto1-U_{(n+1-i)}\) preserves the statistic and maps the lower corner bijectively onto \(R=n\) near the upper endpoint. The latter contributes exactly \(L_n(t)\).

**3. Tail expansion.** The root satisfies \(a_n(t)=1/(n^2t^2)+O_n(t^{-4})\). Hence
\[
 L_n(t)=\frac{(n-1)!}{n^n}t^{-2}+O_n(t^{-4}).
\]
The two exact corner contributions and the localization remainder give the asserted expansion. All bounds hold for each fixed \(n\ge2\), and no finite simulation is used to justify the asymptotic statement.

**4. Moment consequences.** For any nonnegative random variable \(Y\) and real \(q>0\), \(\mathbb E Y^q=q\int_0^\infty t^{q-1}\Pr(Y>t)\,dt\), possibly infinite. The positive coefficient of \(t^{-2}\) makes this integral finite exactly for \(q<2\). Integration by parts of the truncated second moment yields \(2\int_0^t s\Pr(V_n^*>s)\,ds-t^2\Pr(V_n^*>t)\), proving the logarithmic expression. Stirling's formula gives the asserted sample-size asymptotic of the coefficient.

## Verification
Run the included standalone standard-library script with `python3 checker.py`. It checks the quadratic root numerically, the exact corner probability and its limiting constant for multiple sample sizes and thresholds, enumerates the categorical corner geometry through six bins, and independently simulates the original full finite-sample statistic. At packaging, it passed 96 assertions. The exact bin-volume and localization arguments above, not the simulations, establish the infinite-sample-threshold statements.

## Relationship to prior work
Ferger (first public arXiv version July 16, 2022; journal publication 2023) defines the one-sided and two-sided location-normalized empirical-process statistics. His Theorem 2.1 gives an exact finite-sample CDF for the **one-sided** statistic; Theorem 2.3 gives a weak limit for the **two-sided** statistic, whose exact finite-sample distribution the source says is not known. The present theorem concerns the exact **two-sided finite-sample far-tail coefficient**, absent from those statements. The known one-sided exact CDF is not claimed here as new.

The two-sided statistic is not the maximum of the two separately location-normalized one-sided statistics: its maximizing rank is selected **before** normalization. Consequently the one-sided CDF is not a direct two-sided tail formula. General order-statistic integration and Brownian-bridge argmax methods are relevant prior tools, but the calculation here isolates the exact two-sided endpoint-corner volume and the \(O_n(t^{-4})\) remainder.

## Limitations
No exact complete finite-sample CDF or uniform-in-\(n\) error estimate is proved. The inverse-square calibration is a far-tail expansion at fixed sample size; its practical accuracy at ordinary test levels is not claimed. The proof assumes an iid sample and a fully specified continuous null. The result has not undergone independent mathematical validation, and historical-priority searches cannot establish uniqueness.

## References
1. D. Ferger, *Exact and asymptotic goodness-of-fit tests based on the maximum and its location of the empirical process*, arXiv:2207.07947v1, first publicly posted 2022-07-16. https://arxiv.org/abs/2207.07947 ; https://arxiv.org/pdf/2207.07947 (especially pp. 4--10 and 12--14).
2. D. Ferger, same title, *Brazilian Journal of Probability and Statistics* **37** (2023), 140--154. https://doi.org/10.1214/23-BJPS564 .
3. Classical uniform order-statistic simplex density and binomial tail bounds, used as standard probability facts; no new authorship is asserted for them.
