# Exact hazard reversal thresholds for the discrete Rayleigh–Weibull lifetime law

## Finding

For parameters \(q\in(0,1)\), \(t>0\), \(\beta>0\), define a nonnegative-integer lifetime by
\[
\Pr(X\ge n)=q^{\Phi_{\beta,t}(n)},\qquad
\Phi_{\beta,t}(x)=(e^{t x^{\beta}}-1)^2,\quad n=0,1,2,\ldots.
\]
The model is the discrete Rayleigh–Weibull subfamily of the odds-generated Rayleigh class. Its discrete hazard is \(h_n=1-q^{\Phi(n+1)-\Phi(n)}\). The following classification is **global in integer age** and **exact**.

**Theorem.** If \(\beta\ge\tfrac12\), then \(h_{n+1}>h_n\) for every integer \(n\ge0\) and every \(t>0\). If \(0<\beta<\tfrac12\), there is a unique positive threshold \(t_n=t_n(\beta)\) for every \(n\ge0\), defined by
\[
(e^{t_n(n+2)^\beta}-1)^2-2(e^{t_n(n+1)^\beta}-1)^2+(e^{t_n n^\beta}-1)^2=0.
\]
These thresholds are strictly decreasing and tend to zero:
\[
t_0>t_1>t_2>\cdots>0,\qquad t_n\longrightarrow0.
\]
For every \(n\ge0\), \(h_{n+1}-h_n\) is negative, zero, or positive exactly when \(t-t_n\) is negative, zero, or positive. Thus the hazard either increases at all ages (possibly with equality only at ages zero and one), or decreases for a nonempty initial consecutive block of steps and increases thereafter. There is never an increasing-then-decreasing hazard step, and no two disjoint decreasing blocks or distinct flat steps.

The sharp all-age increasing-hazard boundary is
\[
t_0(\beta):\quad \frac{e^{2^\beta t_0}-1}{e^{t_0}-1}=\sqrt2 \qquad(0<\beta<\tfrac12),
\]
with increasing hazard exactly when \(t\ge t_0(\beta)\) (strictly increasing for \(t>t_0\), and just \(h_0=h_1\) at equality). This ordering and every threshold are independent of \(q\).

Furthermore, define \(z_\beta>0\) uniquely by
\[
\frac{z_\beta(2e^{z_\beta}-1)}{e^{z_\beta}-1}=\frac{1-\beta}{\beta}.
\]
Then the entire late-age threshold staircase obeys
\[
\boxed{\displaystyle\lim_{n\to\infty}(n+1)^\beta t_n(\beta)=z_\beta}\qquad(0<\beta<\tfrac12).
\]

## Assumptions and scope

Here \(x^\beta\) denotes the usual real nonnegative power for \(x\ge0\), with \(0^\beta=0\). The survival values are \(\Pr(X\ge n)\), not \(\Pr(X>n)\). The mass function is the positive telescoping difference \(\Pr(X=n)=q^{\Phi(n)}-q^{\Phi(n+1)}\). Since \(\Phi(0)=0\), \(\Phi\) increases strictly to infinity, this is a proper full-support probability distribution for all specified parameters. The result concerns the Rayleigh exponent \(2\), the ordinary Weibull-baseline odds \(G/(1-G)=e^{t x^\beta}-1\), and unit age spacing; it does **not** classify the larger classes with unequal odds powers or arbitrary outer generator exponents.

## Proof

**1. Hazard differences are second differences.** Let \(\Delta\Phi(n)=\Phi(n+1)-\Phi(n)\) and \(D_n(t)=\Phi(n+2)-2\Phi(n+1)+\Phi(n)\). Since \(q\in(0,1)\), the map \(a\mapsto1-q^a\) is strictly increasing; consequently the signs of \(h_{n+1}-h_n\) and \(D_n(t)\) agree.

**2. Each finite-age threshold exists and is unique.** The entire positive-power expansion, for \(x\ge0\), is
\[
\Phi(x)=\sum_{m=2}^\infty\frac{2^m-2}{m!}t^m x^{m\beta}.
\]
Therefore
\[
D_n(t)=\sum_{m=2}^\infty\frac{2^m-2}{m!}\,t^m\big[(n+2)^{m\beta}-2(n+1)^{m\beta}+n^{m\beta}\big].
\]
The term in square brackets has exactly the sign of \(m\beta-1\) for every \(n\ge0\), being the discrete second difference of a strictly concave or strictly convex positive power; it vanishes at \(m\beta=1\). If \(\beta\ge1/2\), all summands are nonnegative and at least one strictly positive, giving \(D_n(t)>0\).

For \(0<\beta<1/2\), the negative terms occur only at the finitely many low powers \(m\beta<1\), including \(m=2\), whereas all sufficiently high powers contribute positively. Write \(D_n(t)=B_n(t)-A_n(t)\), where \(A_n\) is the nonzero finite sum of magnitudes of negative terms and \(B_n\) the sum of strictly positive terms. Every exponent of \(t\) in \(B_n\) is larger than every exponent in \(A_n\). Thus \(t B_n'(t)/B_n(t)>t A_n'(t)/A_n(t)\), since each is a weighted average of its component exponents. It follows that \(B_n/A_n\) increases strictly from zero; it tends to infinity because \(D_n(t)>0\) for large \(t\), by dominance of \(\Phi(n+2)\). There is exactly one positive root \(t_n\), and \(D_n(t)\) changes from negative to positive there.

**3. Thresholds strictly decrease across ages.** Put \(z=t x^\beta\), \(f(z)=z(2e^z-1)/(e^z-1)\), and let \(\Phi''\) denote the ordinary second derivative for \(x>0\). Exact differentiation yields
\[
\Phi''(x)=P_t(x)g_t(x),\quad
P_t(x)=2t\beta x^{\beta-2}e^z(e^z-1)>0,\quad
g_t(x)=\beta f(z)+\beta-1.
\]
The function \(f\) increases strictly on \((0,\infty)\). In fact \(f(z)=2z+z/(e^z-1)\) and
\[
f'(z)-1=\frac{e^z(e^z-1-z)}{(e^z-1)^2}>0.
\]
Therefore \(g_t(x)\) is strictly increasing in \(x\), crossing zero exactly once when \(0<\beta<1/2\). Define the triangular kernel \(K(s)=s\) for \(0\le s\le1\), \(K(s)=2-s\) for \(1\le s\le2\), and zero elsewhere. For every \(n\ge0\), including \(n=0\) by integrable endpoint limiting,
\[
D_n(t)=\int_n^{n+2}K(x-n)P_t(x)g_t(x)\,dx.
\]
Normalize the positive weight \(K(x-n)P_t(x)\,dx\) to a probability measure \(\mu_n\). The ratio of the next kernel to the present kernel is zero to the left of the common support, strictly increasing on \((n+1,n+2)\), where it equals \((x-n-1)/(n+2-x)\), and infinite on the new right-hand support. The factor \(P_t\) cancels. Hence \(\mu_{n+1}\) strictly dominates \(\mu_n\) in monotone likelihood-ratio order, so \(\int g_t\,d\mu_{n+1}>\int g_t\,d\mu_n\) for strictly increasing \(g_t\). If \(t=t_n\), the latter integral vanishes. The former is then positive, so \(D_{n+1}(t_n)>0\). By Step 2 this entails \(t_{n+1}<t_n\).

**4. The boundary and asymptotics.** For \(n=0\), \(D_0=\Phi(2)-2\Phi(1)\), giving the displayed boundary. To analyze late ages set \(m=n+1\), \(t=c/m^\beta\), and \(H_c(s)=(e^{c s^\beta}-1)^2\). Then
\[
D_n(c/m^\beta)=H_c(1+1/m)-2H_c(1)+H_c(1-1/m)=m^{-2}H_c''(1)+O(m^{-4}),
\]
locally uniformly for \(c>0\). The sign of \(H_c''(1)\) is the sign of \(\beta f(c)+\beta-1\). Since \(f(0+)=1\), \(f\) strictly increases to infinity, the unique positive zero \(z_\beta\) exists for \(0<\beta<1/2\). Every fixed \(c<z_\beta\) eventually gives negative \(D_n(c/m^\beta)\), while every \(c>z_\beta\) eventually gives positive \(D_n(c/m^\beta)\). Root uniqueness squeezes \(m^\beta t_n\) to \(z_\beta\). In particular \(t_n\to0\), completing the classification. \(\square\)

## Verification

The script `check_hazard.py` checks the nontrivial second-derivative factorization symbolically, computes roots of the finite-age threshold equations at high precision for three shapes, checks their decreasing order and adjacent-step signs for 25 ages, and checks increasing-hazard differences for other shapes and ages. These finite tests support but do not replace Steps 2–4, which cover **all** integers and all permitted real parameters. At \(\beta=1/4\), the computed first thresholds are approximately \(t_0=1.459025832009218\), \(t_1=1.0668344567889997\), \(t_2=0.955198925455981\). In particular \(t=1\) yields \(h_0>h_1>h_2<h_3<h_4<\cdots\) for **every** \(q\in(0,1)\), rigorously on the stated interval comparisons and the threshold theorem; the decimal values are numerical diagnostics. For this shape \(z_{1/4}\approx1.248858112520993\).

## Relationship to prior work

Aboraya, Yousof, Hamedani and Ibrahim (2020) introduced the original discrete Rayleigh-G class and explicitly displayed its Weibull-baseline formula, including a two-parameter Weibull scale; its Weibull hazard discussion was graphical. Emam and collaborators (2023) considered a related generalized-odds Rayleigh generator and reported graphical hazard flexibility. Ma and Yan (2022) studied a related Weibull-Rayleigh discretization with a **quadratic baseline exponent**, not the varying Weibull exponent \(\beta\) here. Yousof and collaborators (2024) exhibited a broader Weibull-generated-G class with the exact nested Weibull formula as a subcase, but provided graphics and moment formulas rather than a global threshold staircase. The earlier papers establish the **distribution families and qualitative hazard shapes**; these are not claimed new. The present contribution is the complete discrete global hazard ordering, exact sharp age thresholds, and their late-age scaling law for the canonical squared-odds subfamily. The continuous Weibull-G generation mechanism predates all of these papers.

## Limitations

No assertion is made about the general unequal-power odds ratio, arbitrary outer Weibull-generator exponent, other baselines, or changes under nonunit observation intervals without a corresponding rescaling of \(t\). The exact thresholds are implicit transcendental roots, not elementary closed forms except for their defining equations. Literature priority has not been established exhaustively across all unindexed sources. The symbolic and numeric script is a reproducibility check, not independent certification.

## References

1. M. Aboraya, H. M. Yousof, G. G. Hamedani, M. Ibrahim, “A New Family of Discrete Distributions with Mathematical Properties, Characterizations, Bayesian and Non-Bayesian Estimation Methods,” *Mathematics* 8 (2020), 1648, published 24 September 2020, https://doi.org/10.3390/math8101648.
2. W. Emam et al., “A Novel Discrete Generator with Modeling Engineering, Agricultural and Medical Count and Zero-Inflated Real Data with Bayesian, and Non-Bayesian Inference,” *Mathematics* 11 (2023), 1125, published 23 February 2023, https://doi.org/10.3390/math11051125.
3. H.-J. Ma, Z.-Z. Yan, “Discrete Weibull-Rayleigh distribution: Properties and parameter estimations,” *Thermal Science* 26 (2022), 2627–2636, https://doi.org/10.2298/TSCI2203627M.
4. H. M. Yousof et al., “A New Discrete Generator with Mathematical Characterization, Properties, Count Statistical Modeling and Inference with Applications to Reliability, Medicine, Agriculture, and Biology Data,” *Pakistan Journal of Statistics and Operation Research* 20 (2024), 745–770, https://doi.org/10.18187/pjsor.v20i4.4616.
5. M. Bourguignon, R. B. Silva, G. M. Cordeiro, “The Weibull-G family of probability distributions,” *Journal of Data Science* 12 (2014), 53–68, cited as the continuous generator precursor by References 1 and 4.
