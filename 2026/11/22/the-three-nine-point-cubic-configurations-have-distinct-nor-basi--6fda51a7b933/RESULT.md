# The three nine-point cubic configurations have distinct NOR basin spectra

## Finding

The three nonisomorphic combinatorial \((9_3)\) point–line configurations have different complete attraction-basin spectra under synchronous open-neighborhood Boolean NOR dynamics on their eighteen-vertex Levi graphs. Their exact data are:

| Configuration | Noncollinearity cycle lengths | Six-cycles in Levi graph | Fixed points | Primitive two-cycles | Initial states attracted to a fixed point | Initial states attracted to a two-cycle | Basin of the empty/full oscillator |
|---|---|---:|---:|---:|---:|---:|---:|
| Pappus | \((3,3,3)\) | 18 | 110 | 5,995 | 914 | 261,230 | 45,797 |
| Switched | \((3,6)\) | 20 | 112 | 6,216 | 912 | 261,232 | 44,945 |
| Cyclic | \((9)\) | 21 | 113 | 6,328 | 911 | 261,233 | 44,522 |

There are \(2^{18}=262{,}144\) initial Boolean states per graph. Every trajectory enters its final orbit after **at most one synchronous update**, and the bound is attained on all three graphs. The **entire individual-attractor basin-size histogram**, not just the aggregate counts in the table, is specified without omissions in `EXPECTED_COUNTS.json`. In particular, the three types are separated by their fixed-point and two-cycle basin spectra, and the total fixed-attraction population decreases, \(914>912>911\), while the fixed-point count increases, \(110<112<113\).

## Assumptions and scope

A combinatorial \((9_3)\) configuration consists of nine labelled points \(P=\{0,\ldots,8\}\) and nine labelled lines \(L=\{0,\ldots,8\}\), with three incidences per point and line and at most one line incident to any pair of distinct points. Its Levi graph has vertex set \(P\sqcup L\) and exactly the incidence edges; points and lines are distinct shores. The three sets of nine explicit point triples defining the lines are listed in `CONFIGURATIONS.json` and are part of the claim.

For a Boolean vertex configuration, a vertex is occupied at the next step if and only if **none of its three graph neighbors** is occupied at the current step. There are no self-loops, boundary vertices, probabilistic updates, or tie-breaking rules. A *basin* is the collection of all initial states whose eventual temporal attractor is one specified fixed point or primitive two-cycle, including its recurrent states. The *first-entry time* is the smallest nonnegative number of updates until the state is periodic.

The three configurations represent the three known combinatorial isomorphism types of \((9_3)\) configurations. They are inequivalent directly: their point noncollinearity graphs have respective component cycle lengths \((3,3,3)\), \((3,6)\), and \((9)\); their Levi graphs also have respectively 18, 20, and 21 six-cycles. The published enumeration of combinatorial configurations supplies exhaustiveness of the three types [1]. At the smaller feasible orders \(n=7\) and \(n=8\), there is only one combinatorial \((n_3)\) type [1]. No assertion is made about more general incidence graphs or update rules.

## Proof

**One-update projection.** For a point set \(A\subseteq P\), define \(\alpha(A)\subseteq L\) to be the lines disjoint from \(A\). For a line set \(B\subseteq L\), define \(\beta(B)\subseteq P\) to be the points incident with none of \(B\). The synchronous map is exactly
\[
F(A,B)=(\beta(B),\alpha(A)).
\]
The disjointness equivalence
\[
B\subseteq\alpha(A)\quad\Longleftrightarrow\quad A\subseteq\beta(B)
\]
is an antitone Galois connection, implying \(\alpha\beta\alpha=\alpha\) and \(\beta\alpha\beta=\beta\). Indeed, extensivity of \(\beta\alpha\) and antitonicity of \(\alpha\) give \(\alpha\beta\alpha(A)\subseteq\alpha(A)\); applying the equivalence to \(B=\alpha(A)\) gives the reverse inclusion. The second identity is dual. Therefore
\[
F^3(A,B)=\big(\beta\alpha\beta(B),\alpha\beta\alpha(A)\big)=F(A,B).
\]
Every point in the image of \(F\) consequently has period dividing two, and all states enter recurrence in at most one step.

**The recurrent symbols and their fibers.** Let \(I_L=\operatorname{Im}\alpha\) and \(I_P=\operatorname{Im}\beta\). The two Galois identities make \(\alpha:I_P\to I_L\) and \(\beta:I_L\to I_P\) mutual inverse bijections. Put \(r=|I_L|=|I_P|\). The full recurrent set is \(I_P\times I_L\), having \(r^2\) states, and \(F\) acts on it as a flip of its two concept symbols. It has precisely \(r\) fixed points and \(\binom r2\) primitive two-cycle orbits. The three direct nine-point subset enumerations in `verify_closure.py` give respectively \(r=110,112,113\). Thus the orbit counts in the first table are exact.

**All individual attraction basins.** For every \(l\in I_L\) and \(p\in I_P\), define integer fibers
\[
u(l)=|\{A\subseteq P:\alpha(A)=l\}|,\qquad
v(p)=|\{B\subseteq L:\beta(B)=p\}|.
\]
These fibers are computed independently over all \(2^9\) subsets per shore. Any recurrent state \(y=(p,l)\in I_P\times I_L\) has exactly \(v(p)u(l)\) initial predecessors under one update. Since every initial state enters recurrence after that update, if \(F(y)=y\), its fixed-point basin size is \(v(p)u(l)\). Otherwise the basin of \(\{y,F(y)\}\) has size
\[
v(p)u(l)+v(\beta(l))u(\alpha(p)).
\]
Enumerating the finite sets \(I_P\) and \(I_L\) and applying these **proved** formulas yields the individual histograms and aggregate counts in `EXPECTED_COUNTS.json`. They sum to exactly \(2^{18}\) for every graph. The alternating empty/full orbit has basin \(u(\varnothing)v(\varnothing)+u(L)v(P)\), producing the three values in the table.

**Nonisomorphism and scope completion.** Checking incidence in each of the nine listed triples shows every point and line has degree three and distinct lines meet in at most one point. Pairwise noncollinearity forms a two-regular graph on nine points; counting its component sizes gives the three distinct patterns stated above, which are isomorphism invariants even under point/line duality when combined with the distinct Levi six-cycle counts. The known three-type classification [1] therefore identifies a representative of every combinatorial \((9_3)\) type. The bound of one step is sharp because \(r^2<2^{18}\) for each type, so some states are not initially recurrent.

## Verification

The standalone scientific data and scripts are `CONFIGURATIONS.json`, `EXPECTED_COUNTS.json`, `verify_closure.py`, and `verify_direct.py`. From their common directory, execute `python3 verify_closure.py` and `python3 verify_direct.py`; they use the Python standard library. Their corresponding complete recorded outputs are `closure_output.txt` and `direct_output.txt`.

The closure checker enumerates \(512\) point subsets and \(512\) line subsets per graph, explicitly checks \(\alpha\beta\alpha=\alpha\) and \(\beta\alpha\beta=\beta\), constructs all basin histograms by the proved formulas, and checks incidence and noncollinearity invariants. The structurally separate direct checker constructs all eighteen adjacency lists, performs per-vertex NOR on all \(262{,}144\) initial configurations per graph, independently verifies \(F^3=F\), and enumerates every fixed point, primitive two-cycle, and its entire basin by direct successor tracing. Both checkers agree on every shared count. Their finite exhaustive computations establish all claimed integers for the three **fixed specified** graphs, not a statement about arbitrary graph orders.

## Relationship to prior work

Bokowski and Pilaud [1] give the existing enumeration of the combinatorial \((n_3)\) incidence configurations, including exactly three types at order nine; that classification is used rather than claimed as new. The general AND–OR–NAND–NOR fixed-point enumeration of [2] supplies pre-existing broader fixed-point methods, so the general concept-closure principle, the mere existence of equilibria, and counting formulas for fixed points alone are **not** presented as innovations. The specifically claimed finite result is the **entire periodic-orbit and individual basin distribution** for each of the three earliest inequivalent cubic point–line configurations, including their contrasted fixed-attraction totals. Earlier computations of majority dynamics on the Pappus graph and of NOR dynamics on other graph families concern different maps or different incidence structures; their assertions do not determine this complete census. The accessible literature examined did not identify a previously published covering table or an equivalent full basin distribution for these three NOR systems. That search is not a proof of historical uniqueness.

## Limitations

The exact census depends on the incidence triples as supplied and is computationally exhaustive only for these three graphs. The antitone Galois argument proves the one-update transient bound for any bipartite incidence graph, but the reported numerics and inequalities are not asserted for arbitrary incidence graphs. Published fixed-point theory may already imply some of the fixed counts after specialization; those counts are accompanying data, not a stand-alone novelty claim. Comprehensive historical priority and independent external reproduction remain unestablished. One relevant fixed-point article was inspected through accessible article text rather than an unrestricted downloaded full PDF; unseen tables or equivalent work remain a priority risk.

## References

[1] Jürgen Bokowski and Vincent Pilaud, *Enumerating topological \((n_k)\)-configurations*, arXiv:1210.0306 (first public version October 1, 2012), https://arxiv.org/abs/1210.0306 .

[2] *Exact enumeration of fixed points of AND-OR-NAND-NOR Boolean networks*, *Chaos, Solitons & Fractals* **195** (2025), article 116182, https://doi.org/10.1016/j.chaos.2025.116182 .

[3] Aracena, Richard, and Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, *Journal of Computer and System Sciences* (2014), https://doi.org/10.1016/j.jcss.2014.04.025 .
