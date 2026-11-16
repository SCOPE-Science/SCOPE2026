# Period-seven Walsh invertibility of maximal-independent-set path kernels

## Finding

Let \(n\ge2\), let \(P_n\) be the path on vertices \(1,\ldots,n\), and let \(A_n\subseteq\mathbb F_2^n\) consist of the incidence vectors of its **maximal** independent sets (equivalently, its independent dominating sets). Put \(f_n=\mathbf1_{A_n}\), and use the unnormalized Boolean Fourier transform
\[
\widehat f_n(\omega)=\sum_{x\in A_n}(-1)^{\sum_{j=1}^n\omega_jx_j},\qquad \omega\in\mathbb F_2^n.
\]
Then the following conditions are equivalent:

1. Every Fourier coefficient \(\widehat f_n(\omega)\) is nonzero.
2. Convolution by \(f_n\) is invertible on complex-valued functions on \(\mathbb F_2^n\).
3. \(n\pmod7\in\{0,1,4,6\}\).

In the remaining residue classes \(n\pmod7\in\{2,3,5\}\), a zero Fourier coefficient is produced explicitly below. More strongly, for **every** \(n\ge2\) and every prefix of signs \(z_1,\ldots,z_n\in\{-1,1\}\), the signed path-independent-dominating-set sum \(W_n\) satisfies the seven-letter identity
\[
 W_{n+7}(z_1,\ldots,z_n,+1,-1,+1,-1,+1,-1,+1)
 =-W_n(z_1,\ldots,z_n).
\]
Thus an exact sign-antisymmetry, together with the known Padovan count, yields a full infinite-family Fourier-invertibility classification.

## Assumptions and scope

All sums and Fourier coefficients are over integers before any complex Fourier analysis. The word **maximal** is essential: the set \(A_n\) is not the family of all independent sets and is not the family of maximum-cardinality independent sets. Convolution uses the group law of \(\mathbb F_2^n\), and Fourier transforms are unnormalized. The theorem covers exactly the path graph with \(n\ge2\) vertices; it makes no claim for cycles, general trees, or other graph families.

For a sign vector \(z\in\{-1,+1\}^n\), define
\[
W_n(z)=\sum_{x\in A_n}\prod_{j:x_j=1}z_j.
\]
Every Walsh coefficient is one of these sums with \(z_j=(-1)^{\omega_j}\). Consequently, zero-free means zero-free at **all** \(2^n\) frequency choices.

## Proof

**Step 1: finite-state transfer with the correct boundary conditions.** An incidence word \(x_1\cdots x_n\) belongs to \(A_n\) precisely when no consecutive \(1,1\) occur, no triple \(0,0,0\) occurs, and neither endpoint begins or ends with \(0,0\). Indeed, these are exactly the independence and vertex-domination constraints on the path, for \(n\ge2\).

Order the allowable two-letter internal states as \((00,01,10)\). If the new vertex has sign \(z\), extension by one letter multiplies the row state vector by
\[
T(z)=\begin{pmatrix}0&z&0\\0&0&1\\1&z&0\end{pmatrix}.
\]
The initial row vector and terminal column vector are respectively
\[
v_2=(0,z_2,z_1),\qquad w=(0,1,1)^{\mathsf T}.
\]
Therefore the complete sum is
\[
W_n(z_1,\ldots,z_n)=v_2T(z_3)\cdots T(z_n)w,
\]
with an empty product when \(n=2\). This identity follows by tracking every allowed path word exactly once and multiplying the sign at each selected vertex.

**Step 2: universal seven-letter sign antisymmetry.** Direct integer matrix multiplication gives
\[
T(+1)T(-1)T(+1)T(-1)T(+1)T(-1)T(+1)
=\begin{pmatrix}1&0&0\\0&1&-2\\0&0&-1\end{pmatrix}=:B.
\]
Since \(Bw=-w\), multiplication by this seven-letter block on the right changes \(W_n\) to \(-W_n\), for **every** initial prefix. No asymptotic argument is involved.

**Step 3: parity of the number of maximal independent sets.** Write \(a_n=|A_n|\), with the empty and one-vertex conventions \(a_0=a_1=1\) and \(a_2=2\). Partitioning by whether the first or second vertex is selected yields
\[
a_n=a_{n-2}+a_{n-3},\qquad n\ge3.
\]
This is the Padovan-type recurrence for maximal independent sets of paths. Modulo two, the initial values imply \(a_7\equiv a_0\), \(a_8\equiv a_1\), and \(a_9\equiv a_2\). Both sequences \(a_{n+7}\) and \(a_n\) satisfy the same third-order recurrence modulo two, so \(a_{n+7}\equiv a_n\pmod2\) for all \(n\ge0\). The seven residues \(n=0,1,2,3,4,5,6\) have respective parities \((1,1,0,0,1,0,1)\).

For \(n\pmod7\in\{0,1,4,6\}\), \(a_n\) is odd. Every \(W_n(z)\) is the sum of exactly \(a_n\) signs \(\pm1\), hence is odd and cannot vanish.

**Step 4: witnesses for all remaining dimensions.** For \(n=2,3,5\), choose the respective sign strings
\[
(-1,+1),\qquad(+1,+1,-1),\qquad(-1,+1,+1,+1,+1).
\]
The state formula gives respective final row states \((0,1,-1)\), \((1,-1,1)\), and \((-1,0,0)\), all orthogonal to \(w\), hence \(W_n=0\).

For any \(n\ge2\) with \(n\pmod7\in\{2,3,5\}\), start with the corresponding seed string and append the block \((+1,-1,+1,-1,+1,-1,+1)\) exactly \((n-r)/7\) times, where \(r\in\{2,3,5\}\) is the chosen seed length. Step 2 shows that the signed sum stays zero. The sign choices correspond to genuine Walsh frequencies, so a coefficient vanishes in every such dimension.

**Step 5: invertibility.** Characters on \(\mathbb F_2^n\) diagonalize the linear convolution operator \(g\mapsto f_n*g\), with eigenvalues \(\widehat f_n(\omega)\). Thus it is invertible exactly when no coefficient vanishes. This completes the proof.

## Verification

Run `python check_path_mis.py` with Python 3 (standard library only). The checker independently generates the maximal independent sets using bitwise independence and domination tests, takes an integer Walsh-Hadamard transform for every \(2\le n\le14\), checks all frequencies against the transfer for \(2\le n\le10\), checks the universal seven-step identity through dimension \(110\), and constructs explicit zero witnesses in every relevant dimension through \(210\). The expected completion marker is `PATH_MIS_FOURIER_PERIOD_SEVEN_ALL_CHECKS_PASS`. These finite checks support, but do not replace, the complete transfer-matrix proof above.

## Relationship to prior work

Classical work on maximal independent sets and their enumeration, including Nielsen [1] and Nagy [4], concerns counting and extremal families. Bród [2] records Padovan recurrences for related weak-kernel counts on paths and expressly distinguishes weak kernels from arbitrary maximal independent sets. Kotek et al. [3] develop domination-polynomial recurrences, which count dominating sets without the independence restriction. Neethi and Saxena [5] give an output-sensitive enumeration method for generalized caterpillars. Those combinatorial developments motivate the path family and finite-state methods, but the present claim is specifically about **simultaneous nonvanishing at every Boolean character**, an all-frequency invertibility classification, and a sign-block identity. The Padovan count and the concept of maximal independent sets are not presented as new.

## Limitations

The full multiplicity of zero coefficients in the three vanishing congruence classes is not classified, and no sharp inverse norm is claimed in the zero-free classes. Claims of historical originality are bounded by the cited inspected literature and additional searches; an unindexed earlier equivalent characterization remains possible. Independent mathematical validation has not been performed.

## References

[1] J. M. Nielsen, *On the Number of Maximal Independent Sets in a Graph*, BRICS Report Series RS-02-15 (published 2002-04-05). https://doi.org/10.7146/brics.v9i15.21733

[2] D. Bród, *A Note on a Graph Representation of Padovan Numbers*, Int. J. Contemp. Math. Sciences 5 (2010), 2065–2068. https://www.m-hikari.com/ijcms-2010/41-44-2010/brodIJCMS41-44-2010.pdf

[3] T. Kotek, J. Preen, F. Simon, P. Tittmann, M. Trinks, *Recurrence Relations and Splitting Formulas for the Domination Polynomial*, Electronic Journal of Combinatorics 19(3) (2012), P47. https://doi.org/10.37236/2475

[4] Z. L. Nagy, *On the Number of k-Dominating Independent Sets*, arXiv:1504.03224 (first submitted 2015-04-13). https://arxiv.org/abs/1504.03224

[5] Neethi K. S., S. Saxena, *Maximal Independent Sets in Generalised Caterpillar Graphs*, arXiv:1502.04514 (first submitted 2015-02-16). https://arxiv.org/abs/1502.04514
