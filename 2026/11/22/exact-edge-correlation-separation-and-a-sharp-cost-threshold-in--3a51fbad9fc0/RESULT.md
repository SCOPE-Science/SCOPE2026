# Exact edge-correlation separation and a sharp cost threshold in a four-site donation game

## Finding

A finite death–birth game can distinguish the *arrangement* of a fixed multiset of cooperative edge benefits, even when every vertex has the same degree. On a four-cycle with two edges of benefit \(H\) and two of benefit \(L\), define the clustered layout \((H,H,L,L)\) and the alternating layout \((H,L,H,L)\), in cyclic edge order. A randomly placed single cooperator fixes with probabilities \(\rho_{\mathrm{cl}}\) and \(\rho_{\mathrm{alt}}\), respectively.

**All-strength cost-free classification.** For every \(H,L\geq0\), \(H\ne L\), and selection intensity \(w>0\), when the contribution cost is zero,
\[
\rho_{\mathrm{alt}}=\tfrac14,\qquad
\rho_{\mathrm{cl}}-\tfrac14=
\frac{(x-y)^2[3x^2+7xy+3y^2+11x+11y+9]}{2D(x,y)}>0,
\qquad x=wH,\quad y=wL,
\]
where
\[
\begin{aligned}
D(x,y)={}&51(x^4+y^4)+190xy(x^2+y^2)+286x^2y^2\\
 &+288(x^3+y^3)+864xy(x+y)\\
 &+614(x^2+y^2)+1268xy+576(x+y)+192.
\end{aligned}
\]
Thus an alternating high/low edge pattern has **exactly neutral** fixation at arbitrary positive benefit contrast, whereas placing the same two high-benefit edges together yields strictly above-neutral fixation. The result is nonperturbative in the selection intensity.

**Sharp positive-cost separation.** Fix \(H=5\), \(L=1\), \(w=\tfrac14\), and let each cooperative endpoint pay cost \(c>0\) on each incident edge. For the full fitness-admissible interval \(0<c<2\), the clustered fixation probability always exceeds the alternating one, and the alternating one is always below \(\tfrac14\). There is exactly one cost \(c_*\in(0,2)\), given as the unique root in that interval of
\[
\begin{aligned}
N(c)={}&30c^9-2157c^8+64435c^7-1046362c^6+10109558c^5\\
&-59511289c^4+208484029c^3-398421956c^2\\
&+323640240c-15004800,
\end{aligned}
\]
with \(c_*=0.0492757366334561\ldots\). The clustered game has \(\rho_{\mathrm{cl}}>\tfrac14\) precisely when \(0<c<c_*\), equals \(\tfrac14\) at \(c=c_*\), and has \(\rho_{\mathrm{cl}}<\tfrac14\) for \(c_*<c<2\). At \(c=\tfrac1{100}\),
\[
\rho_{\mathrm{cl}}=\frac{3914160121776143533946622}{15437973229592093026196383}>\frac14>
\frac{46254366}{185678399}=\rho_{\mathrm{alt}}.
\]
These are judgments relative to neutral fixation, not a claim that cooperation is favored over defection under the stronger bidirectional fixation criterion.

## Assumptions and scope

The connected undirected four-cycle has vertices \(0,1,2,3\) and edges \(01,12,23,30\), in that order. The two edge layouts have the same multiset \(\{H,H,L,L\}\). For each action profile \(s_i\in\{0,1\}\), cooperative behavior is \(s_i=1\); its payoff is
\[
P_i(s)=\sum_{j\sim i}\bigl(b_{ij}s_j-cs_i\bigr).
\]
Here \(b_{ij}=b_{ji}\) is the benefit carried by **that edge**; the benefit is not a donor-vertex property. Consequently a cooperator can confer different benefits to its two neighbors. Fitness is linear, \(F_i(s)=1+wP_i(s)\). A death vertex is chosen uniformly; its two neighbors compete to replace it in proportion to their *pre-replacement* fitness. There is no mutation. Each of the four one-cooperator initial states has probability \(1/4\). All-zero and all-one profiles are the absorbing states. For the positive-cost theorem \(0<c<2\) makes \(F_i\geq1-c/2>0\); for cost zero, all fitnesses are at least one.

## Proof

**Exact absorbing-chain reduction.** For any profile \(s\) with mask \(m\in\{0,\ldots,15\}\), a death at vertex \(i\) and parent at vertex \(j=i\pm1\pmod4\) has probability
\[
\frac14\frac{F_j(s)}{F_{i-1}(s)+F_{i+1}(s)}.
\]
The next profile replaces only coordinate \(i\) by \(s_j\). Assemble those probabilities into the transient transition matrix \(Q\) and the one-step transition column \(r\) to the all-one state. Because all fitnesses are strictly positive and the graph is connected, absorption occurs with probability one, so \(I-Q\) is invertible and the fixation vector is \(f=(I-Q)^{-1}r\). The fixation probability is \(\tfrac14\sum_{i=0}^3 f_{2^i}\). This identity is an exact rational calculation, not a numerical Markov-chain approximation. Graph automorphisms preserving the edge labels reduce the fourteen transient states to ten clustered or five alternating orbit states; aggregating transitions is legitimate because these automorphisms commute with the full transition law.

**Cost-free identity.** Substitute \(c=0\), \(x=wH\), \(y=wL\) in that finite system, perform rational elimination and cancel common factors. The alternating orbit system gives \(\rho_{\mathrm{alt}}=1/4\) identically. The clustered orbit system gives the displayed rational expression with denominator \(D(x,y)\). Its denominator is strictly positive for all \(x,y\geq0\), and the numerator is strictly positive whenever \(x\ne y\). This proves the universal all-strength separation.

**Exact positive-cost formulas.** With \(H=5\), \(L=1\), and \(w=1/4\), the same elimination yields
\[
\rho_{\mathrm{alt}}(c)=\frac{(c-10)(c-2)(2c-7)}{(c-7)(c-5)(3c-16)},
\qquad
\rho_{\mathrm{cl}}(c)-\tfrac14=\frac{N(c)}{4D_c(c)},
\]
where
\[
\begin{aligned}
D_c(c)={}&18c^9-1347c^8+42753c^7-759242c^6+8345254c^5\\
&-59029779c^4+269178291c^3-763949868c^2\\
&+1225277200c-845827200.
\end{aligned}
\]
Also,
\[
\rho_{\mathrm{alt}}(c)-\tfrac14
=\frac{c(5c^2-72c+199)}{4(c-7)(c-5)(3c-16)}<0
\]
for \(0<c<2\): the quadratic is decreasing and positive throughout this interval, while the denominator is negative.

To prove the unique threshold, substitute \(c=2t/(1+t)\) with \(t>0\). The ascending coefficients of \((1+t)^9N(2t/(1+t))\) are
\[
(-15004800,\ 512237280,\ 3044383216,\ 7375507704,\ 9944710544,\ 8220641176,\ 4270924496,\ 1360894888,\ 242781232,\ 18529000).
\]
They have exactly one sign change, so Descartes' rule gives at most one positive root; the values at \(t=0\) and \(t\to\infty\) have opposite signs, proving existence and uniqueness. All coefficients of \(-(1+t)^9D_c(2t/(1+t))\) are positive, so \(D_c(c)<0\) throughout \(0<c<2\). Since \(N(0)<0\), the stated signs of \(\rho_{\mathrm{cl}}-1/4\) follow.

Finally direct exact subtraction gives
\[
\rho_{\mathrm{cl}}-\rho_{\mathrm{alt}}
=\frac{2(c-20)(c-10)(c-4)(c-2)Q_c(c)}{(c-7)(c-5)(3c-16)D_c(c)},
\]
where \(Q_c(c)=6c^6-366c^5+7630c^4-73129c^3+345210c^2-766635c+656460\). The ascending coefficients of \((1+t)^6Q_c(2t/(1+t))\) are \((656460,2405490,3561390,2734828,1166224,273122,29750)\), all positive; all remaining factors have positive combined sign on \(0<c<2\). Thus clustered fixation strictly dominates alternating fixation throughout the entire admissible interval. The rational witness follows by substituting \(c=1/100\).

## Verification

The accompanying `checker.py` constructs the transition matrix directly from all sixteen action profiles and the stated payoffs, reduces it by edge-color-preserving graph automorphisms, and symbolically verifies the two exact rational formulas. It checks the sharp-threshold sign certificates by polynomial coefficient transformations and the explicit positive-cost rational witness. An independent, unquotiented fourteen-state matrix inversion is also compared at multiple exact positive parameter sets. Run `python checker.py` with Python 3 and SymPy 1.12 or later. The exact symbolic linear-algebra identities and coefficient sign arguments prove the infinite parameter statements; evaluating selected parameter values alone would not.

## Relationship to prior work

Pi, Feng, Deng, Chen and Szolnoki's 2026 variable-game framework motivates heterogeneous edge games, but its reported findings concern time-varying interactions and weak-selection average-game conditions rather than a fixed four-edge two-color exact all-strength comparison. Zhang, Feng, Li, Perc and Szolnoki (2026) treat stochastic transitions among edge games on arbitrary graphs and derive weak-selection criteria; fixing an edge arrangement and extracting these exact finite-selection identities is a different question. Kargaran, Kaveh and Chatterjee (2026) already establish the broader *qualitative* role of spatial clustering and checkerboard arrangements, including higher-order weak-selection effects, for site-specific donor benefits. Their site-based model is not the present symmetric edge-benefit model: a single cooperator's donation to its two neighbors is equal in their model and can differ in this one. Neither the broad observation that arrangement matters nor the general failure of linear weak-selection information is claimed as new. Related finite-state fixation techniques are classical. The assessed contribution is the explicit cost-free all-strength identity for edge coloring and the sharp positive-cost all-interval threshold and strict dominance on the four-cycle.

## Limitations

The exact formula concerns a four-vertex regular graph with precisely two edge qualities and a uniform initial single mutant; it does not generalize without proof to arbitrary graph sizes, mutation, edge rearrangement, or a different updating rule. Linear fitness is assumed and normalized as stated. The cost-free limit is a mathematical benchmark, while the separate strictly positive-cost result supplies an admissible donation-game example. The claim compares cooperation fixation to neutral fixation \(1/4\), not to defector fixation or a full evolutionary equilibrium. The article by Pi and colleagues was accessible only at abstract level during the literature comparison; its unpublished or supplementary finite-size special cases could affect priority. General historical priority requires independent review.

## References

1. B. Pi, M. Feng, L.-J. Deng, X. Chen and A. Szolnoki, *Evolutionary Dynamics of Variable Games in Structured Populations*, arXiv:2603.20603 (first public March 21, 2026), https://arxiv.org/abs/2603.20603.
2. A. Kargaran, K. Kaveh and K. Chatterjee, *Predicting success of cooperators across arbitrary heterogeneous environmental landscapes*, arXiv:2604.12546 (first public April 14, 2026), https://arxiv.org/abs/2604.12546.
3. Y. Zhang, M. Feng, Q. Li, M. Perc and A. Szolnoki, *Effects of stochastic games on evolutionary dynamics in structured populations*, *Communications Physics* **9**, 101 (2026), https://doi.org/10.1038/s42005-026-02536-4; arXiv:2602.07877 (first public February 8, 2026).
4. Y.-T. Chen, A. McAvoy and M. A. Nowak, *Fixation Probabilities for Any Configuration of Two Strategies on Regular Graphs*, *Scientific Reports* **6**, 39181 (2016), https://doi.org/10.1038/srep39181.
5. B. Király and G. Szabó, *Coevolution of strategies and interactions in donation games on a square lattice*, *Physical Review E* **114**, 044302 (October 1, 2026), https://doi.org/10.1103/t3zw-cs6c.
