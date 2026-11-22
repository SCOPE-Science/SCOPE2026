# Parity-forced missing angular channels in second-level polyanalytic Fock space

## Finding
Let \(\mathcal F_{(2)}\) denote the true second polyanalytic Bargmann–Fock space with Gaussian inner product
\[\langle f,g\rangle=\pi^{-1}\int_{\mathbb C} f(z)\overline{g(z)}e^{-|z|^2}\,dA(z).\]
For any integer \(m\ge1\), let \(T_m\) be orthogonal compression to \(\mathcal F_{(2)}\) of multiplication by the unit-modulus angular function \(e^{im\arg z}\) (arbitrary at the origin). Relative to the orthonormal complex-Hermite basis
\[e_p(z)=\frac{z^p\bar z-pz^{p-1}}{\sqrt{p!}},\qquad p\in\mathbb N_0,\]
with the \(p=0\) term interpreted as \(e_0=\bar z\), the operator is an exact \(m\)-step weighted shift:
\[T_m e_p=w_{p,m}e_{p+m},\qquad
 w_{p,m}=\frac{\Gamma(p+m/2)}{\sqrt{p!(p+m)!}}\left(p-\frac{m(m-2)}4\right).\]
The weights are all real. They vanish **exactly** for even \(m=2k\), at the unique index \(p=k(k-1)\). For odd \(m\), no weight vanishes. Consequently,
\[\dim\ker T_m=\begin{cases}1,&m\text{ even},\\0,&m\text{ odd},\end{cases}\qquad
\dim\ker T_m^*=m+\dim\ker T_m,\qquad \operatorname{ind}T_m=-m.\]
For each fixed positive \(m\), \(w_{p,m}=1-3m^2/(8p)+O_m(p^{-2})\) as \(p\to\infty\). Thus \(T_m\) is a compact perturbation of the \(m\)-step unilateral shift, with essential spectrum the unit circle; its ordinary spectrum is the closed unit disk. This is a complete angular-winding selection rule for the first non-analytic Landau level.

## Assumptions and scope
The integer \(m\) is arbitrary and positive and \(p\) ranges over all nonnegative integers. The Hilbert space is the **true second level**, not the direct sum of all levels of order at most two. All symbols are bounded and are only undefined at one null-set point, which does not affect multiplication or compression. The Gaussian parameter is normalized to one. The basis in the finding is known to be complete in \(\mathcal F_{(2)}\), or follows by applying the first creation operator to the analytic Fock monomial basis. Only one angular symbol per integer winding is asserted; no classification of arbitrary angular profiles or higher true levels is claimed.

## Proof
**Basis and angular selection.** Under polar coordinates \(z=\rho e^{i\theta}\), set \(t=\rho^2\). For every \(p\ge0\), with the stated convention, the basis polynomial is \(\rho^{p-1}(t-p)e^{i(p-1)\theta}/\sqrt{p!}\). The standard Gaussian moment identities show \(\|z^p\bar z-pz^{p-1}\|^2=p!\), and its angular frequency is \(p-1\). Completeness follows from the true-level Fock decomposition. Multiplication by \(e^{im\theta}\) shifts angular frequency to \(p+m-1\), so its projection onto this level has only the \(e_{p+m}\) coefficient.

**Exact coefficient.** Removing the normalization gives the Gaussian radial integral
\[I_{p,m}=\int_0^\infty e^{-t}t^{p+m/2-1}(t-p)(t-p-m)\,dt.\]
Write \(a=p+m/2>0\). Expanding the product and using \(\Gamma(a+2)=a(a+1)\Gamma(a)\), \(\Gamma(a+1)=a\Gamma(a)\), gives
\[I_{p,m}=\Gamma(a)\{a(a+1)-(2p+m)a+p(p+m)\}
=\Gamma(a)\left(p+\frac m2-\frac{m^2}4\right).\]
Division by \(\sqrt{p!(p+m)!}\) gives the formula, including \(p=0\), since the formal polar factor cancels against \(t-p\). No numerical integration is used here.

**Zero and defect classification.** The gamma and factorial factors are strictly positive, so \(w_{p,m}=0\) iff \(p=m(m-2)/4\). If \(m=2k\), this equals the nonnegative integer \(k(k-1)\). If \(m\) is odd, the numerator \(m(m-2)\) is odd and cannot be divisible by four; thus no nonnegative integer zero exists. As \(w_{p,m}\to1\), the nonzero weights have a positive lower modulus away from a finite set, the range is closed, and the kernel has the stated dimension. The coordinate range misses the first \(m\) output basis elements and one further output basis element precisely in the even case; hence its orthogonal complement has dimension \(m+\dim\ker T_m\). The index statement follows.

**Asymptotics and spectra.** Stirling's gamma-ratio expansion yields
\[\frac{\Gamma(p+m/2)}{\sqrt{\Gamma(p+1)\Gamma(p+m+1)}}
=p^{-1}\left(1-\frac{m^2/8+m/2}{p}+O_m(p^{-2})\right).\]
Combining this with the linear factor \(p-m(m-2)/4\) gives \(w_{p,m}=1-3m^2/(8p)+O_m(p^{-2})\). The difference from the ordinary \(m\)-step shift is compact, whence the essential spectrum is the unit circle. Compression of a unitary multiplier has norm at most one. For every \(|\lambda|<1\), the operator \(S^m-\lambda I\) is Fredholm of index \(-m\), and compact perturbation preserves that index; hence \(T_m-\lambda I\) cannot be invertible. Its spectrum is therefore the closed disk.

## Verification
The standalone `check_phase_winding.py` performs 1,551 finite checks of the radial gamma identity, integer zero rule, selected norm bounds, high-index asymptotic consistency, and eight independent numerical quadratures. It was executed successfully with Python; the infinite-index theorem is proved by the identities above, not by finite tests. Run `python check_phase_winding.py` from the directory containing that file. The optional `mpmath` package enables numerical quadratures; all rational polynomial checks use the standard library.

## Relationship to prior work
The complex-Hermite true-level decomposition and Toeplitz quantization are established in Keller–Luef (arXiv:1905.07741, first posted 19 May 2019), Hagger (arXiv:2201.10230, first posted 25 January 2022), and Fulsche–Hagger (arXiv:2308.11292, first posted 22 August 2023). Keller–Luef give the Laguerre basis and general semiclassical/symbolic mapping theory. Hagger develops limit-operator Fredholm and compactness criteria. Fulsche–Hagger identify Toeplitz-symbol kernel phenomena. None of the relevant inspected sections provides the exact all-winding complex-Hermite angular matrix coefficient or its even-winding one-channel nullity. The index \(-m\) alone is compatible with existing general Fredholm theory; the distinguishing claim is the **exact additional kernel and cokernel** at every even winding. Babusci–Dattoli–Górska (arXiv:1202.1976) develop general Laguerre integral methods with a different Gaussian-integral setup; broad special-function identities constitute a residual priority risk.

## Limitations
The claim applies only to the true second polyanalytic level and integer positive angular windings. It does not establish a new general Fredholm-index theorem and does not assert that any higher-level or nonconstant radial-symbol analogue has the same parity rule. Historical priority is best-knowledge rather than independently certified; generic integral identities may provide a route to rediscovering the coefficient, but the exact finite-defect conclusion has not been identified as a stated or immediately implied prior result. The finite tests are illustrative, not a completeness proof. No independent audit was performed.

## References
1. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (2019), https://arxiv.org/abs/1905.07741.
2. R. Hagger, *Toeplitz and related operators on polyanalytic Fock spaces*, arXiv:2201.10230 (2022), https://arxiv.org/abs/2201.10230.
3. R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (2023), https://arxiv.org/abs/2308.11292.
4. D. Babusci, G. Dattoli, K. Górska, *Symbolic calculus and integrals of Laguerre polynomials*, arXiv:1202.1976 (2012), https://arxiv.org/abs/1202.1976.
