# Exact extinction basin on cocktail-party graphs under three-state excitation

## Finding

**Theorem (all-size extinction law).** Let \(r\ge4\), and let \(G_r=K_{2,\ldots,2}\) be the labelled graph on \(2r\) vertices obtained from \(K_{2r}\) by deleting the \(r\) edges of a fixed perfect matching. Starting from a configuration in \(\{0,1,2\}^{2r}\), apply the synchronous threshold-one three-state Greenberg–Hastings rule: \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) if and only if some neighbor is currently in state \(1\), otherwise \(0\mapsto0\).

The trajectory reaches the all-zero configuration if and only if the initial configuration has **no rainbow triangle** (a triangle with all three states \(0,1,2\)). The exact number of labelled initial configurations that go extinct is
\[
\boxed{Z_r=3\cdot4^r-3+6r.}
\]
Under independent uniform initial states, the extinction probability is consequently
\[
\boxed{\Pr(\mathrm{extinction})=3(4/9)^r+(6r-3)/9^r,}
\]
with the sharp asymptotic \(\Pr(\mathrm{extinction})\sim3(4/9)^r\). The correction \(6r\) counts the initial colorings that use all three states but fail to contain a rainbow triangle: one matched pair uses two distinct states, and every other matched pair is monochromatic in the third state.

The number of configurations that **eventually** enter a nonzero periodic orbit is the complementary count
\[
\boxed{B_r=9^r-3\cdot4^r+3-6r.}
\]
The conclusion that every such trajectory eventually reaches a primitive three-cycle is an earlier published result for this same graph family; it is used here, **not claimed as new**. Likewise the earlier published count of immediately periodic configurations is not claimed as new. The new exact count concerns the entire **basin**, including transient initial states, which is not determined by the number of periodic configurations.

## Definitions, scope, and prior results

The graph has matched vertex pairs \(\{a_j,b_j\}\), \(1\le j\le r\); two distinct vertices are adjacent precisely when they belong to different pairs. All configurations are individually labelled. Extinction means that the forward orbit eventually reaches the unique fixed configuration \(0^{2r}\), not just that the time-average excitation vanishes. The result holds for every integer \(r\ge4\), with no extrapolation from computations.

We use the graph-general three-state Greenberg–Hastings circulation theorem of Gravner, Lyu and Sivakoff (2018, Theorem 3), which characterizes eventual synchronization by the vanishing of an integer edge one-form on every graph cycle. It is an established premise. The published result *Three-state excitation on cocktail-party graphs: a sharp period transition and exact orbit count* (November 2, 2026) already proves that on this graph family with \(r\ge3\), all nonzero periodic orbits have primitive period three and counts those orbits exactly. Its theorem and proof are credited, not repeated as an original classification. The case \(r=3\) also lies within a previously published complete-tripartite extinction census.

## Proof

**1. Rainbow triangles detect the circulation obstruction.** For an initial colouring \(x\), assign the oriented edge \((u,v)\) the antisymmetric integer weight
\[
\omega_x(u,v)=\begin{cases}1,&(x(u),x(v))=(0,1),\\-1,&(x(u),x(v))=(1,0),\\0,&\text{otherwise}.\end{cases}
\]
By the cited circulation theorem, the GHM process synchronizes if and only if the sum of \(\omega_x\) is zero around every cycle. Any triangle has nonzero circulation precisely when its three vertices carry the three different states; in that case its circulation is \(\pm1\).

In any complete multipartite graph with at least three nonempty parts, a chordless simple cycle is a triangle or a quadrilateral alternating between two parts. Such a quadrilateral is the signed sum of the four triangles obtained by coning to a vertex of a third part. Chord decomposition therefore expresses every cycle as an integer combination of triangles. Consequently all circulations vanish if and only if no rainbow triangle exists. The cited theorem then implies that the trajectory synchronizes. Under this particular GHM rule, a spatially constant state evolves through refractory and resting states to all zero, so synchronization implies extinction. A rainbow triangle has nonzero circulation and prevents extinction. This establishes the claimed equivalence.

**2. Exact Hall-obstruction classification.** For each matched pair \(j\), let \(S_j\subseteq\{0,1,2\}\) be its one- or two-element set of occupied colors. A rainbow triangle is equivalent to selecting three *different* pairs, one containing color \(0\), another color \(1\), and a third color \(2\). By Hall's theorem, this is possible exactly when the three color-candidate sets admit a system of distinct pair representatives.

If at least one state is wholly absent, no rainbow triangle exists. There are exactly \(3\cdot2^{2r}-3=3\cdot4^r-3\) such colorings, by inclusion–exclusion. Suppose all three states occur but no rainbow triangle exists. Every one of the \(r\) matched pairs contains at least one state, so the candidate union for the three colors comprises all \(r\ge4\) pairs; no three-color Hall obstruction is possible. A one-color Hall obstruction is impossible because all colors occur. Thus a two-color Hall obstruction is necessary and sufficient: some two colors occur only within one matched pair. That pair necessarily consists of these two colors, one on each vertex; all remaining matched pairs must be monochromatic in the third color. Conversely each such coloring has no rainbow triangle.

There are exactly \(3\) choices for the monochromatic color of the remaining pairs, \(r\) choices for the exceptional matched pair, and \(2\) assignments of the other two colors to its two labelled vertices, giving \(6r\) colorings. The exceptional matched pair and remaining monochromatic color are unique when \(r\ge4\), so there is no double-counting. Hence \(Z_r=3\cdot4^r-3+6r\).

**3. Complement and sharp probability.** There are \(3^{2r}=9^r\) labelled configurations. The remainder of the configuration space does not go extinct and, by the cited earlier complete family-specific temporal classification, eventually enters a nonzero three-cycle. Thus \(B_r=9^r-Z_r\). Dividing by \(9^r\) gives the displayed exact probability. Since \((6r-3)/9^r=o((4/9)^r)\), its asymptotic equivalence follows. No first-entry-time histogram is asserted.

## Verification and reproducibility

The original package's `census.cpp` and `independent_check.py` directly enumerate the finite dynamical systems and rainbow-triangle obstructions. They agree with the basin formula through the tested sizes, but finite computations do not establish the theorem for arbitrary \(r\). As an additional separate check, a fresh exhaustive inspection of all labelled initial states for \(r=3,4,5\) found extinction-basin counts \(207,789,3099\) respectively, agreeing with \(3\cdot4^r-3+6r\); the \(r=3\) check is a prior-covered boundary. The unrestricted result follows from the cycle-space reduction and Hall argument above. Periodic-orbit numbers in the original verification outputs remain valid as checks of the established earlier theorem, not an originality claim.

## Relationship to prior work and limits

Gravner, Lyu and Sivakoff prove the general finite-graph synchronization/circulation criterion used in Step 1. The November 2, 2026 complete cocktail-party dynamics theorem already gives primitive periods and exact temporal-cycle populations for every \(r\ge3\); both the claim and proof were compared in full. The October 26, 2026 complete-tripartite extinction theorem establishes a stronger first-hitting-time distribution for three-part graphs and covers \(r=3\), not arbitrary \(r\ge4\). None of those inspected results states or, without a family-specific counting argument, directly gives the all-size \(6r\) Hall-obstruction correction for the *extinction basin* of \(K_{2,\ldots,2}\). Novelty is asserted only for that natural unbounded-family population count and its resulting exact probability and complement.

This work does not claim a new graph-general dynamical theorem, a new primitive-cycle count, or an exact first-hitting-time distribution. Historical priority remains best-of-knowledge; unindexed equivalent color-obstruction counts may exist. The original journal model introductions were not exhaustively reexamined. An exact graph-family Hall count is a restricted but useful finite-network reliability invariant, distinct from a temporal-cycle census.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, Annals of Applied Probability **28** (2018), 3324–3357, Theorem 3. https://arxiv.org/abs/1610.07320 ; full authors' paper https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
2. *Three-state excitation on cocktail-party graphs: a sharp period transition and exact orbit count*, published November 2, 2026. https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-three-state-excitation-on-cocktail-party-graphs-a-sharp-period-t--b65add71b337/RESULT.md .
3. *Exact four-layer extinction-basin spectrum for three-state excitation on complete tripartite graphs*, published October 26, 2026. https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-exact-four-layer-extinction-basin-spectrum-for-three-state-excit--8e00ec0e0205/RESULT.md .
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126. https://content.wolfram.com/uploads/sites/13/2018/09/27-2-1.pdf .
