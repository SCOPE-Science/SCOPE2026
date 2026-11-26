# Universal strong-reset current and the two-site anomaly in an open exclusion chain

## Finding
Fix an integer \(L\geq2\) and boundary rates \(\alpha,\beta>0\). In the finite, open, locally resetting totally asymmetric simple exclusion process defined below, let \(J_L(r)\) denote stationary particle throughput at reset rate \(r>0\). As \(r\to\infty\), with \(L,\alpha,\beta\) held fixed,
\[
J_L(r)=\begin{cases}
(\alpha+\beta)r^{-1}+O(r^{-2}),&L=2,\\
\alpha r^{-1}+O(r^{-2}),&L\ge3.
\end{cases}
\]
The exact first-order coefficient is independent of chain length and of extraction rate for every \(L\ge3\), and a two-site chain has the different coefficient \(\alpha+\beta\). Equivalently, \(\lim_{r\to\infty}rJ_L(r)\) equals \(\alpha+\beta\) for \(L=2\) and \(\alpha\) for all \(L\ge3\).

## Assumptions and scope
A configuration is \(\eta\in\{0,1\}^L\), where \(\eta_j=1\) means site \(j\) is occupied. Each particle at site \(j<L\) jumps to an empty site \(j+1\) at rate one; particles enter site \(1\) at rate \(\alpha\) if it is empty, and leave site \(L\) at rate \(\beta\) if occupied. Independently, each occupied site \(j\ge2\) sends its particle directly to site \(1\) at rate \(r\), but only when site \(1\) is empty; such a jump preserves particle count. No two particles can occupy a site. The continuous-time chain is irreducible for each finite \(r>0\), so it has one stationary distribution \(\pi_r\). Define \(J_L(r)=\beta\,\pi_r\{\eta_L=1\}\), equivalently \(\alpha\,\pi_r\{\eta_1=0\}\) by exact stationary particle conservation. All asymptotic constants may depend on fixed \(L,\alpha,\beta\); no bound uniform in growing \(L\) is claimed.

## Proof
Write the generator as \(Q_r=rR+S\), separating the reset and ordinary (hopping, injection, extraction) transitions. Let \(e_1=(1,0,\ldots,0)\), let \(z_j\) be the singleton state with the only particle at site \(j\), and let \(\varnothing\) be the empty state. Partition the finite state space into \(T=\{\eta:\eta_1=0,\ \sum_{j=2}^L\eta_j\ge1\}\) and its complement \(E\). Put \(m=|T|=2^{L-1}-1\). Every state in \(T\) has at least one reset edge, and every reset edge lands in \(E\). No state in \(E\) has a reset edge.

For a state \(x\), the continuous-time Markov chain tree theorem expresses its unnormalized stationary weight \(\tau_x(r)\) as the sum over all directed spanning in-trees rooted at \(x\), each weighted by the product of its edge rates. These are nonnegative polynomials in \(r\) of degree at most \(m\). There exists a tree rooted at \(e_1\) of degree \(m\): select, for each \(\eta\in T\), one available resetting transition into \(E\); for each configuration in \(E\setminus\{e_1,\varnothing\}\), move its rightmost downstream particle to the right or extract it, repeatedly, while leaving its site-1 particle in place, until the state becomes \(e_1\); choose the corresponding first step for each such configuration. From \(\varnothing\), select injection into \(e_1\). The chosen slow edges are acyclic because each step decreases the number of downstream particles or advances the rightmost one toward extraction. Every selected reset edge exits \(T\) and enters \(E\), so the whole graph is a rooted in-tree. Hence \(\tau_{e_1}(r)=c r^m+O(r^{m-1})\) for some \(c>0\).

For a root \(x\in T\), its own outgoing edge is absent, so at most \(m-1\) reset edges can occur in any rooted tree. For \(x\in E\setminus\{e_1\}\), suppose a tree had all \(m\) reset edges: the state \(z_2\in T\) has only one resetting transition, \(z_2\to e_1\), and the state \(e_1\) has only one outgoing transition, its unit-rate hop \(e_1\to z_2\). Both would be selected, forming a prohibited directed two-cycle. Thus every other \(\tau_x(r)=O(r^{m-1})\), and after normalization
\[
\pi_r(e_1)=1+O(r^{-1}),\qquad \pi_r(x)=O(r^{-1})\quad(x\ne e_1).
\]
These inequalities are exact consequences of finite nonnegative tree polynomials, not a mean-field closure.

The state \(z_2\in T\) has exactly one reset opportunity, at rate \(r\). Its ordinary outgoing rate is bounded independently of \(r\). No reset transition enters \(z_2\); its only ordinary incoming transition from \(e_1\) is the unit-rate right hop. All other ordinary incoming states have stationary probability \(O(r^{-1})\). Stationarity therefore gives
\[
(r+O(1))\pi_r(z_2)=\pi_r(e_1)+O(r^{-1})=1+O(r^{-1}),
\]
so \(\pi_r(z_2)=r^{-1}+O(r^{-2})\). Any other \(x\in T\setminus\{z_2\}\) has ordinary incoming flow \(O(r^{-1})\): no direct ordinary transition from \(e_1\) enters it. Its total reset departure rate is \(k_xr\) for some integer \(k_x\ge1\). Thus \(\pi_r(x)=O(r^{-2})\). In particular, \(\pi_r(z_L)=O(r^{-2})\) when \(L\ge3\).

The empty configuration is entered only when a particle exits from \(z_L\), and left only when injected at site \(1\). Its exact stationary balance is
\[
\alpha\pi_r(\varnothing)=\beta\pi_r(z_L).
\]
For \(L=2\), \(z_L=z_2\), hence \(\pi_r(\varnothing)=\beta/(\alpha r)+O(r^{-2})\). For \(L\ge3\), \(\pi_r(\varnothing)=O(r^{-2})\). Finally, the only site-1-vacant configurations are \(\varnothing\) and the states in \(T\). Therefore
\[
\begin{aligned}
J_L(r)&=\alpha\pi_r\{\eta_1=0\}\\
&=\alpha\bigl(\pi_r(\varnothing)+\pi_r(z_2)+O(r^{-2})\bigr),
\end{aligned}
\]
which yields both stated coefficients and completes the proof.

## Verification
`CHECK.py` constructs the exact finite-state transition rules, solves the stationary linear system for multiple positive parameters and sizes, and checks normalized probabilities, stationarity, boundary-current conservation, and numerical convergence of \(rJ_L(r)\) to its predicted value. It also independently derives the exact two-site rational formula by symbolic stationary linear algebra. The executable reports 353 passed finite/symbolic assertions in the recorded run. These checks detect implementation or algebra errors; the all-size theorem is proved by the tree argument above, not finite enumeration.

## Relationship to prior work
Pelizzola and Pretti introduced and analyzed this open-boundary local-reset model, mostly through stationary mean-field and kinetic Monte Carlo techniques, including a strong-reset regime discussed in a joint large-size limit. That paper provides the model and substantial large-system phenomenology but does not state the present exact fixed-\(L\), \(r\to\infty\) coefficient theorem or isolate its two-site anomaly. Pelizzola, Pretti, and Zamparo previously examined local resetting with periodic rather than open boundaries. More recent exact investigations of three-site reset exclusion emphasize covariance sign changes rather than a universal all-size throughput coefficient. The limits \(r\to\infty\) at fixed finite \(L\) and \(L\to\infty\) under resetting-rate scaling must not be conflated.

## Limitations
This is a leading two-term asymptotic with a fixed-size remainder; it does not give a uniform bound as \(L\to\infty\), a complete finite-reset stationary distribution, or an optimal reset rate. It requires local (particle-specific) resets to a vacant injection site, unit ordinary hopping, positive fixed injection and extraction rates, and at least two sites. The argument does not extend automatically to global configuration resets, position-dependent reset rates, or alternative capacity rules. Published or unindexed mathematically equivalent statements remain a residual priority risk despite the stated comparisons.

## References
1. A. Pelizzola and M. Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions*, Journal of Physics A: Mathematical and Theoretical **55** (2022), 454001, DOI: https://doi.org/10.1088/1751-8121/ac9d72 ; accessible version https://arxiv.org/html/2402.13698v1 ; institutional record https://iris.polito.it/handle/11583/2973072 .
2. A. Pelizzola, M. Pretti, and M. Zamparo, *Simple Exclusion Processes with Local Resetting*, https://arxiv.org/abs/2012.10993 (2020).
3. The finite-state continuous-time Markov chain tree theorem (standard stationary in-tree formula; used explicitly in the proof above).
