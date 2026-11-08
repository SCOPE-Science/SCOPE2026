# A single missing spoke creates an exact intermediate excitation phase on wheels

## Finding
Let \(H_n\), for every integer \(n\ge4\), be a wheel on a labelled rim \(v_0,v_1,\ldots,v_{n-1}\) and hub \(h\), with **the one edge \(hv_0\) removed**. For either synchronous three-state cyclic cellular automaton (CCA) or synchronous three-state threshold-one Greenberg–Hastings (GHM) dynamics, the asymptotic excitation rate is restricted to exactly three possible values:

\[
\alpha_{\mathrm{CCA}}\in\{0,3/4,1\},\qquad
\alpha_{\mathrm{GHM}}\in\{0,1/4,1/3\},\qquad
\alpha_{\mathrm{CCA}}=3\alpha_{\mathrm{GHM}}
\]
for the **same initial colouring**. The quantity \(\alpha_{\mathrm{CCA}}\) is the limiting proportion of time steps at which any fixed vertex advances its colour; \(\alpha_{\mathrm{GHM}}\) is the limiting proportion of steps at which any fixed vertex changes from state \(0\) to state \(1\). For finite connected graphs, these limits are common to all vertices, by the finite-graph activity theorem cited below.

Define the integer sequence \(q_0=q_1=2\), \(q_{j+2}=2q_{j+1}+q_j\) for \(j\ge0\). For each rate, the exact number of *labelled initial* colourings is

\[
\begin{aligned}
N_0(n)&=\tfrac92q_{n-2}+6q_{n-1}+6,\\
N_{\mathrm{mid}}(n)&=3q_{n-1}-6,\\
N_{\mathrm{high}}(n)&=3^{n+1}-\tfrac92q_{n-2}-9q_{n-1}.
\end{aligned}
\]
Here the middle rate is \(3/4\) for CCA and \(1/4\) for GHM, while the high rate is \(1\) for CCA and \(1/3\) for GHM. These three disjoint sets partition all \(3^{n+1}\) initial colourings. For the independent uniform initial-colouring law, divide the populations by \(3^{n+1}\).

Let \(E_n\) denote the set of initial colourings with no rainbow triangle among the surviving \(n-2\) hub–rim triangles. The middle-phase conditional fraction has a nonzero limit:
\[
\lim_{n\to\infty}\mathbb P(\alpha=\alpha_{\mathrm{mid}}\mid E_n)
=\frac{1+\sqrt2}{3(3/2+\sqrt2)}
=0.2761423749\ldots.
\]
Thus removal of just one spoke produces a new intermediate excitation regime which is absent on intact wheels. Only excitation-rate classes and their initial populations are claimed; no infinite-family bound on transient lengths or general primitive-period classification is asserted.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The rim is the cycle \(v_0v_1\cdots v_{n-1}v_0\), and the hub is adjacent to precisely \(v_1,\ldots,v_{n-1}\). All states take values in \(\mathbb Z/3\mathbb Z\), with discrete time \(t=0,1,\ldots\); updates are simultaneous at every vertex. For CCA, a vertex of colour \(c\) advances to \(c+1\pmod3\) precisely if a neighbour presently has that successor colour; otherwise it stays. For GHM, \(1\mapsto2\mapsto0\) is unconditional, and \(0\mapsto1\) occurs exactly when at least one neighbour is in state \(1\), otherwise \(0\mapsto0\). Both have contact threshold one. Rates are taken from deterministic trajectories of a fixed initial colouring. The probability statements additionally assume independent, uniform initial states.

## Proof
**1. Cycle integral criterion.** For colours \(a,b\in\{0,1,2\}\), define the antisymmetric oriented-edge increments
\[
 d_C(a,b)=\begin{cases}0&a=b,\\1&b=a+1\pmod3,\\-1&b=a-1\pmod3,\end{cases}
 \quad
 d_G(a,b)=\mathbf1_{(a,b)=(0,1)}-\mathbf1_{(a,b)=(1,0)}.
\]
Gravner–Lyu–Sivakoff, Theorem 3 (arXiv:1610.07320v1; journal version, 2018), proves for either update rule on every finite connected graph: the trajectory synchronizes exactly if all cycle integrals of the corresponding increment vanish, and otherwise its common limiting excitation rate is the maximum **positive** cycle integral divided by the cycle length (over oriented simple cycles). There is also an explicit graph-diameter synchronization bound for the conservative case. This foundational theorem is quoted, not claimed here as new.

The identities
\[
\phi(0)=0,\quad \phi(1)=-2,\quad \phi(2)=-1,\qquad
 d_C(a,b)=3d_G(a,b)+\phi(b)-\phi(a)
\]
hold for each ordered colour pair. Summing around a closed cycle cancels the potential, so every cycle integral for CCA equals three times that for GHM. Hence their rates are in the exact ratio three for the same initial colouring.

**2. Only three activity rates.** The simple cycles in \(H_n\) have a cycle-space generating set comprising its \(n-2\) surviving triangles \((h,v_i,v_{i+1},h)\) for \(1\le i\le n-2\), together with the quadrilateral
\[
Q=(h,v_1,v_0,v_{n-1},h).
\]
This follows directly by replacing any hub-to-hub rim path with the sum of its consecutive triangular wedges and, if it passes through \(v_0\), the quadrilateral \(Q\); the entire rim cycle is obtained similarly. All sums here are oriented integer one-chains, so integrals are additive.

The integral around a triangle is zero unless its three colours are distinct, in which case it equals \(\pm3\) for \(d_C\). If any triangle is rainbow, the directed version with integral \(+3\) has mean \(1\), which is also the maximum possible because each edge increment is at most one. Thus \(\alpha_C=1\).

If all surviving triangles have zero integral, then any simple cycle avoiding \(v_0\) has zero integral. Any simple cycle containing \(v_0\) either is the rim cycle or uses the hub exactly once; its oriented integral equals \(0\) or \(\pm\oint_Qd_C\), because it differs from \(Q\) by a sum of surviving triangles. Its absolute nonzero integral is \(3\). No such simple cycle has fewer than four edges, and \(Q\) itself has four. Therefore if \(\oint_Qd_C\ne0\), the exact maximum mean is \(3/4\); otherwise all cycle integrals vanish, giving rate zero. This proves the CCA classification, with the GHM rates following from the factor-three identity. Each case occurs for some colouring; the positive counts in Step 3 give this for every \(n\ge4\).

**3. Exact counts.** Fix the hub colour to be \(0\), exploiting cyclic colour translation for the combinatorial constraints. A surviving triangle is nonrainbow exactly when its adjacent rim colours do not form the unordered pair \(\{1,2\}\). Thus, on the rim path \(v_1,\ldots,v_{n-1}\), the allowed neighbour transfer is
\[
T=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]
Put \(m=n-2\). The number of allowed path-colourings with endpoint colours \(a,b\) equals \((T^m)_{ab}\). The missing-spoke vertex \(v_0\) has three possible colours. For a fixed pair of endpoints, the number of its colours which give a nonzero quadrilateral integral is the corresponding entry of
\[
B=\begin{pmatrix}0&1&1\\1&0&2\\1&2&0\end{pmatrix}.
\]
For example, with \((a,b)=(1,2)\), either choice \(X(v_0)=1\) or \(X(v_0)=2\) produces signed quadrilateral integral of magnitude three, whereas \(X(v_0)=0\) does not. Direct inspection of the remaining eight endpoint pairs gives \(B\). Define
\[
S_m=\sum_{a,b}(T^m)_{ab},\qquad R_m=\sum_{a,b} B_{ab}(T^m)_{ab}.
\]
The three disjoint counts are therefore
\[
N_0=9S_m-3R_m,\quad N_{\mathrm{mid}}=3R_m,\quad N_{\mathrm{high}}=3^{n+1}-9S_m.
\]
The eigenvalues of \(T\) are \(1+\sqrt2,\ 1-\sqrt2,\ 1\). Diagonalizing in the symmetric and antisymmetric subspaces of the swap \(1\leftrightarrow2\), or applying the characteristic polynomial with the initial matrix values, yields
\[
S_m=\tfrac12q_m+q_{m+1},\qquad R_m=q_{m+1}-2.
\]
Substitution proves all three formulas. Since \(q_m\) is even and \(q_{m+1}\ge6\) for \(m\ge2\), all counts are positive integers. The conditional fraction \(N_{\mathrm{mid}}/(N_0+N_{\mathrm{mid}})=R_m/(3S_m)\) tends to the asserted constant because \(q_j=(1+\sqrt2)^j+(1-\sqrt2)^j\).

## Verification
Three standalone Python 3 programs with captured outputs accompany this result. The direct dynamical program exhaustively evolves every labelled initial state for \(4\le n\le9\), for both update rules, and compares the limiting excitation-rate populations with the formulas. A separately implemented simple-cycle enumerator computes the exact maximum directed cycle-mean for all initial colourings and \(4\le n\le8\), independent of the dynamics simulation. A matrix/recurrence checker proves no infinite statement by itself, but reproduces the integer identities and populations for \(4\le n\le30\). Each is supplied with exact source and output, and can be run without third-party dependencies using `python3 code/<script>.py`.

For orientation, at \(n=4\) the count vector \((N_0,N_{\mathrm{mid}},N_{\mathrm{high}})\) is \((117,36,90)\); at \(n=5\) it is \((273,96,360)\). The proof above is the all-size argument; finite exhaustive checks are not substituted for it.

## Relationship to prior work
The 2016 arXiv manuscript of Gravner, Lyu and Sivakoff established the general three-colour CCA/GHM cycle-integral criterion and the maximum-cycle-mean activity formula for arbitrary finite graphs. This supplies the essential generic dynamics theorem, but does not evaluate the cycle-space and weighted initial-colouring populations of a wheel missing one spoke. Doba (2018) likewise concerns cycle-density control of finite-graph GHM, so generic rate criteria are not claimed to be new here. The mathematical contribution here is the **missing-spoke intermediate rate and its exact, strictly positive census**, including identical initial-state partitions for both different rules and a nonzero conditional asymptotic proportion. The corresponding intact-wheel graph has no intermediate \(3/4\) CCA rate or \(1/4\) GHM rate; an edge deletion changes the support of the asymptotic activity distribution, not merely its normalization.

## Limitations
The conclusion is specific to the finite, simple, undirected, one-spoke-deleted wheel, three states and contact threshold one. It does not claim comparable formulas for multiple missing spokes, thresholds exceeding one, stochastic updating, full eventual orbit periods, transient entry-time populations, or mixing. The full text of Doba's 2018 paper was not available for close comparison, so independent historical-priority review remains advisable. The finite computational checks are corroboration and are not a proof beyond the enumerated sizes. No independent audit is asserted.

## References
1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (public 2016-10-24); *Annals of Applied Probability* 28 (2018), 3324–3357, DOI: 10.1214/17-AAP1350. https://arxiv.org/abs/1610.07320 ; accessible full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf . Theorem 3 and its proof supply the finite-graph cycle-mean criterion.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126, DOI: 10.25088/ComplexSystems.27.2.101. Publisher abstract inspected, full text unavailable for detailed comparison: https://www.complex-systems.com/abstracts/v27_i02_a01/ .
