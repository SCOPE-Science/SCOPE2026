# Reentrant optimal abandonment in a two-bee recruitment queue

## Finding
Consider the final-recipient phase of a two-bee, one-donor recruitment system. One bee has already fed and remains at the donor as a scenter; the other is still searching. A lingering fed bee accelerates discovery but, after discovery, competes with the hungry bee for random-order service. Under exponential discovery and service clocks, the exact optimal abandonment rate has an unexpectedly **reentrant** phase diagram.

Let \(\alpha_0>0\) be the searcher's discovery rate without the scenter, \(\alpha_1>\alpha_0\) its discovery rate with the scenter, \(\mu>0\) the donor's service-event rate, and \(\delta\ge0\) the fed bee's abandonment rate. Define \(u=\alpha_1/\mu\), \(v=\alpha_0/\mu\), and \(z=\delta/\mu\), so \(u>v>0\). Let \(T\) be the first time the remaining hungry bee is fed, starting with one searching bee and one fed scenter. Then

\[
\mu\mathbb E[T]=F_{u,v}(z)=\frac{1+u\frac{1+z}{z+1/2}+z(1+1/v)}{u+z}.
\]

Set \(P(u,v)=2vu^2+(v-1)u+v\). If \(P(u,v)>0\), there is exactly one optimal rate \(z_*>0\), explicitly
\[
z_*=\frac{\sqrt{L^2+(u-v)P(u,v)}-L}{2(u-v)},\qquad L=u(1-v)-v.
\]
If \(P(u,v)\le0\), the unique optimal rate is \(z_*=0\): never abandon during this two-bee phase. No other local minima occur.

The parameter-domain classification is sharp. Define \(v_c=1/(1+2\sqrt2)\). For \(0<v<v_c\), let
\[
u_\pm(v)=\frac{1-v\pm\sqrt{1-2v-7v^2}}{4v}.
\]
Then \(v<u_-<u_+\), and **permanent scenting is optimal exactly for** \(u_-\le u\le u_+\). A strictly positive finite optimal abandonment rate exists on *both* sides: \(v<u<u_-\) and \(u>u_+\). At \(v=v_c\), permanent scenting is optimal only at \(u=(1-v)/(4v)\); for \(v>v_c\), a positive finite abandonment rate is always optimal for \(u>v\). Thus increasing cue-aided arrival intensity can switch the optimal policy from finite abandonment to permanent scenting and back to finite abandonment.

For example, at \(v=1/4\), the permanent-scenting window is exactly \(1/2\le u\le1\). At \(u=3/8\), the unique optimum is \(z_*=(\sqrt6-1)/8\); at \(u=3/4\), it is \(z_*=0\); at \(u=2\), it is \(z_*=(\sqrt{46}-5)/14\).

## Assumptions and scope
There are exactly two bees at the initial state: one hungry and searching; one fed and lingering at one donor. Discovery is a memoryless event at rate \(\alpha_1\) as long as the fed bee lingers and at rate \(\alpha_0\) once it abandons. Abandonment is independent and exponentially distributed at rate \(\delta\); \(\delta=0\) means permanent lingering. The donor generates independent Poisson service events at rate \(\mu\) and selects uniformly among all bees currently at the donor. With one waiting hungry bee and one lingering fed bee, successful feeding events have rate \(\mu/2\); after the fed bee departs, the hungry bee is served at rate \(\mu\). Nonproductive selections of the fed bee do not change the state and are thinned out. Service stops the process as soon as the hungry bee is fed. All stated inequalities are exact for this reduced finite-state continuous-time Markov model.

The discovery-rate approximation is a deliberate closure of the spatial velocity-jump search layer, not a theorem for that layer. In particular, results at zero or very large abandonment rate need not satisfy the time-scale assumptions for approximating spatial search by exponential discovery.

## Proof
Let \(H\) denote the initial state (one searcher, one fed scenter), \(A\) one searcher with no scenter, \(W\) one waiting hungry bee with one fed scenter, and \(V\) one waiting hungry bee with no scenter. The only state-changing transitions, in units of the service rate, are \(H\to W\) at rate \(u\), \(H\to A\) at rate \(z\), \(A\to V\) at rate \(v\), \(W\to V\) at rate \(z\), \(W\to\text{fed}\) at rate \(1/2\), and \(V\to\text{fed}\) at rate \(1\). Independence and exponential memorylessness give the backward equations
\[
t_V=1,\qquad t_A=1/v+t_V,\qquad t_W=\frac{1+zt_V}{z+1/2},\qquad t_H=\frac{1+ut_W+zt_A}{u+z}.
\]
Thus \(t_H=\mu\mathbb E[T]=F_{u,v}(z)\), proving the formula including \(z=0\). Its endpoint values are \(F_{u,v}(0)=1/u+2\) and \(\lim_{z\to\infty}F_{u,v}(z)=1+1/v\).

A direct derivative calculation yields the exact identity
\[
F_{u,v}'(z)=\frac{Q(z)}{v(u+z)^2(2z+1)^2},\qquad
Q(z)=4(u-v)z^2+4Lz-P(u,v).
\]
The denominator is positive for \(z\ge0\). If \(P>0\), then \(Q(0)<0\) and its positive leading coefficient gives precisely one positive root (the other root is negative). Consequently \(F\) strictly decreases to that root and strictly increases thereafter. The quadratic formula and \(L^2+(u-v)P>0\) give \(z_*\) above. If \(P\le0\), use the identity \(L=2vu^2-P\ge2vu^2>0\); therefore \(Q(z)>0\) for every \(z>0\) and \(F\) is strictly increasing away from its unique minimum at zero.

As a quadratic in \(u\), the polynomial \(P=2vu^2+(v-1)u+v\) has discriminant \(1-2v-7v^2\). Its nonnegative region changes at the unique positive discriminant zero \(v_c=1/(1+2\sqrt2)\). For \(0<v<v_c\), both roots are strictly larger than \(v\): at \(u=v\), \(P=v^2(2v+1)>0\), while the parabola's vertex \((1-v)/(4v)\) exceeds \(v\) in this range. Thus the negative-\(P\) region is precisely \((u_-,u_+)\), including its zero endpoints for the zero-abandonment optimum. At equality of the discriminant the two endpoints merge; beyond it \(P>0\) throughout \(u>v\). This proves the entire phase diagram and its strictness assertions.

For \(v=1/4\), exact factorization gives \(P(u,1/4)=(u-1/2)(u-1)/2\). Substituting \(u=3/8\) and \(u=2\) into \(Q\) yields \(64z^2+16z-5=0\) and \(28z^2+20z-3=0\), respectively, up to positive factors. Their positive roots are the stated radicals; \(u=3/4\) lies in the zero-abandonment interval.

## Verification
The included standalone `verify.py` independently inverts the transient-state generator and matches its first-entry expected absorption time against the closed formula; checks the derivative identity, discriminant boundary, and exact radical optimizers; and performs 60 independent exact-rational generator inversions on a parameter grid. Execute \`python verify.py\` with SymPy installed. These symbolic checks corroborate the finite-state algebra but are not a substitute for the analytic sign proof above.

## Relationship to prior work
Magrogan, Peleg and Kilpatrick (2026), arXiv:2611.13314v1, introduce the spatial search, fed-scenter abandonment and random-order donor service. Their equations (3) and (11) motivate precisely the queueing mechanisms and exponential arrival closure used here; their equation (15) is a large-abandonment approximation for a whole colony, and their figures show intermediate-optimum behavior by numerical reduction and simulation. Neither the inspected model sections nor the pertinent appendices give the conditional two-bee exact completion-time formula, the disconnected interior-optimizer regimes, or the sharp \(v_c\) threshold. Standard continuous-time Markov-chain first-step equations are established tools and are not themselves claimed as novel. Research on active search with resetting concerns a different mechanism without a recruited fed bee simultaneously blocking service.

## Limitations
This is a conditional final-recipient theorem, not a complete two-bee process from an all-hungry initial condition and not a theorem for a colony of arbitrary size. It assumes constant exponential cue-on and cue-off discovery rates, which may fail for ballistic trajectories and time-varying spatial cues. It does not establish an empirically optimal residence time for bees or optimality across arbitrary abandonment policies (only constant exponential abandonment rates). The phase diagram is a mathematically exact benchmark for the reduced chain, with no claim of priority over unlocated equivalent queueing results. Independent scientific validation has not been performed.

## References
1. W. Magrogan, O. Peleg and Z. P. Kilpatrick, *Chemotactic recruitment offsets congestion in honeybee trophallaxis*, arXiv:2611.13314v1, first publicly posted 2026-11-09. https://arxiv.org/abs/2611.13314 ; https://arxiv.cnoctave.top/pdf/2611.13314 .
2. Y. Baouche and C. Kurzthaler, *Optimal first-passage times of active Brownian particles under stochastic resetting*, Soft Matter 21 (2025), 5998–6011, DOI:10.1039/D5SM00340G. https://pubs.rsc.org/en/content/articlehtml/2025/sm/d5sm00340g . Compared as a different search/resetting framework, not a predecessor claiming the present two-bee classification.
