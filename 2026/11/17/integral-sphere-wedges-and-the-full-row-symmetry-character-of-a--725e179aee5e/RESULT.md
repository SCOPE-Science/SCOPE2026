# Integral sphere wedges and the full row-symmetry character of a seven-column multiple chessboard complex

## Finding
Let \(X\) be the standard multiple chessboard complex with four rows, seven labelled columns, and row capacities \((1,2,2,2)\). Then
\[
X\simeq\bigvee^{63}S^4\vee\bigvee^{36}S^5.
\]
Permuting the last three rows induces an \(\mathfrak S_3\)-action. In the order identity, transposition, three-cycle, its rational reduced-homology characters are
\[
\chi_{\widetilde H_4}=(63,35,21),\qquad\chi_{\widetilde H_5}=(36,-20,15).
\]
Writing \(\mathbf1\), \(\mathrm{sgn}\), and \(\mathrm{std}\) for the rational trivial, sign, and two-dimensional standard modules, respectively, these representations are
\[
\widetilde H_4(X;\mathbb Q)\cong35\mathbf1\oplus14\mathrm{std},\quad
\widetilde H_5(X;\mathbb Q)\cong\mathbf1\oplus21\mathrm{sgn}\oplus7\mathrm{std}.
\]
The nonzero fourth homology of this pure six-dimensional complex also obstructs shellability.

## Assumptions and scope
The vertices are pairs \((r,c)\) with \(r\in\{1,2,3,4\}\) and \(c\in\{1,\ldots,7\}\). A set is a face exactly when no column repeats, the first row occurs at most once, and each of the remaining three rows occurs at most twice. All complexes are ordinary abstract simplicial complexes and homology is reduced integral homology unless coefficients are specified. The row action fixes row one and permutes rows two through four, leaving columns unchanged. The only source-date assignment is the earliest public version of the motivating 2026 preprint, October 27, 2026.

## Proof
**Complete signed Morse reduction.** Label vertices by \(4(c-1)+(r-1)\). Enumerate faces by scanning seven columns and choosing either no vertex or one permissible row, respecting the four capacities. There are \(19979\) augmented faces; their numbers in dimensions \(-1,0,1,2,3,4,5,6\) are respectively \(1,28,315,1785,5250,7560,4410,630\). In ascending vertex order, toggle the first available vertex in each still-unpaired face, pairing a lower face with its upper coface, and remove both. This is an acyclic matching: orient every unmatched Hasse edge downwards and each matched edge upwards; topological sorting traverses all \(19979\) faces and \(95683\) covers. The unmatched faces comprise \(30\) dimension-three, \(393\) dimension-four, and \(336\) dimension-five faces. As the augmented empty face is paired, the ordinary CW model also has one base vertex.

For each unmatched face, compute the *integral* Morse boundary by summing signed gradient paths; at every matched pair the elementary elimination coefficient is \(\pm1\). The resulting degree-four and degree-five boundary matrices have \(30\times393\) and \(393\times336\) entries (respectively \(1140\) and \(2052\) nonzeros). Check \(\partial_4\partial_5=0\) over the integers. Exact integer elimination by unit pivots cancels \(30\) independent \((4,3)\)-pairs and, in the resulting kernel coordinates, \(300\) independent \((5,4)\)-pairs. The remaining integral boundary matrices are zero, with \(63\) dimension-four and \(36\) dimension-five generators; this establishes torsion-freeness in every degree.

**Upgrade from homology to homotopy.** The Morse CW model has no cells in positive dimensions below three. The attachments of its four-cells to a wedge of three-spheres are classified by their integer degree vectors, since \(\pi_3(\bigvee S^3)\cong\mathbb Z^{30}\). Integral unit pivots thus perform genuine homotopy cancellations of \(30\) degree-three and \(30\) degree-four cells. The resulting four-skeleton is a wedge of \(363\) four-spheres. Attaching maps of five-cells are classified by the degree matrix because \(\pi_4(\bigvee S^4)\cong\mathbb Z^{363}\), so the \(300\) further unit pivots are again homotopy cancellations. The remaining attaching degrees are zero; therefore the reduced model is precisely a wedge of \(63\) four-spheres and \(36\) five-spheres. This argument uses the two consecutive attaching dimensions, not an invalid inference from Betti numbers alone.

**Row-symmetry.** For a row permutation, act on each oriented face and multiply by the sign of the induced reordering of its vertices. For each cyclic subgroup of order two or three, form the integer signed-orbit subcomplex: an orbit contributes an invariant generator iff its stabilizer preserves orientation. Its boundary is the signed sum of all orbit-face boundaries. The supplied checker verifies \(\partial^2=0\) exactly and computes the invariant chain ranks over both primes \(1000003\) and \(1000033\). Both primes are coprime to \(6\). For a transposition, the invariant dimensions in degrees four and five are \((49,8)\); for a three-cycle they are \((35,22)\). These finite-field ranks rigorously determine the *rational* invariant dimensions. Indeed, integral homology was independently proved free. For primes not dividing the group order, the averaging idempotent on this free homology has entries in the localization \(\mathbb Z[1/6]\); its image is a direct summand of fixed rank, so the invariant dimension is unchanged between characteristic zero and each of the two chosen positive characteristics. Exactness of invariants then identifies invariant homology with homology of the signed-orbit invariant chains. Accordingly the traces are \(2\dim H^{\langle g\rangle}-\dim H\) for order two and \((3\dim H^{\langle g\rangle}-\dim H)/2\) for order three. The standard \(\mathfrak S_3\) character table gives the displayed decompositions.

## Verification
Run `python3 verify_chessboard.py` and `python3 verify_symmetry.py` from the same directory. Both use only the Python standard library; their exact captured outputs are `verification-output.txt` and `symmetry-output.txt`. The former checks the complete face list, every Hasse cover, all critical cells, both signed integer Morse differentials, their composite, and unit pivots. The latter independently recomputes signed-orbit invariant chains and their boundaries for both specified primes, checking chain-square-zero and class dimensions. Exhaustiveness is finite because every potential subset is represented in the generated face list; no random sampling or timeout inference is used.

## Relationship to prior work
Limonchenko and Yu, *Homotopy types and torsion in homology of generalized chessboard complexes* (arXiv:2610.37827, first public October 27, 2026), study multiple chessboards and identify the nearby four-row seven-column capacity \((2,2,2,2)\) as a first torsion case; their discussion of reducing one row capacity motivates the present torsion-free boundary. The present exact \(\mathfrak S_3\)-character and explicit finite homotopy model for \((1,2,2,2)\) are not claimed in the parts of that paper inspected. Reiner and Roberts (2000) give broad homological/representation methods for matching and chessboard complexes; a complete implication comparison would require further examination of their full text, which was not available here. A separate research record concerns \((1,1,1,2)\), not this capacity vector. No claim is made that general chessboard homology calculations were first introduced here.

## Limitations
The assertion is restricted to the exact four-row seven-column board and its natural permutation group on the three equal-capacity rows. It does not settle the full parameter family or the integral \(\mathfrak S_3\)-lattice structure. The two modular symmetry computations are exact rank computations but by themselves do not detect arbitrary integral torsion; torsion-freeness follows separately from the unit-pivot Morse certificates. Full-text access to one plausible older representation-theoretic reference was not obtained, so priority remains provisional. Independent mathematical validation has not been performed.

## References
1. Limonchenko and Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827, https://arxiv.org/abs/2610.37827 (initial release 2026-10-27).
2. V. Reiner and J. Roberts, *Minimal Resolutions and the Homology of Matching and Chessboard Complexes*, Journal of Algebraic Combinatorics (2000), https://doi.org/10.1023/A:1008728115910.
3. Research record, *Integral homotopy classification of four-row (1,1,1,2) multiple chessboard complexes*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-homotopy-classification-of-four-row-1-1-1-2-multiple-ch--352b61db3ab2 (distinct capacity parameters).
