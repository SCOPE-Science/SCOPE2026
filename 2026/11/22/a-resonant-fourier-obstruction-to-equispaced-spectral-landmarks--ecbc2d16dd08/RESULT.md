# A resonant Fourier obstruction to equispaced spectral landmarks for analytic circle kernels

## Finding

For every even integer \(m=2q\ge6\) and \(0<\varepsilon<2/15\), there is an explicit **real-analytic strictly positive-definite** translation-invariant kernel on the circle for which \(m\) equally spaced landmarks are **not** minimizers of the rank-three spectral alignment loss. In fact, a nonuniform \(m\)-landmark design, also tight on the three leading eigenfunctions, improves alignment by an arbitrarily large factor as the tail amplitude tends to zero.

Let \(F_m\) be the RKHS projector alignment loss defined below. Define the regular and two-coset designs
\[
R_m=\left\{\frac{2\pi j}{m}:0\le j<m\right\},\qquad
S_m=\left\{\frac{2\pi j}{q},\ \frac{\pi}{m}+\frac{2\pi j}{q}:0\le j<q\right\},\qquad q=m/2.
\]
They both have \(m\) distinct nodes and their leading-eigenfunction sampling matrices have identical column Gram matrices \(mI_3\). Nevertheless,
\[
\boxed{F_m(R_m)\ge\frac13,\qquad 0<F_m(S_m)\le\frac{5\varepsilon}{2}\bigl(1-2^{1-m}\bigr)<\frac13.}
\]
Consequently \(F_m(R_m)/F_m(S_m)\ge 2/(15\varepsilon)\), and there is no universal performance factor for equispacing within this class of analytic positive-definite translation-invariant kernels.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with normalized Haar measure \(d\theta/(2\pi)\) and Fourier functions \(\varphi_k(\theta)=e^{ik\theta}\). Fix even \(m\ge6\) and \(0<\varepsilon<2/15\). Define
\[
\lambda_k=\begin{cases}
2,&k=0,\\
1,&k=\pm1,\\
\tfrac12,&k=\pm m,\\
\varepsilon2^{-|k|},&k\in\mathbb Z\setminus\{0,\pm1,\pm m\}.
\end{cases}
\quad
K_{m,\varepsilon}(\theta,\phi)=\sum_{k\in\mathbb Z}\lambda_k e^{ik(\theta-\phi)}.
\]
The coefficients are positive, absolutely summable, and exponentially decaying, so the kernel is continuous, real-valued, real-analytic, translation-invariant and strictly positive definite. In the RKHS \(\mathcal H\), the functions \(\psi_k=\sqrt{\lambda_k}\,\varphi_k\) form an orthonormal basis. The top-three eigenspace of the Haar-integral operator is exactly \(V_3=\operatorname{span}\{\varphi_{-1},\varphi_0,\varphi_1\}\), separated from the other eigenvalues by a gap at least \(1/2\).

For a set of \(m\) distinct nodes \(Z\), let \(P_Z\) be the **orthogonal RKHS projector** onto \(\operatorname{span}\{K_{m,\varepsilon}(\cdot,z):z\in Z\}\). The numerical approximation objective is
\[
F_m(Z)=\sum_{t=-1}^{1}\|(I-P_Z)\psi_t\|_{\mathcal H}^{2}.
\]
This is the rank-three alignment objective, not a claim about integration error, condition numbers, or data-dependent kernel learning. The kernel is explicitly allowed to depend on the landmark count \(m\).

## Proof

**1. Positive definiteness, spectrum, and tightness.** Because every \(\lambda_k>0\), if \(\sum_{i,j}\overline{a_i}a_jK(z_i,z_j)=0\) then \(\sum_j a_j e^{-ikz_j}=0\) for each integer \(k\). Taking the first \(m\) consecutive frequencies gives a nonsingular Vandermonde matrix since the nodes are distinct. Hence all \(a_j=0\), proving strict positive definiteness. Since \(\varepsilon<2/15\), the eigenvalues \(2,1,1\) are strictly the three largest, and the largest remaining eigenvalue is \(1/2\).

For \(q\ge3\), the sum of \(e^{irz}\) over either regular \(q\)-gon in \(S_m\) vanishes for \(r=\pm1,\pm2\). The same holds over \(R_m\). Thus for both designs the complex sampling matrix \(\Phi_Z=(\varphi_t(z))_{z\in Z,\,t=-1,0,1}\) satisfies \(\Phi_Z^*\Phi_Z=mI_3\). In real sine-cosine coordinates this is the corresponding real unit-norm tight frame.

**2. Equispacing has an irreducible residual.** In \(\mathcal H\) put
\[
u=\frac{\psi_0-\psi_m-\psi_{-m}}{\sqrt3}.
\]
The basis is orthonormal, so \(\|u\|_{\mathcal H}=1\). For any \(z\in R_m\) one has \(e^{\pm imz}=1\), and the reproducing expansion
\[
K(\cdot,z)=\sum_{k\in\mathbb Z}\sqrt{\lambda_k}\,e^{-ikz}\psi_k
\]
shows that \(\langle u,K(\cdot,z)\rangle=(\sqrt2-\sqrt{1/2}-\sqrt{1/2})/\sqrt3=0\). Therefore \(u\perp\operatorname{ran}P_{R_m}\). Since \(|\langle\psi_0,u\rangle|^2=1/3\), the projector residual of \(\psi_0\) alone is at least \(1/3\), yielding \(F_m(R_m)\ge1/3\).

**3. A de-aliasing competitor.** For each \(t\in\{-1,0,1\}\) construct the explicit kernel-translates witness
\[
v_t=\frac{1}{m\sqrt{\lambda_t}}\sum_{z\in S_m}e^{itz}K(\cdot,z)\in\operatorname{ran}P_{S_m}.
\]
Its coefficient along \(\psi_k\) is
\[
\langle v_t,\psi_k\rangle_{\mathcal H}=\sqrt{\frac{\lambda_k}{\lambda_t}}\frac1m\sum_{z\in S_m}e^{i(t-k)z},
\]
up to the harmless convention for conjugate-linearity of the complex inner product. For \(k,t\in\{-1,0,1\}\), the average is the Kronecker delta, by the geometric sums above. For \(k=\pm m\), it is zero: when \(t=\pm1\), \(t-k\) is not divisible by \(q\); when \(t=0\), the two \(q\)-gon contributions cancel because their relative phase at frequency \(m\) is \(e^{\pm i\pi}=-1\). Thus \(v_t\) matches \(\psi_t\) exactly at all five specified frequencies \(\{0,\pm1,\pm m\}\).

All other Fourier coefficients of \(\psi_t-v_t\) have magnitude at most \(\sqrt{\lambda_k/\lambda_t}\). By orthonormality and optimality of orthogonal projection,
\[
\|(I-P_{S_m})\psi_t\|_{\mathcal H}^{2}\le\|\psi_t-v_t\|_{\mathcal H}^{2}\le\frac1{\lambda_t}\sum_{k\notin\{0,\pm1,\pm m\}}\lambda_k.
\]
The sum is exactly \(\varepsilon(1-2^{1-m})\). Summing over the three target frequencies and using \(\lambda_0=2\), \(\lambda_{\pm1}=1\) proves
\[
F_m(S_m)\le\left(\frac12+1+1\right)\varepsilon(1-2^{1-m})=\frac52\varepsilon(1-2^{1-m}).
\]
Positivity \(F_m(S_m)>0\) follows because no finite combination of kernel translates can equal any \(\psi_t\): if its coefficients at all sufficiently large consecutive Fourier indices vanished, the corresponding finite Vandermonde matrix would force all combination coefficients to vanish. The strict inequality \((5/2)\varepsilon(1-2^{1-m})<1/3\) holds for the assumed \(\varepsilon<2/15\). Dividing the bounds gives the asserted factor. This finishes the infinite-family proof.

## Verification

The accompanying standalone `verify.py` evaluates the positive-definite kernel by summing its Fourier tail as a geometric series. It computes \(F_m(Z)=3-\operatorname{tr}(K_Z^{-1}K_Z^{(3)})\), with \(K_Z^{(3)}(\theta,\phi)=2+2\cos(\theta-\phi)\), using independent Gram-matrix inversions. Sixteen parameter combinations were checked: \(m\in\{6,8,10,12\}\) and \(\varepsilon\in\{0.001,0.01,0.05,0.1\}\). Each passed the analytic lower bound, upper bound, and strict comparison.

For instance at \(m=6\), \(\varepsilon=0.01\): \(F_m(R_m)\approx0.3341278\), \(F_m(S_m)\approx0.0029595\), while the rigorous upper bound is \(0.02421875\). These floating-point checks corroborate, but do not establish, the theorem; the proof uses exact Fourier identities and Hilbert-space inequalities.

## Relationship to prior work

Schreiber, *Spectral Landmarks* (arXiv:2611.20336v1, 16 November 2026), introduces the alignment objective, shows that tight leading-eigenfunction sampling matrices optimize standard frame criteria, and gives an exact equispaced aliasing formula for periodic Gaussian spectra. Section 4.3 explicitly notes that for more landmarks than retained eigenfunctions tightness alone does not control the alignment objective, and offers a spherical cube-versus-antiprism instance. The present statement is an explicit **circle**, **real-analytic strictly positive-definite** kernel example in which both competing designs are tight but equispacing has a constant residual while a nonuniform design has vanishing residual; the ratio is unbounded. The source's published Gaussian-kernel behavior is not contradicted, because the constructed Fourier spectrum has a deliberate nonmonotone resonance at frequency \(m\).

Wind-Andersen, *Alias Geometry and Density Compensation in Perturbed Fourier Sampling* (arXiv:2611.02379v1, 2 November 2026), studies perturbative Fourier-Gram defects and reweighting, a distinct objective; its alias-class viewpoint gives background context but no bound for this RKHS projector criterion. Classical Fourier aliasing and multi-coset sampling motivate the two-coset de-aliasing witness, but do not by themselves furnish the present alignment comparison or analytic-kernel bound.

## Limitations

This is a constructed counterexample family, not a classification of optimal landmarks. The staggered set is shown to beat the regular set but is not claimed globally optimal. The kernels vary with \(m\), and the Fourier spectrum is intentionally nonmonotone; no conclusion is asserted for Gaussian circle kernels or monotone spectral profiles. No uniform finite-precision conditioning guarantee is established. The exact statements concern the mathematical RKHS in exact arithmetic, and the extra numerical tests are not substitutes for the analytic proof. Independent mathematical validation has not been performed.

## References

- J. Schreiber, *Spectral Landmarks: Alignment of Landmark Kernel Translates with the Leading Eigenfunctions of a Kernel Operator*, arXiv:2611.20336v1, publicly released 16 November 2026. https://arxiv.org/html/2611.20336v1
- E. Wind-Andersen, *Alias Geometry and Density Compensation in Perturbed Fourier Sampling*, arXiv:2611.02379v1, publicly released 2 November 2026. https://arxiv.org/abs/2611.02379
