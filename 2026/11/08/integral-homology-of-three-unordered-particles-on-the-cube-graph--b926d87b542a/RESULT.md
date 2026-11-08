# Integral homology of three unordered particles on the cube graph

## Finding

Let \(Q_3\) denote the graph with vertices \(\{0,1,\dots,7}\), with \(a\) adjacent to \(b\) exactly when their three-bit binary representations differ in one bit. Let \(B_3(Q_3)\) be the space of three-element subsets of the geometric realization \(|Q_3|\), with the collision-free configuration-space topology. Its complete integral homology is

\[
H_i(B_3(Q_3);\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^6,&i=1,\\
\mathbb Z^{17},&i=2,\\
0,&i\ge3.
\end{cases}
\]

Every group is free abelian, including the second homology group.

## Assumptions and scope

All particles are unlabeled, mutually distinct, and move continuously on the **geometric realization** of the eight-vertex, twelve-edge cube graph, not within the three-dimensional solid cube. There are exactly three particles. Homology is ordinary singular homology with integral coefficients. No assertion is made about spaces with other particle numbers or other graphs.

## Proof

**Integral graph-configuration chain model.** The comparison theorem for the Świątkowski chain complex [2] identifies the singular homology of an unordered graph configuration space with the homology of its weight-graded integral chain complex. Proposition 4.9 of [2] allows replacing the full local generator module by the reduced module spanned by \(\varnothing\) and differences of half-edge generators. For each vertex \(v\) of the cube, list its three incident graph-edge variables in ascending index order as \(e_0(v),e_1(v),e_2(v)\). Use the local basis \(h_1(v)-h_0(v)\), \(h_2(v)-h_0(v)\) with differential

\[
\partial(h_j(v)-h_0(v))=e_j(v)-e_0(v),\qquad j\in\{1,2}.
\]

A degree-\(k\), weight-three basis monomial consists of \(k\) distinct chosen local half-edge differences at \(k\) different vertices (at most one at each vertex), with three minus \(k\) freely repeating graph-edge variables. The exterior sign is the parity of the position of the removed local difference in the vertex-ascending order. Direct counting yields the chain-complex ranks

\[
\operatorname{rank}C_0=364,\quad
\operatorname{rank}C_1=1248,\quad
\operatorname{rank}C_2=1344,\quad
\operatorname{rank}C_3=448,
\]

and no higher terms. The two consecutive composite matrices have every entry zero. The actual matrices are built from these explicit basis conventions, not fitted to expected ranks.

**Integral elementary cancellation.** For each of the matrices \(D_2:C_2\to C_1\) and \(D_3:C_3\to C_2\), the attached verifier repeatedly selects a coefficient of magnitude one and uses exact integer elementary column operations to eliminate the rest of its row, then deletes the selected row and column. All choices are deterministic (minimum fill cost, then row and column indices). The complete exact result is

\[
\operatorname{SNF}(D_2)=\operatorname{diag}(\underbrace{1,\ldots,1}_{879},0,\ldots,0),\qquad
\operatorname{SNF}(D_3)=\operatorname{diag}(\underbrace{1,\ldots,1}_{448},0,\ldots,0).
\]

In both cases the sparse residual matrix is **identically zero**, not merely rank-deficient modulo a prime. Every pivot is a unit, hence both images are saturated direct summands of their target free modules, and the corresponding homology quotients have no torsion.

The graph \(Q_3\) is connected, and the configuration space of three unordered distinct points on a connected graph with a trivalent vertex is path connected: one may move the particles successively to standard positions while routing around any occupied points through a trivalent branch. Thus \(H_0\cong\mathbb Z\) and the rank of \(D_1\) is \(363\). Applying rank-nullity to the integral chain complex gives

\[
\begin{aligned}
\operatorname{rank}H_1&=(1248-363)-879=6,\\
\operatorname{rank}H_2&=(1344-879)-448=17,\\
\operatorname{rank}H_3&=448-448=0.
\end{aligned}
\]

For torsion-freeness: \(C_1/\operatorname{im}D_2\) and \(C_2/\operatorname{im}D_3\) are free abelian by the unit-pivot certificates; their subgroups representing \(H_1\) and \(H_2\) are therefore free. Degree zero is free by connectedness.

## Verification

Execute `python3 verify_cube_graph.py` (standard Python, no external packages) alongside the other files in this folder. It reconstructs the graph and all integral boundary matrices, checks the two chain-condition identities, performs 879 and 448 exact unit-pivot reductions with zero remaining matrices, and prints `CUBE_THREE_PARTICLE_INTEGRAL_HOMOLOGY_PASS`. `verification_output.txt` is the recorded output. The proof depends on the explicit chain model and the described finite exhaustive cancellations, not on modular ranks or a timeout.

## Relationship to prior work

Ko–Park [1] compute the first homology of graph braid groups in general, but do not give the integral second-homology rank for three particles on the cube. An–Drummond-Cole–Knudsen [2] supply the graph-configuration chain comparison, not this cube-specific matrix calculation. An–Knudsen [3] prove that second homology for **all planar graphs** is generated by toric and theta classes, but do not determine the number of independent degree-two classes or all relations for the cube; indeed, they explicitly identify the general problem of relations and combinatorial bases as open directions. This numerical and torsion-free classification does not follow from the statements inspected there. Earlier work by Świątkowski [4] underlies the chain-complex method. The exact rank 17 and absence of higher homology have not been located in inspected primary statements or mathematical records; further external verification of publication priority remains appropriate.

## Limitations

This is a finite, exact integral homology computation for \(B_3(Q_3)\). It is **not** a determination of the fundamental-group presentation, cup-product ring, equivariant module structure, or homotopy type. It does not classify other particle numbers. The mathematical review is same-model only; no independent expert audit has been performed.

## References

[1] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first public version January 13, 2011.
[2] B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351, Definition 4.7, Proposition 4.9 and Theorem 4.5.
[3] B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020), Theorem 1.1 and §7.
[4] J. Świątkowski, *Estimates for homological dimension of configuration spaces of graphs*, Colloquium Mathematicum 89 (2001), 69–79, doi:10.4064/cm89-1-5.
