# Minority-parity exponents for collective encounters under weak independent holds

## Finding

A group of walkers on a bipartite network can have an absolute synchrony barrier: if their resetting sites lie in both bipartition classes, simultaneous non-lazy motion and simultaneous resetting cannot bring all walkers to one vertex. A small independently applied holding probability \(\varepsilon\) removes this obstruction, but the search delay has an exact, graph-independent power. If \(m\) of \(S\) resetting sites lie in one class and the remainder in the other, define
\[
k=\min\{m,S-m\}.
\]
For every fixed connected finite undirected bipartite network and every common target vertex \(j\), the first collective arrival time \(T_\varepsilon\) obeys
\[
\mathbb E T_\varepsilon\sim\frac{1}{\gamma a_j}\varepsilon^{-k},\qquad
\gamma a_j\varepsilon^kT_\varepsilon\Longrightarrow\operatorname{Exp}(1),
\]
with a strictly positive coefficient \(a_j\) obtained from a finite discounted hitting resolvent. Thus the power counts the smallest number of walkers whose initial bipartite phases must be repaired; the graph topology determines the prefactor, but not the power.

For two searchers reset to the hub and a leaf of a star with any number of leaves, the target-hub mean has the exact leaf-count-independent form
\[
M(\varepsilon,\gamma)=
\frac{1+(1-\gamma)\varepsilon(1-2\varepsilon)}
{\varepsilon(1-\varepsilon)(1-\gamma)[2-\gamma-2(1-\gamma)\varepsilon]}.
\]
It has a unique optimal holding probability in the strict interval \((0,1)\). Both too little and too much asynchrony prevent efficient encounters.

## Assumptions and scope

Let \(G=(V,E)\) be any finite connected loopless undirected bipartite graph, with bipartition \(V=V_0\sqcup V_1\), and at least one edge. The simple random walk transition matrix \(P\) is row-stochastic, with \(P(u,v)=1/\deg(u)\) for adjacent vertices and zero otherwise. For an integer \(S\ge2\), fix reset configuration \(r=(r_1,\dots,r_S)\in V^S\), with \(m\) coordinates in \(V_0\) and \(S-m\) in \(V_1\), where \(1\le m<S\). Fix a target \(j\in V\), and call \(d=(j,\ldots,j)\) the diagonal target.

At each positive integer time step a fresh Bernoulli choice resets all walkers simultaneously to \(r\) with probability \(\gamma\in(0,1)\). Otherwise all walkers update independently using \(P_\varepsilon=(1-\varepsilon)P+\varepsilon I\), with \(0<\varepsilon<1\). All choices and successive steps are independent. Starting from \(r\), let \(T_\varepsilon=\inf\{t\ge1:X_t=d\}\). A reset takes one time step and does not constitute arrival (since \(r\ne d\)). Here the graph and all other parameters remain fixed while \(\varepsilon\downarrow0\); no simultaneous graph-size or particle-number limit is asserted.

## Proof

**1. Exact discounted single-cycle probability.** Suppress resets temporarily and let \(H_\varepsilon\) be the first positive time when the product transition kernel \(F_\varepsilon=P_\varepsilon^{\otimes S}\) reaches \(d\), starting from \(r\). Since \(0<\varepsilon<1\), this finite product walk is irreducible and aperiodic, so \(H_\varepsilon<\infty\) almost surely. Write \(q=1-\gamma\) and \(\Omega=V^S\setminus\{d\}\). Let \(Q_\varepsilon=F_\varepsilon|_{\Omega\times\Omega}\), and \(b_\varepsilon=(F_\varepsilon(x,d))_{x\in\Omega}\). Then
\[
p_\varepsilon:=\Pr(H_\varepsilon<R)=\mathbb E[q^{H_\varepsilon}]
=q\,e_r^\top(I-qQ_\varepsilon)^{-1}b_\varepsilon,
\]
where \(R\) is an independent geometric reset-step time with \(\Pr(R=n)=\gamma q^{n-1}\), \(n\ge1\). The inverse exists because \(\|qQ_\varepsilon\|_\infty\le q<1\). It is a rational function of \(\varepsilon\), analytic in a neighborhood of zero; all coefficients and its first nonzero Taylor coefficient are reproducible from these explicitly defined finite matrices.

**2. The sharp minority exponent.** Encode the bipartition of the initial location of walker \(s\) by \(c_s\in\{0,1\}\). After \(n\) nonreset steps in which that walker held exactly \(h_s\) times, its bipartite color is \(c_s+n-h_s\pmod2\). If every walker has reached one vertex, then all \(c_s-h_s\pmod2\) agree. Therefore either every initially class-zero walker or every initially class-one walker has experienced an odd number of holds. Every successful path contains at least \(k=\min(m,S-m)\) individual holding events. For any \(n\), the chance of at least \(k\) holds among \(nS\) independent decisions is at most \(\binom{nS}{k}\varepsilon^k\). Summing the discounted first-arrival probabilities gives
\[
p_\varepsilon\le \sum_{n\ge1}q^n\binom{nS}{k}\varepsilon^k=O(\varepsilon^k).
\]
Conversely, hold exactly once for each walker in a minority initial color class and never hold the others. Choose a sufficiently large common path length \(n\), with parity making every walker end in the bipartition class of \(j\). Connectivity, backtracking, and finite bipartite periodicity ensure that, for each walker, a positive-probability walk of the required length \(n-h_s\) from its reset site to \(j\) exists. The prescribed event has probability at least \(c\varepsilon^k(1-\varepsilon)^{nS-k}\) for some \(c>0\), so \(p_\varepsilon\ge q^n c\varepsilon^k(1-\varepsilon)^{nS-k}\). Analyticity and the upper and lower bounds imply
\[
p_\varepsilon=a_j\varepsilon^k+O(\varepsilon^{k+1}),\quad
0<a_j=\frac{1}{k!}\left.\frac{d^kp_\varepsilon}{d\varepsilon^k}\right|_{\varepsilon=0}<\infty.
\]
This is the exact finite-resolvent coefficient in the statement. No unproved combinatorial enumeration is invoked for the leading exponent.

**3. First moment and complete rare-encounter law.** Between successive global reset steps, the cycles are independent. A cycle is successful precisely when \(H_\varepsilon<R\), with success probability \(p_\varepsilon\), and has length \(L_\varepsilon=\min(H_\varepsilon,R)\). The renewal equation gives
\[
\mathbb ET_\varepsilon=\frac{\mathbb EL_\varepsilon}{p_\varepsilon}
=\frac{1-p_\varepsilon}{\gamma p_\varepsilon}.
\]
The last equality follows by summing \(\sum_{n\ge0}\Pr(H_\varepsilon>n)q^n\). Hence the asserted mean asymptotic follows.

For completeness, let \(u=s\gamma p_\varepsilon\) with fixed \(s\ge0\), and set \(A_\varepsilon(u)=\mathbb E[e^{-uL_\varepsilon};H_\varepsilon<R]\) and \(B_\varepsilon(u)=\mathbb E[e^{-uL_\varepsilon};R\le H_\varepsilon]\). Summing independent failed cycles yields
\[
\mathbb E[e^{-uT_\varepsilon}]=\frac{A_\varepsilon(u)}{1-B_\varepsilon(u)}.
\]
Since \(L_\varepsilon\le R\), the geometric law provides a uniform second moment. Moreover \(p_\varepsilon\to0\) and \(\mathbb E[L_\varepsilon;H_\varepsilon<R]\to0\) by uniform integrability. Thus \(A_\varepsilon(u)=p_\varepsilon+o(p_\varepsilon)\), while \(1-B_\varepsilon(u)=p_\varepsilon+u/\gamma+o(p_\varepsilon)\). The Laplace transforms converge to \((1+s)^{-1}\), proving \(\gamma a_j\varepsilon^kT_\varepsilon\Longrightarrow\operatorname{Exp}(1)\).

**4. Exact star specialization and uniqueness of the optimum.** Let \(G=K_{1,L}\), \(L\ge1\), with hub \(h\), reset positions \((h,\ell)\) for any leaf \(\ell\), and target \((h,h)\). The hub/leaf status of each walker is a four-state chain, independent of \(L\): moving interchanges hub and leaf, while holding preserves status. Declare \((h,h)\) absorbing. The remaining statuses \((h,\ell)\), \((\ell,h)\), \((\ell,\ell)\) form a closed first-passage system after adding reset transitions to \((h,\ell)\). Solving its three linear mean-time equations gives exactly
\[
M(\varepsilon,\gamma)=\frac{1+(1-\gamma)\varepsilon(1-2\varepsilon)}{\varepsilon(1-\varepsilon)(1-\gamma)[2-\gamma-2(1-\gamma)\varepsilon]}.
\]
In particular \(M\sim[(1-\gamma)(2-\gamma)\varepsilon]^{-1}\) as \(\varepsilon\downarrow0\), and \(M\sim[(1-\gamma)(1-\varepsilon)]^{-1}\) as \(\varepsilon\uparrow1\).

For uniqueness, put \(q=1-\gamma\in(0,1)\) and \(t=\varepsilon/(1-\varepsilon)>0\). The same mean becomes
\[
M=\frac{(1+t)[(1-q)t^2+(2+q)t+1]}{qt[(1-q)t+1+q]}.
\]
Its derivative has the sign of
\[
D_q(t)=(1-q)^2t^4+2(1-q^2)t^3+q(q+5)t^2-2(1-q)t-(1+q).
\]
The coefficients in descending powers exhibit exactly one sign change for every \(q\in(0,1)\). Descartes' rule gives at most one positive real root, while \(D_q(0)<0\) and \(D_q(t)\to+\infty\) give at least one. Therefore the mean decreases and then increases exactly once, and its unique stationary point is its global optimum. The exact optimizer is \(\varepsilon_*=t_*/(1+t_*)\), where \(t_*\) is that positive root. The result is invariant under the number of leaves, including the two-vertex star.

## Verification

Run `python check_phase_barrier.py` with Python 3.10 or newer, NumPy and SymPy. The script symbolically reconstructs the three-state first-passage system and its exact rational mean, checks the derivative polynomial and the leading coefficient, and compares the formulas with independent full transition-matrix inversions on stars having one, two and five leaves. It also checks the finite discounted resolvent and the exact restart identity for additional bipartite graphs, including paths and even cycles, and tests the predicted powers for two, three and four walkers. At package preparation it passed 179 deterministic assertions. Numerical finite-parameter checks do not prove the infinite small-holding limit; Sections 2 and 3 give the analytic argument.

## Relationship to prior work

Suarez-Jimenez, Riascos and Boyer (arXiv:2604.20770, first submitted April 22, 2026) derive spectral mean first-encounter expressions for synchronous multiwalker resetting, and contrast simultaneous and independent resetting. Their expressions are prior art for the general collective Markov-chain and first-passage framework. The statement here is the graph-independent order of the singular weak-holding limit, its explicit minority-color combinatorics, the resulting full rare-encounter distribution, and the star-graph exact optimizer. Rubio-Gómez, Riascos and Mateos (arXiv:2508.05313) derive spectral encounter formulas with one or two resetting walkers and explicitly discuss bipartite periodicity, but do not present this independently lazy, globally resetting, arbitrary-number-of-walkers asymptotic theorem. General metastable finite-chain theory, including Betz and Le Roux, supplies broad escape-time machinery; it is not claimed that perturbation of a finite Markov chain or exponential rare-event waiting by itself is new. The substantive specialized classification here is the power \(k\), its domain-uniform sharpness across every connected bipartite graph, and the exact star optimum.

## Limitations

The theorem concerns fixed finite connected loopless bipartite graphs, globally synchronized resets of fixed positive probability, independent per-walker holds, and one prescribed simultaneous target. It does not cover graph-size limits, non-bipartite graphs, continuous-time motion, interactions, heterogeneous holding probabilities, or vanishing reset probability jointly with holding probability. The coefficient \(a_j\) is given algorithmically by a finite resolvent derivative rather than a closed expression for arbitrary graphs. The star simplification requires a hub target and opposite-side resetting sites. General rare-event and metastability results can imply the renewal and exponential-law portions; publication priority for a broader theorem may remain unresolved. No independent external validation is claimed.

## References

1. C. D. Suarez-Jimenez, A. P. Riascos and D. Boyer, *Encounter times of random walkers with simultaneous resetting on networks*, arXiv:2604.20770v1 (first public April 22, 2026); https://arxiv.org/html/2604.20770v2 .
2. D. Rubio-Gómez, A. P. Riascos and J. L. Mateos, *Mean first-encounter times of simultaneous random walkers with resetting on networks*, arXiv:2508.05313v1 (August 7, 2025); https://arxiv.org/html/2508.05313v1 .
3. V. Betz and S. Le Roux, *Multi-scale metastable dynamics and the asymptotic stationary distribution of perturbed Markov chains*, Stochastic Processes and their Applications 126 (2016), 3499–3526; https://doi.org/10.1016/j.spa.2016.05.003 .
4. D. Silvestrov, *Perturbed Semi-Markov Type Processes I: Limit Theorems for Rare-Event Times and Processes*, Springer (2022), https://doi.org/10.1007/978-3-030-92403-4 (overview consulted; full text not inspected).
