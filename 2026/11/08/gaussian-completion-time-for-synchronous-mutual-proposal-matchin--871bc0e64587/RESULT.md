# Gaussian completion time for synchronous mutual-proposal matching on complete graphs

## Finding

Run the following synchronous matching rule on the complete graph \(K_n\): at every round, each currently unmatched vertex independently chooses one *different* currently unmatched vertex uniformly; every pair choosing one another is matched and removed. Fresh, independent choices are used in later rounds. Let \(T_n\) be the number of rounds until at most one vertex remains unmatched, and let \(U_n(j)\) be the number unmatched after \(j\) rounds. The resulting matching is maximum because the residual graph is complete.

**Theorem.** As integers \(n\to\infty\), without a restriction on parity,

\[
\mathbb E T_n=n+O(\log n),\qquad
\operatorname{Var}(T_n)=2n+O(\sqrt n\log n),\qquad
\frac{T_n-n}{\sqrt{2n}}\Longrightarrow N(0,1).
\]

The expectation can be stated more precisely as
\[
\mathbb E T_n=n-(n\bmod2)-\mathbb E A_n,
\quad 0\le\mathbb E A_n=O(\log n),
\]
where \(A_n\) is the explicit cumulative finite-population correction defined in the proof. For each fixed \(\varepsilon\in(0,1)\), there is also a functional central limit theorem in \(D([0,1-\varepsilon])\):
\[
\left(\frac{U_n(\lfloor nt\rfloor)-n(1-t)}{\sqrt n}\right)_{0\le t\le1-\varepsilon}
\Longrightarrow (-\sqrt2\,B_t)_{0\le t\le1-\varepsilon},
\]
where \(B\) is standard Brownian motion. In particular a fixed positive fraction of the original vertices requires a linear, rather than logarithmic, number of rounds to become matched in this complete-graph regime.

## Assumptions and scope

All choices are simultaneous, uniform among the other unmatched vertices, independent between vertices conditional on the current residual graph, and freshly generated between rounds. No self-proposals are allowed. The statement covers even and odd \(n\); for odd \(n\), the lone last vertex is left unmatched. A round with no mutual pair leaves the state unchanged. The asymptotic statements concern a single initially complete graph with \(n\to\infty\); they do not assume a sparse random underlying graph, asynchronous updates, or retention of old proposals.

## Proof

**1. Exact one-round moments.** At a round with \(m\ge2\) unmatched vertices let \(C_m\) be the number of unordered mutual-choice pairs, and let \(D_m=2C_m\) be the number removed. Distinct mutual pairs are vertex-disjoint. For any integer \(r\ge0\) with \(2r\le m\), the ordered collections of \(r\) disjoint pairs number \((m)_{2r}/2^r\), and each specific collection occurs with probability \((m-1)^{-2r}\). Hence
\[
\mathbb E(C_m)_r=\frac{(m)_{2r}}{2^r(m-1)^{2r}};
\]
for \(2r>m\) the factorial moment is zero. In particular,
\[
\mu_m:=\mathbb E D_m=\frac{m}{m-1}=1+\frac1{m-1},
\quad
v_m:=\operatorname{Var}(D_m)
=\frac{2m(m-2)^2}{(m-1)^3},
\quad
|v_m-2|\le\frac4{m-1}.
\]
These identities include the boundary \(m=2\), where \(D_2=2\) deterministically. From the first two factorial moments, \(\mathbb E C_m\ge1/2\) and \(\mathbb E C_m^2\le2\), so Paley--Zygmund yields
\[
\Pr(D_m\ge2)=\Pr(C_m>0)\ge\frac{(\mathbb E C_m)^2}{\mathbb E C_m^2}\ge\frac18.
\]
Moreover \(\mathbb E(C_m)_r\le2^r\) for every \(r\). Expanding the exponential in factorial moments gives for each \(\theta>0\)
\[
\sup_{m\ge2}\mathbb E e^{\theta C_m}
\le\exp\bigl(2(e^\theta-1)\bigr).
\]
In particular the centered increments of \(D_m\) have uniformly bounded moments of all orders and uniformly exponentially decaying tails.

**2. Controlling the finite-population drift.** Write \(m_j=U_n(j)\) and \(N_n=2\lfloor n/2\rfloor\). The process terminates almost surely: at each nonterminal state its chance of decreasing in the next round is at least \(1/8\), and there are only \(\lfloor n/2\rfloor\) possible strict decreases. For each possible visited state \(m\) with \(m\equiv n\pmod2\), let \(L_m\) be its number of rounds before the process leaves it, and take \(L_m=0\) if the state is skipped. Because the path is nonincreasing and strictly decreases when it moves, every state can be visited in only one consecutive block. Conditionally on reaching it, \(L_m\) is geometric with success probability at least \(1/8\). Thus
\[
\sup_m\mathbb E L_m\le8,\quad
\sup_m\mathbb E L_m^2\le120,
\quad
\mathbb E T_n\le8\lfloor n/2\rfloor.
\]
Define the correction
\[
A_n:=\sum_{j=0}^{T_n-1}\frac1{m_j-1}
=\sum_{\substack{2\le m\le n\\m\equiv n\pmod{2}}}\frac{L_m}{m-1}.
\]
The sum of the reciprocal weights is \(O(\log n)\); the preceding uniform moment bounds and the triangle inequality in \(L^2\) imply
\[
\mathbb E A_n=O(\log n),
\qquad \mathbb E A_n^2=O((\log n)^2).
\]

**3. An exact stopped-martingale decomposition.** Let \(\mathcal F_j\) be the history through round \(j\), and for \(j\le T_n\) let \(X_j=D_{m_{j-1}}-\mu_{m_{j-1}}\). Define \(M_k=\sum_{j=1}^{k\wedge T_n}X_j\). This is a square-integrable martingale whose predictable quadratic variation is
\[
Q_k=\sum_{j=1}^{k\wedge T_n}v_{m_{j-1}}.
\]
The finite-population variance bound yields the *pathwise* estimate
\[
\big|Q_{T_n}-2T_n\big|\le4A_n.
\]
Since exactly \(N_n\) vertices are removed on termination, summing the conditional means gives the exact identity
\[
N_n=T_n+A_n+M_{T_n}.
\]
The uniform second-moment bound on increments and \(\mathbb E T_n<\infty\) permit square-integrable optional stopping, so \(\mathbb E M_{T_n}=0\) and \(\mathbb E M_{T_n}^2=\mathbb E Q_{T_n}\). It follows that
\[
\mathbb E T_n=N_n-\mathbb E A_n=n+O(\log n),
\quad
\mathbb E M_{T_n}^2=2\mathbb E T_n+O(\mathbb E A_n)
=2n+O(\log n).
\]
The decomposition and Cauchy--Schwarz therefore give
\[
\operatorname{Var}(T_n)
=\operatorname{Var}(M_{T_n}+A_n)
=2n+O(\sqrt n\log n).
\]
They also imply \(\mathbb E|T_n/n-1|\to0\), hence \(T_n/n\to1\) in probability.

**4. Gaussian limit at absorption.** Regard \(M_{k\wedge T_n}\) as a triangular array martingale, observed to deterministic time \(2n\). Its predictable variation satisfies
\[
\frac{Q_{2n}}n=\frac{2(2n\wedge T_n)}n+O_{\mathbb P}(A_n/n)
\xrightarrow{\mathbb P}2.
\]
For every fixed \(\epsilon>0\), its conditional Lindeberg sum, normalized by \(n\), goes to zero: there are at most \(2n\) terms and the exponential-moment estimate in Step 1 is uniform in the current state. The martingale central limit theorem consequently yields
\[
\frac{M_{2n\wedge T_n}}{\sqrt n}\Longrightarrow N(0,2).
\]
Since \(T_n/n\to1\), the probability of \(T_n>2n\) vanishes, so the same limit holds for \(M_{T_n}/\sqrt n\). Finally \(A_n/\sqrt n\to0\) in probability, and \(|N_n-n|\le1\). The exact decomposition gives the asserted centered Gaussian completion-time limit.

For the functional assertion, on \([0,1-\varepsilon]\) the stopping event has vanishing probability, the predictable variation satisfies
\[
\sup_{0\le t\le1-\varepsilon}
\left|\frac{Q_{\lfloor nt\rfloor}}n-2t\right|
\xrightarrow{\mathbb P}0,
\]
and uniform exponential moments give the functional martingale Lindeberg and tightness conditions. The standard functional martingale central limit theorem gives \(M_{\lfloor nt\rfloor}/\sqrt n\Rightarrow\sqrt2 B_t\). Applying \(m_{\lfloor nt\rfloor}=n-\lfloor nt\rfloor-A_{\lfloor nt\rfloor}-M_{\lfloor nt\rfloor}\) and the uniform bound \(A_{\lfloor nt\rfloor}\le A_n=O_{\mathbb P}(\log n)\) completes the proof.

## Verification

The accompanying `scripts/verify.py` runs with Python's standard library and checks exact rational one-round laws by independent exhaustive enumeration of all loop-free proposal mappings for \(2\le m\le7\), as well as exact inclusion--exclusion probability laws and first two absorption-time moment recurrences for \(2\le m\le48\). It also checks the displayed rational moment and variance bounds over an additional finite range. The recorded replay passed 1,838 finite assertions. These tests are finite diagnostics; all infinite-limit conclusions rest on the proof above and the standard martingale central limit theorems.

## Relationship to prior work

The October 18, 2026 preprint of Vishvajeet N and Shrinidhi Teganahally Sridhara studies precisely this mutual-proposal deletion rule, but on Erdős--Rényi graphs with edge density \(\Theta(\log^{1+\epsilon}n/n)\); it proves degree stability and a constant-fraction matching result there, and specifically raises the behavior at other densities and the endgame as questions. The present theorem addresses a distinct, complete-graph regime and gives a full-absorption Gaussian law and exact first-order variance constant, not a new result in that sparse regime.

Métivier, Saheb and Zemmari (2003) analyze the one-round randomized handshake and show that the *number of one-round rendezvous on a complete graph* approaches a Poisson law with mean \(1/2\). That prior limit is credited here: a one-round statement does not by itself establish the cumulative stopping-time law, the necessary uniform state-dependent tail and drift controls, or the full-completion central limit theorem. Earlier work also considers related iterated handshake variants; see the limitations.

## Limitations

The completion-time theorem is restricted to complete residual graphs, fresh independent simultaneous proposals and uniform neighbor selection. It does not describe sparse random graphs or a continuous density crossover. The known one-round Poisson limit is not claimed as new. A 2017 thesis on related randomized-handshake networks was identifiable through citations and its abstract but its relevant full chapter was not accessible for statement-level comparison, so independent historical-priority assessment remains important. The numerical checker cannot certify an infinite functional or stopping-time CLT. Independent scientific audit has not been performed.

## References

1. Vishvajeet N and Shrinidhi Teganahally Sridhara, *Degree Stability of Parallel Greedy Matching in Random Graphs*, arXiv:2610.25507v1, first public 2026-10-18. https://arxiv.org/abs/2610.25507
2. Yves Métivier, Nasser Saheb and Akka Zemmari, *Analysis of a randomized rendezvous algorithm*, *Information and Computation* **184** (2003), 109--128, DOI:10.1016/S0890-5401(03)00054-3. See Section 6.2, Theorem 27. https://www.labri.fr/perso/zemmari/pdf/ic_2003.pdf
3. Nesrine Ouled Abdallah, *Computing models for networks of tiny objects*, doctoral thesis, 2017; related handshake variants cited by Reference 1. https://theses.fr/2017BORD0597
