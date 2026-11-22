# Integral Smith factors of unit-restricted prime-square GCD-difference kernels

## Finding
For a rational prime \(p\), let \(U_p=(\mathbb Z/p^2\mathbb Z)^\times\), and form the integer matrix
\[
G_p=\bigl(\gcd(a-b,p^2)\bigr)_{a,b\in U_p},\qquad N=p(p-1).
\]
The representative chosen for \(a-b\) does not matter. Write \(s=p-1\). For every odd prime \(p\), the **complete integral Smith normal form** of \(G_p\), with exponents denoting multiplicities, is
\[
\operatorname{SNF}(G_p)=\operatorname{diag}\left(
1,\ s^{[s-1]},\ (ps)^{[s(s-1)]},\ p^2s,\ (2p^2s)^{[s-2]},\ 6p^2s^2
\right).
\]
Here \(d^{[j]}\) denotes \(j\) consecutive entries equal to \(d\), rather than exponentiation; an empty block is omitted. The displayed entries form a divisibility chain. For \(p=2\), the Smith form is \(\operatorname{diag}(2,6)\). Thus \(G_p\) is nonsingular for every prime \(p\), and its integer cokernel is completely determined. For odd \(p\), its largest Smith factor is \(6p^2(p-1)^2\). If \(p\equiv2\pmod3\), the cokernel has exactly one independent \(3\)-primary cyclic factor of order \(3\), despite \(3\nmid p(p-1)\).

## Assumptions and scope
Indices are **the unit residues** modulo the prime square \(p^2\), not all residues, and the kernel is the ordinary greatest common divisor of their difference with \(p^2\), not the ordinary two-index GCD \(\gcd(a,b)\) or a Ramanujan sum. All row and column operations below are integral unimodular operations, so the conclusions concern integer Smith factors, not only rational eigenvalues. The theorem asserts the complete prime-square case; it does not assert a formula for higher prime powers or for arbitrary composite moduli.

## Proof
Fix an odd prime \(p\), put \(s=p-1\), \(c=ps\), and enumerate the units in \(s\) congruence classes modulo \(p\), each of size \(p\). Write \(J_m\) for the \(m\)-by-\(m\) all-ones matrix. A pair of indices in different classes has GCD value \(1\); a pair of distinct indices in the same class has GCD value \(p\); and a repeated index has value \(p^2\). Therefore, with \(N=sp\),
\[
G_p=cI_N+s(I_s\otimes J_p)+J_N. \tag{1}
\]
The determinant and all integer factors can be determined without dividing by \(p\) or \(s\).

Within each class \(a\), use the integer basis \(E_a=e_{a,0}\) and \(D_{a,j}=e_{a,j}-e_{a,0}\) for \(1\le j<p\). This basis is unimodular. The vector of all ones in class \(a\) is \(pE_a+\sum_{j=1}^{p-1}D_{a,j}\). Since the zero-sum difference vectors satisfy \(G_pD_{a,j}=cD_{a,j}\), the matrix in these bases is block lower triangular with upper-left block \(2cI_s+pJ_s\), lower-right block \(cI_{s(p-1)}\), and lower-left rows \(s e_a^T+\mathbf 1_s^T\), identical for the \(p-1\) difference rows in each class. Since the integer vector \((1,\ldots,1)\) is primitive, an integral unimodular change of basis in each difference block carries this repeated-row direction to one coordinate; applying inverse changes to the corresponding domain coordinates leaves its scalar diagonal block unchanged. Hence \(G_p\) is integrally equivalent to
\[
 cI_{s(p-2)}\ \oplus\ M_s,
\qquad
M_s=\begin{pmatrix}2psI_s+pJ_s&0\\sI_s+J_s&psI_s\end{pmatrix}. \tag{2}
\]

In both copies of \(\mathbb Z^s\) in \(M_s\), use the unimodular basis consisting of \(\mathbf 1_s=(1,\ldots,1)\) and \(e_1,\ldots,e_{s-1}\). In the latter \(s-1\) coordinates, the only coupling to the \(\mathbf 1_s\) coordinate is through the sum of coordinates. Replacing \(e_j\) by \(e_j-e_1\) for \(2\le j\le s-1\) in both copies, together with corresponding inverse row/column basis changes, isolates \(s-2\) identical two-by-two blocks and one four-by-four block:
\[
M_s\ \sim_{\mathbb Z}\ 
\bigoplus_{j=1}^{s-2}T\ \oplus\ K,
\quad
T=\begin{pmatrix}2ps&0\\s&ps\end{pmatrix},
\quad
K=\begin{pmatrix}
2ps&0&0&0\\
p&3ps&0&0\\
s&0&ps&0\\
1&2s&0&ps
\end{pmatrix}. \tag{3}
\]
The basis changes are integral and invertible, not orthogonal or rational diagonalizations.

The gcd of all entries of \(T\) is \(s\), and \(|\det T|=2p^2s^2\), so its Smith factors are \(s,2p^2s\). For \(K\), the bottom-left entry is \(1\), so its first determinantal divisor is \(1\). Every two-by-two minor is divisible by \(s\); two such minors are \(-ps\) and \(2s^2\), whose gcd is \(s\) because \(p\) is odd and \(\gcd(p,s)=1\). Thus the second determinantal divisor is \(s\). Every three-by-three minor is divisible by \(p^2s^2\): dividing the eight nonzero minors by this factor gives the explicit list \(6ps,6ps,-4s,2ps,1,-3s,p,3ps\). In particular, the minor on rows \(2,3,4\) and columns \(1,2,3\) (one-based indexing) equals \(p^2s^2\). Finally \(|\det K|=6p^4s^4\). By the determinantal-divisor characterization, \(K\) has Smith factors
\[
1,\quad s,\quad p^2s,\quad 6p^2s^2. \tag{4}
\]
Combining (2)--(4) produces precisely the asserted list. It is already ordered by divisibility, since \(s\mid ps\mid p^2s\mid2p^2s\mid6p^2s^2\). The total multiplicity is \(sp\), as required.

For \(p=2\), the two unit residues modulo four are \(1,3\), giving
\[
G_2=\begin{pmatrix}4&2\\2&4\end{pmatrix}
\quad\Longrightarrow\quad \operatorname{SNF}(G_2)=\operatorname{diag}(2,6).
\]
Finally, if \(p\equiv2\pmod3\), then \(3\) divides neither \(p\) nor \(s\); among all invariant factors exactly the final \(6p^2s^2\) contains a factor \(3\), once. This proves the stated exceptional torsion consequence.

## Verification
The companion script \(verify.py\) constructs the original integer matrix for \(p=2,3,5\), computes its Smith form by exact integer arithmetic, and compares the entire diagonal with the theorem. It independently enumerates every minor of \(K\) for a range of larger odd primes, confirming determinantal divisors \(1,s,p^2s^2,6p^4s^4\). The script checks the entrywise identity (1) for additional primes. These computations are finite stress tests; the all-prime claim follows from the unimodular reductions and determinantal-divisor proof above.

## Relationship to prior work
The classical Smith-GCD matrix \((\gcd(i,j))\) on factor-closed sets has a known integer Smith form (Ilmonen--Haukkanen). It is **not** the difference kernel studied here. The prime-power GCD-graph literature (Sander--Sander) classifies spectra and energies of full-residue circulant adjacency matrices; it does not compute the integral cokernel of the unit-indexed GCD-difference principal submatrix. Other closely related arithmetic Fourier work computes the Smith form of full Ramanujan-sum circulants or unit-restricted Ramanujan Gram matrices, but a different kernel and its Smith factors do not imply this formula by integral equivalence. The restriction to units breaks the full additive-circulant structure, and eigenvalues alone do not give Smith invariants. No identical full formula was located in the checked sources or mathematical finding index.

## Limitations
This is the prime-square case, not a classification for arbitrary prime powers or composites. The claim is mathematical and proved by explicit integer operations; computational checks are supporting evidence only. Earlier equivalent results in unindexed literature are a residual bibliographic risk, especially general integer forms of multipartite block matrices. No independent external mathematical audit has been performed.

## References
- J. W. Sander and T. Sander, *The maximal energy of classes of integral circulant graphs*, arXiv:1205.4603 (first public version 2012-05-21), especially the introduction and sections on prime-power GCD-difference graph spectra: https://arxiv.org/abs/1205.4603.
- X. Liu and S. Zhou, *Spectral properties of unitary Cayley graphs of finite commutative rings*, arXiv:1205.5932 (2012-05-27), sections 1--3: https://arxiv.org/abs/1205.5932.
- P. Ilmonen and P. Haukkanen, *Smith meets Smith: Smith normal form of Smith matrix*, Linear Multilinear Algebra 59 (2011), 557--564, DOI:10.1080/03081081003709819 (ordinary index-GCD matrix, not the present difference kernel).
