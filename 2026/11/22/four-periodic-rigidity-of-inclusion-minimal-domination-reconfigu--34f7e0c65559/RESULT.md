# Four-periodic rigidity of inclusion-minimal domination reconfiguration on cycles

## Finding

Let \(C_n\), \(n\ge 3\), be the labelled simple cycle with vertices \(\mathbb Z/n\mathbb Z\). Let \(\mathcal R(C_n)\) have as vertices **all inclusion-minimal dominating sets**, of possibly different sizes. Two such sets are adjacent if one is obtained from the other by replacing one selected vertex with a nonempty subset of its unselected neighbors (expansion), or by replacing a nonempty subset of selected neighbors with their common unselected neighbor (contraction). Intermediate sets must also be inclusion-minimal dominating sets.

Then **the only isolated configurations in \(\mathcal R(C_n)\)** are the four rotations of the cyclic binary word \(1100\) repeated \(n/4\) times, and they occur exactly when \(4\mid n\) and \(n\ge 8\). In particular,

\[
\#\{M\in\mathcal M(C_n):\deg_{\mathcal R(C_n)}(M)=0\}
=\begin{cases}4,&4\mid n\text{ and }n\ge8,\\0,&\text{otherwise}.\end{cases}
\]

The cycle \(C_4\) is the genuine exception: its four \(1100\)-type sets admit legal moves. For every other inclusion-minimal dominating set on every cycle, at least one legal move is explicitly described below. Hence each \(C_{4k}\) with \(k\ge2\) has a disconnected expansion/contraction reconfiguration graph, even though the underlying cycle is connected and 2-regular. No connectivity assertion is made about the non-isolated configurations.

## Assumptions and scope

A set \(M\subseteq V(C_n)\) *dominates* if every vertex is in \(M\) or adjacent to a vertex of \(M\). It is inclusion-minimal if deleting any element of \(M\) destroys domination. For a cyclic binary string, a 1 indicates membership in \(M\). A selected vertex has a *private witness* if some vertex of its closed neighborhood is dominated by no other selected vertex; inclusion-minimal domination is equivalent to every selected vertex having a private witness. Runs and gaps are cyclic, not linear. The statement concerns the expansion/contraction model of Beaton (2024), **not** token addition/removal on all dominating sets, ordinary token sliding on fixed-cardinality minima, or replacement of one selected vertex by an arbitrary vertex.

## Proof

**1. Local word characterization.** A cyclic word represents an inclusion-minimal dominating set precisely if (a) no zero-run has length three, (b) no one-run has length three, and (c) each run \(11\) is immediately preceded and followed by a zero-run \(00\). To see necessity of (a), the middle of \(000\) would be undominated. For (b), the middle vertex of \(111\) has no private witness. For (c), the two vertices of a run \(11\) cannot use themselves as private witnesses, so their only possible witnesses are the zero immediately outside each end; each of these zeros must have another zero outside it. Domination bounds all zero-runs by length two. Conversely, (a) gives domination, every singleton 1 uses itself as private witness, and the flanking two-zero gaps provide distinct private witnesses for each endpoint of every run \(11\). This includes the small cycles by direct interpretation of cyclic neighbors; \(C_3\) and \(C_4\) are checked separately below.

**2. Any mixture of singleton and double one-runs is mobile.** Suppose both run lengths occur. Going clockwise there is a run \(11\) followed by a singleton \(1\). The intervening zero-run must be \(00\), so the local pattern is \(11001\), with a two-zero gap also preceding the double run. Slide the second 1 of the double run into the first following zero:

\[
11001\longmapsto10101.
\]

The result retains domination and all private witnesses: it replaces the affected double run by singleton runs separated by one zero, while leaving external zero-runs and all other one-runs unchanged. It is a legal one-neighbor expansion and establishes positive degree.

**3. Every all-singleton configuration is mobile.** Such a word is an independent dominating set, and its clockwise zero-gap lengths are all in \(\{1,2\}\). If both lengths occur, there are consecutive gaps of lengths 1 and 2; slide the shared selected vertex one place toward the length-two gap. This interchanges their lengths and preserves independent domination. If every gap has length two, \(n\ge6\) and replacing one selected vertex by its two neighboring unselected vertices converts the three surrounding gaps to lengths \(1,1,1\); all selected vertices remain isolated from each other and domination persists. If every gap has length one, \(n\ge6\) and replacing the two selected endpoints of a \(101\) block by its central zero changes the adjacent gap lengths to two while retaining all others at one; again the result is independent and dominating. These are respectively an expansion, an expansion into two neighbors, and a contraction of two neighbors. All preserve inclusion-minimality. The cases \(C_3\) and \(C_4\) are checked below.

**4. All-double configurations are rigid apart from \(C_4\).** If every one-run is \(11\), condition (c) forces the entire word to repeat \(1100\), so \(4\mid n\). When \(n\ge8\), every selected vertex has exactly one vacant neighbor and every vacant vertex has exactly one selected neighbor. Thus all potential expansions or contractions reduce to a single token slide. But sliding an endpoint of one \(11\)-block toward its adjacent 00-gap removes the unique private zero witness of the adjacent endpoint of the *next* \(11\)-block, without separating that next selected pair; the result is not inclusion-minimal. Every slide is a rotation of this obstruction. Therefore the four phase shifts are isolated.

For \(C_3\), the only minimal dominating sets are its three singletons, connected by slides. For \(C_4\), its two alternating pairs and four consecutive pairs are all minimal dominating, and each consecutive pair can slide one endpoint to produce an alternating pair. There are no isolated configurations. Together with steps 2–4 this proves the theorem for every \(n\ge3\).

## Verification

Two standalone Python programs accompany the claim. Run `python verify_exhaustive.py` to enumerate all subsets directly for every \(3\le n\le18\), test domination and inclusion-minimality by actual deletion, build every expansion and contraction, and check the exact number and form of the isolated configurations. The observed isolated counts are zero for lengths \(3,4,5,6,7,9,10,11,13,14,15,17,18\) and four for lengths \(8,12,16\).

Run `python verify_structure.py` for an independent **all-length finite-state certificate**. It uses eleven-bit local windows to describe forbidden moves; every frozen cycle of length at least 11 corresponds to a closed walk in a 10-bit de Bruijn graph. The unique recurrent strongly connected component consists of four states \(\{204,409,614,819\}\) connected as a directed four-cycle, exactly the repeated \(1100\) words. This is a finite automaton proof for unbounded cycle length, not an inference from testing finitely many cycles. The elementary run proof above independently establishes the result without relying on either program.

## Relationship to prior work

Beaton (arXiv:2411.02300, first public November 4, 2024), Definition 1.1, introduced this precise expansion/contraction model. Theorem 3.4 establishes connectivity for trees; Theorem 3.7 gives isolated vertices for a matching-joined graph family. The paper describes \(\mathcal R(C_5)\) but does not give an all-cycle classification of isolated minimal dominating sets. Its matching-joined construction cannot be specialized directly to simple cycles \(C_{4k}\), since it requires internal edges on both sides in addition to matching edges.

Adaricheva et al. (arXiv:2112.04448, first public December 8, 2021) prove a modulo-four Hamilton-path criterion for *all dominating sets* of cycles under *single-token addition/removal*. This does not imply any claim about the inclusion-minimal-set state space under expansion/contraction; the two reconfiguration graphs have different vertices and edges. The common modulo-four arithmetic is not a reduction.

A separate exact four-periodic published-finding corpus calculation concerns *minimum isolating sets* on cycles under arbitrary one-vertex exchange. Its domination predicate, optimization criterion, allowed transitions and configuration counts are all different from those in this theorem. This result does not claim to improve its count; it classifies a different frozen-set phenomenon.

## Limitations

The theorem identifies exactly the isolated vertices, not the number, size or diameter of all other connected components. It makes no algorithmic complexity claim for arbitrary input graphs. The proof concerns labelled simple cycles, and the \(C_4\) exception cannot be omitted. Comparisons of accessible literature and indexed findings reduce but do not eliminate the risk of an unindexed equivalent statement. Independent external mathematical validation has not been conducted.

## References

1. I. Beaton, *Reconfiguration graphs for minimal domination sets*, arXiv:2411.02300 (first public 2024-11-04). https://arxiv.org/abs/2411.02300
2. K. Adaricheva, H. Smith Blake, C. Bozeman, N. E. Clarke, R. Haas, M.-E. Messinger and K. Seyffarth, *Hamilton Paths in Dominating Graphs of Trees and Cycles*, arXiv:2112.04448 (first public 2021-12-08). https://arxiv.org/abs/2112.04448
3. *A four-periodic reconfiguration theorem for minimum isolating sets on cycles* (2026), accessible public comparison. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-four-periodic-reconfiguration-theorem-for-minimum-isolating-se--4d710023d8c9
