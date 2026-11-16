# Sharp two-erasure stability of near-Nyquist Chebyshev–Gauss cosine sampling

## Finding

Fix an integer \(N\ge4\) and the \(N\) Gauss–Chebyshev nodes \(x_j=\cos\theta_j\), where \(\theta_j=(j+\tfrac12)\pi/N\), \(0\le j<N\). Let \(\mathcal P_{N-3}\) be the polynomials of degree at most \(N-3\), equipped with the probability-normalized Chebyshev \(L^2\) norm. Evaluate at all \(N\) nodes using the normalized discrete-cosine quadrature, and erase any two distinct nodes \(x_j,x_k\). The surviving square analysis matrix \(A_{j,k}\) has dimension \(N-2\).

Every such matrix is invertible. Define \(s_i=\sin\theta_i\), \(c_i=\cos\theta_i\), and
\[
T_{j,k}=\frac2N\bigl[s_j^2(1+4c_j^2)+s_k^2(1+4c_k^2)\bigr],\qquad
D_{j,k}=\frac{16}{N^2}s_j^2s_k^2(c_j-c_k)^2.
\]
Then its squared singular values are \(1\), repeated \(N-4\) times, and exactly
\[
\lambda_{\pm}(j,k)=\frac{T_{j,k}\pm\sqrt{T_{j,k}^2-4D_{j,k}}}{2}.
\]
The smallest squared singular value over **all** two-erasure patterns is achieved **only** by \(\{j,k\}=\{0,1\}\) and \(\{j,k\}=\{N-2,N-1\}\). In particular, with \(t=\pi/(2N)\), put
\[
T_* =\frac2N\bigl[\sin^2t(1+4\cos^2t)+\sin^2(3t)(1+4\cos^2(3t))\bigr],\quad
D_* =\frac{16}{N^2}\sin^2t\sin^2(3t)(\cos t-\cos3t)^2.
\]
The sharp lower analysis-frame bound is \(\lambda_*(N)=(T_*-\sqrt{T_*^2-4D_*})/2\), satisfying
\[
\boxed{\lim_{N\to\infty}N^7\lambda_*(N)=\frac{9\pi^6}{25}.}
\]
For \(N\ge5\), every surviving sampling matrix has largest squared singular value \(1\). Thus the sharp **worst-case squared condition number** is \(1/\lambda_*(N)\), and
\[
\boxed{\lim_{N\to\infty}\frac{1}{N^7}\max_{j<k}\kappa(A_{j,k})=\frac{25}{9\pi^6},}
\]
where \(\kappa(A)\) is the ratio of the largest to the smallest squared singular values (not the ordinary matrix-norm condition number). The erasure patterns producing this worst conditioning are precisely the adjacent pairs at the two ends of the Gauss–Chebyshev grid.

## Assumptions and scope

Use \(\langle p,q\rangle=(1/\pi)\int_{-1}^{1}p(x)\overline{q(x)}(1-x^2)^{-1/2}\,dx\). An orthonormal polynomial basis is \(\phi_0(x)=1\) and \(\phi_r(x)=\sqrt2\,T_r(x)\) for integers \(1\le r\le N-3\), where \(T_r(\cos\theta)=\cos(r\theta)\). The analysis matrix is
\[
(A_{j,k})_{i,r}=N^{-1/2}\phi_r(x_i),\qquad i\notin\{j,k\},\quad0\le r\le N-3.
\]
The sampling energy is \(N^{-1}\sum_{i\notin\{j,k\}}|p(x_i)|^2\), while the coefficient energy equals \(\|p\|_{L^2}^2\). The theorem concerns exact nodes, uniform Gauss–Chebyshev weights, two missing observations and a matching loss of two polynomial degrees. It makes no claim about arbitrary node perturbations, higher erasure counts or noisy arithmetic.

## Proof

**1. Complementary cosine spectrum.** The complete \(N\times N\) normalized DCT-II matrix \(U\), with entries \(U_{i,0}=N^{-1/2}\) and \(U_{i,r}=\sqrt{2/N}\cos(r\theta_i)\) for \(1\le r<N\), is real orthogonal by discrete Chebyshev orthogonality. Partition its rows into the \(N-2\) observed rows and the two erased rows and its columns into degrees \(0,\ldots,N-3\) and the last two degrees. If \(B\) is the lower-right \(2\times2\) block, orthogonal-block identities show that the squared singular values of \(A_{j,k}\) consist of \(N-4\) unit values and the two eigenvalues of \(B^{\mathsf T}B\). Indeed, writing the bottom-left block as \(E\), one has \(A^{\mathsf T}A=I-E^{\mathsf T}E\) and \(BB^{\mathsf T}=I-EE^{\mathsf T}\); nonzero eigenvalues of \(E^{\mathsf T}E\) and \(EE^{\mathsf T}\) agree.

Since \(N\theta_i=(i+\tfrac12)\pi\), the two highest DCT entries satisfy \(\cos((N-2)\theta_i)=(-1)^i\sin2\theta_i\) and \(\cos((N-1)\theta_i)=(-1)^i\sin\theta_i\). Therefore
\[
B=\sqrt{2/N}\begin{pmatrix}(-1)^j\sin2\theta_j&(-1)^j\sin\theta_j\\(-1)^k\sin2\theta_k&(-1)^k\sin\theta_k\end{pmatrix}.
\]
Its squared Frobenius norm is \(T_{j,k}\), and its squared determinant is \(D_{j,k}\), proving the spectrum formula. Since \(\sin\theta_i>0\) and \(\cos\theta_i\) is strictly decreasing with \(i\), the determinant never vanishes. Hence both nonunit eigenvalues are strictly positive and \(A_{j,k}\) is invertible.

**2. A sharp global minimizer.** Write \(\lambda_-(j,k)\) for the smaller eigenvalue. From \(\lambda_-\lambda_+=D\) and \(\lambda_+\le\operatorname{tr}(B^{\mathsf T}B)=T\), and using \(1+4c_i^2\le5\), obtain
\[
\lambda_-(j,k)\ge\frac{D_{j,k}}{T_{j,k}}
\ge\frac{4}{5N}\min(s_j^2,s_k^2)(c_j-c_k)^2.\tag{1}
\]
Let \(t=\pi/(2N)\), \(d_1=\cos t-\cos3t\), and \(R=\sin3t/\sin t=3-4\sin^2t\). For any pair except \(\{0,1\}\) and \(\{N-2,N-1\}\), we claim
\[
\min(s_j^2,s_k^2)(c_j-c_k)^2\ge R^2\sin^2t\,d_1^2.\tag{2}
\]
If \(k-j=1\), both erased indices are interior, so \(\min(s_j,s_k)\ge\sin3t=R\sin t\). Also \(c_j-c_k=2\sin((\theta_j+\theta_k)/2)\sin(\pi/(2N))\ge d_1\), since the midpoint lies between the first and last adjacent-pair midpoints and sine takes its minimum at an endpoint. If \(k-j\ge2\), monotonicity of cosine and the same midpoint argument give \(c_j-c_k\ge c_j-c_{j+2}\ge\cos t-\cos5t=R d_1\); moreover \(\min(s_j,s_k)\ge\sin t\). This proves (2).

On the other hand, the larger eigenvalue of \(B^{\mathsf T}B\) for the pair \(\{0,1\}\) is at least the squared norm of its row at index \(1\), namely \((2/N)\sin^2(3t)(1+4\cos^2(3t))\). Consequently
\[
\lambda_*(N)\le\frac{D_*}{(2/N)\sin^2(3t)(1+4\cos^2(3t))}
=\frac{8}{N}\frac{\sin^2t\,d_1^2}{1+4\cos^2(3t)}.\tag{3}
\]
For \(N\ge5\), \(t\le\pi/10\), so \(R>5/2\) and \(\cos3t>1/2\). Combining (1)–(3), all nonboundary pairs satisfy
\[
\lambda_-(j,k)>\frac5N\sin^2t\,d_1^2
>\frac4N\sin^2t\,d_1^2>\lambda_*(N).
\]
The reflected end pair has the same spectrum, so these two are the only minimizers for \(N\ge5\). At \(N=4\), the exact minima for the six possible pairs are \((2-\sqrt{2+\sqrt2})/4\) for \(\{0,1\},\{2,3\}\); \((2-\sqrt{2-\sqrt2})/4\) for \(\{0,2\},\{1,3\}\); \((2-\sqrt2)/4\) for \(\{0,3\}\); and \(1/2\) for \(\{1,2\}\). The first value is strictly smallest, finishing the all-\(N\) classification.

**3. Sharp asymptotics and condition ratio.** As \(N\to\infty\), elementary Taylor expansions yield
\[
T_*=25\pi^2N^{-3}+O(N^{-5}),\qquad
D_*=9\pi^8N^{-10}+O(N^{-12}).
\]
Since \(D_*/T_*^2\to0\), the smaller root equals \(D_*/T_*\,(1+o(1))\), which proves the claimed \(9\pi^6/(25N^7)\) law. For \(N\ge5\), the \(N-4\) unit eigenvalues are present, and the other squared singular values do not exceed one because \(A\) is a submatrix of an orthogonal matrix. Hence the sharp worst-case squared condition ratio is exactly \(1/\lambda_*(N)\), completing the proof.

## Verification

The standalone numerical checker `check_dct.py` reconstructs every square sampled DCT matrix for \(4\le N\le20\), compares all eigenvalues and determinants against the formulas, and checks both minimizers. It also checks the exact two-row formula and minimizers for \(N=21,30,50,100,200\), and the asymptotic coefficient at larger dimensions. It passed 5,346 finite assertions. The proof of the infinite-dimensional quantifiers and the uniqueness of worst erasures is the analytical argument above; numerical calculations are consistency checks only.

To reproduce, install NumPy and run `python3 check_dct.py` alongside this document. The source uses only NumPy and Python's standard library. The coefficients and the theorem are real; the same squared singular values hold for complex polynomial coefficients.

## Relationship to prior work

Salomon and Ur (2011) use Gauss–Chebyshev nodes, the DCT-II and an iterative gap-filling procedure for analytic signals. They identify vulnerability of edge gaps qualitatively, but their inspected full text does not compute the sharp two-erasure singular spectrum, the unique minimizing pattern, or seventh-power condition law. Goren and Zamir (2021) study robustness of DCT-domain interpolation to irregular packet loss and redesign interpolators; their accessible abstract does not state the same extremal theorem, but the full article was inaccessible and remains a priority risk. Dirckx, Huybrechs and Ongenae (2022) analyze singular-value computation of contiguous submatrices of the *complex DFT*, rather than arbitrary two-row omissions from the near-complete *real cosine* transform; their full HTML text does not imply the current node-specific comparison. Published Chebyshev–Lobatto one-erasure results address a different grid and a supremum-norm Lebesgue constant, rather than two Gauss–Chebyshev erasures and an \(L^2\) singular value. The exact threshold and coefficient here therefore represent a distinct precise stability invariant, subject to the documented inaccessible-source risk.

## Limitations

This result treats a nearly complete cosine sampling system: exactly \(N-2\) retained frequencies and exactly two missing Gauss–Chebyshev nodes. No extrapolation is proved for a fixed low degree, higher erasure counts, perturbed nodes, floating-point inversion or non-Chebyshev weights. The condition ratio is squared singular-value conditioning, not the usual unsquared matrix condition. Historical priority remains provisional; in particular, the full 2021 DCT interpolation article could not be read through available lawful access.

## References

- M. Goren and R. Zamir, “Diversity Image Coding Using Irregular Interpolation,” *IEEE Transactions on Image Processing* 30 (2021), 5665–5677, DOI: 10.1109/TIP.2021.3087404. Article date verified as 2021-06-18 from PubMed PMID 34125679; accessible abstracts inspected, full text not retrieved.
- B. G. Salomon and H. Ur, “A Method for the Recovery of Gaps in General Analytic Signals,” *International Scholarly Research Notices* (2011), article 421502, DOI: 10.5402/2011/421502. Open full-text HTML inspected, especially Sections 2, 4–6.
- S. Dirckx, D. Huybrechs and R. Ongenae, “On the computation of the SVD of Fourier submatrices,” arXiv:2208.12583, first public 2022-08-26. Full arXiv HTML v1 inspected, especially Sections 1.1–1.2, 2.1–2.5 and 3.
- “Single-erasure boundary layers for Chebyshev–Lobatto interpolation,” public mathematical record dated 2026-10-18, GitHub published-finding corpus/2026, complete `RESULT.md` inspected. Later comparison only, treating one Lobatto deletion and uniform-norm interpolation rather than the theorem here.
