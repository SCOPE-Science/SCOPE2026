# Quasi-Schatten classification for separated signed atomic Fock dipoles

## Finding
On normalized Gaussian Fock space, an infinite signed atomic form built from widely separated pairs of nearby point evaluations has a sharp Schatten classification despite potentially unbounded positive and negative parts. More precisely, fix real \(x_j=20j\), \(j\ge1\), displacements \(0<\delta_j<1\), and positive weights \(w_j\), and let \(k_x(z)=\exp(zx-x^2/2)\) be normalized coherent kernels. On the polynomial core define
\[
 B(f,g)=\sum_{j\ge1}w_j\bigl(\langle f,k_{x_j}\rangle\langle k_{x_j},g\rangle-\langle f,k_{x_j+\delta_j}\rangle\langle k_{x_j+\delta_j},g\rangle\bigr).
\]
Assume the weights grow at most polynomially and that \(\sup_j a_j<\infty\), where \(a_j=w_j\sqrt{1-e^{-\delta_j^2}}\). Then the form has a bounded operator extension, which is compact if and only if \(a_j\to0\), and for every \(0<p<\infty\), belongs to \(\mathcal S_p\) if and only if \(\sum_j a_j^p<\infty\). In the compact case, if \(d_1\ge d_2\ge\cdots\) rearranges the multiset \(\{a_j,a_j:j\ge1\}\), then
\[
\tfrac12 d_n\le s_n(T_B)\le\tfrac32d_n \quad(n\ge1).
\]
For \(w_j=j\), \(\delta_j=(j+1)^{-4}\), this gives \(T_B\in\mathcal S_p\) exactly for \(p>1/3\), while neither positive nor negative atomic part defines a bounded positive operator.

## Assumptions and scope
The Fock space consists of entire functions with \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\), and the scalar product is linear in its first entry. Here \(k_x\) has norm one and \(\langle k_x,k_y\rangle=e^{-(x-y)^2/2}\) for real \(x,y\). The signed distribution underlying the form is the locally finite real Borel measure \(\pi\sum_{j\ge1}w_j(\delta_{x_j}-\delta_{x_j+\delta_j})\) with the convention that the measure appears inside the Gaussian-weighted planar integral divided by \(\pi\). Its *formal positive and negative terms are paired before summation*. For general Hilbert-space inputs separate positive and negative integrals need not converge; the assertion is about the bounded sesquilinear-form extension, not an everywhere absolutely convergent measure integral.

## Proof
Set \(u_j=k_{x_j}\), \(c_j=e^{-\delta_j^2/2}\), \(q_j=\sqrt{1-c_j^2}\), and \(v_j=(k_{x_j+\delta_j}-c_ju_j)/q_j\). Each pair \((u_j,v_j)\) is orthonormal. Let \(V:\ell^2(\mathbb N;\mathbb C^2)\to\mathcal F^2\) be synthesis of these pairs.

**Uniform separated-pair lemma.** For all choices \(0<\delta_j<1\), the Gram matrix satisfies \(\|V^*V-I\|\le1/2\). To prove this, use the explicit real coherent overlap \(F(x,y)=e^{-(x-y)^2/2}\). For \(0<d<1\),
\[
 v_{x,d}=\frac{d}{\sqrt{1-e^{-d^2}}}\int_0^1\partial_x k_{x+td}\,dt+\frac{1-e^{-d^2/2}}{\sqrt{1-e^{-d^2}}}k_x.
\]
The two coefficients are bounded respectively by \(4/3\) and \(1/2\), and \(\partial_xF=-(x-y)F\), \(\partial_yF=(x-y)F\), \(\partial_x\partial_yF=(1-(x-y)^2)F\). Thus, whenever \(|x-y|=20m\), \(m\ge1\), **each** cross-pair Gram entry has modulus at most \(10[1+(20m+2)^2]\exp(-(20m-2)^2/2)\). Each of the two rows meets two columns at each remote pair, so Schur's row-and-column bound gives
\[
\|V^*V-I\|\le40\sum_{m\ge1}[1+(20m+2)^2]e^{-(20m-2)^2/2}<1/2.
\]
(The displayed numerical inequality follows already by comparison with a geometric series of ratio \(e^{-200}\), after its first term.) Hence \(\frac12I\le V^*V\le\frac32I\).

The matrix of the \(j\)-th dipole \(w_j(P_{u_j}-P_{k_{x_j+\delta_j}})\) in its pair basis is
\[
 D_j=w_j\begin{pmatrix}q_j^2&-c_jq_j\\-c_jq_j&-q_j^2\end{pmatrix}.
\]
It has two singular values exactly \(a_j=w_jq_j\), because \(D_j^2=a_j^2I_2\). Write \(D=\bigoplus_jD_j\). When \(\sup_j a_j<\infty\), the bounded operator \(T=VDV^*\) agrees with the polynomial-core form: all terms converge absolutely for polynomials due to Gaussian decay and polynomial weight growth, and the finite block operators converge strongly to \(T\).

The map \(V\) has closed range, and its polar decomposition is \(V=U(V^*V)^{1/2}\) where \(U\) is an isometry. Thus nonzero singular values of \(T\) are those of \((V^*V)^{1/2}D(V^*V)^{1/2}\). The ideal property of singular values applied in both directions to the invertible factor \((V^*V)^{1/2}\) proves the displayed two-sided bounds. The same factorization gives the compactness criterion and every Schatten membership criterion, including \(0<p<1\).

For the example, \(\sqrt{1-e^{-\delta_j^2}}\sim\delta_j\), so \(a_j\sim j^{-3}\). The positive part evaluated on \(k_{x_j}\) contributes at least \(w_j=j\), so its operator form is unbounded; likewise the negative part evaluated at \(k_{x_j+\delta_j}\) contributes \(j\). This proves the contrasting assertions.

## Verification
Run `python check.py` with Python 3 standard library. It verifies the exact two-by-two block eigenvalue identities, finite separated-pair Gram entries, and the explicit uniform Schur-tail inequality. Expected output: `SIGNED_FOCK_DIPOLE_FINITE_CHECK_OK 507`. These finite checks corroborate, but do not prove, the infinite theorem; the analytical Gaussian-derivative estimate and polar-decomposition argument supply that proof.

## Relationship to prior work
Dileep–Fang–Tien [1] characterize *positive* Gaussian Fock Toeplitz forms by local masses and the Berezin profile. Their positivity assumption excludes cancellation in a signed pair, and their theorems do not characterize Schatten quasi-ideals for such signed forms. Rozenblum–Vasilevski [2] introduce a broad sesquilinear-form framework for highly singular Fock symbols and show that compact operators can have generalized Toeplitz representations; this framework does not specify the sharp separated-dipole singular-value criterion or the example with individually unbounded positive parts. Fulsche [3] studies signed measures whose **total variation** is Fock-Carleson; this excludes the example with \(w_j=j\). The theorem is a concrete spectral criterion within a narrower atomic subclass, not a claim of an entirely new general definition of Toeplitz operators.

## Limitations
The pair separation is a fixed explicit sufficient condition, not claimed optimal. The proof assumes polynomial-growth coefficients to define a polynomial-core form and explicitly paired summation. In the example, an integral against the signed measure is not absolutely defined for all Fock functions. All general Schatten statements use the sesquilinear extension. No exact singular-value constants or assertions for arbitrary signed measures are claimed. No independent audit or publication-priority determination has been performed.

## References
[1] D. K. Dileep, X. Fang, and P. T. Tien, *Positive Toeplitz Operators Between Gaussian Mixed-Norm Fock Spaces*, arXiv:2610.40236v1 (first publicly posted 2026-10-29), https://arxiv.org/html/2610.40236v1 .

[2] G. Rozenblum and N. Vasilevski, *Toeplitz operators defined by sesquilinear forms: Fock space case*, arXiv:1405.5767 (2014), https://arxiv.org/abs/1405.5767 .

[3] R. Fulsche, *Essential positivity for Toeplitz operators on the Fock space*, *Integral Equations and Operator Theory* 96, 21 (2024), DOI 10.1007/s00020-024-02770-x, https://link.springer.com/article/10.1007/s00020-024-02770-x .
