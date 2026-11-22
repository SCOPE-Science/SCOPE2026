# Sharp winding-length spectrum of cycle graph-coloring Hom complexes

## Finding

Let \(m\ge4\), \(n\ge5\), and \(1\le r<m\) be integers with \(n\mid(m-2r)\). In the standard polyhedral graph-multihomomorphism complex \(\operatorname{Hom}(C_m,C_n)\), consider any connected component \(X\) whose graph-coloring vertices have exactly \(r\) negative cyclic target increments. Every such component has \(\pi_1(X)\cong\mathbb Z\). For each nonzero integer \(q\), the shortest closed edge path in the one-skeleton representing the \(q\)-th power of a primitive fundamental-group generator has exactly

\[
\boxed{\operatorname{sys}_1(X;q)=|q|\,\frac{mn}{\gcd(n,2)}.}
\]

In particular, the minimum non-nullhomotopic *single-vertex recoloring* loop has \(mn\) steps for odd \(n\), and \(mn/2\) steps for even \(n\). The answer is independent of the winding sector \(r\). Both the lower bound and an optimal explicit recoloring loop hold for every admissible parameter, not merely for enumerated examples.

## Assumptions and scope

The source and target graphs are undirected simple cycles with vertices respectively \(\mathbb Z/m\mathbb Z\) and \(\mathbb Z/n\mathbb Z\). A vertex of \(\operatorname{Hom}(C_m,C_n)\) is a map \(f\) taking adjacent source vertices to adjacent target vertices. A cell assigns a nonempty set of target vertices at each source vertex, with complete adjacency across every source edge. We equip each one-cell with combinatorial length one; the length of an edge path is the number of traversed one-cells, including repetitions. Nullhomotopy refers to the full polyhedral complex, not only its one-skeleton. For a coloring \(f\), the unique increments \(\epsilon_i\in\{-1,+1\}\) are characterized by \(f(i+1)-f(i)\equiv\epsilon_i\pmod n\). The integer \(r\) counts the indices with \(\epsilon_i=-1\); its winding is \(w=(m-2r)/n\).

The divisibility condition is necessary and sufficient for the specified vertex-coloring sector to be nonempty. The endpoints \(r=0,m\) are excluded because their monotone homomorphisms are isolated and have trivial fundamental group. If \(n\) is even, the sector has two components distinguished by the parity of the initial target color; if \(n\) is odd it has one. The formula applies to each component and uses either primitive orientation of its infinite cyclic fundamental group.

## Proof

**1. Encode recolorings by exclusion particles.** A coloring in the specified sector is uniquely determined by the initial color \(a=f(0)\in\mathbb Z/n\mathbb Z\) and the set \(S=\{i:\epsilon_i=-1\}\subset\mathbb Z/m\mathbb Z\), with \(|S|=r\): given \(a,S\), integrate the signed steps around the source, which closes exactly because \(n\mid(m-2r)\). Since \(n\ge5\), every coordinate set in a Hom cell has at most two target colors, and a nontrivial recoloring at source vertex \(i+1\) occurs exactly when the two neighboring colors coincide. It interchanges the opposite signs on the two source edges \(i\) and \(i+1\). Thus a one-cell moves a particle at a position \(i\in S\) into an empty adjacent position \(i+1\), or the reverse, in a simple-exclusion configuration on \(C_m\). If the particle crosses the cut from \(m-1\) to \(0\) in the positive direction, the initial color changes by \(+2\pmod n\); the reverse crossing changes it by \(-2\pmod n\). Other moves leave the initial color unchanged. Simultaneously allowed recolorings involve disjoint source-coordinate pairs, equivalently independent particle-edge moves. Because adjacent source vertices cannot simultaneously carry two-valued target-coordinate sets for \(n\ge5\), this correspondence respects all cubical faces.

In particular, the target-color rotation group \(C_n\) acts freely and cellularly, and the quotient of the entire winding sector is exactly the discrete cubical configuration complex \(UD_r(C_m)\) of \(r\) unordered, non-colliding particles on the source cycle, with cells parametrized by pairwise disjoint occupied vertices and open edges. The quotient projection is a regular \(n\)-fold covering, possibly with disconnected total space.

**2. Its fundamental group and primitive displacement.** The Abrams–Prue–Scrimshaw discretization theorem applies because the source cycle has no essential vertices and its sole noncontractible circuit has \(m\ge r+1\) edges. Thus \(UD_r(C_m)\simeq\operatorname{UConf}_r(S^1)\simeq S^1\). The final homotopy equivalence follows by recording the cyclically ordered positive gaps between consecutive distinct unlabeled particles: the gap simplex is contractible, and a cyclic permutation of the distinguished first particle supplies the generator of the mapping torus.

Orient the source cycle. Give a positive one-edge particle move the signed increment \(+1\), and a negative move \(-1\). For any closed edge walk in \(UD_r(C_m)\), the total signed displacement \(\Delta\) is divisible by \(m\): the sum of occupied vertex positions changes by \(\Delta\pmod m\). The integer \(D=\Delta/m\) is the winding of the continuous product-of-particle-positions map \(\operatorname{UConf}_r(S^1)\to S^1\), and is homotopy invariant. A full circulating particle loop of \(m\) positive moves cyclically permutes the \(r\) particle identities once, so it generates \(\pi_1(UD_r(C_m))\cong\mathbb Z\) and has \(D=1\). Therefore \(D\) is precisely the primitive fundamental-group coordinate.

**3. Covering monodromy and lower bound.** Lifting one base generator across the coloring cover changes its initial target color by \(+2\pmod n\), since it makes one positive crossing of the cut. The monodromy has order \(L=n/\gcd(n,2)\). Consequently each connected coloring component is an \(L\)-sheet cover of \(UD_r(C_m)\), and its fundamental group injects as \(L\mathbb Z\subset\mathbb Z\). A closed edge walk representing a \(q\)-fold primitive generator in that component has \(D=qL\), and hence total signed displacement \(\Delta=qmL\). Each edge contributes only \(+1\) or \(-1\), so its length \(T\) satisfies

\[
T\ge|\Delta|=|q|mL=|q|\,\frac{mn}{\gcd(n,2)}.
\]

This lower bound holds for any starting coloring and allows arbitrary cancellations and cubical homotopies.

**4. Attaining every bound.** Start with the consecutive occupied positions \(S=\{0,1,\ldots,r-1\}\). Move particle \(r-1\) to \(r\), then \(r-2\) to \(r-1\), continuing down to particle \(0\) moving to \(1\). Continue moving the particle at \(r\) successively to \(r+1,r+2,\ldots,m-1,0\). Exactly \(m\) permitted positive moves return the unordered occupied set to \(S\), with one positive cut crossing. Lifting this walk \(L\) times returns the initial color modulo \(n\), hence closes the coloring path. This produces a primitive non-nullhomotopic edge loop of length \(mL\). Repeating it \(|q|\) times, or traversing it backwards if \(q<0\), gives length \(|q|mL\), attaining the lower bound. It also establishes every claimed nonempty component and the entire minimum-length spectrum.

## Verification

Run `python3 cycle_recoloring_systole_verify.py` with Python 3 and no external packages. The verifier independently reconstructs every proper graph coloring from its signed steps, tests each encoded edge against a single-coordinate recoloring in the actual target cycle, and constructs the explicit optimal loops. For six manageable parameter choices, a signed-displacement breadth-first search independently confirms the minimum closed walk with nonzero fundamental-group displacement. It covers both odd and even target parity and densely or sparsely occupied sectors. All seven example checks passed, ending with `CYCLE_RECOLORING_SYSTOLE_CHECKS_OK`. The finite tests are supplementary: Steps 1–4 establish the unbounded all-parameter result.

## Relationship to prior work

Čukić and Kozlov (2004) prove the component homotopy classification of \(\operatorname{Hom}(C_m,C_n)\) and present special examples with explicitly long cycles, notably \(\operatorname{Hom}(C_{2s+1},C_{2s-1})\). Their special cycle lengths agree with the formula here, but their homotopy classification alone supplies no lower bound for a generator's length in the original one-skeleton or the complete \(q\)-spectrum. Prue and Scrimshaw (first public 2009) establish the required equivalence between discrete and continuous graph configuration spaces; neither that equivalence nor the circle homotopy type by itself determines this recoloring metric.

The published finding *The integral dihedral homology module of cycle-to-cycle graph Hom complexes* (record `57b6b00dbd46`) establishes the complete integral source–target symmetry module, including an odd/even evaluation-index dichotomy, but does not state or prove an exact minimum number of single-vertex recolorings. The separate published finding *Integral transfer and parity cancellation for covering maps of cycle Hom complexes* (record `05782b23a296`) determines induced first-homology coefficients under cycle coverings; this is not the one-skeleton word metric. The later Fujii–Iwamasa–Kimura–Nozaki–Suzuki preprint (2024) generalizes cycle-target component topology and builds explicit universal covers; its inspected general results do not specify the sharp edge-length spectrum. The new statement is specifically the tight recoloring length bound with its geometric exclusion-particle obstruction and optimal construction, not the known circle homotopy type or evaluation-index calculation.

## Limitations

The theorem concerns unweighted undirected simple cycles with target length at least five and the standard polyhedral Hom complex, counting one-cell recolorings rather than arbitrary continuous path length. It makes no claim for targets \(C_3,C_4\), monotone isolated sectors, general graph targets, or the metric after quotienting by symmetries. A scan of indexed and accessible published material cannot rule out every unindexed equivalent formulation; the older literature already contains matching special examples. The result has undergone a self-review, not an independent audit.

## References

1. S. Lj. Čukić and D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015 (first publicly submitted 2004-08-02), especially Sections 2, 5 and 6. https://arxiv.org/abs/math/0408015
2. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (first publicly submitted 2009-09-30), Theorem 3.2. https://arxiv.org/abs/0909.5511
3. S. Fujii, Y. Iwamasa, K. Kimura, Y. Nozaki, and A. Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, arXiv:2408.04802 (first publicly submitted 2024-08-09), especially its universal-cover construction. https://arxiv.org/abs/2408.04802
4. *The integral dihedral homology module of cycle-to-cycle graph Hom complexes*, published mathematical record `57b6b00dbd46` (2026).
5. *Integral transfer and parity cancellation for covering maps of cycle Hom complexes*, published mathematical record `05782b23a296` (2026).
