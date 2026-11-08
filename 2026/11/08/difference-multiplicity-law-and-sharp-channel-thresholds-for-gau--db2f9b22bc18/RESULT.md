# Difference-multiplicity law and sharp channel thresholds for Gaussian-bin Fourier intensity tomography

## Finding
Let \(S=\{\nu_1<\cdots<\nu_n\}\subset\mathbb Z\) contain \(n\ge2\) frequencies, let \(\tau>0\), and choose \(r\ge1\) distinct real filter centers \(b_1,\ldots,b_r\). Define \(w_{jk}=\exp[-\tau(\nu_k-b_j)^2]\). For each Hermitian matrix \(H\in\operatorname{Herm}(n)\), observe the complete periodic real intensity profile
\[
(\mathcal L H)_j(t)=\sum_{k,l=1}^n H_{kl}w_{jk}w_{jl}\exp\big(i(\nu_k-\nu_l)t\big),\qquad 0\le t<2\pi.
\]
This is the linear extension of the filtered squared magnitude \(\left|\sum_k c_kw_{jk}e^{i\nu_kt}\right|^2\), with \(H_{kl}=c_k\overline{c_l}\). For each positive difference \(d\), write \(m_d=\#\{(k,l):\nu_k-\nu_l=d\}\). The exact real rank and nullity, **for every choice of distinct filter centers**, are
\[
\boxed{\operatorname{rank}_{\mathbb R}\mathcal L=\min(n,r)+2\sum_{d>0}\min(r,m_d),\quad
\dim_{\mathbb R}\ker\mathcal L=(n-r)_++2\sum_{d>0}(m_d-r)_+.}
\]
The positive singular values (Hilbert--Schmidt norm on Hermitian matrices and normalized \(L^2\) norm on each output circle) are exactly the singular values of the real matrix \(W_0\), each once, together with those of \(W_d\), each twice for each \(d>0\), where
\[
W_d[j,(k,l)]=\exp[-\tau((\nu_k-b_j)^2+(\nu_l-b_j)^2)],\quad \nu_k-\nu_l=d.
\]
Only nonzero singular values are counted in this description. For fixed \(n,r\), the sharp maximum over frequency sets is
\[
\boxed{\max_{|S|=n}\operatorname{rank}_{\mathbb R}\mathcal L=n^2-(n-r)_+,}
\]
with equality **if and only if** every positive frequency difference occurs at most \(r\) times. All such optima exist: a geometric (unique-difference) spectrum achieves equality for every \(r\). For the consecutive spectrum the exact rank is \(m(2n-m)\), where \(m=\min(r,n)\), and the nullity is \((n-r)_+^2\).

The same data recover **every** Hermitian matrix exactly if and only if \(r\ge n\). On the affine space of **trace-one** Hermitian matrices (hence also on density matrices), \(r\le n-2\) never suffices. At the sharp intermediate channel count \(r=n-1\), injectivity holds precisely when
\[
\det\begin{pmatrix}W_0\\ \mathbf1^{\mathsf T}\end{pmatrix}\ne0.
\]
This holds for almost every choice of pairwise-distinct real filter centers, but not for all. For example, when \(S=\{-1,0,1\}\) and the two centers are \(\pm b\) with \(b>0\), trace-one recovery fails **exactly** when \(\cosh(4\tau b)=e^{2\tau}\).

## Assumptions and scope
The integer frequencies are distinct but need not be consecutive or symmetric; amplitudes and Hermitian matrices are complex-valued, while \(\tau\) is any fixed positive real number and the centers are arbitrary distinct real numbers. Time is continuous over one full circle. The real domain has dimension \(n^2\), with \(\lVert H\rVert_{\mathrm{HS}}^2=\operatorname{tr}(H^2)\), and the output norm is \(\sum_{j=1}^r\frac1{2\pi}\int_0^{2\pi}|(\mathcal L H)_j(t)|^2dt\). No positivity assumption is used in the rank/spectrum statements. The trace-one consequence applies in particular to all positive semidefinite density matrices, not merely rank-one states.

## Proof
**Fourier blocks.** Orthogonality of the exponentials gives, for every difference \(d\in S-S\), the output Fourier coefficient
\[
\widehat{(\mathcal L H)}_j(d)=\sum_{(k,l):\nu_k-\nu_l=d} H_{kl}W_d[j,(k,l)].
\]
The coefficients for negative differences are complex conjugates. The diagonal \(d=0\) sector is a real \(n\)-dimensional space; each \(d>0\) sector is a complex \(m_d\)-dimensional space (real dimension \(2m_d\)). All sectors are Hilbert--Schmidt orthogonal, as are their output Fourier sectors. For the off-diagonal sector, the normalized real and imaginary Hilbert--Schmidt basis elements have entries of magnitude \(1/\sqrt2\), and the corresponding real sine/cosine output basis has \(L^2\) norm \(1\) after its \(\sqrt2\) normalization. Consequently the two real blocks are each exactly \(W_d\), with no additional singular-value factor. This proves the stated singular-value decomposition as soon as each \(W_d\) has full possible rank.

**Strict generalized Vandermonde rank.** For \(d\ge0\), let \(E_d=\{(k,l):\nu_k-\nu_l=d\}\), with diagonal pairs at \(d=0\). Setting \(z_j=e^{4\tau b_j}\) and \(h_{kl}=H_{kl}e^{-\tau(\nu_k^2+\nu_l^2)}\), direct completion of squares yields
\[
\widehat{(\mathcal LH)}_j(d)=e^{2\tau b_jd-2\tau b_j^2}\sum_{(k,l)\in E_d}h_{kl}z_j^{\nu_l}.
\]
The exponents \(\nu_l\) are distinct inside each \(E_d\), and the \(z_j\)'s are positive and distinct. A real nonzero linear combination of \(m\) distinct real monomials has at most \(m-1\) distinct positive zeros: multiply by a positive monomial to make the smallest exponent zero, differentiate, and apply Rolle's theorem inductively to the remaining \(m-1\) monomials. Hence any square generalized Vandermonde submatrix at \(m\) distinct positive nodes is nonsingular. Applied to the first \(\min(r,m_d)\) nodes and exponent columns, this gives \(\operatorname{rank}W_d=\min(r,m_d)\). Complex coefficient equations split into two identical real systems. Adding the blocks proves the rank/nullity identities.

**Kernel as sparse-polynomial interpolation.** The preceding identity shows that a Hermitian matrix belongs to the kernel exactly when the real Laurent polynomial
\[
P_0(z)=\sum_k H_{kk}e^{-2\tau\nu_k^2}z^{\nu_k}
\]
and, for every positive difference \(d\), the complex Laurent polynomial
\[
P_d(z)=\sum_{(k,l)\in E_d}H_{kl}e^{-\tau(\nu_k^2+\nu_l^2)}z^{\nu_l}
\]
vanish at each \(z_1,\ldots,z_r\). Multiplying by a suitable power of \(z\) converts any Laurent polynomial to an ordinary polynomial and does not change its positive roots. The resulting independent interpolation conditions specify the **entire** kernel; no nonlinear or hidden constraints are imposed.

**Optimal spectrum and consecutive frequencies.** As \(\sum_{d>0}m_d=n(n-1)/2\), the rank formula implies \(\operatorname{rank}\mathcal L\le\min(r,n)+n(n-1)\). Equality holds exactly if \(m_d\le r\) for all \(d>0\). The frequencies \(S=\{1,2,4,\ldots,2^{n-1}\}\) have unique positive differences: if \(2^a-2^b=2^c-2^e>0\) with \(a>b\) and \(c>e\), the exact power of two dividing each side gives \(b=e\), then \(a=c\). Thus equality is attainable for every parameter pair. For the consecutive set, \(m_d=n-d\) for \(1\le d<n\); summation of \(\min(r,n-d)\) yields \(\min(r,n)(2n-\min(r,n))\) and square nullity \((n-r)_+^2\).

**Trace-one threshold and exceptional centers.** If \(r<n\), the diagonal kernel is nonzero and if \(r\le n-2\), its dimension is at least two; its intersection with the trace-zero hyperplane therefore contains a nonzero matrix \(K\). For sufficiently small \(\varepsilon>0\), both \(I/n+\varepsilon K\) and \(I/n-\varepsilon K\) are distinct positive density matrices with identical profiles. If \(r=n-1\), each off-diagonal block has full column rank, since \(m_d\le n-1\). The sole unconstrained direction is diagonal, and trace-one uniqueness is equivalent to the determinant condition. It is not identically zero as a function of the distinct centers: choose \(n\) distinct centers whose \(n\) positive generalized-Vandermonde rows span \(\mathbb R^n\), express \(\mathbf1^{\mathsf T}\) in that basis, and remove one row with a nonzero coefficient. The remaining \(n-1\) rows together with \(\mathbf1^{\mathsf T}\) are independent. The determinant is real analytic, so its zero locus has Lebesgue measure zero. For \(S=\{-1,0,1\}\) and centers \(\pm b\), the two diagonal rows are independent for \(b>0\). The trace row lies in their span exactly when their sum, proportional to \((e^{-2\tau}\cosh(4\tau b),1,e^{-2\tau}\cosh(4\tau b))\), is constant, giving \(\cosh(4\tau b)=e^{2\tau}\), as claimed. If \(r\ge n\), all blocks have full column rank and complete Hermitian recovery follows.

## Verification
The accompanying standalone `CHECK.py` constructs the original untransformed real Hermitian lifting matrix from sampled intensity profiles and independently computes its singular values. It compares those singular values with the predicted Fourier-block matrices, checks generalized Vandermonde ranks and interpolation nullspaces with exact integer arithmetic, checks the sharp rank/optimality laws across several frequency families, and tests the trace-one threshold and explicit exceptional-center equation. Use `python -m pip install -r requirements.txt` and then `python CHECK.py`; expected output includes `PASS including trace-one checks: 2656 assertions`. For each given finite frequency set, the entire profile is also recovered exactly from \(2(\max S-\min S)+1\) equally spaced time samples by discrete Fourier interpolation. Finite computations corroborate the algebra but do not replace the all-size proof.

## Relationship to prior work
Liu, Ning, Wu and Zhang (2026), Theorem 3.1 and its Gaussian-convolution reduction, prove **rank-one signal phase uniqueness** with two well-chosen frequency-bin channels for a bandlimited setting. Wellershoff (2022), Theorem 5, proves a related two-bin uniqueness result for bandlimited Gabor phase retrieval; Chen, Lu, Sun and Zhao (2026), Theorem 4.1, treat periodic signals with two STFT windows. These address nonlinear identification of pure signals, not injectivity of linear intensity measurements on **all Hermitian matrices**, and therefore do not imply the rank/nullity formula here. The distinction is essential: two channels can identify pure signals while leaving a large linear kernel of mixed-state directions. An earlier narrow three-tone calculation of two-filter lifting and standard generalized-Vandermonde facts overlap special techniques, not the sharp all-spectra difference-multiplicity classification and trace-one threshold. No priority is claimed for generalized Vandermonde interpolation itself.

## Limitations
The main result is exact and deterministic for finite integer frequency sets and continuously observed periodic time profiles; it does not establish noise-robust recovery rates, stability under approximately known bins, general non-Gaussian filters, or global phase retrieval for every rank-one signal. The rank-maximizing powers-of-two frequencies use potentially large bandwidth. The exceptional set for trace-one recovery is characterized by an explicit determinant, not enumerated in general. Reproduction checks cover finite examples only. Independent mathematical and publication-priority review has not been performed.

## References
1. B. Liu, M. Ning, L. Wu, Q. Zhang, *Phase Retrieval of Bandlimited Signals Using a Morlet Wavelet and an Admissible Companion*, arXiv:2610.39145v1 (first public 2026-10-29), https://arxiv.org/html/2610.39145v1 .
2. M. Wellershoff, *Sampling at twice the Nyquist rate in two frequency bins guarantees uniqueness in Gabor phase retrieval*, arXiv:2206.03946 (first public 2022-06-08), https://arxiv.org/abs/2206.03946 .
3. T. Chen, H. Lu, W. Sun, Y. Zhao, *STFT Phase Retrieval with Two Window Functions*, arXiv:2602.05210v1 (first public 2026-02-05), https://arxiv.org/html/2602.05210v1 .
