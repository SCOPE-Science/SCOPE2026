# A six-cycle resonance and exact ten-class entrance law for four-color cyclic dynamics on complete bipartite graphs

## Finding

Let \(m,n\ge1\). On the labelled complete bipartite graph \(K_{m,n}\), apply the synchronous four-color cyclic successor-contact rule: color \(c\in\mathbb Z/4\mathbb Z\) advances to \(c+1\) exactly when an adjacent vertex already has \(c+1\); otherwise it stays at \(c\). Let \(F\) be the resulting map, and let \(N_{t,p}(m,n)\) be the number of initial labelled colorings whose *first* periodic-entry time is exactly \(t\), with eventual *least* period \(p\).

For all positive \(m,n\),
\[
F^{16}=F^4,\qquad (t,p)\in\{(0,1),(1,1),(2,1),(3,1),(4,1),(0,4),(1,4),(2,4),(3,4),(0,6)\}.
\]
All ten classes are governed by the complete coefficient matrices below. In particular, six-cycles are **always periodic at time zero** and their labelled population is exactly
\[
N_{0,6}(m,n)=4\bigl(3^m-3\cdot2^m+3\bigr)\bigl(3^n-3\cdot2^n+3\bigr).
\]
A primitive six-cycle exists exactly when \(m,n\ge3\); the number of such distinct labelled temporal orbits is \(N_{0,6}(m,n)/6\). A primitive four-cycle exists exactly when \(m,n\ge2\). The fixed-point count is \(2^{m+n+1}\), and the sharp maximum first-entry time is four when \(m\ge2,n\ge3\) or \(m\ge3,n\ge2\). The lag \(12\) and entrance exponent \(4\) in the displayed identity are each sharp simultaneously when \(m,n\ge3\).

## Assumptions and scope

The two shores consist of \(m\) and \(n\) individually labelled vertices; all cross-shore edges are present, no within-shore edges and no loops are present. There are exactly four colors with the stated threshold-one successor-contact rule. No randomness is assumed in the theorem. For distributional consequences, initial colors are taken independently and uniformly from the four possibilities.

Define the onto-coloring number
\[
U_k(d)=\sum_{j=0}^k(-1)^j\binom kj(k-j)^d\quad(1\le k\le4,\ d\ge1),
\]
where \(0^d=0\) for positive \(d\). Let the row and column indices of every matrix below run from \(1\) through \(4\). For each \(t,p\), the exact count is
\[
N_{t,p}(m,n)=\sum_{k=1}^4\sum_{\ell=1}^4 C_{t,p}(k,\ell)U_k(m)U_{\ell}(n).
\]
For any pair not listed below, \(N_{t,p}=0\).

### Complete temporal coefficient matrices

\[C_{0,1}=\begin{pmatrix}8 & 4 & 0 & 0\\4 & 2 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 0 & 0\end{pmatrix}.\]

\[C_{0,4}=\begin{pmatrix}0 & 0 & 0 & 0\\0 & 2 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 0 & 1\end{pmatrix}.\]

\[C_{0,6}=\begin{pmatrix}0 & 0 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 4 & 0\\0 & 0 & 0 & 0\end{pmatrix}.\]

\[C_{1,1}=\begin{pmatrix}8 & 8 & 4 & 0\\8 & 8 & 0 & 0\\4 & 0 & 0 & 0\\0 & 0 & 0 & 0\end{pmatrix}.\]

\[C_{1,4}=\begin{pmatrix}0 & 0 & 0 & 0\\0 & 0 & 4 & 2\\0 & 4 & 0 & 0\\0 & 2 & 0 & 0\end{pmatrix}.\]

\[C_{2,1}=\begin{pmatrix}0 & 8 & 4 & 0\\8 & 16 & 8 & 0\\4 & 8 & 4 & 0\\0 & 0 & 0 & 0\end{pmatrix}.\]

\[C_{2,4}=\begin{pmatrix}0 & 0 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 8 & 0\\0 & 0 & 0 & 0\end{pmatrix}.\]

\[C_{3,1}=\begin{pmatrix}0 & 4 & 8 & 4\\4 & 8 & 8 & 4\\8 & 8 & 0 & 0\\4 & 4 & 0 & 0\end{pmatrix}.\]

\[C_{3,4}=\begin{pmatrix}0 & 0 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 0 & 4\\0 & 0 & 4 & 0\end{pmatrix}.\]

\[C_{4,1}=\begin{pmatrix}0 & 0 & 0 & 0\\0 & 0 & 4 & 0\\0 & 4 & 0 & 0\\0 & 0 & 0 & 0\end{pmatrix}.\]

## Proof

**Exact finite-state reduction.** In either shore, vertices that initially share a color have exactly the same neighboring vertices and hence evolve identically at every step. For an initial configuration, write the initially occupied colors on the left as an ordered, distinct tagged tuple \(L=(a_1,\ldots,a_k)\) and on the right as \(R=(b_1,\ldots,b_\ell)\), retaining a representative for every initial color class even if two classes later merge. There are exactly \((2^4-1)^2=225\) possible pairs of nonempty initial color supports. Evolve the tagged tuples by the explicit map
\[
(a_i)'=a_i+\mathbf1_{\{a_i+1\in\{b_1,\ldots,b_\ell\}\}}\pmod4,
\qquad
(b_j)'=b_j+\mathbf1_{\{b_j+1\in\{a_1,\ldots,a_k\}\}}\pmod4.
\]
The two right sides use the *previous* values simultaneously. Duplicates in later tagged tuples are retained: they encode originally different vertex classes that have coalesced. Because each original vertex belongs to exactly one tag, the entire labelled trajectory has precisely the same first periodic-entry time and least period as its tagged trajectory. The number of labelled initial states with specified left and right supports of sizes \(k,\ell\) is \(U_k(m)U_\ell(n)\).

**Finite classification certificate.** The 225 initial pairs are enumerated by nonempty subsets of \(\{0,1,2,3\}\), with each subset listed in increasing order. For every pair the explicit successor recurrence is iterated until its first repeated *tagged* state; its first occurrence gives \(t\) and the difference in occurrence times gives \(p\). The full 225-row catalogue is supplied in `checks/support_catalog.tsv`; `scripts/verify_supports.py` independently regenerates all ten displayed matrices from the recurrence and tests the partition of all 225 pairs. This is a complete finite reduction, not an empirical assumption about unbounded graph sizes. The largest observed tagged first-entry time is exactly four, and the only detected periods are one, four and six; the complete list of all tags is small enough for direct replay.

**Lifting and counts.** Each labelled configuration contributes exactly once to its unique initial support pair. Multiplying the number of support pairs of type \((t,p,k,\ell)\) by \(U_k(m)U_\ell(n)\) and summing yields every displayed census formula. The matrix \(C_{0,6}\) has its only nonzero entry \(C_{0,6}(3,3)=4\), and \(U_3(d)=3^d-3\cdot2^d+3\), giving the six-cycle formula. The matrix \(C_{0,1}\) has four nonzero entries \(8,4,4,2\) in its leading \(2\)-by-\(2\) block. Since \(U_1(d)=1\) and \(U_2(d)=2^d-2\), its weighted count simplifies to \(2^{m+n+1}\). All period-six configurations are already periodic, so dividing the period-six population by six counts genuine primitive temporal orbits, without double counting.

**Sharpness and limiting behavior.** Since the coefficient \(C_{4,1}(2,3)=C_{4,1}(3,2)=4\), time four occurs as soon as one shore can use two colors and the other three; the finite table precludes later entry for any shore sizes. When both shores have at least three vertices, the nonzero period-four and period-six classes force any common eventual temporal lag to be divisible by \(\operatorname{lcm}(4,6)=12\). This proves sharpness of \(F^{16}=F^4\) in both senses. Under independent uniform initial colors, the eventual period-six probability is \(4U_3(m)U_3(n)/4^{m+n}\); it is asymptotic to \(4(3/4)^{m+n}\) as both shore sizes diverge, while the probability of being periodic from time zero with period four tends to one because both shores initially contain all four colors with probability tending to one.

## Verification

The source files in this package can be replayed with Python 3 without third-party dependencies. Run `python scripts/verify_supports.py` to regenerate the 225-case tagged-support classification, ten coefficient matrices and sample arbitrary-size polynomial counts. Run `python scripts/verify_vertices.py` to evolve every labelled configuration of ten small bicliques directly by the original vertex-neighbor rule. This separate implementation evolves 92,752 labelled initial states in total, including all 65,536 colorings of \(K_{4,4}\). It agrees with the support-coefficient formulas for every tested case. Full raw reports are `checks/support_check.log` and `checks/vertex_check.log`.

The executable exhaustive certificate plus the deterministic, inspectable recurrence is the basis of the infinite-family proof. Direct simulation of finite graphs alone would not establish the theorem, nor would a list of examples prove the exhaustive catalogue.

## Relationship to prior work

Durrett and Griffeath's 1993 treatment of cyclic cellular automata allows multiple colors but addresses spatial lattice models and spiral-core phase regimes, rather than exact temporal basins on labelled bicliques. Gravner, Lyu and Sivakoff's 2016 arbitrary-graph work concerns the **three-color** model and does not directly imply the four-color phenomenon proved here. A previously reported classification of the four-color successor-contact map on complete **tripartite** graphs with all three shores nonempty admits only periods one and four; the present bipartite case is outside that domain and has genuine primitive period-six attractors. The new statement is the complete ten-class bipartite temporal census and the six-cycle support-resonance law, not the definitions of cellular automata or generic eventual periodicity.

## Limitations

This classification applies to the specified synchronous, threshold-one four-color rule on complete bipartite graphs. It does not assert the same bound for other graphs, other color counts, asynchronous updates, or nonuniform transition thresholds. Historical-priority comparison is limited by searchable literature and accessible theorem statements. An exact equivalent in unindexed literature has not been excluded, and the original 1993 manuscript could not be read in full through the available access routes. The finite-state proof has been computationally reviewed here; it has not undergone an independent audit.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, initial public submission 1993-03-22; *Experimental Mathematics* 2 (1993), 183–208. https://arxiv.org/abs/patt-sol/9303002
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, initial public submission 2016-10-24. https://arxiv.org/abs/1610.07320
3. Earlier complete-tripartite four-color cyclic successor-contact classification, research statement identifier `a56bc883-e0df-4bd1-b2ee-cc23f563bed1` (consulted for implication comparison; different graph family).
