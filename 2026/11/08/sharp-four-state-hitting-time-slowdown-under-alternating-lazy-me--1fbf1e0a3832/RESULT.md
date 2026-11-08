# Sharp four-state hitting-time slowdown under alternating lazy Metropolis walks

## Finding

**Theorem (sharp four-state periodic slowdown).** Let \(n\in\{2,3,4\}\), \(V=\{0,1,\ldots,n-1\}\), and let \(G,H\) be any connected simple undirected graphs on \(V\). On each graph use the lazy Metropolis random walk: for distinct vertices \(u,v\),
\[
P_G(u,v)=\begin{cases}
\bigl(2\max\{\deg_G(u),\deg_G(v)\}\bigr)^{-1},&\{u,v\}\in E(G),\\
0,&\text{otherwise},
\end{cases}
\qquad P_G(u,u)=1-\sum_{v\ne u}P_G(u,v).
\]
Let \(T_{G,H}(s,t)\) be the expected number of discrete steps to first visit \(t\), starting from \(s\ne t\), when the successive transition matrices are \(P_G,P_H,P_G,P_H,\ldots\). For a fixed graph, write \(T_G(s,t)=T_{G,G}(s,t)\). Define
\[
R_n=\max_{G,H\ \text{connected}}\ \max_{s\ne t}\frac{T_{G,H}(s,t)}{\max\{T_G(s,t),T_H(s,t)\}}.
\]
The maxima include both alternation phases since \(G,H\) are ordered. Then
\[
\boxed{R_2=R_3=1,\qquad R_4=\frac{646}{607}.}
\]
Thus strict degradation relative to *each* static walk first occurs on four vertices. In a complete exact census, the four-vertex maximum is attained with a four-cycle and a triangle-with-one-leaf (a paw), and its slowdown is \(39/607\), or approximately \(6.43\%\), relative to the larger static mean.

## Assumptions and scope

Both graphs have the identical labeled vertex set; edges may change every step but every graph appearing is connected. Time starts at zero, the initial vertex differs from the fixed target, and the first transition uses \(G\). Graphs have no loops or multiple edges; the diagonal holding probability is part of the random-walk transition rule. The comparison uses the *same ordered start-target pair* in both static chains, not the maximum over all pairs. The theorem does not assert anything about other graph orders, other kernels, random switching schedules, or global cover times.

Every \(P_G\) is symmetric, has uniform stationary distribution, and satisfies \(P_G(u,u)\ge 1/2\), so the phenomenon occurs even with a common stationary law and genuine laziness.

## Proof

**1. Absorbing equations.** Fix the target \(t\). Delete its row and column from the transition matrices, obtaining substochastic matrices \(A\) and \(B\) indexed by \(V\setminus\{t\}\). Let \(a_u\) and \(b_u\) be expected hitting times from non-target vertex \(u\) when the first transition uses \(G\), respectively \(H\). First-step conditioning gives
\[
a=\mathbf1+Ab,\qquad b=\mathbf1+Ba,
\]
and therefore
\[
(I-AB)a=\mathbf1+A\mathbf1,\qquad
b=\mathbf1+Ba.
\]
For a single fixed graph, the equation is \((I-A)h=\mathbf1\). These formulas uniquely determine finite expectations. To justify invertibility, take any vertex and a path of length at most \(n-1\) to \(t\) in \(G\). A positive-probability trajectory follows this path during successive \(G\)-phases, staying in place during intervening \(H\)-phases (diagonal probabilities at least \(1/2\)). The finite state space gives a uniform positive absorption probability within \(2(n-1)\) steps; the same holds starting in the other phase using a path in \(H\). Thus the killed two-phase chain has spectral radius below one and all equations are nonsingular.

**2. An attaining pair.** On \(V=\{0,1,2,3\}\), take
\[
E(G)=\{\{0,1\},\{0,2\},\{1,3\},\{2,3\}\},\quad
E(H)=\{\{0,2\},\{1,2\},\{1,3\},\{2,3\}\}.
\]
Thus \(G\) is a four-cycle and \(H\) has a triangle on vertices \(1,2,3\) and a leaf \(0\) attached to \(2\). For target \(t=3\), in non-target order \((0,1,2)\), the exact kernels are
\[
P_G=\begin{pmatrix}1/2&1/4&1/4&0\\1/4&1/2&0&1/4\\1/4&0&1/2&1/4\\0&1/4&1/4&1/2\end{pmatrix},
\quad
P_H=\begin{pmatrix}5/6&0&1/6&0\\0&7/12&1/6&1/4\\1/6&1/6&1/2&1/6\\0&1/4&1/6&7/12\end{pmatrix}.
\]
The displayed absorbing equations give
\[
a=\frac1{607}(5538,3876,4236)^\top,
\qquad b=\frac1{607}(5928,3574,4294)^\top.
\]
The two *static* target-hitting vectors, in the same order, are
\[
h_G=(8,6,6)^\top,\qquad h_H=(15,6,9)^\top.
\]
Starting at \(s=1\) and using \(G\) first gives \(T_{G,H}(1,3)=3876/607\), while both \(T_G(1,3)\) and \(T_H(1,3)\) equal \(6\). Hence the ratio is \((3876/607)/6=646/607\).

**3. Exact complete finite upper bound and minimality.** The accompanying standalone `verify.py` exhausts every labeled simple graph on \(n\in\{2,3,4\}\) vertices: represent the \(\binom n2\) possible edges by binary masks and retain exactly the connected graphs. The resulting counts are respectively \(1,4,38\). For each unordered pair of connected graphs, every target, every different start, and *both* initial phases, solve the rational absorbing equations above and compare against the two static values. Interchanging the graph order only interchanges the two initial phases, so this exhausts every ordered graph pair.

Exact `fractions.Fraction` arithmetic, pivoting elimination and substitution residual checks avoid numerical ambiguity. The complete census has respectively \(4,120,17784\) phase/start/target cases in orders \(2,3,4\). The numbers of cases with ratio strictly above \(1\) are \(0,0,168\); the maximal ratios are respectively \(1,1,646/607\). There are \(24\) attaining labeled phase cases in order four. The script independently reconstructs the witness with a full six-state, two-phase absorbing system (rather than relying only on the reduced three-state equation). For order three, the four labeled graphs comprise three paths and one triangle. Pairing two distinct paths gives maximal ratio \(2/3\), while any pair including a repeated graph or a triangle has maximal ratio \(1\). Thus the stated extrema are exhaustive and exact.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The script prints `VERIFY_OK` after checking graph connectivity, transition-matrix symmetry and laziness, rational linear-system residuals, all \(17784\) four-vertex comparison cases, exact extremal multiplicities, and the independent augmented-system witness. The completed replay produced

`VERIFY_OK [(2, 1, 4, 0, Fraction(1, 1), 0), (3, 4, 120, 0, Fraction(1, 1), 0), (4, 38, 17784, 168, Fraction(646, 607), 24)] witness=3876/607 > 6; ratio=646/607`

The calculation is an exhaustive **finite** proof of these three fixed vertex orders, not evidence about larger graphs.

## Relationship to prior work

Shimizu and Shiraga, *Reversible Random Walks on Dynamic Graphs* (arXiv:2102.08002, initial public posting 2021-02-16), define the same lazy Metropolis kernel in their Equation (3) and prove universal hitting and mixing bounds for time-varying reversible kernels with a common stationary distribution. Their reported results do not specify a graph-order threshold or an exact maximum of the pointwise ratio to both static target-hitting times. Sauerwald and Zanetti, *Random Walks on Dynamic Graphs: Mixing Times, Hitting Times, and Return Probabilities* (arXiv:1903.01342, 2019), provide dynamic-graph hitting-time bounds and compare behavior with static graph settings; their asymptotic bounds do not imply this exact small-graph ratio. The static Metropolis-hitting literature by Nonaka et al. (2010) addresses fixed kernels and hence does not settle a two-phase comparison. The shared-stationary-law property and general dynamic upper bounds are **not** claimed as new.

## Limitations

The classification is exact only for orders two through four. It does not assert an asymptotic ratio bound, uniqueness up to graph isomorphism of all maximizing pairs, persistence for nonperiodic schedules, or any analogous result for simple rather than Metropolis walks. The maximal slowdown on four vertices is small but strict. Priority is based on targeted comparisons with accessible prior publications and mathematical search results and is not independently adjudicated.

## References

1. N. Shimizu and T. Shiraga, *Reversible Random Walks on Dynamic Graphs*, arXiv:2102.08002 (first posted 2021-02-16), https://arxiv.org/abs/2102.08002. See Sections 1.2 and 4, particularly Equation (3).
2. T. Sauerwald and L. Zanetti, *Random Walks on Dynamic Graphs: Mixing Times, Hitting Times, and Return Probabilities*, arXiv:1903.01342 (2019), https://arxiv.org/abs/1903.01342. See Introduction and results on hitting-time bounds.
3. Y. Nonaka, H. Ono, K. Sadakane and M. Yamashita, *The hitting and cover times of Metropolis walks*, Theoretical Computer Science 411 (2010), 1889–1894, https://doi.org/10.1016/j.tcs.2010.01.032.
