# Tutte–Coxeter majority dynamics: eighteen graph types and a four-step clock

## Finding

For synchronous binary open-neighbor majority dynamics on the 30-vertex Tutte–Coxeter graph (the Tutte eight-cage), let \(F:\{0,1\}^{30}\to\{0,1\}^{30}\) be the global update map. The exact, sharp universal identity is
\[
F^6=F^4,\qquad F^5\ne F^3.
\]
Thus every configuration first enters a fixed point or a primitive temporal two-cycle after at most **four** updates. There are exactly **2,386 fixed configurations** and **2,845,305 primitive temporal two-cycle orbits** (so 5,692,996 initially periodic configurations). Spatial symmetry and bit complementation are **not** quotiented in these labelled counts.

The following table is the complete first-periodic-entry census, resolved by eventual least temporal period. Each entry is an exact integer count of initial configurations; the sum is \(2^{30}=1,073,741,824\).

| First periodic entry \(t\) | Eventual period 1 | Eventual period 2 | All configurations |
| ---: | ---: | ---: | ---: |
| 0 | 2,386 | 5,690,610 | 5,692,996 |
| 1 | 261,646 | 276,554,222 | 276,815,868 |
| 2 | 1,108,080 | 351,826,320 | 352,934,400 |
| 3 | 9,757,440 | 170,929,920 | 180,687,360 |
| 4 | 28,072,800 | 229,538,400 | 257,611,200 |
| **Total** | **39,202,352** | **1,034,539,472** | **1,073,741,824** |

A structural refinement identifies exactly **18** isomorphism types of six-vertex simple graphs among the recurrent duad-shore symbols (out of the **156** simple-graph isomorphism types on six vertices). Their orbit-size distribution under six-symbol relabelling is: two types of size 1, two of size 10, four of size 60, two of size 72, two of size 90, two of size 180, and four of size 360. The weighted total is \(2,386\). These are **shore-symbol** classes, not claimed to be the geometric orbit classes of the full 30-vertex system.

## Assumptions and scope

Write \(U=\{1,2,3,4,5,6\}\). A *duad* is one of the 15 two-subsets of \(U\); a *syntheme* is one of the 15 partitions of \(U\) into three duads (perfect matchings of the complete six-vertex graph). The graph has one vertex for each duad and each syntheme; a duad is adjacent precisely to the three synthemes containing it. Every syntheme similarly has three duad neighbors. This is the standard incidence model of the Tutte–Coxeter graph, which has 30 vertices, 45 edges and girth 8 [1].

Each of the 30 vertices has an opinion in \(\{0,1\}\). At each synchronous time step, a vertex adopts opinion 1 iff at least two of its three neighbors have opinion 1, and opinion 0 otherwise. There are no ties or self-neighbor votes. A configuration first enters periodic behavior at the least nonnegative \(t\) such that \(F^{t+2}(x)=F^t(x)\). An orbit's temporal rotations are identified only when counting primitive two-cycle orbits.

## Proof

**1. Incidence factorization.** Represent a duad-shore state by a subset \(A\) of the 15 duads, and a syntheme-shore state by a subset \(B\) of the 15 synthemes. Define \(\Phi(A)\) as the set of synthemes containing at least two duads from \(A\), and \(\Psi(B)\) as the set of duads belonging to at least two synthemes from \(B\). The full update is exactly
\[
F(A,B)=(\Psi(B),\Phi(A)).
\]
Let \(G=\Psi\circ\Phi\) act on duad subsets, and \(J=\Phi\circ\Psi\) act on syntheme subsets. Thus \(F^2(A,B)=(G(A),J(B))\), and more generally \(F^{2r}(A,B)=(G^r(A),J^r(B))\).

**2. Exhaustive but finite projection lemma.** The full space on either shore has \(2^{15}=32,768\) members. Both independent verification implementations enumerate every one of those members, construct the 15 incidence triples directly from the six-symbol definition, and verify the exact identities
\[
G^3=G^2,\qquad J^3=J^2,\qquad G^2\ne G.
\]
They separately find
\[
|\operatorname{Fix}(G)|=|\operatorname{Fix}(J)|=2,386.
\]
An independently checkable stratification of the first count by the number of duads chosen is:

| Number of selected duads | 0 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 15 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Stable subsets | 1 | 90 | 132 | 430 | 540 | 540 | 430 | 132 | 90 | 1 |

There are no other stable duad-set sizes. As an additional classification certificate, relabelling the six base symbols partitions all 32,768 duad subsets (all simple graphs on six labelled vertices) into exactly 156 orbits; precisely 18 are entirely fixed under \(G\), in the orbit-size distribution stated above. The code checks all 720 base-symbol permutations on each orbit representative, and verifies invariance of fixedness under relabelling. All identities and counts are finite exact computations, not extrapolations.

**3. Recurrent swap and period counts.** The two projection identities imply \(F^6=F^4\), so every trajectory is ultimately period one or two. A state is initially periodic iff \(A\in\operatorname{Fix}(G)\) and \(B\in\operatorname{Fix}(J)\). If \(A\) is fixed by \(G\), then \(\Phi(A)\) is fixed by \(J\), and \(\Psi\) is its inverse. Consequently the periodic configurations can be written uniquely as \((A,\Phi(C))\), with \(A,C\in\operatorname{Fix}(G)\), and
\[
F(A,\Phi(C))=(C,\Phi(A)).
\]
The map swaps two symbols from a set of size 2,386. It therefore has exactly 2,386 fixed configurations and \(\binom{2386}{2}=2,845,305\) primitive two-cycles. This also proves there are no other temporal periods.

**4. Exact entrance-time counts and eventual period.** For each \(t=0,1,2,3,4\), let \(a_t\) be the number of initial duad-shore states whose evolving coordinate after \(t\) updates belongs to the fixed set of the appropriate two-step map (\(G\) at even \(t\), \(J\) at odd \(t\)). Define \(b_t\) analogously for the opposite shore. Direct exhaustive evaluation of the two independent 15-bit maps yields
\[
(a_t)_{t=0}^4=(b_t)_{t=0}^4=(2386,16808,25208,28568,32768).
\]
The two evolving coordinates depend on disjoint initial shores. Thus exactly \(a_tb_t\) initial configurations have become periodic by update \(t\); successive differences give the last column of the table.

For the period-one refinement, define the final shore projections \(\pi_G=G^2\) and \(\pi_J=J^2\). Put \(u_t(A)\) for the indicator that the duad-origin coordinate has become two-step fixed at time \(t\), and define \(v_t(B)\) for the syntheme-origin coordinate. Let
\[
X_t(s)=\#\{A:\pi_G(A)=s,\ u_t(A)=1\},\qquad
Y_t(s)=\#\{B:\pi_J(B)=\Phi(s),\ v_t(B)=1\},
\]
for fixed \(s\in\operatorname{Fix}(G)\). The number of initial states reaching eventual period one by time \(t\) is \(\sum_sX_t(s)Y_t(s)\), because eventual equilibrium requires the two projected phases to match. The exact values from exhaustive shore enumeration are
\[
(2386,264032,1372112,11129552,39202352).
\]
Successive differences give the period-one column. Subtracting from the all-period first-entry column gives the period-two column. Both standalone checkers independently reproduce all five numbers.

**5. Sharpness.** One explicit initial state has duad subset \(\{13,15,23,24\}\) and no selected synthemes. Its first periodic entry is update four; direct substitution into the incidence maps verifies that it is not two-periodic at update three. Hence \(F^5\ne F^3\). In fact, 257,611,200 initial states attain the fourth entry step.

## Verification

The package contains `check_duad_syntheme.py`, `check_vertex_dynamics.py`, and their respective captured text outputs. Both use only the Python 3 standard library. Run `python3 check_duad_syntheme.py` and `python3 check_vertex_dynamics.py` in the extracted file directory. The first checker constructs all synthemes recursively, verifies the two exact projection identities on every 15-bit state, enumerates all six-symbol relabelling classes, and verifies all numerical claims. The second independently constructs the 30-vertex adjacency list from ordered permutations, verifies girth eight and the exact same census via explicit neighbor votes, and cross-checks 12,032 direct 30-bit update configurations. These independent samples are supplementary: **the proof for all \(2^{30}\) configurations is the exhaustive shore factorization**, not an unperformed billion-state scan.

## Relationship to prior work

The classical Goles–Olivos theorem supplies eventual period at most two for finite symmetric threshold networks [2]. Benjamini and coauthors [3] likewise state and use that general fact; Kaaser, Mallmann-Trenn and Natale [4] study worst-case voting time on broad graph families. Neither gives this graph's sharp four-update identity or the 30-vertex census. Baez [1] explains the six-symbol duad–syntheme model, but does not investigate voting dynamics.

A previously published result on the Heawood graph [5] uses a related point–line incidence factorization, with a 58-symbol **idempotent** shore projection and a sharp two-update cutoff. That result is not being reasserted. Here the Tutte–Coxeter projection is not idempotent, has 2,386 recurrent symbols, requires two two-step projections, and gives a distinct sharp four-update entrance-time distribution. No general consequence of the Heawood calculations supplies these 18 graph-isomorphism classes or the enumerated phase basins.

## Limitations

The classification is specific to the labelled Tutte–Coxeter graph and its deterministic strict-neighbor binary majority rule. It does not imply the same four-step bound on every cubic graph or every generalized-quadrangle incidence graph. Exact finite enumeration is a proof here because it checks **every** possible state on each 15-vertex shore; sample global trajectories alone would not suffice. Broader historical priority remains qualified: differently indexed or unpublished graph-specific enumerations may exist. Independent external validation has not been performed.

## References

1. John C. Baez, *Tutte–Coxeter Graph*, Visual Insight, 2015-08-15, https://math.ucr.edu/home/baez/visual_insight/20150815%20-%20Tutte-Coxeter%20Graph.html .
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, first submitted 2014-05-11, https://arxiv.org/abs/1405.2486 .
4. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first submitted 2015-08-14, https://arxiv.org/abs/1508.03519 .
5. *A two-step majority projection and exact attraction basins on the Heawood graph*, scientific result and reproducible files, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 .
