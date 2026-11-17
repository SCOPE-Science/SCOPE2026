# A length-weighted primitive-clock spectrum for minimal-activity chip firing on theta graphs

## Finding

Let \(\Theta(a,b,c)\) be the simple graph consisting of three internally vertex-disjoint paths between two marked vertices, of edge lengths \(a,b,c\ge1\), with at most one of the lengths equal to one. Write \((L_1,L_2,L_3)=(a,b,c)\). For each integer \(p\ge4\), let \(N_p^{(1)}\) denote the number of labelled primitive temporal period-\(p\) orbits of synchronous parallel chip firing in which **each vertex fires exactly once in each period**. Temporal rotations identify states; spatial automorphisms do not. Then
\[
\boxed{N_p^{(1)}=2\sum_{i=1}^3L_i\,\mathbf1_{\{p\mid L_j+L_k\}},\qquad\{i,j,k\}=\{1,2,3\}.}
\]
Thus the full length-weighted minimal-activity clock polynomial is
\[
\sum_{p\ge4}N_p^{(1)}t^p
=2\sum_{i=1}^3L_i\sum_{\substack{d\mid L_j+L_k\\d\ge4}}t^d.
\]
In particular a primitive activity-\(1/p\) clock exists if and only if at least one of the graph's three simple-cycle lengths is divisible by \(p\). If several cycle lengths are divisible, their contributions add with coefficients equal to lengths of the *opposite* paths. For example \(\Theta(1,2,3)\) has four such period-four orbits and two period-five orbits, while \(\Theta(3,3,3)\) has eighteen period-six orbits.

## Assumptions and scope

Every vertex \(v\) holds a nonnegative integer \(x_v\). At each synchronous update it fires precisely when \(x_v\ge d_v\), where \(d_v\) is its degree, and sends one chip to each neighbor. The deterministic map is
\[
F(x)_v=x_v-d_v f_v(x)+\sum_{w\sim v}f_w(x),\qquad f_v(x)=\mathbf1_{\{x_v\ge d_v\}}.
\]
The graph is finite, connected, undirected and simple, without sinks or dissipation. A period-\(p\) orbit has \(F^p(x)=x\) and least return time \(p\). The additional *minimal-activity* condition requires \(\sum_{t=0}^{p-1}f_v(F^t(x))=1\) for every vertex; no claim is made about period-\(p\) orbits with other per-vertex firing counts, transient orbits, or attraction basins.

## Proof

**Firing phases and admissible chip heights.** Fix \(p\ge4\) and a phase function \(s:V\to\mathbb Z/p\mathbb Z\), indicating the unique firing time of each vertex. Put \(a_v(s)=|\{w\sim v:s(w)=s(v)-1\pmod p\}|\). At its firing instant a vertex has \(d_v+u_v\) chips for a nonnegative integer \(u_v\). After firing, its successive waiting-step heights equal \(u_v\) plus the cumulative number of neighbors firing since its own firing time. Immediately before its next firing the height is \(d_v+u_v-a_v(s)\). These heights are nondecreasing through the waiting portion of the period. Consequently the required pattern is valid exactly for
\[
0\le u_v<a_v(s).
\]
Conversely these bounds at every vertex construct a unique nonnegative period-\(p\) state, with the prescribed phases and heights, because the chip balance after one full period is zero. Thus for a fixed phase function the number of time-zero microscopic states is precisely \(\prod_v a_v(s)\). All such states have least period \(p\), since each vertex fires once, rather than zero or two or more times, in that period. Division by \(p\) removes precisely the temporal rotations.

**Parent choices and directed cycles.** The product \(\prod_v a_v(s)\) counts choices, at each vertex, of a neighboring vertex whose phase is one less. Direct one arc from each vertex to its chosen predecessor. The result is a functional digraph, and every directed cycle has length divisible by \(p\), since phases decrease by one on each directed arc. Conversely a functional orientation with all directed cycles of lengths divisible by \(p\) admits \(p\) phase assignments for each weak component. In the connected theta graph, every undirected simple cycle passes through both terminals, so two vertex-disjoint directed cycles are impossible. Every such functional orientation therefore has exactly one directed cycle, and this cycle must traverse two of the three terminal-to-terminal paths. It can follow either orientation. The phase labels are then uniquely determined up to a global choice of \(p\) phases, which cancels the division by \(p\) above.

**Exact orientation count.** Fix the directed cycle using paths \(j\) and \(k\). Its length is \(L_j+L_k\), so it is admissible precisely when \(p\mid L_j+L_k\). The remaining path \(i\) has \(L_i-1\) internal vertices. Each such vertex must direct its unique outgoing arc toward one terminal, and no reciprocal two-cycle is allowed. Along that path, the outward-pointing vertices form a prefix from one terminal and a suffix toward the other. There are exactly \(L_i\) possible choices of the separation point, including both extreme cases. Each combines with either of the two cycle orientations. Therefore this choice of cycle contributes \(2L_i\) primitive temporal orbits. The possible directed cycles are mutually exclusive for a functional orientation, so summing over the three complementary path pairs proves the formula.

The divisor polynomial and all examples follow immediately. This is an all-period **orbit multiplicity** result; the known general criterion for existence of a period-\(p\) firing pattern does not itself state these path-length-weighted counts.

## Verification

The standalone file `theta_allperiod_check.py` separately enumerates phase-weight products and bounded microscopic chip configurations. Its output reports 35 phase cases and 32 direct microscopic cases (868,608 bounded states in total) across several theta graphs and periods three through eight, including the claimed range four through eight. All checks pass. The finite checks test the implementation, not the proof for arbitrary path lengths or periods. Reproduce with `python3 theta_allperiod_check.py`.

## Relationship to prior work

Prisner (1994) constructs periodic firing-phase patterns and establishes a cycle-length divisibility condition for possible periods in broader graph classes. That establishes the existence aspect of this result, **not novelty of a period criterion**. Jiang (2010) discusses common vertex firing activity and periodicity. The full available Dall'Asta (2006) preprint studies one-dimensional rings, not competing theta cycles. A published general three-period polynomial explicitly covers the period-three analogue of the phase-counting method, and is **stronger for period-three mass enumeration**; accordingly the theorem here is restricted to periods at least four and makes no new period-three claim. The new subject is a closed, all-period quantitative count of minimal-activity primitive temporal orbits on a rank-two, three-path graph, including the exact length weight of each cycle's contribution.

## Limitations

The result counts only orbits with one firing per vertex and period, not all period-\(p\) orbits. Some such orbits may coexist with other activity sectors. The cycle-divisibility *existence* criterion and the phase-partition method are classical. The full 1992 Bitar–Goles article could not be accessed, leaving historical-priority risk for an equivalent orbit enumeration. The 1994 phase-construction literature may contain an implicit counting route; an equivalent explicitly evaluated theta formula was not found in inspected material. No independent validation is asserted.

## References

- E. Prisner, *Parallel Chip Firing on Digraphs*, Complex Systems 8 (1994), 367–383, in particular Lemma 6.7 and Proposition 6.8. https://content.wolfram.com/uploads/sites/13/2018/02/08-5-5.pdf
- L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267 (first posted 2006-01-12). https://arxiv.org/abs/cond-mat/0601267
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (2010). https://arxiv.org/abs/1003.0943
- J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300, DOI:10.1016/0304-3975(92)90316-8 (abstract only).
- *Two contiguous chip-energy bands and an exact three-cycle census on connected graphs*, mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-contiguous-chip-energy-bands-and-an-exact-three-cycle-census--99e5dddcdc6e (period-three theorem only).
