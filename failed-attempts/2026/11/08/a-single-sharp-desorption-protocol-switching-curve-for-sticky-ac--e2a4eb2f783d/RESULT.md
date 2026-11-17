# A single sharp desorption-protocol switching curve for sticky active search

## Finding
Consider a one-dimensional run-and-tumble particle with bulk Poisson resetting, an adsorbing wall and a partially absorbing bound state as specified below. Compare the **home-return protocol** (H), in which desorption sends the particle back to its original position and orientation, against the **wall-launch protocol** (W), in which desorption releases it at the wall moving outward. The two protocols use identical adsorption-time laws and absorption probabilities.

For an initially right-moving particle, the wall-launch protocol always has strictly smaller mean permanent-absorption time. For an initially left-moving particle, define
\[
 u=\frac{x_0}{v},\qquad \beta=\alpha u,\qquad
 \theta=\operatorname{arcosh}\left(1+\frac r\alpha\right).
\]
Then H is strictly faster precisely when
\[
 \beta<\frac{\theta}{\sinh\theta},
\]
W is strictly faster precisely when the inequality is reversed, and the protocols tie at equality. In particular, if \(\beta\geq1\), W is strictly faster for every positive bulk reset rate. If \(0<\beta<1\), there is **exactly one** rate \(r_c>0\): H wins below \(r_c\), and W wins above it.

The **entire switching curve** in the dimensionless plane of tumbling and resetting rates admits the single-parameter representation
\[
 \boxed{\left(\frac{\alpha x_0}{v},\frac{r x_0}{v}\right)
 =\left(\frac{\theta}{\sinh\theta},\;
 \theta\tanh\frac\theta2\right),\quad 0<\theta<\infty.}
\]
Consequently, for each fixed \(r>0\) there is exactly one critical tumbling rate \(\alpha_c(r)>0\), with H faster for \(\alpha<\alpha_c\) and W faster for \(\alpha>\alpha_c\). These decisions are independent of both the bound-state waiting-time distribution and the permanent-absorption probability, provided the two protocols use the same laws and the probability is strictly between zero and one.

The curve has sharp endpoint behavior. Writing \(s=rx_0/v\),
\[
 \frac{\alpha_c(r)x_0}{v}=1-\frac{s}{3}+O(s^2)
 \quad(s\downarrow0),\qquad
 \alpha_c(r)\sim 2r e^{-s}\quad(s\to\infty).
\]
For fixed \(\alpha>0\), writing \(\delta=1-\beta\) as \(\beta\uparrow1\),
\[
 \frac{r_c}{\alpha}=3\delta+O(\delta^2).
\]
As \(\beta\downarrow0\),
\[
 \frac{r_c x_0}{v}
 =\log\frac{2}{\beta}+\log\log\frac{2}{\beta}+o(1).
\]

## Assumptions and scope
The particle moves on \([0,\infty)\) at constant speed \(v>0\), with orientation \(\sigma\in\{-1,+1\}\), independently switching sign at rate \(\alpha>0\). Its initial state is \((x_0,\sigma_0)\), where \(x_0>0\). While moving in the bulk, it resets at independent exponential rate \(r>0\) to this same initial state, regardless of its current orientation. The first arrival at the wall in the inward orientation produces adsorption. During adsorption no bulk resetting operates. Each adsorption is followed by a nonnegative random dwell \(B\), identically distributed over encounters, with finite mean \(b\). Independently of dwell and bulk motion, permanent absorption follows with probability \(p\in(0,1)\); otherwise the particle desorbs in protocol H or W. All cycles and random choices are independent as appropriate for renewal. The same \(p\) and dwell law must apply in both protocols. The comparison concerns the **mean time to permanent absorption** from the initial bulk state; it does not compare higher passage-time moments or two protocols with different absorption kinetics.

## Proof
**1. Unreset first-hit transforms.** For Laplace variable \(z>0\), let \(f_\pm(x;z)\) be the transforms of the first time a free (nonresetting) particle hits the wall, given initial position \(x>0\) and orientation. The bounded backward equations are
\[
 \pm v\partial_x f_\pm+\alpha(f_\mp-f_\pm)=zf_\pm,
 \qquad f_-(0;z)=1.
\]
The decaying solution, unique under boundedness at infinity, is
\[
 f_-(x;z)=e^{-q(z)x},\qquad
 f_+(x;z)=c(z)e^{-q(z)x},
\]
with
\[
 q(z)=\frac{\sqrt{z(z+2\alpha)}}v,\quad
 c(z)=\frac{z+\alpha-\sqrt{z(z+2\alpha)}}\alpha
 =e^{-\vartheta(z)},\quad
 \vartheta(z)=\operatorname{arcosh}(1+z/\alpha).
\]
In particular \(f_+(0;z)=c(z)\). Write \(F_\sigma=f_\sigma(x_0;r)\), \(C=f_+(0;r)\). They are positive for all stipulated parameters.

**2. Bulk reset renewal.** A Poisson clock stopped by a nonresetting wall-hit has mean \((1-F_\sigma)/r\) and probability \(1-F_\sigma\) of triggering a reset first. Thus the mean time \(H_\sigma\) to first adsorption from the home state satisfies
\[
 H_\sigma=\frac{1-F_\sigma}{r}+(1-F_\sigma)H_\sigma,
 \qquad H_\sigma=\frac{1-F_\sigma}{rF_\sigma}.
\]
For a fresh wall launch in the outward direction, the same argument gives
\[
 W_\sigma=\frac{1-C}{r}+(1-C)H_\sigma
 =\frac{1-C}{rF_\sigma}.
\]
This second expression accounts explicitly for a bulk resetting event from the wall-launched excursion to the original home state; it is not a restart at the wall.

**3. Absorption renewal and exact difference.** The number \(N\) of failed adsorption attempts before permanent absorption is geometric, with \(\mathbb E N=(1-p)/p=:\Gamma>0\). The initial excursion always begins at home. Linearity of expectations yields
\[
 M_{\rm H}=(1+\Gamma)(H_\sigma+b),\qquad
 M_{\rm W}=H_\sigma+b+\Gamma(W_\sigma+b).
\]
Subtracting gives the exact identity
\[
 \boxed{M_{\rm W}-M_{\rm H}
 =\frac\Gamma r\left(1-\frac C{F_\sigma}\right).}
\]
Thus \(b\) cancels and the positive factor \(\Gamma\) cannot affect the preferred protocol. If \(\sigma_0=+1\), then \(F_+=C\exp(-x_0q(r))\), so \(C/F_+=\exp(x_0q(r))>1\), proving W is always faster. If \(\sigma_0=-1\), \(F_-=\exp(-x_0q(r))\) and
\[
 M_{\rm W}-M_{\rm H}
 =\frac\Gamma r\left(1-
 \exp\left[\beta\sinh\theta-\theta\right]\right).
\]
The sign is therefore positive exactly when \(\beta<\theta/\sinh\theta\), as asserted.

**4. Uniqueness and the two parameter sections.** The function \(h(\theta)=\theta/\sinh\theta\) decreases strictly from one to zero: its derivative has the sign of \(\sinh\theta-\theta\cosh\theta<0\), since the opposite expression vanishes at zero and has derivative \(\theta\sinh\theta>0\). For fixed \(\alpha\), the parameter \(\theta=\operatorname{arcosh}(1+r/\alpha)\) increases strictly from zero to infinity as \(r\) increases. This proves the claimed dichotomy and one-crossing assertion. On the equality curve, \(\alpha u=\theta/\sinh\theta\) and \(r/\alpha=\cosh\theta-1\), whence \(ru=\theta\tanh(\theta/2)\). The latter is strictly increasing from zero to infinity, and \(\alpha=r/(\cosh\theta-1)\) is strictly decreasing in \(\theta\). This proves existence and uniqueness of \(\alpha_c\) at each fixed positive reset rate and gives its sign orientation.

**5. Endpoint expansions.** The Taylor expansions \(\theta/\sinh\theta=1-\theta^2/6+O(\theta^4)\) and \(\theta\tanh(\theta/2)=\theta^2/2-\theta^4/24+O(\theta^6)\) imply the small-\(s\) and near-\(\beta=1\) formulas. As \(\theta\to\infty\), \(s=\theta\tanh(\theta/2)=\theta+o(1)\), while \(\alpha_c/r=1/(\cosh\theta-1)\sim 2e^{-\theta}\), proving the high-reset rate law. Finally \(\beta=\theta/\sinh\theta=2\theta e^{-\theta}(1+o(1))\) implies \(\theta=\log(2/\beta)+\log\log(2/\beta)+o(1)\), and \(ru=\theta\tanh(\theta/2)=\theta+o(1)\), giving the remaining endpoint law.

## Verification
The standalone Python 3 script `verify.py` uses only the standard library and checks the backward eigen-solution, renewal-difference identity, waiting-law invariance, both orientation decisions, unique switching thresholds and numerical values. A separately generated event-driven simulation of the free RTP stopped by an exponential reset clock compares empirical hit-before-reset probabilities with independently computed first-hit transforms. The script reports 923 passed checks under its deterministic seed. These computations check implementation and examples only; the assertions for all positive parameters and all finite-mean dwell laws follow from the proof, not from sampling or bounded numerical enumeration.

For reproduction, run `python3 verify.py` from the directory containing the standalone script. Numerical example: at \(\beta=1/2\), the unique threshold is \(\theta_*=2.177318984965306\ldots\) and \(r_c/\alpha=3.46798297323987\ldots\).

## Relationship to prior work
Bressloff and Linn [1] formulated this exact half-line sticky-wall model, provided the two desorption-protocol mean-passage expressions (their Eqs. (4.9) and (4.17)), and displayed qualitative preference regions in a two-parameter contour plot (their Fig. 9). Thus the present claim is an analytical consequence of a known renewal framework, **not** the first proposal of the protocol comparison or of its mean-first-passage formulas. What is sharpened here is a single necessary-and-sufficient global phase boundary for both initial orientations, exact one-crossing uniqueness in either reset-rate or tumble-rate sections, universal independence from bound-state kinetics, and the two endpoint asymptotic regimes of that boundary. The earlier encounter-based RTP resetting model [2] concerns wall contact-count absorption rather than an explicit comparison of the two sticky-wall desorption rules. The classic resetting analysis [3] provides the telegraph-process renewal background without this exact sticky-boundary classification.

## Limitations
The desorption protocol comparison assumes equal independent adsorption waiting-time laws and equal strictly interior absorption probabilities. It does not hold without further analysis if the protocols use different wall kinetics, the particle has translational diffusion, resetting is non-Poisson, or the wall geometry changes. The result is a same-model analytical assessment and has not received independent validation. The original 2026 preprint already contains general formulas from which specialized inequalities can be derived; publication priority for the particular global phase-boundary classification remains qualified. No claim is made of a general downstream thermodynamic or experimental theorem.

## References
1. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446v1, first public 2026-02-02, https://arxiv.org/html/2602.02446v1.
2. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle with stochastic resetting*, arXiv:2503.01304, first public 2025-03-03, https://arxiv.org/abs/2503.01304.
3. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450, https://arxiv.org/abs/1808.06450.
