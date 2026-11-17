# Universal strict suppression by regular higher-order hypergraphs under full-group birth–death updating

## Finding

**Theorem (all-size, all-fitness, all-initial-state suppression).** Let \(H=(V,E)\) be a finite, connected, undirected hypergraph on \(N\ge3\) labeled vertices, with every hyperedge containing at least three distinct vertices. Suppose every vertex is incident with exactly \(d\ge1\) hyperedges. Hyperedges need not all have the same size. Give mutants fitness \(r>0\) and residents fitness \(1\). At each discrete time step choose one parent with probability proportional to its fitness, choose one of its \(d\) incident hyperedges uniformly, and convert *every* vertex in that hyperedge to the parent's type (including the parent, which does not change).

For every initial mutant set \(S\) with \(1\le i=|S|\le N-1\), fixation of one of the two types occurs almost surely. Let \(\rho_H(S;r)\) be the probability of eventual all-mutant fixation. Then

\[
\boxed{\begin{aligned}
\rho_H(S;r)&<\frac{1-r^{-i}}{1-r^{-N}} &&\text{if }r>1,\\
\rho_H(S;1)&=\frac{i}{N},\\
\rho_H(S;r)&>\frac{1-r^{-i}}{1-r^{-N}} &&\text{if }0<r<1.
\end{aligned}}
\]

The comparison is pointwise in the initial configuration, not merely an average over uniformly placed single mutants. In particular every connected regular uniform hypergraph of hyperedge size at least three strictly suppresses selection for every nonneutral fitness. For a connected regular *pairwise* graph, the inequalities become exact equalities, displaying the group-size boundary.

## Assumptions and scope

A hypergraph is **connected** if every nonempty proper vertex set is crossed by at least one hyperedge. All hyperedges are distinct subsets of \(V\), no hyperedge is empty, and every vertex has the same *incidence degree* \(d\), not merely the same projected-graph degree. No symmetry, transitivity, fixed edge size, or random placement of initial mutants is assumed. The result concerns the complete-group overwrite process designated *Model 1* in Liu and Masuda [1], not their majority-conditioned Model 2 or a death–birth focal-imitation model.

For comparison, the classical Moran probability from \(i\) mutants in an \(N\)-person population is \(M_{N,i}(r)=(1-r^{-i})/(1-r^{-N})\) for \(r\ne1\) and \(i/N\) at neutrality. The theorem is a bound on fixation probability, not a closed form for \(\rho_H\), nor a fixation-time or game-payoff claim.

## Proof

**1. One-step identity.** At a state with mutant set \(S\), put \(i=|S|\) and \(Z=ri+N-i\). For each hyperedge \(e\), let \(a_e=|e\cap S|\) and \(b_e=|e\setminus S|\). Every mutant parent within \(e\) causes the mutant count to jump by \(b_e\) if that edge is selected; the sum of their selection weights for this event is \(ra_e/(dZ)\). Every resident parent within \(e\) causes a jump by \(-a_e\), with total weight \(b_e/(dZ)\). Summing all parent-edge events is legitimate even when distinct events lead to the same next state.

For \(I_t\), the mutant count at time \(t\), define \(Y_t=r^{-I_t}\). At any state \(S_t=S\), the exact conditional drift is

\[
\mathbb E[Y_{t+1}-Y_t\mid S_t=S]
=\frac{r^{-i}}{dZ}\sum_{e\in E}G_{a_e,b_e}(r),
\qquad
G_{a,b}(r):=ra(r^{-b}-1)+b(r^a-1).
\tag{1}
\]

A monochromatic hyperedge has \(G_{a,0}=G_{0,b}=0\). If \(a,b\ge1\), then

\[
G_{a,b}(1)=G'_{a,b}(1)=0,
\qquad
G''_{a,b}(r)=ab\bigl((b-1)r^{-b-1}+(a-1)r^{a-2}\bigr).
\tag{2}
\]

For \(a+b\ge3\), at least one of \(a-1\) or \(b-1\) is positive, so \(G''_{a,b}(r)>0\) at every \(r>0\). Hence \(G_{a,b}(r)>0\) for all \(r>0\), \(r\ne1\). When \(a=b=1\), \(G_{1,1}\equiv0\).

Because the hypergraph is connected, every mixed state has at least one crossing hyperedge, and because every edge has size at least three, equation (1) is **strictly positive** for every mixed state at \(r\ne1\). At absorbing states it is zero. Thus \((Y_t)\) is a bounded submartingale, with strict expected increase from each mixed state.

**2. Absorption.** From any mixed state choose a hyperedge crossing the mutant–resident cut and choose one of its mutant vertices as parent. This event has positive probability and strictly increases the mutant set. Repeating across successive cuts constructs a finite positive-probability path to the all-mutant state. Since the finite chain admits such a path to an absorbing state from *every* nonabsorbing configuration, there is no closed recurrent class apart from the two unanimous states, and its absorption time \(\tau\) is finite almost surely. The boundedness of \(Y_t\) gives convergence of expectations as \(t\to\infty\).

**3. Strict Moran comparison.** For an initial mixed state, strict one-step drift and the submartingale property imply

\[
\mathbb E[Y_\tau]>Y_0=r^{-i}.
\]

Writing \(p=\rho_H(S;r)\) and using \(I_\tau\in\{0,N\}\) yields \(\mathbb E[Y_\tau]=(1-p)+pr^{-N}\). Consequently

\[
1-p(1-r^{-N})>r^{-i}.
\]

If \(r>1\), the factor \(1-r^{-N}\) is positive, so \(p<M_{N,i}(r)\). If \(0<r<1\), it is negative, and the inequality reverses on division, yielding \(p>M_{N,i}(r)\).

At \(r=1\), the number of mutants itself is a bounded martingale: within each hyperedge, the \(a_e\) mutant parents contribute \(a_eb_e/(Nd)\) to expected change, while the \(b_e\) resident parents contribute \(-a_eb_e/(Nd)\). Optional stopping gives \(\rho_H(S;1)=i/N\).

**4. Sharp pairwise boundary.** If instead all edges have exactly two vertices, every mixed edge has \(a=b=1\) and all terms in (1) vanish identically. On a connected regular graph, \(Y_t\) is a bounded martingale at every \(r>0\), so the Moran expression holds with equality for each initial set. This proves that the strict effect is genuinely associated with full-group replacements of size at least three. \(\square\)

## Verification

The standard-library verifier `verify.py` constructs the complete exact rational transition matrices directly from parent choices. It independently reconstructs the right-hand side of equation (1) using hyperedge mutant counts, checks neutrality, checks strict drift for higher-order edges and equality for pairwise cycles, and solves the entire finite absorbing linear systems for examples with up to five vertices. Examples include a single large hyperedge, complete triple systems, cyclic triple systems, and a regular nonuniform hypergraph consisting of all triples and quadruples on five vertices. Its complete run gives `PASS 8112 exact rational assertions`.

For the complete triple system on four vertices, the computed single-mutant probability agrees exactly with \(r^2/(r+1)^2\) from Liu and Masuda [1], equations (20)–(21). The exact finite checks serve as independent sanity checks; the infinite-family theorem is supplied by equations (1)–(2) and finite-state absorption, not by extrapolating enumeration.

To reproduce, use `python3 verify.py` with Python 3.10 or later. No external packages or network access are required.

## Relationship to prior work

Liu and Masuda [1] introduce precisely the full-hyperedge birth–death model and give model-specific computations and evidence of suppression for complete, cyclic, and star three-uniform hypergraphs, as well as empirical datasets. Their analysis does not state or establish the present all-fitness, all-initial-state theorem for *every* connected incidence-regular hypergraph, including nonuniform edges. The derivation here identifies the strictly convex edge contribution that yields an exact optional-stopping comparison.

The classical isothermal theorem for connected regular graphs [2] supplies the pairwise equality benchmark and is therefore compatible, not stronger in the higher-order setting. Liu and Masuda [3] prove submartingale-based suppression in a **different two-layer network process** with coupled fitnesses, which motivates comparison of methods but does not imply formula (1) for full-hyperedge overwrites. Sheng and collaborators [4] analyze a **single-focal-node death–birth/complex-contagion update** on regular hypergraphs using a weak-selection hyperedge approximation, not the exact globally fitness-proportional full-group overwrite transition studied here.

## Limitations

The proof requires common incidence degree; it makes no claim for irregular hypergraphs. It assumes that one selected parent overwrites *every* other member of its chosen hyperedge. It is not valid without separate analysis for majority-filtered Model 2, single-node imitation, temporal hypergraphs, or state-dependent payoffs. It gives strict fixation-probability inequalities but no uniform quantitative gap away from the Moran baseline and no general closed-form exact fixation probability. An equivalent unindexed result remains possible; independent external priority review has not been undertaken.

## References

[1] R. Liu and N. Masuda, *Fixation dynamics on hypergraphs*, PLOS Computational Biology 19 (2023), e1011494; first public arXiv version 13 January 2023, https://arxiv.org/abs/2301.05343 ; https://doi.org/10.1371/journal.pcbi.1011494 .

[2] E. Lieberman, C. Hauert, and M. A. Nowak, *Evolutionary dynamics on graphs*, Nature 433 (2005), 312–316, https://doi.org/10.1038/nature03204 .

[3] R. Liu and N. Masuda, *Fixation dynamics on multilayer networks*, SIAM Journal on Applied Mathematics 84 (2024), 2028–2050, https://doi.org/10.1137/23M1620144 .

[4] A. Sheng, A. McAvoy, Y. Tian, S. Zhang, A. Fontan, and J. B. Plotkin, *Hyperedge approximation for stochastic processes on higher-order networks*, first publicly released 22 May 2026, https://arxiv.org/abs/2605.23444 .
