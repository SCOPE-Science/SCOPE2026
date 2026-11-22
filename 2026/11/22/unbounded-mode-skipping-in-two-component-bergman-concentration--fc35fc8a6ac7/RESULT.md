# Unbounded mode skipping in two-component Bergman concentration

## Finding
Let \(A^2(\mathbb D)\) be the analytic Bergman Hilbert space for normalized planar area, and let \(T_E=P_{A^2}M_{\mathbf1_E}\) be concentration on a radial set \(E\). For the **two-component** masks
\[
E_a=\{z\in\mathbb D:|z|^2\in[0,a]\cup[3/4,7/8]\},\qquad 0\le a<3/4,
\]
there is a unique \(\alpha\in(3/20,151/1000)\) satisfying
\[
\alpha-\alpha^5=4935/32768.
\]
The exact operator norm and **complete top eigenspace** are
\[
\|T_{E_a}\|=\max\{a+1/8,\ a^5+9031/32768\},
\]
with unique maximizing monomial degree \(4\) for \(a<\alpha\), unique maximizing degree \(0\) for \(a>\alpha\), and exactly the two-dimensional space \(\operatorname{span}\{1,z^4\}\) at equality. No degree \(1,2,3\), or degree at least \(5\), ever maximizes. Thus increasing a connected central observation disk can cause a **direct four-degree jump**, with no intermediate winning monomial.

More generally, arbitrarily large jumps occur with only two radial components. For every sufficiently large integer \(M\), set
\[
R_M=2^{1/(M+1/2)},\quad h_M=\frac{R_M-1}{2R_M-1},\quad b_M=1-2h_M,\quad c_M=1-h_M,
\]
and \(\mu_n(M)=c_M^{n+1}-b_M^{n+1}\). There is a unique \(a_M\in(0,1/3)\) satisfying
\[
a_M-a_M^{M+1}=\mu_M(M)-h_M.
\]
For \(E_M=\{z: |z|^2\in[0,a_M]\cup[b_M,c_M]\}\), the top eigenvalue has multiplicity exactly two, with eigenspace \(\operatorname{span}\{1,z^M\}\); every other monomial eigenvalue is strictly smaller. One has \(h_M\sim(\log2)/M\) and \(a_M\to1/4\). In a neighborhood of \(a_M\) with the outer annulus fixed, the unique maximizing degree switches directly from \(M\) to zero as the inner radius-squared crosses \(a_M\).

## Assumptions and scope
The normalized Bergman inner product is \(\langle f,g\rangle=\pi^{-1}\int_{\mathbb D}f(z)\overline{g(z)}\,dA(z)\); an orthonormal monomial basis is \(e_n(z)=\sqrt{n+1}\,z^n\), \(n=0,1,2,\ldots\). The masks are characterized by **squared** radii, not ordinary radii. Intervals may share endpoints, which have zero area. All operators are positive, self-adjoint and compact because the largest squared radius is strictly below one. The theorem concerns the maximizing eigenspace, not an arbitrary ordering of all eigenvalues or a connected mask.

## Proof
**1. Exact diagonalization.** Radial integration gives, for any finite union \(S\subset[0,1)\) of squared-radius intervals and \(E=\{|z|^2\in S\}\),
\[
T_Ee_n=\lambda_ne_n,\qquad \lambda_n=(n+1)\int_S t^n\,dt.
\]
For \(S=[0,a]\cup[b,c]\),
\[
\lambda_n(a;b,c)=a^{n+1}+c^{n+1}-b^{n+1}=a^{n+1}+\mu_n.
\]
Since \(\lambda_n\to0\), the largest eigenvalue equals the operator norm, and equality of maximizing degrees is equality of the associated monomial eigenvalues.

**2. A complete finite-parameter diagram.** Fix \(b=3/4\), \(c=7/8\), and \(\mu_n=c^{n+1}-b^{n+1}\). Its successive differences are
\[
\mu_{n+1}-\mu_n=\frac14(3/4)^{n+1}-\frac18(7/8)^{n+1}.
\]
They are strictly positive precisely when \(2(6/7)^{n+1}>1\); in particular they are positive for \(n=0,1,2,3\) and negative for every integer \(n\ge4\). Thus \(\mu_4=9031/32768\) is the unique peak, while \(\mu_0=1/8\), and \(\mu_4-\mu_0=4935/32768\). Since \(a<1\), for every \(n\ge5\) both \(a^{n+1}<a^5\) (unless \(a=0\), when equality holds) and \(\mu_n<\mu_4\); hence \(\lambda_n<\lambda_4\).

Put \(d=4935/32768\). The function \(H(a)=a-a^5\) is strictly concave on \((0,3/4)\), satisfies \(H(0)=0<d\), \(H(3/4)>d\), and therefore crosses the level \(d\) exactly once in \((0,3/4)\): its superlevel set is an interval containing the right endpoint, and the derivative at the first crossing is positive. Exact rational substitution gives \(H(3/20)<d<H(151/1000)\), locating the unique crossing \(\alpha\).

For \(n=1,2,3\), the function \(a-a^{n+1}\) is increasing on \([0,151/1000]\). The exact inequalities
\[
3/20-(3/20)^{n+1}>\mu_n-\mu_0\qquad(n=1,2,3)
\]
therefore prove \(\lambda_0(\alpha)>\lambda_n(\alpha)\). For \(0\le a\le\alpha\), the difference \(\lambda_n-\lambda_4=(\mu_n-\mu_4)+a^{n+1}-a^5\) is strictly increasing, because \((n+1)a^n-5a^4>0\) throughout this short interval. Its value at \(\alpha\) is negative, so \(\lambda_n<\lambda_4\) there. For \(\alpha\le a<3/4\), \(\lambda_0-\lambda_n=(a-a^{n+1})+(\mu_0-\mu_n)\) is strictly concave as a function of \(a\), positive at \(a=\alpha\), and positive at \(a=3/4\), where \(\lambda_n=(7/8)^{n+1}\). It is consequently positive throughout. Combining these inequalities with the elimination of \(n\ge5\) proves that only degrees zero and four can maximize. The sign of \(\lambda_0-\lambda_4=H(a)-d\) gives all three cases claimed.

**3. Arbitrarily remote crossings.** For each sufficiently large integer \(M\), let \(h,b,c,R\) be as in the finding and set \(\mu_n=c^{n+1}-b^{n+1}\). Then \(0<b<c<1\) and
\[
\frac c b=R=2^{1/(M+1/2)}.
\]
The first difference obeys
\[
\mu_{n+1}-\mu_n=h c^{n+1}\left(2(b/c)^{n+1}-1\right).
\]
It is strictly positive for \(n<M\) and strictly negative for \(n\ge M\), because \(\log2/\log(c/b)=M+1/2\). Hence \(\mu_M\) is the unique outer-shell maximum. Also \(h\sim (\log2)/M\), \(c^{M+1}\to1/2\), \(b^{M+1}\to1/4\), whence \(\mu_M\to1/4\) and \(\mu_M-h\to1/4\). For large \(M\), the strictly increasing function \(a\mapsto a-a^{M+1}\) on \([0,1/3]\) takes values from zero to a value approaching \(1/3\). This proves existence and uniqueness of \(a_M\in(0,1/3)\) and \(a_M\to1/4\). By its defining equation, \(\lambda_0(a_M)=\lambda_M(a_M)\).

To exclude every other degree **uniformly in the unbounded index**, expand the two differences adjacent to the outer peak. Writing \(\rho=b/c=2^{-1/(M+1/2)}\) gives
\[
\mu_M-\mu_{M-1}=h c^M(2\rho^M-1),\qquad
\mu_M-\mu_{M+1}=h c^{M+1}(1-2\rho^{M+1}).
\]
Because \(h\sim (\log2)/M\) and \(c^M\to1/2\), both right sides are \(h^2(1/4+o(1))\). By strict unimodality,
\[
\mu_M-\mu_n\ge(1/8)h^2\qquad(n\ne M)
\]
for all sufficiently large \(M\). Let \(J_h=\lceil 3\log(1/h)/\log3\rceil\). For \(1\le n<J_h\), the mean-value theorem yields \(\mu_n\le(n+1)h=O(h\log(1/h))\) and \(a_M^{n+1}\le1/9\), so \(\lambda_n\le1/9+o(1)<\lambda_M\to1/4\). For \(n\ge J_h\), \(a_M^{n+1}\le3^{-(n+1)}\le h^3\); if \(n\ne M\), then
\[
\lambda_n\le\mu_M-(1/8)h^2+h^3<\mu_M<\lambda_M.
\]
This proves exclusion of **all** degrees other than \(0,M\), not merely a finite numerical sample. Finally, when the outer annulus is fixed, \(\lambda_0(a)-\lambda_M(a)=a-a^{M+1}-(\mu_M-h)\) has derivative \(1-(M+1)a_M^M>0\) at the crossing for all large \(M\). Strict separation from other eigenvalues and uniform geometric decay in \(n\) preserve the two-contender classification in a neighborhood, proving the direct switch.

## Verification
The standalone `check.py` checks the finite example with exact rational inequalities: the two isolating endpoints, every comparison used for degrees one through three, the outer-shell peak signs, and the algebraic constants. It also calculates selected large-jump examples by high-precision decimal arithmetic; these illustrations are **not** a substitute for the asymptotic proof in Step 3. Run `python3 check.py` from the extracted package directory. No third-party Python modules are needed.

## Relationship to prior work
Rozenblum and Vasilevski (arXiv:2203.04170, initial public version 2022-03-08), especially their section on elliptic/radial Toeplitz operators, describe the common spectral-function diagonalization. That framework does not give the present complete two-component maximizing-degree phase diagram or its unbounded-jump construction. A published mathematical result on a *single* weighted Bergman annulus gives an adjacent-degree maximum criterion, which does not cover a disconnected disk-plus-annulus mask. Results on disconnected **Gaussian Fock** masks establish nonadjacent crossings (including degree zero to two) and sharp shell-count bounds in a different Hilbert space; they suggest the geometric question but do not imply the Bergman constants or arbitrary large top-mode gaps here. Earlier radial Toeplitz algebra and moment-sequence literature supplies background; historical priority for a specialized undiscovered two-shell Bergman result remains a risk.

## Limitations
The explicit complete phase diagram is for the stated rational outer annulus on unweighted analytic Bergman space. The general assertion is eventual in \(M\), not a claimed explicit earliest threshold or all-parameter classification. The theorem does not prove an arbitrary multi-annulus peak-count law, handle all weighted Bergman exponents, or classify nonradial masks. The asymptotic proof gives genuine infinite-index exclusion, whereas finite experiments have only a supporting role. An equivalent result in less searchable radial moment literature may remain unidentified.

## References
1. G. Rozenblum and N. Vasilevski, *Commutative algebras of Toeplitz operators on the Bergman space revisited: Spectral theorem approach*, arXiv:2203.04170, initial public version 2022-03-08. https://arxiv.org/abs/2203.04170
2. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, Bull. London Math. Soc. 40 (2008), 631–641, DOI:10.1112/blms/bdn042. https://doi.org/10.1112/blms/bdn042
3. published-finding corpus, *Gamma spectral crossover for hyperbolic annulus localization*, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-gamma-spectral-crossover-for-hyperbolic-annulus-localization--1a134dd07c62
4. published-finding corpus, *A two-component radial Gaussian localization mask with a nonadjacent top-mode crossing*, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-two-component-radial-gaussian-localization-mask-with-a-nonadja--6b39c825507d
5. published-finding corpus, *A sharp shell-count law for angular-momentum peaks in Gaussian Fock localization*, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-shell-count-law-for-angular-momentum-peaks-in-gaussian-f--41fa2b45e61f
