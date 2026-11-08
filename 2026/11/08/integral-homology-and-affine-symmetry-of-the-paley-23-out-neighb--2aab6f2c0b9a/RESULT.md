# Integral homology and affine symmetry of the Paley-23 out-neighborhood complex

## Finding
Let \(Q=\{1,2,3,4,6,8,9,12,13,16,18\}\subset\mathbb F_{23}\) be the nonzero quadratic residues. The Paley tournament \(T\) has an arc \(u\to v\) exactly when \(v-u\in Q\). Define \(K\) to be the abstract simplicial complex whose nonempty faces \(S\) satisfy \(S\subseteq u+Q\) for some \(u\in\mathbb F_{23}\). Then its **complete reduced integral homology** is

\[
\widetilde H_i(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{209},&i=3,\\
\mathbb Z,&i=4,\\
0,&i\ne3,4.
\end{cases}
\]

The natural affine group \(G=\mathbb F_{23}\rtimes Q\), of order \(253\), acts on \(K\). Let \(W=\mathbb Q^{\mathbb F_{23}}/\mathbb Q\mathbf1\) be the \(22\)-dimensional reduced affine permutation module, and let \(R\) be the \(11\)-dimensional regular rational representation of \(G/\mathbb F_{23}\cong C_{11}\), inflated to \(G\). Then

\[
\widetilde H_3(K;\mathbb Q)\cong R\oplus W^{\oplus9},\qquad
\widetilde H_4(K;\mathbb Q)\cong\mathbb Q
\]

as rational \(G\)-representations; the second representation is trivial. Consequently the ordinary orbit space has

\[
\widetilde H_i(K/G;\mathbb Q)\cong
\begin{cases}\mathbb Q,&i=3,4,\\0,&\text{otherwise}.\end{cases}
\]

## Assumptions and scope
All faces are *irreflexive outward-neighborhood* subsets: a witnessing vertex cannot witness itself. This is a Dowker or directed neighborhood complex, not the directed flag complex of transitive subtournaments and not the ordinary undirected Paley-graph neighborhood complex. Integer simplicial boundaries use increasing vertex order and alternating signs. Only the displayed natural affine subgroup is used; equality with the full automorphism group is not asserted. No integral homotopy wedge or equivariant homotopy decomposition is claimed.

The established \(3\)-existentially-closed property of \(T\) motivates studying this example. It implies every three-element subset belongs to \(K\), so \(K\) has the complete two-skeleton on \(23\) vertices; this fact is also checked directly.

## Proof
**Face construction and finite boundary problem.** For each \(u\in\mathbb F_{23}\), the set \(u+Q\) is a facet of size \(11\). All \(23\) facets are distinct. Enumerating every submask of these facets gives exactly \(42{,}298\) faces including the empty face. In degrees \(0\) through \(10\), the face vector is

\[
(23,253,1771,6325,10373,10626,7590,3795,1265,253,23).
\]

This is exhaustive since membership in \(K\) is, by definition, membership in the downward closure of these \(23\) sets.

**Integral Morse reduction.** The accompanying `verify.py` uses a fixed deterministic matching: scan vertex labels in ascending order; at each label pair each currently unmatched face without that vertex to its one-vertex extension when both faces exist, processing faces by cardinality and mask order. It includes the empty face. The result is \(20{,}762\) matched pairs and critical cells only in dimensions \(2,3,4,5\), of respective counts \((21,443,262,48)\). The code explicitly orients and topologically sorts **all** \(244{,}421\) cover relations of the complete augmented face poset, reversing exactly matching arrows. All \(42{,}298\) faces appear in the topological ordering, so the matching is acyclic.

The code computes signed integer Morse boundary maps by recursive unit-coefficient elimination along the matched pairs (not by merely counting critical cells). In dimensions \(3,4,5\), their matrix sizes and complete Smith normal forms are

\[
\begin{array}{c|c|c}
\partial_3&21\times443&1^{\times21},\ 0^{\times422}\\
\partial_4&443\times262&1^{\times213},\ 0^{\times49}\\
\partial_5&262\times48&1^{\times48}.
\end{array}
\]

Exact integer multiplication confirms \(\partial_3\partial_4=0\) and \(\partial_4\partial_5=0\). The ranks are therefore \(21,213,48\). No nonzero Smith factor is nonunit, so the resulting reduced integral homology is torsionfree. The free ranks are \(443-21-213=209\) in degree \(3\) and \(262-213-48=1\) in degree \(4\), with zero in all other degrees. Discrete Morse cancellation over \(\mathbb Z\) preserves homology, proving the first assertion.

**Affine character and quotient.** Each \(g(x)=ax+b\) with \(a\in Q\), \(b\in\mathbb F_{23}\), preserves every facet family. Its order is odd. Thus the one-dimensional rational \(H_4\)-module is trivial. A nonidentity translation fixes no nonempty proper vertex subset, so its reduced chain Lefschetz number is \(-1\). A nonidentity multiplier-affine element fixes exactly one vertex and one eleven-vertex facet setwise, and acts on the latter by an eleven-cycle with sign \(+1\). Its reduced Lefschetz number is \(1+1-1=1\). The Hopf trace identity then gives the \(H_3\)-character:

\[
\chi_3(g)=\begin{cases}209,&g=1,\\2,&g\text{ is a nonzero translation},\\0,&\text{otherwise}.
\end{cases}
\]

The module \(W\) has character \((22,-1,0)\) on these same three element types, and \(R\) has \((11,11,0)\), hence \(\chi_R+9\chi_W=(209,2,0)\). Semisimplicity of rational representations of finite groups proves the asserted module isomorphism. Averaging the characters gives one invariant dimension in each of degrees \(3,4\). Rational simplicial transfer, using barycentric subdivision to make the action admissible, identifies these invariant groups with homology of \(K/G\).

## Verification
Run `python verify.py` with Python \(3.10\) or later and SymPy \(1.14\). `verification_output.txt` records the exact output. The verifier reconstructs all faces; checks the complete two-skeleton, an exhaustive directed-acyclicity topological sort, all integer reduced Morse differentials and complete Smith normal forms; and independently enumerates the \(253\) affine transformations to check their fixed-face patterns. It prints `ALL_CHECKS_PASS` upon success. The computation is a finite exhaustive proof of the exact finite assertion; it is **not** an assertion about other Paley tournaments or all skew Hadamard designs.

## Relationship to prior work
Bonato, Gordinowicz and Prałat (2010) identify the order-\(23\) Paley tournament as \(3\)-existentially closed and study adjacency properties and doubly regular tournaments, but do not calculate the stated complex's homology. Chowdhury and Mémoli (first public preprint August 18, 2016) give general functorial Dowker-network methods, but no such exact Paley-\(23\) calculation. Dochtermann and Singh (2021) study directed neighborhood complexes and prove general high-degree vanishing bounds; their results do not fix the nonzero degree-\(3\) and degree-\(4\) ranks or their affine characters. Previously reported directed flag complexes of Paley tournaments concern a **different** simplicial construction; smaller Paley out-neighborhood examples do not imply this finite case. No published theorem implying the full result was located in the searched sources, but unindexed prior work remains possible.

## Limitations
This establishes integral homology, not the homotopy type, integral automorphism modules or integral homology of the orbit space. It does not identify every automorphism of \(K\), nor classify higher-order Paley tournaments or arbitrary designs with the same parameters. Symbolic computation is reproducible from the attached script, with the exact finite proofs dependent on its correct execution and on the stated unit-pivot integer linear algebra algorithms. Independent validation and definitive publication-priority assessment have not been performed.

## References
1. A. Bonato, P. Gordinowicz and P. Prałat, *Bounds and constructions for n-e.c. tournaments*, Contributions to Discrete Mathematics **5** (2010), 52–66. DOI: `10.55016/ojs/cdm.v5i2.62061`. Original publisher date: 2010-09-28. Full author-uploaded text: https://www.researchgate.net/publication/234018219_Bounds_and_constructions_for_n-ec_tournaments.
2. S. Chowdhury and F. Mémoli, *A functorial Dowker theorem and persistent homology of asymmetric networks*, preprint arXiv:1608.05432, first public 2016-08-18, subsequently journal publication.
3. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, preprint arXiv:2108.10948, first public 2021-08-24.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145 (standard discrete-Morse cancellation framework).
