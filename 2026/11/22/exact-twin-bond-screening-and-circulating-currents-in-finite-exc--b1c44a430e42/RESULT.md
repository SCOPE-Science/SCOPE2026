# Exact twin-bond screening and circulating currents in finite exclusion networks

## Finding

Let \(G\) be a connected undirected weighted graph on \(N\ge3\) vertices with \(1\le k\le N-1\) indistinguishable exclusion particles. Fix adjacent vertices \(u,v\). Hops on every edge other than \(uv\) have equal rates in both directions, given by the positive conductance of that edge. The special edge has rate \(a>0\) from \(u\) to \(v\) and rate \(b>0\) in reverse, with \(a\ne b\). Define \(\rho=k/N\) and \(P=k(N-k)/[N(N-1)]\).

**Exact screening criterion.** Every vertex outside \(\{u,v\}\) has stationary occupation mean exactly \(\rho\) **if and only if** \(u\) and \(v\) are weighted twins outside their mutual edge: for every \(w\notin\{u,v\}\), \(c_{uw}=c_{vw}\), interpreting a missing edge as conductance zero.

Under this criterion put \(g_w=c_{uw}=c_{vw}\), \(s=\sum_{w\notin\{u,v\}}g_w>0\), and \(\delta=(b-a)/(s+a+b)\). The **entire**, unique fixed-particle-number stationary law, for any \(k\)-particle configuration \(\eta\), is

\[
\pi(\eta)=\binom Nk^{-1}\bigl(1+\delta(\eta_u-\eta_v)\bigr).
\]

Not merely their means: the joint law of all vertices outside \(\{u,v\}\) is exactly its equilibrium hypergeometric marginal. The marked occupation means are \(\rho+P\delta\) and \(\rho-P\delta\). For an oriented edge, let \(J_{xy}\) be its expected forward jump rate minus reverse jump rate. Then

\[
J_{uv}=\frac{P(a-b)s}{s+a+b},\qquad
J_{uw}=g_w P\delta,\qquad
J_{vw}=-g_wP\delta,
\]

and all currents with neither endpoint marked vanish. For \(a>b\), these currents decompose into clockwise cycles \(u\to v\to w\to u\) for each \(w\) with \(g_w>0\), of circulation \(g_wP(a-b)/(s+a+b)\). The steady-state entropy-production rate is exactly

\[
\sigma=\frac{P(a-b)s}{s+a+b}\log\!\frac ab>0.
\]

## Assumptions and scope

The state space is the finite collection \(\Omega_{N,k}=\{\eta\in\{0,1\}^N:\sum_x\eta_x=k\}\). Every edge conductance is strictly positive when the undirected edge exists. Each allowed particle hop to an empty neighbor occurs at the specified continuous-time rate. All unmarked bonds are symmetric. The graph is connected; consequently the exclusion chain is irreducible for every intermediate filling. All assertions are finite-volume and hold for arbitrary real positive rates. The exact formula for \(\pi\), the full outside marginal, and the currents require weighted twins, while the if-and-only-if equivalence uses only stationarity of the unmarked one-point means and the condition \(a\ne b\).

## Proof

For a configuration write \(f(\eta)=\eta_u-\eta_v\), and let \(\mu\) be uniform on \(\Omega_{N,k}\). Use \(L^*\) for the adjoint of the generator acting on densities relative to \(\mu\). The only asymmetry is on \(uv\); direct incoming-minus-outgoing balance gives \(L^*1=(b-a)f\). When the other conductances incident to \(u,v\) agree, cancellation of paired transitions from each common neighbor gives \(L^*f=-s f-(a+b)f\): for \(f=1\) each common neighbor contributes total rate \(g_w\) to departure from the marked contrast, and the same cancellation holds for \(f=-1\) and \(f=0\). Transitions disjoint from \(\{u,v\}\) do not change \(f\) and cancel in the adjoint. Thus

\[
L^*(1+\delta f)=\bigl[b-a-\delta(s+a+b)\bigr]f=0.
\]

Because \(|\delta|<1\), this strictly positive density is normalized (the uniform mean of \(f\) is zero), hence is the unique stationary density by finite irreducibility. Pair configurations with \(u\) and \(v\) swapped while holding all other occupations fixed: their \(f\)-contributions cancel, proving the *complete* unmarked joint marginal is unchanged. The uniform probabilities of each directed \(10\) and \(01\) pattern at the marked sites are both \(P\); hence under \(\pi\) they are \(P(1+\delta)\) and \(P(1-\delta)\). The two marked occupation means and the stated current formulas follow by subtraction. Currents on unmarked edges vanish because their occupation differences have zero mean. The cycle decomposition is then direct. Entropy production \(\sum_{\eta\to\xi}\pi(\eta)r_{\eta\xi}\log[\pi(\eta)r_{\eta\xi}/(\pi(\xi)r_{\xi\eta})]\) equals the sum of edge currents times logarithms of directional rate ratios: stationarity cancels the logarithms of stationary probabilities. Only \(uv\) has a nonzero ratio, yielding \(\sigma=J_{uv}\log(a/b)\).

For necessity, suppose only that all unmarked vertices have mean \(\rho\), without assuming twin conductances. Conservation of total particle number implies \(m_u+m_v=2\rho\). If also \(m_u=m_v=\rho\), every symmetric-edge current equals its conductance times the difference of the endpoint means and therefore vanishes. Stationarity at \(u\) would force \(J_{uv}=0\). But \(m_u=m_v\) implies \(\Pr(\eta_u=1,\eta_v=0)=\Pr(\eta_u=0,\eta_v=1)>0\), where strict positivity follows from irreducibility, so \(J_{uv}=(a-b)\Pr(10)\ne0\), a contradiction. Thus \(d=m_u-\rho\ne0\), \(m_v=\rho-d\). At any unmarked vertex \(w\), stationarity and the symmetry of all incident bonds imply

\[
0=\sum_z c_{wz}(m_z-m_w)=(c_{wu}-c_{wv})d.
\]

Therefore \(c_{wu}=c_{wv}\) for every \(w\notin\{u,v\}\), which is the claimed necessary condition.

## Verification

The exact finite-state master equation, every edge-current formula, and every unmarked joint marginal were tested with rational arithmetic in five connected weighted geometries and fillings (61 states checked in total). An independently constructed generator and exact rational stationary linear-system solver checked five fillings each on a twin and a non-twin graph, including the converse for non-twin perturbations. Both standalone programs are included and require only the Python standard library; run \(\texttt{python verify_master.py}\) and \(\texttt{python verify_independent.py}\). These finite checks are corroboration; the proof above is valid for all finite \(N\), all fillings, and arbitrary positive rates.

## Relationship to prior work

Bodineau, Derrida, and Lebowitz (2010) studied a one-dimensional ring with a driven battery, computing macroscopic profiles and correlations rather than this general finite-graph exact invariant law. Sadhu, Majumdar, and Mukamel (2011, 2014) analyzed localized driven bonds and algebraically extended density or correlation disturbances on multidimensional lattices. Their models do not assume the weighted-twin cancellation, and their reported lattice response does not imply the full finite-particle stationary formula, the sharp if-and-only-if screening criterion, or triangle-by-triangle current decomposition. The present statement concerns an exactly soluble structural exception to generic extended responses; it does not claim the original introduction of battery-driven exclusion or of stationary current cycles.

## Limitations

The result does not cover multiple driven bonds, asymmetric rates elsewhere, nonidentical rates of a purported twin pair, reservoirs, infinite-volume dynamics, or general interacting particle models beyond simple exclusion. No relaxation-time or current-fluctuation theorem is claimed. The historical comparison is based on the primary sources listed below and research-result searches, not on an exhaustive proof of publication priority. Independent verification has not yet been performed.

## References

1. T. Bodineau, B. Derrida, J. L. Lebowitz, *A diffusive system driven by a battery or by a smoothly varying field* (first public 2010-03-30), https://arxiv.org/abs/1003.5838 .
2. T. Sadhu, S. N. Majumdar, D. Mukamel, *Long-range steady state density profiles induced by localized drive* (first public 2011-06-09), https://arxiv.org/abs/1106.1838 .
3. T. Sadhu, S. N. Majumdar, D. Mukamel, *Long-range correlations in a locally driven exclusion process* (first public 2014-02-26), https://arxiv.org/abs/1402.6669 .
