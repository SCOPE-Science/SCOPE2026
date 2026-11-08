# Two-step magnetization and a saturation jump in the Robertson-cage antiferromagnet

## Finding

Let \(G\) be the unique \((4,5)\)-cage (Robertson graph), with 19 vertices, 38 edges, and the explicit adjacency list in `verify.py`. In the classical Ising model
\[
H_{J,h}(s)=J\sum_{\{u,v\}\in E(G)}s_us_v-h\sum_{v\in V(G)}s_v,
\qquad s_v\in\{-1,+1\},\quad J>0,\quad h\in\mathbb R,
\]
write \(b=|h|/J\). The **complete zero-temperature energy for all fields** is
\[
\boxed{\frac{E_0(h)}J=\min\{-22-3b,\,-18-5b,\,38-19b\}.}
\]
For \(h>0\), the only positive critical fields are \(h/J=2\) and \(h/J=4\). The magnetization \(M=\sum_v s_v\) and number of labeled ground configurations are

| Field range | Ground-state magnetization | Degeneracy |
|---|---:|---:|
| \(h=0\) | \(-3,-1,+1,+3\) | 16 total (2, 6, 6, 2 respectively) |
| \(0<h<2J\) | \(3\) | 2 |
| \(h=2J\) | \(3,5\) | 6 total (2, 4) |
| \(2J<h<4J\) | \(5\) | 4 |
| \(h=4J\) | \(5,7,9,11,13,15,17,19\) | 1,950 total |
| \(h>4J\) | \(19\) | 1 |

For \(h<0\), reverse the sign of every magnetization. **The 1,950 independent sets underlying the saturation-field degeneracy are already recorded in Cambie--Jooken (2023), and their count is not presented as a new result.** The new classification concerns the full nonzero-field energy envelope and the interior magnetization plateaus, including their exact multiplicities.

## Assumptions and scope

The model uses classical, labeled two-state spins with uniform positive antiferromagnetic exchange \(J\). Zero temperature means global minimization over every configuration. There are no boundary approximations, thermodynamic-limit claims, or assertions about dynamical transitions. The graph is fixed to the 19-vertex Robertson graph, not the 30-vertex Robertson--Wegner graph. The prescribed graph is encoded completely as a symmetric numbered adjacency list in the accompanying self-contained checker; the graph has 38 edges, degree four, no triangles or four-cycles, and exactly 54 pentagons.

## Proof

For each subset \(S\subseteq V(G)\), place \(+1\) spins on \(S\) and \(-1\) spins elsewhere. Let \(k=|S|\), and let \(c(S)\) count edges with exactly one end in \(S\). Then
\[
H_{J,h}(S)/J=38-2c(S)-(h/J)(2k-19).
\]
Define \(B_k=\max_{|S|=k}c(S)\) and let \(N_k\) count labeled subsets attaining \(B_k\). The exhaustive integer enumeration in `verify.py` establishes, for \(k=0,\ldots,19\) in order,
\[
(B_k)=(0,4,8,12,16,20,24,28,30,30,30,30,28,24,20,16,12,8,4,0)
\]
and
\[
(N_k)=(1,19,133,437,703,516,137,4,2,6,6,2,4,137,516,703,437,133,19,1).
\]
The list is obtained by evaluating *all* \(2^{19}=524288\) possible spin assignments, independently via direct edge counting and an incremental Gray-code scan. The checker asserts equality of all 40 resulting integers. This is a finite exhaustive proof, rather than partial sampling.

For each \(k\), the minimized energy within that magnetization sector is the affine function
\[
F_k(x)=38-2B_k-x(2k-19),\qquad x=h/J.
\]
The complete enumeration implies that for every \(k\), \(F_k(0)\ge F_{11}(0)\) and \(F_k(2)\ge F_{11}(2)\); hence, by linearity, \(F_{11}\) is a global minimum on the entire closed interval \([0,2]\). Similarly, \(F_k(2)\ge F_{12}(2)\) and \(F_k(4)\ge F_{12}(4)\) for all \(k\), so \(F_{12}\) minimizes on \([2,4]\). Finally \(F_k(4)\ge F_{19}(4)\) for all \(k\); \(F_{19}\) has the most negative slope of all the lines, so it stays minimal for all \(x\ge4\). These exact inequalities are asserted by the checker using rational arithmetic. Global spin reversal maps field \(h\) to \(-h\), establishing all negative fields.

For \(x\in(0,2)\), the unique minimizing sector is \(k=11\), giving \(M=3\) and degeneracy \(N_{11}=2\). For \(x\in(2,4)\), the unique minimizing sector is \(k=12\), giving \(M=5\) and degeneracy \(N_{12}=4\). For \(x>4\), the sector \(k=19\) is unique with multiplicity one. At each boundary the exact ties are read directly from the \(F_k\) and \(N_k\) arrays. In particular, at \(x=0\) sectors \(k=8,9,10,11\) contribute \(2+6+6+2=16\); at \(x=2\) the two active sectors contribute \(2+4=6\). At \(x=4\) the active sectors are \(k=12,\ldots,19\) with total 1,950, which agrees with the published independent-set count. This exhausts all fields and all competing spin assignments.

## Verification

Run `python3 verify.py` using Python 3.9 or later. The checker uses only standard-library integer arithmetic and `fractions.Fraction`. It verifies graph regularity, absence of triangles and four-cycles, the original source's count of 54 pentagons, two independently implemented complete configuration scans, all occupancy-sector optima and counts, the exact affine lower-envelope inequalities at both boundaries of each field interval, and the complete sets of ties. The printed output lists all sector data and the zero-field and critical-field degeneracies. In particular, finite exhaustive enumeration here is conclusive because the state space consists of exactly \(2^{19}\) configurations; no thermodynamic limit is inferred.

## Relationship to prior work

Robertson's original 1964 article defines and characterizes the unique 19-vertex quartic girth-five cage; the Exoo--Jajcay survey (first publicly dated 2008-09-29 in the journal record) provides a dated reference for this canonical family. Cambie and Jooken (arXiv:2311.05542, 2023), Section 4 and Theorem 4.6, already determine that this graph has 1,950 independent sets, and use its independence polynomial for hard-core-model occupancy comparisons. For a four-regular graph, the field \(h=4J\) maps precisely to an independent-set count; thus this part of the computation is a known implication. **It does not imply the frustrated-Ising maximum-cut profile in the interior field region, the two interior magnetization sectors, or their exact degeneracies.** The inspected two-page original graph article and eight-page hard-core-model article do not establish the full magnetic-field formula. Previous calculations on other named spin clusters do not logically determine these 19-vertex values.

## Limitations

The claim is confined to this single canonical finite graph with classical Ising spins. The saturation degeneracy 1,950 is not new. The finite-size critical fields are ground-state level crossings, not bulk phase transitions. The originality assessment is based on identifiable published literature and record searches; additional unindexed numerical tables could exist. Independent review of the computation and historical priority has not been performed.

## References

1. N. Robertson, *The Smallest Graph of Girth 5 and Valency 4*, Bull. Amer. Math. Soc. 70 (1964), 824–825. https://artefacts-discovery.researcher.life/full_text/DA-2/bb/bb3144f818ed314f9cebb308a0a5efd6/full_text/9b254f347a4a56021538dea19270036d.pdf
2. G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics, DS16, first published 2008-09-29. https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS16
3. S. Cambie and J. Jooken, *Counterexamples to conjectures on the occupancy fraction of graphs*, arXiv:2311.05542 (2023), especially Section 4 and Theorem 4.6. https://arxiv.org/abs/2311.05542
