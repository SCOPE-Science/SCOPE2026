# An exact Schatten-order reversal between analytic and maximal Gaussian Fock projections

## Finding
For the analytic Gaussian Fock–Bargmann integral projection and the associated positive-kernel (maximal) integral projection, the Schatten ordering reverses at exactly two exponents. Their trace norms and Hilbert–Schmidt norms agree *for every strictly compact Gaussian weight triple*, although the maximal operator has the larger operator norm. For the intermediate exponents the maximal operator has a **strictly smaller** Schatten norm, while for lower and higher exponents it has a **strictly larger** one.

Precisely, let \(t,\alpha,\beta>0\), let \(\delta=\beta(2t-\alpha)-t^2>0\), and set
\[
C=\sqrt{\beta/\alpha},\qquad r=\frac{t}{\sqrt{\beta(2t-\alpha)}},\qquad
q=\frac{t}{\sqrt{\beta(2t-\alpha)}+\sqrt\delta}.
\]
Then \(0<q,r<1\), \(r=2q/(1+q^2)\), and the **complete nonzero singular-value multisets**, with multiplicity, are
\[
\{s_n(P_t)\}_{n\ge0}=\{Cr^{n+1}:n\ge0\},\qquad
\{s_{j,k}(P_t^+)\}_{j,k\ge0}=\{2Cq^{j+k+1}:j,k\ge0\}.
\]
For every \(p>0\), the corresponding Schatten quasi-norms satisfy
\[
\|P_t\|_{\mathcal S_p}^{p}=C^p\frac{r^p}{1-r^p},\qquad
\|P_t^+\|_{\mathcal S_p}^{p}=(2C)^p\frac{q^p}{(1-q^p)^2},
\]
so their strict ordering is
\[
\boxed{\quad
\begin{array}{ll}
\|P_t^+\|_{\mathcal S_p}>\|P_t\|_{\mathcal S_p},&0<p<1\ \text{or}\ p>2,\\
\|P_t^+\|_{\mathcal S_p}=\|P_t\|_{\mathcal S_p},&p=1\ \text{or}\ p=2,\\
\|P_t^+\|_{\mathcal S_p}<\|P_t\|_{\mathcal S_p},&1<p<2.
\end{array}\quad}
\]
In contrast, \(\|P_t^+\|_{\rm op}/\|P_t\|_{\rm op}=1+q^2>1\).

The singular-value formulas also quantify the distinct approach to noncompactness. Fix \(\alpha,t>0\) with \(2t>\alpha\), let \(\beta\downarrow t^2/(2t-\alpha)\), and write the positive deficit as \(\delta\downarrow0\). For each \(u>0\), put \(N_\delta=\lfloor ut^2/\delta\rfloor\). With decreasing singular values indexed from zero,
\[
\frac{s_{N_\delta}(P_t)}{\|P_t\|_{\rm op}}\longrightarrow e^{-u/2},\qquad
\frac{s_{N_\delta}^{\downarrow}(P_t^+)}{\|P_t^+\|_{\rm op}}\longrightarrow e^{-\sqrt{2u}}.
\]
At the boundary \(\delta=0\), with \(2t>\alpha\), the analytic operator is a noncompact scalar multiple of a partial isometry, while the maximal operator has continuous singular spectrum \([0,2\sqrt{\beta/\alpha}]\) and does not attain its operator norm.

## Assumptions and scope
Write \(d\lambda_c(z)=(c/\pi)e^{-c|z|^2}\,dA(z)\) for normalized Gaussian area measure on \(\mathbb C\), \(H_c=L^2(\mathbb C,d\lambda_c)\), and \(F_c^2\subset H_c\) for the closed holomorphic Fock subspace. On bounded compactly supported inputs define
\[
(P_tf)(z)=\frac t\pi\int_{\mathbb C}e^{tz\overline w}f(w)e^{-t|w|^2}\,dA(w),\quad
(P_t^+f)(z)=\frac t\pi\int_{\mathbb C}e^{t\operatorname{Re}(z\bar w)}f(w)e^{-t|w|^2}\,dA(w).
\]
In the strict region \(\delta>0\), they extend compactly as \(P_t:H_\alpha\to F_\beta^2\) and \(P_t^+:H_\alpha\to H_\beta\). Their singular values are computed using the normalized Hilbert norms of these spaces; \(F_\beta^2\) can be regarded as a subspace of \(H_\beta\). The notation \(s_n\) starts at \(n=0\); the extra zero singular values from the analytic operator's kernel do not enter its positive singular-value sequence. For \(0<p<1\) the Schatten expression is a quasi-norm. The critical assertions concern \(\delta=0\) only with \(2t-\alpha>0\). The singular spectrum at the boundary means the spectrum of the positive modulus \(|P_t^+|\) on its source space.

## Proof
**1. Analytic singular spectrum.** Expanding the holomorphic exponential in the output variable yields
\[
(P_tf)(z)=\sum_{n=0}^\infty \frac{t^{n+1}}{\alpha n!}
\langle f, w^ne^{-(t-\alpha)|w|^2}\rangle_{H_\alpha}\,z^n.
\]
(The inner product is linear in the first slot.) Because the coefficient vectors are radial multiples of distinct monomials, they are mutually orthogonal in the source. So are the target monomials; indeed \(\|z^n\|_{H_\beta}^2=n!/\beta^n\). A Gaussian moment gives
\[
\int_{\mathbb C}|w|^{2n}e^{-2(t-\alpha)|w|^2}\,d\lambda_\alpha(w)
=\frac{\alpha n!}{(2t-\alpha)^{n+1}}.
\]
The square of the singular value associated with the \(n\)-th monomial is consequently
\[
\frac{t^{2n+2}}{\alpha\,\beta^n(2t-\alpha)^{n+1}}
=C^2r^{2n+2}.
\]
After normalization the source vectors and output monomials are orthonormal sequences, with the output monomials complete in \(F_\beta^2\). For both \(r<1\) and \(r=1\) the coefficient multipliers are bounded, giving the bounded extension by density. The source orthogonal complement is the kernel, so the displayed list is the full nonzero singular multiset when \(r<1\).

**2. Maximal singular spectrum.** The unitary Gaussian change \(U_c:H_c\to L^2(\mathbb C,dA)\),
\(U_cf(z)=\sqrt{c/\pi}\,e^{-c|z|^2/2}f(z)\), transforms \(P_t^+\) into an integral operator with kernel
\[
\frac t\pi\sqrt{\frac\beta\alpha}
\exp\!\left[-\frac\beta2|z|^2-\frac{2t-\alpha}{2}|w|^2
+t\operatorname{Re}(z\bar w)\right].
\]
Two unitary real-plane dilations, \(x=\sqrt{\beta/2}\,z\) and \(y=\sqrt{(2t-\alpha)/2}\,w\), turn it into an operator on \(L^2(\mathbb R^2)\) with kernel
\[
\frac{2Cr}{\pi}\exp[-|x|^2-|y|^2+2r\,x\cdot y].
\]
Put \(d=\sqrt{1-r^2}\) and \(q=r/(1+d)\), equivalent to the definition in the finding. In one real dimension the Gaussian ground function \(e^{-dx^2}\) is an eigenfunction of the operator with kernel \(e^{-x^2-y^2+2rxy}\), with eigenvalue \(\sqrt{\pi/(1+d)}\). The classical Mehler identity provides the complete orthogonal Hermite eigenfamily with successive eigenvalue ratio \(q\). Taking its two-dimensional tensor product and the prefactor gives
\[
\frac{2Cr}{\pi}\frac\pi{1+d}\,q^{j+k}=2Cq^{j+k+1},
\quad j,k\in\mathbb N_0.
\]
These are all eigenvalues, since the Hermite functions are complete. They are positive, so the transformed operator's singular values are these eigenvalues. The two unitary changes preserve singular values.

**3. Exact Schatten comparison.** Geometric summation gives the two powered Schatten formulas and
\[
\left(\frac{\|P_t^+\|_{\mathcal S_p}}{\|P_t\|_{\mathcal S_p}}\right)^p
=\frac{(1+q^2)^p-(2q)^p}{(1-q^p)^2}.
\]
We prove its sign relative to \(1\) for all real \(p>0\). Let \(q=e^{-s}\) with \(s>0\), and set
\[
F_p(s)=(e^s+e^{-s})^p-e^{ps}-e^{-ps}.
\]
Multiplying the numerator-minus-denominator of the preceding fraction by \(e^{ps}\) produces \(F_p(s)-F_p(0)\). With \(a=e^s/(e^s+e^{-s})\), \(b=e^{-s}/(e^s+e^{-s})\), so \(a+b=1\), \(a>b\), differentiation yields
\[
F_p'(s)=p(e^s-e^{-s})(e^s+e^{-s})^{p-1}
\left(1-\frac{a^p-b^p}{a-b}\right).
\]
The fraction is the mean of \(f_p(x)=p x^{p-1}\) over \([b,a]\). To compare with its mean over \([0,1]\), take \(U\) uniform on \((0,1)\): \(aU+b(1-U)\) is uniform on \((b,a)\). Pointwise there is a strict convexity inequality \(f_p(aU+b(1-U))<a f_p(U)+b f_p(1-U)\) except at \(U=1/2\), for \(0<p<1\) and \(p>2\). Both terms on the right are integrable even for \(0<p<1\). The reverse inequality holds for \(1<p<2\), by strict concavity. The right-hand mean is \(1\) in all cases, and for \(p=1,2\) the function is affine so equality holds. Thus the derivative has the claimed sign, and integrating from \(s=0\) gives the strict ordering and both equality exponents. The operator norm comparison follows from the leading entries \(2Cq\) and \(Cr\).

**4. Sharp boundary profiles.** Put \(\delta\downarrow0\) with \(\alpha,t\) fixed and \(\beta=(t^2+\delta)/(2t-\alpha)\). Then
\[
-\log r=\frac\delta{2t^2}+O(\delta^2),\qquad
-\log q=\operatorname{arsinh}(\sqrt\delta/t)
=\frac{\sqrt\delta}t+O(\delta^{3/2}).
\]
The normalized analytic singular sequence is \(r^n\), giving the first profile. The maximal level \(m=j+k\) has multiplicity \(m+1\), hence its zero-based decreasing index is between \(m(m+1)/2\) and \((m+1)(m+2)/2-1\). Thus the level at index \(N\) is \(m=\sqrt{2N}+O(1)\). Since its normalized singular value is \(q^m\), the second profile follows.

At \(\delta=0\), the decomposition in Step 1 has \(r=1\), so the operator is \(C\) times an isometry on the closed span of infinitely many source vectors, vanishing on its orthogonal complement. For the maximal operator the transformed kernel becomes \((2C/\pi)e^{-|x-y|^2}\), a Gaussian convolution on \(L^2(\mathbb R^2)\). Its Fourier multiplier is \(2C e^{- |\xi|^2/4}\), whose essential range is \([0,2C]\). Every level set has Lebesgue measure zero, so no value in the spectrum is an eigenvalue, and the operator norm \(2C\) is not attained. The modulus of the original operator is unitarily equivalent to this positive convolution. Thus the compactness boundary is genuine.

## Verification
The standalone `verify.py` checks the exact rational example \(\alpha=t=1\), \(\beta=25/16\): here \(q=1/2\), \(r=4/5\), \(C=5/4\). The trace norms are both \(5\) and the squared Hilbert–Schmidt norms are both \(25/9\). The analytic operator has operator norm \(1\); the maximal operator has operator norm \(5/4\). The script also samples the sign comparison, hyperbolic parameter identity and near-critical scaling profiles. A passing finite grid is **not** a proof of universal inequalities or asymptotics; those follow from Steps 1–4.

## Relationship to prior work
Fang and Tien introduce exactly the pair \(P_t,P_t^+\) and classify their boundedness and compactness over a wider family of Gaussian mixed-norm source and target spaces. Their Theorems 1.1–1.2 already give bounded noncompact operators at the Gaussian boundary for the Hilbert-to-Hilbert case. The result *Anisotropic Gaussian Fock projections: exact singular spectra and a rational–irrational counting transition* already computes product singular spectra of the **analytic** Gaussian projection; its isotropic one-dimensional specialization gives the analytic multiset in Step 1. The positive-kernel spectrum in Step 2 is a direct application of the classical Mehler identity after Gaussian unitary changes. The Hilbert–Schmidt equality also follows directly from equality of the absolute values of the kernels. The contribution here is the relative ordering at all real Schatten exponents, including the strict reversal between \(1\) and \(2\), and the comparison of the two near-critical ordered-rank profiles and limiting spectral types. It is not a new compactness criterion or a new general Mehler theorem.

## Limitations
The theorem is proved for complex dimension one, source and target Hilbert norms, positive scalar Gaussian weights and the displayed standard kernels. It does not assert comparisons of arbitrary absolute-value integral kernels, higher-dimensional anisotropy, mixed non-Hilbert Banach norms, or perturbation robustness. A more general unlocated theorem on Gaussian-kernel majorization or rearrangements might subsume the comparison. The threshold analysis keeps \(\alpha,t\) fixed with \(2t>\alpha\); no uniformity over all weight triples is asserted.

## References
1. X. Fang and P. T. Tien, *Fock Projections between Gaussian Mixed-Norm Spaces: Full-Range Boundedness and Compactness*, arXiv:2610.41461v1, https://arxiv.org/abs/2610.41461.
2. *Anisotropic Gaussian Fock projections: exact singular spectra and a rational–irrational counting transition*, `SCOPE-anisotropic-gaussian-fock-projections-exact-singular-spectra-and--1cedacd12a18`, November 8, 2026.
3. F. A. Berezin, *The Method of Second Quantization*, for the classical Mehler-Hermite semigroup and Gaussian kernel diagonalization.
