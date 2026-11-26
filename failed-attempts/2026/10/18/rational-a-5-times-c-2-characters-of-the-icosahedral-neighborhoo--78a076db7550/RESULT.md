# Rational \(A_5\times C_2\)-characters of the icosahedral neighborhood complex
## Finding
Let \(I\) be the icosahedral graph and \(X=\mathcal N(I)\) its **open** Lovász neighborhood complex: a nonempty vertex subset is a face precisely when it has a common adjacent vertex. Let \(G=\operatorname{Aut}(I)\cong A_5\times C_2\), let \(A_5\) denote the orientation-preserving icosahedral rotations and let \(\varepsilon\) denote the nontrivial character of the central inversion \(C_2\). Over \(\mathbb Q\), all reduced homology is zero except in degree two, and
\[
\widetilde H_2(X;\mathbb Q)\cong
(V_6\oplus V_5)\boxtimes\mathbf1
\;\oplus\;
(2\mathbf1\oplus2V_5)\boxtimes\varepsilon.
\]
Here \(V_5\) is the rational five-dimensional irreducible representation of \(A_5\), and \(V_6\) is its six-dimensional rational irreducible representation whose complexification is the sum of the two Galois-conjugate three-dimensional irreducibles. In particular, \(\dim\widetilde H_2(X;\mathbb Q)=23\).

Consequently the two geometric symmetry quotients have sharply different rational homology:
\[
\widetilde H_i(|X|/A_5;\mathbb Q)\cong
\begin{cases}\mathbb Q^2&i=2,\\0&i\ne2,\end{cases}
\qquad
\widetilde H_i(|X|/G;\mathbb Q)=0\quad\text{for all }i.
\]
The result determines the full rational representation and quotient homology; it does **not** claim an integral group-lattice decomposition or equivariant homotopy equivalence.

## Assumptions and scope
The graph \(I\) has vertices \(0,1,\ldots,11\), and the following 30 edges (each pair is unordered):

```
(0,1) (0,5) (0,7) (0,8) (0,11)
(1,2) (1,5) (1,6) (1,8)
(2,3) (2,6) (2,8) (2,9)
(3,4) (3,6) (3,9) (3,10)
(4,5) (4,6) (4,10) (4,11)
(5,6) (5,11)
(7,8) (7,9) (7,10) (7,11)
(8,9) (9,10) (10,11)
```

Let \(F_k\) be the \(k\)-simplices of \(X\). A direct generation of all nonempty subsets of the twelve five-point open neighborhoods gives the face vector
\[
(|F_0|,|F_1|,|F_2|,|F_3|,|F_4|)=(12,60,120,60,12).
\]
All homology and quotient assertions use rational coefficients. The action on \(X\) is induced by permuting graph vertices, not by flipping source vertices of a graph Hom complex.

## Proof
**Step 1: determine rational homology without assuming the preceding sphere-wedge result.** Form the augmented simplicial chain complex, with \(\partial_0:C_0\to\mathbb Q\) the augmentation. Enumerating each simplex and its codimension-one faces gives boundary ranks over \(\mathbb F_2\)
\[
\operatorname{rank}(\partial_0,\partial_1,\partial_2,\partial_3,\partial_4)=(1,11,49,48,12).
\]
The nontrivial four ranks are reconstructed by exact bit-vector Gaussian elimination in `verify_icosahedral_character.py`; the augmentation rank is one. A nonzero minor over \(\mathbb F_2\) remains nonzero over \(\mathbb Q\), so the respective rational ranks are at least those values. They are also at most those values: \(\partial_1\) maps into the 11-dimensional kernel of augmentation; \(\partial_2\) maps into the resulting 49-dimensional kernel of \(\partial_1\); \(\partial_4\) has only 12 columns; and \(\operatorname{im}\partial_4\subseteq\ker\partial_3\) with \(\operatorname{rank}\partial_4=12\), so \(\partial_3\) has rank at most \(60-12=48\). Thus all these rational ranks are exact. It follows that
\[
\widetilde H_k(X;\mathbb Q)=0\ (k\ne2),\qquad
\dim\widetilde H_2(X;\mathbb Q)=120-49-48=23.
\]

**Step 2: determine the complete symmetry group.** Images of one ordered triangular face of the icosahedral graph give exactly 120 ordered triangle flags; adjacency backtracking proves each extends uniquely to a graph automorphism. The rotation subgroup \(R\) preserves a coherent orientation of the twenty triangular faces of the icosahedral sphere and has order 60. The explicit rotations \(a,b\) and central inversion \(z\) are

```
a = (1,0,11,10,9,8,7,6,5,4,3,2)
b = (0,8,9,3,6,1,2,11,7,10,4,5)
z = (3,10,11,0,8,9,7,6,4,5,1,2)
```

Each tuple lists the images of vertices \(0,\ldots,11\). Their orders are respectively two, five and two; \(ab\) has order three; \(z\) is central, reverses sphere orientation and is not a rotation. Closure of \(a,b\) gives 60 maps and closure of \(a,b,z\) gives 120. The spherical \((2,3,5)\) triangle-group presentation and these orders identify \(R\cong A_5\), so \(G\cong A_5\times C_2\).

**Step 3: compute the top homology character.** For an automorphism \(g\), write \(t_k(g)\) for the trace on oriented \(k\)-chains. For each simplex preserved setwise by \(g\), its contribution to \(t_k(g)\) is the sign of the restricted vertex permutation; all other simplices contribute zero. The reduced Hopf trace formula, valid because homology is concentrated in even degree two, is
\[
\chi(g)=-1+\sum_{k=0}^{4}(-1)^kt_k(g).
\]
Exact enumeration of the 120 automorphisms and all 264 nonempty faces gives the table below. Signs \(+\) and \(-\) indicate whether the automorphism preserves or reverses the oriented boundary sphere, \(o(g)\) is its order, and \(f(g)\) its number of fixed graph vertices.

| Sign | \(o(g)\) | \(f(g)\) | Number of elements | \(\chi(g)\) |
|:---:|---:|---:|---:|---:|
| \(+\) | 1 | 12 | 1 | 23 |
| \(+\) | 2 | 0 | 15 | 3 |
| \(+\) | 3 | 0 | 20 | -1 |
| \(+\) | 5 | 2 | 24 | 3 |
| \(-\) | 2 | 0 | 1 | -1 |
| \(-\) | 2 | 4 | 15 | -5 |
| \(-\) | 6 | 0 | 20 | -1 |
| \(-\) | 10 | 0 | 24 | -1 |

The two distinct order-five rotation classes of \(A_5\) have the same character value, so combining them in the table loses no character information. An independent derivation in `verify_icosahedral_orbits.py` enumerates unions of vertex cycles of each automorphism and uses the equivalent sign \((-1)^{|\sigma|-c(\sigma)}\), where \(c(\sigma)\) counts the selected vertex cycles.

**Step 4: split by central inversion and decompose over \(\mathbb Q\).** The two eigenspace characters of \(z\), evaluated at each \(h\in A_5\), are
\[
\chi_+(h)=\frac{\chi(h)+\chi(zh)}2,
\qquad \chi_-(h)=\frac{\chi(h)-\chi(zh)}2.
\]
On the identity, elements of order two, elements of order three and either order-five class, their value vectors are respectively
\[
\chi_+=(11,-1,-1,1),\qquad\chi_-=(12,4,0,2).
\]
Comparison with the ordinary \(A_5\) irreducible character table gives \(\chi_+=\chi_{V_6}+\chi_{V_5}\) and \(\chi_-=2\chi_{\mathbf1}+2\chi_{V_5}\). This establishes the rational decomposition in the Finding.

**Step 5: passage to quotients.** Barycentric subdivision removes cell inversions. For a finite group acting simplicially, the rational chain complex of the geometric quotient identifies with invariant rational chains, hence the quotient's rational homology equals invariant rational homology. The \(A_5\)-fixed subspace in the displayed decomposition has dimension two, both basis dimensions lying in the \(z\)-odd part. Hence \(\dim\widetilde H_2(|X|/A_5;\mathbb Q)=2\) and the central inversion eliminates both classes on further passage to \(G\). All other reduced quotient groups vanish.

## Verification
Run `python3 verify_icosahedral_character.py` and `python3 verify_icosahedral_orbits.py` with Python 3.10 or later, using no third-party packages. Both scripts reconstruct their objects from the published edge and neighborhood data, respectively. The first computes exact mod-two boundary ranks and independently enumerates all graph automorphisms by triangle images; the second constructs the group from three permutations and derives traces from vertex-cycle unions. Both return `VERIFY_OK`, with the same 120-element class counts, homology character and quotient invariant dimensions. No stochastic sampling or numerical rank threshold is used.

## Relationship to prior work
The exact ordinary homotopy classification \(\mathcal N(I)\simeq\bigvee^{23}S^2\) was previously obtained by an explicit discrete-Morse matching in the published record listed below; this paper **does not claim** that sphere-wedge classification as original. Its numerical Betti number alone does not determine the group action: distinct \(23\)-dimensional representations have different class traces and symmetry quotient homology.

Dochtermann and Schultz give general equivariant Hom-complex methods, Matsushita develops neighborhood-complex fundamental groups and covering theory, and Shukla classifies neighborhood complexes for degree-at-most-three graphs and four-regular circulants. Their inspected theorems do not specify the \(A_5\times C_2\) character on this five-regular icosahedral graph. The four basic originality comparisons—equivalent `Hom(K_2,I)` formulations, stronger equivariant results, exact data records, and implication from the prior homotopy type—found no covering character theorem. Undiscovered or unindexed computations remain a bibliographic risk, so absolute priority is not asserted.

## Limitations
This is an exact finite-graph calculation, not a theorem for arbitrary vertex-transitive graphs. It determines the rational representation but does not identify the integral \(\mathbb Z[G]\)-lattice, integral torsion in quotient spaces, or their equivariant homotopy types. The two scripts provide exhaustive finite calculations and the proof explains why those calculations entail the claimed rational theorem; there is no claimed independent external audit.

## References
1. Anton Dochtermann and Carsten Schultz, *Topology of Hom complexes and test graphs for bounding chromatic number*, arXiv:0907.5079, first publicly posted 29 July 2009; especially the equivariant Hom-complex results. https://arxiv.org/abs/0907.5079
2. Takahiro Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first publicly posted 10 October 2012. https://arxiv.org/abs/1210.2803
3. Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first publicly posted 13 February 2018. https://arxiv.org/abs/1802.04526
4. *The icosahedral neighborhood complex is a wedge of twenty-three 2-spheres*, published research record (2026), full finding and Morse verification: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-icosahedral-neighborhood-complex-is-a-wedge-of-twenty-three--07e6e60de0e7
