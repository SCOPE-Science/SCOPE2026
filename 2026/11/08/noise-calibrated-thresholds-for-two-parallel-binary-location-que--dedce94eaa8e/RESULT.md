# Noise-calibrated thresholds for two parallel binary location queries

## Finding

Consider an unknown location \(X\sim\operatorname{Uniform}[0,1]\). Before receiving any feedback, one poses two binary threshold questions at \(t\) and \(1-t\), with \(0\le t\le1/2\). Each truthful bit \(\mathbf1_{\{X\ge u\}}\) is independently flipped with probability \(\varepsilon\in[0,1/2]\), independently of \(X\). The location estimate is the posterior mean \(\widehat X=\mathbb E[X\mid Y_1,Y_2]\), which minimizes expected squared loss among all decoders for the selected thresholds.

Set \(\delta=1-2\varepsilon\). The exact squared-error Bayes risk is
\[
R_\delta(t)=\frac1{12}-\frac{2\delta^2t^2(1-t)^2}{1-\delta^2+4\delta^2t}.
\]
The apparent indeterminacy at \((\delta,t)=(1,0)\) is resolved by \(R_1(0)=1/12\), since both questions are then deterministic for almost every location. When \(\delta=0\), every permitted \(t\) has risk \(1/12\).

For every \(0<\delta\le1\), the **unique** optimum within this mirror-symmetric two-threshold family is
\[
t_*(\delta)=\frac{2\delta^2-1+\sqrt{1+2\delta^2-2\delta^4}}{6\delta^2},
\qquad \frac13\le t_*(\delta)<\frac12.
\]
It decreases strictly with signal strength \(\delta\), with \(t_*(1)=1/3\), \(\lim_{\delta\downarrow0}t_*(\delta)=1/2\), and
\[
t_*(\delta)=\frac12-\frac{\delta^2}{4}+O(\delta^4)\quad(\delta\downarrow0),
\qquad
t_*(\delta)=\frac13+\frac{1-\delta^2}{6}+O((1-\delta^2)^2)\quad(\delta\uparrow1).
\]
For \(0<\delta<1\), both the noiseless trisection thresholds \(1/3,2/3\) and the repeated midpoint query \(1/2,1/2\) are strictly suboptimal.

For instance, at \(\varepsilon=1/4\), the unique optimal left threshold is \(t_*=(\sqrt{22}-2)/6\), giving exact risk \((419-88\sqrt{22})/108\approx0.0578093808846\). Repeating the midpoint yields \(7/120\approx0.0583333333333\), and noiseless trisection yields \(85/1404\approx0.0605413105413\).

## Assumptions and scope

The prior is uniform on the unit interval. Both threshold locations are chosen before either response is observed, and are constrained to be reflections around the midpoint. The two bit-flip errors are mutually independent conditional on \(X\), with a common constant flip probability. For a chosen threshold pair, the estimator is the exact posterior conditional mean; the risk averages over both the target location and the oracle noise. This theorem does **not** claim optimality among non-symmetric pairs, all measurable query sets, adaptive designs, or other noise channels.

## Proof

Write \(\delta=1-2\varepsilon\) and encode each binary answer as zero or one. Partition the target domain into \([0,t)\), \([t,1-t)\), and \([1-t,1]\). Their truthful response pairs, corresponding to threshold order \((t,1-t)\), are \((0,0)\), \((1,0)\), and \((1,1)\). On each interval the likelihood for a fixed observed response pair is constant, so its probability and first moment can be integrated exactly.

Let \(p_y=\Pr(Y=y)\) and \(c_y=\mathbb E[(X-1/2)\mathbf1_{\{Y=y\}}]\). Direct integration gives
\[
\begin{aligned}
p_{00}=p_{11}&=\frac{1-\delta^2+4\delta^2t}{4},\\
c_{00}&=-\frac{\delta t(1-t)}2,\qquad
c_{11}=\frac{\delta t(1-t)}2,\\
c_{01}=c_{10}&=0.
\end{aligned}
\]
(The individual probabilities \(p_{01}\), \(p_{10}\) need not be equal.) For every answer pattern of positive probability, \(\mathbb E[X\mid Y=y]-1/2=c_y/p_y\). The law of total variance gives
\[
R_\delta(t)=\operatorname{Var}(X)-\operatorname{Var}(\mathbb E[X\mid Y])
=\frac1{12}-\sum_y\frac{c_y^2}{p_y},
\]
which yields the announced expression. When \(\delta=1,t=0\), there is no informative observation, and the separate boundary definition follows.

For \(0<\delta\le1\), minimizing \(R_\delta\) is equivalent to maximizing \(F(t)=t^2(1-t)^2/(1-\delta^2+4\delta^2t)\). In the open interval \(0<t<1/2\), differentiating shows that the sign of \(F'(t)\) is the sign of \(-H(t)\), where
\[
H(t)=3\delta^2t^2+(1-2\delta^2)t-\frac{1-\delta^2}{2}.
\]
At \(0<\delta<1\), its constant term is negative and leading coefficient positive, so it has exactly one positive zero. Moreover \(H(1/3)=-(1-\delta^2)/6<0\) and \(H(1/2)=\delta^2/4>0\), placing this zero strictly between \(1/3\) and \(1/2\). The derivative is positive before this zero and negative after it, hence the maximizer is unique. At \(\delta=1\), the polynomial becomes \(H(t)=t(3t-1)\), giving a unique interior maximizer \(t=1/3\), while \(F(0)\) corresponds to the uninformative boundary. The quadratic formula gives the displayed \(t_*\).

For monotonicity, set \(s=\delta^2\). At a root \(t\in[1/3,1/2]\), \(\partial_t H=6st+1-2s\ge1\) (indeed \(6t-2\ge0\)) and \(\partial_s H=3t^2-2t+1/2>0\). The implicit-function formula gives \(dt_*/ds<0\). Expansions at \(s=0\) and \(s=1\) follow from the explicit root formula. The same derivative signs give strict suboptimality of the two fixed designs at interior noise strengths.

## Verification

A standalone exact-arithmetic verifier, `verify.py`, independently integrates the three regions for every response pattern and compares the resulting posterior mean-square risk to the closed formula at a grid of rational parameters. It also checks exact parameter-specific risks, the symbolic stationary-root equation on chosen algebraic examples, and boundary cases. Run `python verify.py` with Python 3.10 or later; no third-party packages are required. These finite checks support, but do not replace, the analytic proof above.

## Relationship to prior work

The noisy 20-questions literature includes nonadaptive query coding, entropy-based query selection, and quadratic-loss localization. Variani et al. (2015) study noisy nonadaptive **dyadic-bit** queries and derive bounds and asymptotic MSE under bit-repetition policies. Chung et al. (2016) study **superposition-code/unequal-error-protection** policies and error exponents for many queries. Zhou and Hero (2020) obtain **resolution-exceedance** bounds and finite-blocklength approximations for general noisy nonadaptive queries, explicitly distinguishing their objective from quadratic loss. Those settings do not state this exact closed-form Bayes-risk optimum over two mirror-symmetric threshold locations, and the present calculation does not imply their much broader coding guarantees.

The classical noiseless trisection is recovered as \(\varepsilon=0\); repeated median approaches optimality only in the completely noisy limit. Restricting to a parallel, reflection-balanced pair is substantive: the result is not a theorem of global optimality over arbitrary threshold placements. Originality is assessed under the inspected sources, not a claim of exhaustive publication precedence.

## Limitations

Only the uniform prior, exactly two nonadaptive mirror-symmetric threshold queries, identically reliable independent bit-flip errors, and squared-loss Bayes estimation are treated. An unrestricted two-threshold optimizer could differ; general sequential localization, measurement-dependent noise, finite-horizon dynamic programming and robustness to unknown noise parameters are not established. Closely related work on classical Bayes experimental design may contain an equivalent optimum not identified in the inspected literature. The analytic result does not rely on computer enumeration or random experiments.

## References

1. E. Variani, K. Lahouel, A. Bar-Hen and B. Jedynak, *Non-Adaptive Policies for 20 Questions Target Localization*, arXiv:1504.05996 (first posted 2015-04-22), https://arxiv.org/abs/1504.05996 .
2. H. W. Chung, B. M. Sadler, L. Zheng and A. O. Hero, *Unequal Error Protection Querying Policies for the Noisy 20 Questions Problem*, arXiv:1606.09233 (first posted 2016-06-29), https://arxiv.org/abs/1606.09233 .
3. L. Zhou and A. O. Hero, *Resolution Limits for the Noisy Non-Adaptive 20 Questions Problem*, arXiv:2004.07231 (first posted 2020-04-15), https://arxiv.org/abs/2004.07231 .
