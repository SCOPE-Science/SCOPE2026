# Exact fixed-core-edge fastest-mixing frontier on complete split graphs

## Finding
Let \(s,m\ge2\) be integers and let \(G_{s,m}=K_s\vee\overline{K_m}\). For \(0\le t\le1/(s-1)\), consider **all** real symmetric nonnegative stochastic matrices \(P\) supported on the diagonal and the edges of \(G_{s,m}\), subject to the requirement that every off-diagonal transition between two different vertices of the clique \(K_s\) equals the prescribed value \(t\). Other allowed transition probabilities, including those between the clique and independent set, are free. Define the second-largest eigenvalue modulus \(\mu(P)=\max_{v\perp\mathbf1,\,\|v\|=1}|v^TPv|\). Then its global optimum is the maximum of seven explicit affine functions:

\[
\begin{aligned}
\mu_{s,m}^{\star}(t)=\max\Big\{&0,\;st-1,\;\frac{m}{m+2s},\\
&\frac{m-s+s^2t}{m+s},\;
1-\frac{s}{m}\big(1-(s-1)t\big),\\
&\frac{s\big(1-(m+s)t\big)}{2m+s},\;
1-\frac ms-st\Big\}.
\end{aligned}
\]

This is a global optimum even among nonsymmetric-in-vertices transition assignments, provided that \(P\) itself is a symmetric matrix. Every prescribed value \(t\) in the stated interval admits an optimal matrix, and it can be chosen with constant probability \(a\) on every clique-to-independent-set edge. An explicit optimal \(a\) is
\[
a=\max\left\{0,\;\frac{1-\mu_{s,m}^{\star}(t)}s,\;\frac{1-\mu_{s,m}^{\star}(t)-st}{m}\right\}.
\]

In particular, with \(s=5\) and \(m=2\), four *different* regimes occur:
\[
\mu_{5,2}^{\star}(t)=\begin{cases}
\frac35-5t,&0\le t\le\frac1{25},\\
\frac59-\frac{35}{9}t,&\frac1{25}\le t\le\frac1{10},\\
\frac16,&\frac1{10}\le t\le\frac16,\\
10t-\frac32,&\frac16\le t\le\frac14.
\end{cases}
\]
The fixed-core-edge constraint initially improves mixing, then leaves the optimum unchanged over a nontrivial interval, then worsens it. The sharp endpoints of the plateau are both rational.

## Assumptions and scope
All graph edges have undirected support; \(P_{ij}=P_{ji}\ge0\), \(\sum_jP_{ij}=1\), and \(P_{ij}=0\) for nonedges with \(i\ne j\). Self-loops (holding probabilities) are allowed. The independent set has no mutual off-diagonal transitions. The constraints fix **each** distinct clique-to-clique entry at \(t\), not their sum or an upper bound. The interval \(0\le t\le1/(s-1)\) is exactly the feasible range for the prescribed core transitions. At \(t=1/(s-1)\), cross transitions are forced to zero and the optimal SLEM equals \(1\); at this disconnected boundary it is not an ergodic mixing rate. The claim concerns discrete-time, uniform-stationary, reversible chains, not arbitrary nonreversible chains or nonuniform prescribed stationary distributions.

## Proof
Let \(J=\mathbf1\mathbf1^T/(s+m)\). For a symmetric stochastic \(P\), the objective is \(\|P-J\|_{\mathrm{op}}\). It is convex in \(P\). The group \(S_s\times S_m\) of permutations within the clique and independent set preserves the graph, the entrywise fixed-\(t\) constraints, and the objective under conjugation. Averaging any feasible \(P\) over this group cannot increase SLEM. Thus a global minimizer exists in the two-orbit form with free common cross-edge probability \(a\), while the core probability is fixed at \(t\).

Nonnegative diagonal entries are equivalent to
\[
0\le a\le u:=\min\left\{\frac1s,\;\frac{1-(s-1)t}{m}\right\}.
\]
Every such \(a\) produces a valid symmetric stochastic matrix by setting leaf holding probabilities to \(1-sa\) and clique holding probabilities to \(1-ma-(s-1)t\).

The orthogonal subspaces of independent-set differences (dimension \(m-1\)), clique differences (dimension \(s-1\)), the difference of the two partwise-constant vectors (dimension one), and the constants (dimension one) diagonalize the matrix. Their respective eigenvalues are
\[
1-sa,\qquad 1-ma-st,\qquad 1-(m+s)a,\qquad 1.
\]
Because \(a\le1/s\), the first nontrivial eigenvalue is nonnegative. A proposed upper bound \(r\ge0\) on SLEM is feasible if and only if there exists \(a\) satisfying
\[
\max\left\{0,\frac{1-r}{s},\frac{1-r-st}{m}\right\}
\le a\le
\min\left\{\frac1s,\frac{1-(s-1)t}{m},\frac{1+r}{m+s},\frac{1+r-st}{m}\right\}.
\]
Comparing each lower bound with each upper bound produces the necessary and sufficient conditions
\[
\begin{aligned}
r&\ge0,\qquad r\ge st-1,\qquad r\ge\frac m{m+2s},\\
r&\ge\frac{m-s+s^2t}{m+s},\qquad
r\ge1-\frac{s}{m}\big(1-(s-1)t\big),\\
r&\ge\frac{s\big(1-(m+s)t\big)}{2m+s},\qquad
r\ge1-\frac ms-st.
\end{aligned}
\]
All remaining pairwise inequalities are automatic from \(r\ge0\), \(t\ge0\), and \(1-(s-1)t\ge0\). Hence the maximum of the seven listed functions is both necessary and sufficient, and choosing \(a\) to be the displayed lower endpoint constructs an optimal matrix. Because the averaging bound already applies to every feasible symmetric matrix, this proves unrestricted global optimality under the fixed-edge constraint. Substituting \((s,m)=(5,2)\) and taking the upper envelope gives the four stated intervals and exact crossings at \(1/25\), \(1/10\), and \(1/6\).

## Verification
The standalone standard-library program `verify.py` reconstructs the seven-branch formula with exact rational arithmetic and independently minimizes the maximum of the six signed eigenvalue affine functions over the full feasible \(a\)-interval by enumerating their intersections and endpoints. It checked \(3332\) parameter instances with \(2\le s,m\le15\) and seventeen rational values of \(t\) per pair, including both feasibility boundaries. It additionally built \(180\) exact transition matrices and verified stochasticity and all three invariant eigenspace identities. It checked the entire displayed four-regime formula at \(3001\) rational grid points. These finite tests are regression checks; the proof above establishes the result for every permitted integer pair and every real \(t\) in the interval.

Reproduce using Python 3 without external libraries: `python verify.py`.

## Relationship to prior work
Boyd, Diaconis, and Xiao (2004) formulated symmetric fastest-mixing Markov-chain design as a convex spectral optimization; their setup contains this problem as a constrained subclass, but does not give the displayed fixed-core-edge envelope. Boyd, Diaconis, Parrilo, and Xiao (2007), Section 3.1.2, give the exact complete-bipartite result, which covers the boundary \(t=0\) and does not determine the positive-\(t\) frontier. Jafarizadeh (2020) gives the **unconstrained** fastest-mixing result on clique-lifted star graphs, a stronger relevant baseline in the opposite direction: it can optimize internal clique transitions freely and therefore does not yield a formula after every core-to-core transition is prescribed. In the example \((s,m,t)=(5,2,0)\), the fixed-edge optimum is \(3/5\), whereas optimizing internal clique transitions as well gives \(1/6\). Jafarizadeh (2019) explicitly treats trade-offs with fixed edge weights, but on *friendship graphs*, unions of edge-disjoint triangles with one common hub; those are not the complete split graphs considered here (for the stated parameters). This distinction is structural, not just a different variable name.

## Limitations
The result characterizes optimum SLEM and supplies one optimal invariant matrix; it does **not** classify every possible noninvariant optimal matrix. Distinct parameter choices may have coincident active affine branches, and the general formula intentionally leaves the upper-envelope selection implicit rather than listing all possible parameter-dependent regimes. The analysis does not prove universal publication priority: unindexed or inaccessible specialist coverage could subsume the constrained frontier. Its relationship to previously published general SDP formulations is an explicit specialization plus a newly derived closed form, not a new general-purpose convex-optimization principle.

## References
- Stephen Boyd, Persi Diaconis, Lin Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: https://doi.org/10.1137/S0036144503423264 . Published electronically 2004-10-29. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
- Stephen Boyd, Persi Diaconis, Pablo A. Parrilo, Lin Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, preprint arXiv:0709.0955 (2007), https://arxiv.org/abs/0709.0955 ; see Section 3.1.2.
- Saber Jafarizadeh, *Fastest mixing reversible Markov chain on friendship graph: Trade-off between transition probabilities among friends and convergence rate*, Systems & Control Letters 130 (2019), 13–22, DOI: https://doi.org/10.1016/j.sysconle.2019.07.001 . Full text: https://www.researchgate.net/publication/334842673_Fastest_mixing_reversible_Markov_chain_on_friendship_graph_Trade-off_between_transition_probabilities_among_friends_and_convergence_rate .
- Saber Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, DOI: https://doi.org/10.1109/TSIPN.2020.2964211 . Full text: https://www.researchgate.net/publication/338414306_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_and_Subgraphs .
