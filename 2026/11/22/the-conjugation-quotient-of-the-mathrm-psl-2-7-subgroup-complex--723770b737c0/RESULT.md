# The conjugation quotient of the \(\mathrm{PSL}_2(7)\) subgroup complex is collapsible

## Finding

Let \(G=\mathrm{PSL}_2(7)\cong\mathrm{GL}_3(\mathbb F_2)\), and let \(L(G)\) be the finite poset of **all** subgroups \(H\) with \(1<H<G\), ordered by strict inclusion. Let \(G\) act by simultaneous inner conjugation of the members of each chain. The ordinary geometric orbit space is **collapsible** and hence contractible:

\[
\bigl|\Delta L(G)\bigr|/G\searrow\{\mathrm{point}\}.
\]

Its rank-ordered orbit-cell structure has exactly \(13\) zero-cells, \(37\) one-cells, \(37\) two-cells and \(12\) three-cells. An explicit sequence of \(49\) valid free-face/coface removals leaves one vertex. No claim is made about quotients by outer automorphisms or other simple groups.

## Assumptions and scope

The finite group is represented as the \(168\) invertible three-by-three matrices over \(\mathbb F_2\). The simplicial complex \(\Delta L(G)\) contains one \(d\)-simplex per strict chain \(H_0<\cdots<H_d\), where none of its members is trivial or the full group. Quotienting means the topological orbit space of the **realization**, not the orbit poset of individually conjugate subgroups, not a homotopy quotient, and not a prime-subgroup complex. All subgroups, including composite-order proper subgroups, enter the computation.

## Proof

**Group and subgroup completeness.** A binary three-by-three matrix is encoded by a nine-bit integer in row-major order; the standard integer masks represent group elements. The verifier lists every matrix inducing a permutation of the eight vectors in \(\mathbb F_2^3\), producing all \(168\) invertible matrices. Its multiplication table is defined directly by binary matrix composition. Start from the trivial subgroup and, for every discovered subgroup and every group element outside it, adjoin that element and take the full group closure. Induction on a finite generating set shows this procedure reaches *every* subgroup: each newly adjoined generator is considered when its predecessor subgroup is reached. This gives exactly \(179\) subgroups in total and \(177\) proper nontrivial subgroups. Counts by subgroup order, including endpoints, are:

\[
\begin{array}{c|rrrrrrrrrrr}
\text{order}&1&2&3&4&6&7&8&12&21&24&168\\
\text{number}&1&21&28&35&28&8&21&14&8&14&1.
\end{array}
\]

The published subgroup lattice table of Connor and Leemans independently lists the same sizes and precisely \(15\) conjugacy classes of subgroups, including the trivial and full subgroups.

**The genuine orbit cells.** Exhaustively list the strict subgroup chains by recursively extending with a larger containing subgroup. In simplex dimensions zero through three the unquotiented chain counts are
\[
(177,911,1071,336).
\]
For each chain, choose its lexicographically least image under the \(168\) simultaneous conjugations. The resulting orbit-cell counts are
\[
(c_0,c_1,c_2,c_3)=(13,37,37,12).
\]
A chain has strictly increasing subgroup orders. A stabilizing group element must therefore fix each vertex separately: no simplex inversion occurs. Furthermore, distinct faces of one chain have different sets of subgroup orders, so they cannot be identified with one another by conjugation. The quotient thus has a regular rank-ordered CW/\(\Delta\)-complex structure whose faces are the distinct orbits of chains obtained by deleting one subgroup. This is not generally the abstract simplicial complex on the individual subgroup-conjugacy classes.

**Complete free-face certificate.** Number the canonical orbit-cell representatives lexicographically, separately in each dimension, starting at zero. The companion `collapse_certificate.json` lists \(49\) ordered triples `[d,upper,face]`: remove the indicated active \(d\)-cell and its active \((d-1)\)-face. At each step `verify.py` reconstructs every facet by deleting one chain member and reconjugating it. It checks that the proposed face occurs **exactly once among all active \(d\)-cell facets**, and occurs exactly once in the specified upper cell, and that no active higher-dimensional cell contains it. Since the characteristic maps are injective on the face being removed, each operation is a genuine CW elementary collapse. The \(12\) three-cells are eliminated first, followed by collapses in lower dimensions. The \(49\) pairs remove all cells but one vertex:
\[
(13+37+37+12)-2\cdot49=1.
\]
Every elementary collapse is a strong deformation retraction, proving the asserted contractibility.

## Verification

Place `verify.py` and `collapse_certificate.json` in one directory and execute `python3 verify.py`. Only Python 3 standard-library modules are needed. The program computes the matrices and inverse table afresh, exhaustively enumerates subgroups and all chains, reconstructs every chain-orbit cell and deletion face, and checks every ordered certificate move, including the absence of higher cofaces. The actual check reports:

```
PSL27_ORBIT_SUBGROUP_COMPLEX_COLLAPSE_OK
group=168 subgroups=179 proper=177 chains=2495
orbit_cells=(13,37,37,12) certified_collapses=49 residual_vertex=1
```

Every finite object is enumerated without probabilistic sampling. The tabulated subgroup-class counts independently agree with the Connor–Leemans atlas; the topological conclusion rests additionally on the explicit orbit incidence and collapse checks.

## Relationship to prior work

Ramras (2002) analyzes topology and connectivity of the unquotiented subgroup and coset posets; these do not determine the ordinary inner-conjugation quotient. Connor–Leemans (2013; subgroup table dated 2012) enumerate and classify subgroups of finite almost-simple groups, including \(G\), but tabulating subgroups or their individual conjugacy classes does not encode all simultaneous flag-orbit incidence maps or the free-face sequence. The published \(A_5\) and \(S_5\) conjugation quotient classifications yield a circle and a two-sphere respectively; they concern different groups and neither implies the present contractibility. Theorems on conjugation quotients of **\(p\)-subgroup complexes** concern a different subposet and do not by themselves establish the all-proper-subgroup claim.

This is a natural next simple-group case: \(\mathrm{PSL}_2(7)\) is the second smallest nonabelian simple group and its maximal proper subgroups are solvable. Standard results cited by Ramras imply that its *unquotiented* subgroup complex has nonzero first homology, while the geometric conjugation quotient collapses to a point.

## Limitations

The conclusion applies only to \(\mathrm{PSL}_2(7)\cong\mathrm{GL}_3(\mathbb F_2)\) and the complete inner-conjugation action. It does not compute the topology of the unquotiented complex, or assert a classification for all finite simple groups. The proof is exhaustive and machine-replayable but has not received independent mathematical validation. Although related primary literature and indexed claims were compared at the level of mathematical implication, an equivalent unindexed result may exist.

## References

1. Daniel A. Ramras, *Connectivity of the coset poset and the subgroup poset of a group*, arXiv:math/0210001v1, first public 2002-10-01, https://arxiv.org/abs/math/0210001 .
2. Thomas Connor and Dimitri Leemans, *An Atlas of subgroup lattices of finite almost simple groups*, arXiv:1306.4820v1, first public 2013-06-20, https://arxiv.org/abs/1306.4820 .
3. Connor and Leemans, *The subgroup lattice of \(L_2(7)\)*, table dated 2012-11-25, https://leemans.dimitri.web.ulb.be/atlaslat/psl27.pdf .
4. *Conjugation quotients of the proper-subgroup complexes of \(A_5\) and \(S_5\)* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-conjugation-quotients-of-the-proper-subgroup-complexes-of-a-5-an--5700bda30292 .
5. Kevin Iván Piterman, *Homotopy properties of the \(p\)-subgroup complexes* (2019 thesis), https://mate.dm.uba.ar/~kpiterman/thesis.pdf .
