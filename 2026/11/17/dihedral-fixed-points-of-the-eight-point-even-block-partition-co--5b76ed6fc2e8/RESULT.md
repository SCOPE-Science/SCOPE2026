# Dihedral fixed points of the eight-point even-block partition complex: a sixteen-circle exception

## Finding

Let \(P\) be the poset of set partitions of \(\{0,1,\ldots,7\}\) into at least two nonempty blocks, all of even cardinality, ordered by refinement. Put \(K=\Delta(P)\), its order complex. The dihedral group of the eight labeled points acts simplicially by \(r(i)=i+1\pmod 8\) and \(s(i)=-i\pmod 8\). For **every nonidentity** \(g\in D_8=\langle r,s\rangle\), the actual geometric fixed-point space satisfies

\[
|K|^{g}\simeq
\begin{cases}
\bigvee^{16}S^1,&g=r^4\ \text{or}\ g=r^ks\ \text{with odd }k,\\
\{\mathrm{pt}\},&\text{all other nonidentity }g.
\end{cases}
\]

There are five nonidentity elements with sixteen-circle fixed spaces (one half-turn and four reflections through gaps) and ten with contractible fixed spaces (six non-half-turn rotations and four reflections through opposite vertices). This classifies all fifteen nonidentity elements, not subgroup-intersections of their fixed sets. The sphere wedge for the underlying complex is already established in the literature; the geometric fixed-point homotopy types above are the finding.

## Assumptions and scope

A set partition is an *unordered* collection of nonempty disjoint blocks covering all eight labels. The admissible block-size patterns are \((2,2,2,2)\), \((2,2,4)\), \((2,6)\), and \((4,4)\). The one-block maximum is omitted, as is the artificially adjoined minimum in the standard 2-divisible partition lattice. There are exactly 378 admissible partitions. A simplex of \(K\) is a strictly increasing chain under refinement, and chains have at most three elements, so \(K\) is two-dimensional.

The notation \(|K|^{g}\) means **pointwise geometric fixed points**, not a quotient by \(g\) and not the fixed-point set of a nontrivial action on arbitrary single simplices. For the cyclic powers, \(r^k\) acts by index addition modulo eight; the reflections \(r^ks\) act by \(i\mapsto k-i\pmod8\).

## Proof

**Fixed-subcomplex reduction.** Every automorphism induced by a label permutation preserves the number of blocks of a partition. Consequently, if a chain simplex is preserved setwise, each vertex of the chain is preserved individually: different chain vertices have different numbers of blocks. Any point in the realization has a unique relative interior simplex, and if that point is fixed, its support simplex is preserved setwise. It follows that \(|K|^g=|\Delta(P^g)|\) exactly, where \(P^g\) is the induced subposet of individually invariant partitions. There are no barycenters of exchanged incomparable vertices to add.

**Reduction to four cycle types.** Relabeling by \(S_8\) induces an automorphism of \(K\). If two label permutations are conjugate in \(S_8\), their fixed complexes are simplicially isomorphic. The fifteen nonidentity elements of \(D_8\) have precisely four cycle types: \((8)\) occurs four times; \((4,4)\) twice; \((2,2,2,2)\) five times; and \((1,1,2,2,2)\) four times. Representatives are \(r\), \(r^2\), \(r^4\) and \(s\), respectively. Thus a complete exact analysis of these four finite fixed subposets suffices.

**Exhaustive finite collapse.** Encode each set partition uniquely by a restricted-growth string, enumerate the 4,140 set partitions of eight labels, retain the 378 with all blocks even and at least two blocks, then form all comparable pairs and three-term chains. The entire order complex has \((f_0,f_1,f_2)=(378,1995,1890)\). For the four representatives, the exact face counts, elementary free-edge/triangle collapse counts, and surviving connected graph statistics are:

| Cycle type | Fixed face counts \((f_0,f_1,f_2)\) | Free-edge/triangle collapses | Remaining vertices and edges | First Betti number |
|---|---:|---:|---:|---:|
| \((8)\) | \((2,1,0)\) | 0 | \((2,1)\) | 0 |
| \((4,4)\) | \((10,11,2)\) | 2 | \((10,9)\) | 0 |
| \((2,2,2,2)\) | \((58,163,90)\) | 90 | \((58,73)\) | 16 |
| \((1,1,2,2,2)\) | \((26,67,42)\) | 42 | \((26,25)\) | 0 |

These are **explicit finite proof certificates**, not statistical or partial enumerations. The accompanying `collapse_certificate.json` supplies every collapse pair, listed as the edge and its unique incident triangle at the moment of removal. `verify_even_partition_fixed.py` independently reconstructs all partitions from restricted-growth strings, computes all chains, checks that each designated edge is free in the current simplicial complex, verifies every surviving edge set, checks connectivity using spanning trees, and counts the four cycle-type multiplicities among all nonidentity dihedral elements. Each collapse is an elementary simplicial collapse, hence preserves homotopy type.

A finite connected graph has homotopy type a wedge of \(e-v+1\) circles. The three zero-rank graphs are trees, hence contractible; the \((2,2,2,2)\) graph has rank \(73-58+1=16\). Conjugacy extends these results from the four checked representatives to every nonidentity dihedral element, proving the assertion.

## Verification

Run `python3 verify_even_partition_fixed.py` in the directory containing the supplied `collapse_certificate.json`. It uses only the Python standard library. The verifier deterministically checks the 4,140 original partitions, 378 eligible vertices, all 1,995 edges and 1,890 triangles; it then replays 134 elementary collapses across the four representative types and checks that every resulting graph is connected with the asserted cycle rank. The last line must read `ALL CHECKS PASSED`. Every triangle in each nontrivial fixed complex is eliminated; no inference from a finite sample to an unbounded family is made. The reduction to fifteen group elements is exact because the dihedral group has order sixteen.

## Relationship to prior work

Hanlon (1981) analyzes the full partition lattice fixed by a permutation, without imposing even block sizes. Wachs (1996) gives an EL-shelling, a homology basis, and symmetric-group homology matrices for the **2-divisible** partition lattice; her results determine the ordinary nonequivariant sphere-wedge homology and the Lefschetz traces, but do not supply the homotopy types of its elementwise geometric fixed loci. Arone and Brantner (2018 preprint, later journal publication) study fixed points of the **full** partition complex. For example, their result for a freely acting involution on eight labels describes a different fixed space from the even-block subcomplex here. The full-partition conclusions cannot be restricted to even-block partitions without further work: deleting non-even vertices can alter fixed-space homotopy.

The contrast is topologically substantial: the 2-divisible proper-part complex is two-dimensional and shellable, but its five half-turn/edge-reflection fixed loci all retract to a **one-dimensional wedge of sixteen circles**. This homotopy information is stronger than the alternating fixed-face count or a rational character alone. No claim is made about fixed loci of arbitrary subgroups, other label permutations not realized by the polygon's dihedral group, or larger numbers of labels.

## Limitations

The result is an exact finite classification for the 15 nonidentity symmetries of one eight-label complex. It neither extrapolates to larger 2-divisible partition lattices nor identifies the equivariant homotopy type of the ambient complex as a genuine diagram of all subgroup fixed points. The collapse certificate is exhaustively reproducible but is not a computer-independent handwritten classification of the collapsed graphs. No independent mathematical audit is asserted. The possibility of an unindexed equivalent derivation in the older restricted-partition literature remains a publication-priority risk.

## References

- P. Hanlon, *The Fixed-Point Partition Lattices*, Pacific Journal of Mathematics 96 (1981), 319–341. https://msp.org/pjm/1981/96-2/pjm-v96-n2-p04-s.pdf
- M. L. Wachs, *A Basis for the Homology of the d-Divisible Partition Lattice*, Advances in Mathematics 117 (1996), 294–318. https://doi.org/10.1006/aima.1996.0014
- G. Z. Arone and D. L. B. Brantner, *The Action of Young Subgroups on the Partition Complex*, arXiv:1801.01491 (first submitted January 4, 2018); Publications Mathématiques de l'IHÉS 133 (2021), 47–156. https://arxiv.org/abs/1801.01491
