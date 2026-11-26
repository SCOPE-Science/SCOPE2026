# An exact telescoping sensitivity law for piecewise Bayesian opinion networks

## Finding
For the finite-agent Bayesian opinion-update process described below, with an initial state \(b(0)\in(0,1)^n\) and an externally fixed order of updates, every regular length-\(T\) branch has the **exact** diagonal derivative
\[
D F_T(b(0))=\operatorname{diag}\!\left(\frac{b_i(T)(1-b_i(T))}{b_i(0)(1-b_i(0))}:1\le i\le n\right).
\]
Consequently, for every \(T\ge0\),
\[
0<\|D F_T(b(0))\|_2\le C(b(0)):=\max_{1\le i\le n}\frac{1}{4b_i(0)(1-b_i(0))},
\qquad \limsup_{T\to\infty}\frac1T\log\sigma_j(D F_T)\le0
\]
for every ordered singular value \(\sigma_j\). If the log-odds drift of coordinate \(i\) exists, \(v_i=\lim_{T\to\infty}\big(\log\frac{b_i(T)}{1-b_i(T)}\big)/T\), its coordinate tangent exponent is exactly \(-|v_i|\); otherwise the limsup coordinate exponent is \(-\liminf_{T\to\infty}|\log(b_i(T)/(1-b_i(T)))|/T\).

The time-uniform bound cannot be replaced by a bound on positive **finite-horizon** logarithmic growth uniformly over initial conditions: for a constant likelihood ratio \(\gamma\in(0,1)\), the one-agent initial condition \(b(0)=\gamma^T/(1+\gamma^T)\) yields
\[
\frac1T\log F_T'(b(0))=\frac1T\log\frac{(1+\gamma^T)^2}{4\gamma^T}\longrightarrow -\log\gamma>0
\]
as the selected horizon \(T\to\infty\). Each such fixed initial condition nevertheless has a negative infinite-time tangent exponent, \(\log\gamma\). Thus arbitrarily long positive finite-time tangent indicators are compatible with the absence of positive asymptotic tangent exponents.

## Assumptions and scope
Fix a finite integer \(n\ge1\). Beliefs are real numbers \(b_i\in(0,1)\). An elementary update selects a receiving coordinate \(i\), potentially observes a sender's current belief and exogenous data, selects a **positive** likelihood ratio \(\gamma\) from a finite set by locally constant decision rules, and replaces
\[
b_i\longmapsto \frac{b_i}{b_i+\gamma(1-b_i)},
\]
leaving other coordinates unchanged. The selected receiving-coordinate sequence, the sender sequence, network and exogenous data are held fixed when differentiating with respect to the initial beliefs; the likelihood-ratio decision rules themselves may depend on the current beliefs, including comparisons with \(1/2\) and receiver-sender distances, and may vary over time. This includes the interior-belief branches of the confirmation-bias, anti-confirmation-bias and in-group-bias update rules of Dong and Marzen [1].

For each finite \(T\), call an initial condition **regular to time \(T\)** when its branch decisions through the first \(T\) updates are constant on an open neighborhood. All derivative identities apply at such conditions. In the original models with finite thresholds expressed by nonconstant analytic equalities and fixed external choices, the exceptional boundaries are finite unions of branchwise analytic hypersurfaces and hence null at a fixed finite horizon; no derivative is asserted on these switching boundaries. The asymptotic claim applies to every trajectory that is regular at all finite horizons. It is also meaningful pathwise conditional on a fixed externally randomized update schedule, without asserting differentiability of a random schedule that changes with the initial condition.

## Proof
**Step 1 (an exact conjugacy).** Define the bijection \(\ell:(0,1)\to\mathbb R\) by \(\ell(u)=\log(u/(1-u))\), and its inverse logistic function \(s(y)=1/(1+e^{-y})\). A Bayesian update with fixed positive \(\gamma\) obeys
\[
\ell\!\left(\frac{u}{u+\gamma(1-u)}\right)=\ell(u)-\log\gamma.
\]
On a regular branch, \(\gamma\) is locally constant with respect to every initial opinion. Thus the update, expressed in all \(n\) log-odds coordinates, is a translation by \(-\log\gamma\) in one coordinate. Each branchwise Jacobian in log-odds coordinates is the identity. By induction, the complete branchwise log-odds map through time \(T\) is a translation, with derivative \(I_n\), even when \(\gamma\) is chosen according to the evolving network opinions.

**Step 2 (Jacobian telescoping).** The derivative of \(s\) satisfies \(s'(y)=s(y)(1-s(y))\), and the derivative of \(\ell\) satisfies \(\ell'(u)=1/[u(1-u)]\). The chain rule for the coordinatewise conjugacy gives the asserted diagonal formula. Alternatively, the elementary derivative is \(\gamma/[u+\gamma(1-u)]^2=u'(1-u')/[u(1-u)]\), and these factors telescope separately for each receiving coordinate. Coordinates not updated simply have ratio one.

**Step 3 (global-in-time tangent bound).** Since \(0<b_i(T)(1-b_i(T))\le1/4\), every diagonal derivative has magnitude at most \(1/[4b_i(0)(1-b_i(0))]\). The spectral norm of a positive diagonal matrix is its largest diagonal entry. For each singular value and each \(T>0\), \(T^{-1}\log\sigma_j\le T^{-1}\log C(b(0))\); the stated upper exponent bound follows upon taking the limsup. This is an upper bound on *tangent* exponents, not on the ratio of distances between trajectories that follow distinct branch histories.

**Step 4 (log-odds drift classification).** The identity
\[
s(y)(1-s(y))=\frac{e^{-|y|}}{(1+e^{-|y|})^2}
\]
shows \(-|y|-2\log2\le\log(s(y)(1-s(y)))\le-|y|\). Therefore the coordinate tangent logarithm divided by \(T\) differs from \(-|\ell(b_i(T))|/T\) by a quantity tending to zero. This gives the stated exact exponent whenever \(v_i\) exists, and its limsup formula otherwise. In particular, if all opinions remain in a common compact subinterval of \((0,1)\), all coordinate exponents are zero.

**Step 5 (sharp finite-time obstruction).** In the one-agent constant-ratio example, log odds increase by \(-\log\gamma>0\) each step. The chosen \(b(0)\) has initial log odds \(T\log\gamma\), so \(b(T)=1/2\). Step 2 gives \(F_T'(b(0))=(1+\gamma^T)^2/(4\gamma^T)>1\) for all \(T\ge1\). Its finite-time exponent tends to \(-\log\gamma>0\) along the specified family of initial conditions. For each *fixed* such initial condition, the log odds tend to positive infinity at rate \(-\log\gamma\), and Step 4 gives infinite-time exponent \(\log\gamma<0\). The upper bound from Step 3 is attained at the exact selected horizon \(T\) for this initial condition, since its final belief is precisely \(1/2\). This completes the proof.

## Verification
The accompanying self-contained program `verification_bayesian.py` uses exact rational arithmetic for finite belief networks with belief-dependent likelihood switches. It independently checks the local posterior derivative identity, the product-to-endpoint telescoping identity and the time-uniform bound for \(480\) network experiments involving \(2\) to \(6\) agents and \(14\) elementary updates each. It also checks the exact sharp finite-horizon construction and large-horizon logarithmic limits. Execution reports `PASSED 1995 exact rational and analytic-limit spot checks`. The universal and infinite-time statements are established by the proof, not extrapolated from this finite test.

## Relationship to prior work
Dong and Marzen [1] introduced the particular belief-update network and explicitly calculated the diagonal one-step Jacobian in their Eqs. (4)–(5). Their empirical finite-time Lyapunov analysis reports small positive finite-time indicators alongside later negative indicators; their treatment does not derive the coordinatewise exact all-time product, the initial-state-dependent uniform bound, its sharp positive finite-horizon witness, or the exact log-odds drift classification. Their numerical evidence for transient chaotic *signatures* is not contradicted: the theorem distinguishes finite-horizon tangent growth from a positive asymptotic tangent exponent. The log-odds transformation of Bayesian updates is classical and is not claimed as new. General piecewise-translation dynamics, including [2], inform the connection but do not provide the model-specific belief-space derivative estimates and sharp horizon examples asserted here.

## Limitations
This is a conditional regular-orbit theorem for an external update schedule and a **finite-valued locally constant positive** likelihood-ratio rule. It does not apply to smoothly state-dependent likelihood ratios with nonzero derivatives, adaptive activation whose selection changes under perturbation, initial conditions exactly at decision discontinuities, or boundary beliefs equal to \(0\) or \(1\). The theorem does not establish global consensus, rule out sensitive dependence between trajectories lying in different itinerary cells, exclude all definitions of deterministic chaos, or quantify a stochastic Lyapunov exponent under a perturbation-dependent random update sequence. It does not certify priority against all published work; broader coordinate-conjugacy results may imply parts of the claim.

## References
[1] Emily Dong and Sarah Marzen, *Cognitive biases can move opinion dynamics from consensus to signatures of transient chaos*, arXiv:2405.19128v1 (first posted May 29, 2024), https://arxiv.org/pdf/2405.19128 ; American Journal of Physics, DOI:10.1119/5.0220792.

[2] Denis Volk, *Attractors of Piecewise Translation Maps*, arXiv:1708.03780, https://arxiv.org/pdf/1708.03780.
