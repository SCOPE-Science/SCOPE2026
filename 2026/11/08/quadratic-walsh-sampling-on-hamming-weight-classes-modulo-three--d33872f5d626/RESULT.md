# Quadratic Walsh sampling on Hamming-weight classes modulo three: exact spectrum and injectivity threshold

## Finding

For every integer \(n\ge4\) and residue \(r\in\{0,1,2\}\), put
\[
\Omega_n=\{-1,1\}^n,\quad
X_{n,r}=\{x\in\Omega_n: w(x)\equiv r\pmod3\},\quad
w(x)=\#\{j:x_j=-1\}.
\]
Let \(V_{\le2}=\operatorname{span}\{\chi_I: I\subseteq[n],\ |I|\le2\}\), where \(\chi_I(x)=\prod_{i\in I}x_i\), and equip \(X_{n,r}\) with **uniform probability**. The squared sampling singular values are the eigenvalues of the coefficient Gram matrix
\[
G_{n,r}[I,J]=\frac1{|X_{n,r}|}\sum_{x\in X_{n,r}}\chi_I(x)\chi_J(x),\qquad |I|,|J|\le2.
\]
Write \(N=\binom n2\), \(\theta=(n-2r)\pi/3\), \(D=2^n+2\cos\theta\), and
\[
 m_0=1,\quad m_j=\frac{2\,3^{j/2}\cos(\theta-j\pi/2)}{D}\quad(1\le j\le4).
\]
In particular \(m_3=-3m_1\) and \(m_4=-3m_2\). Define the real symmetric matrices
\[
T=\begin{pmatrix}
1&\sqrt n\,m_1&\sqrt N\,m_2\\
\sqrt n\,m_1&1+(n-1)m_2&\sqrt{N/n}\,[2m_1+(n-2)m_3]\\
\sqrt N\,m_2&\sqrt{N/n}\,[2m_1+(n-2)m_3]&1+2(n-2)m_2+\binom{n-2}{2}m_4
\end{pmatrix},
\]
\[
S=\begin{pmatrix}
1-m_2&\sqrt{n-2}(m_1-m_3)\\
\sqrt{n-2}(m_1-m_3)&1+(n-4)m_2-(n-3)m_4
\end{pmatrix},\quad L=1-2m_2+m_4=1-5m_2.
\]
The **entire spectrum, including zero eigenvalues**, is
\[
\boxed{\operatorname{spec}(G_{n,r})=\operatorname{spec}(T)\ \sqcup\
\big(\operatorname{spec}(S)\text{ each repeated }n-1\text{ times}\big)\ \sqcup\
\big\{L\text{ repeated }n(n-3)/2\text{ times}\big\}.}
\]
Coincidences are counted with multiplicity. This determines every sharp sampling bound by diagonalizing matrices of size at most three, regardless of \(n\).

The exact rank has an equally simple combinatorial form. Set
\[
 h_j(n,r)=\#\{k\in\mathbb Z:j\le k\le n-j,\ k\equiv r\pmod3\}\quad(j=0,1,2).
\]
Then
\[
\boxed{\operatorname{rank}G_{n,r}=\min(3,h_0)+(n-1)\min(2,h_1)+\frac{n(n-3)}2\min(1,h_2).}
\]
Consequently, **sampling is injective on every quadratic Walsh polynomial if and only if either \(n\ge8\), or \(n=7\) and \(r\in\{0,1\}\)**. The remaining \(n=7,r=2\) mask has exactly one null direction, and none of the three masks is injective for \(4\le n\le6\).

For every \(n\ge4\), two residue classes have identical spectra. More precisely, putting \(\epsilon=(-1)^n\), the two classes have
\[
 |m_1|=\frac3{2^n-\epsilon},\qquad m_2=\frac{3\epsilon}{2^n-\epsilon},
\]
while the third has \(m_1=0\) and \(m_2=-6\epsilon/(2^n+2\epsilon)\). As \(n\to\infty\), the squared condition ratios \(\rho=\lambda_{\max}(G)/\lambda_{\min}(G)\) satisfy
\[
\boxed{\rho_{\mathrm{paired}}=1+\frac{9n^2}{2^{n+1}}+O(n^{3/2}2^{-n}),\qquad
\rho_{\mathrm{third}}=1+\frac{9n^2}{2^n}+O(n^{3/2}2^{-n}).}
\]
The ratios here are taken in dimensions where the matrices are positive definite. Therefore the paired classes strictly outperform the third for all sufficiently large \(n\); no claim about a smallest universal finite optimality threshold is needed.

## Assumptions and scope

All functions are complex-valued. Walsh coefficient vectors use the orthonormal Fourier character basis of the **uniform full cube**; spatial samples use the **conditional probability measure on the selected residue class**. The two normalizations are different: replacing conditional spatial probability by the inherited full-cube measure scales all Gram eigenvalues by \(|X_{n,r}|/2^n\), without changing rank or condition number. The statement concerns the complete bandwidth through degree two, not the homogeneous degree-two space alone. It includes every integer \(n\ge4\) and all three residues.

## Proof

**1. The exact four Fourier moments.** For a fixed \(j\)-subset \(I\), exchangeability makes \(m_j=|X_{n,r}|^{-1}\sum_{x\in X_{n,r}}\chi_I(x)\) depend only on \(j\). Let \(\omega=e^{2\pi i/3}\). The root-of-unity filter for Hamming weight gives
\[
|X_{n,r}|=\frac13\left(2^n+2\operatorname{Re}[\omega^{-r}(1+\omega)^n]\right)=\frac D3,
\]
\[
\sum_{x\in X_{n,r}}\chi_I(x)=\frac23\operatorname{Re}[\omega^{-r}(1-\omega)^j(1+\omega)^{n-j}]\quad(j\ge1).
\]
Since \(1+\omega=e^{i\pi/3}\), \(1-\omega=\sqrt3e^{-i\pi/6}\), the displayed formula for \(m_j\) follows, and the identities \(m_3=-3m_1\), \(m_4=-3m_2\) are exact. Moreover \(G[I,J]=m_{|I\triangle J|}\).

**2. Three isotypic sectors.** Split the coordinate index set \(\{I:|I|\le2\}\) into the constant index, singletons, and pairs. Under coordinate permutations, this space is an orthogonal direct sum of a three-dimensional trivial component, two copies of the \((n-1)\)-dimensional standard component, and a pair-harmonic component of dimension \(n(n-3)/2\). The last consists of symmetric pair arrays \((a_{ij})\) with \(\sum_{j\ne i}a_{ij}=0\) for every \(i\). Its dimension is \(N-n\), since the point-pair incidence map has rank \(n\) for \(n\ge4\).

On the normalized bases consisting of the constant vector, the sum of all singleton coordinates divided by \(\sqrt n\), and the sum of all pair coordinates divided by \(\sqrt N\), counting the possible differences \(|I\triangle J|\) gives exactly the matrix \(T\). On each standard component, the point-pair incidence matrix has singular value \(\sqrt{n-2}\); hence the two-copy block is exactly \(S\). The pair-sharing-one Johnson adjacency has eigenvalue \(-2\) on pair-harmonics, and the disjointness adjacency has eigenvalue \(1\). Hence the final scalar is \(L=m_0-2m_2+m_4\). This proves the spectral decomposition and all multiplicities, without relying on a numerical eigenvalue computation.

**3. Exact rank from restriction to shells.** Write \(z_i=(1-x_i)/2\) and \(W=\sum_i z_i\). The space of squarefree polynomials of degree at most two decomposes into three inequivalent permutation types: radial polynomials \(p(W)\) of degree at most two (three copies of the trivial representation); standard polynomials \((\sum_i c_i z_i)q(W)\), with \(\sum_i c_i=0\) and \(\deg q\le1\) (two copies of the standard representation); and harmonic pair polynomials \(\sum_{i<j}c_{ij}z_iz_j\), with all row sums of \(c\) zero (one pair-harmonic copy). These span the full coefficient dimension \(3+2(n-1)+n(n-3)/2=1+n+N\).

On the shell \(W=k\), the three types respectively restrict to \(p(k)\), \(q(k)\sum_i c_i z_i\), and the pair harmonic. A standard vector has nonzero slice norm precisely for \(1\le k\le n-1\); a nonzero pair-harmonic has positive slice norm precisely for \(2\le k\le n-2\). The latter follows directly by the Johnson pair incidence rank (equivalently, exchange-difference argument), as in the orthogonal harmonic-slice basis. Functions of distinct permutation type are orthogonal under any permutation-invariant mask. Therefore restriction to the **union** of shells with \(k\equiv r\pmod3\) has rank \(\min(3,h_0)\) in the trivial sector, \((n-1)\min(2,h_1)\) in the standard sector, and \(n(n-3)/2\) if \(h_2\ge1\), otherwise zero. This gives the claimed exact rank. Counting the residue-class shell indices proves the injectivity cutoff and the unique one-dimensional exception at \((n,r)=(7,2)\). In that exceptional case the complete nullspace is generated by the nonzero quadratic function \( (W-2)(W-5)\), which vanishes at exactly the two sampled Hamming weights.

**4. Spectral pairing and asymptotic gap.** Three consecutive residue phases \(\theta=(n-2r)\pi/3\) consist of one angle with \(\sin\theta=0\), \(\cos\theta=\epsilon\), and two angles with \(\cos\theta=-\epsilon/2\), \(\sin\theta=\pm\sqrt3/2\). The latter two have equal \(m_2,m_4\) and opposite \(m_1,m_3\); conjugation by the sign change of the singleton coordinate block takes one Gram matrix into the other, proving exact isospectrality.

Put \(a=(n-2)(13-3n)/2\). The bottom-right entry of \(T\) is \(1+a m_2\). All other diagonal deviations from one are \(O(n2^{-n})\), and all off-diagonal entries are \(O(n^{3/2}2^{-n})\). Likewise \(S-I\) and \(L-1\) have norm \(O(n2^{-n})\). Weyl's eigenvalue inequality therefore leaves one eigenvalue at \(1+a m_2+O(n^{3/2}2^{-n})\), while all others equal \(1+O(n^{3/2}2^{-n})\). Because \(a=-3n^2/2+O(n)\), the squared condition ratio is \(1+|a m_2|+O(n^{3/2}2^{-n})\). Substituting the exact paired or third \(m_2\) proves the two sharp leading constants. The conclusion of eventual strict superiority follows because the leading coefficients differ by a factor two.

## Verification

The standalone standard-library checker `verify.py` constructs the exact Gram matrix from every point of every residue class for all \(4\le n\le9\), then checks the four moment values, the three invariant actions, the pair-harmonic scalar, and the rank formula using finite-field elimination for 18 cases. It reports `QUADRATIC_MOD3_WALSH_VERIFY_PASS exact_spectrum_blocks_and_modular_rank 18`. The modular rank calculation is corroborative only: the infinite rank classification follows from the shell harmonic decomposition, not modular arithmetic or finite enumeration. Reproduce with `python3 verify.py`.

## Relationship to prior work

The harmonic-slice bases of Srinivasan and Filmus establish the general permutation-isotypic technology used in step three. Rao studies Fourier transforms of restrictions to a **single** slice, with a different principal objective. Cornelissen, Mande, Ozols, and de Wolf analyze exact **quantum query complexity** of weight modulo three, not the quadratic Fourier-restriction Gram spectrum. Existing results on a single Hamming shell calculate quadratic-band concentration sectors and even classify arithmetic eigenvalue collisions; they do **not** automatically supply the spectrum of a **union** of periodically separated shells, because the individual Gram operators have coupled multiplicity blocks. The present congruence-filter identities \(m_3=-3m_1\) and \(m_4=-3m_2\), exact 3-by-3/2-by-2 blocks, sharp injectivity cutoff, and paired-versus-third asymptotic are the stated specialization. The general Johnson/Terwilliger decomposition and the concept of restriction to symmetric Boolean sets are not claimed as new.

## Limitations

The theorem is specialized to sampling by weight modulo three at complete Walsh degree at most two. It makes no claim of optimality of the mask among all subsets of comparable cardinality, nor of a best finite dimension beyond which the paired classes outperform the third. The condition-ratio asymptotic is for \(n\to\infty\), while the exact eigenvalue matrices apply at each fixed \(n\). No external independent validation has been performed. The general algebraic decomposition is part of established literature, leaving possible residual priority risk from an unlocated published specialization to the exact periodic mask.

## References

1. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213v1, first posted 2021-11-05. https://arxiv.org/abs/2111.03213
2. A. Cornelissen, N. S. Mande, M. Ozols and R. de Wolf, *Exact quantum query complexity of computing Hamming weight modulo powers of two and three*, arXiv:2112.14682v1, first posted 2021-12-29. https://arxiv.org/abs/2112.14682
3. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, originally made public 2014, later revised. https://arxiv.org/abs/1406.0142
4. M. K. Srinivasan, *Symmetric chains, Gelfand–Tsetlin chains, and the Terwilliger algebra of the binary Hamming scheme*, arXiv:1001.0280, first posted 2010. https://arxiv.org/abs/1001.0280
5. *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, open mathematical record 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95
6. *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, open mathematical record 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90
