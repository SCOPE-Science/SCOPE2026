# Exact positive-semidefinite fibers of two-circle quadratic intensity samples

## Finding
Fix real radii \(0<r<s\) and five angles \(\theta_m=2\pi m/5\), where \(m=0,\ldots,4\). For \(\rho>0\), define
\[
w_\rho(\theta)=(1,\rho e^{-i\theta},\rho^2 e^{-2i\theta})^T,
\qquad \mathcal M_{r,s}(H)=\big(w_\rho(\theta_m)^*H w_\rho(\theta_m)\big)_{\rho\in\{r,s\},\ 0\le m<5}
\]
on the real vector space \(\operatorname{Herm}(3)\) of complex Hermitian matrices. Then
\[
\ker\mathcal M_{r,s}=\mathbb R K_{r,s},\quad
K_{r,s}=\operatorname{diag}\big(r^2s^2,-(r^2+s^2),1\big).
\]
Consequently, for every \(q=(q_0,q_1,q_2)^T\in\mathbb C^3\), the **complete positive-semidefinite measurement fiber** over \(P=qq^*\) is
\[
\{H\succeq0:\mathcal M_{r,s}(H)=\mathcal M_{r,s}(P)\}
=\{P+tK_{r,s}:0\le t\le\max(0,\tau_{r,s}(q))\},
\]
where
\[
\tau_{r,s}(q)=\frac{|q_1|^2}{r^2+s^2}
-\frac{|q_0|^2}{r^2s^2}-|q_2|^2.
\]
The fiber is nontrivial precisely when \(\tau_{r,s}(q)>0\). In that case its interior members have rank three and its nonzero endpoint has rank two; \(P\) has rank one. Regardless of \(q\), two-circle measurements uniquely identify \(P\) among **rank-one** positive-semidefinite matrices, so ordinary vector phase retrieval holds.

At any third radius \(u>0\) with \(u\notin\{r,s\}\), one further sample at **any** angle \(\varphi\) yields an injective real-linear measurement map on all of \(\operatorname{Herm}(3)\), because
\[
w_u(\varphi)^*K_{r,s}w_u(\varphi)
=(u^2-r^2)(u^2-s^2)\ne0.
\]
Exactly one extra scalar sample is necessary and sufficient to achieve injectivity on arbitrary Hermitian matrices after the ten specified samples.

For the concrete radii \(r=1\), \(s=2\), the distinct, trace-one positive-semidefinite matrices
\[
P=\operatorname{diag}(0,1,0),\qquad
H=\operatorname{diag}(4/5,0,1/5)
\]
produce identical measurements at both radii for **every** angle; their trace distance is one. Their intensities at radius \(3\) are respectively \(9\) and \(17\).

## Assumptions and scope
The radii are positive and distinct. The five angular samples at each radius are equally spaced through a complete fifth-root grid. The measured matrices are \(3\times3\) Hermitian; the fiber statement concerns arbitrary positive-semidefinite candidates given data from a rank-one matrix. No trace normalization is assumed in the general theorem. The example additionally has trace one. The two-radius rank-one uniqueness statement includes the zero vector as a trivial endpoint.

A direct Gaussian-STFT realization uses a periodic three-tone function
\[
f(x)=\sum_{k=0}^{2}a_k e^{2\pi i k\Omega x},\qquad \Omega>0,
\]
and the window \(h(x)=e^{-\pi x^2}\), with
\[
V_hf(t,\omega)=\int_{\mathbb R}f(x)h(x-t)e^{-2\pi i\omega x}\,dx.
\]
The integral converges absolutely for this bounded periodic \(f\). Writing \(q_k=a_k e^{-\pi k^2\Omega^2}\) gives the exact identity
\[
V_hf(t,\omega)=e^{-2\pi i\omega t-\pi\omega^2}
\sum_{k=0}^2q_k\left(e^{2\pi\Omega\omega}e^{2\pi i\Omega t}\right)^k.
\]
Thus the Gaussian-normalized intensity \(e^{2\pi\omega^2}|V_hf(t,\omega)|^2\) equals \(w_\rho(\theta)^*qq^*w_\rho(\theta)\), where \(\rho=e^{2\pi\Omega\omega}\) and \(\theta=2\pi\Omega t\). The two circles correspond to two distinct frequency lines sampled at \(t=m/(5\Omega)\); a single measurement at a third frequency line completes the Hermitian lift. Positivity for higher-rank lifts corresponds to a positive-semidefinite coefficient covariance, not necessarily one deterministic signal.

## Proof
**1. Exact linear kernel.** For every Hermitian \(H=(H_{jk})_{j,k=0}^2\), expand
\[
w_\rho(\theta)^*Hw_\rho(\theta)
=\sum_{j,k=0}^2\rho^{j+k}H_{jk}e^{i(j-k)\theta}.
\]
This is a trigonometric polynomial of degree at most two. Its five samples at \(\theta_m=2\pi m/5\) determine all five Fourier coefficients without aliasing. If every measured value is zero at both radii, the coefficient of \(e^{2i\theta}\), namely \(\rho^2H_{20}\), forces \(H_{20}=H_{02}=0\). The coefficient of \(e^{i\theta}\) is \(\rho H_{10}+\rho^3H_{21}\). Its vanishing at the distinct positive radii forces \(H_{10}=H_{21}=0\), hence all off-diagonal entries are zero. The constant coefficient is \(H_{00}+\rho^2H_{11}+\rho^4H_{22}\). As a quadratic polynomial in \(\rho^2\), it vanishes at \(r^2\) and \(s^2\) precisely when its coefficient vector is a real multiple of \((r^2s^2,-r^2-s^2,1)\). This proves the kernel formula, of real dimension one. Its generator has determinant \(-r^2s^2(r^2+s^2)\ne0\).

**2. Exact positive-semidefinite intersection.** Let \(P=qq^*\). By step 1, every Hermitian matrix with the same data has the unique form \(P+tK_{r,s}\) for a real number \(t\). If \(t<0\), the two-dimensional coordinate subspace spanned by the first and third standard basis vectors is strictly negative for \(tK_{r,s}\). Its intersection with \(q^\perp\) is nonzero, so some nonzero vector has a strictly negative quadratic form under \(P+tK_{r,s}\). Thus \(t<0\) is impossible.

Suppose \(t>0\). In the outer coordinates \(0,2\), the principal block is \(A=tD+vv^*\succ0\), where
\[
D=\operatorname{diag}(r^2s^2,1),\qquad v=(q_0,q_2)^T.
\]
Let \(\beta=v^*D^{-1}v=|q_0|^2/(r^2s^2)+|q_2|^2\). By the rank-one inverse identity, \(v^*A^{-1}v=\beta/(t+\beta)\). The Schur complement of \(A\) in \(P+tK_{r,s}\) is therefore
\[
|q_1|^2-t(r^2+s^2)-|q_1|^2\frac{\beta}{t+\beta}
=t\left(\frac{|q_1|^2}{t+\beta}-(r^2+s^2)\right).
\]
It is nonnegative exactly when \(t\le|q_1|^2/(r^2+s^2)-\beta=\tau_{r,s}(q)\). When \(\tau_{r,s}(q)>0\), the Schur complement is strictly positive for \(0<t<\tau\), giving rank three, and vanishes at \(t=\tau\), giving rank two. At \(t=0\), \(P\) is positive semidefinite. This proves the complete fiber statement, including boundary and zero cases.

**3. Rank-one injectivity and its failure for unrestricted lifts.** A difference of two rank-one Hermitian matrices has rank at most two. Since every nonzero multiple of \(K_{r,s}\) has rank three, equal two-circle data imply equal rank-one matrices, hence the underlying vectors agree up to global phase. Conversely, the positive-\(\tau\) cone admits rank-two and rank-three competitors exactly as stated; it is not strictly complete there.

**4. One extra sample.** The displayed evaluation of \(K_{r,s}\) at \(u\) is the factorization of \(u^4-(r^2+s^2)u^2+r^2s^2\). It does not depend on angle and is nonzero if \(u\notin\{r,s\}\). Consequently the added functional detects the sole existing kernel direction, giving rank nine on the nine-dimensional real Hermitian space. Because the original rank is eight, fewer than one additional scalar measurement cannot suffice.

**5. Exact example and STFT.** With \(r=1,s=2,q=(0,1,0)^T\), the endpoint is \(\tau=1/5\) and \(P+\tau K=\operatorname{diag}(4/5,0,1/5)\). Its intensity equals \(4/5+\rho^4/5\), while that of \(P\) is \(\rho^2\); they coincide at \(\rho=1,2\). Both matrices are trace-one with orthogonal support, so \(\frac12\|P-H\|_1=1\). At \(\rho=3\) the intensities are \(17\) and \(9\). Finally, direct substitution and the Gaussian Fourier integral \(\int e^{-\pi y^2}e^{-2\pi i\xi y}dy=e^{-\pi\xi^2}\) establish the STFT identity in the scope section.

## Verification
The standalone `CHECK.py` reconstructs the measurement matrix directly from a nine-element real Hermitian basis, checks its numerical rank eight, and verifies rank nine after adding an off-circle sample. It also tests the exact kernel, the PSD fiber endpoint and interior for sixteen parameter/seed combinations, the trace-one counterexample, and the Gaussian-STFT identity against independent Gauss-Hermite quadrature. Running `python CHECK.py` with NumPy produces `TWO_CIRCLE_PSD_FIBER_CHECKS_PASSED 16_SETS_AND_GAUSSIAN_STFT`. These are finite numerical consistency checks; the preceding proof establishes the universal assertions.

## Relationship to prior work
Chen, Lu, Sun and Zhao (2026) study short-time Fourier-transform phase retrieval with two window functions and sampled lines, including periodic signals. Their compact-window, two-window hypotheses and uniqueness theorems do not formulate this fixed-Gaussian, three-tone, positive-semidefinite matrix fiber. Chalendar and Partington (2024) establish phase retrieval for analytic functions from modulus data on two circles; this covers the qualitative **rank-one** uniqueness phenomenon, which is not claimed as novel here. Baldwin, Deutsch and Kalev (2016) distinguish rank-constrained from strictly-complete positive-semidefinite measurements in quantum tomography. Jaming and Rathmair (2024) use semidefinite programming and matrix completion in general Gabor reconstruction. None of these inspected results specifies the exact two-radius degree-two PSD feasibility segment, its coefficient cone and rank transition, or its sharp one-sample completion. An equivalent identity in older moment, analytic, or tomography literature remains an originality risk.

## Limitations
The theorem treats only quadratic polynomial evaluations (three Fourier tones), exactly five equally spaced time samples on each of two frequency lines, and noiseless intensities. The statement is pointwise in the source vector, and the extra sample gives linear injectivity without a quantitative noise-stability bound. The general PSD matrices need not have trace one; the trace-one ambiguity is demonstrated only for the specified normalized example. No claim is made about all periodic signals, arbitrary sampling grids, or generic dimension-independent tomography.

## References
1. T. Chen, H. Lu, W. Sun and Y. Zhao, *STFT Phase Retrieval with Two Window Functions*, arXiv:2602.05210v1 (first publicly posted 2026-02-05), https://arxiv.org/abs/2602.05210.
2. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255v1 (2024), https://arxiv.org/abs/2403.16255.
3. C. H. Baldwin, I. H. Deutsch and A. Kalev, *Strictly-complete measurements for bounded-rank quantum-state tomography*, arXiv:1605.02109v1 (2016), https://arxiv.org/abs/1605.02109.
4. P. Jaming and M. Rathmair, *Gabor Phase Retrieval via Semidefinite Programming*, *Foundations of Computational Mathematics* (first published 2024-11-07), https://doi.org/10.1007/s10208-024-09683-6.
