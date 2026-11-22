# An integral wedge of twenty-eight three-spheres from transpose symmetry of the five-by-five chessboard complex

## Finding
Let \(X=\mathcal M(K_{5,5})\) be the chessboard complex: its vertices are squares \((i,j)\), with \(0\le i,j<5\), and a finite set of squares is a simplex when no two share a row or column. Transposition \(\tau(i,j)=(j,i)\) is a simplicial involution. For the **ordinary geometric orbit space** \(Y=|X|/\langle\tau\rangle\),
\[
\boxed{Y\simeq\bigvee^{28}S^3.}
\]
Consequently \(\pi_1(Y)=\pi_2(Y)=0\), \(\widetilde H_3(Y;\mathbb Z)\cong\mathbb Z^{28}\), and all remaining reduced integral homology groups vanish. In particular, there is neither two-primary nor three-primary torsion in the orbit space.

## Assumptions and scope
The vertex set consists of the 25 distinct ordered positions, not diagonal-only positions or the five-crown restriction. We use the complete ordinary chessboard matching complex, including partial matchings of sizes one through five. The involution simultaneously exchanges rows and columns and has fixed diagonal vertices. The quotient is an actual topological orbit space, **not** a homotopy-orbit/Borel construction. Homology has integral coefficients unless indicated otherwise. The assertion is about this one canonical board and symmetry, with no claim for general board sizes or arbitrary subgroups.

## Proof
**Step 1: Enumerate the quotient as a regular cellular complex.** Every size-\(k\) matching is specified uniquely by \(k\) increasing row labels and an injective assignment of \(k\) column labels. Exhaustive enumeration yields \((25,200,600,600,120)\) faces by number of rooks, hence 1545 nonempty faces. For each nonempty face \(F\), enumerate every strictly increasing nonempty flag of faces ending in \(F\). The barycentric subdivision of \(X\) has one simplex for each such flag. Transposition preserves its increasing face-size sequence. Hence a flag preserved setwise is fixed vertexwise, and the quotient of the barycentric subdivision is a regular CW/Delta complex with a cell for each flag orbit and the standard rank-ordered signed boundary, with no inversions.

Explicit enumeration gives the quotient cellular counts in dimensions 0 through 4:
\[
(c_0,c_1,c_2,c_3,c_4)=(843,8340,22110,21900,7260).
\]
As a separate consistency check, the full flag counts are \((1545,16000,43200,43200,14400)\), the flags fixed by transposition are \((141,680,1020,600,120)\), and Burnside's half-sum gives precisely the listed quotient counts. The Euler characteristic is \(-27\). The checker explicitly verifies \(\partial^2=0\) for every quotient cell in dimensions at least two.

**Step 2: Remove genuine topological free faces.** In descending upper dimension four, three, two, one, repeatedly delete a pair \((\sigma^{d-1},\eta^d)\) only when \(\sigma\) belongs to exactly one currently surviving \(d\)-cell \(\eta\), and all higher-dimensional cells have already been removed. Each deletion is an elementary cellular collapse, a deformation retraction, not merely an algebraic chain cancellation. The exact counts of deleted pairs by upper dimension are
\[
(7260,9156,2919,173)\quad\text{for }d=4,3,2,1.
\]
Thus a three-dimensional connected CW complex \(Z\simeq Y\) remains, with cell counts \((670,5248,10035,5484,0)\). Its cellular differential consists of the original quotient incidence matrices restricted to the surviving cells because the removed pairs were free faces. This is verified using the regenerated face incidences, not presumed from their counts.

**Step 3: Compute integral homology by exact unimodular cancellation.** On the remaining free abelian cellular chain groups, choose an entry \(p=\pm1\) in a differential. The elementary integral basis change subtracting \((a/p)\) times the pivot column from every other column incident on its pivot row, followed by deletion of the pivot row and column, splits off an acyclic two-term complex. The Schur complement is calculated over the integers without rational division; corresponding basis changes in adjacent degrees preserve \(\partial^2=0\). Every pivot is checked to be \(\pm1\). In upper dimensions three, two and one, the verifier performs respectively 5456, 4579 and 669 such cancellations, until only one degree-zero generator and 28 degree-three generators remain. There are no remaining boundary entries. It follows that
\[
\widetilde H_q(Y;\mathbb Z)=\begin{cases}\mathbb Z^{28},&q=3,\\0,&q\ne3.\end{cases}
\]
The use of integer unit pivots (rather than numerical ranks or finite-field computation) establishes the absence of **all** integral torsion. These algebraic cancellations compute homology; they are not themselves claimed to preserve homotopy type.

**Step 4: Recover the integral homotopy type.** The classical connectivity theorem for the ordinary \(5\times5\) chessboard complex gives \(\pi_1(X)=0\). Armstrong's orbit-space theorem for a simply connected complex under a finite group identifies \(\pi_1(Y)\) with the group modulo the subgroup generated by fixed-point elements. Since \(\tau\) fixes each diagonal vertex, \(\pi_1(Y)=0\). The Hurewicz theorem then gives \(\pi_2(Y)\cong H_2(Y;\mathbb Z)=0\). Therefore \(Y\) is two-connected. Hurewicz identifies \(\pi_3(Y)\cong\mathbb Z^{28}\). Choose 28 based maps of three-spheres representing a basis and form their wedge map \(\bigvee^{28}S^3\to Z\). This map is an isomorphism on integral homology, and both spaces are simply connected CW complexes. The homological Whitehead theorem gives a homotopy equivalence. This completes the proof.

## Verification
The standalone `verify.py` needs only Python 3's standard library. Run `python verify.py`; it constructs all matching faces, every strict face flag, its full involution orbit, every regular quotient boundary and the descending free-face collapses, then performs only unit integer chain pivots. It independently checks Burnside orbit counts, exact \(\partial^2=0\), final ranks and every enumerated cancellation count. Its final success marker is `CHESSBOARD_TRANSPOSE_INTEGRAL_HOMOTOPY_OK`. The checker is regenerated from definitions, with no external certificate file, cached matrix or undocumented data dependency.

The noncomputational inputs are the published chessboard connectivity theorem (establishing simply connectivity), Armstrong's fundamental-group theorem for an orbit space and standard Hurewicz/Whitehead theorems. The computation is finite and exhaustive specifically for the five-by-five complex; it does not prove any infinite-family assertion. Verification of the script does not constitute an independent mathematical audit.

## Relationship to prior work
Shareshian and Wachs establish connectivity and the nontrivial three-torsion in the unquotiented \(X\); Jonsson supplies a separate argument for \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z/3\). These are explicitly cited as known premises. The closest earlier **same quotient** calculation determines the action of transposition on the three-torsion generator and shows that its three-local homotopy is \(\bigvee^{28}(S^3)_{(3)}\). Its scope and limitations explicitly leave integral homotopy type and possible two-primary phenomena undecided. The present complete **integral** calculation, together with simple connectivity and a genuine three-dimensional topological reduction, resolves that precise gap. The earlier three-local claim is a corollary, not a newly discovered contribution. The row- and column-symmetry quotients and diagonal-deleted chessboard results are different spaces and cannot be substituted for this ordinary transpose orbit space.

## Limitations
No generalization to larger chessboards or other symmetries follows. The computational homology proof depends on the specified finite exact enumeration and integer elimination, which is directly reproducible from the standalone program. The fundamental-group and homotopy upgrades use the indicated standard external topological theorems, not a computer-generated presentation. The originality assessment covers checked indexed findings and accessible sources; an unknown equivalent publication could change publication priority. No independent audit has been performed.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first public 2004-09-03, particularly connectivity and Section 5: https://arxiv.org/abs/math/0409054 .
2. J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644, first arXiv public 2012-03-26: https://arxiv.org/abs/1203.5644 .
3. M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. 61 (1965), 639–646, DOI 10.1017/S0305004100038974.
4. *Three-local torsion cancellation in the transpose quotient of the five-by-five chessboard complex*, prior published research result: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-three-local-torsion-cancellation-in-the-transpose-quotient-of-th--62667cf31b8c/RESULT.md .
