# A sharp six-vertex cutoff for transient environmental-variance ordering on trees

## Finding

In the finite edge-environment evolutionary game defined below, let \(G\) be a simple tree with \(N\ge4\) vertices. Begin with every agent playing the same strategy and every edge in the same environmental state \(h\in\{0,1\}\). Let \(S_G(t)\) be the number of rich (state-one) edges after \(t\) complete update attempts. At all positive integer times, its expectation depends only on \(N\), but its variance depends on the topology **exactly** through the count of adjacent edge pairs
\[
W(G)=\sum_{v\in V(G)}\binom{\deg(v)}2.
\]

For the path \(P_N\) and the star \(K_{1,N-1}\), with identical model parameters and initial conditions, the exact difference is
\[
\operatorname{Var} S_{K_{1,N-1}}(t)-\operatorname{Var} S_{P_N}(t)
=(N-2)(N-3)(h-\pi)^2\bigl(b_1^t-b_0^t\bigr),
\]
where \(s=p+q\), \(\pi=p/s\), \(b_0=1-4\omega s/N\), and \(b_1=b_0+\omega s^2/N\). This difference is always positive at odd \(t\), and for even \(t\) its sign is precisely the sign of \(2N-\omega s(8-s)\). Consequently **six vertices are the sharp minimum network size** above which the star always has strictly greater transient rich-edge-count variance than the path for every admissible update rate and every positive time, and indeed maximizes variance among all trees while the path minimizes it.

At \(N=5\), both directions occur at successive times for the same admissible parameters: an explicit example has star-minus-path variance \(4617/5000>0\) at \(t=1\) but \(-1389717/12500000<0\) at \(t=2\). This is a transient finite-network statement; the eventual edge-environment distribution is independent Bernoulli with common rich probability \(\pi\).

## Assumptions and scope

Use the binary edge-environment game of Betz, Fu and Masuda (2026), on an arbitrary finite, simple, undirected graph. At each discrete update attempt: with probability \(1-\omega\), one Fermi strategy-imitation event occurs; with probability \(\omega\in(0,1)\), a uniformly selected vertex causes **all its incident edges to update independently**, with environmental transitions \(0\to1\) having probability \(p_j\in(0,1)\) and \(1\to0\) having probability \(q_j\in(0,1)\). The type \(j=0,1,2\) specifies cooperator–cooperator, mixed, or defector–defector edges, respectively. The source assumes \(p_0>p_1>p_2\) and \(q_0<q_1<q_2\); these inequalities are respected in the rational example. Strategies all begin as cooperators or all as defectors, and consequently remain unchanged under imitation. Set \((p,q)=(p_0,q_0)\) in the first case or \((p_2,q_2)\) in the second. No assumption is needed on Fermi selection intensity beyond the source's domain.

Write \(M=|E(G)|\), \(s=p+q\in(0,2)\), \(\pi=p/s\in(0,1)\), \(z=h-\pi\ne0\), and
\[
a=1-\frac{2\omega s}{N},\qquad
b_0=1-\frac{4\omega s}{N},\qquad
b_1=1-\frac{4\omega s}{N}+\frac{\omega s^2}{N},\qquad
\mu_t=\pi+za^t.
\]
The following exact result holds for any finite simple graph; the tree comparison follows by specializing \(M=N-1\):
\[
\mathbb E S_G(t)=M\mu_t,
\]
\[
\begin{split}
\operatorname{Var} S_G(t)
={}&M\mu_t(1-\mu_t)\\
&+2z^2 W(G)(b_1^t-a^{2t})\\
&+2z^2\left(\binom M2-W(G)\right)(b_0^t-a^{2t}).
\end{split}
\]
All powers here are ordinary integer powers. No continuous-time rescaling is being made.

## Proof

**Step 1: Exact one-edge moment.** Write \(Y_e(t)\in\{0,1\}\) for the state of edge \(e\) and \(Z_e(t)=Y_e(t)-\pi\). For a single environmental update applied to \(e\), direct conditioning on its current binary state gives
\[
\mathbb E[Z_e(t+1)\mid Y_e(t),\ e\text{ updated}]=(1-s)Z_e(t).
\]
No update leaves \(Z_e\) unchanged. An environmental event selects either endpoint of a particular edge with total probability \(2\omega/N\); thus \(\mathbb E[Z_e(t+1)\mid\mathbf Y(t)]=aZ_e(t)\). Since every edge starts at \(h\), \(\mathbb E Y_e(t)=\pi+za^t=\mu_t\).

**Step 2: Exact two-edge moment without a closure assumption.** Let \(e\ne f\), and set \(r=|e\cap f|\), which is either zero or one on a simple graph. Conditional on the uniformly selected environmental-update vertex and the current edge states, the coin flips of the distinct edges are independent by the model definition. Therefore the conditional expectation of \(Z_e(t+1)Z_f(t+1)\) is its old product times the product of the two edge-specific factors (either \(1\) or \(1-s\)). Averaging over the environmental versus imitation event and over the selected vertex gives
\[
\mathbb E[Z_e(t+1)Z_f(t+1)\mid\mathbf Y(t)]
=\left(1-\frac{4\omega s}{N}+\frac{r\omega s^2}{N}\right)Z_e(t)Z_f(t).
\]
Iterating from \(Z_e(0)Z_f(0)=z^2\) yields \(\mathbb E[Z_e(t)Z_f(t)]=z^2b_r^t\). Accordingly
\[
\operatorname{Cov}(Y_e(t),Y_f(t))=z^2\bigl(b_r^t-a^{2t}\bigr).
\]
The binary single-edge variance is \(\mu_t(1-\mu_t)\). Summing all one-edge variances and all distinct-pair covariances proves the exact displayed formula, since \(W(G)\) counts exactly the pairs of different edges sharing a vertex.

**Step 3: Sharp tree extrema.** In every tree on \(N\) vertices, \(M=N-1\) and \(\sum_v\deg(v)=2N-2\). Since \(\binom d2\ge d-1\) for positive integer \(d\), with equality exactly when \(d\le2\), one has \(W(G)\ge N-2\), with equality exactly for the path. Also \(W(G)\le\binom{N-1}2\), with equality exactly when every edge pair shares a vertex; for trees with \(N\ge4\) this is exactly the star. The difference of these sharp counts is \((N-2)(N-3)/2\). The variance formula is affine in \(W(G)\), of slope \(2z^2(b_1^t-b_0^t)\), so the claimed tree ordering and exact star-minus-path difference follow.

**Step 4: Parity and sharp size.** Because \(b_1-b_0=\omega s^2/N>0\), odd integer powers preserve strict order. For positive even integer \(t\), the sign of \(b_1^t-b_0^t\) is that of \(b_1+b_0\), namely
\[
b_1+b_0=\frac{2N-\omega s(8-s)}{N}.
\]
For \(0<s<2\) and \(0<\omega<1\), one has \(\omega s(8-s)<12\). Hence when \(N\ge6\), the sign is strictly positive for every integer \(t\ge1\). For \(N=4\) or \(5\), both signs are attainable for even \(t\), as demonstrated next. Equality in the even-time comparison, if attainable, makes every tree's variance equal at that time. These statements are exhaustive.

**Step 5: Admissible rational sharpness witness.** Let every agent initially cooperate and every edge initially be depleted, take \(N=5\), and choose
\[
(p_0,p_1,p_2)=(9/10,4/5,7/10),\qquad
(q_0,q_1,q_2)=(9/10,19/20,99/100),\qquad \omega=19/20.
\]
The source's monotonic feedback constraints are satisfied. For definiteness, payoff matrices \(A_0=\bigl(\begin{smallmatrix}2&2\\1&1\end{smallmatrix}\bigr)\) and \(A_1=\bigl(\begin{smallmatrix}0&0\\1&1\end{smallmatrix}\bigr)\) satisfy its opposite-Nash-environment constraints, and any admissible Fermi selection strength is allowed because unanimous strategies cannot change. The active rates are \(p=q=9/10\), giving \(s=9/5\), \(\pi=1/2\), \(a=79/250\), \(b_0=-46/125\), and \(b_1=619/2500\). Substituting in the exact difference yields \(4617/5000\) at \(t=1\) and \(-1389717/12500000\) at \(t=2\). Thus \(N=5\) is a counterexample to universal star-maximal variance, proving six is the sharp cutoff.

## Verification

The self-contained Python 3.10+ checker `checks/edge_environment_checker.py` builds the **full** discrete-time transition matrix implicitly, using exact rational probabilities for every binary edge-state configuration. It does **not** use the moment recurrence to generate transitions. It checks the resulting exact first two moments against the formulas at times zero through three on paths and stars with four, five, and six vertices, for both homogeneous initial environmental states; a nonextremal five-vertex tree and a four-cycle are checked, and additional rational-parameter paths from three through six vertices are also checked. All specified assertions passed. Run `python3 checks/edge_environment_checker.py` from the directory containing this report. The displayed rational numbers arise from the theorem and are also independently reproduced by state enumeration. Finite checks are supplementary only: the proof for arbitrary graphs, parameters and all positive integer times is analytical.

## Relationship to prior work

Betz, Fu and Masuda (2026) define this edge-dependent environment-switching game and analyze mean-field and pair-approximation dynamics and simulations. Their pair approximation explicitly treats edges at the same node as conditionally independent (their equation (78)); their boundary equilibrium analysis gives equilibrium rich/depleted frequencies, but no exact finite-time covariance or total-rich-edge variance formula, and no path/star fluctuation ordering. The new comparison explicitly uses the finite asynchronous common-vertex update that the pair closure suppresses. Clementi and coauthors' edge-Markovian evolving graphs give a different process in which each edge evolves independently rather than through shared vertex activation; generic random-scan/block-update theory provides mathematical context but the stated graph-invariant exact variance, parity reversal and sharp six-vertex cutoff were not located in the inspected and searched sources. This is a bounded literature comparison, not proof of absolute historical priority.

## Limitations

The result is conditional on already unanimous strategies and a homogeneous initial environmental state. It does not classify fixation probabilities, the coexistence dynamics of mixed strategies, nor environmental covariance along an active strategic evolution. It treats simple undirected graphs, one vertex selected uniformly in each environmental-update event and conditionally independent edge-update coin flips. Changing any of these mechanisms changes the factors. The surprising parity reversal requires relatively high two-direction switching rates and environmental-update frequency; typical low-rate regimes remain star-maximal. Infinite-time variance is topology-independent because correlations decay. Independent scientific audit has not been performed; historical-priority comparisons may miss an unindexed general block-Markov-chain formula that subsumes these specializations.

## References

1. K. Betz, F. Fu, N. Masuda, *Evolutionary games on networks with negative edge-based environmental feedback*, arXiv:2611.11029, initial posting 2026-11-08, https://arxiv.org/abs/2611.11029 . Model, environmental update rule, pair closure, and boundary analysis.
2. A. Clementi, C. Macci, A. Monti, F. Pasquale, R. Silvestri, *Flooding Time of Edge-Markovian Evolving Graphs*, SIAM Journal on Discrete Mathematics, https://doi.org/10.1137/090756053 . Distinct independent-edge evolution model.
3. Y. Kwon, *Cost Comparisons for Random and Deterministic Scans in Component-Wise Markov Chains*, arXiv:2610.01121, initial posting 2026-10-01, https://arxiv.org/abs/2610.01121 . General random-scan context; no claimed equivalence.
4. American Mathematical Society, MSC2020, 91A22, *Evolutionary games*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=91-10 .
