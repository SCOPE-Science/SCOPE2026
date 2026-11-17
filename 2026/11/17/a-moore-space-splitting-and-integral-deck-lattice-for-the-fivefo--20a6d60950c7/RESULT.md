# A Moore-space splitting and integral deck lattice for the fivefold chessboard quotient

## Finding
Let \(\Delta_{3,5}\) be the ordinary chessboard complex of nonattacking rook placements on three labeled rows and five cyclically ordered columns. Write \(C_5=\langle \rho\rangle\), where \(\rho(r,c)=(r,c+1)\) on row-column coordinates \(r\in\{0,1,2\}\) and \(c\in\mathbb Z/5\mathbb Z\). The **ordinary geometric quotient** \(Y=|\Delta_{3,5}|/C_5\) has the integral homotopy type
\[
Y\simeq M(\mathbb Z/5\mathbb Z,1)\vee S^2\vee S^2,
\]
where \(M(\mathbb Z/5\mathbb Z,1)\) specifically denotes the standard two-cell Moore complex \(S^1\cup_{5}e^2\), with attaching map of degree five. Consequently,
\[
\pi_1(Y)\cong H_1(Y;\mathbb Z)\cong\mathbb Z/5\mathbb Z,\qquad
H_2(Y;\mathbb Z)\cong\mathbb Z^2,
\]
with \(H_0(Y;\mathbb Z)\cong\mathbb Z\) and all higher homology zero. The covering complex is \(|\Delta_{3,5}|\simeq\bigvee^{14}S^2\). More precisely, its **integral deck-group homology lattice** is
\[
\widetilde H_2(\Delta_{3,5};\mathbb Z)
\cong I_{C_5}\oplus\mathbb Z[C_5]^{\oplus2},
\]
where \(I_{C_5}=\ker(\varepsilon:\mathbb Z[C_5]\to\mathbb Z)\) is the augmentation ideal. The isomorphism is as \(\mathbb Z[C_5]\)-modules for the natural column-rotation action.

## Assumptions and scope
A simplex consists of at most three squares \((r,c)\), with no repeated row or column. Rows are fixed by rotation, and the action rotates all five columns simultaneously. The quotient is a topological orbit space of the geometric realization, **not** the abstract simplicial complex on column-rotation orbits of vertices. No quotient by reflections or row permutations is asserted. All homotopy equivalences concern CW spaces, not homeomorphism types. The ring \(\mathbb Z[C_5]\) acts on covering homology via the column-rotation deck action.

## Proof
**1. Freeness and a quotient cell structure.** A nontrivial column rotation cannot setwise preserve a nonempty rook placement: a face contains at most one square from each fixed row, so preserving the face forces the selected square in each row to be individually fixed, while a nontrivial rotation of five columns fixes no square. Consequently the action is free on the realization. The quotient inherits a finite two-dimensional \(\Delta\)-complex structure from simplex orbits. There are \(3\) quotient vertices, one for each row, \(12\) quotient edges, and \(12\) quotient triangles. Indeed, the source contains respectively \(15\), \(60\), and \(60\) nonempty simplices, and every orbit has size five.

Choose ascending row order as orientation. For \(i\in\{1,2,3,4\}\), label by \(a_i\) the edge \((0,0)\to(1,i)\), by \(b_i\) the edge \((0,0)\to(2,i)\), and by \(c_i\) the edge \((1,0)\to(2,i)\). These exhaust the twelve quotient edges. For every pair \(i,j\in\{1,2,3,4\}\) with \(i\ne j\), there is one quotient triangle represented by the three squares \((0,0),(1,i),(2,j)\), and its positively oriented attaching word is
\[
a_i\,c_{j-i}\,b_j^{-1},
\]
where the subscript of \(c\) is reduced modulo five into \(\{1,2,3,4\}\). There are exactly twelve such triangles.

**2. An explicit homotopy-preserving presentation reduction.** The edges \(a_1,b_1\) form a maximal tree in the one-skeleton, and collapsing that tree preserves homotopy type. Thus set \(a_1=b_1=1\) in the twelve attaching words. The six relations having \(i=1\) or \(j=1\) eliminate six generators, each appearing **exactly once in its selected attaching word**, giving
\[
 b_2=c_1,\quad b_3=c_2,\quad b_4=c_3,\qquad
 a_2=c_4^{-1},\quad a_3=c_3^{-1},\quad a_4=c_2^{-1}.
\]
The remaining six relations, in order \((i,j)=(2,3),(2,4),(3,2),(3,4),(4,2),(4,3)\), are
\[
\begin{aligned}
&c_4^{-1}c_1c_2^{-1},\quad c_4^{-1}c_2c_3^{-1},\quad
c_3^{-1}c_4c_1^{-1},\\
&c_3^{-1}c_1c_3^{-1},\quad c_2^{-1}c_3c_1^{-1},\quad
c_2^{-1}c_4c_2^{-1}.
\end{aligned}
\]
The last, second, and fourth of these, respectively, eliminate \(c_4,c_3,c_1\), each again appearing exactly once in the chosen word. With \(t=c_2\), the substitutions are
\[
c_4=t^2,\qquad c_3=t^{-1},\qquad c_1=t^{-2}.
\]
The three remaining attaching words are exactly \(t^{-5}\), \(t^5\), and the empty word. Eliminating a generator occurring once in an attaching word is a homotopy-preserving elementary two-complex presentation move: it replaces that generator edge and its chosen two-cell by their substituted attaching paths in the other cells. The script independently checks all nine eligible eliminations and all twelve initial relators.

The resulting CW complex has one vertex, one edge \(t\), and three two-cells: two attached along opposite degree-five loops and one attached trivially. Sliding one degree-five two-cell over the other replaces its attaching loop by a null loop. Therefore its homotopy type is
\[
(S^1\cup_{5}e^2)\vee S^2\vee S^2.
\]
This establishes the asserted quotient homotopy type and its fundamental group and homology.

**3. The integral deck lattice.** The free rotation action makes \(\Delta_{3,5}\to Y\) a regular five-sheeted covering. Because \(\pi_1(Y)\cong C_5\), its corresponding index-five subgroup is trivial, so this is the universal covering. Let \(R=\mathbb Z[C_5]\) and \(N=\sum_{g\in C_5}g\). The standard cellular chain complex of the universal cover of \(S^1\cup_5e^2\) has differentials \(R\xrightarrow{N}R\xrightarrow{g-1}R\). Its second homology is \(\ker N=I_{C_5}\). Each of the two additional two-spheres lifts to a free \(R\)-orbit of spheres and contributes \(R\) in degree two. Thus \(H_2(\Delta_{3,5};\mathbb Z)\cong I_{C_5}\oplus R^2\) as claimed. As abelian groups this has rank \(4+2\cdot5=14\); since the covering is simply connected and two-dimensional, its homotopy type is a wedge of fourteen two-spheres.

## Verification
The dependency-free file `verification/verify.py` enumerates all admissible faces, checks that each nonempty face orbit has exactly five members, checks all quotient edge labels and triangle representatives against the original squares, generates the twelve complete attaching words, and independently performs nine exact free-group substitutions after the two tree-edge collapses. Its surviving three words are \(t^{-5}\), \(t^5\), and the empty word. Execute `python3 verification/verify.py` from the package root. The output is in `verification/expected_output.txt`; the final line is `PASS`. The printed homology and module conclusions are consequences of the detailed proof above, not substitutes for it. The proof is finite and exact; no probabilistic tests, numerical approximations, or unbounded search are involved.

## Relationship to prior work
Björner–Lovász–Vrećica–Živaljević introduced the chessboard complexes and proved connectivity bounds for them; in particular, their discussion includes simple connectivity for three-row, five-column complexes. Ziegler established the shellable range. Reiner–Roberts, building on Friedman–Hanlon, calculate the **rational** symmetric-group homology representations for ordinary chessboard complexes, but those representations do not determine the integral deck lattice, the degree-five attaching map, or the homotopy type of the geometric orbit. Limonchenko–Yu's general three-row classification concerns the **unquotiented** generalized chessboard complexes. A published cyclic quotient theorem for three-row **capacity-two** (two-matching) complexes addresses a distinct complex (with six-dimensional maximum faces rather than three-rook faces); neither its group action nor its homology conclusions imply this result. Earlier calculations for cyclic quotients of larger chessboards similarly do not specialize to this induced three-row subcomplex.

## Limitations
This result treats one natural minimal simply connected three-row chessboard and a specified fivefold column action. It does not classify all widths or other group actions. The integral module statement is derived from the explicit quotient homotopy splitting, not a chain-level equivariant basis in the original simplicial chain complex. A homotopy equivalence of quotient spaces is not asserted to preserve preferred geometric cells. The selected-primary and published-results comparisons do not guarantee bibliographic uniqueness; an unindexed computation or a more general transformation-group theorem could supply an equivalent result.

## References
1. A. Björner, L. Lovász, S. T. Vrećica, and R. T. Živaljević, *Chessboard complexes and matching complexes*, J. London Math. Soc. 49 (1994), 25–39. First published February 1, 1994. DOI: 10.1112/jlms/49.1.25; author-uploaded text at https://www.researchgate.net/publication/245653497_Chessboard_Complexes_and_Matching_Complexes.
2. G. M. Ziegler, *Shellability of chessboard complexes*, Israel J. Math. 87 (1994), 97–110. DOI: 10.1007/BF02772986.
3. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, J. Algebr. Comb. 11 (2000), 135–154, Theorems 1.3 and 3.3. https://www-users.cse.umn.edu/~rober005/chessmatch.pdf.
4. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827, first posted October 27, 2026, Theorem 1.1. https://arxiv.org/abs/2610.37827.
5. *Cyclic quotient torsion and the parity threshold for three-row two-matching complexes*, published mathematical record, October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cyclic-quotient-torsion-and-the-parity-threshold-for-three-row-t--e5952a573c96.
