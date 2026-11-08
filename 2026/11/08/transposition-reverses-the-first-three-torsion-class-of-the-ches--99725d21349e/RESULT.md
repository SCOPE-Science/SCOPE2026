# Transposition reverses the first three-torsion class of the chessboard complex

## Finding

Let \(X=\Delta_{5,5}\) be the ordinary chessboard complex: a simplex is a placement of nonattacking rooks on a \(5\)-by-\(5\) board. The known group \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z/3\) carries the following action of the natural row, column, and transposition symmetries. For \(\sigma,\rho\in S_5\), let \((\sigma,\rho)\) permute rows and columns respectively; let \(\tau(i,j)=(j,i)\). Then

\[
 ((\sigma,\rho)\tau^e)_* = \operatorname{sgn}(\sigma)\operatorname{sgn}(\rho)(-1)^e
 \quad\text{on }\widetilde H_2(X;\mathbb Z),\qquad e\in\{0,1\}.
\]

The distinguishing assertion is the **transpose sign** \(\tau_*=-1\); the symmetric-group sign actions and the group \(\mathbb Z/3\) were previously established. A topological consequence is

\[
\widetilde H_2(|X|/\langle\tau\rangle;\mathbb F_3)=0.
\]

## Assumptions and scope

The vertex \(v_{ij}\) represents square \((i,j)\), where \(i,j\in\{1,2,3,4,5\}\). Simplices contain at most one square in any row or column. Orient a simplex by increasing lexicographic order on its pairs. Use the usual augmented simplicial chains and their simplicial join product. All symmetry actions on chains include the induced orientation sign. The result concerns integral degree-two torsion and the indicated finite group; it does not determine the entire integral homology of the geometric quotient.

## Proof

**1. A concrete homology generator.** Define the reduced zero-cycles

\[
 a=v_{11}-v_{21},\qquad b=v_{32}-v_{42},\qquad c=v_{53}-v_{54},
\]

and the degree-two chain \(z=a*b*c\). Because \(a,b,c\) are reduced zero-cycles and their supports use disjoint row and column sets across factors, all eight oriented triangles of \(z\) are simplices and \(\partial z=0\). The cited integral homology calculation gives \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z/3\). The complete finite-field boundary computation in `verify.py` finds \(z\notin\operatorname{im}(\partial_3\otimes\mathbb F_3)\), confirming that its integral class is nonzero and hence generates this cyclic group. In particular the reduction map from this integral group into \(\widetilde H_2(X;\mathbb F_3)\) is injective (by the universal coefficient theorem).

**2. Transpose.** The oriented \(3\)-chain \(w\) specified by `certificate.json` has exactly sixty nonzero coefficients in \(\mathbb F_3\) and satisfies the exact chain identity

\[
 \partial_3w=\tau z+z\pmod3.
\]

The certificate indexes its tetrahedra by first choosing a four-element row set in increasing order and then assigning an ordered four-tuple of distinct column labels. `verify.py` constructs the complete bases, checks the signed boundary of every listed tetrahedron, and verifies this identity coefficient-by-coefficient on all \(600\) oriented triangles. It also proves by full linear-algebra elimination that \(z\) is not a boundary modulo three. Consequently \(\tau[z]=-[z]\) in degree-two homology over \(\mathbb F_3\). Injectivity of integral reduction proves \(\tau_*=-1\) on the integral \(\mathbb Z/3\) group.

**3. The entire natural symmetry action.** The row-transposition \((1\ 2)\) sends \(z\) to \(-z\) on the nose. The column-transposition \((3\ 4)\) likewise sends \(z\) to \(-z\) on the nose. All transpositions in either \(S_5\) are conjugate, and a nonzero cyclic group of order three has only automorphisms \(\pm1\), so row and column factors act by their sign characters. This agrees with the previously published equivariant identities (5.9)–(5.10) of Shareshian–Wachs. Transposition exchanges these two factors, so the displayed semidirect-product character follows.

**4. Geometric quotient.** After barycentric subdivision, the order-two action admits a cellular quotient chain complex identified with coinvariants. Since two is invertible in \(\mathbb F_3\), taking coinvariants commutes with homology. The nontrivial one-dimensional \(\mathbb F_3\)-module in degree two has zero coinvariants, proving \(\widetilde H_2(|X|/\langle\tau\rangle;\mathbb F_3)=0\).

## Verification

Run `python3 verify.py` beside `certificate.json` with Python's standard library. The program independently enumerates all \(25,200,600,600,120\) nonempty simplices in dimensions zero through four, computes the first three boundary ranks \(24,176,423\) over \(\mathbb F_3\), verifies \(\dim\widetilde H_2(X;\mathbb F_3)=1\), checks \(\partial z=0\), shows \([z]\ne0\), and verifies the signed transposition, row, and column actions. The explicitly stored sixty-term chain supplies a separately replayable positive boundary witness. Its actual stdout is recorded in `verification_output.txt`. These finite calculations are exhaustive for this finite complex, not asymptotic experiments.

## Relationship to prior work

The integral group \(\widetilde H_2(\Delta_{5,5};\mathbb Z)\cong\mathbb Z/3\) is classical (Shareshian–Wachs; Jonsson). Shareshian–Wachs, Theorem 5.4 and equations (5.9)–(5.10), already determine the two separate \(S_5\) sign actions, which are **not** presented as new here. Limonchenko–Yu (first posted October 27, 2026) discuss torsion in generalized chessboard complexes and recognize the \(5\)-by-\(5\) group, but do not state this integral row–column transposition character or its quotient consequence in the inspected material. The additional transpose sign distinguishes the two possible extensions of the previously known product sign character to the group allowing row–column exchange. A short unindexed calculation or an implicit consequence of older chain identities remains an originality risk.

## Limitations

The classification is specific to the first torsion-bearing ordinary square chessboard complex. It makes no claim for larger boards, generalized capacities, the homotopy type of the quotient, or its homology in other degrees. The proof imports the known integral \(\mathbb Z/3\) homology computation; the attached certificate independently checks the finite-field action and does not itself give a Smith-normal-form proof of the integral group. No independent mathematical assessment has been performed.

## References

1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first public September 3, 2004), especially Theorem 5.4, equations (5.9)–(5.10).
2. Jakob Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644 (first public March 26, 2012), including the \(5\)-by-\(5\) computation.
3. Ivan Limonchenko and Seonghyeon Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827 (first public October 27, 2026), primary MSC2020 \(55U10\).
