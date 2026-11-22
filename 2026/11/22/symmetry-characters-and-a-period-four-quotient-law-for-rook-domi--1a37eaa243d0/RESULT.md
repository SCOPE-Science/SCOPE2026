# Symmetry characters and a period-four quotient law for rook dominance complexes

## Finding
Let \(p,q\ge3\) be integers, let \(R_{p,q}=K_p\square K_q\) be the graph on \([p]\times[q]\) whose distinct vertices are adjacent exactly when a coordinate agrees, and let \(D_{p,q}\) consist of all sets whose complements dominate \(R_{p,q}\). The coordinate-permutation group \(S_p\times S_q\) acts simplicially on \(D_{p,q}\). Write \(\varepsilon_p\) and \(\varepsilon_q\) for the integral sign characters of the two factors. All reduced integral homology is free, with exactly the following three **graded rank-one character summands** (repeated degrees mean a direct sum):
\[
\begin{array}{c|c}
\text{homological degree}&\mathbb Z[S_p\times S_q]\text{-module}\ \\ \hline
pq-p-1 & \varepsilon_p^{\otimes(q+1)}\boxtimes\varepsilon_q^{\otimes p} \\
pq-q-1 & \varepsilon_p^{\otimes q}\boxtimes\varepsilon_q^{\otimes(p+1)} \\
(p-1)(q-1)&\varepsilon_p^{\otimes(q+1)}\boxtimes\varepsilon_q^{\otimes(p+1)}
\end{array}
\]
Every other reduced integral homology group vanishes. The formula determines the full graded character of the complete automorphism group when \(p\ne q\).

When \(p=q=n\ge3\), the full automorphism group is \((S_n\times S_n)\rtimes C_2\), with the last generator \(\tau\) transposing the board. It exchanges the two upper-degree rank-one summands. On the unique lower-degree summand, in degree \((n-1)^2\), it acts by
\[
\boxed{\tau_*=(-1)^{\binom n2+(n-2)^2}.}
\]
These statements also determine the rational homology of the quotient by **every** subgroup \(H\) of the automorphism group: average the displayed graded character over \(H\). In particular, for the full automorphism group of a rectangular board with \(p\ne q\), the reduced rational quotient homology is one-dimensional in degree \(pq-p-1\) when \(p\) is even and \(q\) is odd, one-dimensional in degree \(pq-q-1\) when \(p\) is odd and \(q\) is even, one-dimensional in degree \((p-1)(q-1)\) when both are odd, and zero in every degree when both are even. For a square board the striking sharper law is
\[
\boxed{\widetilde H_i(D_{n,n}/\operatorname{Aut}(R_{n,n});\mathbb Q)\cong
\begin{cases}
\mathbb Q,&n\equiv3\pmod4,\ i=(n-1)^2,\\
0,&\text{otherwise}.
\end{cases}}
\]
This is a rational homology statement about topological quotients, not an assertion that those quotients are spheres or contractible.

## Assumptions and scope
All graph automorphisms act by permuting vertices, and the quotient means the topological orbit space of the geometric realization. Graphs are simple and undirected; domination uses **closed** graph neighborhoods, while the intermediary neighborhood complex below uses **open** neighborhoods of the graph complement. Integers \(p,q\ge3\) exclude exceptional zero-sphere bookkeeping. Character notation \(\boxtimes\) means external tensor product of rank-one integral representations; a tensor power of a sign character is trivial for even exponent and sign for odd exponent. For \(p=q\), the displayed direct sum is a decomposition under the normal subgroup \(S_n\times S_n\), while the transpose exchanges its two equal-degree upper summands. No canonical nonequivariant wedge decomposition is asserted to be group-equivariant.

## Proof
**1. Duality identifies the complex.** Let \(N=pq\) and write \(L=\mathcal N(\overline{R_{p,q}})\) for the ordinary open-neighborhood complex of the complement graph. For \((i,j)\), its open neighborhood in the complement is the rectangle
\[
B_{ij}=([p]\setminus\{i\})\times([q]\setminus\{j\}).
\]
The maximal simplices of \(L\) are these rectangles. The graph domination criterion shows directly that \(D_{p,q}=L^\vee\), the combinatorial Alexander dual on the fixed \(N\)-element vertex set: a complement fails to dominate precisely when it misses the entire closed neighborhood of some vertex. This identity is also Matsushita--Wakatsuki's general duality theorem.

**2. An equivariant product model for the neighborhood nerve.** Cover \(L\) by the simplices \(2^{B_{ij}}\). For a nonempty selection \(T\subseteq[p]\times[q]\), their intersection is a nonempty simplex exactly when the row-support \(r(T)\) and column-support \(c(T)\) are both proper subsets of \([p]\) and \([q]\). Thus their nerve \(K\) is the complex of all such nonempty selections, including their faces. The nerve equivalence is natural under coordinate permutations and board transpose. The order-preserving map
\[
\mathcal F(K)\longrightarrow \mathcal F(\partial\Delta^{p-1})\times\mathcal F(\partial\Delta^{q-1}),\qquad T\longmapsto(r(T),c(T))
\]
is equivariant. For every pair of nonempty proper sets \((A,B)\), the lower fiber consists of nonempty subsets of \(A\times B\), the face poset of a simplex, hence is contractible. Quillen's fiber lemma gives an equivariant map inducing an integral homology isomorphism
\[
\widetilde H^*(L;\mathbb Z)\cong\widetilde H^*(S^{p-2}\times S^{q-2};\mathbb Z)
\]
compatible with all coordinate permutations and the factor flip. The ordinary homotopy equivalence suffices here because the actual maps commute with the group; no equivariant fixed-point equivalence is claimed.

**3. Product cohomology characters.** The reduced top cohomology of \(\partial\Delta^{p-1}\) carries \(\varepsilon_p\), since a coordinate permutation acts on the oriented simplex boundary by its sign. By integral Künneth, the three cohomological lines are in degrees \(p-2\), \(q-2\), and \(p+q-4\), with respective characters \(\varepsilon_p\), \(\varepsilon_q\), and \(\varepsilon_p\boxtimes\varepsilon_q\). When \(p=q\), the first two lie in the same degree but remain two natural summands for the coordinate subgroup.

**4. The orientation twist in combinatorial Alexander duality.** The natural integral chain-level Alexander-duality correspondence between \(D_{p,q}=L^\vee\) and \(L\) reverses degrees by \(i\mapsto N-i-3\) and twists the group action by the orientation character \(\det(\mathbb Z^{[p]\times[q]})\). A row permutation \(\pi\) permutes \(q\) copies of its letter permutation, and a column permutation \(\sigma\) permutes \(p\) copies of its permutation. The twist is therefore
\[
\delta(\pi,\sigma)=\operatorname{sgn}(\pi)^q\operatorname{sgn}(\sigma)^p.
\]
Tensoring each product-cohomology line by \(\delta\) gives exactly the three degrees and integral characters in the statement. The integral groups are torsion-free because the product-cohomology groups are free. This argument uses the actual orientation sign, not an assumption that nonequivariant homotopy equivalences preserve representations.

**5. Board transpose and the mod-four law.** When the board is square, \(\tau:(i,j)\mapsto(j,i)\) permutes the \(n^2\) ground vertices by \(\binom n2\) disjoint transpositions, contributing orientation sign \((-1)^{\binom n2}\). On the top product-cohomology line the factor flip contributes the Koszul sign \((-1)^{(n-2)^2}\). Their product is the displayed scalar on the lower-degree line. The two other lines are exchanged, so the trace on their sum is zero for every symmetry involving the transpose. All statements extend to products of a transpose with arbitrary coordinate permutations by the group law.

**6. Rational quotients.** For a finite group acting simplicially on a finite complex, barycentric subdivision and rational transfer identify the rational homology of its orbit space with the invariant part of rational homology. For unequal side lengths the automorphism group is \(S_p\times S_q\); triviality of the three sign characters gives the stated parity cases. For square boards, the only coordinate-permutation-invariant line occurs when \(n\) is odd, namely the lower-degree one. The transpose fixes it exactly when \(n\equiv3\pmod4\), because then \((-1)^{\binom n2+(n-2)^2}=1\). This proves the period-four quotient law and, by character averaging, the assertion for all subgroups.

## Verification
The companion standalone Python program independently constructs the dominance face predicate directly from row and column domination, independently computes signed simplicial Lefschetz numbers by iterating all faces, and separately computes the same numbers by iterating invariant vertex-cycle unions. It compares both computations with the claimed character formula for 45 selected actions on boards of sizes \(3\times3\), \(3\times4\), and \(4\times4\), including the transpose and its products with permutations. The corresponding face counts are 420, 3614, and 59746, respectively. It additionally verifies the predicted rational-quotient reduced Euler characteristics by averaging over all 72, 144, and 1152 automorphisms in these cases. The actual output is in `verification_output.txt`; the general theorem rests on the preceding integral-equivariant proof, not extrapolation from finite cases.

## Relationship to prior work
Matsushita and Wakatsuki (2023) establish the dominance/open-neighborhood Alexander-dual identity and compute selected path-grid cases; they do not determine these rook-graph automorphism characters. Mertens (2024) computes the domination polynomial of rook graphs, including the row-or-column domination criterion, but this enumerative polynomial does not determine the action on homology or the homology of symmetry quotients. Björner and Tancer (2009) supply the standard nonequivariant combinatorial duality; the orientation-character naturality needed here is made explicit in Step 4. A public 2026 classification already proves the nonequivariant three-sphere wedge type for all rectangular rook dominance complexes, so **no nonequivariant homotopy or Betti-number novelty is claimed**. The present result determines previously unspecified integral symmetry representations and a full-automorphism rational quotient parity law; these do not follow from the nonequivariant wedge assertion alone. Standard graph-Hom product methods provide a related product-of-spheres viewpoint, but the asserted induced characters and orbit-space law require the sign-twisted duality and transpose action.

## Limitations
The result does not classify the integral torsion of orbit spaces, equivariant homotopy types, fixed-point sets, or integral cellular attaching maps of quotients. Neither rational homology-sphere behavior nor rational acyclicity establishes an actual sphere equivalence or contractibility. The computation of an explicit full character is a consequence of several classical constructions; unindexed prior equivariant calculations could give an equivalent result. No external independent audit or priority certification is claimed.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first public 2023-12-05. https://arxiv.org/abs/2312.02639
2. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716, first public 2024-01-01. https://arxiv.org/abs/2401.00716
3. A. Björner and M. Tancer, *Combinatorial Alexander Duality—A Short and Elementary Proof*, arXiv:0710.1172, first public 2007-10. https://arxiv.org/abs/0710.1172
4. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first public 2003-10. https://arxiv.org/abs/math/0310056
5. *Three-sphere homotopy types of rook-graph dominance complexes*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-sphere-homotopy-types-of-rook-graph-dominance-complexes--89367a150c4b
