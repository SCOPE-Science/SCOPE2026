# Independent home-reset clocks strictly beat synchronous resetting for complete-graph encounters

## Finding

Two independent unit-jump-rate continuous-time random walkers start at distinct vertices of a complete graph on \(n\ge3\) vertices. They are absorbed at their **first encounter anywhere**, including a meeting caused immediately by a reset. Each walker is assigned its own, distinct home vertex. A common Poisson alarm resets both walkers to their respective homes simultaneously; alternatively, two independent Poisson alarms reset the walkers separately.

For *every* common-alarm rate \(\lambda\ge0\), the common-reset collision time \(T_{\mathrm{com}}\) is exactly exponential:
\[
\Pr(T_{\mathrm{com}}>t)=\exp\!\left(-\frac{2t}{n-1}\right),\qquad
\mathbb E T_{\mathrm{com}}=\frac{n-1}{2}.
\]
For independent reset alarms, each at rate \(r>0\), the first-collision time \(T_{\mathrm{ind}}(r)\) is **strictly stochastically smaller**:
\[
\Pr(T_{\mathrm{ind}}(r)>t)<\Pr(T_{\mathrm{com}}>t)
\quad\text{for every }t>0.
\]
Moreover, writing
\[
Q_n(r)=2(n-1)^2r^2+2(n-1)(2n+1)r+n(n+2),
\]
its mean and the fractional gain over the common-alarm process are
\[
\boxed{\mathbb E T_{\mathrm{ind}}(r)=\frac{n-1}{2}
-\frac{(n-2)(n-1)^2r}{2Q_n(r)}},\qquad
\boxed{\eta_n(r)=\frac{(n-2)(n-1)r}{Q_n(r)}}.
\]
For every \(n\ge3\), there is exactly one optimal strictly positive *per-walker* rate,
\[
\boxed{r_*(n)=\sqrt{\frac{n(n+2)}{2(n-1)^2}}},
\]
with maximal fractional reduction
\[
\boxed{\eta_n^*=\frac{n-2}{2\bigl(2n+1+\sqrt{2n(n+2)}\bigr)}},
\qquad
\lim_{n\to\infty}\eta_n^*=\frac{1}{4+2\sqrt2}.
\]
For \(n=2\), both schemes are neutral because all nontrivial jumps cause encounters. Comparing protocols at the **same total alarm-event rate** does not alter the strict ranking: a common alarm of rate \(\lambda\) has no effect, whereas independent alarms of rate \(\lambda/2\) per walker yield strict improvement whenever \(\lambda>0\).

## Assumptions and scope

The state is an ordered pair \((X_t,Y_t)\) of vertices on the simple complete graph \(K_n\). Distinct home vertices are designated \(A\) for the first walker and \(B\) for the second; initially \((X_0,Y_0)=(A,B)\). Independently, each walker at rate one jumps to a uniformly sampled *different* vertex; hence each permitted jump has intensity \(q=1/(n-1)\). Under common resetting, an independent Poisson clock of rate \(\lambda\) maps \((X,Y)\) to \((A,B)\) in one event, without creating collision. Under individual resetting, independent Poisson clocks each of rate \(r\) map \(X\mapsto A\) and \(Y\mapsto B\), respectively, and **any event leaving \(X=Y\) ends the experiment instantly**. An ineffective reset back to the same home does not change the state. No exclusion, asynchronous holding penalty, or prescribed meeting target is assumed. Rate units refer to each walker's total ordinary jump intensity, not to each edge.

## Proof

**Constant collision hazard for ordinary motion.** From any distinct configuration, the first walker jumps to the second's current vertex at rate \(q\), and vice versa at rate \(q\). Thus the total ordinary collision hazard is the state-independent constant \(h=2q\). Under common resetting, distinct homes remain distinct after every alarm, so no alarm causes absorption. Killing at this constant jump hazard implies \(\Pr(T_{\mathrm{com}}>t)=e^{-ht}\), independently of \(\lambda\) and of the resetting history.

**Strict stochastic dominance.** Under separate alarms, an extra collision can occur whenever the second walker occupies \(A\) and the first alarm fires, or the first occupies \(B\) and the second alarm fires. The extra killing rate at a distinct configuration is precisely
\[
 k_r(X,Y)=r\bigl(\mathbf1_{\{Y=A\}}+\mathbf1_{\{X=B\}}\bigr)\ge0.
\]
If \(S_r(t)=\Pr(T_{\mathrm{ind}}(r)>t)\), the finite-state forward equations, summed over all nonabsorbed configurations, give
\[
\frac{d}{dt}S_r(t)=-hS_r(t)
-\mathbb E\bigl[\mathbf1_{\{T_{\mathrm{ind}}(r)>t\}} k_r(X_t,Y_t)\bigr].
\]
Hence \(e^{ht}S_r(t)\) is nonincreasing from one. For every \(t>0\), with positive probability the first walker jumps \(A\to B\) while the second independently jumps \(B\to C\) to a third vertex \(C\) beforehand, avoiding collision; at time \(t\) the state \((B,C)\) has positive transient probability, making the extra killing rate positive. Therefore the displayed derivative is strictly negative for positive \(t\), and \(S_r(t)<e^{-ht}\) for every \(t>0\).

**Exact finite-state reduction.** By exchanging walker/home labels and permuting the \(n-2\) other vertices, the nonabsorbed ordered pairs divide into the following permutation classes: \(H=(A,B)\), \(X=(B,A)\), \(U=(A,C)\) or \((C,B)\), \(V=(B,C)\) or \((C,A)\), and \(W=(C,D)\) for distinct vertices \(C,D\notin\{A,B\}\). The last class is absent when \(n=3\). Write \(m=n-2\), \(q=1/(n-1)\), and let \(*\) denote absorption. All *out-of-class* transition intensities, including killing, are:

| Source class | Destination and rate |
| --- | --- |
| \(H\) | \(U:2mq\), \(*:2q\) |
| \(X\) | \(V:2mq\), \(*:2q+2r\) |
| \(U\) | \(H:q+r\), \(V:q\), \(W:(m-1)q\), \(*:2q\) |
| \(V\) | \(U:q+r\), \(X:q\), \(W:(m-1)q\), \(*:2q+r\) |
| \(W\) | \(U:2q+2r\), \(V:2q\), \(*:2q\) |

Within-class transitions, if present, cancel in the first-step equations. For \(n=3\), the \(W\) rates vanish and that row is omitted. With \(t_* = 0\), the mean first-encounter times satisfy the **exact** linear backward system
\[
1=\sum_{j\ne i}q_{ij}(t_i-t_j)+q_{i*}t_i,
\quad i\in\{H,X,U,V,W\},
\]
with the foregoing rates and with \(W\) omitted as appropriate. Every state is absorbed almost surely (the jump collision rate \(h>0\) persists), hence the system has a unique solution. Symbolic elimination gives
\[
 t_H=\frac{n-1}{2}-\frac{(n-2)(n-1)^2r}{2Q_n(r)}.
\]
This equals the required mean since the initial state is \(H\). The independent-reset mean is positive and finite for all positive parameters.

**Sharp optimizer and limiting gain.** Differentiating the preceding identity yields
\[
\frac{d}{dr}\mathbb E T_{\mathrm{ind}}(r)
=\frac{(n-2)(n-1)^2\bigl(2(n-1)^2r^2-n(n+2)\bigr)}{2Q_n(r)^2}.
\]
Its numerator has exactly one positive zero, the asserted \(r_*(n)\), with the derivative negative before and positive after. Substitution gives \(\eta_n^*\) and dividing its numerator and denominator by \(n\) gives the limit. As \(r\downarrow0\) or \(r\to\infty\), the fractional gain approaches zero, so this interior minimum is global and unique.

## Verification

The standalone standard-library checker `verify_meeting.py` independently constructs the full ordered-pair killed generator; its rational backward solution agrees with the claimed closed formula for all \(3\le n\le7\) at four rational reset rates. Separately, it solves the five-class quotient over rational numbers for \(3\le n\le30\), and checks optimizer and ordinary collision-hazard identities. It reports 3162 passed checks. In an optional separate symbolic calculation, exact symbolic elimination of the five-class generator gave zero difference from the closed formula and the displayed derivative factorization. To reproduce the self-contained exact checks, run `python3 verify_meeting.py` with Python 3; no third-party package is required. Finite generator instances and floating optimizer comparisons are supporting checks, not the proof for all \(n\); the proof is the general generator reduction and algebra above.

## Relationship to prior work

Suarez-Jimenez, Riascos and Boyer (first public 2026-04-22) formulate simultaneous and independent reset searches and compare their efficiency on several network types. Their mean first-encounter observable concerns **first meeting at a prescribed node** under **simultaneous discrete-time walker steps**. A collision at another vertex preempts an encounter in our absorption convention, and Poisson jump clocks allow only one ordinary move at a time, so their specified-node results do not imply the present complete-graph all-site collision-time distribution or the exact independent-clock optimum. The paper's finding that common resetting can help on homogeneous networks must not be transferred to this different observable.

Rubio-Gomez, Riascos and Mateos (first public 2025-08-07) similarly derive spectral mean first encounters at a *specified* vertex for walkers with individual and shared discrete-time restarting, not the present continuous-time all-site absorption problem. Ohwa (2015, Proposition 3) already establishes the **exponential** meeting law for non-reset continuous-time walkers on complete graphs, which is credited. The additional neutrality of shared resetting follows immediately from this known constant collision-hazard observation; it is **not claimed independently as a novel theorem**. The assessed combined contribution is the **strict all-time independent-clock ordering together with its nontrivial rational mean, unique finite optimum and large-graph gain**.

A published Fourier first-collision-location result for two jointly resetting walkers on odd cycles addresses **nearest-neighbor simultaneous discrete-time updates** and a different graph and resetting protocol. Its coincidence absorption shares the same stopping convention, but neither its first-location transform nor its weak-reset threshold covers independent Poisson clocks on complete graphs. Broad finite absorbing-chain and phase-type methods are preexisting tools, not asserted as new.

## Limitations

The strict improvement relies on counting encounters *caused directly by separate reset events*; ignoring those events would change the first-passage model. The treatment covers two identical continuous-time walkers, complete simple graphs, distinct specified home vertices, independent homogeneous jump rates, and Poisson clocks. It does not establish a general graph optimality principle, an optimum when reset costs depend on events, a result for synchronous discrete-time jumps, or an analogous ordering for prescribed-target meetings. The limiting fractional improvement is an asymptotic mathematical property, not an experimentally observed efficiency gain. An unindexed stronger collision-reset theorem might subsume the result; publication priority has not been independently certified.

## References

1. C. D. Suarez-Jimenez, A. P. Riascos and D. Boyer, *Encounter times of random walkers with simultaneous resetting on networks*, arXiv:2604.20770v1, first submitted 22 April 2026. https://arxiv.org/abs/2604.20770
2. D. Rubio-Gomez, A. P. Riascos and J. L. Mateos, *Mean first-encounter times of simultaneous random walkers with resetting on networks*, arXiv:2508.05313v1, first submitted 7 August 2025. https://arxiv.org/abs/2508.05313
3. T. Ohwa, *Exact computation for meeting times and infection times of random walks on graphs*, Pacific Journal of Mathematics for Industry 7, 5 (2015), Proposition 3. https://doi.org/10.1186/s40736-015-0016-2
4. *Fourier law for first-collision locations under synchronous resetting on odd cycles*, publicly accessible mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-fourier-law-for-first-collision-locations-under-synchronous-rese--8c4ea21ad59b
5. J. Lee, S.-G. Yang, H. J. Park and L. Lizana, *General theory for group resetting with application to avoidance*, Physical Review Research 8, 013227 (2026). https://doi.org/10.1103/zxff-tkq5
