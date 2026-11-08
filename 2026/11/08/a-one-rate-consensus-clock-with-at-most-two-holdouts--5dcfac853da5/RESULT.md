# A one-rate consensus clock with at most two holdouts

## Finding

Let \(n\ge4\) labeled agents have one of two opinions. In each **discrete event**, choose a \(k\)-element group uniformly from all \(\binom nk\) groups, choose one of its members uniformly as speaker, and set **every member** of the group (including the speaker) to that speaker's opinion. All events count, including events on monochromatic groups that leave the state unchanged. The group family is fixed and complete; there is no rewiring or active-only conditioning. Let \(T\) be the first number of events required to reach unanimity, and assume initially exactly \(x\) agents hold opinion A, where \(1\le x\le n-1\).

**Theorem.** For \(k=n\), \(T=1\) almost surely. For \(k=n-c\), with \(c\in\{1,2\}\), let

\[
(a_c,\lambda_c)=\begin{cases}
\bigl(\dfrac{2x(n-x)}{n(n-1)},\dfrac2n\bigr),&c=1,\\[5pt]
\bigl(\dfrac{3x(n-x)}{n(n-1)},\dfrac{4n-6}{n(n-1)}\bigr),&c=2.
\end{cases}
\]

Then, for **every integer** \(t\ge1\),

\[
\Pr_x(T>t)=a_c\lambda_c^{t-1},\qquad
\Pr_x(T=1)=1-a_c,\qquad
\Pr_x(T=t)=a_c(1-\lambda_c)\lambda_c^{t-2}\ (t\ge2).
\]

In particular, these are exact full finite-population first-consensus laws, not large-population approximations, and

\[
\mathbb E_x T=\begin{cases}
1,&k=n,\\[2pt]
1+\dfrac{2x(n-x)}{(n-1)(n-2)},&k=n-1,\\[5pt]
1+\dfrac{3x(n-x)}{(n-2)(n-3)},&k=n-2.
\end{cases}
\]

The probability of eventual A-consensus is exactly \(x/n\). The one-rate tail phenomenon has a concrete boundary: if \(n=6\), \(k=3\) and \(x=1\) (three excluded group members), the first three survival probabilities are \(2/3\), \(1/2\) and \(59/150\); the ratios \(3/4\) and \(59/75\) differ. Thus a single geometric tail beginning after event one is not a general property of smaller groups.

## Assumptions and scope

Agents are distinguishable but the interaction rule is fully exchangeable. The initial configuration is any deterministic binary labeling with exactly \(x\) opinion-A agents. The speaker is selected uniformly **within** the uniformly selected group. Times count global opportunities to choose groups; there is no conditioning on the group being mixed, no independent opinion choices by group members, and no continuous-time Poisson normalization. The result applies to all \(n\ge4\) and the three indicated group sizes, with arbitrary initial mixture. No claim is made for noncomplete hypergraphs, adaptive rewiring, majority propagation, active-only scheduling, or group sizes \(k\le n-3\) beyond the stated counterexample.

## Proof

**1. Reduction and fixation probability.** By permutation symmetry, the opinion-count process depends only on the current number of A opinions. Selecting a group and copying its uniformly selected speaker preserves the **conditional expectation** of the A count: when a selected group has \(j\) A agents, its expected final number of A agents is \(k(j/k)=j\). Thus the count is a bounded martingale. With \(k\ge2\), each non-unanimous count has a positive-probability route to unanimity in finitely many steps, so absorption occurs almost surely on the finite state space. Optional stopping for the bounded count gives eventual A-consensus probability \(x/n\). When \(k=n\), one update is unanimous.

**2. One excluded agent.** For \(k=n-1\), the first update leaves disagreement precisely if the omitted agent and the chosen speaker have opposite opinions. Its probability is

\[
 a_1=\frac{2x(n-x)}{n(n-1)}.
\]

Whenever disagreement survives, exactly one agent differs from the other \(n-1\). From such a configuration the next update still leaves one dissenter if (i) that dissenter is omitted (probability \(1/n\)), or (ii) a majority agent is omitted and the speaker is the dissenter (probability \(1/n\)). The total survival probability per later event is therefore \(\lambda_1=2/n\), independent of the dissenter's color or identity. Iterating yields \(\Pr(T>t)=a_1\lambda_1^{t-1}\).

**3. Two excluded agents.** For \(k=n-2\), every group update makes all but two agents agree. Write \(u=x(n-x)/[n(n-1)]\). Of all first-event outcomes, exactly one dissenter arises when the two omitted agents have different opinions, with probability \(2u\). Exactly two dissenters arise when the omitted agents agree but the chosen speaker has the opposite opinion. Counting the two possible omitted colors gives

\[
 \frac{\binom{n-x}{2}\,x+\binom x2\,(n-x)}{\binom n2(n-2)}=u.
\]

All other outcomes are unanimous. As \(n\ge4\), the two surviving occupancy types (one or two dissenters) are well defined; when the two colors tie at \(n=4\), the type with two dissenters is still unambiguous. In the ordered state types \((1,2)\), the **substochastic** transition matrix is

\[
 Q=\begin{pmatrix}
 2/n&1/n\\[3pt]
 4(n-2)/[n(n-1)]&2(n-2)/[n(n-1)]
 \end{pmatrix}.
\]

This follows by distinguishing the zero, one or two dissenters in the omitted pair, and copying a uniformly chosen member of the included group. Its second row is a multiple of its first, and direct multiplication shows

\[
 (2,1)Q=\lambda_2(2,1),\qquad
 \lambda_2=\frac{4n-6}{n(n-1)}<1.
\]

After event one, the nonabsorbed state has row distribution \(u(2,1)\). After event \(t\), its substochastic distribution is therefore \(u(2,1)Q^{t-1}=u\lambda_2^{t-1}(2,1)\). Adding the two coordinates proves \(\Pr(T>t)=3u\lambda_2^{t-1}\) for all \(t\ge1\). The probability-mass and mean formulas in the theorem follow from this geometric survival law, using \(1-\lambda_2=(n-2)(n-3)/[n(n-1)]\).

**4. Boundary example.** For general \(k\), if the selected group contains \(j\) A agents, then the A-count transitions to \(x-j+k\) with probability \(j/k\), or to \(x-j\) with probability \((k-j)/k\). Averaging over the hypergeometric number of A agents in the group gives the exact count-chain kernel

\[
 P_{x,y}=\sum_j \frac{\binom xj\binom{n-x}{k-j}}{\binom nk}
 \left(\frac jk\mathbf1_{\{y=x-j+k\}}+
 \frac{k-j}{k}\mathbf1_{\{y=x-j\}}\right).
\]

For \(n=6,k=3,x=1\), multiplying this finite stochastic matrix one, two and three times gives \(\Pr(T>1)=2/3\), \(\Pr(T>2)=1/2\), and \(\Pr(T>3)=59/150\). Since \((1/2)/(2/3)=3/4\), but \((59/150)/(1/2)=59/75\), there is no single geometric survival ratio for this example.

## Verification

Run `python3 verify_consensus.py` using only the Python standard library. It performs 14,940 exact-rational checks of survival probabilities by **direct labeled-state enumeration**, including every mixed binary labeling for \(4\le n\le9\), the three group sizes and event times one through five. An independently coded hypergeometric count-chain implementation checks another 1,575 survival cases and solves the rational hitting-time equations for \(4\le n\le13\). A separate small-case test checks the non-geometric three-holdout example. These finite checks corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work

Golovin, Mölter and Kuehn (arXiv:2308.03640, earliest posted August 7, 2023 UTC) describe the same proportional **whole-hyperedge copying rule**, but in an adaptive model whose interaction clock is triggered by mixed hyperedges. Here the group family is complete and every group is sampled uniformly, including monochromatic ones. That is a different, explicitly specified scheduling convention. Their accessible full text studies motif equations, simulations and the fragmentation transition, not this exact finite-population first-passage law.

Kim, Lee, Min, Porter, San Miguel and Goh (arXiv:2407.11261, later Phys. Rev. E 111, L052301, 2025) study a distinct group-driven voter rule: a sampled **single node** may flip after observing other group members. Their large-population exit-time analysis does not imply whole-group simultaneous-copying distributions. Related results on pair-codegrees and expected binary discordance concern first and second moments, which alone cannot specify the survival probability of the nonabsorbed chain. The rank-one occupancy reduction here supplies the missing first-passage information.

## Limitations

The result does **not** apply to active-only updates under a Poisson clock, to rewiring, or to independent per-member opinion changes; even when the copied opinion rule is the same, these alter the time law. The geometric tail starts at event one, not event zero. The three-holdout example only proves that an analogous universal one-rate formula already fails in one natural case, not that every smaller group fails it. A claim of global priority among all unindexed literature is not made; the cited comparisons and reproducible proof delimit the contribution.

## References

1. A. Golovin, J. Mölter and C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640 (first publicly posted August 7, 2023 UTC). https://arxiv.org/abs/2308.03640
2. J. Kim, D.-S. Lee, B. Min, M. A. Porter, M. San Miguel and K.-I. Goh, *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, arXiv:2407.11261 (2024); Phys. Rev. E 111, L052301 (2025). https://arxiv.org/abs/2407.11261
3. C. Cooper, M. Dyer, A. Frieze and N. Rivera, *Discordant Voting Processes on Finite Graphs*, ICALP 2016, LIPIcs 55, 145:1--145:13. https://doi.org/10.4230/LIPIcs.ICALP.2016.146
