# Antipodal Hamming-shell Walsh frames: five spectral bands and a sharp square-dimensional design

## Finding

Write \(\Omega_n=\{-1,1\}^n\), equipped with uniform probability. For \(n\ge5\), let \(V_{\le2}\subset L^2(\Omega_n)\) be the complex Walsh band of degrees zero, one and two, with orthonormal characters \(\chi_I(x)=\prod_{i\in I}x_i\), \(|I|\le2\). For an integer \(s\) satisfying
\[
1\le s\le n-4,\qquad s\equiv n\pmod2,
\]
let \(E_{n,s}=\{x\in\Omega_n:|\sum_i x_i|=s\}\), the union of two complementary interior Hamming shells. Equip it with its *conditional uniform probability measure*, and write \(R_{n,s}:V_{\le2}\to L^2(E_{n,s})\) for restriction. The conditional Gram operator \(G_{n,s}=R_{n,s}^*R_{n,s}\) has exactly one zero eigenvalue, with kernel
\[
\operatorname{span}\left\{\sum_{i<j}x_ix_j-\frac{s^2-n}{2}\right\}.
\]
Its nonzero eigenvalues, with multiplicities (coincident entries are combined), are precisely
\[
\begin{array}{c|c|c}
\text{sector}&\text{eigenvalue}&\text{multiplicity}\\ \hline
\text{odd, radial}&s^2/n&1\\
\text{odd, standard}&(n^2-s^2)/(n(n-1))&n-1\\
\text{even, radial}&1+(s^2-n)^2/(2n(n-1))&1\\
\text{even, standard}&s^2(n^2-s^2)/(n(n-1)(n-2))&n-1\\
\text{even, quadratic}&(n^2-s^2)((n-2)^2-s^2)/(n(n-1)(n-2)(n-3))&n(n-3)/2.
\end{array}
\]
Thus the sampling operator identifies the entire quadratic Walsh band modulo a single radial polynomial, unlike a single shell, which has an \((n+1)\)-dimensional kernel. For the usual spatial concentration operator \(P_{\le2}M_{\mathbf1_{E_{n,s}}}P_{\le2}\), multiply every nonzero displayed eigenvalue by \(2^{1-n}\binom n{(n-s)/2}\).

**Sharp square-dimensional optimal design.** Suppose \(n=m^2\), where \(m\ge3\) is an integer. Among *all* admissible complementary-shell pairs \(E_{n,s}\), the squared nonzero-singular-value condition number \(\kappa_+(R_{n,s})^2=\lambda_{\max}^+(G_{n,s})/\lambda_{\min}^+(G_{n,s})\) is uniquely minimized at \(s=m\), equivalently at Hamming weights \((m^2-m)/2\) and \((m^2+m)/2\). The exact optimum is
\[
\boxed{\min_s\kappa_+(R_{m^2,s})^2=\frac{m^2(m^2-3)}{(m^2-1)(m^2-4)},\qquad
\kappa_+\longrightarrow1\quad(m\to\infty).}
\]
At the optimal pair the conditional distribution is three-wise independent (every nonempty Walsh character of degree at most three has mean zero); no other admissible complementary-shell pair has this property. Its nontrivial Gram spectrum has eigenvalue \(1\) of multiplicity \(n+1\), eigenvalue \(n/(n-2)\) of multiplicity \(n-1\), and eigenvalue \(1-2/((n-2)(n-3))\) of multiplicity \(n(n-3)/2\).

## Assumptions and scope

All claims concern the full degree-at-most-two Walsh coefficient Hilbert space with its uniform-cube \(L^2\) norm. The measurement norm on \(E_{n,s}\) is conditional probability, not unnormalized counting measure. The nonzero condition number is taken on the orthogonal complement of the unavoidable one-dimensional kernel, not on the whole noninjective space. The antipodal pair consists of **full** Hamming shells, not random point samples. Weights of both component shells are equal because the two shells have the same cardinality. In the optimum, \(n=m^2\ge9\). The restrictions on \(s\) guarantee both shells have weight between two and \(n-2\) and are distinct. No optimality is asserted for asymmetric shell pairs, for arbitrary sampling distributions, or for degree greater than two.

## Proof

**Step 1: Two-shell moments.** Let \(X=\sum_{i=1}^n x_i\) and denote expectation under conditional uniform measure on \(E_{n,s}\) by \(\mathbb E_s\). Since the set is invariant under \(x\mapsto-x\), every odd Walsh moment vanishes. Since \(X^2=s^2\) pointwise, for distinct \(i,j\),
\[
\rho:=\mathbb E_s[x_ix_j]=\frac{s^2-n}{n(n-1)}.
\]
From Newton's identities applied to \(\prod_i(1+zx_i)\), the four-distinct-coordinate moment is
\[
\tau:=\mathbb E_s[x_ix_jx_kx_\ell]=\frac{s^4-(6n-8)s^2+3n(n-2)}{n(n-1)(n-2)(n-3)}.
\]
The same expressions can be derived directly by counting signs in the two equal-size Hamming layers. These are the only needed nontrivial moments, because a product of two Walsh characters of degree at most two reduces to a character of degree at most four.

**Step 2: Odd sector.** Odd and even Walsh degrees are orthogonal under \(\mathbb E_s\). The odd sector has basis \(x_i\). Its conditional Gram matrix has diagonal entries one and off-diagonal entries \(\rho\). The radial vector \(n^{-1/2}\sum_i x_i\) consequently has eigenvalue \(1+(n-1)\rho=s^2/n\). The orthogonal coordinate-contrast space has eigenvalue \(1-\rho=(n^2-s^2)/(n(n-1))\) with multiplicity \(n-1\).

**Step 3: Even radial sector.** Write \(Q=\sum_{i<j}x_ix_j=(X^2-n)/2\), so \(Q=(s^2-n)/2=:q\) on \(E_{n,s}\). Under the ambient cube measure, \(1\) and \(Q/\sqrt{\binom n2}\) are orthonormal. Their conditional Gram is the rank-one matrix
\[
\begin{pmatrix}1&q/\sqrt{\binom n2}\\q/\sqrt{\binom n2}&q^2/\binom n2\end{pmatrix},
\]
with eigenvalues \(1+q^2/\binom n2=1+(s^2-n)^2/(2n(n-1))\) and zero. The zero vector is exactly \(Q-q\), up to normalization.

**Step 4: Even standard and quadratic sectors.** The degree-two coefficient space, indexed by unordered pairs, decomposes orthogonally under permutations into a radial line, a standard space of dimension \(n-1\), and the zero-row-sum space of dimension \(n(n-3)/2\). An explicit standard vector is
\[
U_a(x)=\sum_i a_i\sum_{j\ne i}x_ix_j=X\sum_i a_i x_i,\qquad\sum_i a_i=0.
\]
Its ambient squared norm is \((n-2)\sum_i|a_i|^2\), and its conditional squared norm is \(s^2(1-\rho)\sum_i|a_i|^2\). Therefore the even standard eigenvalue is \(s^2(n^2-s^2)/(n(n-1)(n-2))\).

On the zero-row-sum space, the conditional pair-character Gram has entry one for coincident pairs, \(\rho\) for pairs meeting in one coordinate, and \(\tau\) for disjoint pairs. The adjacency sums on any zero-row-sum array \(b_{ij}\) are exactly \(-2b_{ij}\) for pairs meeting the selected pair and \(+b_{ij}\) for disjoint pairs (total row sums and global sum vanish). Thus the eigenvalue is \(1-2\rho+\tau\), which factors to
\[
\frac{(n^2-s^2)((n-2)^2-s^2)}{n(n-1)(n-2)(n-3)}.
\]
All five listed levels are strictly positive when \(1\le s\le n-4\), and the indicated orthogonal sectors exhaust the ambient dimension \(1+n+\binom n2\). This proves the spectrum and exact kernel.

**Step 5: Optimal antipodal shells when the dimension is a square.** Put \(n=m^2\), \(m\ge3\), and first take \(s=m\). In the formulas above, \(\rho=0\) and \(\tau=-2/((n-2)(n-3))\). The five levels become
\[
1,\quad1,\quad1,\quad \frac n{n-2},\quad 1-\frac2{(n-2)(n-3)}.
\]
The maximum and minimum are the last two displayed levels; their ratio is
\[
R_*:=\frac{n(n-3)}{(n-1)(n-4)}
=1+\frac{2(n-2)}{(n-1)(n-4)}<1+\frac4n
\]
for every \(n\ge9\).

Every other admissible \(s\) has the same parity as \(m\), hence either \(s\le m-2\) or \(s\ge m+2\). If \(s<m\), the odd radial level is \(s^2/n<1\), while the even radial level is at least one; hence
\[
\kappa_+^2\ge\frac n{s^2}\ge\frac{m^2}{(m-2)^2}>1+\frac4{m^2}>R_*.
\]
If \(s>m\), the odd radial level is \(s^2/n>1\) while the odd standard level is strictly below one, so
\[
\kappa_+^2>\frac{s^2}{n}\ge\frac{(m+2)^2}{m^2}>1+\frac4{m^2}>R_*.
\]
Both inequalities are strict, proving the claimed unique global optimum within this family. Since \(R_*\to1\), the nonzero singular values become asymptotically equal after a common normalization. Finally, antipodal symmetry annihilates all degree-one and degree-three characters; degree-two characters have mean \(\rho\), so three-wise independence holds exactly when \(s^2=n\), which is precisely the optimal case.

## Verification

The standalone program `artifacts/verify.py` constructs actual degree-\(\le2\) Walsh evaluation matrices from all points of each two-shell set and compares the full Hermitian Gram spectrum with the five formulas for every admissible \(s\) in dimensions \(5\) through \(11\). It verifies one-dimensional nullity, exact normalizations, and the formula for the shell probability. It also uses exact rational arithmetic for the proposed square-dimensional eigenvalues, their sharp ratio and their inequalities at the nearest competing shell radii for \(3\le m\le500\). The output marker from the delivered package is `ANTIPODAL_TWO_SHELL_CHECKS_PASS 3566`. Reproduce with `python3 artifacts/verify.py` and NumPy. The finite checks corroborate but do not substitute for the unrestricted algebraic argument in the Proof section.

## Relationship to prior work

The complete Johnson-slice decomposition and its basis are classical, as developed by Filmus (first posted in 2014), and Rao (first posted in 2021) studies Fourier coefficients of restrictions *of functions already defined on one slice* to coordinate sub-slices. These are foundational but do not specify a two-shell inverse-Walsh Gram spectrum or the global shell-pair conditioning design. Bannai, Bannai and Bannai (2013) treat cardinality-tight relative designs on two shells, a different tightness criterion; the three-wise-independence observation here is elementary and is not claimed as a historical discovery.

A published result titled *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells* (published-finding corpus, 2026) provides the three positive eigenvalues and their resonances **for one shell**. The two-shell statement is neither a special case nor an immediate substitution: the complementary-shell sum splits radial and standard modes by Walsh parity, restoring all but a one-dimensional kernel, and its sharp optimal-radius theorem compares the full nonzero spectra of different paired sampling designs. In particular, the prior single-shell resonance occurs in dimensions one greater than a square, rather than the square-dimensional optimum established here. Published results for degree-one Fourier sampling on nonbinary single shells and for Boolean Hamming balls concern different bandwidths or regions. These works supply strong techniques and partial spectral information, not the paired-shell optimization claim.

## Limitations

The result applies only to full *antipodal* interior Hamming-shell pairs and the complete quadratic Walsh band, under equal point weights. Asymmetric pairs, nonuniform shell weights, stochastic subsampling and higher degrees are not covered. The reconstruction condition number is for the identifiable quotient and does not remove the one-dimensional radial ambiguity. Explicit general Johnson or Terwilliger block formulas in older literature could imply some eigenvalues by specialization; historical priority for the full sharp optimization claim remains provisional. Independent mathematical validation has not been performed.

## References

1. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213v1, first posted 2021-11-05. https://arxiv.org/abs/2111.03213
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142v1, first posted 2014-06-01; Electron. J. Combin. 23 (2016), P1.23. https://arxiv.org/abs/1406.0142
3. E. Bannai, E. Bannai and H. Bannai, *On the existence of tight relative 2-designs on binary Hamming association schemes*, arXiv:1304.5760v1, first posted 2013-04-21. https://arxiv.org/abs/1304.5760
4. *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, published-finding corpus (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95
5. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, published-finding corpus (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594
