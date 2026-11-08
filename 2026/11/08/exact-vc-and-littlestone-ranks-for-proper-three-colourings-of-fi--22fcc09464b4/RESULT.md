# Exact VC and Littlestone ranks for proper three-colourings of finite cycles

## Finding
Let \(n\ge 3\), let \(C_n\) be the simple cycle on vertices \(0,\ldots,n-1\), and let \(F_n\) be the set of all proper maps \(f:\{0,\ldots,n-1\}\to\{0,1,2\}\), meaning \(f(i)\ne f(i+1\bmod n)\). Regard each map as the Boolean concept \(h_f(i,a)=\mathbf 1[f(i)=a]\), with query domain \(X_n=\{0,\ldots,n-1\}\times\{0,1,2\}\). Then for every \(n\ge3\),

\[
\operatorname{VCdim}(\{h_f:f\in F_n\})=\left\lfloor\frac{3n}{4}\right\rfloor,
\qquad
\operatorname{Ldim}(\{h_f:f\in F_n\})=n-1.
\]

Thus the online-minus-static gap is \(\lceil n/4\rceil-1\), which grows without bound on a single connected graph family; it first becomes positive at \(n=5\). These are binary **vertex–colour equality** queries, not queries returning an entire colour or identifying an unknown graph.

## Assumptions and scope
Colours are three distinct named symbols. All proper colourings are hypotheses; no global colour-symmetry quotient is taken. Both dimensions concern the same finite Boolean class on the \(3n\) possible coordinate–colour tests. A subset of tests is VC-shattered when all its binary traces occur. A complete online mistake tree of depth \(d\) has one binary test at each internal node and a realizing proper colouring on every one of its \(2^d\) branches. No statement is made for fewer or more than three colours, for noncyclic graphs, or for different feedback models.

## Proof
**1. At most one query per vertex in a shattered set.** Two different colour-equality tests at one vertex cannot both be positive. Hence a shattered set of tests selects at most one prescribed colour \(a_i\) at each selected vertex \(i\).

**2. Three and four consecutive selected vertices.** Suppose three consecutive vertices \(i,i+1,i+2\) all carry selected tests. All-positive realizability forces \(a_i\ne a_{i+1}\) and \(a_{i+1}\ne a_{i+2}\). If their prescribed colours are all different, the trace \((1,0,1)\) is impossible: the two positive endpoints fix different colours, and the middle vertex is forced to take the third colour, namely its prescribed colour. Therefore a shattered collection containing such a triple must have \(a_i=a_{i+2}\). If four consecutive vertices are selected, the overlapping triples force prescribed colours \((A,B,A,B)\) with \(A\ne B\). The trace \((1,0,0,1)\) is then impossible: the first and last vertices are fixed at \(A\) and \(B\); the second vertex is forced to the third colour \(C\), and the third vertex is then forced to \(B\), contradicting its adjacency to the final \(B\). Thus no four consecutive cycle vertices can be selected.

For \(n\ge4\), there are \(n\) cyclic windows of four distinct vertices. Each contains at most three selected vertices, while each selected vertex belongs to exactly four windows. Therefore \(4|S|\le3n\), giving \(|S|\le\lfloor3n/4\rfloor\). For \(n=3\), three selected tests would require all three prescribed colours to be different (because the cycle is a triangle), but would then fail the \((1,0,1)\) trace. Hence \(\operatorname{VCdim}\le 2=\lfloor9/4\rfloor\).

**3. A shattered support meeting the upper bound.** Write \(n=4k+r\), where \(0\le r\le3\). Place \(k\) successive cyclic blocks of length four with selected/unselected pattern \(1110\). If \(r=1,2,3\), follow these blocks respectively by \(0\), \(10\), or \(110\). This chooses precisely \(3k+\lfloor3r/4\rfloor=\lfloor3n/4\rfloor\) tests. In each selected run of length up to three, prescribe alternating colours \(0,1,0\) (truncated for shorter runs). Each run is VC-shattered in isolation. In the three-vertex case, every binary trace is realized by a proper colouring; in lexicographic trace order \(000,001,010,011,100,101,110,111\), explicit realizing colour strings are respectively \(101,120,212,210,021,020,012,010\). The one- and two-vertex cases follow by restriction. Selected runs are separated by at least one unselected vertex. Once a proper colouring has been chosen on every selected run, each intervening unselected vertex can be coloured differently from its two neighbours using one of the three colours (and any longer gap can be filled greedily). For the displayed block construction every gap has length one, except possibly two adjacent unselected vertices when \(r=1\); a gap of length two can likewise be filled because the corresponding three-edge path always admits an extension with any fixed endpoint colours. Thus arbitrary traces on all selected runs extend simultaneously to a proper colouring of the whole cycle. This proves the VC lower bound, including \(n=3\).

**4. An online tree of depth \(n-1\).** At the root ask whether vertex \(0\) has colour \(0\). On its positive branch restrict to colour \(0\) at that vertex; on its negative branch restrict to colour \(1\). Along each branch, query vertices \(1,2,\ldots,n-2\) successively. When the preceding vertex has already been assigned colour \(c\), exactly two colours \(u,v\) remain; ask whether the current vertex has colour \(u\), and assign \(u\) on a positive answer and \(v\) on a negative answer. Every binary response sequence is therefore realized on the first \(n-1\) vertices. The final vertex has at most two forbidden neighbour colours, and thus at least one available colour. This constructs a complete depth-\((n-1)\) online mistake tree.

**5. Optimality of online depth.** A proper \(3\)-colouring of a cycle corresponds to a closed length-\(n\) walk in the three-state graph with transition matrix \(J-I\). That matrix has eigenvalues \(2,-1,-1\), so the number of proper colourings is exactly \(|F_n|=2^n+2(-1)^n\). Colour permutations act transitively on the three possible colours at any specified vertex; hence the positive branch at *every* query contains exactly \(|F_n|/3\) concepts. For every \(n\ge3\),
\[
\frac{2^n+2(-1)^n}{3}\le\frac{2^n+2}{3}<2^{n-1}.
\]
A binary mistake tree of depth \(n\) would need \(2^{n-1}\) different realizing concepts in its root-positive subtree, an impossibility. Therefore \(\operatorname{Ldim}\le n-1\), proving equality.

## Verification
The standalone standard-library Python program `check_cycle.py` exhaustively generates all proper three-colourings of \(C_n\). For \(3\le n\le8\) it calculates the exact static shattering dimension by enumerating every possible one-test-per-vertex support. For \(3\le n\le7\) it independently evaluates the exact online minimax recurrence. Through \(n=10\), it separately checks the constructive VC witness and every branch of the explicit depth-\((n-1)\) online tree. The recorded output `checks_output.txt` ends with `ALL_CYCLE_3_COLORING_SHATTERING_CHECKS_PASS`. The proof above, not the finite computations, justifies all \(n\ge3\).

## Relationship to prior work
The 2017 preprint *Structure Learning of H-colorings* by Blanca, Chen, Vigoda and Štefankovič studies recovery of an unknown graph from random proper-colouring samples. It provides the same natural proper-colouring objects but does not address VC or Littlestone ranks of the one-hot coordinate-membership concept class. The 2021 paper *Littlestone and VC-dimension of families of zero sets* by Guingona, Kolesnikov, Nierwinski and Soucy proves equal dimensions for zero-set families of linear combinations; that theorem does not imply the strict gap here. Walker's 2022 *Tree Dimension and the Sauer–Shelah Dichotomy* gives general tree-shattering bounds but not the two exact ranks of the cyclic proper-colouring family.

The path-colouring analogue has different dimension formulas, but a cycle's closing edge changes the admissible hypotheses and neither dimension can simply be carried over. The present proof identifies the cyclic four-window obstruction and one-endpoint online constraint explicitly. Searches under equivalent wording, cyclic words, graph homomorphisms to the three-colour constraint graph, and antiferromagnetic three-state configurations did not locate an equivalent statement in the accessible records; absence from a search index is not a proof of historical uniqueness.

## Limitations
The theorem is for finite simple cycles with three named colours and binary vertex–colour tests. The VC proof establishes a maximum size, not a classification of all individual shattered supports. The checker stops at the stated finite sizes, while the universal assertion is purely deductive. A comprehensive historical-priority review and independent mathematical audit have not been performed. This result does not address sample complexity for learning an unknown underlying graph.

## References
- A. Blanca, Z. Chen, E. Vigoda, and D. Štefankovič, *Structure Learning of H-colorings*, arXiv:1708.05118, first posted 17 August 2017, https://arxiv.org/abs/1708.05118.
- V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first posted 10 September 2021, https://arxiv.org/abs/2109.04805.
- R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted 23 March 2022, https://arxiv.org/abs/2203.12211.
