# Exact Gaussian-symbol spectral transition for two-parameter Fock operators

## Finding
Let \(\mathcal F^2\) be the one-variable Bargmann–Fock space with Gaussian measure \(d\lambda(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). Fix real \(s>0\), \(t>0\) with \(H=s^2-t^2>1\), and a real exponent \(\beta<1\). Set \(r=1-\beta\), \(\eta=t(H-1)/s\), and
\[
\beta_* =1-\sqrt{\frac{1+\eta}{H}},\qquad Q=\frac1{r^2H},\quad P=-\eta Q,\quad D=\frac1{r^2\sqrt H}.
\]
Define initially on finite linear combinations of reproducing kernels the Gaussian-symbol Toeplitz-type integral operator
\[
(A_\beta f)(z)=\frac1{\sqrt s}\int_{\mathbb C}\exp\!\left(\frac{tz^2-t\bar w^2+2z\bar w}{2s}\right)e^{\beta|w|^2}f(w)\,d\lambda(w).
\]
Then \(0<\beta_*<1\), and the following is an exact three-regime classification.

**Compact regime:** If \(\beta<\beta_*\), \(A_\beta\) is compact, belongs to every Schatten class, and all its singular values, in decreasing order, are
\[
s_n(A_\beta)=\sqrt{\frac{D}{\sqrt{1-Ph}}}\left(\frac{Q}{1-Ph}\right)^{n/2},\qquad n=0,1,2,\ldots,
\]
where \(h\in(-1,0)\) is the unique root of
\[
(h-P)(1-Ph)=hQ^2.
\]
In particular, if \(q=Q/(1-Ph)\), then \(0<q<1\) and \(\|A_\beta\|_{\mathcal S_p}=\sqrt{D/\sqrt{1-Ph}}\,(1-q^{p/2})^{-1/p}\) for every \(p>0\).

**Critical regime:** If \(\beta=\beta_*\), \(A_\beta\) remains bounded but is not compact. Under the unitary Bargmann transform \(\mathcal B:L^2(\mathbb R)\to\mathcal F^2\),
\[
A_{\beta_*}^*A_{\beta_*}=\mathcal B\,M_{r^{-1}e^{-c x^2}}\,\mathcal B^{-1},\qquad c=\frac{1-Q}{Q}=\eta>0.
\]
Thus \(\|A_{\beta_*}\|=r^{-1/2}\), the spectrum of \(|A_{\beta_*}|\) is \([0,r^{-1/2}]\), and it has no eigenvalues.

**Unbounded regime:** For \(\beta_*<\beta<1\), the defining operator on reproducing-kernel combinations has no bounded extension to \(\mathcal F^2\).

For example, with \((s,t)=(2,1)\), the exact transition is \(\beta_*=1-\sqrt{2/3}\); at this value, \(A^*A\) is unitarily equivalent to \(\sqrt{3/2}\,M_{e^{-x^2}}\). The sharp Gaussian-symbol transition strictly exceeds the universal sufficient growth threshold \(\beta_0=(H-1)/(2s(s+t))\), but its numerical location was already implicit in a published coherent-state calculation; the new assertions are the complete boundedness/compactness classification, exact subcritical singular spectrum, and critical continuous spectral model.

## Assumptions and scope
The kernel is the two-parameter Fock kernel of Dong–Wang–Zhu; parameters here are **real** with \(t>0\) and \(s^2>t^2+1\). The positive radial symbol is exactly \(\varphi_\beta(w)=e^{\beta|w|^2}\). The integral on each kernel vector is absolutely convergent for every real \(\beta<1\), and its image belongs to \(\mathcal F^2\). The singular-value formula applies only below the transition; the endpoint has continuous, rather than discrete, nonzero spectral values. The case \(t=0\), excluded from the main assertion, has a scalar identity rather than a nontrivial multiplication operator at the transition.

## Proof
Let \(K_w(z)=e^{z\bar w}\). Gaussian integration, initially for \(f=K_w\), gives
\[
(A_\beta K_w)(z)=\frac1{r\sqrt s}\exp\!\left(\frac{t}{2s}z^2+\frac{z\bar w}{sr}-\frac{t\bar w^2}{2sr^2}\right).
\]
This is an entire Fock function because \(0<t/s<1\). Taking its Gram inner product against \(A_\beta K_z\), then evaluating the elementary real two-dimensional Gaussian integral, yields the positive Gram kernel
\[
L(z,w)=\langle A_\beta K_w,A_\beta K_z\rangle
=D\exp\!\left[\frac P2(z^2+\bar w^2)+Qz\bar w\right],
\]
with the coefficients displayed in the finding. This identity holds as a positive quadratic form on the dense linear span of reproducing kernels, whether or not \(A_\beta\) has a bounded extension.

For \(Q-P<1\), i.e. \(r^2>(1+\eta)/H\), the quadratic form defines a positive trace-class operator \(B=A_\beta^*A_\beta\). Indeed the diagonal integral is finite:
\[
\operatorname{tr}B= D\int_{\mathbb C}\exp\!\left[(Q-1)|z|^2+P\operatorname{Re}(z^2)\right]\,\frac{dA(z)}\pi
=\frac{D}{\sqrt{(1-Q)^2-P^2}}.
\]
The inequality \(Q-P<1\) also implies \(|P|+Q<1\), since \(P<0\). The quadratic equation for \(h\) has exactly one root in \((-1,0)\): the function \(P+hQ^2/(1-Ph)-h\) changes sign between \(-1\) and \(0\), and its derivative is \(Q^2/(1-Ph)^2-1<0\) there. Put \(q=Q/(1-Ph)\) and \(C=P/[2(1-Ph)(q^2-1)]\). The quadratic equation implies \(0<q<1\) and \(C=-h/[2(1-h^2)]\). Define the generating functions
\[
\Phi_u(z)=\exp\!\left(\frac h2 z^2+uz+Cu^2\right),\qquad u\in\mathbb C.
\]
A second Gaussian integration proves the *exact* generating relation
\[
B\Phi_u=\frac{D}{\sqrt{1-Ph}}\,\Phi_{qu}.
\]
Moreover
\[
\langle\Phi_u,\Phi_v\rangle=\frac1{\sqrt{1-h^2}}\exp\!\left(\frac{u\bar v}{1-h^2}\right).
\]
Consequently the Taylor coefficients of \(\Phi_u\) in \(u\) form mutually orthogonal nonzero eigenvectors with eigenvalues \(\lambda_n=[D/\sqrt{1-Ph}]q^n\). They are complete: if an Fock vector is orthogonal to every polynomial times \(e^{hz^2/2}\), then the corresponding entire Gaussian generating pairing vanishes identically, forcing that vector to be zero. The trace integral equals \(\sum_{n\ge0}\lambda_n\) (also follows algebraically from the quadratic relation), excluding any additional positive eigenvalues. Taking square roots yields the stated singular spectrum and Schatten norms.

At the threshold, \(Q-P=1\), hence \(P=Q-1\), \(0<Q<1\), and \(c=(1-Q)/Q=\eta\). The standard unitary Bargmann transform is
\[
(\mathcal B f)(z)=\pi^{-1/4}\int_{\mathbb R}e^{-x^2/2+\sqrt2 xz-z^2/2}f(x)\,dx.
\]
Direct Gaussian integration gives the kernel of \(\mathcal B M_{e^{-cx^2}}\mathcal B^{-1}\):
\[
\sqrt Q\exp\!\left[\frac{Q-1}{2}(z^2+\bar w^2)+Qz\bar w\right].
\]
Comparing with \(L\) and observing \(D/\sqrt Q=1/r\) proves the critical operator equality as quadratic forms, hence bounded extensions by density. The essential range of \(r^{-1}e^{-cx^2}\) is \([0,r^{-1}]\), with no positive-measure level sets because \(c>0\). This proves boundedness, noncompactness, norm, and absence of point spectrum for \(|A|\).

Finally, above threshold \(Q-P>1\). For the normalized kernel vector \(k_{iy}=e^{-y^2/2}K_{iy}\), the exact Gram formula gives
\[
\|A_\beta k_{iy}\|^2=D\exp\!\left[(Q-P-1)y^2\right]\longrightarrow\infty\quad(y\to\infty).
\]
No bounded extension is possible. Since \(0<\beta_0<1/2\) and \(r_*^2=1-2\beta_0\), the endpoint equals \(\beta_*=1-\sqrt{1-2\beta_0}>\beta_0\), as claimed.

## Verification
The proof uses exact Gaussian integrals and operator identities, not finite truncation. Checks for \((s,t)=(2,1)\) give \(H=3\), \(\eta=1\), \(P=-Q\), and \(r_*^2=2/3\). At \(\beta=0\), the eigenvalues of \(A^*A\) are \(\frac{\sqrt5-1}{2}\left(\frac{3-\sqrt5}{2}\right)^n\), consistent with the independent canonical-operator formula in Dong–Zhu (2025). The Hilbert–Schmidt identity \(\sum\lambda_n=D/\sqrt{(1-Q)^2-P^2}\) follows both from the eigenvalue sum and from direct Gaussian integration. The endpoint identification is an exact operator equality, not an extrapolation of subcritical eigenvalues.

## Relationship to prior work
Dong, Wang, and Zhu (2026, arXiv:2610.24318v1) introduce the same Toeplitz-type operators and establish a universal growth bound \(\beta_0\), together with boundedness, compactness, and all-Schatten sufficiency below that universal bound. **Their Proposition 14 already identifies \(\beta_*=1-\sqrt{1-2\beta_0}\) as the precise obstruction threshold for uniform normalized coherent-state norms for radial exponentials**; it does not identify sufficiency for boundedness or compactness of this radial family, nor diagonalize the singular spectrum or the endpoint. Their Corollary 16 completely treats radial exponentials only on the unitary parameter boundary \(s^2=t^2+1\), whereas the present classification concerns the strict compact canonical region. Dong and Zhu (2025, arXiv:2509.16672v1, Theorem A) obtain all singular values for the **unweighted** canonical operator \(\beta=0\); our formula agrees at that parameter but the unequal squeezing coefficients for \(\beta\ne0\) place the Gaussian-symbol family outside that two-parameter canonical kernel. Classical Gaussian–Hermite/Mehler diagonalization underlies the mechanism; no independent priority is asserted for that general technique.

## Limitations
Only real \(s,t\) with \(t>0\), \(s^2>t^2+1\), radial exponential symbols, and Hilbert Fock space are treated. In particular this does not establish the same parameter threshold for complex \(s,t\), arbitrary symbols of the same growth, or non-Hilbert Fock norms. The source's known coherent-state threshold is expressly **not** claimed as a new numerical result. General oscillator-semigroup theory could subsume the spectral mechanism; the genuinely model-specific content is the exact radial-family sufficiency, all singular values and the noncompact critical multiplication model. Independent validation is not supplied.

## References
1. X. Dong, Z. Wang, K. Zhu, *Two-parameter Toeplitz-type operators between Fock spaces*, arXiv:2610.24318v1 (first public October 16, 2026), especially Proposition 14, Corollary 16, Theorem B and Section 5. https://arxiv.org/html/2610.24318v1
2. X. Dong, K. Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672v1 (2025), especially Theorem A. https://arxiv.org/pdf/2509.16672
3. X. Dong, K. Zhu, *Canonical integral operators on the Fock space*, arXiv:2208.06214 (2022; Math. Z. 2024). https://arxiv.org/abs/2208.06214
4. V. Bargmann, *On a Hilbert space of analytic functions and an associated integral transform I*, Comm. Pure Appl. Math. 14 (1961), 187–214.
