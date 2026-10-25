# The Fano-plane symmetry character of the Heawood matching complex

## Finding
Let \(H\) be the Heawood graph, the incidence graph of the Fano projective plane \(\mathrm{PG}(2,2)\). Let \(G=\mathrm{GL}(3,\mathbf F_2)\), of order \(168\), act on the points and lines by its natural and contragredient linear actions, respectively. For the ordinary matching complex \(K=\mathcal M(H)\), set
\[
V=\widetilde H_4(K;\mathbf Q).
\]
Then \(\widetilde H_i(K;\mathbf Q)=0\) for \(i\ne4\), and, as rational \(G\)-representations,
\[
\boxed{V\cong \mathbf 1\oplus U_7\oplus U_8.}
\]
Here \(U_7\) is the seven-dimensional augmentation representation of the permutation action of \(G\) on its eight Sylow-seven subgroups, and \(U_8\) is an irreducible rational representation of dimension eight. Both are absolutely irreducible and nonisomorphic. Equivalently, the character \(\chi_V\) depends only on the order of the group element:

| Element order | Number of elements | \(\chi_V\) | Sylow-seven permutation character \(\pi\) | \(\chi_{U_7}\) | \(\chi_{U_8}\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 16 | 8 | 7 | 8 |
| 2 | 21 | 0 | 0 | -1 | 0 |
| 3 | 56 | 1 | 2 | 1 | -1 |
| 4 | 42 | 0 | 0 | -1 | 0 |
| 7 | 48 | 2 | 1 | 0 | 1 |

(The order-seven row combines two conjugacy classes of size \(24\); their values agree.)

## Assumptions and scope
Represent each nonzero element of \(\mathbf F_2^3\) by a binary integer in \(\{1,\ldots,7\}\). Points are nonzero vectors \(p\) and lines are nonzero covectors \(a\); incidence means the mod-two dot product \(a\cdot p=0\). Hence \(H\) has fourteen graph vertices and twenty-one graph edges, namely the incidence pairs \((p,a)\). A face of \(K\) is a finite set of incidence edges no two of which share a point or line. In particular \(K\) is the **ordinary** matching complex, not the perfect-matching-generated subcomplex.

The action is the color-preserving subgroup \(G\) of the full Heawood graph automorphism group; no claim about the additional point-line dualities or integral representations is made. The mathematical object, coefficient field, group action, and precise representation are fixed by these definitions.

## Proof
**Homology concentration.** Enumerate all matchings as subsets of the twenty-one incidence edges, including the empty matching. The numbers of faces in dimensions \(-1,0,1,2,3,4,5,6\) are exactly
\[
(1,21,168,644,1218,1050,336,24).
\]
In the ordinary mod-two simplicial chain complex, exact bit-vector Gaussian elimination gives ranks of boundary maps in dimensions \(1,2,3,4,5,6\), respectively,
\[
(20,148,496,722,312,24).
\]
Therefore all reduced mod-two Betti numbers vanish except for \(\widetilde\beta_4=16\). For an integral finite simplicial complex the rational Betti numbers are bounded by the mod-two Betti numbers in each degree. Consequently its reduced rational homology is concentrated in degree four, with rank at most sixteen. The face numbers give reduced Euler characteristic \(16\); thus the rank is exactly sixteen. These steps independently verify the homological premises, without assuming a prior sphere-wedge computation.

**Group action.** For each of the \(168\) invertible binary \(3\times3\) matrices \(A\), define the point action \(p\mapsto Ap\) and the line action \(a\mapsto A^{-\mathsf T}a\). The incidence pairing is invariant, so this permutes all twenty-one edge-vertices of \(K\). Compute the order of every matrix and the induced permutation of edge-vertices. There are respectively \(1,21,56,42,48\) elements of orders \(1,2,3,4,7\).

**Oriented fixed-face formula.** Let \(f\) be any induced edge-vertex permutation. For every nonempty matching \(\sigma=\{e_1<\cdots<e_k\}\) with \(f\sigma=\sigma\), the trace of \(f\) on its oriented simplex is the sign of the permutation of the \(k\) ordered vertices. The reduced Lefschetz number is therefore
\[
L_{\mathrm{red}}(f)=-1+\sum_{\substack{\varnothing\ne\sigma\in K\\ f\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(f|_\sigma).
\]
As reduced rational homology is supported only in the even degree four, this is precisely \(\chi_V(f)\).

A second calculation groups the twenty-one edge-vertices into their cycles under \(f\). A fixed matching is a union of cycles, each of which must itself be a matching and different selected cycles must be mutually compatible. A cycle of length \(s\) contributes \((-1)^s(-1)^{s-1}=-1\) to the alternating oriented-chain sum, so
\[
\chi_V(f)=-\sum_{J\;\mathrm{compatible}}(-1)^{|J|},
\]
where the empty compatible family is included. Exact evaluation of **both** formulas for **every** group element yields the character column in the table. Thus the traces use genuine orientation signs, not merely counts of invariant simplices.

**Representation decomposition.** Exactly \(48\) group elements have order seven and each order-seven subgroup contains six of them, yielding eight distinct Sylow-seven subgroups. By direct conjugation of these subgroups, the permutation character \(\pi\) of the eight-element set takes values \((8,0,2,0,1)\) on the five order rows. Put \(\alpha=\pi-1\) and \(\beta=\chi_V-\pi\). Summing class functions over all \(168\) group elements gives
\[
\langle\alpha,\alpha\rangle=\langle\beta,\beta\rangle=1,\quad
\langle 1,\alpha\rangle=\langle 1,\beta\rangle=\langle\alpha,\beta\rangle=0,
\]
while \(\langle\chi_V,1\rangle=\langle\chi_V,\alpha\rangle=1\). Since \(\alpha\) is the character of the actual seven-dimensional augmentation module, it is irreducible; \(\chi_V\) contains both \(1\) and \(\alpha\) once. By semisimplicity in characteristic zero their complement is an actual rational module with character \(\beta\), whose norm-one calculation proves absolute irreducibility. This establishes the displayed direct-sum decomposition.

## Verification
Run `python3 verify_heawood_equiv.py` using Python 3 standard library only. The verifier independently builds every matching, computes the full mod-two boundary ranks, enumerates all \(168\) invertible matrices, evaluates **two independent** fixed-face character formulas, constructs the eight Sylow-seven subgroups, verifies their conjugation permutation character, and checks all three irreducible-character inner products exactly. It prints a single `VERIFY_OK` line only after all assertions pass. The source code, not a detached runtime log, is the reproducible finite certificate.

## Relationship to prior work
The publicly available 2026 Heawood matching-complex calculation [1] establishes the nonequivariant homotopy equivalence \(\mathcal M(H)\simeq\bigvee^{16}S^4\), explicitly **without** an equivariant statement. That homotopy type fixes the dimension of \(V\) but leaves its action by \(G\) undetermined. The all-element trace table and decomposition into the \(1\)-, \(7\)-, and \(8\)-dimensional representations require additional equivariant information.

Bate, Everitt, Ford, and Ramos [2] analyze symmetric-group representations in the homology of matching complexes of *complete hypergraphs* and fiber-closed families. Their objects are not this Fano incidence graph, and their theorems do not give the stated \(\mathrm{GL}(3,\mathbf F_2)\) character. The present calculation is consistent with the general chain-orientation convention in [2], but is not a specialization of their classification. Matsushita's [3] polygonal-line-tiling results concern a different graph family. Ordinary irreducible character tables for the abstract group, if known, do not determine which irreducibles occur in the homology of this particular complex.

## Limitations
The theorem concerns rational homology and the index-two color-preserving automorphism subgroup, not the full automorphism group of order \(336\). It does not determine integral lattice structure, equivariant stable homotopy, action on chosen integral sphere generators, or matching complexes of other incidence graphs. The finite certificate exhausts this fixed graph and group; it is not a general-family theorem. Published mathematical searches and comparison cannot rule out an unindexed or differently named equivalent computation, especially one in representation-theoretic literature.

## References
1. *The Heawood matching complex is a wedge of sixteen 4-spheres*, public scientific record dated 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-heawood-matching-complex-is-a-wedge-of-sixteen-4-spheres--7150930ba12a/RESULT.md.
2. M. Bate, B. Everitt, S. Ford, E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750 (2023), Proc. Amer. Math. Soc. 154 (2026), 1467–1478, https://arxiv.org/abs/2312.13750.
3. T. Matsushita, *Matching complexes of polygonal line tilings*, arXiv:1910.00186 (2019).
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
