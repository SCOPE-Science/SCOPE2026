# Sharp non-Hilbert Pascal transfer exponents and radial lattice dynamics

## Finding

Consider the directed quadrant \(V=\mathbb N_0^2\) and the backward lattice shift
\[
(Bf)(i,j)=f(i+1,j)+f(i,j+1).
\]
Let \(\omega=(\omega_k)_{k\ge0}\) be nonzero complex numbers satisfying
\[
L:=\sup_{k\ge0}\left|\frac{\omega_k}{\omega_{k+1}}\right|<\infty,
\qquad \mu_{i,j}=\omega_{i+j}.
\]
For \(1\le p<\infty\), let \(X_p=\ell^p(V,\mu)\), with norm \(\bigl(\sum_{i,j}|\mu_{i,j}f(i,j)|^p\bigr)^{1/p}\). Let \(X_\infty=c_0(V,\mu)\) with the weighted supremum norm. The symbol \(p=\infty\) *always* means this separable \(c_0\)-space, not \(\ell^\infty\). Then \(B\) is bounded on every \(X_p\).

For integers \(m\ge0\), \(n\ge1\), define the rectangular Pascal matrix
\[
(P_{m,n})_{i,k}=\binom{n}{k-i},\qquad 0\le i\le m,\quad0\le k\le m+n,
\]
with out-of-range binomial coefficients zero. Let \(p'\) be the Hölder conjugate of \(p\), including \(1'=\infty\) and \(\infty'=1\). There are positive constants \(c_{m,p},C_{m,p}\), independent of \(n\), such that
\[
\boxed{\quad
c_{m,p}\,2^n(n+1)^{-m/2-1/(2p)}
\le\inf_{\|y\|_{p'}=1}\|P_{m,n}^*y\|_{p'}
\le C_{m,p}\,2^n(n+1)^{-m/2-1/(2p)}.
\quad}
\tag{1}
\]
Here \(1/\infty=0\). Both exponents are sharp, also at the two endpoint norms. Consequently the smallest operator norm among linear right inverses of the normalized degree-transfer map from level \(m+n\) to level \(m\) is, up to constants depending only on \(m,p\),
\[
\boxed{\quad
\Psi_{m,p}(n):=\frac{|\omega_{m+n}|}{|\omega_m|}\,
\frac{(n+1)^{m/2+1/(2p)}}{2^n}.
\quad}
\tag{2}
\]

**Complete dynamical classification across Banach exponents.** For every \(1\le p\le\infty\) with the preceding convention:
\[
\boxed{\begin{aligned}
B\text{ is hypercyclic }&\Longleftrightarrow B\text{ is weakly mixing}
\Longleftrightarrow \forall m\ge0:\ \liminf_{n\to\infty}\Psi_{m,p}(n)=0,\\
B\text{ is mixing }&\Longleftrightarrow
\forall m\ge0:\ \lim_{n\to\infty}\Psi_{m,p}(n)=0.
\end{aligned}}
\tag{3}
\]
In particular, for a fixed radial weight, hypercyclicity and mixing are **independent of the choice of \(p\)** among all \(1\le p<\infty\) and weighted \(c_0\). The Hilbert-space case of the dynamical classification and its sharp exponent were previously established; (1) in all non-Hilbert norms and the corresponding across-exponent extension are the contribution here.

## Assumptions and scope

All Banach spaces are complex, and the quadrant starts at coordinate zero. A level \(m\) consists of the \(m+1\) vertices \((i,m-i)\), \(0\le i\le m\). A column of the normalized degree-transfer operator is multiplied by \(\omega_m/\omega_{m+n}\). Only the one-step bound \(L<\infty\) on radial weights is assumed; monotonicity, regular variation and positivity of the \(\omega_k\) are not required. Constants in (1) and (2) may depend on the fixed level and Banach exponent, never on the transfer length.

## Proof

**1. Exact diagonal transfer.** On each fixed level, multiply coordinates by the common weight \(\omega_m\). This identifies its Banach norm with \(\ell^p_{m+1}\) (or the finite-dimensional supremum norm). The binomial identity for lattice paths gives
\[
(B^nf)(i,m-i)=\sum_{r=0}^{n}\binom nr f(i+r,m-i+n-r),
\]
so the transfer matrix is \(M_{m,n}=(\omega_m/\omega_{m+n})P_{m,n}\). The elementary row-sum estimate gives \(\|B\|\le2L\). Every \(P_{m,n}\) is surjective: the first \(m+1\) columns form a triangular matrix with diagonal entries one.

**2. A uniform Banach finite-difference lemma.** Extend the binomial mass \(b_n(k)=2^{-n}\binom nk\) by zero outside its support, and put \(\Delta u(k)=u(k)-u(k-1)\). For fixed \(m\) and \(1\le r\le\infty\), the following *uniform coefficient estimate* holds for all sufficiently large \(n\):
\[
\left\|\sum_{j=0}^m a_j\Delta^j b_n\right\|_{\ell^r(\mathbb Z)}
\asymp_{m,r}
 n^{-1/2+1/(2r)}
 \left(\sum_{j=0}^m |a_j|^2n^{-j}\right)^{1/2},
\tag{4}
\]
where \(1/r=0\) when \(r=\infty\). We verify the uniformity (including coefficient choices depending on \(n\)) rather than invoking pointwise central-limit heuristics.

Write \(s=(k-n/2)/\sqrt n\). Fourier coefficient extraction gives, for fixed \(j\),
\[
n^{(j+1)/2}\Delta^j b_n(k)
=\frac1{2\pi}\int_{-\pi\sqrt n}^{\pi\sqrt n}
 e^{-isu}\,[\sqrt n(1-e^{iu/\sqrt n})]^j
 \cos(u/(2\sqrt n))^n\,du.
\tag{5}
\]
The integrand converges in \(L^1(du)\) to \((-iu)^je^{-u^2/8}\). Its Fourier transform is a signed derivative \(G_j\) of \(g(s)=\sqrt{2/\pi}e^{-2s^2}\). For every fixed positive integer \(K\), elementary differentiation of the integrand, combined with \(|\cos(u/(2\sqrt n))|^n\le e^{-c u^2}\) on its integration interval, bounds its first \(K\) derivatives in \(L^1\) uniformly for all sufficiently large \(n\). Endpoint derivatives vanish once \(n>K+j\). Repeated integration by parts therefore gives the uniform tail bound
\[
|n^{(j+1)/2}\Delta^j b_n(k)|\le C_{j,K}(1+|s|)^{-K}.
\]
This establishes convergence of the sampled functions in rescaled \(\ell^r\) for every finite \(r\), and in the supremum norm when \(r=\infty\). The limits \(G_0,\ldots,G_m\) are linearly independent because each is a Gaussian times a polynomial of its own degree. On their finite-dimensional span, the \(L^r\)-norm is equivalent to Euclidean coefficient norm. Uniform convergence on the coefficient unit sphere now gives
\[
\left\|\sum_{j=0}^m c_j n^{(j+1)/2}\Delta^j b_n\right\|_r
\asymp_{m,r}n^{1/(2r)}\|(c_j)\|_2.
\]
Taking \(c_j=a_jn^{-(j+1)/2}\) proves (4). For small \(n\) the estimates are absorbed into constants; the finitely many relevant coefficient maps remain injective.

**3. Sharp dual transfer rate.** For \(y=(y_0,\ldots,y_m)\), write \(Q_y(z)=\sum_{i=0}^m y_iz^i=\sum_{j=0}^m a_j(z-1)^j\). The coefficients of \((1+z)^nQ_y(z)\) are exactly \(P_{m,n}^*y\). Thus (4), with \(r=p'\), gives
\[
2^{-n}\|P_{m,n}^*y\|_{p'}\asymp_{m,p}
 n^{-1/(2p)}\left(\sum_{j=0}^m |a_j|^2 n^{-j}\right)^{1/2}.
\tag{6}
\]
The fixed invertible change of coordinates between \((y_i)\) and \((a_j)\) implies \(\sum|a_j|^2\asymp_m\|y\|_{p'}^2\). Therefore the right side is at least a constant times \(n^{-m/2-1/(2p)}\|y\|_{p'}\). For the reverse bound take the fixed difference polynomial \(Q_y(z)=(z-1)^m\), which has only the highest-order difference. This proves (1), including both endpoints.

For a surjective finite-dimensional operator \(P:E\to F\), set \(\lambda(P)=\inf_{\|y\|_{F^*}=1}\|P^*y\|_{E^*}\). Every right inverse \(R\) obeys \(\|R\|\ge1/\lambda(P)\), by \(R^*P^*=I\). Conversely the induced quotient isomorphism \(E/\ker P\to F\) has inverse norm \(1/\lambda(P)\) by finite-dimensional duality. Lift each vector of a fixed Auerbach basis of \(F\) through this inverse; the resulting linear right inverse has norm at most \((\dim F)/\lambda(P)\). Since \(\dim F=m+1\) is fixed, (1) gives the right-inverse comparison (2).

**4. Sufficiency of the dynamical tests.** Let \(D\) be the dense set of finitely supported vectors in \(X_p\). Every \(f\in D\) is eventually killed by \(B^n\). The assumption \(L<\infty\) gives, for each \(0\le m\le M\), a constant \(A_{m,M}\) such that
\[
\Psi_{m,p}(n)\le A_{m,M}\Psi_{M,p}(n),\qquad n\ge1.
\tag{7}
\]
Indeed, \(|\omega_{m+n}/\omega_{M+n}|\le L^{M-m}\) and \((n+1)^{(m-M)/2}\le1\). If every \(\liminf\Psi_{M,p}=0\), let \(C_{j,p}\) bound the right-inverse comparison (2) at level \(j\). Choose increasing \(n_j\), using the full freedom supplied by the zero liminf at level \(j\), so that \(\Psi_{j,p}(n_j)<[j\max_{0\le m\le j} C_{m,p}A_{m,j}]^{-1}\). Then (7) and (2) give right inverses for the transfers to *all* levels \(m\le j\) with norms at most \(1/j\). In particular they tend to zero for each fixed finite collection of levels. Summing those lifts over distinct input levels defines maps \(R_{n_j}:D\to X_p\) with \(R_{n_j}g\to0\) and \(B^{n_j}R_{n_j}g=g\) for each \(g\in D\). The Hypercyclicity Criterion gives weak mixing, hence hypercyclicity. If every full limit of \(\Psi_{m,p}\) is zero, use every integer \(n\) instead; the full-sequence Hypercyclicity Criterion gives mixing.

**5. Necessity.** Fix \(m\). Let \(u_m\) be the nonzero output-level dual vector with coefficient polynomial \((z-1)^m\), normalized in \(\ell^{p'}\). By (6),
\[
\|M_{m,n}^*u_m\|_{p'}\asymp_{m,p}\Psi_{m,p}(n)^{-1}.
\tag{8}
\]
Choose a finite-level output target \(v_m\) with \(\langle v_m,u_m\rangle=1\). If \(x\) is hypercyclic, infinitely many orbit iterates approach \(v_m\) closely. Their output on level \(m\) comes *only* from the input block on level \(m+n\), whose norm tends to zero as \(n\to\infty\). Hölder duality and (8) force \(\Psi_{m,p}(n)\to0\) along those visits. This proves the liminf necessity. If \(B\) is mixing but \(\Psi_{m,p}\) stays bounded below along infinitely many indices, (8) gives a uniform bound on the dual transfer norm there. A sufficiently small neighborhood of zero cannot reach a fixed neighborhood of \(v_m\) at those indices, contradicting mixing. Thus the full limit must be zero.

**6. Independence of exponent.** For any two exponents \(p,t\) in the stated range, the ratio of their tests at a common level is \((n+1)^{1/(2p)-1/(2t)}\). Given a level \(m\) for exponent \(t\), choose a larger integer \(M\) so that \((m-M)/2+1/(2t)-1/(2p)\le0\). The bounded-ratio argument in (7) then yields \(\Psi_{m,t}(n)\le C\Psi_{M,p}(n)\). This transfers both liminf and full-limit conditions from \(p\) to \(t\); reversing the roles proves their equivalence.

## Verification

The standalone `checker.py` verifies the exact integer-valued Pascal adjoint identity, Vandermonde Gram formula, binomial normalizations, first-difference total variation, and one-step block bounds in finitely many low-dimensional cases. It uses only the Python standard library. Reproduce with `python checker.py`. These finite checks are diagnostics; (1)–(3) follow from the Fourier/duality argument above for all levels and powers.

As a check on the sharp exponents, at level \(m=0\) the adjoint vector is the binomial row, whose \(\ell^1\), \(\ell^2\), and \(\ell^\infty\) norms are exactly \(2^n\), \(\binom{2n}{n}^{1/2}\), and \(\binom n{\lfloor n/2\rfloor}\), respectively. At level \(m=1\), the first difference has exact \(\ell^1\) norm \(2\binom n{\lfloor n/2\rfloor}\). These confirm the endpoint and Hilbert exponents independently of numerical fitting.

## Relationship to prior work

Chen, Wang and Zhou (first public 2026-09-28), Section 4, prove the radial **Hilbert-space** criterion, with a sharp \(\ell^2\) smallest-singular-value asymptotic, and expressly ask in Section 5 whether it extends to \(\ell^p\) and \(c_0\). Their finite-width lattice results do treat general \(p\), but have fixed transverse dimension and different transfer geometry. Here the new mathematical ingredient is the uniform Banach-norm binomial-difference estimate (4), which gives the sharp \(p\)-dependent exponent in (1) and permits the infinite-quadrant classification in all the requested spaces. The \(p=2\) specialization of (3), and its previous singular-value rate, are *not* claimed as new.

Baranov, Lishanskii and Papathanasiou first posed the broader infinite-lattice hypercyclicity problem in a December 2023 preprint. Their 2026 journal appearance is not used as the first-public date. Their sufficient and necessary bounds at exponential base two leave critical weights unresolved in the general nonradial setting. The present result remains restricted to radial weights.

A separate published construction decomposes a specially **nonradial**, binomially weighted lattice into scalar shifts by a symmetric-Fock transformation. That representation does not imply the Banach-norm radial estimate (1) or the all-\(p\) criteria (3).

## Limitations

The theorem concerns radial weights and the standard degree-two quadrant only. It does not characterize general nonradial weights, higher-dimensional lattices, or frequent hypercyclicity and arbitrary Furstenberg-family transitivity. Constants in (1) are shown to be positive and finite, but their optimal numerical values for each \(m,p\) are not evaluated. No independent external mathematical audit has been performed.

## References

1. X. Chen, C. Wang, Z.-H. Zhou, *\(\mathcal F\)-Transitivity of Backward Shifts on Lattice Graphs*, arXiv:2609.34308, first public 2026-09-28, especially Section 4, Corollary 4.7, and Section 5, question (1). https://arxiv.org/abs/2609.34308
2. A. Baranov, A. Lishanskii, D. Papathanasiou, *Hypercyclic shifts on lattice graphs*, arXiv:2312.13934, first public 2023-12-21; *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A* 120 (2026), article 78. https://doi.org/10.1007/s13398-026-01868-8
3. F. Bayart, É. Matheron, *Dynamics of Linear Operators*, Cambridge Tracts in Mathematics 179, Cambridge University Press, 2009, Hypercyclicity Criterion.
