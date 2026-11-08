# Maximum-cut law for primitive-two chip-firing energy spectra

## Finding

Let \(G=(V,E)\) be a finite connected simple undirected graph with \(n=|V|\ge2\), \(m=|E|\), and maximum cut size \(C=\operatorname{MaxCut}(G)\). Under synchronous parallel chip-firing, let \(H_G(z)\) count the *immediately* primitive-two-periodic configurations by their conserved total number of chips:
\[
H_G(z)=\sum_{\substack{x\in\mathbb Z_{\ge0}^{V}\\ U^2x=x,\ Ux\ne x}}z^{\sum_{v\in V}x(v)}.
\]
Define \([r]_z=1+z+\cdots+z^{r-1}\) for positive integers \(r\), and \([0]_z=0\). For a vertex subset \(S\subseteq V\), let \(c_S(v)\) be its number of neighbors across the cut and \(c(S)=|E(S,V\setminus S)|\). Then
\[
\boxed{H_G(z)=\sum_{S\subseteq V}z^{2m-c(S)}\prod_{v\in V}[c_S(v)]_z.}
\]
In particular, its exact nonzero coefficient support is the **complete integer interval**
\[
\boxed{\operatorname{supp}H_G=\{2m-C,2m-C+1,\ldots,2m+C-n\}.}
\]
If \(M(G)\) denotes the number of unordered maximum cuts (identifying \(S\) and \(V\setminus S\)), both endpoint coefficients equal \(2M(G)\). The mass polynomial is reciprocal in the sense \(H_G(z)=z^{4m-n}H_G(z^{-1})\).

A further consequence is that the decision problem **whether there exists an immediately primitive-two-periodic chip configuration of mass at most a given integer bound** is NP-complete, even when restricted to connected simple graphs. Thus the exact lowest two-cycle mass encodes the MAX-CUT invariant:
\[
\boxed{\min\{|x|: U^2x=x\ne Ux\}=2m-\operatorname{MaxCut}(G).}
\]

## Assumptions and scope

Vertices are labelled, edges are simple and undirected, and \(G\) is connected with at least two vertices. At each discrete simultaneous update, vertex \(v\) fires if and only if its current nonnegative integer chip count \(x(v)\) is at least its degree \(d(v)\), sending one chip to each neighbor. Write \(f_x(v)=\mathbf1_{x(v)\ge d(v)}\). The update is
\[
(Ux)(v)=x(v)+\sum_{w\sim v}f_x(w)-d(v)f_x(v).
\]
Mass means \(|x|=\sum_v x(v)\). A primitive two-cycle is required **from time zero**: \(U^2x=x\) and \(Ux\ne x\). No assertion is made about the transient or eventual period of an arbitrary configuration. The equality for support concerns integer chip masses, not counts modulo a prime or labelled temporal orbit classes.

## Proof

**Step 1: exactly one firing per vertex over two rounds.** If \(U^2x=x\), let \(t(v)=f_x(v)+f_{Ux}(v)\in\{0,1,2\}\). Summing the two updates gives \(d(v)t(v)=\sum_{w\sim v}t(w)\), so \(t\) is harmonic on the connected graph and is constant. If this constant is zero, no vertex fires in either round and \(Ux=x\); if it is two, every vertex fires in both rounds and \(Ux=x\). Thus any primitive-two state has \(t(v)=1\) for all \(v\).

**Step 2: exact cut parametrization.** Set \(S=\{v:f_x(v)=1\}\). Put \(q_v=c_S(v)\). At the first update, a vertex in \(S\) receives \(d(v)-q_v\) chips and loses \(d(v)\); a vertex outside \(S\) receives \(q_v\) chips and loses none. Requiring the second-round firing pattern to be precisely \(V\setminus S\) is therefore equivalent to the independent integer intervals
\[
\begin{aligned}
  d(v)\le x(v)\le d(v)+q_v-1, &&v\in S,\\
  d(v)-q_v\le x(v)\le d(v)-1, &&v\notin S.
\end{aligned}
\]
All these endpoints are nonnegative. An interval is empty exactly when \(q_v=0\). Conversely, these inequalities guarantee alternate firing; because every vertex then fires once and receives one chip from every neighbor over the two rounds, \(U^2x=x\). Both firing sets are nonempty (each vertex has a cross-cut neighbor), hence \(Ux\ne x\). Every state has a unique first-round firing set \(S\), so the contributions do not overlap.

**Step 3: mass polynomial and cut interval.** For a fixed \(S\) with \(q_v\ge1\) for all vertices, the minimum mass is
\[
\sum_{v\in S}d(v)+\sum_{v\notin S}(d(v)-q_v)=2m-c(S),
\]
since \(\sum_{v\notin S}q_v=c(S)\). Each vertex contributes an independent slack in \(\{0,\ldots,q_v-1\}\). This proves the stated sum of products of finite geometric series. Their aggregate slack realizes **every integer** from zero through \(\sum_v(q_v-1)=2c(S)-n\), giving the interval \([2m-c(S),\,2m+c(S)-n]\). If some \(q_v=0\), that cut contributes zero, as specified by \([0]_z=0\).

**Step 4: maximum cut makes the union an interval.** Let \(S_*\) be a maximum cut of size \(C\). Every vertex has \(c_{S_*}(v)\ge1\): otherwise switching that vertex to the other side strictly increases the cut size because \(G\) has positive degree at that vertex. Thus \(S_*\) realizes every mass in \([2m-C,2m+C-n]\). Every other contributing cut of size \(c\le C\) realizes only a subinterval of this one. This proves equality of the support. At either endpoint only maximum cuts contribute, with exactly one slack choice for each oriented maximum cut. Therefore the endpoint coefficient is \(2M(G)\). Each geometric-series factor is reciprocal; equivalently, chip-complementation \(x(v)\mapsto2d(v)-1-x(v)\) reverses mass, proving \(H_G(z)=z^{4m-n}H_G(z^{-1})\).

**Step 5: computational complexity.** Connected MAX-CUT decision on input \((G,k)\) reduces in polynomial time to existence of a primitive-two state of mass at most \(2m-k\), by the minimum-mass equality. MAX-CUT is NP-complete on connected simple graphs: from a possibly disconnected graph one may connect components by a tree of bridges; each bridge can be cut simultaneously by choosing orientations of the component cuts, so the optimum increases by exactly the number of bridges. Membership in NP follows by presenting the integer chip vector and computing two updates: the inequalities from Step 2 ensure every primitive-two witness has \(0\le x(v)\le2d(v)-1\), hence its binary encoding is polynomial in the graph size. The same argument provides an explicit polynomial-size witness from a maximum cut.

## Verification

Two independent, standard-library Python programs accompany this note. `tests/verify_dynamics.py` exhaustively enumerates every connected labelled simple graph on two through five vertices (771 graphs), all 1,769,796 chip configurations in the necessary bounded ranges, and compares the actual primitive-two mass histogram to the cut polynomial. It also checks the exact support and endpoint multiplicities. `tests/verify_maxcut.py` independently constructs states at *every* claimed mass for all oriented maximum cuts in 139 connected test graphs (paths, cliques and reproducibly sampled graphs of orders two through eleven), checking both iterates and endpoint uniqueness. The actual package outputs are in `tests/dynamics_output.txt` and `tests/maxcut_output.txt`.

Both programs are finite tests of the general proof, not substitutes for the connected-graph argument or complexity reduction.

## Relationship to prior work

Jiang's 2010 Proposition 2.5 characterizes return after a fixed number of updates by equal firing totals across vertices. That result supplies the established conservation backdrop to Step 1, but does not give the cut polynomial, the maximum-cut energy endpoints, the full contiguous support, the boundary multiplicities, or the MAX-CUT equivalence. Jiang, Scully and Zhang's 2012/2015 study characterizes which firing patterns can occur and analyzes local/tree-like dynamics; in the relevant full-text sections it does not state the present cut-to-energy identity. The foundational Bitar–Goles paper concerns periods, including trees. Subsequent work on universal *eventual* period two within a prescribed density band addresses a different predicate than immediate periodicity and does not determine these endpoints.

Exact mass polynomials for individual graph families (notably paths/cycles, wheels and complete split graphs) are compatible with this theorem; those family formulas cannot imply a graph-universal MAX-CUT support law. Searches for the statement under “period-two chip-firing maximum cut”, “minimum chip total”, “cut-degree product” and related aliases revealed no dominating published result in the sources inspected. This is a qualified originality assessment, not a proof of priority.

## Limitations

The theorem applies to connected simple graphs with at least two vertices and to synchronous threshold-equals-degree chip-firing. It says nothing about all longer primitive periods or all eventual two-cycles from a transient. It identifies the support and the **two extreme coefficients**, but does not give a computationally efficient method to obtain all interior coefficients; the displayed cut expansion is exponential in general. The inaccessible full text of the 1992 foundational paper and of the closely related August 2026 density-band study leaves residual literature-priority risk. Independent audit has not been performed.

## References

- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, original arXiv posting 2010-03-04, arXiv:1003.0943, especially Proposition 2.5. https://arxiv.org/abs/1003.0943
- T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first publicly posted 2012-11-29, arXiv:1211.6786; SIAM J. Discrete Math. 29 (2015), 615–630. https://arxiv.org/abs/1211.6786
- J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoret. Comput. Sci. 92 (1992), 291–300. https://doi.org/10.1016/0304-3975(92)90316-8
- D. Wang and N. Lannan, *All parallel chip-firing games with a middle density band have period two*, arXiv:2608.03258 (2026). The accessible abstract states an eventual-period result, not an initial periodic-state census.
- R. M. Karp, *Reducibility Among Combinatorial Problems*, 1972; classical NP-completeness of MAX-CUT.
