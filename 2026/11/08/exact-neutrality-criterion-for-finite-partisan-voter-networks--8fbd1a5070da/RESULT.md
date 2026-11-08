# Exact neutrality criterion for finite partisan voter networks

## Finding

**Theorem (sharp topology–preference neutrality and uniqueness of linear conservation).** Let \(G=(V,E)\) be any finite connected, simple, undirected graph with \(|V|\ge2\), \(m=|E|\ge1\), and degrees \(d_i\). Give each vertex a fixed preference \(p_i\in\{-1,+1\}\). Fix \(0<\varepsilon<1\), and let opinions \(\eta_i\in\{0,1\}\) follow the asynchronous partisan-copying dynamics specified below. Put

\[
M(\eta)=\frac{1}{2m}\sum_{i\in V}d_i\eta_i.
\]

Then the following conditions are equivalent:

1. **Universal exact neutrality:** for every initial opinion configuration \(\eta\), the probability of eventual all-\(1\) consensus is exactly \(M(\eta)\), independently of the positive partisan bias \(\varepsilon\).
2. **Perfect cross-preference connectivity:** every edge connects vertices with opposite fixed preferences, \(p_i=-p_j\) whenever \(\{i,j\}\in E\). Thus the graph is bipartite and its preferences are a proper two-colouring.
3. **Linear conservation:** there exists a nonzero weight vector \(w\) such that \(\sum_i w_i\eta_i(t)\) is a martingale for every initial configuration.

Moreover, whenever these conditions hold, **every** linear opinion martingale is a scalar multiple of the degree-weighted mass \(M\). No sign or positivity restriction on the weights \(w\) is needed for this uniqueness.

For arbitrary preferences, an exact correction to the neutral fixation probability is

\[
\Pr_\eta(\text{all-}\!1\text{ consensus})=M(\eta)+\frac{\varepsilon}{2m}\,\mathbb E_\eta\!\int_0^\tau\!\bigl(A_{++}(\eta(t))-A_{--}(\eta(t))\bigr)\,dt,
\]

where \(\tau\) is the first consensus time and \(A_{++}\), respectively \(A_{--}\), counts active edges whose endpoints both prefer opinion \(+1\), respectively \(-1\). This is an exact identity, not a mean-field closure.

In particular, if the graph is the star \(K_{1,r}\) with \(r\ge1\), its centre prefers \(+1\), all leaves prefer \(-1\), and initially each agent holds its own preferred opinion, then the probability of eventual all-\(+1\) consensus is exactly \(1/2\) for every \(r\) and every \(0<\varepsilon<1\). The mean waiting time to the **first** opinion change is \(2/((r+1)(1-\varepsilon))\), which diverges as \(\varepsilon\uparrow1\), although that consensus probability remains fixed.

## Assumptions and scope

Each vertex attempts an update at rate one, independently. An updating vertex \(i\) chooses a uniformly random neighbour \(j\). If their opinions disagree, it adopts the neighbour's opinion with probability

\[
q_i(\eta)=\frac{1-\varepsilon(2\eta_i-1)p_i}{2}.
\]

Otherwise nothing changes. Thus moving toward one's fixed preference has probability \((1+\varepsilon)/2\) and moving away has probability \((1-\varepsilon)/2\). This is the Poissonized, time-rescaled version of the asynchronous microscopic partisan voter rule in Llabrés–San Miguel–Toral (2026), their Eq. (1). The same absorption probabilities hold for the one-vertex-per-discrete-step chain. Unlike the balanced-preference assumption used in that article's macroscopic analysis, the microscopic theorem permits any fixed preference assignment.

The generator for any function \(f\) on opinion configurations is

\[
(\mathcal Lf)(\eta)=\sum_{i\in V}\frac1{d_i}\sum_{j\sim i}\mathbf1_{\{\eta_i\ne\eta_j\}}\frac{1-\varepsilon(2\eta_i-1)p_i}{2}\bigl(f(\eta^{(i)})-f(\eta)\bigr),
\]

where \(\eta^{(i)}\) flips the opinion at vertex \(i\). The only absorbing states for \(0<\varepsilon<1\) are all-zero and all-one consensus. For every other state, a positive-probability finite sequence of permitted copying events leads to consensus. Finiteness of the state space then yields \(\Pr_\eta(\tau<\infty)=1\) and \(\mathbb E_\eta\tau<\infty\).

## Proof

**1. Exact local drift.** On an active edge \(\{i,j\}\), orient the labels temporarily so \(\eta_i=1\), \(\eta_j=0\). The \(i\to0\) transition contributes \(-(1-\varepsilon p_i)/(4m)\) to \(\mathcal LM\); the \(j\to1\) transition contributes \((1+\varepsilon p_j)/(4m)\). Their sum is \(\varepsilon(p_i+p_j)/(4m)\). Adding edges gives

\[
(\mathcal LM)(\eta)=\frac{\varepsilon}{4m}\sum_{\{i,j\}\in E}(p_i+p_j)\mathbf1_{\{\eta_i\ne\eta_j\}}=\frac{\varepsilon}{2m}(A_{++}(\eta)-A_{--}(\eta)).
\]

There is no contribution from cross-preference active edges, for every configuration, even when partisan bias is strong.

**2. Stopping and occupation formula.** For the bounded function \(M\), Dynkin's formula up to \(t\wedge\tau\) gives

\[
\mathbb E_\eta M(\eta(t\wedge\tau))-M(\eta)=\mathbb E_\eta\int_0^{t\wedge\tau}(\mathcal LM)(\eta(s))\,ds.
\]

The integrand is bounded, and the mean absorption time is finite, so dominated convergence allows \(t\to\infty\). At absorption \(M\) is zero or one according as consensus is all-zero or all-one. This proves the displayed exact correction identity. In particular, condition 2 implies \(\mathcal LM\equiv0\), hence condition 1.

**3. Neutrality forces proper preference colouring.** Write \(H(\eta)=\Pr_\eta(\text{all-}\!1\text{ consensus})\). The Markov property and finite absorption show \(\mathcal LH=0\) at each transient configuration. If condition 1 holds, then \(H=M\), so \(\mathcal LM=0\) everywhere. Take the configuration with only vertex \(i\) carrying opinion one. Its active edges are exactly those incident to \(i\). Thus

\[
0=\frac{4m}{\varepsilon}(\mathcal LM)(\eta)=\sum_{j\sim i}(p_i+p_j).
\]

Every summand is either zero or has the same nonzero sign as \(p_i\), since \(p_i,p_j\in\{-1,+1\}\). Consequently every summand vanishes, so \(p_j=-p_i\) for every neighbour \(j\). This holds at every vertex. Hence condition 1 implies condition 2.

**4. No other linear martingale exists.** Suppose \(F_w(\eta)=\sum_i w_i\eta_i\) satisfies \(\mathcal LF_w=0\) for all \(\eta\), for some nonzero real vector \(w\). Test first the configuration with exactly one \(1\) at \(i\), then the complementary configuration with exactly one \(0\) at \(i\). Direct use of the flip rates gives, respectively,

\[
w_i(1-\varepsilon p_i)=\sum_{j\sim i}\frac{w_j}{d_j}(1+\varepsilon p_j),\qquad
w_i(1+\varepsilon p_i)=\sum_{j\sim i}\frac{w_j}{d_j}(1-\varepsilon p_j).
\]

Adding yields \(w_i=\sum_{j\sim i}w_j/d_j\). The matrix of this linear system is the transpose of the simple random-walk transition matrix on the connected graph. Its eigenvalue-one right eigenspace is one-dimensional, spanned by the strictly positive degree vector. Thus \(w_i=c d_i\) for a nonzero constant \(c\). Subtracting the two displayed equations and dividing by \(c\varepsilon\) yields

\[
d_i p_i+\sum_{j\sim i}p_j=0.
\]

Since every summand \(p_i+p_j\) is zero or has sign \(p_i\), this again forces \(p_i=-p_j\) along every edge. Thus condition 3 implies condition 2, and every nonzero linear martingale must be a multiple of \(M\). Conversely condition 2 makes \(M\) a martingale, proving condition 3. This completes all equivalences and the uniqueness statement.

**5. Star consequence and timescale separation.** On \(K_{1,r}\) the hub degree is \(r\), the combined leaf degree is \(r\), and \(2m=2r\). The hub-only positive initial state therefore has \(M=1/2\). Its preferences alternate across every edge; condition 1 gives the exact fixation probability \(1/2\), despite only one of \(r+1\) agents initially holding opinion \(+1\). Initially every opinion is preference-aligned, so each of the \(r+1\) vertex clocks causes an opinion change with probability \((1-\varepsilon)/2\) per attempt; the total change rate is \((r+1)(1-\varepsilon)/2\). Its reciprocal is the claimed first-change mean. The consensus time dominates that first-change time. For balanced preference populations, the analogous bipartite example \(K_{r,r}\) with the two parts oppositely preferring opinions and initially holding those opinions also has all-plus fixation probability \(1/2\).

## Verification

Run the accompanying self-contained Python 3 program `check.py` (standard library only). It reconstructs all directed state-change rates and checks the exact drift algebra for 3,360 state/parameter instances on six connected graphs, the if-and-only-if criterion for 168 combinations of preference assignment and bias, and rational absorbing-chain fixation probabilities for 20 properly coloured cases. Its additional controls calculate a non-neutral triangle fixation of \(9/13\) versus the neutral prediction \(1/3\), and the star's exact half fixation.

These finite checks support and stress-test the symbolic arguments; they are **not** treated as an exhaustive proof for graphs of arbitrary order. The all-graph theorem follows from the generator identity, finite-state absorption and the one-eigenspace argument above.

## Relationship to prior work

The microscopic partisan update rule and decomposition of active edges by preference are in Llabrés, San Miguel and Toral (2026), especially Eqs. (1), (3), (4), (17), and their pair-approximation Eq. (20a). In particular, the fact that two same-preference active-link densities affect a macroscopic drift is **already present there** and is not claimed as new. That work studies local ordering through approximate macroscopic equations and network simulations; it does not give the finite-graph universal fixation if-and-only-if, the uniqueness classification of all linear martingales, or the exact neutral-bias timescale separation.

The conventional degree-weighted conserved quantity for the **unbiased** voter model is classical (Suchecki–Eguíluz–San Miguel, 2004; Sood–Antal–Redner, 2008). Masuda–Gibert–Redner (2010), Masuda–Redner (2011), and Llabrés–San Miguel–Toral (2023) study preference-biased voter dynamics, chiefly at mean-field or complete-graph scale. The result here isolates the restrictive network/preference alignment under which exact finite-population neutrality survives **nonzero bias**.

## Limitations

The graph must be finite, simple, connected and undirected; preferences must be fixed binary signs, and the same strict bias parameter is used at all sites. For \(\varepsilon=0\) all preference assignments trivially have neutral fixation, invalidating the converse; for \(\varepsilon=1\) non-consensus frozen preference-aligned configurations can occur and the finite-time consensus argument fails. No conclusion is asserted for directed, weighted, noisy, adaptive or multi-opinion networks, or for consensus times beyond the specified star first-change lower bound. The statement is an exact theorem for the specified stochastic process, not a behavioural prediction.

The underlying local edge-type drift is close to formulas in the 2026 source; the claimed distinction is the exact global **equivalence and uniqueness** result. Equivalent statements elsewhere in the broad generalized-voter literature may have escaped the literature comparison. No independent scientific audit has been conducted.

## References

1. J. Llabrés, M. San Miguel, R. Toral. *Partisan voter model on complex networks: Dynamics of local ordering*. arXiv:2606.05062, first version June 3, 2026. https://arxiv.org/abs/2606.05062
2. J. Llabrés, M. San Miguel, R. Toral. *Partisan voter model: Stochastic description and noise-induced transitions*. Physical Review E 108, 054106 (2023); arXiv:2301.09563. https://arxiv.org/abs/2301.09563
3. N. Masuda, N. Gibert, S. Redner. *Heterogeneous voter models*. Physical Review E 82, 010103 (2010). https://doi.org/10.1103/PhysRevE.82.010103
4. N. Masuda, S. Redner. *Can partisan voting lead to truth?* Journal of Statistical Mechanics L02002 (2011); arXiv:1012.2462. https://sites.santafe.edu/~redner/pubs/pdf/truth.pdf
5. K. Suchecki, V. M. Eguíluz, M. San Miguel. *Conservation laws for the voter model in complex networks*. Europhysics Letters 69, 228 (2005); arXiv:cond-mat/0408101. https://arxiv.org/abs/cond-mat/0408101
6. V. Sood, T. Antal, S. Redner. *Voter models on heterogeneous networks*. Physical Review E 77, 041121 (2008). https://doi.org/10.1103/PhysRevE.77.041121
