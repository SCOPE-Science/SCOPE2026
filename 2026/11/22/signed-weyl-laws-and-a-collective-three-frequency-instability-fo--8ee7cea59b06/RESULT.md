# Signed Weyl laws and a collective three-frequency instability for Hardy–Volterra self-commutators

## Finding

Let \(H^2(\mathbb D)\) have orthonormal monomial basis \(e_n(z)=z^n\), \(n\ge0\). For any nonconstant complex polynomial \(g(z)=a_0+\sum_{k=1}^d a_kz^k\), define the Volterra operator and its self-commutator by
\[
(T_gf)(z)=\int_0^z f(w)g'(w)\,dw,\qquad K_g=T_g^*T_g-T_gT_g^*.
\]
Set, for \(|z|=1\),
\[
B(z)=zg'(z)=\sum_{k=1}^d b_kz^k,\quad b_k=ka_k,\qquad C(z)=zB'(z),
\]
and define the real trigonometric polynomial
\[
\sigma_g(\theta)=-2\operatorname{Re}\!\left(\overline{B(e^{i\theta})}\,C(e^{i\theta})\right).
\]
For \(t>0\), let \(N_+(t)\) and \(N_-(t)\) count, with multiplicity, eigenvalues of \(K_g\) respectively greater than \(t\) and less than \(-t\). Then
\[
\boxed{\lim_{t\downarrow0}t^{1/3}N_\pm(t)=\mathcal C_\pm(g):=\frac{1}{2\pi}\int_0^{2\pi}(\pm\sigma_g(\theta))_+^{1/3}\,d\theta.}
\]
The negative constant \(\mathcal C_-(g)\) is always strictly positive. Thus, for \(\mathcal C(g)=\mathcal C_+(g)+\mathcal C_-(g)>0\), the singular values satisfy the **exact** law
\[
\boxed{s_j(K_g)\sim \left(\frac{\mathcal C(g)}j\right)^3\quad(j\to\infty).}
\]
In particular, \(K_g\in\mathcal S_p\) exactly for \(p>1/3\), including quasi-Schatten exponents \(0<p<1\), and
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^N s_j(K_g)^{1/3}=\mathcal C(g).
\]
The positive inertia is infinite whenever \(\max_\theta\sigma_g(\theta)>0\), and finite whenever \(\max_\theta\sigma_g(\theta)<0\). No assertion about its finite/infinite status is made in the critical case \(\max\sigma_g=0\).

The full polynomial family exhibits an effect invisible to all pairwise truncations. With
\[
\boxed{g_*(z)=\frac9{10}z+\frac12z^2+\frac{11i}{30}z^3,}
\]
every two-term polynomial obtained by retaining exactly two nonconstant monomials has **only finitely many positive** self-commutator eigenvalues, but \(K_{g_*}\) has **infinitely many positive and infinitely many negative** eigenvalues, each with a positive cubic Weyl coefficient. This is a collective three-frequency sign instability, not a binomial critical-endpoint effect.

## Assumptions and scope

The space is the usual complex Hardy Hilbert space on the open unit disk with coefficient norm \(\|\sum f_nz^n\|_2^2=\sum|f_n|^2\); integration follows any path in the simply connected disk. Only the nonconstant coefficients of \(g\) matter. The integer \(d\) is finite and at least one of \(a_1,\dots,a_d\) is nonzero; zero coefficients are allowed. The symbols \(\sigma_g\) are real-valued and continuous. The eigenvalue counts are those of the infinite compact self-adjoint operator, not finite-section matrices. The notations \((x)_+=\max(x,0)\) and \(\mathcal S_p\) follow the usual real positive-part and Schatten-class conventions. All limits are for a fixed polynomial \(g\), not uniform over growing degree.

## Proof

**1. Exact weighted-shift representation and trace.** Write \(b_k=ka_k\). For every \(n\ge0\), direct integration gives
\[
T_ge_n=\sum_{k=1}^d\frac{b_k}{n+k}e_{n+k}.
\]
The squared Hilbert–Schmidt norm is exactly
\[
\|T_g\|_{\mathcal S_2}^2=\sum_{k=1}^d|b_k|^2\sum_{n=0}^{\infty}(n+k)^{-2}<\infty.
\]
Consequently \(K_g\) is self-adjoint and trace class with \(\operatorname{tr}K_g=0\). Its matrix is Hermitian and has bandwidth at most \(d-1\) (the nonzero diagonals of \(T_g^*T_g\) and \(T_gT_g^*\) have differences of shift degrees).

**2. Exact tail coefficients and the angular symbol.** For \(n\ge d\), \(0\le j\le d-1\), putting \(b_k=0\) for \(k>d\), the entry in row \(n\), column \(n+j\) is
\[
(K_g)_{n,n+j}=\sum_{\ell=1}^{d-j}b_\ell\overline{b_{\ell+j}}
\left[\frac1{(n+\ell+j)^2}-\frac1{n(n+j)}\right].
\]
The conjugate formula holds for negative offsets. The expansion of the bracket is \(-(2\ell+j)n^{-3}+O_g(n^{-4})\), uniformly over the finitely many offsets. Hence
\[
(K_g)_{n,n+j}=n^{-3}\sigma_j+O_g(n^{-4}),\qquad
\sigma_j=-\sum_{\ell=1}^{d-j}(2\ell+j)b_\ell\overline{b_{\ell+j}}.
\]
Expanding \(-2\operatorname{Re}(\overline B C)\) in exponentials shows that
\[
\sigma_j=\frac1{2\pi}\int_0^{2\pi}\sigma_g(\theta)e^{ij\theta}\,d\theta.
\]
This convention for the Fourier coefficient makes \((T(\sigma_g))_{n,n+j}=\sigma_j\), where \(T(\sigma_g)\) is the self-adjoint Toeplitz compression on the monomial basis.

Put \(D=\operatorname{diag}((n+1)^{-3/2})_{n\ge0}\) and \(A_g=DT(\sigma_g)D\). The preceding expansion and the finite bandwidth show that \(E_g=K_g-A_g\) has a finite initial block followed by entries \(O_g((n+1)^{-4})\) along each of its finitely many diagonals. Truncating its first \(N\) rows and columns changes it by rank at most \(2N\), while the remaining tail has norm \(O_g(N^{-4})\) by the Schur test. Therefore
\[
s_j(E_g)=O_g(j^{-4}),\qquad
N_{|E_g|}(t)=O_g(t^{-1/4}).
\]
Here \(N_{|E|}(t)\) counts singular values greater than \(t\).

**3. Weighted finite-band Toeplitz counting lemma.** We prove the particular compact Weyl lemma needed here, without appealing to an unverified continuum approximation. If \(\sigma\) is any real trigonometric polynomial, then for \(A=DT(\sigma)D\) as above,
\[
\lim_{t\downarrow0}t^{1/3}N_\pm(A;t)
=\frac1{2\pi}\int_0^{2\pi}(\pm\sigma(\theta))_+^{1/3}\,d\theta.
\]
Indeed, put \(r=t^{-1/3}\). Discard the first \(\lfloor\varepsilon r\rfloor\) coordinates, at a possible error of at most \(\varepsilon r+O(1)\) in either eigenvalue count by finite-rank interlacing. For \(R>\|\sigma\|_\infty^{1/3}+1\), the compression to coordinates above \(Rr\) has norm strictly below \(t\), because \(\|D_{>Rr}\|^2\|T(\sigma)\|\le \|\sigma\|_\infty(Rr)^{-3}\). Couplings across either cut have rank bounded solely by the bandwidth; they do not contribute after division by \(r\).

On the remaining index interval \([\varepsilon r,Rr]\), partition into blocks of length about \(\eta r\), where \(\eta>0\) is small after \(\varepsilon,R\) have been fixed. Removing the finitely many inter-block bands costs rank \(O_{\varepsilon,R,\eta}(1)\). On each block, \(D\) differs in norm from its value at the block's left endpoint by at most a relative \(O(\eta/\varepsilon)\); the resulting compression is, to arbitrarily small error in units of \(t\), a scalar multiple of a finite Hermitian Toeplitz section \(T_L(\sigma)\). As \(L\to\infty\), the empirical eigenvalue distribution of \(T_L(\sigma)\) is the distribution of \(\sigma(\theta)\) under normalized arc measure: this follows first for polynomial test functions from the Toeplitz trace identity, since fixed powers differ from the corresponding Fourier-multiplier traces only in \(O(1)\) boundary rows, and then for continuous test functions by uniform approximation. We may approximate the threshold indicator from above and below by continuous functions. The joint boundary \(x^{-3}\sigma(\theta)=\pm1\) has two-dimensional measure zero, so no regular-value assumption is needed, including when \(\sigma\) is constant.

Sending \(r\to\infty\), then \(\eta\downarrow0\), yields the normalized integral over \(\varepsilon\le x\le R\) of the indicator of \(\pm x^{-3}\sigma(\theta)>1\). Finally send \(\varepsilon\downarrow0\) and \(R\to\infty\), using the initial-rank bound and tail-norm bound. Integrating the indicator in \(x\) gives \((\pm\sigma(\theta))_+^{1/3}\), establishing the lemma. This argument also covers sign-changing symbols with zero arcs.

**4. Perturbation stability and spectral consequences.** For compact self-adjoint \(A,E\), the min–max inequalities compare \(N_\pm(A+E;t)\) with \(N_\pm(A;(1\pm\delta)t)\), up to the number of singular values of \(E\) exceeding \(\delta t\), for any fixed \(0<\delta<1\). Since \(t^{1/3}N_{|E_g|}(\delta t)=O_g(t^{1/12})\to0\), step 3 applied to \(A_g\), followed by \(\delta\downarrow0\), gives both displayed signed Weyl limits for \(K_g\).

The mean of the symbol is
\[
\frac1{2\pi}\int_0^{2\pi}\sigma_g(\theta)\,d\theta
=-2\sum_{k=1}^d k|b_k|^2<0,
\]
so \(\sigma_g\) is negative on a nonempty open arc and \(\mathcal C_-(g)>0\). Adding the two signed counts gives \(N_{|K_g|}(t)\sim\mathcal C(g)t^{-1/3}\), which inverts to \(s_j(K_g)\sim(\mathcal C(g)/j)^3\). The quasi-Schatten threshold and logarithmic singular-value residue follow by comparing with \(j^{-3p}\) and the harmonic series. Positive symbol on an open arc forces infinitely many positive eigenvalues by \(\mathcal C_+>0\).

If \(\max\sigma_g=-c<0\), then for any finitely supported \(y\), the Toeplitz quadratic form satisfies \(\langle T(\sigma_g)y,y\rangle\le-c\|y\|^2\). On the remote coordinate tail, conjugating the error matrix by \(D^{-1}\) produces another finite-band matrix of norm \(O_g(N^{-1})\). Thus \(\langle K_gx,x\rangle\le-(c-O_g(N^{-1}))\|Dx\|^2\) on the codimension-\(N\) tail. Taking \(N\) large proves that the positive spectral subspace is finite-dimensional.

**5. Explicit collective instability not seen in any binomial.** For
\[
g_*(z)=\frac9{10}z+\frac12z^2+\frac{11i}{30}z^3,
\quad B_*(z)=\frac9{10}z+z^2+\frac{11i}{10}z^3,
\]
the derivative-coefficient moduli are \(9/10<1<11/10\). Consider any restriction of \(B_*\) to just two monomials with degrees \(\ell<m\) and moduli \(u<v\). Its radial derivative expression satisfies for every \(\theta\)
\[
\operatorname{Re}(\overline{B_{\ell,m}}\,zB_{\ell,m}')
\ge \ell u^2+mv^2-(\ell+m)uv
=(v-u)(mv-\ell u)>0.
\]
Its angular symbol is therefore strictly negative everywhere, so its self-commutator has only finitely many positive eigenvalues by step 4. For the full three-term polynomial, a direct exact trigonometric evaluation at \(\theta=\pi/3\) gives
\[
\operatorname{Re}\bigl(\overline{B_*(e^{i\pi/3})}\,C_*(e^{i\pi/3})\bigr)
=\frac{779-473\sqrt3}{100}<0,
\]
where the strict inequality is equivalently \(3(473)^2>(779)^2\). Hence \(\sigma_{g_*}(\pi/3)=(473\sqrt3-779)/50>0\), so \(\mathcal C_+(g_*)>0\). Step 4 gives infinitely many positive eigenvalues; the universal negative coefficient gives infinitely many negative eigenvalues. This completes the example and theorem.

## Verification

The standalone `verify.py` reconstructs finite Volterra matrices from the exact monomial action, checks interior commutator entries against the infinite-matrix formula, tests scaled leading coefficients and Fourier-symbol conventions for real and complex polynomials, verifies the exact strict trinary sign inequality, and compares finite signed eigenvalue counts against the predicted asymptotic scales. It requires Python 3.10+ and NumPy. Running it with one BLAS thread returned `VERIFICATION_OK 231`. These 231 diagnostics are **finite corroboration**, not proofs of infinite-dimensional eigenvalue-counting limits, spectral inertia, or bibliographic priority. Those follow from the analytical steps above and the literature comparison below.

## Relationship to prior work

Chalmoukis and Stylogiannis, first publicly posted 4 May 2020 as arXiv:2005.01660, prove boundedness and quasinilpotency for generalized Volterra operators on weighted analytic sequence spaces. Their original theorem and its published 2021 full text do not state signed self-commutator Weyl coefficients or pairwise-versus-collective spectral inertia. Aleman–Siskakis and Pau–Peláez provide earlier analytic-function integration-operator and Schatten background; Schatten membership of \(T_g\) does not itself calculate signed eigenvalue counts of \(T_g^*T_g-T_gT_g^*\).

A closely related published calculation, “Critical spectral-inertia transitions for binomial Volterra integration on the Bergman disk” (2026), gives the **two-term** unweighted Bergman criterion for infinitely many positive eigenvalues and two-sided order estimates \(s_j\asymp j^{-3}\). It is not being reasserted here as new. Its statement covers neither arbitrary polynomial symbols on \(H^2\), exact signed angular Weyl coefficients, nor the strict three-term example whose every binomial restriction has finite positive inertia. General Hermitian Toeplitz-section eigenvalue distribution theory supplies a standard ingredient to the proof, not the application-specific third-order symbol cancellation or the collective-trinomial assertion. The proof above includes the required weighted compact Toeplitz counting argument.

## Limitations

This is a fixed-finite-degree polynomial theorem on the unweighted Hardy Hilbert space; it does not assert an extension to arbitrary analytic symbols, varying polynomial degree, or weighted Bergman spaces. The signed limits alone do not decide whether positive inertia is finite or infinite at the critical boundary \(\max\sigma_g=0\). There is no claim of exact individual eigenvalues or an optimal remainder term beyond the leading asymptotic. Historical papers applying general compact pseudodifferential eigenvalue methods might contain an equivalent formulation; bibliographic searches cannot certify uniqueness. Independent verification has not been performed.

## References

1. N. Chalmoukis and G. Stylogiannis, “Quasi-nilpotency of generalized Volterra operators on sequence spaces,” arXiv:2005.01660, first posted 2020-05-04; *Results in Mathematics* **76** (2021), article 173, DOI: 10.1007/s00025-021-01482-7. Full open-access text: https://link.springer.com/article/10.1007/s00025-021-01482-7.
2. A. Aleman and A. G. Siskakis, “Integration operators on Bergman spaces,” *Indiana University Mathematics Journal* **46** (1997), 337–356, DOI: 10.1512/iumj.1997.46.1373.
3. J. Pau and J. A. Peláez, “Schatten classes of integration operators on Dirichlet spaces,” arXiv:1302.2417, first posted 2013-02-11, https://arxiv.org/abs/1302.2417.
4. “Critical spectral-inertia transitions for binomial Volterra integration on the Bergman disk,” publicly recorded 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-critical-spectral-inertia-transitions-for-binomial-volterra-inte--ce14ed846aa0. Directly relevant published comparison; full `RESULT.md` inspected.
5. A. Böttcher and S. M. Grudsky, *Spectral Properties of Banded Toeplitz Matrices*, SIAM (2005), chapter 11, DOI: 10.1137/1.9780898717853.ch11. Background on finite Toeplitz spectral distribution; the weighted compact counting lemma is proved here.
