# A sharp affine-composition threshold on dyadically punctured weighted Hardy spaces

## Finding

For each real \(\alpha>0\), define the coefficient-weighted analytic Hilbert space \(H^2(\beta^{(\alpha)})\) by
\[
\|f\|_{\beta^{(\alpha)}}^2=\sum_{n=0}^{\infty}\beta_n^{(\alpha)}|\widehat f(n)|^2,
\qquad
\beta_n^{(\alpha)}=\begin{cases}
  n^{-\alpha},& n=2^k\text{ for some integer }k\ge0,\\
  1,&\text{otherwise}.
\end{cases}
\]
For every real \(0<t<1\), let \(\varphi_t(z)=1-t+tz\). Then the composition map \(C_{\varphi_t}f=f\circ\varphi_t\), initially defined on polynomials, extends boundedly on \(H^2(\beta^{(\alpha)})\) **if and only if**
\[
\boxed{\alpha\le\tfrac12.}
\]
Let \(L_\alpha\) be the closed span of the normalized lacunary monomials \(e_k(z)=(2^k)^{\alpha/2}z^{2^k}\), \(k\ge0\). Whenever the restriction \(A_{\alpha,t}=C_{\varphi_t}|_{L_\alpha}\) is bounded, it has the following sharp operator-ideal phases:

1. If \(0<\alpha<\tfrac12\), then \(A_{\alpha,t}\) belongs to every Schatten class \(\mathcal S_p(L_\alpha,H^2(\beta^{(\alpha)}))\), \(p>0\), and its singular values decrease at least geometrically.
2. At \(\alpha=\tfrac12\), with \(c_t=(2\sqrt{\pi t(1-t)})^{-1}\),
\[
 A_{1/2,t}^*A_{1/2,t}-c_t I_{L_{1/2}}\in\mathcal S_1(L_{1/2}),
 \qquad |A_{1/2,t}|-\sqrt{c_t}\,I_{L_{1/2}}\in\mathcal S_1(L_{1/2}).
\]
In particular, its exact essential norm and essential singular spectrum are
\[
\boxed{\|A_{1/2,t}\|_{\mathrm{ess}}=[4\pi t(1-t)]^{-1/4}},
\qquad
\boxed{\sigma_{\mathrm{ess}}(|A_{1/2,t}|)=\{[4\pi t(1-t)]^{-1/4}\}.}
\]
3. If \(\alpha>\tfrac12\), even the restriction of the polynomial composition map to normalized lacunary monomials is unbounded.

## Assumptions and scope

The scalars are complex, \(0<t<1\) and \(\alpha>0\) are fixed real parameters, and \(H^2(\beta^{(\alpha)})\) is the coefficient Hilbert space above. The weights satisfy \(\liminf_{n\to\infty}(\beta_n^{(\alpha)})^{1/n}=1\), so point evaluations in the open unit disk are continuous. The statement concerns one specific affine boundary-contact symbol family and its canonical lacunary-input restriction; it does not characterize arbitrary composition symbols or all weighted Hardy spaces.

## Proof

Put \(p_{n,j}=\binom nj t^j(1-t)^{n-j}\) for \(0\le j\le n\), and zero otherwise. Then
\[
\varphi_t(z)^n=\sum_{j=0}^np_{n,j}z^j,
\quad
\langle A_{\alpha,t}e_k,A_{\alpha,t}e_\ell\rangle_\beta
=(2^k2^\ell)^{\alpha/2}\sum_{j\ge0}\beta_j^{(\alpha)}p_{2^k,j}p_{2^\ell,j}.
\tag{1}
\]
Let \(v=t(1-t)>0\). The unweighted diagonal mass is
\[
G_t(n,n)=\sum_jp_{n,j}^2=\frac1{2\pi}\int_{-\pi}^{\pi}
[1-4v\sin^2(\theta/2)]^n\,d\theta
=\frac{1}{2\sqrt{\pi vn}}+O_t(n^{-3/2}).
\tag{2}
\]
To justify the error, split the integral into \(|\theta|\le n^{-5/12}\) and its complement. On the central arc, write \(u=\sqrt n\,\theta\); the logarithm of the integrand is \(-vu^2+O_t(u^4/n)\). Integrating the Gaussian remainder gives \(O_t(n^{-3/2})\) after the \(n^{-1/2}\) Jacobian, while the complementary arc is \(O_t(e^{-a_t n^{1/6}})\). These estimates hold for every fixed \(0<t<1\).

The binomial probabilities are unimodal, with maximum near \(j=nt\). The ratio \(p_{n,j+1}/p_{n,j}=(n-j)t/((j+1)(1-t))\) and Stirling's bounds at a maximizing index give
\[
\max_{0\le j\le n}p_{n,j}\le C_t n^{-1/2}.
\tag{3}
\]
There are at most \(1+\lfloor\log_2 n\rfloor\) positive powers of two not exceeding \(n\). Since \(0<\beta_j^{(\alpha)}\le1\), equations (2) and (3) imply, for \(n=2^k\),
\[
\begin{split}
d_k&:=\|A_{\alpha,t}e_k\|_\beta^2
=n^{\alpha}\left(G_t(n,n)-\sum_{j=2^r\le n}(1-j^{-\alpha})p_{n,j}^2\right)\\
&=c_t n^{\alpha-1/2}+O_{\alpha,t}(n^{\alpha-1}\log(2+n)),
\qquad c_t=\frac1{2\sqrt{\pi t(1-t)}}.
\end{split}
\tag{4}
\]
In particular, \(d_k\to\infty\) when \(\alpha>1/2\); boundedness then fails on the unit vectors \(e_k\).

For the off-diagonal terms, let \(X_n\) and \(Y_m\) be independent binomial random variables of respective orders \(n,m\), both with success probability \(t\). Their collision probability satisfies
\[
G_t(n,m):=\sum_jp_{n,j}p_{m,j}=\mathbb P(X_n=Y_m)
\le(1-t+tu)^n(1-t+t/u)^m\quad(u>1),
\tag{5}
\]
because \(\mathbf1_{\{X_n=Y_m\}}\le u^{X_n-Y_m}\). If \(m\ge2n\), the right side is at most \(\rho_t(u)^m\), where
\[
\rho_t(u)=(1-t+tu)^{1/2}(1-t+t/u).
\]
Here \(\rho_t(1)=1\), while the derivative of \(\log\rho_t(e^s)\) at \(s=0\) is \(-t/2<0\). Fix \(u>1\) sufficiently close to one that \(\rho_t(u)<1\), and abbreviate it to \(\rho_t\). For distinct dyadic \(n<m\), equation (1) and positivity give
\[
0\le\langle A_{\alpha,t}e_k,A_{\alpha,t}e_\ell\rangle_\beta
\le(nm)^{\alpha/2}G_t(n,m)
\le m^\alpha\rho_t^m.
\tag{6}
\]
The sum of the right side over all distinct dyadic pairs is finite, since \(\sum_{\ell\ge1}\ell(2^\ell)^\alpha\rho_t^{2^\ell}<\infty\). Thus the off-diagonal portion of the Gram matrix of \(A_{\alpha,t}\) is trace class wherever the restriction is bounded, and its matrix entries are absolutely summable.

If \(\alpha<1/2\), equation (4) yields \(\|A_{\alpha,t}e_k\|_\beta\le C_{\alpha,t}2^{(\alpha-1/2)k/2}\). Hence the rank-\(K\) column truncation \(A_{\alpha,t}P_K\) satisfies
\[
\|A_{\alpha,t}-A_{\alpha,t}P_K\|\le
\left(\sum_{k\ge K}\|A_{\alpha,t}e_k\|_\beta^2\right)^{1/2}
\le C_{\alpha,t}\,2^{(\alpha-1/2)K/2}.
\tag{7}
\]
The approximation-number estimate in (7) proves membership in every \(\mathcal S_p\), \(p>0\), and shows boundedness.

At \(\alpha=1/2\), equation (4) gives \(d_k=c_t+O_t(k2^{-k/2})\), so \(\sum_k|d_k-c_t|<\infty\). Together with the absolute off-diagonal sum (6), this proves \(A_{1/2,t}^*A_{1/2,t}-c_tI\in\mathcal S_1\) and boundedness. Applying the bounded scalar function \(\lambda\mapsto(\sqrt\lambda+\sqrt{c_t})^{-1}\) to the positive operator \(A_{1/2,t}^*A_{1/2,t}\) gives
\[
|A_{1/2,t}|-\sqrt{c_t}I
=(A_{1/2,t}^*A_{1/2,t}-c_tI)
(|A_{1/2,t}|+\sqrt{c_t}I)^{-1}\in\mathcal S_1.
\]
The essential spectrum and essential norm follow by compact perturbation and the weakly null orthonormal basis \((e_k)\).

Finally, split the full Hilbert space orthogonally into \(L_\alpha\) and the span of monomials with non-dyadic degrees. On the latter span, the \(H^2(\beta^{(\alpha)})\)-norm equals the classical Hardy norm, and the output weighted norm is at most the Hardy norm. Littlewood's classical boundedness theorem therefore controls this component under \(C_{\varphi_t}:H^2\to H^2\). Adding the already controlled lacunary component establishes boundedness of the full operator for \(\alpha\le1/2\). Continuity of point evaluations shows the extension agrees with pointwise composition on every input function.

## Verification

Run `python VERIFY_LACUNARY_AFFINE.py` using Python 3. It performs 1,183 exact or finite numerical checks: exact Vandermonde identities, exact rational weighted-Gram identities at three affine parameters, exact moment-bound examples, and finite critical-diagonal asymptotic sanity tests. The infinite-dimensional proof is equations (1)–(7), not a finite computation. No third-party dataset or downloaded document is needed by the checker.

## Relationship to prior work

Cruz-Zamorano, Dellepiane and Seco (2026, arXiv:2610.40148v1) study when weighted Hardy spaces share the same compact and Hilbert–Schmidt composition-symbol classes as classical \(H^2\), including lacunary coefficient weights. That classification does not state a boundedness threshold for the fixed boundary-contact affine symbols \(\varphi_t\), nor the critical trace-class Gram defect. Lefèvre, Li, Queffélec and Rodríguez-Piazza (2023, arXiv:2312.03482) characterize weights for which **every** disk composition operator is bounded, which does not supply the present single-symbol boundary. Sun and Liu (2026, arXiv:2610.19658) treat coefficient power-weight Dirichlet and mixed-norm spaces; their exact linear-symbol model uses \(\varphi(z)=\rho z\) and does not cover the sparse dyadic coefficient weights or \(1-t+tz\).

## Limitations

The threshold is for the specifically defined sparse coefficient weights and the affine family with \(0<t<1\). The operator-ideal assertions concern the **lacunary-input restriction** and are not asserted for the full composition operator. At \(\alpha>1/2\) no bounded operator exists, so no essential spectrum is assigned. Source-overlap searches do not independently certify publication priority; equivalently formulated earlier theorems may exist.

## References

1. F. J. Cruz-Zamorano, E. Dellepiane, D. Seco, *Compact and Hilbert–Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1 (2026), https://arxiv.org/abs/2610.40148.
2. P. Lefèvre, D. Li, H. Queffélec, L. Rodríguez-Piazza, *Characterization of weighted Hardy spaces on which all composition operators are bounded*, arXiv:2312.03482 (2023), https://arxiv.org/abs/2312.03482.
3. J. Sun, J. Liu, *Weighted composition–differentiation operators on mixed-norm, derivative Hardy and F(p,q,s) spaces*, arXiv:2610.19658 (2026), https://arxiv.org/abs/2610.19658.
4. Classical tools: Littlewood's boundedness principle for Hardy-space composition operators; Stirling's binomial estimates and Laplace's method.
