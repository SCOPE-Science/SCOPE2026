# Global turnout capture and sharp basin selection in a negative-partisanship map

## Finding

For the symmetric two-candidate threshold-mobilization model of Fontanari [1], consider the subcritical bistability wedge
\[
\frac12<\lambda<1,\qquad 2<\gamma<1+\frac1\lambda 2^{1-1/\lambda}.
\]
Use the natural endpoint-saturated continuation of the stated individual surplus-maximization rule whenever its formal indifference equation has no root in the electorate's ideological interval. Then **every nonzero initial mobilization reaches full turnout in finite time**. Once full turnout is reached, there is exactly one positive threshold \(z_*\in(0,1)\), defined in (F) below, for the absolute difference between the two polling fractions:

* Smaller difference: convergence to the balanced half-and-half equilibrium.
* Difference equal to \(z_*\): an unstable, nonsaturated prime-two orbit.
* Larger difference: **exact** alternating unanimous support after finitely many rounds.

The origin is a fixed state, and there are no other periodic orbits. Moreover, the balanced basin contains **all sufficiently small positive-turnout states, regardless of their initial candidate ratio**: abstention can reverse the destination of an otherwise identical 80:20 split. The time to reach exact alternating unanimity diverges logarithmically as the full-turnout difference approaches \(z_*\) from above. At \(\lambda=2/3,\gamma=41/20\), the basin threshold is available in radicals and corresponds to a critical initially mobilized candidate share of approximately \(0.739945567566123\).

The source [1] already finds the parameter wedge, the balanced and saturated attractors, and an implicit unstable two-cycle. The contribution here is the **complete global attraction/capture classification on the entire electoral simplex**, with finite activation and absorption bounds, the sharp escape-time law, and an explicit radical threshold in a natural rational example.

## Assumptions and scope

Let \(\Delta=\{(p,q):p\ge0,q\ge0,p+q\le1\}\); \(p,q\) are the fractions supporting candidates A and B. The abstention fraction is \(1-p-q\). Fix \(a=1/\lambda\in(1,2)\), \(c=\gamma-1\in(1,a2^{1-a})\), and define the drives
\[
U_A=p+\gamma q,\qquad U_B=q+\gamma p.
\]
Individuals have a uniform latent coordinate \(u\in[0,1]\), with candidate-specific activation thresholds \(u^a\) and \((1-u)^a\). If \(U_A^\lambda+U_B^\lambda<1\), the next state is \((U_A^\lambda,U_B^\lambda)\). Otherwise all individuals qualify for at least one candidate and choose the one with larger surplus \(U_A-u^a\) or \(U_B-(1-u)^a\). The resulting candidate shares are the lengths of their respective choice subsets of \([0,1]\).

**Endpoint convention:** when the formal surplus-equality root lies below \(0\) or above \(1\), every individual selects the same candidate; the cut is clipped to the relevant endpoint. This is the direct individual-level choice rule, and is needed since the root asserted in Eq. (7) of [1] need not exist inside \([0,1]\) for \(\gamma>2\). Without an endpoint convention the printed implicit-cut equation is not a globally defined map. No claim is made about alternative conventions.

For an initial state \((p_0,q_0)\ne(0,0)\) write \(s_0=p_0+q_0\) and let \(T\) be the first integer with \(p_T+q_T=1\). For \(z\in[0,1]\), define
\[
H(z)=\left(\frac{1+z}{2}\right)^a-\left(\frac{1-z}{2}\right)^a.\tag{H}
\]
The unique interior number \(z_*\) is specified by
\[
H(z_*)=c z_* .\tag{F}
\]
Here \(z_T=|p_T-q_T|\) is an absolute *full-turnout* difference, not the initial difference if the original state contains abstainers.

## Proof

**1. Finite capture of full turnout.** Before full turnout, the overlap condition is false, and \(p+q=s\in(0,1)\). Since \(\gamma>1\), both drives are at least \(s\), so
\[
s_{t+1}=U_A^\lambda+U_B^\lambda\ge 2s_t^\lambda\ge 2s_t
\]
for every step that remains in the non-overlapping branch. If the new state is already fully mobilized there is nothing to prove. Otherwise the same argument repeats. As \(s_t\le1\), this implies
\[
T\le\left\lceil\log_2\frac1{s_0}\right\rceil.\tag{1}
\]
A state with full turnout stays fully mobilized, because \(p+q=1\) gives \(U_A\ge1\) and \(U_B\ge1\); consequently every individual qualifies for both candidates. The zero state is fixed.

**2. Exact full-turnout scalar recurrence, including endpoints.** On \(p+q=1\), put \(d=p-q\). The difference between drives is \(U_A-U_B=(1-\gamma)d=-cd\). The strictly increasing odd-about-one-half function
\[
h(u)=u^a-(1-u)^a,\qquad h(0)=-1,\quad h(1)=1,
\]
separates the candidates' surplus choices. Thus if \(d>0\) the next majority is B; if \(d<0\) the next majority is A. Including the cases where the cut is an endpoint, the absolute difference evolves as
\[
z_{t+1}=\Phi(z_t),\qquad \Phi(z)=H^{-1}(\min\{cz,1\}),\quad z_t=|d_t|.\tag{2}
\]
The sign of every nonzero difference reverses at each step. Formula (2) is valid for all \(0\le z\le1\).

**3. Exactly one positive interior threshold.** Direct differentiation gives
\[
H'(0)=a2^{1-a}>1,\qquad H(0)=0,\qquad H(1)=1,
\]
and, for \(0<z<1\),
\[
H''(z)=\frac{a(a-1)}4\left[\left(\frac{1+z}{2}\right)^{a-2}-\left(\frac{1-z}{2}\right)^{a-2}\right]<0.\tag{3}
\]
The inequality \(a2^{1-a}>1\) follows by strict concavity of \(\log a+(1-a)\log2\) between its zero endpoints \(a=1,2\). Strict concavity of \(H\), with \(H(0)=0\), makes \(H(z)/z\) strictly decreasing from \(a2^{1-a}\) to \(1\). Since \(1<c<a2^{1-a}\), equation (F) has exactly one solution in \((0,1)\). Also \(z_*<1/c\), because \(H(z_*)=cz_*<H(1)=1\).

For \(0<z<z_*\), \(H(z)>cz\), so \(\Phi(z)<z\). For \(z_*<z<1\), \(H(z)<cz\), so \(\Phi(z)>z\), with saturation at \(1\) when \(cz\ge1\). At \(z=0,z_*,1\), the amplitude remains fixed. Thus every amplitude below \(z_*\) decreases monotonically to zero, and every amplitude above \(z_*\) increases monotonically until it reaches one. Indeed, a nonsaturated increasing orbit cannot converge to an interior value other than \(z_*\), but every one of its terms exceeds \(z_*\). Once its amplitude reaches \(1/c\), the following step gives exactly \(1\). This proves finite-time polarized capture, not merely asymptotic approach.

Since the map \(\Phi\) is increasing, its periodic points are exactly its fixed points. Hence the original signed vote-difference map has only the balanced fixed point and the two prime-two cycles of amplitudes \(z_*\) and \(1\) on the full-turnout edge. A nonzero periodic orbit off that edge is impossible by strict turnout growth. The only remaining periodic point is the zero state.

**4. Explicit escape bounds and asymptotics.** Strict concavity also yields \(H'(z_*)<H(z_*)/z_*=c\). Let
\[
L=\frac{c}{H'(z_*)}>1.\tag{4}
\]
For \(z>z_*\) with \(z<1/c\), the derivative of the nonsaturated branch is \(\Phi'(z)=c/H'(\Phi(z))>L\). The mean value theorem therefore gives
\[
\Phi(z)-z_*\ge L(z-z_*).\tag{5}
\]
Writing \(K(z)\) for the number of full-turnout iterations until amplitude one, we obtain the finite bound
\[
K(z)\le 1+\max\left\{0,\left\lceil\frac{\log\big((1/c-z_*)/(z-z_*)\big)}{\log L}\right\rceil\right\},\qquad z>z_* .\tag{6}
\]
Near \(z_*\), the smooth recurrence is \(z_{t+1}-z_*=L(z_t-z_*)+O((z_t-z_*)^2)\). Choose a small fixed neighborhood on which expansion is uniformly greater than one. The sum of all distances from \(z_*\) before leaving that neighborhood is bounded independently of the starting distance, by comparison with a reverse geometric series. Summing logarithms of the recurrence therefore produces a bounded cumulative distortion. Outside this neighborhood, the strict increasing drift gives a uniformly bounded remaining number of iterations to saturation. Consequently
\[
K(z)=\frac{\log(1/(z-z_*))}{\log L}+O(1)\quad\text{as }z\downarrow z_* .\tag{7}
\]
The intermediate two-cycle is thus repelling, with second-iterate multiplier \(L^2>1\).

**5. Small-turnout immunity and a turnout-induced destination reversal.** For each under-mobilized step define the *relative* candidate difference \(m_t=|p_t-q_t|/(p_t+q_t)\), and put \(k=(\gamma-1)/(\gamma+1)\in(0,1)\). Directly from the two power-law updates,
\[
m_{t+1}=\tanh\left(\lambda\operatorname{arctanh}(k m_t)\right)\le k m_t.\tag{8}
\]
Thus \(m_t\) contracts at least geometrically while some voters remain uncommitted. At the first full-turnout update after \(T-1\) under-mobilized rounds, the absolute drive difference is \(c s_{T-1}m_{T-1}\), and \(s_{T-1}\le1\). If \(k^{T-1}m_0<z_*\), then
\[
H(z_T)=\min\{c s_{T-1}m_{T-1},1\}<H(z_*),
\]
so the new full-turnout state is strictly inside the balanced basin. For each fixed positive integer \(N\), all sufficiently small positive initial totals remain under-mobilized for the first \(N\) rounds: the map is continuous at the zero state, and its first finitely many iterates tend uniformly to zero as initial turnout tends to zero. Choose \(N\) with \(k^N<z_*\). Then all sufficiently small positive initial totals eventually enter the balanced basin, uniformly over every initial candidate ratio (including one-sided support). This also shows that the apathy origin is a nonattracting isolated fixed point.

**6. Exact rational-parameter example.** Choose \(\lambda=2/3\) and \(\gamma=41/20\), so \(a=3/2\), \(c=21/20\). For \(z\in(0,1)\), put
\[
X=\sqrt{(1+z)/2},\qquad Y=\sqrt{(1-z)/2},\qquad S=X+Y.
\]
As \(X^2+Y^2=1\), direct factorization gives
\[
\frac{H(z)}z=\frac{X^3-Y^3}{X^2-Y^2}=\frac{1+XY}{X+Y}=\frac12\left(S+\frac1S\right).
\]
The equation \(H(z_*)=cz_*\) therefore yields
\[
S_*=\frac{21+\sqrt{41}}{20},\qquad z_*=S_*\sqrt{2-S_*^2}\approx0.4798911351322463.\tag{9}
\]
On the fully mobilized edge, \(p_0=0.70\) approaches the balanced state, whereas \(p_0=0.80\) reaches exact alternating unanimity after finitely many rounds. The intervening critical share is \((1+z_*)/2\approx0.7399455675661231\). The same committed ratio 80:20 has two rigorously different outcomes: full-turnout \((p_0,q_0)=(4/5,1/5)\) has initial difference \(3/5>z_*\) and reaches alternating unanimity; half-turnout \((p_0,q_0)=(2/5,1/10)\) has drives \(U_A=121/200\), \(U_B=23/25\), enters full turnout in one step, and has new difference \(z_1\) satisfying \(H(z_1)=63/200<c z_*\), so converges to parity. The inequalities are exact since expression (9) gives \(2/5<z_*<3/5\). These approximate decimals are for orientation; equation (9) is exact.

## Verification

Run the standalone standard-library program `python CHECK.py`. It independently reconstructs the electorate's choices by sampling uniformly spaced ideological coordinates, compares the result with the analytic piecewise map, verifies the exact radical threshold to numerical precision, checks full-turnout capture over 400 random starts including very small initial mobilization, and checks the sharp amplitude recursion, both basins, turnout-induced destination reversal and delayed finite-time absorption. It passes 160 independent 10,001-point quadrature checks and reports escape times that increase by approximately \(\log(10)/\log L\) per additional decimal place of proximity to the threshold. These tests are finite numerical corroboration; Steps 1–5 are the proof for all allowed parameters and initial states.

## Relationship to prior work

Fontanari [1, v2, Secs. 2–4] supplies the two-dimensional individual-threshold model, its implicit indifference cut, the pitchfork/border/flip boundaries, the subcritical wedge, and the implicit unstable two-cycle [Eq. (19)]. None of these is claimed new. The present result resolves global behavior from **every** nonzero starting state of the simplex in the wedge, proves a uniform finite-time turnout bound, gives an exact full-edge basin criterion, uniform low-turnout access to the balanced basin and an explicit 80:20 turnout reversal, finite-time alternating saturation, counts all periodic states, and quantifies logarithmic escape from the separatrix. It also spells out the endpoint saturation required when the cut is outside the ideological interval. The 2017 conformist/anticonformist double-clique \(q\)-voter model [2] has different individual updating, network topology and state equations; its polarizing phase transition does not furnish this power-threshold-map classification. General monotone-map and one-dimensional concavity techniques are established background, not newly invented methods.

## Limitations

The result assumes identical candidate parameters, uniformly distributed latent ideological coordinates, deterministic synchronous evaluation rounds, exactly the activation and surplus rules above, and strict inequalities in the displayed parameter wedge. It is a theorem about the idealized map, not observed electoral behavior, the stochastic finite-electorate process, or the asymmetric-parameter model. The exact full-turnout capture time depends on initial turnout; classification for initial abstention uses the state at its **first full-turnout round**, not just the initial absolute candidate difference. The endpoint-saturated continuation is stated explicitly because the unmodified implicit-cut equation alone does not specify outcomes when the desired cut is outside \([0,1]\). No global claim is made for other conventions or the wedge boundaries.

## References

[1] J. F. Fontanari, *Negative partisanship drives anti-frontrunner volatility in election dynamics*, arXiv:2610.25210, first public version 18 October 2026; version 2 dated 2 November 2026, https://arxiv.org/html/2610.25210v2 . In particular Eqs. (1)–(19), Secs. 2–4.

[2] T. Krueger, J. Szwabiński and T. Weron, *Conformity, Anticonformity and Polarization of Opinions: Insights from a Mathematical Model of Opinion Dynamics*, Entropy 19 (2017), 371, https://www.mdpi.com/1099-4300/19/7/371 .
