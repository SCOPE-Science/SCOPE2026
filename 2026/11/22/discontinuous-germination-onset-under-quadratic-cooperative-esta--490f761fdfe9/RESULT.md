# Discontinuous germination onset under quadratic cooperative establishment

## Finding

For the two-environment germination model specified below, positive germination is never optimal when the good-season cooperative return does not exceed seed-bank retention. When its ratio \(R\) to retention exceeds one, increasing the frequency \(p\) of favorable years creates exactly one **discontinuous** switch from complete dormancy to a strictly positive germination fraction. The unique switching frequency is specified by a scalar tangency equation; its strong-cooperation limit has a universal square-root scale. In contrast, replacing quadratic establishment by linear establishment makes the onset continuous and changes the critical-frequency scale to reciprocal strength.

Specifically, define
\[
 h_R(t)=\log\bigl(1+2R(\cosh t-1)\bigr),\qquad t>0.
\]
For every \(R>1\), there is exactly one positive \(t_c\) solving
\[
 t_ch_R'(t_c)=h_R(t_c).
\]
Set \(p_c=t_c/h_R(t_c)=1/h_R'(t_c)\) and \(g_c=1-e^{-t_c}\). Then \(0<p_c<1\), \(0<g_c<1\), and the global maximizers are exactly:

- \(\{0\}\) when \(0<p<p_c\);
- \(\{0,g_c\}\) when \(p=p_c\);
- \(\{1-e^{-t_p}\}\) when \(p_c<p<1\), where \(t_p>t_c\) is the unique root of \(p h_R'(t_p)=1\) on the decreasing branch of \(h_R'\).

The dormant policy remains a **strict local maximum** throughout \(0<p<1\). Thus the threshold is an optimizer jump, not the loss of local stability of dormancy. Write \(u_*>2\) for the unique nontrivial solution of
\[
 \log u_*=2(1-u_*^{-1}).
\]
As \(R\to\infty\),
\[
 \sqrt R\,g_c\longrightarrow \sqrt{u_*-1}=1.9802913004\ldots,
 \qquad
 \sqrt R\,p_c\longrightarrow
 \frac{\sqrt{u_*-1}}{\log u_*}=1.2426337563\ldots.
\]
These limits apply to the stipulated quadratic-return model, not to arbitrary forms of cooperative reproduction.

## Assumptions and scope

A fraction \(g\in[0,1)\) of a viable seed pool germinates in every season and the remainder survives with constant factor \(s\in(0,1)\). In a poor season, no germinating seeds successfully recruit, giving the per-season **multiplicative factor**
\[
 M_b(g)=s(1-g).
\]
In a favorable season, an idealized positive-density/facilitation response contributes quadratically in the germinating fraction:
\[
 M_g(g)=s(1-g)+Ag^2,\qquad A>0.
\]
The frequency of favorable seasons converges to \(p\in(0,1)\); independent Bernoulli seasons with favorable probability \(p\) are one sufficient case. The same policy is used every season, and geometric growth is the optimization criterion. The resulting long-run log multiplier is
\[
 \Lambda_p(g)=(1-p)\log M_b(g)+p\log M_g(g).
\]
Neither the biological origin of the quadratic coefficient nor frequency-independent population-density dynamics are asserted: this is a normalized, phenomenological per-capita payoff model. At \(g=1\), poor-season survival vanishes and \(\Lambda_p(1)=-\infty\) for \(p<1\), so the optimization domain may equivalently be extended to \([0,1]\) with that value. Define \(R=A/s\).

## Proof

**1. Weak cooperative establishment.** If \(0<R\le1\), then for every \(0<g<1\),
\[
 \frac{M_g(g)}s=1-g+Rg^2<1,
 \qquad \frac{M_b(g)}s=1-g<1.
\]
Consequently \(\Lambda_p(g)<\Lambda_p(0)=\log s\). Complete dormancy is the unique optimum.

**2. Exact one-variable reduction.** Assume \(R>1\) and put \(t=-\log(1-g)\). Direct factorization gives
\[
 \frac{M_g(g)}{M_b(g)}=1+R(e^t+e^{-t}-2).
\]
Therefore
\[
 \Lambda_p(g)=\log s-t+ph_R(t),
 \qquad
 h_R'(t)=\frac{2R\sinh t}{1+2R(\cosh t-1)}.
\]
For \(t>0\), define \(q_R(t)=t/h_R(t)\). The strict improvement over dormancy is equivalent to \(p>q_R(t)\). Since \(h_R(t)\sim Rt^2\) as \(t\downarrow0\), we have \(q_R(t)\to\infty\) at zero; since \(h_R(t)=t+\log R+o(1)\), we have \(q_R(t)\to1\) as \(t\to\infty\).

**3. Unique tangency and global classification.** Compute
\[
 h_R''(t)=\frac{2R\bigl[(1-2R)\cosh t+2R\bigr]}{\bigl[1+2R(\cosh t-1)\bigr]^2}.
\]
It changes from positive to negative exactly at
\[
 t_0=\operatorname{arcosh}\frac{2R}{2R-1}.
\]
For \(H(t)=t h_R'(t)-h_R(t)\), we have \(H'(t)=t h_R''(t)\). Thus \(H\) increases strictly from \(H(0)=0\) to a positive value at \(t_0\), then decreases strictly to \(-\log R<0\). There is precisely one zero \(t_c>t_0\). Since \(q_R'(t)=-H(t)/h_R(t)^2\), its unique minimum is \(p_c=q_R(t_c)\). The asymptotic \(h_R(t)=t+\log R+o(1)\) shows that \(q_R(t)<1\) for all sufficiently large \(t\), so \(p_c<1\); clearly \(p_c>0\).

For \(p<p_c\), every \(t>0\) has \(-t+ph_R(t)<0\). At equality precisely \(t=0\) and \(t=t_c\) maximize. For \(p>p_c\), \(\partial_t\Lambda=-1+ph_R'(t)\) starts negative, rises and then falls, so there is at most one positive local maximum, on \(t>t_0\). It exists because the value is positive somewhere, and is globally unique. Since \(h_R'\) decreases strictly for \(t>t_0\), its root \(t_p\) is unique. Moreover \(\partial_t\Lambda(0)=-1\), proving that dormancy stays a strict local maximum even after the global switch.

**4. Strong-cooperation asymptotics.** Set \(x=\sqrt R\,t\). On compact positive \(x\)-intervals,
\[
 h_R(x/\sqrt R)\longrightarrow\log(1+x^2),
 \qquad
 \frac{h_R(x/\sqrt R)}x\longrightarrow\frac{\log(1+x^2)}x.
\]
This convergence captures the global maximizers: when \(x\downarrow0\), the ratio is at most \(Cx\) on a fixed small-\(t\) neighborhood; when \(x\to\infty\) while \(t\le\delta\), it is bounded by \(\log(1+Cx^2)/x\); for \(t\ge\delta>0\), the global bound \(h_R(t)\le t+\log(1+R)\) makes \(h_R(t)/(\sqrt R\,t)\to0\) uniformly. Here \(C\) may depend on the fixed \(\delta\), but not on large \(R\). Hence \(\sqrt R\,t_c\) converges to the unique maximizer \(x_*>0\) of \(\log(1+x^2)/x\). Its stationary equation, with \(u_*=1+x_*^2\), is \(\log u_*=2(1-1/u_*)\). The difference between the left and right sides decreases on \((1,2)\) and increases on \((2,\infty)\); it is negative at \(u=2\) and tends to infinity, hence crosses zero once in \((2,\infty)\). Finally \(g_c=1-e^{-t_c}\sim t_c\) and \(p_c=t_c/h_R(t_c)\), giving both asserted limits.

**5. Linear-establishment comparison.** If the favorable factor is instead \(M_g^{\mathrm{lin}}=s(1-g)+Ag\), keeping the same poor-season multiplier, its log-growth objective is strictly concave and the unique optimizer is
\[
 g_{\mathrm{lin}}^*(p)=\max\left\{0,\frac{pR-1}{R-1}\right\},\qquad R>1,\quad 0<p<1.
\]
It starts continuously at \(p=1/R\). This is a comparison within two specified payoff functions, not a universal claim about all ecological facilitation laws.

## Verification

The standalone `verify.py` uses only the Python standard library. Running `python verify.py` performs bracketing and root checks for five strength ratios, confirms the threshold tie and phase signs on a finite grid, compares the closed linear-return optimizer, and examines high-strength asymptotics. It reports 66 passed assertion groups. The all-parameter and asymptotic statements are certified by the analytical arguments above, not by finite sampling. The numerical example at \(R=4\) is \(p_c\approx0.5951834959\) and \(g_c\approx0.6685147200\).

## Relationship to prior work

Siegmund, Moeller, Eckhart, and Geber (2022 preprint; 2023 journal article) found that a density-independent germination bet-hedging model did not fully explain observed germination fractions in a winter annual plant. Leverett and Shaw (2019) studied interactions between facilitation, competition, and dormancy in population models. ten Brink, Gremer, and Kokko (2020) studied timing under unpredictable environments. These papers motivate examining supplementary mechanisms but do not, in the sections inspected, establish the present explicit cooperative-payoff threshold, its exact global optimizer classification, or the universal strong-cooperation scaling. The general use of logarithmic growth and seed-bank survival is established background. This is not a claim of a new empirical mechanism or of a previously unknown general principle of stochastic optimization.

## Limitations

The quadratic term depends on the **germination fraction**, not dynamically on absolute population density; it is a deliberately stylized positive-density proxy. The theorem concerns constant strategies, prescribed long-run frequencies, and geometric growth, not evolutionary stability in a game of competing strategies, density-dependent demographic regulation, fluctuating seed survival, or measured plant fitness. In particular, a positive maximizing growth exponent is not asserted, and the optimum may still correspond to population decline. The historical novelty comparison was limited to accessible published material and indexed research; some related earlier articles were available only as abstracts and could contain stronger results.

## References

1. Siegmund, G.-F., Moeller, D. A., Eckhart, V. M., and Geber, M. A. *Bet hedging is not sufficient to explain intraspecific variation in germination patterns of a winter annual plant*. bioRxiv preprint, first posted September 17, 2022. https://doi.org/10.1101/2022.09.15.508102 . Revised journal article: *Bet Hedging Is Not Sufficient to Explain Germination Patterns of a Winter Annual Plant*, *American Naturalist* (2023), https://doi.org/10.1086/726785 .
2. Leverett, L. D. and Shaw, A. K. *Facilitation and competition interact with seed dormancy to affect population dynamics in annual plants* (2019). https://doi.org/10.1002/1438-390X.12021 .
3. ten Brink, H., Gremer, J. R., and Kokko, H. *Optimal germination timing in unpredictable environments* (2020). https://doi.org/10.1111/ele.13461 .
4. Valleriani, A. *Algebraic determination of the evolutionary stable germination fraction* (2005). https://doi.org/10.1016/j.tpb.2005.01.006 .
5. Ellner, S. *ESS germination strategies in randomly varying environments. I. Logistic-type models* (1985). https://doi.org/10.1016/0040-5809(85)90022-X .
