# Cubic boundary jets produce a sharp weak-trace tangent for Hardy composition differences

## Finding
In the classical Hardy Hilbert space \(H^2(\mathbb D)\) let \(\varphi(z)=(1+z)/2\), \(h(z)=(1-z)^3\), and \(\psi_\varepsilon=\varphi+\varepsilon h\). For every complex \(\varepsilon\) with \(|\varepsilon|\le1/100\), \(\psi_\varepsilon\) maps \(\mathbb D\) into itself. The curve of composition operators \(C_{\psi_\varepsilon}-C_\varphi\) is differentiable at zero in the Hilbert–Schmidt norm, and its derivative is the compact operator
\[
(Af)(z)=(1-z)^3f'((1+z)/2).
\]
Its squared Hilbert–Schmidt norm is exactly \(96\). More significantly, with the singular values in nonincreasing order (starting with \(s_1\)),
\[
\lim_{n\to\infty}n\,s_n(A)=\frac{32\sqrt2}{\pi}.
\]
Thus \(A\in\mathcal S_p\) exactly for \(p>1\), and the endpoint logarithmic mean has the exact coefficient
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(A)=\frac{32\sqrt2}{\pi}.
\]
The endpoint statement refers to the tangent, not to an asserted exact singular-value law for any fixed nonzero difference.

## Assumptions and scope
All operators act on the complex Hilbert space \(H^2(\mathbb D)\) with \(\{z^n:n\ge0\}\) orthonormal. Only complex perturbations \(|\varepsilon|\le1/100\) and the cubic direction \(h(z)=(1-z)^3\) are covered. The derivative at \(\varepsilon=0\) is in the Hilbert–Schmidt (not merely strong or weak operator) norm. \(\mathcal S_p\) denotes the Schatten ideal of compact operators having \(\sum_n s_n^p<\infty\); the weak trace class designation means \(\sup_n n s_n<\infty\).

## Proof
**1. Genuine disk self-maps and differentiation.** On \(|z|=1\), put \(u=\sin^2(\arg z/2)\). Then \(|\varphi(z)|^2=1-u\) and \(|h(z)|=8u^{3/2}\), so
\[
|\psi_\varepsilon(z)|^2\le 1-[1-16|\varepsilon|-64|\varepsilon|^2]u<1
\]
for \(z\ne1\) and the stipulated \(\varepsilon\); the maximum principle yields a disk self-map. Also \(C_{\psi_\varepsilon}\) is bounded on \(H^2\) by the standard Littlewood subordination theorem. On monomials, \(\varepsilon^{-1}(C_{\psi_\varepsilon}-C_\varphi)z^n\to n h\varphi^{n-1}\). The bound
\[
\left|\frac{\psi_\varepsilon(z)^n-\varphi(z)^n}{\varepsilon}\right|
\le n|h(z)|\max(|\psi_\varepsilon(z)|,|\varphi(z)|)^{n-1}
\]
implies a uniform integrable majorant of the sum of squared boundary moduli over \(n\): with \(c=1-16/100-64/10000>0\), it is no larger than \(64u^3(2-cu)/(cu)^3\). Dominated convergence for boundary integration and the monomial basis gives differentiation in \(\mathcal S_2\) and identifies \(A\). Directly,
\[
\|A\|_{\mathcal S_2}^2=\int_{\mathbb T}|h|^2\sum_{n\ge1}n^2|\varphi|^{2n-2}\,dm
=64\int_{\mathbb T}(2-u)dm=96.
\]
Here \(m\) is normalized arc length and \(\int u\,dm=1/2\).

**2. Exact Volterra reduction.** The Cayley map \(w=(1+z)/(1-z)\) and Hardy-space unitary \((Uf)(w)=\sqrt2\,f((w-1)/(w+1))/(w+1)\) give, by differentiation,
\[
(UAU^{-1}F)(w)=\frac{16}{(w+1)^2}F(2w+1)+\frac{32}{w+1}F'(2w+1).
\]
Under the Laplace realization \(F(w)=\int_0^\infty e^{-wt}g(t)\,dt\) of right-half-plane \(H^2\), the corresponding \(L^2(0,\infty)\) kernel is
\[
(\widetilde Ag)(t)=16e^{-t}\int_0^{t/2}(t-4u)e^u g(u)\,du.
\]
The unitary output dilation \((Df)(x)=\sqrt2 f(2x)\) turns this into
\[
(DA_{\!L}g)(x)=32\sqrt2\,\bigl[-Tg(x)+Rg(x)\bigr],
\quad Tg(x)=e^{-2x}\int_0^x ue^ug(u)\,du,
\quad Rg(x)=e^{-2x}\int_0^x(x-u)e^ug(u)\,du.
\]
All normalizing constants cancel under these unitary identifications. In particular \(s_n(A)=32\sqrt2\,s_n(-T+R)\).

**3. The remainder is trace class.** Write \(Vf(x)=\int_0^x f(u)\,du\), interpreted only inside the exponentially weighted products. Then \(R=(M_{e^{-2x}}VM_{e^{3x/2}})(M_{e^{-3x/2}}VM_{e^x})\). Both parentheses are Hilbert–Schmidt with squared norms \(1/4\) and \(1/3\), respectively, by direct integration of their triangular kernels. Hence \(R\in\mathcal S_1\) and \(n s_n(R)\to0\).

**4. Weyl law for \(T\).** The operator \(T\) is Hilbert–Schmidt, injective, and has dense range; its adjoint is injective because the tail integral \(\int_u^\infty e^{-2x}g(x)\,dx\) can vanish almost everywhere only for \(g=0\). Writing \(f=Tg=e^{-2x}y(x)\) gives \(g(x)=e^{-x}y'(x)/x\). Thus inverse squared singular values are the positive eigenvalues \(\mu_n=s_n(T)^{-2}\) of the closed quadratic-form problem
\[
-\frac{d}{dx}\left(\frac{e^{-2x}}{x^2}\frac{dy}{dx}\right)
=\mu\,e^{-4x}y,\qquad x>0,
\]
with the Friedrichs boundary realization determined by the inverse form \(\int_0^\infty e^{-2x}|y'|^2/x^2\,dx\) and norm \(\int_0^\infty e^{-4x}|y|^2\,dx\). For completeness, smooth compactly supported \(y\) form a core: starting with a compactly supported smooth \(g\), cancel its weighted moment \(\int_0^\infty ue^ug(u)\,du\) using a smooth compensator supported near \(x=L\); the compensator's \(L^2\) norm tends to zero as \(L\to\infty\), because the moment functional has exponentially increasing size there. After cancellation, \(y(x)=\int_0^x ue^ug(u)\,du\) is compactly supported. Density of smooth compactly supported \(g\) proves the core assertion.

Set
\[
\xi=1-(1+x)e^{-x}\in(0,1),\qquad
v(\xi)=\frac{e^{-3x/2}}{\sqrt x}\,y(x).
\]
This is a unitary Liouville transformation in the weighted spaces, and the Friedrichs form becomes the Schrödinger form of \(-d^2/d\xi^2+Q(\xi)\), where
\[
Q(\xi)=\frac{(3x^2+10x+5)e^{2x}}{4x^4}>0.
\]
Indeed \(d\xi/dx=xe^{-x}\), and differentiating \(e^{-3x/2}/\sqrt x\) twice in \(\xi\) yields the displayed potential. By core closure, the form is Dirichlet at both ends in the Friedrichs sense. Its length is exactly one. Positivity of \(Q\) and the Dirichlet min–max principle give \(\mu_n\ge\pi^2n^2\). For each \(0<\eta<1/2\), trial spaces of the first \(n\) Dirichlet eigenfunctions supported on \([\eta,1-\eta]\) give
\[
\mu_n\le\frac{\pi^2n^2}{(1-2\eta)^2}+\sup_{\eta\le\xi\le1-\eta}Q(\xi).
\]
First let \(n\to\infty\), then \(\eta\downarrow0\), to deduce \(\mu_n\sim\pi^2n^2\), or \(n s_n(T)\to1/\pi\).

**5. Endpoint stability.** Ky Fan inequalities \(s_{n+k-1}(X+Y)\le s_n(X)+s_k(Y)\), applied in both directions with \(k\) asymptotic to \(\eta n\), show that adding a trace-class \(Y\) leaves an asymptotic \(s_n(X)\sim c/n\) unchanged: \(ks_k(Y)\to0\), and \(\eta\downarrow0\) removes the index shift. Apply with \(X=-T\), \(Y=R\) and the factor \(32\sqrt2\). The stated \(\mathcal S_p\), weak ideal, and logarithmic-mean conclusions then follow from the resulting strictly positive \(1/n\) coefficient.

## Verification
The boundary monomial identity gives an independent exact check \(\|A\|_{\mathcal S_2}^2=96\); direct integration of the transformed Volterra kernel gives the same value. The triangular-factor squared Hilbert–Schmidt norms are exactly \(1/4\) and \(1/3\). Symbolic differentiation independently confirms \(Q=(3x^2+10x+5)e^{2x}/(4x^4)\). The standalone `verify.py` uses exact rational arithmetic for the monomial column formula and exact rational evaluation of the transformed kernel moments. Finite sections or numerical approximations alone cannot establish the infinite singular-value limit; Steps 3–5 provide that proof.

## Relationship to prior work
Allen, Heller and Pons (2022, arXiv:2207.12635) analyze compact differences on weighted Dirichlet spaces and show why boundary jets matter; the present object is a Hilbert–Schmidt tangent of a concrete Hardy composition-difference curve, not a claim about their weighted Dirichlet classification. Acharyya and Wu (2017) provide comparability formulas for Hilbert–Schmidt differences of weighted composition operators, but not an exact individual singular-value asymptotic or endpoint logarithmic coefficient. Allen, Heller and Pons (2022, arXiv:2207.09015) analyze composition–differentiation operators on the Dirichlet space, with different domain and unweighted derivative. Standard one-dimensional Sturm–Liouville spectral asymptotics motivate the approach, but the exact Hardy-to-Volterra conjugacy, length, and remainder control are shown here. Published mathematical-record matches concern affine symbols on lacunary Hardy spaces, strictly contracting composition–differentiation symbols, and different Volterra companions; their reported conclusions do not imply this precise coefficient. An exhaustive historical-priority determination has not been independently established.

## Limitations
The sharp \(1/n\) law is only for the derivative \(A\) at zero; it is not established for the fixed nonzero operators \(C_{\psi_\varepsilon}-C_\varphi\). No independent proof audit is claimed. Earlier related abstract frameworks might yield the result after a nontrivial reduction; the priority assessment uses inspected sources and is not a formal proof of novelty.

## References
- R. F. Allen, K. Heller, M. A. Pons, *Compact differences of composition operators on weighted Dirichlet spaces*, arXiv:2207.12635 (first posted 26 July 2022), https://arxiv.org/abs/2207.12635.
- R. F. Allen, K. Heller, M. A. Pons, *Composition-differentiation operators on the Dirichlet space*, arXiv:2207.09015 (first posted 19 July 2022), https://arxiv.org/abs/2207.09015.
- S. Acharyya and Z. Wu, *Compact and Hilbert–Schmidt Differences of Weighted Composition Operators*, Integral Equations and Operator Theory (2017), DOI:10.1007/s00020-017-2374-x, https://doi.org/10.1007/s00020-017-2374-x.
- W. Yang and C. Yuan, *Schatten class composition operators on the Hardy space*, Proceedings of the Royal Society of Edinburgh A (online 24 July 2023), https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/abs/schatten-class-composition-operators-on-the-hardy-space/946FD41322692349BB9BA4B62C91BC93.
