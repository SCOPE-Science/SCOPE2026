# Coherent-state tunneling and the sharp top spectral doublet of two distant Gaussian localization disks

## Finding
Fix an area \(R>0\). For each real separation \(d>2\sqrt{R/\pi}\), let \(E_{d,R}\subset\mathbb C\simeq\mathbb R^2\) be the union of the two closed disks of area \(R\), with centers \(w_\pm=\pm d/2\). In the standard Gaussian short-time Fourier localization problem, let \(L_{d,R}=V_\varphi^*\mathbf 1_{E_{d,R}}V_\varphi\), with normalized Gaussian \(\varphi(t)=2^{1/4}e^{-\pi t^2}\). List its eigenvalues nonincreasingly as \(\nu_1(d),\nu_2(d),\ldots\).

Put \(\ell_R=1-e^{-R}\), \(r_R=\sqrt{R/\pi}\), and \(s_d=e^{-\pi d^2/2}\). Then as \(d\to\infty\), with \(R\) fixed,

\[
\nu_1(d)=\ell_R(1+s_d)+O_R\!\left(e^{-\pi(d-r_R)^2}\right),\qquad
\nu_2(d)=\ell_R(1-s_d)+O_R\!\left(e^{-\pi(d-r_R)^2}\right).
\]

In particular, the two largest eigenvalues are eventually distinct and

\[
\lim_{d\to\infty}e^{\pi d^2/2}\big(\nu_1(d)-\nu_2(d)\big)=2(1-e^{-R}).
\]

Under the unitary Bargmann transform, the corresponding normalized eigenfunctions converge, up to individual phases, to the even and odd coherent-state combinations

\[
\Psi_{\pm,d}=\frac{K_{d/2}\pm K_{-d/2}}{\sqrt{2(1\pm s_d)}},\qquad
K_w(z)=e^{\pi z\overline w-\pi|w|^2/2},
\]

with errors \(O_R(e^{-\pi(d-r_R)^2/2})\) in Fock-space norm. The third eigenvalue satisfies the uniform far-separation gap bound

\[
\limsup_{d\to\infty}\nu_3(d)\le 1-(1+R)e^{-R}<\ell_R.
\]

The result identifies the *leading constant* of the exponential two-well splitting rather than merely the existence of almost-degenerate modes.

## Assumptions and scope
The Fock space is \(\mathcal F^2=\{F\text{ entire}:\int_{\mathbb C}|F(z)|^2e^{-\pi|z|^2}\,dz<\infty\}\), with its natural complex Hilbert-space norm. The Bargmann unitary conjugates Gaussian STFT localization to the positive Fock Toeplitz operator \(T_E\) whose quadratic form is \(\langle T_EF,F\rangle=\int_E|F(z)|^2e^{-\pi|z|^2}\,dz\). There is no semiclassical parameter: \(R\) is fixed and only the distance \(d\) tends to infinity. All spectral eigenvalues are counted with multiplicity. The disks have disjoint interiors for the stated range. The two centers lie on the real axis; Euclidean phase-space rotations and translations give unitarily equivalent versions, after adjusting coherent-state phases.

The index convention is \(\nu_1\ge\nu_2\ge\nu_3\ge0\). The error constants are allowed to depend on the *fixed* area \(R\), but not on \(d\). The theorem does not assert a uniform estimate when \(R\) grows with \(d\).

## Proof
**1. Single-disk spectrum and coherent overlap.** The normalized reproducing vectors satisfy \(\langle K_w,K_z\rangle=e^{\pi\overline w z-\pi(|z|^2+|w|^2)/2}\); consequently \(|\langle K_w,K_z\rangle|=e^{-\pi|w-z|^2/2}\). A disk \(D(w,R)\) of area \(R\), centered at \(w\), has the coherent vector \(K_w\) as its simple top eigenvector, with radial Hermite eigenvalues

\[
\ell_n(R)=\frac1{n!}\int_0^R e^{-t}t^n\,dt,\qquad n=0,1,\ldots.
\]

The top and next eigenvalues are \(\ell_0(R)=\ell_R\) and \(\ell_1(R)=1-(1+R)e^{-R}\). Their positive gap is \(g_R=Re^{-R}\). For the opposite disk centers, the coherent overlap is the positive real number \(s_d=\langle K_{d/2},K_{-d/2}\rangle=e^{-\pi d^2/2}\).

**2. Almost orthogonality of the nonleading sectors.** Write \(B_\pm=T_{D(w_\pm,R)}\) and \(P_\pm=|K_{w_\pm}\rangle\langle K_{w_\pm}|\). Since \(K_{w_\pm}\) is a single-disk eigenvector, the positive remainders \(H_\pm=B_\pm-\ell_R P_\pm\) satisfy \(0\le H_\pm\le B_\pm\) and \(\|H_\pm\|=\ell_1(R)\).

The coherent-state integral representation \(B_\pm=\int_{D(w_\pm,R)}|K_z\rangle\langle K_z|\,dz\) yields

\[
\operatorname{tr}(B_+B_-)=\int_{D(w_+,R)}\!\int_{D(w_-,R)}e^{-\pi|z-v|^2}\,dz\,dv
\le R^2e^{-\pi(d-2r_R)^2}.
\]

For positive trace-class operators, trace monotonicity gives \(\operatorname{tr}(H_+H_-)\le\operatorname{tr}(B_+B_-)\). The factorization \(H_++H_-=[H_+^{1/2},H_-^{1/2}][H_+^{1/2},H_-^{1/2}]^*\), combined with its two-by-two Gram operator, gives

\[
\|H_++H_-\|\le\ell_1(R)+\|H_+^{1/2}H_-^{1/2}\|
\le\ell_1(R)+R e^{-\pi(d-2r_R)^2/2}.
\]

This is the quantitative bound that prevents the excited states in the two disks from forming a spurious third leading level.

**3. Exact two-dimensional compression.** Let \(P\) be the orthogonal projector onto \(\operatorname{span}\{K_{w_+},K_{w_-}\}\), let \(Q=I-P\), and put \(A=B_++B_-\). Reflection \(z\mapsto-z\) interchanges the disks and their coherent vectors, so the even and odd unit vectors \(\Psi_{\pm,d}\) diagonalize \(PAP\). Define the opposite-disk leakage

\[
q_d=\langle K_{w_+},B_-K_{w_+}\rangle
=\int_{D(w_-,R)}e^{-\pi|z-w_+|^2}\,dz
\le R e^{-\pi(d-r_R)^2}.
\]

The diagonal matrix elements in the coherent basis are \(\ell_R+q_d\). Because \(B_\pm K_{w_\pm}=\ell_R K_{w_\pm}\), its cross element is exactly \(2\ell_Rs_d\). Taking account of the nonorthogonal basis, the two eigenvalues of the **orthogonal** compression are therefore

\[
\mu_+(d)=\frac{\ell_R+q_d+2\ell_R s_d}{1+s_d},\qquad
\mu_-(d)=\frac{\ell_R+q_d-2\ell_R s_d}{1-s_d}.
\]

In particular \(\mu_\pm=\ell_R\pm\ell_Rs_d+O_R(q_d+s_d^2)\). Since \(q_d/s_d\to0\), this is an asymptotically resolved doublet.

**4. Coupling to the orthogonal complement.** Because \(QK_{w_\pm}=0\), the residual \(QA K_{w_+}\) is \(QB_-K_{w_+}\), and similarly after interchanging the signs. Positivity and \(B_\pm\le I\) imply \(\|B_-K_{w_+}\|^2\le\langle K_{w_+},B_-K_{w_+}\rangle=q_d\). The Gram matrix of the two coherent vectors has smallest eigenvalue \(1-s_d\), so

\[
\|QAP\|^2\le \frac{2q_d}{1-s_d}.
\]

By step 2, \(\|QAQ\|\le\ell_1(R)+R e^{-\pi(d-2r_R)^2/2}\), which is below \(\min\{\mu_+,\mu_-\}\) by at least \(g_R/2\) for sufficiently large \(d\).

Here is the elementary block spectral estimate being used. If a positive compact selfadjoint operator is decomposed over a rank-two projection and its orthogonal complement, its diagonal blocks are \(M\) and \(C\), and \(\mu_2(M)>\|C\|\), then the top two eigenvalues \(\nu_j\) satisfy

\[
0\le\nu_j-\mu_j(M)\le\frac{\|QAP\|^2}{\mu_2(M)-\|C\|},\qquad j=1,2.
\]

Indeed, for \(\nu>\|C\|\), eliminating the complement from the eigenvector equation gives the Schur complement \(M+(QAP)^*(\nu-C)^{-1}(QAP)\). Its ordered eigenvalue functions are nonincreasing in \(\nu\), and its positive correction is bounded by \(\|QAP\|^2/(\nu-\|C\|)\). The min-max principle places the two desired eigenvalues above \(\mu_2(M)\) and the third no higher than \(\|C\|\), proving the asserted indexwise bounds.

It follows that \(\nu_{1,2}(d)=\mu_{\pm}(d)+O_R(q_d)\), and hence

\[
\nu_{1,2}(d)=\ell_R\big(1\pm s_d\big)+O_R\big(e^{-\pi(d-r_R)^2}\big).
\]

The main term dominates this remainder because \(e^{-\pi(d-r_R)^2}/s_d\to0\). The third eigenvalue is bounded above by \(\|QAQ\|\), by the codimension-two min-max principle. Finally, for a normalized top-doublet eigenvector \(F=p+q\) with \(p\in P\mathcal F^2\), \(q\in Q\mathcal F^2\), the complementary equation gives \(\|q\|\le \|QAP\|/(\nu-\|QAQ\|)=O_R(\sqrt{q_d})\). Reflection parity forces \(p\) to be along the corresponding \(\Psi_{\pm,d}\), establishing the stated eigenfunction approximation and completing the proof.

## Verification
The standalone program `check_double_disk.py` independently constructs the finite Bargmann–Fock matrix of the two-disk Toeplitz operator by Gaussian radial quadrature and angular sampling. It checks the two top eigenvalues, the even/odd coherent eigenvectors, the opposite-disk leakage inequality, the third-eigenvalue separation, and convergence of the normalized splitting for areas \(0.45\) and \(1.10\) and separations \(2.10,2.60,3.10\). The program reports `DOUBLE_DISK_CHECKS_PASS 56` when all 56 asserted conditions pass. The analytic argument in the preceding section, not the finite matrix computations, proves the infinite-dimensional statement.

Run with `python check_double_disk.py` using Python 3, NumPy, and SciPy. The numerical matrix truncation is \(64\) monomial degrees; verification has finite precision and does not certify exact infinite-dimensional eigenvalues. The leakage bound, gap estimate, and Schur complement are established analytically.

## Relationship to prior work
The Gaussian Faber–Krahn theorem of Nicola and Tilli establishes the optimal *one-disk* concentration norm and identifies coherent-state optimizers; their 2022 norm paper establishes general sharp bounds for weighted localization. The single-disk Hermite spectrum derives from the classical Daubechies radial diagonalization. The 2024 quantitative stability paper of Gómez, Guerra, Ramos, and Tilli controls near-optimality relative to disks, rather than the exponentially split leading doublet of two equally sized disks. Huang and Zhang give a global bound for general nonradial Fock Toeplitz symbols, not an asymptotic formula for their two leading eigenvalues.

The contribution claimed here is specifically the sharp coefficient \(2(1-e^{-R})\) in the exponential splitting, the parity-resolved coherent combinations, and the quantitative isolation of the doublet for fixed-area distant disks. It is *not* the one-disk diagonalization, Faber–Krahn inequality, Gaussian reproducing formula, or a general statement that separated positive operators become nearly orthogonal.

## Limitations
This is a fixed-area large-separation theorem. It does not treat growing areas, unequal disks, more than two components, higher dimensions, or all lower eigenvalue clusters. The error bound is not claimed optimal. The existence of related general anti-Wick double-well perturbation results under other terminology is a residual historical-priority risk; the present theorem is a mathematics claim subject to independent review, not independently certified.

## References
1. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624, first posted 2022-07-18. https://arxiv.org/abs/2207.08624
2. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423, first posted 2021-06-07; Invent. Math. 230 (2022), 1–30. https://arxiv.org/abs/2106.03423
3. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, Invent. Math. 236 (2024), 779–836. https://link.springer.com/article/10.1007/s00222-024-01248-2
4. Y. C. Huang and J.-Y. Zhang, *Norm bounds for self-adjoint Toeplitz operators with non-radial symbols on the Fock space*, arXiv:2405.11147, 2024-05-18. https://arxiv.org/html/2405.11147v1
5. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Trans. Inform. Theory 34 (1988), 605–612.
