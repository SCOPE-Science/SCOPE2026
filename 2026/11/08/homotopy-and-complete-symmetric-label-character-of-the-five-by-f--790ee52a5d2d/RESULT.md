# Homotopy and complete symmetric-label character of the five-by-five diagonal-deleted chessboard complex

## Finding
For \(D_5=\{(i,j)\in[5]^2:i\ne j\}\), define \(X=\mathcal M(D_5)\) to have a simplex for each set of squares with no two in one row or column. This is the ordinary matching complex of the crown graph \(K_{5,5}\) with a perfect matching deleted. The ordinary homotopy type is
\[
X\simeq S^2\vee\bigvee^{13} S^3.
\]
The graph-automorphism group \(G=S_5\times C_2\) acts by simultaneous label permutations and by transposition \(\tau:(i,j)\mapsto(j,i)\). The integral second homology is \(\mathbb Z\), with trivial \(S_5\)-action and \(\tau=-1\). Its rational third-homology representation is
\[
\widetilde H_3(X;\mathbb Q)\cong
(S^{(4,1)}\boxtimes\mathbf1)\oplus
(S^{(2,1,1,1)}\boxtimes\varepsilon)\oplus
(S^{(3,2)}\boxtimes\mathbf1),
\]
where \(\varepsilon(\tau)=-1\). The rational dimension is thirteen. All reduced integral homology outside degrees two and three vanishes.

Equivalently, write \(f=f(p)\) for fixed labels and \(t=t(p)\) for two-cycles of \(p\in S_5\). Put \(A=f-1\), \(B=\operatorname{sgn}(p)(f-1)\), and \(C=\binom f2+t-f\). Then
\[
\operatorname{tr}(p\mid\widetilde H_3)=A+B+C,\qquad
\operatorname{tr}(p\tau\mid\widetilde H_3)=A-B+C;
\]
\(\operatorname{tr}(p\mid\widetilde H_2)=1\) and \(\operatorname{tr}(p\tau\mid\widetilde H_2)=-1\). The first formula classifies the \(S_5\)-module asked about for this degree and size in a longstanding directed-matching-complex representation problem.

## Assumptions and scope
The complex has twenty vertices, one for each off-diagonal square. The complete bipartite graph with a perfect matching removed is connected and has a unique bipartition up to interchange. Therefore its automorphisms consist exactly of simultaneous permutations of the five labels, optionally followed by interchange of the parts: \(G\cong S_5\times C_2\). Homology is reduced simplicial homology over \(\mathbb Z\) unless \(\mathbb Q\) is specified. Specht modules denote the standard characteristic-zero irreducible representations of \(S_5\). The homotopy equivalence is ordinary, not an asserted equivariant homotopy equivalence.

## Proof
**Exact finite complex and acyclic matching.** List the twenty off-diagonal squares lexicographically, with zero-based coordinates for the standalone program. There are respectively \(1,20,130,320,265,44\) allowed square sets of cardinalities zero through five. Their sizes come from exhaustive enumeration of subsets with pairwise-distinct rows and columns. Apply consecutive vertex-toggle matching on the still-unmatched face set, in this zero-based vertex order:

`(19,9,10,17,16,3,11,14,4,8,0,7,2,6,1,15,18,5,13,12)`.

At a toggle, match each currently unmatched face not containing the chosen vertex with its enlargement by that vertex, provided the enlargement is also currently unmatched. This matching pairs the empty face with a vertex. Remove that single pair and leave the vertex critical, restricting attention to the ordinary nonempty face poset. The resulting 382 matched pairs leave exactly one critical vertex, one critical two-simplex, and thirteen critical three-simplices. Direct each unmatched codimension-one cover downward and each matched cover upward. All 2,500 nonempty-face covers form a directed acyclic graph; the standalone program performs a topological sort visiting all 779 nonempty faces. Forman's discrete Morse theorem therefore yields a CW complex with one cell in dimension zero, one in dimension two, and thirteen in dimension three, with no other cells.

**Zero attaching degrees and the homotopy splitting.** Independently form the signed augmented simplicial boundaries from oriented faces in lexicographic vertex order. Exact rational Gaussian elimination gives boundary ranks \((1,19,111,208,44)\) between consecutive face-cardinality layers. Hence \(\dim_{\mathbb Q}\widetilde H_2(X;\mathbb Q)=1\) and \(\dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)=13\), and all other reduced rational homology vanishes. The Morse CW chain differential from its thirteen three-cells to its sole two-cell is an integer matrix. Rational rank zero forces this integer matrix to be zero. The CW two-skeleton is \(S^2\); each three-cell attaches by a map \(S^2\to S^2\), classified by its degree, and every degree is zero. Thus each attaching map is nullhomotopic and the displayed ordinary wedge decomposition follows. In particular there is no integral torsion and both reduced homology groups have the asserted integral ranks.

**The second-homology sign.** The ordered pairs of square-vertices numbered \(((0,1),(0,2)),((1,0),(1,3)),((2,4),(3,4))\) define three copies of \(S^0\) whose join is a simplicial two-sphere in \(X\). Its eight oriented triangles have alternating coefficients \(\pm1\); their integral boundary vanishes. A complete mod-three boundary-column reduction of the 265 three-simplices has rank 208 and shows this sphere is not a boundary modulo three. Under the label transposition \((0\;1)\), its difference from its image is a boundary modulo three; under board transposition, its *sum* with its image is a boundary modulo three. The opposite signs in each case are excluded by the same reduction. Since integral \(\widetilde H_2\) is free of rank one, an automorphism acts by \(\pm1\); reduction modulo three identifies the signs unambiguously. All transpositions of \(S_5\) are conjugate and generate it, so \(S_5\) acts trivially while \(\tau\) acts as \(-1\).

**All third-homology characters.** For any \(g\in G\), the reduced simplicial Hopf trace formula gives \(\operatorname{tr}(g\mid\widetilde H_2)-\operatorname{tr}(g\mid\widetilde H_3)\) as the signed alternating sum of traces on augmented simplicial chain groups. Each chain trace is the sum of orientation signs over simplices stabilized setwise by \(g\). The accompanying standalone program computes these traces independently for all \(240\) elements of \(G\) and verifies the two closed character formulas in the Finding. The character of the standard \(S_5\)-module \(S^{(4,1)}\) is \(A=f-1\); that of its sign twist \(S^{(2,1,1,1)}\) is \(B\); the two-subset permutation module decomposes as \(\mathbf1\oplus S^{(4,1)}\oplus S^{(3,2)}\), giving character \(C=\binom f2+t-f\) for the last summand. Equality on every conjugacy class gives the asserted complete rational decomposition, including the transposition eigenspaces.

## Verification
Run `python3 crown_d5_verify.py` with Python 3 and SymPy. This rebuilds the complex, verifies every matching cover, checks acyclicity, calculates *exact characteristic-zero* boundary ranks, constructs the eight-triangle integral sphere, proves its nonzero residue modulo three, checks both generating symmetries on that class, and computes the signed Lefschetz trace of all \(240\) automorphisms. The program ends with the exact marker `DIAGONAL_DELETION_HOMOTOPY_AND_SYMMETRY_PASS`. `verification_output.txt` is the output from an actual replay of that same embedded source.

## Relationship to prior work
Björner and Welker introduced this diagonal-deleted chessboard/directed matching complex and proved a connectivity bound; their 1999 work also tabulates homology in small sizes. Shareshian and Wachs explicitly define the identical \(D_n\) complex in Section 8 of their 2004 preprint. Their Table 8.1 gives the **already known** fact \(\widetilde H_2(\mathcal M(D_5);\mathbb Z)\cong\mathbb Z\), and their Theorem 8.3 proves nonzero bottom homology in general. Neither inspected text determines the *ordinary homotopy type* or the full \(S_5\times C_2\) character exhibited here. Wachs's survey, Section 8.3, explicitly poses determination of the \(S_n\) homology representations of these loopless directed matching complexes (Problem 8.16). Here that question is answered for the five-label instance in both nonzero degrees. The earlier homology rank table is not presented as a new result.

## Limitations
The representation statement in degree three is rational; the complete integral \(G\)-lattice in degree three is not classified. The homotopy equivalence is not claimed equivariant. No assertion extends to other numbers of labels. A complete version of the original Björner–Welker 1999 article was not available for direct full-text comparison; its surveyed connectivity and homology claims were compared and an undiscovered equivalent homotopy or character calculation remains a publication-priority risk. No independent mathematical audit has been performed.

## References
- J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first arXiv version 2004-09-03), especially Section 8, Theorem 8.3 and Table 8.1: https://arxiv.org/pdf/math/0409054.
- M. L. Wachs, *Topology of Matching, Chessboard, and General Bounded Degree Graph Complexes* (survey, 2001 manuscript), Section 8.1 and Problem 8.16: https://www.math.miami.edu/~wachs/papers/tmc.pdf.
- A. Björner and V. Welker, *Complexes of Directed Graphs*, SIAM Journal on Discrete Mathematics **12** (1999), 413–424, DOI:10.1137/S0895480198338724 (full text not directly inspected).
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145 (standard discrete Morse theorem).
