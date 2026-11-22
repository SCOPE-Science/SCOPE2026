# A waveform-independent cooperation fold amid periodic mixing of pair and triple games

## Finding

In the well-mixed nonlinear public-goods replicator for discounted two-player and synergistic three-player interactions, there is a **unique admissible mean proportion of triple interactions** at which periodic variation of this proportion leaves the coexistence saddle-node **exactly fixed**, regardless of the waveform, period, or amplitude (provided the instantaneous proportions remain between zero and one). For all other means in the same coexistence-fold range, every sufficiently weak nonconstant mean-zero periodic variation shifts the local fold **strictly toward lower benefit-to-cost ratios**, with a universal coefficient determined by the squared primitive of the waveform. The fixed-fold and shifted-fold alternatives constitute a single local bifurcation classification.

Write the fraction of cooperators as \(x\in(0,1)\). Fix two-player discount \(0<a<1\), three-player synergy \(b>1\), a positive benefit-to-cost factor \(r\), and the fraction \(\theta(t)\in(0,1)\) of three-player games. Let
\[
 g_2(x)=\frac{1-(1-a)x}{2},\qquad
 g_3(x)=\frac{[1+(b-1)x]^2}{3},\quad k(x)=g_3(x)-g_2(x),
\]
\[
 \dot x=x(1-x)\{r[(1-\theta(t))g_2(x)+\theta(t)g_3(x)]-1\}. \tag{1}
\]
These are the source's well-mixed pair/triple payoff functions, with time-varying interaction-order mix as an explicitly prescribed extension. Put \(h=1-a>0\), \(d=b-1>0\), and choose the mean \(\theta_0\) in the open interval
\[
 \frac{3h}{3h+4bd}<\theta_0<\frac{3h}{3h+4d}. \tag{2}
\]
Then \(G(x)=g_2(x)+\theta_0 k(x)\) has a unique strict interior minimum at \(s\in(0,1)\), positive curvature coefficient \(q=\theta_0d^2/3\), and stationary fold at \(r_0=1/G(s)>0\).

**Exact pinning.** Assume additionally \(b^2/3>a/2\). Then there is exactly one \(\theta_*\) in (2) for which \(k(s)=0\), where \(s\) is the vertex of the corresponding mean payoff \(G\). At this mean, for **every continuous positive-periodic** interaction mix \(\theta(t)\in(0,1)\) with time average \(\theta_*\), equation (1) has the exact constant solution \(x(t)=s_*\) when \(r=r_*\). Its period return map has multiplier exactly one **and a strictly positive quadratic coefficient**. The parameter derivative of the return displacement with respect to \(r\) is strictly positive. Consequently \(r=r_*\) is a nondegenerate saddle-node of interior period-one responses for every such waveform, without a small-amplitude restriction. In a neighborhood of that constant orbit there are two periodic states just below \(r_*\) (lower attracting, upper repelling), one double state at equality, and none just above. No global enumeration of other periodic orbits is asserted.

**Strict unpinning elsewhere.** Fix any \(\theta_0\) in (2), a continuously differentiable nonconstant \(T\)-periodic function \(w\) with mean zero, and set \(\theta(t)=\theta_0+\varepsilon w(t)\), for sufficiently small real \(\varepsilon\). Let \(W\) be the unique mean-zero periodic primitive \(W'=w\), let \(P=s(1-s)\), and denote period averaging by angle brackets. The unique local periodic-orbit fold satisfies
\[
 \boxed{r_{\rm fold}(\varepsilon)=r_0-\varepsilon^2P^2r_0^4q[k(s)]^2\langle W^2\rangle+O(\varepsilon^3).} \tag{3}
\]
Thus the leading shift is strictly negative precisely away from the pinned mean. For \(w(t)=\cos(\omega t)\), the remainder improves to \(O_\omega(\varepsilon^4)\) and \(\langle W^2\rangle=1/(2\omega^2)\).

An exact example with \(a=1/2\), \(b=3/2\) has
\[
 s_*=(\sqrt{57}-7)/2,\qquad \theta_*=3/\sqrt{57},\qquad r_*=(11+\sqrt{57})/8. \tag{4}
\]
At the different mean \(\theta_0=3/8\), for cosine forcing the fold obeys
\[
 r_{\rm fold}(\varepsilon)=\frac{128}{55}
 -\frac{50176}{82355625\,\omega^2}\varepsilon^2+O_\omega(\varepsilon^4). \tag{5}
\]

## Assumptions and scope

Equation (1) is a one-dimensional deterministic mean-field game with an externally imposed time-dependent probability of three-player encounters. It is not a derived mean-field limit of a temporally switching finite hypergraph, and does not assert individual stochastic fixation. The parameters \(a,b\) remain fixed, \(r>0\) is the varied control parameter, and the interaction share stays in the open probability range for every time. Time averages are over one period \(T>0\); a continuous waveform suffices for the exact pinned fold, while a continuously differentiable mean-zero modulation is used for the smooth small-amplitude expansion. The underlying fixed-mean saddle-node exists as an **interior** stationary collision under (2), with the vertex and fold specified above. The order-\(\varepsilon^2\) expression is at fixed period and fixed waveform, not uniform as frequency tends to zero. Fold conclusions are local to the colliding coexistence states and do not classify all globally possible periodic responses. In all cases the constant full-cooperation solution \(x=1\) is present; near the specified static fold it is attracting because \(G(1)>G(s)\).

## Proof

**1. Static fold and the unique chance to pin it.** Since
\[
 G'(x)= -\frac{h(1-\theta_0)}2+\frac{2d\theta_0}{3}(1+dx),\qquad G''(x)=2\theta_0 d^2/3>0,
\]
its vertex is
\[
 s(\theta_0)=\frac{3h-\theta_0(3h+4d)}{4\theta_0d^2}.
\]
The inequalities \(0<s<1\) are equivalent to (2). Moreover \(s(\theta_0)\) decreases strictly from \(1\) to \(0\) along that open interval. Meanwhile \(k'(x)=h/2+2d(1+dx)/3>0\), with \(k(0)=-1/6\) and \(k(1)=b^2/3-a/2\). Exactly when \(k(1)>0\), the unique zero of \(k\) lies inside \((0,1)\), giving precisely one \(\theta_*\) with \(s(\theta_*)=s_*\). At that point \(G_{\theta_*}(s_*)=g_2(s_*)=g_3(s_*)>0\) and \(r_*=1/G_{\theta_*}(s_*)\). The nonzero second derivative \(G''\) and positive \(\partial_r\dot x=P G>0\) establish the autonomous fold.

**2. Exact pinned return map at arbitrary admissible modulation.** At \(r=r_*\), write \(z=x-s_*\), \(P(z)=(s_*+z)(1-s_*-z)\), and set
\[
 A(t)=G'_{\theta(t)}(s_*)=k'(s_*)[\theta(t)-\theta_*],\qquad Q(t)=\frac{d^2\theta(t)}3>0.
\]
The exact local equation is
\[
 \dot z=r_*P(z)z[A(t)+Q(t)z]. \tag{6}
\]
Because \(\langle\theta\rangle=\theta_*\), the function \(A\) has zero integral. Hence \(z=0\) is a fixed solution and its linear growth factor
\[
 E(t)=\exp\left(r_*s_*(1-s_*)\int_0^t A(u)\,du\right)
\]
satisfies \(E(T)=1\). Expand \(z'=a(t)z+b(t)z^2+O(z^3)\) with
\[
 a(t)=r_*P_0 A(t),\quad b(t)=r_*[P_0Q(t)+(1-2s_*)A(t)],\quad P_0=s_*(1-s_*)>0.
\]
Variation of constants gives for the period return map
\[
 \Pi_{r_*}(s_*+z)=s_*+z+Bz^2+O(z^3),\quad
 B=\int_0^T b(t)E(t)\,dt.
\]
The \(A\)-part vanishes since \(\int_0^T A(t)E(t)\,dt=(E(T)-E(0))/(r_*P_0)=0\). Therefore
\[
 \boxed{B=r_*P_0\int_0^T Q(t)E(t)\,dt>0.} \tag{7}
\]
Differentiating the flow with respect to \(r\) at the pinned solution yields
\[
 \left.\partial_r[\Pi_r(s_*)-s_*]\right|_{r=r_*}
 =P_0G_{\theta_*}(s_*)\int_0^T\frac{dt}{E(t)}>0. \tag{8}
\]
Here the instantaneous value \(G_{\theta(t)}(s_*)\) is constant, independent of mixing. Equations (7) and (8), with multiplier one, are the two nonzero derivatives defining a nondegenerate scalar saddle-node. The standard local return-map expansion with positive quadratic and parameter coefficients proves the two/one/zero periodic states, including stability signs, with no restriction on the forcing amplitude beyond \(0<\theta(t)<1\).

**3. Small-amplitude displacement for other mixing means.** At \((x,r,\varepsilon)=(s,r_0,0)\), denote \(P=s(1-s)\). The necessary derivatives of the right-hand side \(f\) in (1) are
\[
 f_r=P/r_0,\qquad f_{xx}=2Pr_0q,\qquad f_\theta=Pr_0k(s),\qquad f_{\theta\theta}=0.
\]
Write a local periodic solution as \(x(t)=s+\eta+u(t)\), with \(\langle u\rangle=0\). The zero-mean part of the periodic equation has an invertible derivative \(u\mapsto u'\) on zero-mean periodic functions, so the implicit-function theorem solves it uniquely for \(u\) near zero. The remaining averaged scalar equation \(\Phi(\eta,r,\varepsilon)=0\) has a nondegenerate saddle-node at \((0,r_0,0)\), since \(\Phi_r=f_r>0\) and \(\Phi_{\eta\eta}=f_{xx}>0\). Thus the fold \(\Phi=\Phi_\eta=0\) is uniquely smooth for small \(\varepsilon\). Mean-zero forcing makes both its first-order parameter and constant-coordinate displacements vanish; the first-order oscillatory correction is \(u_1=f_\theta W(t)\), with zero mean. At second order, average the Taylor expansion of \(f\) at the fold:
\[
 0=f_r r_2+\tfrac12f_{xx}\langle u_1^2\rangle
  +f_{x\theta}\langle u_1w\rangle.
\]
The last term vanishes because \(\langle Ww\rangle=\langle(W^2)'\rangle/2=0\). Substitution gives \(r_2=-P^2r_0^4q[k(s)]^2\langle W^2\rangle\), establishing (3). For a nonconstant mean-zero \(w\), its primitive has \(\langle W^2\rangle>0\); thus the shift is strictly negative when \(k(s)\ne0\). With a cosine waveform, changing \(\varepsilon\) to its negative is a half-period time translation; the fold parameter is even and smooth in \(\varepsilon\), sharpening the remainder to order four. When \(k(s)=0\), Step 2 gives the exact fold instead of merely a vanishing quadratic coefficient.

**4. Exact calibration.** For \(a=1/2\) and \(b=3/2\), \(k(x)=(x^2+7x-2)/12\). Its unique positive root is \(s_*=(\sqrt{57}-7)/2\). Substitution into the vertex condition gives \(\theta_*=3/\sqrt{57}\), and \(g_2(s_*)^{-1}=(11+\sqrt{57})/8\), establishing (4). At \(\theta_0=3/8\), direct exact calculation gives \(s=1/2\), \(q=1/32\), \(G(s)=55/128\), \(r_0=128/55\), \(k(s)=7/48\); substituting \(\langle W^2\rangle=1/(2\omega^2)\) proves (5).

## Verification

The standalone `verify.py` checks all algebraic calibration identities using exact SymPy arithmetic, finds the Poincaré map's double point by solving the return and unit-multiplier conditions with SciPy for two frequencies and three amplitudes each, and compares measured shifts against equation (5). It separately integrates the neutral orbit at two frequencies, two finite amplitudes, and cosine as well as asymmetric two-harmonic waveforms; the numerical return and Floquet errors are below \(10^{-9}\). Run `python verify.py` with the versions in `requirements.txt`. These numerical checks support, but do not replace, the analytic return-map and Lyapunov–Schmidt proofs.

## Relationship to prior work

Llabrés, Sadekar, Malizia and Battiston [1], especially their well-mixed equations (11)–(13) and Appendix A, establish the autonomous mixed-order nonlinear public-goods game, the possibility of active-cooperation/full-cooperation bistability, and the number of stationary roots. Their results do not vary the mix as an external periodic function and do not give an exactly pinned nondegenerate periodic fold or the universal waveform-primitive coefficient. Related published work on periodically mixing a two-/three-person Prisoner's Dilemma [2] establishes a different temporal budget and a positive shift of a different autonomous fold; it does not identify the cross-game payoff intersection and the exact invariance in (6)–(8). Published work using a finite-state Fermi closure for the same nonlinear source game [3] studies stochastic fixation versus payoff levels at a fixed mix and does not imply the periodic fold result. Classical forcing theory [4] already establishes that sinusoidal forcing can shift generic saddle-node thresholds by an amplitude-squared/frequency-squared law. The generic perturbation mechanism is not claimed as new; the source-specific unique exact pinning and signed general-waveform classification are the contribution here. The other temporal-games study [5] changes participation on spatial networks, not this scalar interaction-order share. The literature comparison is necessarily bounded and does not establish absolute historical priority.

## Limitations

The theorem concerns a prescribed mean-field composition schedule and local coexistence periodic states, not full nonautonomous hypergraph dynamics. At the pinned fold, other, distant periodic orbits are not excluded; the result does not claim global uniqueness or a global cooperation threshold. Away from pinning, the sign is perturbative at fixed waveform and frequency, not guaranteed for arbitrary amplitude. No stochastic finite-population fixation or empirical cooperation prediction is established.

## References

1. J. Llabrés, O. Sadekar, F. Malizia and F. Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228, first public April 8, 2026; https://arxiv.org/abs/2604.07228. Specifically the mixed-order well-mixed equations and Appendix A (accessible full PDF, version 2, September 2026).
2. *Temporal interaction budgets and a reversible cooperative fold in a higher-order Prisoner's Dilemma*, published research record, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-temporal-interaction-budgets-and-a-reversible-cooperative-fold-i--71d91cebdc32.
3. *A logarithmically shifted stochastic fixation threshold in a nonlinear mixed-order public-goods game*, published research record, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-logarithmically-shifted-stochastic-fixation-threshold-in-a-non--7053e63dac2d.
4. J. Zhu, R. Kuske and T. Erneux, *Tipping points near a delayed saddle node bifurcation with periodic forcing*, arXiv:1410.5101, 2014; https://arxiv.org/abs/1410.5101.
5. Y. He et al., *Temporal Interaction and its Role in the Evolution of Cooperation*, arXiv:2401.11782, 2024; https://arxiv.org/abs/2401.11782.
