# Universal two-term critical extinction and a saturation-independent prey correction in a discrete plankton map

## Finding
For the Holling-II discrete phytoplankton–zooplankton system at a **quadratically tangent predator-invasion threshold**, every orbit in a natural open positive region has a universal inverse-square-root predator extinction clock and a two-term prey recovery law. Under the parameter and initial-state conditions stated below,
\[
\begin{aligned}
v_n&=\sqrt{\frac{(1+c)^3}{2\theta c}}\,n^{-1/2}
-\frac{3(1+c)}{2\theta}\,n^{-1}
+O\!\left(\frac{\log n}{n^{3/2}}\right),\\[3pt]
u_n&=1-\sqrt{\frac{1+c}{2\theta c}}\,n^{-1/2}
+\frac1\theta\,n^{-1}
+O\!\left(\frac{\log n}{n^{3/2}}\right).
\end{aligned}
\]
In particular, the second-order coefficient of prey density is **exactly \(1/\theta\)** and is independent of the Holling-II saturation parameter \(c\), although its leading coefficient is not. Both displayed two-term laws hold for every positive initial state in the specified domain; the remainder constants may depend on that state.

## Assumptions and scope
Let \(0<c\le 1/2\), \(\theta>0\) and \(0<\theta c<1\). Set
\[
r=c\theta,\qquad \beta=\theta(1+c)^2.
\]
The integer-time map is
\[
\begin{aligned}
u_{n+1}&=u_n(2-u_n)-\frac{u_nv_n}{1+cu_n},\\
v_{n+1}&=v_n\left(1-r+\frac{\beta u_n}{1+cu_n}-\theta u_n\right).
\end{aligned}
\]
Start at any \(0<u_0<2\) and \(0<v_0<(2-u_0)(1+cu_0)\). This is a nonempty open region in the positive quadrant. The recurrence is deterministic; \(u_n\) is phytoplankton and \(v_n\) zooplankton. The equality \(r=c\theta\) and the value of \(\beta\) make the predator multiplier at the prey-only equilibrium \((1,0)\) equal to one with *zero first derivative* in prey density, not merely a usual simple invasion threshold. These restrictions form a codimension-two critical surface; no claim is made for arbitrary ecological parameters.

## Proof
Put \(w_n=1-u_n\), and denote the one-step update by primes. Elementary rational simplification at the specified parameters gives the **exact identities**
\[
\boxed{w'=w^2+\frac{(1-w)v}{1+c-cw}},\qquad
\boxed{v'=v\left(1-\frac{\theta c w^2}{1+c-cw}\right)}.
\tag{1}
\]
First establish positivity globally in the stated domain. Define \(B(u)=(2-u)(1+cu)\). On \([0,2]\) this is nonincreasing since \(B'(u)=2c-1-2cu\le0\). If \(0<u<2\), \(0<v<B(u)\), then \(0<u'=u[2-u-v/(1+cu)]<u(2-u)\le1\) and \(0<v'\le v\): the predator multiplier in (1) lies in \( (0,1] \), attaining one only at \(u=1\), because \(0<\theta c<1\), \(|1-u|<1\), and \(1+cu\ge1\). To verify \(v'<B(u')\), if \(u'\le u\), monotonicity gives \(B(u')\ge B(u)>v\ge v'\). If \(u'>u\), then \(u<1\), whence \(v<(1-u)(1+cu)<1\), while \(B(u')\ge B(1)=1+c>1\). Thus the positive region is forward invariant, and every updated prey value satisfies \(0<u_{n+1}<1\). In particular, \(v_{n+1}<v_n\) for all \(n\ge1\), although the first predator step can be neutral if \(u_0=1\).

Let \(v_n\downarrow v_\infty\). If \(v_\infty>0\), the ratio \(v_{n+1}/v_n\to1\) in (1) implies \(w_n\to0\); then the prey update would tend to \(1-v_\infty/(1+c)<1\), contradicting \(u_n\to1\). Hence \(v_n\to0\). To prove \(u_n\to1\), choose any \(0<\delta<1/4\) and take \(n\) sufficiently large that \(v_n<\delta\). For \(0<u_n\le1\),
\[
u_{n+1}\ge u_n(2-u_n-\delta).
\]
As long as \(u_n<1-2\delta\), its growth factor exceeds \(1+\delta\). Once \(u_n\ge1-2\delta\), the lower comparison map takes the entire interval \([1-2\delta,1]\) into itself: its two endpoint values are \(1-\delta-2\delta^2\) and \(1-\delta\), both at least \(1-2\delta\), and the function is concave. Thus \(\liminf u_n\ge1-2\delta\) for each \(\delta\), and \(u_n\to1\). Consequently \(w_n\to0\).

We next establish expansions with controlled errors rather than relying on a formal center-manifold series. For all sufficiently large \(n\), (1) gives
\[
0\le w_{n+1}\le \varepsilon w_n+C_0v_n,
\qquad v_{n+1}\ge(1-\varepsilon)v_n
\]
for arbitrarily small fixed \(\varepsilon>0\). The ratio inequality is a contraction, proving \(w_n=O(v_n)\). From (1), then, \(v_{n+1}=v_n+O(v_n^3)\) and
\[
w_{n+1}=a v_n+O(v_n^2),\qquad a=\frac{1}{1+c}.
\]
Subtracting \(a v_{n+1}\) gives \(w_{n+1}-a v_{n+1}=O(v_n^2)=O(v_{n+1}^2)\), since \(v_{n+1}/v_n\to1\). Relabeling the index yields \(w_n=a v_n+O(v_n^2)\). Substituting once more in (1) shows
\[
w_{n+1}=a v_n+(a^2-a^3)v_n^2+O(v_n^3).
\]
Since \(v_{n+1}=v_n+O(v_n^3)\), subtracting \(a v_{n+1}+b v_{n+1}^2\), with \(b=a^2-a^3\), leaves \(O(v_n^3)=O(v_{n+1}^3)\). Thus, after relabeling,
\[
\boxed{w_n=a v_n+b v_n^2+O(v_n^3)},\qquad
b=a^2-a^3=\frac{c}{(1+c)^3}.
\tag{2}
\]
All constants implicit in the error terms are finite for each fixed admissible parameter pair and starting state.

Inserting (2) into the exact predator update yields
\[
v_{n+1}=v_n-Kv_n^3-Lv_n^4+O(v_n^5),
\quad K=\frac{\theta c}{(1+c)^3}>0,
\quad L=\frac{3\theta c^2}{(1+c)^5}.
\tag{3}
\]
Set \(Y_n=v_n^{-2}\). Expanding (3) gives
\[
Y_{n+1}-Y_n=2K+2L v_n+O(v_n^2).
\tag{4}
\]
Since \(v_n\to0\), summing (4) first yields \(Y_n/n\to2K\). Hence
\[
v_n=A n^{-1/2}(1+o(1)),\qquad A=(2K)^{-1/2}.
\]
The same recurrence shows \(Y_n=2Kn+O(\sqrt n)\), and thus the preliminary sharper estimate \(v_n=A n^{-1/2}+O(n^{-1})\). Consequently
\[
\sum_{j=1}^{n-1}v_j=2A\sqrt n+O(\log n),
\qquad \sum_{j=1}^{n-1}v_j^2=O(\log n).
\]
Summing (4) again now yields
\[
Y_n=2Kn+4LA\sqrt n+O(\log n).
\]
Inversion gives the asserted two-term predator law:
\[
v_n=A n^{-1/2}-\frac{L}{2K^2}n^{-1}
+O\!\left(\frac{\log n}{n^{3/2}}\right),
\qquad \frac{L}{2K^2}=\frac{3(1+c)}{2\theta}.
\]
Finally insert this into (2). The coefficient of \(n^{-1}\) in \(w_n\) is
\[
-\frac{aL}{2K^2}+\frac{b}{2K}=-\frac{1}{\theta},
\]
so \(u_n=1-w_n\) has the displayed \(+1/\theta\) correction. All asymptotics are proved for the entire positive initial-data region specified above. \(\square\)

## Verification
The standalone `check.py` uses only Python's standard library. Execute it with `python3 check.py` from the extracted directory. For three exact rational parameter pairs, it checks the rational map identities, admissible first iterate, exact coefficients \(a,b,K,L\), and the cancellation producing \(+1/\theta\). It also computes three long finite trajectories for diagnostic comparison. Exact finite algebra supports the critical coefficients; the all-time decay and remainder bounds rest on the proof, **not** finite numerical experiments.

## Relationship to prior work
Shoyimardonov (arXiv:2207.01961v1, first posted 2022-07-05) introduced and analyzed the discrete Holling-II predator–prey map, classifying equilibria and Neimark–Sacker behavior. The later 2024 analysis by Shoyimardonov and Rozikov (arXiv:2408.13804v1, first posted 2024-08-25), which explicitly contains this Holling-II map, obtains invariant-set and qualitative convergence results. Its equilibrium classification notes the neutral prey-only boundary but does not state the global two-term critical asymptotics or the cancellation in the prey correction. The new claim is the *joint sharp two-term critical extinction profile* and its saturation-independent prey coefficient, not the model, equilibrium, or elementary neutral invasion test. A published result for this same discrete map concerns the existence of strictly positive prime-two orbits as the ratio \(q=\theta/\beta\) varies; its endpoint \(q=(1+c)^{-2}\) coincides with the present critical parameter ratio, but exclusion of such cycles does not imply global convergence speeds or the two-term coefficients. Neighboring mathematical results establish slow extinction in other discrete predator–prey maps, but different nonlinear terms and threshold conditions do not imply these constants.

## Limitations
The theorem is deterministic and applies only for \(0<c\le1/2\), \(0<\theta c<1\), the exact tuning \(r=c\theta\), \(\beta=\theta(1+c)^2\), and the stated strictly positive initial states. It is not a general global theorem for all Holling-II parameters, for stochastic plankton systems, or for trajectories outside this invariant positive region. The exact stated \(O(\log n/n^{3/2})\) remainder is not a full asymptotic expansion; equivalently phrased unindexed prior results remain a publication-priority risk.

## References
1. S. Shoyimardonov, *Neimark-Sacker bifurcation and stability analysis in a discrete phytoplankton-zooplankton system with Holling type II functional response*, arXiv:2207.01961v1 (first public 2022-07-05), https://arxiv.org/abs/2207.01961.
2. S. K. Shoyimardonov and U. A. Rozikov, *Discrete dynamics of phytoplankton-zooplankton systems with Holling type functional responses*, arXiv:2408.13804v1 (first public 2024-08-25), https://arxiv.org/html/2408.13804v1.
3. S. Shoyimardonov, *Stability, Bifurcation, and Chaos Control in a Discrete-Time Phytoplankton-Zooplankton Model with Holling Type II and Type III Functional Responses*, arXiv:2505.09954 (2025), https://arxiv.org/abs/2505.09954 (related but differing toxin-response term).
