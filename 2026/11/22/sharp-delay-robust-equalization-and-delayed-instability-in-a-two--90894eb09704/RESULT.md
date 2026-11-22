# Sharp delay-robust equalization and delayed instability in a two-agent influence model

## Finding

Consider two competing agents whose relative influence shares are updated multiplicatively, with delayed negative feedback on each agent's favorability. For every finite integer delay \(\tau\geq0\), all strictly interior histories converge to equal influence when \(0\leq\beta\leq c\), where \(c\in(0,1]\) is the common baseline favorability and \(\beta\) is feedback strength. Convergence is exponential for each fixed delay, with a direct global bound when \(\beta<c\).

This threshold is sharp for stability **uniformly over delay lengths**: for every \(c<\beta<2c\), equal influence is locally attracting when there is no delay, yet becomes linearly unstable at all sufficiently large integer delays. An unstable characteristic multiplier has the asymptotic form

\[
r_\tau=1+\frac{\log(\beta/(2c-\beta))+i\pi}{\tau}+O(\tau^{-2}).
\]

This is an exact statement about the specified deterministic two-agent relative-influence mechanism, not an assertion of persistent oscillations or chaos after instability.

## Assumptions and scope

Let \(p_1(t)+p_2(t)=1\) and \(0<p_i(t)<1\) for every prescribed history time \(t=-\tau,\ldots,0\). The source's normalized resource/influence update specialized to two agents is

\[
p_i(t+1)=\frac{p_i(t)\,[1+c_i(t)(1-p_i(t))]}{\sum_{j=1}^{2}p_j(t)\,[1+c_j(t)(1-p_j(t))]},\quad
c_i(t)=c-\beta p_i(t-\tau).
\]

Assume \(0<c\leq1\), an integer \(\tau\geq0\), and \(0\leq\beta<2c\). The multiplicative factors are strictly positive on interior shares: \(c_i(t)>c-\beta>-c\geq-1\) and \(1-p_i(t)<1\). Consequently normalization is well defined, both shares stay positive, and the simplex is forward invariant. In the range \(\beta>c\), individual favorability coefficients may become negative away from the balanced state; only the strictly positive *multiplicative weights* are required by this extension. When \(\beta\leq c\), the coefficients themselves are nonnegative.

Define the signed influence imbalance \(v_t=2p_1(t)-1\in(-1,1)\) and \(d_t=1-v_t^2\). The exact scalar delay recurrence is

\[
 v_{t+1}=\frac{4v_t-\beta d_t v_{t-\tau}}{4+(2c-\beta)d_t}.\tag{1}
\]

The unique interior fixed point is \(v=0\): substituting a constant \(v\) into (1) gives \(2c(1-v^2)v=0\). Boundary points \(v=\pm1\) are fixed but are excluded by the positive-history assumption.

## Proof

**Exact reduction.** Put \(p_1=(1+v)/2\) and \(p_2=(1-v)/2\), with delayed imbalance \(w\). The two unnormalized weights are \(p_1[1+(c-\beta(1+w)/2)p_2]\) and \(p_2[1+(c-\beta(1-w)/2)p_1]\). Subtracting and adding them, then multiplying numerator and denominator by four, gives (1).

**Subcritical global exponential equalization.** Take any positive-history initial state and let \(\rho=\max_{-\tau\leq j\leq0}|v_j|<1\). Set \(W_t=\max_{t-\tau\leq j\leq t}|v_j|\). For \(0\leq\beta<c\), the rational function \(f(s)=[4+\beta s]/[4+(2c-\beta)s]\) is strictly decreasing on \([0,1]\). If \(W_t\leq\rho\), equation (1) implies

\[
|v_{t+1}|\leq f(d_t)W_t\leq qW_t,\qquad
q=\frac{4+\beta(1-\rho^2)}{4+(2c-\beta)(1-\rho^2)}<1.
\]

Induction yields \(W_t\leq\rho\) for all \(t\), and the next \(\tau+1\) values all have magnitude at most \(qW_t\). Hence \(W_{t+\tau+1}\leq qW_t\), and \(v_t\to0\) exponentially, uniformly for all histories with the same \(\rho\) at a fixed delay.

**Critical global convergence.** If \(\beta=c\), (1) becomes \(v_{t+1}=(1-h_t)v_t-h_tv_{t-\tau}\), where \(h_t=c(1-v_t^2)/[4+c(1-v_t^2)]\in(0,1/2)\). Thus \(W_{t+1}\leq W_t\) and \(W_t\downarrow L\geq0\). If \(L>0\), compactness of the history state space supplies a complete two-sided orbit in the omega-limit set whose sliding-window maximum is \(L\) and some coordinate equals \(\pm L\). Whenever \(|v_{t+1}|=L\), equality in the triangle inequality forces \(v_t\) to have the same sign and magnitude \(L\) and \(v_{t-\tau}\) to have opposite sign and magnitude \(L\): the coefficients \(1-h_t\) and \(h_t\) are strictly positive, and \(1-h_t>h_t\). Applying this to all backward predecessors successively forces every earlier value to have the same sign \(\pm L\), contradicting the required opposite sign at a delayed predecessor. Therefore \(L=0\) and every interior history equalizes. Local exponential convergence follows from the characteristic root argument below, since at \(\beta=c\) all multipliers lie strictly inside the unit disk; an orbit converging to the fixed point eventually enters that exponential-stability neighborhood.

**Sharpness against large delays.** Linearizing (1) at zero gives

\[
v_{t+1}=a v_t-hv_{t-\tau},\qquad
 a=\frac4{4+2c-\beta},\quad h=\frac\beta{4+2c-\beta},\quad
 r^{\tau+1}-ar^\tau+h=0.\tag{2}
\]

For \(\beta\leq c\), \(a+h\leq1\). If a root had \(|r|\geq1\), then \(h=|r|^\tau|r-a|\geq1-a\). Strict inequality \(a+h<1\) rules this out; at \(a+h=1\), equality requires \(r=1\), which fails equation (2) because \(1-a+h=2h>0\). Thus all roots are strictly Schur stable whenever \(0<\beta\leq c\), as needed in the critical argument. When \(\beta=0\), (2) has roots zero and \(a=4/(4+2c)<1\).

For \(c<\beta<2c\), \(0<a<1\) and \(h/(1-a)=\beta/(2c-\beta)>1\). At \(\tau=0\) the unique multiplier is \((4-\beta)/(4+2c-\beta)\in(0,1)\), so equal influence is locally attracting. For large integer \(\tau\), put \(r=e^{z/\tau}\) in (2); then

\[
e^z(e^{z/\tau}-a)+h=0.
\]

At \(\tau^{-1}=0\), this equation has the simple root \(z_0=\log[h/(1-a)]+i\pi\); its \(z\)-derivative equals \(-h\ne0\). The analytic implicit-function theorem gives \(z_\tau=z_0+O(\tau^{-1})\) and thus the displayed multiplier expansion. Its modulus exceeds one for all sufficiently large integer \(\tau\) because \(\operatorname{Re} z_0>0\). The smooth delayed map is therefore locally linearly unstable at balanced influence. This proves the sharp delay-robust boundary. \(\square\)

## Verification

The companion `verify.py` is a Python-standard-library supplementary checker. It (i) evaluates the two-agent normalized update and equation (1) with exact rational arithmetic on a deterministic rational grid; (ii) checks the subcritical window bound on sample histories; and (iii) computes sample complex characteristic residuals and unstable long-delay roots using Newton's method. The infinite-delay and all-history statements rest on the preceding analytic proof, **not** on finite numerical tests. Execute `python3 verify.py`.

## Relationship to prior work

Satur (2026), arXiv:2602.17852, introduces the normalized attractive-interaction map, proves convergence for *constant* favorable conditions, and in Section 4 defines the delayed own-share feedback studied here. It numerically explores high-feedback cycles and complex behavior but does not derive the two-agent all-delay equalization boundary. Equation (1), the global critical case, and the large-delay root expansion concern that explicit extension rather than the original constant-parameter theorem.

Alboszta and Miękisz (2004) give delay-dependent instability in a two-action game replicator with delayed payoffs and a different delay-independent stable biological update. Ben Khalifa, El Azouzi, and Hayel (2017) address continuous-time replicators with distributed fitness delays. Iijima (2012) treats stability under delayed information in symmetric games. These demonstrate that delay-dependent and independent stability are established general phenomena; none of the inspected material states the specific normalized two-agent own-share map or its strict global/critical phase boundary. Abstract-only access to Iijima and incomplete availability of other works leave historical-priority risk. The multiplier condition uses standard elementary delay-characteristic reasoning, not a purported new general theorem of delay equations.

The natural object is the distribution of influence between two social agents under fatigue-like delayed negative feedback, placing this finding primarily under MSC2020 91D30 (social networks; opinion dynamics), rather than classifying an arbitrary delayed difference equation.

## Limitations

This is a deterministic two-agent model with equal baseline favorabilities and common discrete lag. Strictly positive initial history is required; boundary fixed states need not equalize. For \(c<\beta<2c\), the theorem establishes eventual *linear instability* of balanced influence for sufficiently large delays, not a general periodic orbit, global attractor, or chaos. The delay size where instability starts is not explicitly optimized, and the theorem does not treat unequal agents or more than two components. In the supercritical range, instantaneous feedback coefficients can be negative away from balance, although normalized update weights stay positive. No statistical or empirical social validation is implied.

## References

1. Oksana Satur, *Mean-field dynamics of attractive resource interaction: From uniform to aggregated states*, arXiv:2602.17852 (first public release 2026-02-19), especially equations (2)–(3) and Section 4. https://arxiv.org/html/2602.17852v2
2. Jan Alboszta and Jacek Miękisz, *Stability of evolutionarily stable strategies in discrete replicator dynamics with time delay*, *Journal of Theoretical Biology* 231 (2004), 175–179; arXiv:q-bio/0409024. https://arxiv.org/abs/q-bio/0409024
3. Nesrine Ben Khalifa, Rachid El Azouzi, and Yezekael Hayel, *Hopf Bifurcations in Replicator Dynamics with Distributed Delays*, arXiv:1703.06721 (2017). https://arxiv.org/abs/1703.06721
4. Ryota Iijima, *On delayed discrete evolutionary dynamics*, *Journal of Theoretical Biology* 300 (2012), 1–6, DOI 10.1016/j.jtbi.2012.01.001. https://pubmed.ncbi.nlm.nih.gov/22266122/
