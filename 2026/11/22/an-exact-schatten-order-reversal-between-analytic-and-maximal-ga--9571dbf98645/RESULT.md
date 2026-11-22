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
In the strict region \(\delta>0\), they extend compactly as \(P_t:H_\alpha\to F_\beta^2\) and \(P_t^+:H_\alpha\to H_\beta\). Their singular values are computed using the normalized Hilbert norms of these spaces; \(F_\beta^2\) can be regarded as a subspace of \(H_\beta\). The notation \(s_n\) starts at \(n=0\); the extra zero singular values from the analytic operator's kernel do not enter its positive singular-value sequence. For \(0<p<1\) the Schatten expression is a quasi-norm. The critical assertions concern \(\delta=0\) only with \(2t-\alpha>0\).

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
The coefficient vectors yield a mutually orthogonal complete description of the nonzero part; hence the displayed list is the full nonzero singular multiset, not merely a bound.

**2. Maximal singular spectrum.** The unitary Gaussian change \(U_c:H_c\to L^2(\mathbb C,dA)\),
\(U_cf(z)=\sqrt{c/\pi}\,e^{-c|z|^2/2}f(z)\), transforms \(P_t^+\) into an integral operator with kernel
\[
\frac t\pi\sqrt{\frac\beta\alpha}
\exp\!\left[-\frac\beta2|z|^2-\frac{2t-\alpha}{2}|w|^2
+t\operatorname{Re}(z\bar w)\right].
\]
Two unitary real-plane dilations, \(x=\sqrt{\beta/2}\,z\) and \(y=\sqrt{(2t-\alpha)/2}\,w\), turn it into the self-adjoint positive integral operator on \(L^2(\mathbb R^2)\) with kernel
\[
\frac{2Cr}{\pi}\exp[-|x|^2-|y|^2+2r\,x\cdot y].
\]
Put \(d=\sqrt{1-r^2}\) and \(q=r/(1+d)\), equivalent to the definition in the finding. In one real dimension the Gaussian ground function \(e^{-dx^2}\) is an eigenfunction of \(e^{-x^2-y^2+2rxy}\), with eigenvalue \(\sqrt{\pi/(1+d)}\). The classical Mehler identity, or conjugation to the Hermite oscillator semigroup, provides the complete orthogonal Hermite eigenfamily with successive eigenvalue ratio \(q\). Taking its two-dimensional tensor product and the prefactor gives
\[
\frac{2Cr}{\pi}\frac\pi{1+d}\,q^{j+k}=2Cq^{j+k+1},
\quad j,k\in\mathbb N_0.
\]
These are all eigenvalues, since the Hermite functions are complete. They are positive, and the two unitary changes preserve singular values.

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
The fraction inside is the mean of \(p x^{p-1}\) over \([b,a]\). That interval is a strict symmetric contraction of \([0,1]\). Comparing uniform distributions by convex order shows that this mean is **smaller than** its \([0,1]\) mean (which is \(1\)) when \(p x^{p-1}\) is strictly convex, i.e. \(0<p<1\) or \(p>2\); it is **larger than** \(1\) when the function is strictly concave, i.e. \(1<p<2\). Integrability at the origin for \(0<p<1\) permits the same convex-order argument by truncation. For \(p=1,2\) the integrand is affine or constant and both means coincide. Because \(F_p(0)\) is the comparison baseline, this proves the strict sign pattern and both exact equality exponents. The operator norm comparison follows from the leading entries \(2Cq\) and \(Cr\).

**4. Sharp boundary profiles.** Put \(\delta\downarrow0\) with \(\alpha,t\) fixed and \(\beta=(t^2+\delta)/(2t-\alpha)\). Then
\[
-\log r=\frac\delta{2t^2}+O(\delta^2),\qquad
-\log q=\operatorname{arsinh}(\sqrt\delta/t)
=\frac{\sqrt\delta}t+O(\delta^{3/2}).
\]
The normalized analytic singular sequence is \(r^n\), giving the first profile. The maximal level \(m=j+k\) has multiplicity \(m+1\), hence its zero-based decreasing index is between \(m(m+1)/2\) and \((m+1)(m+2)/2-1\). Thus the level at index \(N\) is \(m=\sqrt{2N}+O(1)\). Since its normalized singular value is \(q^m\), the second profile follows.

At \(\delta=0\), the analytic formula has \(r=1\), so its nonzero singular values all equal \(C\), proving the partial-isometry statement. For the maximal operator the transformed kernel becomes \((2C/\pi)e^{-|x-y|^2}\), a Gaussian convolution on \(L^2(\mathbb R^2)\). Its Fourier multiplier is \(2C e^{-|\xi|^2/4}\); this gives purely continuous spectrum of the positive transformed operator, essential norm \(2C\) and nonattainment of its norm. Thus the compactness boundary is genuine.

## Verification
The standalone `verify.py` checks the exact rational example \(\alpha=t=1\), \(\beta=25/16\): here \(q=1/2\), \(r=4/5\), \(C=5/4\). The two trace norms both equal \(5\); both squared Hilbert–Schmidt norms equal \(25/9\); their operator norms are \(5/4\) and \(1\), respectively. The script additionally tests the strict sign changes, the hyperbolic parameter identity and the two near-critical scaling profiles on finite parameter grids. A passing finite grid is **not** a proof of universal inequalities or asymptotics; those follow from Steps 1–4.

## Relationship to prior work
Fang and Tien, arXiv:2610.41461v1 (first public source dated 2026-10-30), introduce exactly the pair \(P_t,P_t^+\) and classify their boundedness and compactness over a much wider family of Gaussian mixed-norm source and target spaces. Their full available text gives neither exact Hilbert-space singular multisets nor the counterintuitive Schatten-order reversal for the two operators. The previously published published-finding corpus result *Anisotropic Gaussian Fock projections: exact singular spectra and a rational–irrational counting transition* (2026-11-08) already computes product singular spectra of the **analytic** Gaussian projection in arbitrary covariance dimensions; its isotropic one-dimensional specialization covers the analytic multiset in Step 1. It does not address the maximal absolute-kernel operator or compare the two \(\mathcal S_p\) sequences. Dong and Zhu, arXiv:2509.16672v1, compute spectra for other Gaussian operators acting **between analytic Fock spaces**; the source and target of the present maximal operator are full Gaussian \(L^2\) spaces. The classical Hermite/Mehler identity supplies the complete maximal Gaussian spectrum as a proof ingredient, and convex order supplies the sign mechanism. The assessed contribution is the **all-exponent sharp relative Schatten law**, together with the contrasting near-critical ordered-rank profiles of these two naturally paired projections; neither is claimed to be a new general Mehler theorem.

## Limitations
The theorem is proved for complex dimension one, source and target Hilbert norms, positive scalar Gaussian weights and the displayed standard kernels. It does not assert comparisons of arbitrary absolute-value integral kernels, higher-dimensional anisotropy, mixed non-Hilbert Banach norms, or perturbation robustness. The classical Hermite calculus and prior analytic singular-value work cover substantial ingredients. A more general unlocated theorem on positive Gaussian-kernel majorization or rearrangements might subsume the Schatten comparison and remains a bibliographic risk. The threshold analysis keeps \(\alpha,t\) fixed with \(2t>\alpha\); no uniformity over all weight triples is asserted. No independent audit has been performed.

## References
1. X. Fang and P. T. Tien, *Fock Projections between Gaussian Mixed-Norm Spaces: Full-Range Boundedness and Compactness*, arXiv:2610.41461v1, first public 2026-10-30, https://arxiv.org/abs/2610.41461.
2. *Anisotropic Gaussian Fock projections: exact singular spectra and a rational–irrational counting transition*, public result 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-anisotropic-gaussian-fock-projections-exact-singular-spectra-and--1cedacd12a18.
3. X. Dong and K. Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672, https://arxiv.org/abs/2509.16672.
4. F. A. Berezin, *The Method of Second Quantization*, for the classical Mehler-Hermite semigroup and Gaussian kernel diagonalization.
5. K. Zhu, *Analysis on Fock Spaces*, Springer (2012), for standard Gaussian Fock conventions.
