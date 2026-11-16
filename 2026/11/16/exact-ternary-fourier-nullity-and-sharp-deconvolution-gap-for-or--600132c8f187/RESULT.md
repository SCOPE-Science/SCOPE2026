# Exact ternary Fourier nullity and sharp deconvolution gap for order-four alternating-sign matrices

## Finding

Let \(\mathcal A_4\) be the set of all \(42\) alternating-sign matrices of order four, with entries \(-1,0,1\). Regard each matrix as an element of \(G=M_4(\mathbb F_3)\), using the natural reduction of integer entries modulo three. Let \(f=1_{\mathcal A_4}\), \(\omega=\exp(2\pi i/3)\), and define the unnormalized Fourier multiplier
\[
W(K)=\sum_{A\in\mathcal A_4}\omega^{\sum_{i,j=1}^4 K_{ij}A_{ij}},\qquad K\in G.
\]
Exactly \(1,605,258\) of the \(43,046,721\) multipliers vanish. The convolution operator \(T:h\mapsto f*h\) therefore has exact complex rank \(41,441,463\) and nullity \(1,605,258\). Its sharp smallest nonzero singular value is \(\sqrt3\), its largest is \(42\), and
\[
\|T^\dagger\|_{\ell^2(G)\to\ell^2(G)}=\frac1{\sqrt3},\qquad
\kappa_+(T)=14\sqrt3.
\]
There are exactly \(53\) distinct squared multiplier magnitudes, with the complete multiplicity distribution given in `SPECTRUM.json` after reduction to a nine-dimensional frequency quotient.

The first Fourier zeros occur at character support weight two. There are exactly \(16\) such characters: choose one of the four rows and its two middle columns, or one of the four columns and its two middle rows, and give the two selected positions the coefficients \(1\) and \(2\) (in either order) in \(\mathbb F_3\). No one-coordinate character vanishes, and no other two-coordinate character vanishes. For example, the statistic \(A_{1,2}-A_{1,3}\pmod3\) takes each residue exactly \(14\) times over \(\mathcal A_4\).

## Assumptions and scope

All matrices, indices, and frequencies are labelled, with rows and columns numbered \(1,2,3,4\). An alternating-sign matrix has entries in \(\{-1,0,1\}\), row and column sums equal to one, and alternating nonzero signs within every row and column. No weighting or identification by geometric symmetry is used. Additive convolution on \(G\) is **unnormalized**; the \(\ell^2\) space uses counting measure, so its singular values are \(|W(K)|\). Character weight means the number of nonzero entries of the frequency matrix \(K\), not its rank.

## Proof

**Complete finite parametrization.** Each matrix column's partial sums from top to bottom are in \(\{0,1\}\), start at zero, and finish at one. Every permissible row is obtained by choosing one or three strictly increasing positions, placing alternating signs \(+1,-1,+1\) at the chosen positions, and zeros elsewhere. The recursive enumeration starts with four zero column sums, appends every such row while maintaining all partial column sums in \(\{0,1\}\), and accepts precisely when all four final sums equal one. These conditions are necessary and sufficient for the alternating-sign requirements. The exhaustive recursion has \(42\) distinct outputs.

**Affine Fourier reduction.** Every matrix in \(\mathcal A_4\) has all row and column sums congruent to one modulo three. These eight affine equations have exactly one dependency, hence describe an affine translate of a nine-dimensional linear subspace of \(\mathbb F_3^{16}\). The upper-left \(3\times3\) entries determine the fourth row and column. Consequently, every character on \(G\), when restricted to this affine translate, equals a constant cube-root phase times exactly one of \(3^9=19683\) characters applied to the nine upper-left entries. The kernel of the restriction on frequency vectors has \(3^7=2187\) elements, so each reduced squared magnitude and each reduced zero occurs exactly \(2187\) times in the full spectrum.

**Exact algebraic spectrum.** For each reduced frequency \(q\in\mathbb F_3^9\), count the numbers \(c_0(q),c_1(q),c_2(q)\) of the \(42\) matrices for which the dot product with \(q\) is respectively \(0,1,2\pmod3\). Then \(W(q)=c_0+c_1\omega+c_2\omega^2\) and
\[
|W(q)|^2=c_0^2+c_1^2+c_2^2-c_0c_1-c_0c_2-c_1c_2.
\]
A complete exhaustive evaluation of all \(19683\) reduced frequencies gives \(734\) zero values, \(18949\) nonzero values and \(53\) distinct squared magnitudes. The least positive squared magnitude is \(3\) and the maximum is \(1764\). The explicit reduced frequency whose base-three digits (least significant first) are \((2,2,0,0,1,0,0,0,0)\) has phase counts \((13,15,14)\), so it attains squared magnitude \(3\). The trivial frequency attains \(42\). Multiplying reduced zero and nonzero counts by \(2187\) gives the stated full nullity and rank. Fourier diagonalization yields the sharp inverse-on-range norm and condition number.

**First cancellation structure.** Exhaustively evaluate each of the \(32\) nontrivial single-coordinate frequencies and all \(480\) frequencies with precisely two nonzero entries (choose two of the sixteen coordinates, then coefficients in \(\{1,2\}\)). Exactly \(16\) of the latter vanish. All have opposite nonzero coefficients on one of the eight central horizontal/vertical pairs described above, and none with weight one vanishes. This proves the exhaustive minimum-support classification, including its quantifiers.

## Verification

Both provided Python 3 programs use exact integer arithmetic and no external dependencies. Run `python3 verify_ternary_row.py` and `python3 verify_ternary_triangle.py` in a directory containing those files. The first enumerates valid rows recursively, computes \(19,683\) exact phase-count triples, checks all weight-one and weight-two characters, and checks the full squared-magnitude histogram against the stated invariants. The second independently generates all \(42\) configurations via monotone triangles, performs a nine-axis ternary Fourier transform in the ring \(\mathbb Z[\omega]\), and checks the identical spectrum. Their independently computed \(53\)-level histograms agree entrywise; they also satisfy Parseval's identity
\[
\sum_{q\in\mathbb F_3^9}|W(q)|^2=42\cdot3^9=826686.
\]
The full histogram and its scope are recorded in `SPECTRUM.json`. The finite exhaustive check covers every frequency in the specified finite group, not merely a sample.

## Relationship to prior work

Alternating-sign matrices and the monotone-triangle bijection are classical; neither their definition nor the count \(42\) is new. Propp's 2002 survey describes the bijection and equivalent square-ice models. Ayyer and Romik (2012) and Behrend (2013) develop refined enumerations and boundary or bulk statistics, but their inspected statements do not supply the independent-entry ternary additive-character zero set, the exact \(53\)-level squared-magnitude spectrum, or the resulting deconvolution stability. A separate published binary-incidence Fourier analysis of order-four alternating-sign matrices concerns a different reduction and character field; its binary nonzero-entry multipliers do not directly specialize to the present ternary signed-entry characters. The exact signed matrix census is nevertheless available in classical enumeration data, so the historical novelty assessment concerns the **evaluated Fourier invariants and structural first-zero classification**, not the ability to enumerate \(42\) known objects.

## Limitations

This is a finite, order-four theorem for reduction modulo three. It does not classify general-order alternating-sign matrix Fourier spectra, establish a general modulus law, or claim independent mathematical certification. The published-literature comparison is bounded; hidden historical tables or unpublished computations may affect priority. Numerical approximations were not used to decide Fourier cancellation.

## References

1. J. Propp, *The many faces of alternating-sign matrices*, arXiv:math/0208125v1 (first publicly posted 2002-08-15), https://arxiv.org/abs/math/0208125.
2. A. Ayyer and D. Romik, *New enumeration formulas for alternating sign matrices and square ice partition functions*, arXiv:1202.3651 (first publicly posted 2012-02-16), https://arxiv.org/abs/1202.3651.
3. R. E. Behrend, *Multiply-refined enumeration of alternating sign matrices*, arXiv:1203.3187 (2012 preprint), https://arxiv.org/abs/1203.3187.
4. FindStat, *Alternating sign matrices*, https://www.findstat.org/CollectionsDatabase/AlternatingSignMatrices/.
