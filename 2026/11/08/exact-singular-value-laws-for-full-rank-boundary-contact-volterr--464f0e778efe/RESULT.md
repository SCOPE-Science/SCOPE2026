# Exact singular-value laws for full-rank boundary-contact Volterra companions

## Finding
Let \(d\ge2\), \(1\le h<d\), \(k\ge1\) be integers. On the normalized-volume Bergman space \(A^2(\mathbb B_d)\), take the full-rank diagonal self-map
\[
\varphi_\lambda(z)=(z_1,\ldots,z_h,\lambda_{h+1}z_{h+1},\ldots,\lambda_dz_d),\qquad 0<|\lambda_j|<1\quad(j>h),
\]
and the transverse monomial symbol \(g(z)=z_{h+1}^k\). The generalized Volterra companion is
\[
(Tf)(z)=\int_0^1 (Rf)(\varphi_\lambda(tz))g(tz)\,\frac{dt}{t},
\qquad Rf(z)=\sum_{j=1}^{d}z_j\partial_{z_j}f(z).
\]
For \(\alpha\in\mathbb N_0^d\), let \(N=|\alpha|\) and
\[
 b_\alpha=\frac{N}{N+k}\Big(\prod_{j=h+1}^{d}\lambda_j^{\alpha_j}\Big)
 \left[\frac{(\alpha_{h+1}+k)!}{\alpha_{h+1}!}\frac{(N+d)!}{(N+d+k)!}\right]^{1/2}.
\]
The complete nonzero singular-value multiset of \(T\) is precisely \(\{|b_\alpha|:\alpha\in\mathbb N_0^d,\ |\alpha|\ge1\}\). The kernel consists of the constant functions.

Set \(q=2h/k\), \(r_j=|\lambda_j|\), and define the finite, strictly positive constant
\[
\mathcal C_{d,h,k}(\lambda)
=\frac1{h!}\left(\prod_{j=h+2}^{d}\frac1{1-r_j^q}\right)
\sum_{b=0}^\infty r_{h+1}^{qb}
\left(\frac{(b+k)!}{b!}\right)^{h/k}.
\]
Here an empty product equals one. With multiplicities, let \(s_n(T)\) be the decreasing nonzero singular values. Then
\[
\boxed{\lim_{t\downarrow0}t^q\#\{n:s_n(T)>t\}=\mathcal C_{d,h,k}(\lambda),\qquad
\lim_{n\to\infty}n^{1/q}s_n(T)=\mathcal C_{d,h,k}(\lambda)^{1/q}.}
\]
In particular, for every real \(p>0\),
\[
\boxed{T\in\mathcal S_p\ \Longleftrightarrow\ p>q.}
\]
The operator belongs to weak \(\mathcal S_q\), but not to \(\mathcal S_q\), and it obeys
\[
\lim_{n\to\infty}\frac{\sum_{j=1}^n s_j(T)^q}{\log n}=\mathcal C_{d,h,k}(\lambda).
\]
For \(h=k\), the constant simplifies to
\[
\mathcal C_{d,h,h}(\lambda)
=(1-r_{h+1}^2)^{-(h+1)}\prod_{j=h+2}^d(1-r_j^2)^{-1}.
\]
Thus the critical Schatten exponent depends only on the dimension \(h\) of the undamped contact directions and the transverse vanishing order \(k\), while its exact coefficient records all damping parameters.

## Assumptions and scope
The Bergman norm uses normalized Lebesgue volume on the open complex unit ball \(\mathbb B_d\). All the contraction parameters are nonzero and strictly smaller than one in modulus, so \(\varphi_\lambda\) has full complex rank and meets the sphere along the first \(h\) coordinate directions. The integral is first defined on holomorphic polynomials and then extended as a bounded compact operator. The assertions concern singular values (not ordinary eigenvalues), with their Hilbert-space multiplicities, for exactly this monomial-symbol diagonal family.

## Proof
The normalized monomials form an orthonormal basis:
\[
 e_\alpha(z)=\left(\frac{(N+d)!}{d!\,\alpha!}\right)^{1/2}z^\alpha,
\qquad
\|z^\alpha\|^2=\frac{d!\,\alpha!}{(N+d)!}.
\]
Here \(\alpha!=\prod_{j=1}^{d}\alpha_j!\). Homogeneity gives \((Rf)(\varphi_\lambda(tz))=Nt^N(\prod_{j>h}\lambda_j^{\alpha_j})z^\alpha\) for \(f(z)=z^\alpha\). Therefore integrating \(t^{N+k-1}\), including the zero action when \(N=0\), gives
\[
Te_\alpha=b_\alpha e_{\alpha+k\mathbf e_{h+1}}.
\]
Different \(\alpha\)'s have different output multi-indices. Thus \(T^*T\) is diagonal with eigenvalues \(|b_\alpha|^2\), proving the complete singular multiset and the stated one-dimensional kernel. For \(\beta=(\alpha_{h+1},\ldots,\alpha_d)\), define \(M=\alpha_1+\cdots+\alpha_h\), \(B=|\beta|\), and
\[
A_\beta=\left(\prod_{j=h+1}^d r_j^{\beta_{j-h}}\right)
\left[\frac{(\beta_1+k)!}{\beta_1!}\right]^{1/2}.
\]
The coefficient \(|b_\alpha|\) depends on the undamped indices only through \(M\); call it \(a_{M,\beta}\). Explicitly,
\[
 a_{M,\beta}=\frac{M+B}{M+B+k}A_\beta
 \left(\prod_{\ell=1}^{k}(M+B+d+\ell)\right)^{-1/2}.
\]
For each fixed \(\beta\),
\[
\lim_{M\to\infty}M^{k/2}a_{M,\beta}=A_\beta,
\qquad 0\le a_{M,\beta}\le\frac{A_\beta}{(M+1)^{k/2}}.
\]
There are \(\binom{M+h-1}{h-1}\) undamped multi-indices of degree \(M\). The hockey-stick identity therefore implies, for each fixed \(\beta\),
\[
\lim_{t\downarrow0}t^q\sum_{M\ge0}\binom{M+h-1}{h-1}\mathbf 1_{\{a_{M,\beta}>t\}}
=\frac{A_\beta^q}{h!}.
\]
Indeed the upper and lower tail bounds from \(a_{M,\beta}\sim A_\beta M^{-k/2}\) sandwich the relevant degrees between \((1\pm\varepsilon)(A_\beta/t)^{2/k}\) for large \(M\); the sum of multiplicities through degree \(L\) is \(\binom{L+h}{h}\sim L^h/h!\).

To justify summation over every transverse index, the upper bound on \(a_{M,\beta}\) and the same binomial identity give a uniform estimate
\[
 t^q\sum_{M\ge0}\binom{M+h-1}{h-1}\mathbf 1_{\{a_{M,\beta}>t\}}
 \le C_h A_\beta^q,
\]
where \(C_h\) depends only on \(h\). The series \(\sum_\beta A_\beta^q\) converges because all \(r_j<1\) and the factorial quotient grows polynomially in \(\beta_1\). Dominated convergence yields
\[
\lim_{t\downarrow0}t^q\#\{n:s_n(T)>t\}
=\frac1{h!}\sum_\beta A_\beta^q
=\mathcal C_{d,h,k}(\lambda),
\]
where separating the geometric sums over \(\beta_2,\ldots,\beta_{d-h}\) gives the stated expression. Inversion of this strictly positive counting asymptotic proves \(s_n(T)\sim\mathcal C^{1/q}n^{-1/q}\). This also proves compactness; directly, the weights vanish for fixed transverse indices as \(M\to\infty\) and decay exponentially as the transverse degree increases.

The singular-value asymptotic shows \(\mathcal S_p\) membership exactly for \(p>q\), strict failure at \(p=q\), and the sharp weak endpoint. Since \(s_n(T)^q\sim\mathcal C/n\), comparison with harmonic sums proves the logarithmic coefficient. Finally, when \(h=k\), \(q=2\) and \(\sum_{b\ge0}((b+h)!/b!)x^b=h!(1-x)^{-h-1}\), giving the closed form.

## Verification
The standalone script `check.py` computes the monomial norms and compares the squared shift weights with two independently encoded formulas using exact rational arithmetic. It also checks injectivity of the output-index map for finite collections of monomials. Execution under Python 3.11 produced `MONOMIAL_COMPANION_EXACT_OK 40065`. Optional numerical truncations corroborate convergence of the counting function to its predicted constant, including its slow approach at moderate cutoffs. The infinite-dimensional proof uses the exact basis action, counting multiplicity, and dominated convergence, not finite enumeration.

## Relationship to prior work
Dong and Xu's September 2026 generalized companion paper gives derivative-Carleson boundedness, compactness, Schatten criteria in the covered exponent ranges, compact-range exponential decay, and a sharp-power ellipsoid example with a **rank-deficient** projection self-map. Their Section 3.3 uses a collapsed transverse variable, whereas the self-maps here have full complex rank and retain every transverse monomial mode. Its power threshold in the ball/projection limit is compatible with ours; it does not state the new full-rank coefficient \(\mathcal C_{d,h,k}(\lambda)\) or its dependence on all strict damping parameters. Li, Long and Wang study ordinary Toeplitz and weighted-composition operators rather than these radial derivative companions. Mengestie's companion Schatten criteria use Fock spaces, not the complex ball; their results do not imply this Bergman singular coefficient. Searches for diagonal, partial-contact, anisotropic, and weak-Schatten formulations identified no directly covering primary theorem. The argument gives a specialized exact quantitative refinement, not a solution to the general small-exponent derivative-Carleson characterization.

## Limitations
The result assumes diagonal full-rank maps, strict transverse contraction, and a single transverse monomial. It does not claim a Weyl law for arbitrary symbols or arbitrary finite-type convex domains, nor a general characterization of the derivative pull-back measure below the Hilbert–Schmidt threshold. The published projection example already predicts the same exponent in its overlapping degenerate limit; originality is specifically the all-parameter full-rank exact spectral asymptotic and coefficient. A broader unlocated operator-weighted-shift result could conceivably imply the counting argument. A separate independent mathematical review has not been performed.

## References
- J. Dong and C. Xu, *Generalized Volterra Companion Operators on Bergman Spaces over Convex Domains of Finite Type*, arXiv:2609.27584, first submitted 2026-09-23, especially Sections 3.3 and 4.3; https://arxiv.org/abs/2609.27584.
- M. Li, J. Long, and L. Wang, *Small exponent Schatten class Toeplitz operators on convex domains of finite type*, arXiv:2609.22908, first submitted 2026-09-19; https://arxiv.org/abs/2609.22908.
- T. Mengestie, *Schatten class generalized Volterra companion integral operators*, arXiv:1507.03536 (2015), on Fock spaces; https://arxiv.org/abs/1507.03536.
