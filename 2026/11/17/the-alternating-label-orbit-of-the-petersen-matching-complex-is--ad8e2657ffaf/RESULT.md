# The alternating-label orbit of the Petersen matching complex is a two-sphere

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with vertices the two-element subsets of \(\{0,1,2,3,4\}\) and edges joining disjoint subsets. Let \(X=\mathcal M(P)\) be the *ordinary edge-matching complex*: each simplicial vertex is an edge of \(P\), and the faces are sets of pairwise endpoint-disjoint graph edges. The alternating group \(A_5\) permutes the five original labels and acts simplicially on \(X\). For the **ordinary geometric orbit space** \(Y=|X|/A_5\),

\[
\boxed{Y\simeq S^2.}
\]

In particular, \(\pi_1(Y)=1\), \(H_0(Y;\mathbb Z)\cong H_2(Y;\mathbb Z)\cong\mathbb Z\), and \(H_i(Y;\mathbb Z)=0\) for all other nonnegative \(i\).

## Assumptions and scope

The graph is specifically the ten-vertex Petersen graph \(\operatorname{KG}(5,2)\), not the complete graph on five vertices. Its fifteen graph edges form the fifteen vertices of \(X\). A matching of cardinality \(r\) is a simplex of dimension \(r-1\). The action is the natural **even-label** subgroup of the full \(S_5\) graph-automorphism action; it is not the action on perfect matchings alone. The quotient is a geometric orbit space, not a Borel homotopy quotient. There are no asymptotic or arbitrary-subgroup claims.

## Proof

**1. An integral regular quotient cell structure.** Exhaustive enumeration of pairwise endpoint-disjoint subsets of the fifteen graph edges gives the nonempty face counts, by cardinality, \((15,75,145,90,6)\), for a total of \(331\) faces. Form the barycentric subdivision \(\operatorname{sd}X\); a \(d\)-simplex is a strict chain \(F_0\subsetneq\cdots\subsetneq F_d\) of nonempty matching faces. Its simplex counts in degrees zero through four are \((331,2460,5010,3600,720)\).

The \(60\) even permutations preserve the cardinality of every face, so no nonidentity group element can permute vertices within a barycentric chain. Moreover, distinct proper faces of one barycentric simplex cannot be identified by the action: deleting different chain entries leaves different sets of matching-cardinalities. Consequently the orbit cells form a regular CW complex, with one cell for each orbit of strict matching-face chains. Exact enumeration gives

\[
(c_0,c_1,c_2,c_3,c_4)=(14,58,94,60,12).
\]

Orient a chain by its increasing matching-cardinality sequence. Every label permutation preserves this orientation. Therefore the integral boundary of an orbit-chain representative is calculated by

\[
\partial[F_0<\cdots<F_d]=\sum_{j=0}^{d}(-1)^j[F_0<\cdots<\widehat F_j<\cdots<F_d],
\]

where each face is replaced by its canonical orbit representative. The standalone verifier reconstructs these exact integer differentials from the graph definition, confirms \(\partial^2=0\), and performs \(118\) successive chain cancellations on coefficients \(+1\) or \(-1\). Each cancellation uses unimodular row/column basis changes and removes a contractible pair of adjacent-dimensional generators. Precisely one zero-dimensional and one two-dimensional generator survive, and every remaining differential vanishes. Thus, *integrally*,

\[
H_0(Y;\mathbb Z)=\mathbb Z,\qquad H_2(Y;\mathbb Z)=\mathbb Z,
\qquad H_i(Y;\mathbb Z)=0\ (i\notin\{0,2\}).
\]

**2. The original matching complex is simply connected.** Its one-skeleton has fifteen vertices and seventy-five edges. Choose a spanning tree with fourteen edges. The resulting triangle presentation of \(\pi_1(X)\) has sixty-one free generators (non-tree edges) and one triangular relation for each of the \(145\) two-simplices. An exhaustive free-group Tietze reduction, implemented independently of the orbit-chain elimination in the supplied program, successively finds a relation with exactly one occurrence of one generator, solves that relation for the generator, and substitutes in all other relations. Exactly \(61\) such legal eliminations remove every generator, and all remaining relators freely reduce to the empty word. Hence \(\pi_1(X)=1\). This calculation requires only the two-skeleton and makes no assumption about homotopy groups of the higher cells.

**3. The quotient is simply connected.** The three-cycle \(g=(0\ 1\ 2)\in A_5\) cyclically permutes the three graph edges

\[
\{\{0,1\},\{2,3\}\},\quad
\{\{0,2\},\{1,3\}\},\quad
\{\{0,3\},\{1,2\}\}.
\]

They are pairwise endpoint-disjoint as Petersen graph edges, so they form a two-simplex of \(X\). Its barycenter is fixed by \(g\). By the orbit-space fundamental-group theorem of Armstrong, because \(X\) is simply connected,

\[
\pi_1(Y)\cong A_5/\langle\!\langle h:\,|X|^h\ne\varnothing\rangle\!\rangle.
\]

The nontrivial three-cycle normally generates the simple group \(A_5\), so this quotient group is trivial.

**4. Homotopy classification.** The simply connected finite CW complex \(Y\) has exactly the integral homology of a two-sphere. By Hurewicz, a generator of \(H_2(Y;\mathbb Z)\) is represented by a map \(S^2\to Y\); that map is an integral homology isomorphism. The homological Whitehead theorem for simply connected CW complexes makes it a homotopy equivalence. This completes the proof.

## Verification

Run `python3 verify_petersen_a5.py` using standard Python 3, without additional dependencies or network access. The program independently generates all fifteen graph edges and all nonempty matching faces, the even permutation action, every barycentric chain, and all orbit representatives. It verifies every signed boundary composition exactly, performs the \(118\) integer unit cancellations, and separately eliminates all \(61\) generators of the original fundamental-group presentation. The decisive outputs are the quotient cell vector \((14,58,94,60,12)\), residual chain ranks \((1,0,1,0,0)\) with zero differentials, and the fixed matching simplex for a three-cycle. Modular checks at characteristics \(2,3,5,7,1009\) are included as independent sanity checks, but do **not** replace the exact integer reductions. The proof is exhaustive only for the explicitly defined finite complex.

## Relationship to prior work

The literature on matching complexes and the Petersen graph supplies the object and its natural label symmetry. Jonsson's *Simplicial Complexes of Graphs* (2007 print publication) treats matching complexes systematically. Zaslavsky's classification of Petersen graph matching-orbit types (Section 3.2 of the accessible full preprint) establishes important combinatorial orbit information but not a topological orbit-space homotopy classification. Earlier mathematical records determine the nonequivariant integral sphere-wedge type of \(X\) and the rational second cohomology of \(|X|/A_5\), while another establishes contractibility under the larger full \(S_5\) action. Neither rational cohomology nor the different full-symmetry quotient determines the *integral* homotopy type under \(A_5\). The exact quotient differentials and fundamental-group argument supply this missing conclusion.

## Limitations

This is an exact statement for one canonical finite graph and one natural index-two symmetry subgroup; no assertion is made for arbitrary graph complexes or other subgroups. Existing indexed mathematical records and the directly relevant matching-orbit sections of the primary literature were compared, but unindexed equivalent work cannot be excluded. The full text of Jonsson's matching-complex chapter was not accessible in this inspection; its available chapter preview and bibliographic scope were reviewed. No independent mathematical audit is claimed.

## References

1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, print publication 15 November 2007; matching-complex chapter: https://doi.org/10.1007/978-3-540-75859-4_11.
2. T. Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, *Discrete Mathematics* 312 (2012), 1558–1583, especially Section 3.2: https://doi.org/10.1016/j.disc.2011.12.010; lawful full preprint: https://arxiv.org/abs/1303.3347.
3. M. A. Armstrong, *On the fundamental group of an orbit space*, *Proc. Cambridge Philos. Soc.* 61 (1965), 639–646: https://doi.org/10.1017/S0305004100038974.
4. Previously indexed mathematical results on the Petersen matching complex's integral homotopy, \(S_5\) character and rational \(A_5\) orbit cohomology (2026), distinguished from the present integral orbit-homotopy classification.
