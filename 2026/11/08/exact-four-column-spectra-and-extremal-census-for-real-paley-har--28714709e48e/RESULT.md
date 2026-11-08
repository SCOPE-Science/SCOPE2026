# Exact four-column spectra and extremal census for real Paley harmonic frames

## Finding
For every prime \(p\ge5\) with \(p\equiv1\pmod4\), restrict the real Paley equiangular Gram matrix to the \(p\) columns indexed by \(\mathbb F_p\). Exactly three four-column spectral types occur, with explicitly determined multiplicities. The sharp order-four squared-norm deviation is \(\delta_4=1\) at \(p=5\), and \(\delta_4=3/\sqrt p\) at every \(p\ge13\). The full counts and equality configurations are given below.

## Assumptions and scope
Let \(\chi:\mathbb F_p\to\{-1,0,1\}\) denote the Legendre character, and put \(S_{a,b}=0\) when \(a=b\), and \(S_{a,b}=\chi(a-b)\) otherwise. Because \(\chi(-1)=1\), \(S\) is real symmetric. Its eigenvalues are \(0\) once and \(\pm\sqrt p\) with multiplicity \((p-1)/2\) each; hence \(G=I+S/\sqrt p\) is positive semidefinite with unit diagonal and is the Gram matrix of \(p\) real unit vectors in dimension \((p+1)/2\). These vectors are the finite-index part of the standard \(p+1\)-vector Paley equiangular tight frame, without the extra index at infinity. Only subsets of four of these \(p\) columns are considered; no all-\(p+1\)-column assertion is made.

For an unordered four-point set \(X\), let \(S_X\) be its principal submatrix. Write \(T_{abc}=\chi((a-b)(a-c)(b-c))\) for each of the four three-element subsets of \(X\). These numbers lie in \(\{-1,1\}\), and their product equals \(1\). Thus exactly \(0\), \(2\), or \(4\) of them are negative. We count every unordered \(X\) once.

## Proof
**Spectral trichotomy.** Switching rows/columns of \(S_X\) by independent signs leaves its spectrum unchanged. First make all three edges emanating from one vertex positive. The remaining three signs are precisely the three triangle products involving that vertex. If all four \(T\)'s are positive, the switched matrix is \(J_4-I_4\), with spectrum \(\{3,-1,-1,-1\}\). If all four are negative, it has the spectrum \(\{-3,1,1,1\}\). If exactly two are negative, a further permutation gives the matrix with edges from vertex one all positive and remaining signs \((-1,1,1)\); its characteristic polynomial is \((u^2-1)(u^2-5)\). Consequently the third spectrum is \(\{-\sqrt5,-1,1,\sqrt5\}\). Adding \(I\) and scaling by \(p^-0.5\) proves the asserted three Gram spectra.

**Counting.** Let \(L=p(p-1)(p-2)(p-3)\) count ordered distinct quadruples. For each unordered pair of distinct triangles in such a quadruple, the product of their two \(T\)-values is \(\chi((c-a)(c-b)(d-a)(d-b))\) for some order of \(a,b,c,d\). For fixed distinct \(a,b\), the standard quadratic character identity \(\sum_{c\in\mathbb F_p}\chi((c-a)(c-b))=-1\), together with the zero terms at \(a,b\), gives
\[
\sum_{\substack{c,d\notin\{a,b\}\\c\ne d}}\chi((c-a)(c-b)(d-a)(d-b))=1-(p-2)=3-p.
\]
Hence each of the six unordered pairs of triangles has the aggregate sum \(p(p-1)(3-p)\). Let \(U\) count the ordered quadruples for which all four triangle signs agree. Since their product is one, the indicator for all signs agreeing is precisely \((2+\sum_{i<j}T_iT_j)/8\). Thus
\[
U=\frac{2L+6p(p-1)(3-p)}8=\frac{p(p-1)(p-3)(p-5)}4.
\]
Dividing by \(4!=24\) gives exactly \(p(p-1)(p-3)(p-5)/96\) unordered four-sets of the two extreme types combined. Multiplying all four vertices by a fixed quadratic nonresidue reverses every edge sign, so interchanges the all-positive and all-negative triangle types. These types therefore have equal numbers, each \(p(p-1)(p-3)(p-5)/192\). Subtracting from \(\binom p4\) gives the middle count.

**Sharp deviation and equality.** The spectral deviation \(\|G_X-I_4\|_{\mathrm{op}}\) is \(3/\sqrt p\) in either extreme class and \(\sqrt{5/p}\) in the middle class. At \(p=5\), the extreme counts vanish and all five four-sets have middle type, giving \(\delta_4=1\). For every admissible prime \(p\ge13\), the extreme counts are positive and \(3>\sqrt5\), giving the claimed sharp deviation and precisely the asserted maximizing sets. No probabilistic sampling or asymptotic argument is used.

## Verification
The standalone `verify.py` enumerates all unordered four-subsets for primes \(5,13,17,29,37,41\); computes triangle signs directly from quadratic residues; matches every class count to the closed formulas; checks the quadratic-character pair identity; and verifies the three four-by-four characteristic polynomials by integer determinants. These finite checks corroborate, but do not replace, the all-prime proof.

## Relationship to prior work
Magsino, Mixon and Parshall (2019) analyze asymptotic spectral measures for random subensembles of symmetric Paley conference frames and provide the Paley Gram normalization. Satake (2020) studies the Paley restricted-isometry property at growing sparsity under conjectural hypotheses; the present exact deterministic four-column count is a different finite-order statement. Brouwer and Martin (2021) analyze common-neighbor and triple-intersection counts in Paley graphs; their intersections are graph-theoretic context, not an explicit four-column frame spectrum and sharp restricted-isometry census. A published harmonic-frame study for primes congruent to three modulo four classifies four-column spectra in the skew-Paley tournament setting; its hypotheses exclude the symmetric prime class treated here.

## Limitations
The result is restricted to primes \(p\equiv1\pmod4\), exactly four columns among the finite-index \(p\) columns, and the real symmetric Gram model. It does not classify configurations involving the additional Paley frame vector, arbitrary four-column subframes of other ETFs, higher sparsity, or reconstruction performance under noisy sampling. Historical priority remains provisional; the classical theory of Seidel switching and strongly regular Paley graphs might imply the counts indirectly. Independent mathematical validation has not been performed.

## References
1. M. Magsino, D. G. Mixon, H. Parshall, *Kesten–McKay law for random subensembles of Paley equiangular tight frames*, arXiv:1905.04360 (first public 2019-05-10), https://arxiv.org/abs/1905.04360.
2. S. Satake, *On the restricted isometry property of the Paley matrix*, arXiv:2011.02907 (first public 2020-10-19), https://arxiv.org/abs/2011.02907.
3. A. E. Brouwer, W. J. Martin, *Triple intersection numbers for the Paley graphs*, arXiv:2109.03654 (first public 2021-09-08), https://arxiv.org/abs/2109.03654.
4. *Four-column spectral census and sharp distortion of Paley harmonic frames*, published research record (2026-10-11, prime class \(p\equiv3\pmod4\)); see public results archive.
