# Two five-primary Moore summands in the alternating-diagonal five-by-five chessboard quotient

## Finding
Let \(\Delta_{5,5}\) be the simplicial complex of partial injective maps from five labelled elements to five labelled elements: its vertices are board squares \((i,j)\), and a face is a placement of pairwise nonattacking rooks. Let \(A_5\) act by **simultaneous even relabeling** \(g(i,j)=(g(i),g(j))\). For the ordinary geometric quotient \(Y=|\Delta_{5,5}|/A_5\), there is an integral homotopy equivalence
\[
Y\simeq M(\mathbb Z/5\mathbb Z,2)\vee M(\mathbb Z/5\mathbb Z,2),
\]
where \(M(\mathbb Z/5\mathbb Z,2)\) is the Moore space formed from \(S^2\) by attaching a three-cell along a degree-five map. In particular \(\pi_1(Y)=0\), \(\widetilde H_2(Y;\mathbb Z)\cong(\mathbb Z/5\mathbb Z)^2\), and all other reduced integral homology groups vanish.

## Assumptions and scope
All topology is ordinary (not Borel-equivariant) topology. The base complex is the **full** five-by-five chessboard complex, including all nonempty nonattacking placements of one through five rooks. The acting group is the diagonal \(A_5\) of order \(60\), not the independently acting row and column groups, not the diagonal \(S_5\) of order \(120\), and not a cyclic subgroup. The quotient is taken after geometric realization; no assumption of a free action is made.

## Proof
**1. Exact quotient CW model.** Barycentrically subdivide \(\Delta_{5,5}\). A vertex of this subdivision is a nonempty partial matching, and a simplex is a strictly nested chain of nonempty matchings. Because all vertices within a chain have distinct matching cardinalities, the diagonal group action has no simplex inversions. Its geometric quotient therefore has one oriented simplicial cell for each orbit of chains, with boundary obtained by deleting each chain member with its alternating sign. Enumerate all partial injections and all chains and then take each orbit's lexicographically least bitmask tuple. The cell counts in dimensions \(0,1,2,3,4\) are exactly \((45,308,744,720,240)\). The executable verifier constructs these cells from the definition, not from a stored orbit table, and checks every composition of successive cellular boundaries vanishes.

**2. Geometric collapses and integral computation.** Every one of the \(240\) four-cells has a successively chosen free three-face, and after these cancellations another \(404\) three-cells have successively chosen free two-faces. No lower-dimensional cancellations are used. The resulting genuine three-dimensional CW complex has cells \((45,308,340,76)\). It deformation retracts from \(Y\) through \(644\) elementary free-face collapses. Exact integer row and column operations on its cellular boundary matrices give nonzero Smith factors
\[
\begin{array}{c|c}
\partial_1&1\text{ repeated }44\text{ times}\\
\partial_2&1\text{ repeated }264\text{ times}\\
\partial_3&1\text{ repeated }74\text{ times},\quad5,5.
\end{array}
\]
The last result comes from \(74\) determinant-one integer pivot cancellations leaving two independent columns with entries \((5,-5)\), on disjoint row supports. Consequently the only nontrivial positive-degree homology is the asserted two-dimensional order-five torsion group.

**3. Fundamental group.** The classical chessboard-connectivity theorem gives that \(|\Delta_{5,5}|\) is simply connected: its connectivity lower bound is \(\min(5,5,\lfloor11/3\rfloor)-2=1\). Every three-cycle in the diagonal \(A_5\) action fixes a diagonal-square vertex \((i,i)\) with \(i\) among its two unmoved labels. Three-cycles generate \(A_5\). Armstrong's orbit-space fundamental-group theorem therefore gives \(\pi_1(Y)=A_5/A_5=0\).

**4. Homotopy type.** As \(Y\) is simply connected, Hurewicz identifies \(\pi_2(Y)\) with its second integral homology. Choose two homotopy classes representing its two independent elements of order five; their fifth multiples are null-homotopic and hence define a map from the wedge of the two degree-five three-cell Moore spaces to \(Y\). This map is an integral homology isomorphism in every dimension: both spaces have \(\widetilde H_2\cong(\mathbb Z/5\mathbb Z)^2\) and no other reduced homology. The homological Whitehead theorem for simply connected CW complexes makes it a homotopy equivalence.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier enumerates all \(1545\) nonempty matchings and all \(60\) even permutations; builds all orbit-chain cells, checks signed cellular boundary compositions, validates each of the \(644\) top-down geometric free-face collapses, and reduces all three surviving integral boundary maps by determinant-one operations to the displayed Smith factors. Its success marker is `DIAGONAL_A5_CHESSBOARD_TWO_FIVE_MOORE_SPACES_OK`. The mathematical connectivity, orbit-space fundamental-group, and homological Whitehead steps are stated and justified above rather than claimed as consequences of finite enumeration.

## Relationship to prior work
Björner–Lovász–Vrećica–Živaljević established the chessboard-complex connectivity theorem, investigated small square chessboard complexes, and developed the foundational framework in 1994. Their result concerns the unreduced complex; it does not classify this diagonal-alternating geometric quotient. Armstrong's 1965 theorem supplies the fundamental-group step. The previously reported full diagonal \(S_5\) quotient has the homotopy type of **one** \(M(\mathbb Z/5\mathbb Z,2)\); the present index-two alternating quotient has **two** such summands. Existing calculations for a diagonal cyclic subgroup similarly do not determine the quotient by its substantially larger alternating group, because the relevant actions have fixed points and ordinary quotient homology is not obtained by naïvely taking subgroup invariants.

## Limitations
This theorem concerns exactly the five-label square chessboard, the specified simultaneous even-label action and ordinary integral homotopy type. It makes no claim about all board sizes or a full group-action classification. No independent mathematical audit or formal proof assistant is claimed. The classification of the quotient uses a complete, reproducible finite cellular computation coupled with classical topological theorems. Some closely related indexed results were available as scientific summaries rather than accessible full text, so a publication-priority risk from an unindexed or inaccessible equivalent source remains.

## References
- A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. 49 (1994), 25–39, https://doi.org/10.1112/jlms/49.1.25. First publication 1 February 1994.
- M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. 61 (1965), 639–646, https://doi.org/10.1017/S0305004100038974.
- S. T. Vrećica, R. T. Živaljević, *Chessboard complexes indomitable*, arXiv:0911.3512, https://arxiv.org/abs/0911.3512 (general background).
- *Five-primary Moore homotopy in the diagonal symmetric quotient of a chessboard complex*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-five-primary-moore-homotopy-in-the-diagonal-symmetric-quotient-o--00ec8ccb6aa0.
- *Prime-order second homotopy in diagonal cyclic quotients of square chessboard complexes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-prime-order-second-homotopy-in-diagonal-cyclic-quotients-of-squa--2c10a7de25b1.
