# A reentrant dispersion phase diagram for one-inflated zero-truncated negative-binomial counts

## Finding

The following **shape-dependent phase diagram** classifies underdispersion, equidispersion and overdispersion for the entire one-inflated zero-truncated negative-binomial family. The probability model and its first two moments are known; the contribution here is the complete set of sign transitions and the sharp structural boundary at shape \(r=1\).

Let \(r>0\), \(0<q<1\), and let \(N\) have probability mass
\[
\Pr\{N=n\}=\frac{(r)_n}{n!}(1-q)^r q^n,\qquad n=0,1,\ldots.
\]
Here \((r)_n\) is the rising factorial. Let \(Y\) have the conditional law of \(N\) given \(N>0\), and independently construct \(X\) as the constant \(1\) with probability \(1-t\) and as \(Y\) with probability \(t\), for \(0\le t\le1\). Thus \(1-t\) is the additional mass-at-one mixture weight.

Define
\[
\begin{aligned}
s&=1-(1-q)^r, &z&=\frac{q}{1-q},\\
\mu&=\frac{rz}{s}, &F_2&=\frac{r(r+1)z^2}{s},\\
B&=\mu-1, &A&=F_2-2\mu+2.
\end{aligned}
\]
Both \(A\) and \(B\) are strictly positive. The exact variance-minus-mean is
\[
\boxed{\operatorname{Var}(X)-\mathbb E[X]=-1+At-B^2t^2.}\tag{1}
\]
Set \(q_c(r)=1-(r+1)^{-1/r}\). For **every shape \(r>1\)** there is a unique \(q_d(r)\) in \((0,q_c(r))\), determined by the explicit equation
\[
\boxed{A(r,q_d)=2B(r,q_d).}\tag{2}
\]
For that shape the exact classification, as the retention \(t\) varies over \([0,1]\), is:

- If \(0<q<q_d(r)\), the distribution is strictly underdispersed for all \(t\).
- If \(q=q_d(r)\), it is strictly underdispersed except for the unique interior equidispersion tangency \(t=1/B\).
- If \(q_d(r)<q<q_c(r)\), there are **two distinct interior equidispersion weights** \(0<t_-<t_+<1\); the distribution is strictly overdispersed exactly for \(t_-<t<t_+\) and strictly underdispersed outside the closed interval. In particular, the uninflated distribution and the all-one limit are both underdispersed, but intermediate one-inflation produces overdispersion.
- If \(q=q_c(r)\), the two roots are \(t_-=B^{-2}\) and \(t_+=1\); the distribution is overdispersed precisely for \(B^{-2}<t<1\).
- If \(q_c(r)<q<1\), exactly one equidispersion root lies in \((0,1)\); below it the distribution is underdispersed and above it overdispersed.

For \(q>q_d(r)\), the root pair, including a root outside \([0,1]\) when \(q>q_c(r)\), is
\[
 t_\pm=\frac{A\pm\sqrt{A^2-4B^2}}{2B^2}.\tag{3}
\]

**No such two-transition interval exists when \(0<r\le1\).** In that entire shape regime the surplus in (1) is strictly increasing for \(0<t<1\): if \(q<q_c(r)\), all distributions are underdispersed; if \(q=q_c(r)\), only the uninflated case \(t=1\) is equidispersed; and if \(q>q_c(r)\), there is exactly one equidispersion crossing from underdispersion to overdispersion as \(t\) increases. Thus \(r>1\) is necessary and sufficient for the existence of a reentrant under/over/under dispersion interval within this family.

## Assumptions and scope

All probabilities are exact and parameters are real, with \(r>0\), \(0<q<1\), \(t\in[0,1]\). Zero truncation is conditionalization on the event \(N>0\). The mixture is an additional independent structural-one component, not binomial thinning. Dispersions are compared to each distribution's **own mean**, so the sign being classified is \(\operatorname{Var}(X)-\mathbb E[X]\). Equidispersion means equality; it does not imply a Poisson distribution. Numerical illustrations do not establish any global sign claim.

## Proof

**Step 1: Exact moments and the dispersion polynomial.** The untruncated negative-binomial variable has mean \(rz\), factorial second moment \(r(r+1)z^2\), and positive-count probability \(s\). Therefore \(\mathbb E[Y]=\mu\) and \(\mathbb E[Y(Y-1)]=F_2\). Since the unit atom contributes zero to the second factorial moment,
\[
\mathbb E[X]=1+t(\mu-1)=1+tB,\qquad
\mathbb E[X(X-1)]=tF_2.
\]
The identity \(\operatorname{Var}(X)-\mathbb E[X]=\mathbb E[X(X-1)]-\mathbb E[X]^2\) gives (1). Furthermore \(B=\mathbb E[Y-1]>0\) and \(A=\mathbb E[(Y-1)(Y-2)]>0\), because \(Y\) assigns positive mass to every positive integer. At \(t=1\),
\[
\begin{aligned}
\operatorname{Var}(Y)-\mathbb E[Y]
&=F_2-\mu^2\\
&=\frac{r z^2}{s^2}\bigl[(r+1)s-r\bigr]
=\frac{r z^2}{s^2}\bigl[1-(r+1)(1-q)^r\bigr].
\end{aligned}
\]
This gives the unique uninflated sign boundary \(q_c(r)=1-(r+1)^{-1/r}\).

**Step 2: A global curvature inequality, including the sharp shape boundary.** We show
\[
\operatorname{sgn}(A-2B^2)=\operatorname{sgn}(1-r).\tag{4}
\]
Indeed, substitution into the definitions yields
\[
 A-2B^2=\frac{rz}{s^2}\bigl[s((r+1)z+2)-2rz\bigr].
\]
Write \(u=1-q\). The bracket times \(u\) equals \(-g_r(u)\), where
\[
 g_r(u)=u^r[(r+1)-(r-1)u]-(r+1)u+(r-1),\qquad g_r(1)=0.
\]
A direct differentiation gives
\[
 g_r'(u)=(r+1)\bigl[h_r(u)-1\bigr],\qquad
 h_r(u)=u^{r-1}[r-(r-1)u],
\]
\[
 h_r'(u)=r(r-1)u^{r-2}(1-u),\qquad h_r(1)=1.
\]
For \(r>1\), the last derivative is positive on \((0,1)\), so \(h_r(u)<1\), \(g_r'(u)<0\), \(g_r(u)>0\), and \(A<2B^2\). For \(0<r<1\), every relevant inequality reverses, so \(A>2B^2\). At \(r=1\), equality holds identically. Thus (4) follows without finite truncation or numerical approximation.

**Step 3: Existence and uniqueness of the additional threshold.** Put \(Z=Y-1\), taking values \(0,1,2,\ldots\). Its size-biased distribution, defined on positive integers by
\[
 \Pr\{Z^*=k\}=\frac{k\Pr\{Z=k\}}{\mathbb E[Z]},\qquad k\ge1,
\]
has the form \(\Pr\{Z^*=k\}\propto k(r)_{k+1}q^{k+1}/(k+1)!\), with the proportionality independent of \(k\). From the definitions,
\[
 \frac AB=\frac{\mathbb E[Z(Z-1)]}{\mathbb E[Z]}=\mathbb E[Z^*-1].
\]
The family \(Z^*\) is a strictly nondegenerate exponential tilt in the statistic \(Z^*\). Termwise differentiation of its absolutely convergent series at each \(0<q<1\) gives
\[
 \frac{d}{d\log q}\frac AB=\operatorname{Var}(Z^*)>0.\tag{5}
\]
As \(q\downarrow0\), \(Z^*\) concentrates at \(1\) and \(A/B\to0\). As \(q\uparrow1\), \(A/B\sim(r+1)q/(1-q)\to\infty\). Therefore the equation \(A/B=2\) defines precisely one \(q_d(r)\) for each fixed \(r>0\).

For \(r>1\), equality \(A=2B\) combined with the strict inequality \(A<2B^2\) from (4) implies \(B>1\) at \(q=q_d\). Substituting \(A=2B\) in (1) yields \(\Delta(1)=-(B-1)^2<0\), so the already-established unique boundary \(q_c(r)\) lies strictly above \(q_d(r)\).

**Step 4: Complete root classification.** For \(r>1\), (4) places the vertex of the strictly concave quadratic (1) at \(t_v=A/(2B^2)<1\). Its maximum over all real \(t\) equals \(-1+A^2/(4B^2)\), whose sign is the sign of \(A/B-2\). By (5), the maximum is negative at \(q<q_d\), zero at \(q=q_d\), and positive at \(q>q_d\). At the tangency, \(t_v=1/B\in(0,1)\). Since \(\Delta(0)=-1\) and the sign of \(\Delta(1)\) changes exactly at \(q_c\), elementary concavity establishes all five regimes, together with root formula (3). When \(q=q_c\), the relation \(A=1+B^2\) and (4) imply \(B>1\); factoring (1) then gives exactly the roots \(1\) and \(B^{-2}\). For \(0<r\le1\), (4) implies \(\Delta'(t)=A-2B^2t>0\) for all \(0<t<1\), including \(r=1\), so its endpoint signs yield the three non-reentrant regimes.

**Step 5: Exact nontrivial witness.** At \(r=5\), \(q=3/10\), the variance-minus-mean has exact values
\[
\Delta(0)=-1,\qquad
\Delta(1/2)=\frac{2479941473}{21532234108}>0,\qquad
\Delta(1)=-\frac{421000000}{37681409689}<0.
\]
These three exact rational signs establish the concrete reentrance, independently of numerical root-finding. The strict general classification above, rather than these three sample points, supplies the universal theorem.

## Verification

The companion standalone Python 3 script `verify.py` uses exact fractions to reproduce the three signs for \((r,q)=(5,3/10)\), compares the exact rational polynomial to a separately accumulated positive-count mass sum for five retention weights, and numerically brackets \(q_d<q_c\) for several noninteger and integer shapes. A successful script run prints `Exact rational witness and sampled numerical checks: PASS`. The global assertions, including uniqueness and the all-shape sign inequality, are established analytically in Steps 1–4 rather than by finite computation. Run using `python3 verify.py` without external libraries. The reported decimal thresholds are numerical illustrations, not certified exact enclosures.

## Relationship to prior work

The one-inflated zero-truncated negative-binomial distribution and its mean and variance were developed earlier, explicitly in Godwin's 2012 dissertation (Chapter Four, §2.1, p.80), with subsequent studies of one-inflated count regression and capture–recapture estimation. The 2023 paper of Jolayemi and Aderoju treats a zero-truncated negative binomial with excess ones and its goodness-of-fit; the 2022 and 2024 literature develops inference and mixture representations. Those published moment formulas imply the quadratic identity (1) after simplification; **neither the model, the mixture parametrization, the basic moment formulas nor the reduction to a quadratic is claimed as new**. The claimed advance is the full global sign phase diagram, its sharp shape \(r=1\) demarcation, existence/uniqueness of the additional boundary \(q_d(r)\), and the reentrant window with both endpoints underdispersed. A search and comparison of accessible prior studies identified no theorem covering this classification, but does not establish exhaustive historical priority.

## Limitations

The result is only about unconditional variance versus unconditional mean; it does not address likelihood fitting, dispersion tests, residual dispersion conditional on regressors, stochastic order, or all higher moments. Equality of variance and mean does not identify a Poisson law. The baseline distribution and its moment formulas date to earlier literature, including a publicly accessible 2012 dissertation. The complete 2023 publisher PDF and the full 2016 journal article were not available for inspection; their relevant indexed material was assessed, leaving residual priority risk. An independent mathematical assessment has not yet been performed.

## References

- Godwin, R. T. (2012), *Econometric Analysis of Non-Standard Count Data*, PhD thesis, University of Victoria, Chapter Four, especially pp. 76–80. https://dspace.library.uvic.ca/bitstream/handle/1828/4315/Godwin_Ryan_PhD_2012.pdf
- Godwin, R. T. (2016), *One-inflation and unobserved heterogeneity in population size estimation*, *Biometrical Journal*. https://doi.org/10.1002/bimj.201600063
- Jolayemi, E. T., and Aderoju, S. A. (2023), *On Zero-Truncated Negative Binomial with Excess Ones*, *Asian Journal of Probability and Statistics* **22**(3), 45–50, first published 2023-05-11. https://doi.org/10.9734/AJPAS/2023/v22i3487
- Böhning, D. (2022), *On the equivalence of one-inflated zero-truncated and zero-truncated one-inflated count data likelihoods*. https://doi.org/10.1002/bimj.202100343
- Tuoto, T., Di Cecco, V., and Tancredi, A. (2022), *Bayesian analysis of one-inflated models for elusive population size estimation*. https://doi.org/10.1002/bimj.202100187
- Godwin, R. T. (2024), *One-inflated zero-truncated Poisson and negative binomial regression models*, arXiv:2402.02272, first published 2024-02-03. https://arxiv.org/abs/2402.02272
- Böhning, D., and Friedl, H. (2024), *One-Inflation and Zero-Truncation Count Data Modelling Revisited*. https://doi.org/10.1111/insr.12570
