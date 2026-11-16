# The first square Fourier-gap jump for binary lonesum matrices

## Finding
For integers \(m,n\ge2\), let \(L_{m,n}\subseteq\mathbb F_2^{mn}\) be the incidence vectors of all binary \(m\times n\) lonesum matrices. Write
\[
W_{m,n}(b)=\sum_{A\in L_{m,n}}(-1)^{\langle b,A\rangle},\qquad b\in\mathbb F_2^{mn},
\]
with row-major coordinates and the ordinary binary dot product. Unnormalized convolution by \(\mathbf 1_{L_{m,n}}\) has Fourier support **exactly** the even-Hamming-weight frequencies, and hence rank \(2^{mn-1}\). This general symmetry-and-parity fact is a consequence of the known poly-Bernoulli enumeration and is included as context, not as an independent novelty claim.

The new exact finite spectral census concerns the first square with a nontrivial jump in the least surviving singular value: for \((m,n)=(4,4)\), there are precisely **34 distinct positive magnitudes** among the \(65,536\) Walsh coefficients, and
\[
\min_{b:\,W_{4,4}(b)\ne0}|W_{4,4}(b)|=6.
\]
Exactly \(6,360\) frequencies attain this minimum. For the two preceding nontrivial squares \((2,2)\) and \((3,3)\), the corresponding minimum is \(2\). All even-weight \(4\times4\) coefficients are congruent to \(6\) modulo \(16\), and all odd-weight coefficients vanish. The largest multiplier magnitude is \(6,902\), attained only at zero frequency. Full signed row/column-permutation orbits and the complete absolute-value distribution are given in the attached exact integer certificates `ORBIT_SPECTRUM.csv` and `MAGNITUDE_SPECTRUM.csv`.

Thus the \(4\times4\) lonesum convolution has rank \(32,768\), exact \(\ell^2\) Moore–Penrose inverse norm \(1/6\), and positive spectral condition number \(3451/3\). Its Fourier range projection is the complementation average
\[
(Pf)(x)=\tfrac12\bigl(f(x)+f(x+\mathbf 1)\bigr),
\]
which has sharp \(\ell^1\) and \(\ell^\infty\) norm \(1\).

## Assumptions and scope
A binary matrix is **lonesum** if its row and column sums uniquely identify it among binary matrices of the same dimensions. Equivalently, its rows are totally ordered by coordinatewise inclusion, or it contains neither diagonal \(2\times2\) permutation pattern as a submatrix. Rows and columns are labeled. All Fourier transforms, convolutions, and singular values are **unnormalized** over the finite additive group \(\mathbb F_2^{mn}\). The \(4\times4\) statement refers to all \(2^{16}=65,536\) frequencies; nothing is asserted for the minimum positive magnitude of larger squares.

## Proof
**Universal Fourier support.** Complementing all entries maps each lonesum matrix to another lonesum matrix, because it reverses inclusion chains. The involution \(A\mapsto A+\mathbf 1\) is fixed-point-free. Thus \(W_{m,n}(b)=0\) whenever \(b\) has odd weight. The classical Stirling-number formula for the number of binary lonesum matrices is
\[
|L_{m,n}|=\sum_{j=0}^{\min(m,n)}(j!)^2 S(m+1,j+1)S(n+1,j+1).
\]
For \(m,n\ge2\), the terms \(j=0,1\) are congruent modulo four to \(1\) and \((2^m-1)(2^n-1)\equiv1\), while every term with \(j\ge2\) is divisible by four. Hence \(|L_{m,n}|\equiv2\pmod4\). For an even-weight frequency, each complementary pair contributes either \(+2\) or \(-2\) to its Walsh coefficient, and there are an odd number \(|L_{m,n}|/2\) of such pairs. Therefore \(W_{m,n}(b)\equiv2\pmod4\) and cannot vanish. This proves the exact rank and range-projection statements.

**Exact first-jump certificate.** At a binary \(4\times4\) matrix represented by its row-major sixteen-bit integer \(x\), the forbidden-submatrix test independently agrees at every \(x\in\{0,\ldots,65535\}\) with the nested-row test. Both select exactly \(6,902\) matrices; the Stirling formula independently evaluates to
\[
1+15^2+4(25)^2+36(10)^2+24^2=6,902.
\]
The attached standalone `checker.py` computes all \(65,536\) Walsh coefficients with the exact integer butterfly \((a,b)\mapsto(a+b,a-b)\). It separately partitions the frequency matrices into **317** orbits under all row and column permutations, and calculates a direct \(6,902\)-term character sum for one representative of each orbit. These two independently evaluated spectra agree at every labeled frequency. The orbit sizes sum to \(65,536\); their minimum positive absolute coefficient is \(6\), achieved for a total orbit size of \(6,360\), and there are exactly \(34\) nonzero magnitude levels. In the same calculation each even-weight multiplier is \(6\pmod{16}\), providing an exact arithmetic obstruction to modulus \(2\) or \(4\) at this width.

Running identical exhaustive tests on the preceding square sizes gives counts \(14\) and \(230\), ranks \(8\) and \(256\), and least positive Walsh magnitudes \(2\) and \(2\). Thus \(4\times4\) is the first square after \(2\times2\) where the spectral gap rises above the universal lower bound \(2\).

**Operator claims.** Each Walsh character diagonalizes unnormalized convolution by \(\mathbf1_{L_{m,n}}\), with eigenvalue \(W_{m,n}(b)\). All eigenvalues are real. The maximum absolute eigenvalue is \(|L_{4,4}|=6902\), since the triangle inequality bounds all Walsh sums and the zero character attains equality. The minimum positive singular value is \(6\) by the independent exact census; the Moore–Penrose operator norm and condition number follow. Fourier support at exactly even-weight frequencies is the orthogonal complement of the all-one vector, so the orthogonal range projection averages antipodal translates. Since this average is a positive unital contraction and preserves constants, its endpoint norms equal one.

## Verification
Run `python3 checker.py <output-directory>` with Python 3 and no third-party packages. It regenerates the two CSV certificates deterministically, checks independent lonesum enumerators, checks full frequency-by-frequency agreement of the orbit/direct-character method and the butterfly transform, verifies Parseval's identity and the congruence modulo sixteen, and checks the two preceding square sizes. Success prints `SQUARE_LONESUM_ORBIT_WALSH_EXACT_PASS`. Certificate row counts are 317 signed orbits and 35 magnitude rows including zero.

## Relationship to prior work
Ryser's forbidden-submatrix characterization and the Stirling/poly-Bernoulli count are classical; the accessible texts of Kim–Krotov–Lee (2011), Cameron–Glass–Rekvényi–Schumacher (first posted 2014), and Bényi–Hajnal (2015) supply these premises. The all-rectangle rank conclusion is a simple new application of those **known** premises, not the novel claim here. The finite novelty assessed is the complete \(4\times4\) signed Walsh orbit census, its 34-level magnitude table, and the sharp first-square spectral-gap jump to six. A previously studied \(2\times n\) lonesum transform does not imply the \(4\times4\) signed spectrum. Kamano–Ohno–Yamamoto (2013) also give a generating polynomial by the total number of ones, which determines the single all-ones character but not arbitrary edge-frequency character sums. The other inspected primary references concern counts, avoidance patterns, orientations, and partitions, rather than the full signed character distribution. Absence of a matching database or literature result in bounded search does not establish absolute historical priority.

## Limitations
The new amplitude classification is finite and specific to labeled binary \(4\times4\) matrices. The general rectangular Fourier-support statement is an elementary corollary of prior enumerations; it should not be counted as a separate discovery. The enumeration is exhaustive and reproducible, but its finite nature does not imply any minimum-amplitude formula for larger sizes or \(q\)-ary lonesum matrices. The exact spectrum has not received independent mathematical audit, and older equivalent enumerations may exist.

## References
1. H. K. Kim, D. S. Krotov, and J. Y. Lee, *Poly-Bernoulli numbers and lonesum matrices*, arXiv:1103.4884, first posted 2011-03-25, https://arxiv.org/abs/1103.4884 . See formula (1.3), Ryser's criterion, and Section 2.
2. P. J. Cameron, C. A. Glass, K. Rekvényi, and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685, first posted 2014-12-11, https://arxiv.org/abs/1412.3685 . See Theorem 3.1 and the bipartite orientation/lonesum identification.
3. B. Bényi and P. Hajnal, *Combinatorics of poly-Bernoulli numbers*, arXiv:1510.05765, first posted 2015-10-20, https://arxiv.org/abs/1510.05765 . See Sections 2.1–2.2.

4. K. Kamano, Y. Ohno, and S. Yamamoto, *Weighted lonesum matrices and their generating function*, Integers 13 (2013), A25, first online publication 2013-05-10, https://www.emis.de/journals/INTEGERS/papers/n25/n25.Abstract.html . Its polynomial weights the **total** entry sum, not sixteen independent edge frequencies.
