# Exact additive-Fourier Hamming-band spectra on finite-field multiplicative varieties

## Finding

Let \(q\) be any prime power, \(d\ge2\), and \(j\in\mathbb F_q^\times\). Put \(Q=q-1\) and
\[
H_j=\{x\in(\mathbb F_q^\times)^d:\prod_{i=1}^d x_i=j\},\qquad |H_j|=Q^{d-1}.
\]
Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). For \(0\le s\le d\), let \(M_s\) be the matrix with rows indexed by \(x\in H_j\), columns indexed by frequency vectors \(a\in\mathbb F_q^d\) having exactly \(s\) nonzero coordinates, and entries \((M_s)_{x,a}=\psi(a\cdot x)\). Write \(B_k=[M_0\;M_1\;\cdots\;M_k]\) for \(0\le k\le d\). All matrices here are **unnormalized**; the relevant squared singular values are the eigenvalues of their row Gram operators.

Let \(\Gamma=\widehat{\mathbb F_q^\times}\), a cyclic group of order \(Q\). The characters of \(H_1\) are indexed by the quotient \(\Gamma^d/\Delta\), where \(\Delta=\{(\gamma,\ldots,\gamma):\gamma\in\Gamma\}\). For one class \([e]\) and representative \(e=(e_1,\ldots,e_d)\), set \(m_\gamma=|\{i:e_i=\gamma\}|\). Define the polynomial
\[
\boxed{F_{[e]}(z)=\frac1Q\sum_{\gamma\in\Gamma}
(qz)^{d-m_\gamma}(Q+z)^{m_\gamma}.}
\]
This polynomial is independent of the representative and has nonnegative integer coefficients. **The complete squared-singular-value spectra, including all multiplicities,** are
\[
\boxed{\operatorname{Spec}(M_sM_s^*)=\{[z^s]F_{[e]}(z):[e]\in\Gamma^d/\Delta\},}
\]
\[
\boxed{\operatorname{Spec}(B_kB_k^*)=\{\sum_{s=0}^k[z^s]F_{[e]}(z):[e]\in\Gamma^d/\Delta\}.}
\]
Each character class contributes one eigenvalue; equal levels are combined. The associated eigenvectors are multiplicative characters of the torsor \(H_j\). Thus the spectrum, rank and sharp frame bounds are independent of \(j\) and of the choice of nontrivial \(\psi\). For a value \(v\), the exact multiplicity can also be computed as
\[
\frac1Q\sum_{\substack{m_1+\cdots+m_Q=d\\m_i\ge0}}
\frac{d!}{\prod_i m_i!}\,\mathbf1_{\{\lambda(m_1,\ldots,m_Q)=v\}},
\]
where \(\lambda\) is the corresponding displayed eigenvalue formula.

An exact-weight shell of additive frequencies has **the same restricted span and rank** as the entire frequency band up to that weight. For \(0\le s\le d\),
\[
\boxed{\operatorname{rank}M_s=\operatorname{rank}B_s
=Q^{d-1}-\frac{d!}{Q}[z^d]\left(\sum_{\ell=0}^{d-s-1}\frac{z^\ell}{\ell!}\right)^Q,}
\]
where an empty sum is zero. In particular, either family spans all functions on \(H_j\) precisely when
\[
\boxed{s\ge d-\left\lceil d/Q\right\rceil.}
\]
The rank threshold itself follows from the classical diagonal-annihilator/occupancy framework; the asserted spectral contribution is the **additive**, rather than multiplicative-character, weighted all-degree law above.

There is a sharp closed stability formula at the last proper band, \(k=d-1\). When \(q\ge3\), write \(d=Qa+b\), \(0\le b<Q\). Then
\[
\boxed{\lambda_{\min}(B_{d-1}B_{d-1}^*)=\frac{q^d-1}{Q},\qquad
\lambda_{\max}(B_{d-1}B_{d-1}^*)
=q^d-\frac{bq^{d-a-1}+(Q-b)q^{d-a}}{Q}.}
\]
The least eigenvalue is simple, attained only by the trivial multiplicative character. The greatest eigenvalue has multiplicity
\[
\boxed{\frac1Q\binom Qb\frac{d!}{((a+1)!)^b(a!)^{Q-b}},}
\]
and corresponds exactly to character classes with optimally balanced occupancies. Consequently the sharp spectral condition number of \(B_{d-1}\) is the square root of the ratio of these two bounds, strictly greater than one for \(q\ge3\) and \(d\ge2\). In the degenerate field \(q=2\), \(H_j\) is a singleton and the sole squared singular value of this band is \(2^d-1\).

## Assumptions and scope

Finite fields of **all characteristics and extension degrees** are included; \(d\ge2\), \(j\ne0\), and the observation set contains every point of \(H_j\). The support of an additive frequency is its number of nonzero coordinate entries. No a priori assumption that the Fourier column family is independent is made. Eigenvalues are counted on the row domain \(\mathbb C^{H_j}\); additional zero singular values on the column domain are not listed. Dividing every matrix entry by \(|H_j|^{1/2}\) divides each displayed Gram eigenvalue by \(|H_j|\) and does not change condition numbers. For any \(s\) or \(k\), a zero spectral level means the observation map is not surjective; the positive levels still give the exact sharp bounds on its range.

## Proof

**1. Generating the additive-frequency Gram kernels.** For any \(x,y\in H_j\), additive-character orthogonality gives
\[
\sum_{u\in\mathbb F_q^\times}\psi(u(x_i-y_i))
=q\mathbf1_{\{x_i=y_i\}}-1.
\]
Therefore the polynomial-valued kernel
\[
\mathcal K_z(x,y)=\prod_{i=1}^d\left(1+z(q\mathbf1_{\{x_i=y_i\}}-1)\right)
=\sum_{s=0}^d z^s(M_sM_s^*)_{x,y}.
\]
Its coefficient sum through degree \(k\) is the Gram kernel of \(B_k\). Because the coordinate equality indicators depend only on \(x_i/y_i\), every coefficient kernel is convolution on the multiplicative torsor \(H_j\) for the group \(H_1\). Thus **all** Gram kernels are simultaneously diagonalized by the multiplicative characters of \(H_1\).

**2. Exact diagonalization.** Choose a base point \(x^{(0)}\in H_j\), identifying \(H_j=x^{(0)}H_1\). The annihilator of \(H_1\) in \(\Gamma^d\) is exactly the diagonal \(\Delta\). For a representative \(e\) of \([e]\), evaluate the Fourier multiplier of \(\mathcal K_z\) on \(H_1\). Insert multiplicative-character orthogonality
\[
\mathbf1_{\{\prod t_i=1\}}=\frac1Q\sum_{\gamma\in\Gamma}\gamma\left(\prod_i t_i\right).
\]
For any character \(\eta\) of \(\mathbb F_q^\times\), the local sum is
\[
\sum_{t\in\mathbb F_q^\times}\eta(t)\bigl(1+z(q\mathbf1_{\{t=1\}}-1)\bigr)
=Q(1-z)\mathbf1_{\{\eta=1\}}+qz.
\]
Thus when the diagonal shift is \(\gamma\), exactly \(m_\gamma\) local characters become trivial. Multiplying the local factors yields
\[
\frac1Q\sum_{\gamma\in\Gamma}(qz)^{d-m_\gamma}
\bigl(Q(1-z)+qz\bigr)^{m_\gamma}=F_{[e]}(z),
\]
since \(Q=q-1\). Coefficient comparison proves both spectral formulas and the character-eigenvector assertion. Each character class of \(H_1\) occurs exactly once. The nonnegative-integer coefficient assertion also follows directly because \(M_sM_s^*\) has integer character multipliers from this expression: \(\Gamma^d\) words form free diagonal-shift orbits, and the numerator is invariant under that shift. More explicitly, the Fourier eigenvalues are algebraic integers by the integral kernel, and rational numbers by the formula, hence integers; their coefficients are visibly nonnegative.

**3. Exact rank and shell–band span equality.** Each summand of \(F_{[e]}\) has nonzero coefficients exactly in degrees \(d-m_\gamma,\ldots,d\), since \(q,Q>0\). Hence both \([z^s]F_{[e]}\) and \(\sum_{t=0}^s[z^t]F_{[e]}\) are positive exactly when \(\max_\gamma m_\gamma\ge d-s\). The corresponding column spans on \(H_j\) are \(H_1\)-invariant and are therefore sums of their positive character eigenspaces. Their identical positive-character supports show that the two spans coincide, not merely their dimensions. The number of all character classes is \(Q^{d-1}\). Character words of length \(d\) whose every occupancy is at most \(d-s-1\) are counted by
\[
d![z^d]\left(\sum_{\ell=0}^{d-s-1}z^\ell/\ell!\right)^Q.
\]
Every diagonal-shift orbit has \(Q\) words, so dividing by \(Q\) gives precisely the missing character classes and the rank formula. The smallest possible maximum occupancy among \(Q\) symbols in \(d\) slots is \(\lceil d/Q\rceil\), attained by balanced occupancies, proving the sharp full-row-rank threshold.

**4. Sharp final-band conditioning and all equality modes.** Summing all exact-weight Gram kernels gives the complete additive Fourier Gram \(q^d I\). The top polynomial coefficient from step 2 is
\[
[z^d]F_{[e]}(z)=\frac1Q\sum_{\gamma\in\Gamma}q^{d-m_\gamma}.
\]
Therefore \(\lambda_{[e]}(B_{d-1}B_{d-1}^*)=q^d-Q^{-1}\sum_\gamma q^{d-m_\gamma}\). With \(\sum_\gamma m_\gamma=d\), strict convexity of \(m\mapsto q^{-m}\) makes the sum largest at \((d,0,\ldots,0)\) and smallest exactly at the balanced occupancy vectors with \(b\) entries \(a+1\) and the other \(Q-b\) entries \(a\). Substitution proves both sharp eigenvalues. The concentrated word is a single diagonal-shift orbit, so the least eigenvalue is simple. Counting balanced words and dividing by their free orbit size \(Q\) gives the maximum-eigenvalue multiplicity above. All other eigenvalues lie between the two by the same strict convexity argument. When \(Q=1\), the single character mode is immediate.

## Verification

The standalone `check.py` generates direct additive Fourier matrices, then diagonalizes their complex Hermitian row Grams independently of the symbolic character calculation. It checks both **exact Hamming shells** and **cumulative bands** for all degrees on prime fields of orders \(2,3,5,7\) and the quadratic extension field \(\mathbb F_4\); it also compares nontrivial product cosets, rank thresholds, sharp last-band endpoints, and endpoint multiplicities. The recorded replay succeeded for **148 direct spectra and 6 nontrivial-coset comparisons**, with maximum absolute eigenvalue discrepancy \(1.933\times10^{-12}\). Execute `python check.py` from the package directory after installing NumPy as described in `requirements.txt`. These finite tests corroborate the formulas; the preceding character-orthogonality proof establishes them for all fields and dimensions.

For example, at \((q,d,k)=(5,4,3)\), the unnormalized last-band squared singular levels are \(156,280,300,400,500\); the least is simple, and the greatest has multiplicity \(6\). For the same field and dimension, the weight-two shell and the degree-two band both have rank \(58<64\).

## Relationship to prior work

Fraser and Rakhmonov study exactly the underlying multiplicative variety \(H_j\) and prove finite-field restriction results and Fourier decay statements, including a character-sum formula in their Section 5.2. They do **not** state a complete sparse additive-frequency sampling spectrum, shell–band spectral law, or sharp last-band condition number. Classical multiplicative-character orthogonality is an ingredient of the proof, not itself claimed as new.

A published result titled *Exact alias spectra and the binary Nyquist boundary for parity-check Fourier sampling* treats **multiplicative Fourier-character** bands on a checksum subgroup, with integer occupancy-block singular values. Applied to the multiplicative group \(\mathbb F_q^\times\), it already yields the rank/occupancy threshold for character-band sampling and provides a direct structural comparison. The present additive-character system has a different local Gram kernel, its actual spectral eigenvalues are given by \(F_{[e]}\), and its sharp last-band conditioning is not supplied by that result. Its rank-threshold consequence is **not claimed as independently novel**. Published spectra for fixed-weight **Hamming observation shells** concern a different observation set, not the multiplicative product-one variety. The exact all-degree additive spectrum and final-band eigenvalue extrema are the claimed contribution.

## Limitations

The result assumes the complete product-one multiplicative variety with nonzero product, and complete shells or balls of additive frequencies. It does not address arbitrary missing observation points, irregular frequency masks, Fourier \(L^p\) extension exponents, or nonlinear reconstruction. Counting-norm choices change the numerical eigenvalues but not the condition numbers. The self-review and targeted priority searches do not establish historical uniqueness: a general weighted harmonic-analysis identity may already imply this specialization under another terminology. Independent mathematical audit has not been performed.

## References

- J. M. Fraser and F. Rakhmonov, *An improved \(L^2\) restriction theorem in finite fields*, arXiv:2505.09293, first publicly posted 2025-05-14, https://arxiv.org/abs/2505.09293. Relevant full text: Section 5.2, Lemma 5.3 and Corollary 5.5, https://pure.st-andrews.ac.uk/ws/portalfiles/portal/336282202/Fraser_2026_PAMS_Improved-L2-restriction-finite-fields_AAM_CCBY.pdf.
- *Exact alias spectra and the binary Nyquist boundary for parity-check Fourier sampling*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-alias-spectra-and-the-binary-nyquist-boundary-for-parity-c--75b261de521c.
- *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.
- *Exact Poisson-binomial conditioning for heterogeneous Fourier sampling on coordinate hyperplanes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-poisson-binomial-conditioning-for-heterogeneous-fourier-sa--b286e6b4e2c8.
