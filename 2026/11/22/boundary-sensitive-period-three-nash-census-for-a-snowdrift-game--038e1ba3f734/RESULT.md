# Boundary-sensitive period-three Nash census for a snowdrift game with an individual solution

## Finding

Consider the three-strategy snowdrift game with a safe individual solution defined below on a finite simple undirected network whose connected components are paths or cycles, with no isolated vertices. Outside the two stated payoff-tie surfaces, **every pure Nash equilibrium is explicitly classified**. An all-individual-solution equilibrium always exists. Additional equilibria occur only when the benefit exceeds three times the cooperation cost and the safe option costs more than one and a half times the cooperation cost. Then each path of order congruent to one modulo three admits exactly one additional equilibrium, while each cycle of order divisible by three admits exactly three additional equilibria. Every other path or cycle has only the all-individual-solution equilibrium.

In particular, a periodic ring with 10,000 individuals has no cooperator-containing pure Nash equilibrium in the generic parameter domain, whereas a ring with 9,999 individuals admits three such equilibria in the cooperative regime. This arithmetic obstruction applies to noiseless pure Nash profiles; it says nothing by itself about the positive-mutation stationary distribution.

## Assumptions and scope

Let \(G\) be a finite undirected simple graph with no isolated vertices and maximum degree two. A path component \(P_n\) has \(n\ge2\) vertices, and a cycle component \(C_n\) has \(n\ge3\) vertices. At each vertex the available pure actions are cooperation \(C\), defection \(D\), and the individual solution \(I\). The symmetric *row-player* per-neighbor payoff matrix, with columns ordered \((C,D,I)\), is

\[
\begin{array}{c|ccc}
 & C&D&I\\\hline
 C&b-c&b-2c&b-2c\\
 D&b&0&0\\
 I&b-c_I&b-c_I&b-c_I
\end{array}.
\]

A vertex sums its per-neighbor payoffs, and an equilibrium is a pure-action profile in which no vertex can gain by a unilateral change. Assume \(c>0\), \(b>2c\), and \(c<c_I<2c\). Exclude the payoff-tie surfaces \(b=3c\) and \(c_I=3c/2\). Set

\[
\chi=\begin{cases}
1,&b>3c\text{ and }c_I>3c/2,\\
0,&\text{otherwise}.
\end{cases}
\]

For a path, label vertices consecutively and write words over \(\{C,D,I\}\). For a cycle, words are read cyclically on labeled vertices. If \(\chi=1\), the complete list of pure equilibria on \(P_n\) consists of \(I^n\) and, only when \(n=3k+1\) for an integer \(k\ge1\), the additional word

\[
D(CCD)^k.
\]

On \(C_n\), the complete list consists of \(I^n\) and, only when \(n=3k\) for an integer \(k\ge1\), the three distinct cyclic shifts of \((CCD)^k\). If \(\chi=0\), the all-\(I\) profile is the unique pure equilibrium on every component. In every case listed, all unilateral best replies are strict.

Consequently, if \(G\) has path components of orders \(n_1,\dots,n_a\) and cycle components of orders \(m_1,\dots,m_d\), the number of pure Nash equilibria is

\[
\prod_{j=1}^{a}\bigl(1+\chi\,\mathbf1_{\{n_j\equiv1\pmod3\}}\bigr)
\prod_{j=1}^{d}\bigl(1+3\chi\,\mathbf1_{\{m_j\equiv0\pmod3\}}\bigr).
\]

## Proof

**1. Exact local payoffs.** At a vertex of degree \(d\in\{1,2\}\), let \(m\) of its neighbors play \(C\). The payoff of a hypothetical unilateral choice is

\[
U_C=d(b-2c)+mc,\qquad U_D=mb,\qquad U_I=d(b-c_I).
\]

At a degree-one vertex with \(m=0\), \(I\) is the unique best reply: \(U_I>U_C\) because \(c_I<2c\), and \(U_I>U_D=0\) because \(b>c_I\). With \(m=1\), \(D\) is the unique best reply, since \(b>b-c\) and \(b>b-c_I\). Thus path endpoints can never cooperate.

At a degree-two vertex with \(m=0\), \(I\) is the unique best reply for the same reasons. With \(m=2\), \(D\) is the unique best reply, since \(2b>2(b-c)\) and \(2b>2(b-c_I)\). With \(m=1\), the three payoff values are \(2b-3c\), \(b\), and \(2b-2c_I\). Hence \(C\) is the unique best reply exactly if \(b>3c\) and \(c_I>3c/2\). Under the excluded-tie assumptions, if either inequality fails then \(C\) is never a best reply at any vertex.

**2. Noncooperative region.** If \(\chi=0\), there are no best-reply cooperators. In a profile without cooperators, all vertices have \(m=0\), and \(I\) is their unique best reply. Thus \(I^{|G|}\) is the unique equilibrium.

**3. Cooperative region on cycles.** If \(\chi=1\), the best-response rule at every degree-two vertex is

\[
 m=0:\ I,\qquad m=1:\ C,\qquad m=2:\ D.
\]

At any equilibrium containing a cooperator, that cooperator has exactly one cooperative neighbor. So the induced cooperator graph is a disjoint union of edges \(CC\). A noncooperator neighboring at least one cooperator cannot have exactly one cooperative neighbor (it would strictly prefer \(C\)); thus it must have exactly two, and must itself play \(D\). Every \(CC\) block is therefore flanked by a single \(D\) separating it from the next \(CC\) block. Repeating along a connected cycle forces the word \(CCDCCD\cdots\), whose length must be divisible by three. There are exactly three labeled rotations, each satisfying every local best-response condition. The remaining possibility is no cooperators, which forces all \(I\).

**4. Cooperative region on paths.** Any cooperative vertex is interior and has precisely one cooperative neighbor; therefore each cooperator block is \(CC\). The noncooperative neighbor immediately outside such a block, if interior, needs two cooperative neighbors and is a \(D\) separating two blocks. If instead it is an endpoint, the endpoint is uniquely \(D\) because its one neighbor cooperates. Induction to the two ends therefore forces exactly \(D(CCD)^k\) with \(k\ge1\), giving \(n=3k+1\). Direct substitution into the local rules proves existence, uniqueness and strictness. With no cooperators the only equilibrium is \(I^n\).

**5. Disconnected graphs.** Distinct connected components have no payoff interactions. Their equilibrium choices are independent, so multiplying the componentwise counts gives the stated product.

## Verification

The executable `verify.py` enumerates every profile over the three actions, tests all unilateral deviations using exact rational arithmetic, and compares the resulting equilibrium sets with the formulas. It passed 85 graph/parameter comparisons: all paths of orders 2–10 and cycles of orders 3–10, at five rational payoff pairs covering both sides of each strict threshold. Direct constructive checks for ring orders 9,999 and 10,000 verify the two differing prediction sets, without exhaustively enumerating those large rings. The universal result rests on the proof, not on finite tests.

## Relationship to prior work

Hirofumi Takesue, *Myopic Best Response as a Double-Edged Mechanism in Networked Social Dilemmas with Individual Solutions*, arXiv:2603.18128 (first posted March 18, 2026), supplies the payoff model and simulation setting, including 10,000-agent rings, and describes a local \(CC\)-pair/defector pattern and its susceptibility to single-agent mutation. Its degree-two heuristic already identifies the threshold values \(b=3c\) and \(c_I=3c/2\); these thresholds and the existence of locally stable \(CC\)-defector patterns are not claimed as new. The present finding is the *exhaustive pure-equilibrium classification*, with the ring divisibility obstruction, the open-path residue shift, and the multiplicative census over arbitrary degree-two networks.

Takesue's earlier arXiv:2411.05543 studies the same underlying safe-option payoff game under imitation and well-mixed replicator dynamics. Lee, Cleveland and Szolnoki, arXiv:2307.02832, analyze myopic updates with a different third action (quasi-cooperation, not a constant-payoff individual solution). Neither provides this exact pure-equilibrium census in the inspected full texts.

## Limitations

This result classifies deterministic pure Nash equilibrium profiles, not quasistationary cooperation or the invariant law of the stochastic logit/mutation dynamics. It does not classify behavior on graphs of degree at least three, directed graphs, or isolated vertices. Exact payoff-tie surfaces are excluded: at equality additional non-strict equilibria may arise. The ring-periodic pattern was already qualitatively recognized in the originating work, so the scientific increment is the global completeness and precise finite-size/path arithmetic rather than the discovery of that local pattern. Priority beyond the inspected primary literature and indexed records has not been independently established.

## References

1. H. Takesue, *Myopic Best Response as a Double-Edged Mechanism in Networked Social Dilemmas with Individual Solutions*, arXiv:2603.18128 (2026). https://arxiv.org/abs/2603.18128
2. H. Takesue, *Evolution of cooperation in a three-strategy game combining snowdrift and stag hunt games*, arXiv:2411.05543 (2024). https://arxiv.org/abs/2411.05543
3. H.-W. Lee, C. Cleveland and A. Szolnoki, *Restoring spatial cooperation with myopic agents in a three-strategy social dilemma*, arXiv:2307.02832 (2023). https://arxiv.org/abs/2307.02832
