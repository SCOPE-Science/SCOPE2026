# Seven goods are the sharp online round-robin EF1 failure threshold for three agents

## Finding

For **three agents** taking the available indivisible goods in cyclic order \(A,B,C,A,B,C,\ldots\), with full observation of earlier picks, any allocation induced by a **Nash equilibrium**, hence any subgame-perfect Nash equilibrium (SPNE), is envy-free up to one good (EF1) whenever the total number of goods is at most \(6\). This assertion holds for any normalized, nonnegative, monotone bundle valuations.

At \(7\) goods there are strictly positive **additive** valuations, with each agent assigning different utilities to every two distinct bundles, and a pure SPNE whose allocation is **not EF1**. Hence \(7\) is the exact smallest number of goods for which an online three-agent round-robin SPNE can fail EF1. The claim is **existential at the boundary**; it does not claim that every SPNE of the exhibited instance fails EF1 or that the equilibrium allocation is unique.

## Assumptions and scope

All \(m\) goods are indivisible and allocated, one per turn, with agents \(A,B,C\) in that order, repeating cyclically and truncating at exhaustion. Every move is observed. A pure strategy selects an available good after every possible history; a pure SPNE is a profile that is a Nash equilibrium in every resulting subgame. For \(m\le6\), valuations \(v_i:2^M\to\mathbb R_{\ge0}\) are monotone and normalized by \(v_i(\varnothing)=0\). For the seven-good witness they are additive and strictly positive.

EF1 means that for every ordered pair of agents \((i,j)\) with \(S_j\ne\varnothing\), there exists \(g\in S_j\) such that \(v_i(S_i)\ge v_i(S_j\setminus\{g\})\). The online extensive-form game differs from a simultaneous, once-for-all ranking-report mechanism.

The following is the **entire integer singleton-value table** for the witness. Column \(g_t\) denotes the \(t\)-th labeled good, not the \(t\)-th pick:

| Agent | \(g_1\) | \(g_2\) | \(g_3\) | \(g_4\) | \(g_5\) | \(g_6\) | \(g_7\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(A\) | 904 | 192 | 132 | 144 | 514 | 385 | 672 |
| \(B\) | 1296 | 160 | 136 | 960 | 900 | 129 | 386 |
| \(C\) | 648 | 641 | 144 | 672 | 192 | 898 | 132 |

## Proof

**1. Sharp lower bound (no more than six goods).** Fix an equilibrium outcome, and an ordered pair of distinct agents \((i,j)\). If \(j\) receives zero or one good, EF1 toward \(j\) is immediate from normalization and nonnegativity. Otherwise, since at most six goods are allocated, \(j\) receives exactly two goods, say \(x\) and \(y\), in that temporal order. In the cyclic order of three agents, **every agent takes her first turn before anyone takes a second turn**. Thus at \(i\)'s first decision node, the good \(y\), eventually taken on \(j\)'s second turn, is still available along the original equilibrium play. Agent \(i\) could instead select \(y\) at that first node; by monotonicity, whatever happens afterward, the total value of the deviating bundle is at least \(v_i(\{y\})\). Since a Nash-equilibrium strategy cannot be improved by this deviation, \(v_i(S_i)\ge v_i(\{y\})=v_i(S_j\setminus\{x\})\), proving EF1. Cases with fewer than three initial picks are included: an agent with no turn cannot envy a bundle after the latter's only good is removed. The stated theorem concerns pure equilibrium allocations.

**2. Explicit SPNE at seven goods.** Let \(M=\{g_1,\ldots,g_7\}\). For every subset \(R\subseteq M\) of remaining goods, the player to move is determined by \(|R|\); write \(i(R)\) for that agent. Define \(F(\varnothing)=(0,0,0)\). For nonempty \(R\), choose the lowest-index good \(g\in R\) that maximizes
\[
v_{i(R)}(\{g\})+F_{i(R)}(R\setminus\{g\}),
\]
and set \(F(R)=F(R\setminus\{g\})+v_{i(R)}(\{g\})e_{i(R)}\). At every history with remaining set \(R\), have the current mover pick this chosen good. The earlier bundle values are sunk additive terms. Induction on \(|R|\) therefore establishes that the strategy profile is a pure SPNE at **every** possible history. The rule resolves any equal continuation payoff by smaller good index.

The complete \(128\)-state dynamic-programming certificate and standalone exact-integer checker are supplied as `DP_CERTIFICATE.json` and `CHECKER.py`. They validate every one of the \(448\) state-action alternatives, including those off the equilibrium path. An independent full-history tree recursion visits all \(13{,}700\) game-tree nodes and all \(5040\) terminal histories, checking the same equilibrium action at every history. At the full remaining set the selected path is
\[
g_1,\ g_2,\ g_3,\ g_5,\ g_4,\ g_6,\ g_7,
\]
giving
\[
S_A=\{g_1,g_5,g_7\},\quad S_B=\{g_2,g_4\},\quad S_C=\{g_3,g_6\}.
\]
The respective attained utilities are \((2090,1120,1042)\). In particular, player \(B\) has \(v_B(S_B)=160+960=1120\), whereas the **smallest** value remaining after removing any one good of \(A\)'s bundle is
\[
\min_{g\in S_A}v_B(S_A\setminus\{g\})=v_B(\{g_5,g_7\})=900+386=1286>1120.
\]
Hence the allocation fails EF1.

**3. Genuine strict bundle valuations.** Each witness entry is of the form \(128(b+1)+2^r\) for an integer \(b\ge0\) and a permutation \(r\) of \(0,1,\ldots,6\) separately for each agent. Thus all singleton values are positive. Distinct subsets have different sums of the seven lower-power terms, each in \(\{0,\ldots,127\}\); changing the multiple of \(128\) cannot cancel a difference in those sums. Hence no agent is indifferent between **distinct bundles**. The SPNE can nonetheless have equal payoffs after different **immediate** actions when the final bundle for that mover is the same; the specified tie rule handles these continuation coincidences.

Together the universal six-good lower bound and seven-good SPNE witness establish the claimed sharp boundary.

## Verification

Run `python3 CHECKER.py` in the directory containing `CHECKER.py` and `DP_CERTIFICATE.json`. The checker recomputes \(128\) remaining-set states by independent recurrence and all \(13{,}700\) histories by an independent game-tree recursion, checks the prescribed choice maximizes the mover's continuation payoff at all \(448\) edges and matches the supplied certificate in all components, reconstructs the path and bundles, checks \(128\) distinct bundle values per agent, and verifies the strict \(166\)-unit EF1 violation. Arithmetic is exact integers; no random sampling, solver tolerances, or scientific extrapolation are involved.

The algebraic lower-bound argument covers all finite instances up to six goods; the finite certificate establishes only the explicit seven-good instance and its specified SPNE, not a census of all seven-good profiles or a uniqueness result.

## Relationship to prior work

Goldberg, Hollender, and Tyrovolas [1] formulate the same **online SPNE** mechanism and provide an additive **nine-good instance where every SPNE outcome fails EF1** (their Section 4, Table 3). The present result is a different, sharper **existential** cutoff: an online SPNE already violates EF1 at seven goods, and no smaller instance can. The new lower bound and the exact seven-good witness are not implied by their existence result at nine goods. Crucially, this does **not** replace their stronger all-equilibria property.

Amanatidis et al. [2] study equilibria of **simultaneously submitted rankings followed by offline round-robin**, and exhibit an eight-good counterexample. Their strategy space differs from the contingent sequential strategy space studied here. Therefore their eight-good example or lower bounds about offline reports neither imply nor contradict the seven-good **online** threshold. Earlier strategic sequential picking work [3] analyzes SPNE behavior but not this exact EF1 boundary. This comparison concerns theorem implications, not merely matching title keywords.

## Limitations

The seven-good example proves existence of **one** non-EF1 SPNE, not non-EF1 behavior in all SPNEs. Only three agents, the fixed cyclic turn sequence, complete information, and nonnegative valuations are covered by the sharp cutoff. With more agents or altered sequences the cutoff may differ. The numerical certificate establishes the seven-good outcome only; the universal lower bound is proved analytically. Potential unindexed equivalent constructions remain a publication-priority risk.

## References

[1] P. W. Goldberg, A. Hollender, and G. Tyrovolas, *Equilibria of Round-Robin: Computational Hardness and Fairness for Few Subadditive Agents*, arXiv:2609.18309 (first publicly submitted 2026-09-16), https://arxiv.org/abs/2609.18309 . Primary full text, particularly Sections 2–4 and Table 3.

[2] G. Amanatidis, H. Aziz, G. Birmpas, F. Fusco, S. Leonardi, and R. Reiffenhäuser, *Revisiting the Fairness of Pure Nash Equilibria of Round-Robin*, arXiv:2610.23686 (first publicly submitted 2026-10-16), https://arxiv.org/abs/2610.23686 . Primary full text, Sections 2–4.

[3] T. Kalinowski, N. Narodytska, T. Walsh, and L. Xia, *Strategic Behavior when Allocating Indivisible Goods Sequentially*, AAAI (2013), https://cgi.cse.unsw.edu.au/~tw/knwxaaai13.pdf . Supporting antecedent on online strategic picking.
