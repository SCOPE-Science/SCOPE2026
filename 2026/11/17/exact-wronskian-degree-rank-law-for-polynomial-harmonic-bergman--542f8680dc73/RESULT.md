# Exact Wronskian-degree rank law for polynomial harmonic Bergman commutators

## Finding

Let \(a,b\in\mathbb C[z]\), let \(f(z)=a(z)-a(0)\) and \(g(z)=b(z)-b(0)\), and define their centered Wronskian
\[
W_{a,b}(z)=f'(z)g(z)-f(z)g'(z).
\]
On the complex harmonic Bergman space \(b^2(\mathbb D)\), with its normalized area measure, let \(T_a=Q M_a|_{b^2}\) denote the Toeplitz operator with analytic polynomial symbol \(a\). Then, with the zero-polynomial case specified separately,
\[
\boxed{
\operatorname{rank}[T_a,T_b]=
\begin{cases}
0,&W_{a,b}\equiv0,\\[2pt]
2\left\lfloor\dfrac{\deg W_{a,b}}{2}\right\rfloor,&W_{a,b}\not\equiv0.
\end{cases}}
\]
Moreover \([T_a,T_b]^2=0\). If both symbols are nonconstant, the range is contained in the analytic polynomials of degree at most \(\deg a+\deg b-1\) and with zero constant term; if either symbol is constant, the commutator vanishes. Every nonzero rank in the formula is an even positive integer.

Equivalently, if the two centered polynomials are linearly independent, choose a basis \((u,v)\) of their two-dimensional complex span with \(r=\deg u>s=\deg v\ge1\). Then
\[
\operatorname{rank}[T_a,T_b]=
\begin{cases}
r+s-1,&r+s\text{ odd},\\
r+s-2,&r+s\text{ even}.
\end{cases}
\]
Thus the rank depends only on the two pivot degrees of the centered polynomial pencil, not on its other coefficients.

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(dA=\pi^{-1}\,dx\,dy\), and \(b^2(\mathbb D)\) is the closed complex Hilbert space of square-integrable harmonic functions. Its orthogonal projection \(Q\) from \(L^2(\mathbb D,dA)\) defines \(T_a h=Q(ah)\). Analytic polynomials are bounded on the disk, so every operator used is bounded. Our commutator convention is \([A,B]=AB-BA\). Rank is complex linear dimension. Constants commute with all operators, so centering is necessary. The derivative and degree are those of ordinary complex polynomials. When the centered polynomials are dependent, \(W_{a,b}=0\), including the case where one is zero.

No assertion about arbitrary nonpolynomial rational symbols, essential spectra, or optimal singular values is made.

## Proof

**1. Monomial Toeplitz actions.** For integers \(p\ge0\), \(n\ge1\), and \(j\ge0\), the angular orthogonality of disk monomials and the identity \(\int_{\mathbb D}|z|^{2j}\,dA=1/(j+1)\) give
\[
T_{z^p}z^j=z^{p+j},\qquad
T_{z^p}\overline{z}^{\,n}=
\begin{cases}
\dfrac{p-n+1}{p+1}z^{p-n},&n\le p,\\[4pt]
\dfrac{n-p+1}{n+1}\overline z^{\,n-p},&n>p.
\end{cases}
\]
In particular, two analytic-polynomial Toeplitz operators commute on the analytic Bergman summand, so their commutator annihilates all analytic vectors. A second application of this monomial identity, carried out next, shows that its only possible nonzero action is from the strictly anti-analytic summand to the analytic one.

**2. Exact anti-diagonal for two monomials.** Take integers \(1\le p<q\), let \(S=p+q\), and put \(C_{p,q}=[T_{z^p},T_{z^q}]\). Two applications of the preceding monomial action give
\[
C_{p,q}\overline z^{\,n}=d_{p,q}(n)z^{S-n}\quad(1\le n\le S-1),
\]
where
\[
d_{p,q}(n)=
\begin{cases}
\dfrac{(q-p)n}{(p+1)(q+1)},&1\le n\le p,\\[5pt]
\dfrac{p(S-2n)}{(q+1)(n+1)},&p<n\le q,\\[5pt]
\dfrac{(p-q)(S-n)(S-n+1)}{(p+1)(q+1)(n+1)},&q<n<S.
\end{cases}
\]
The same calculation gives zero for \(n\ge S\) (and for the analytic vectors), and changing the order of \(p,q\) changes the coefficient sign. Each coefficient in the displayed range is nonzero except when \(S\) is even and \(n=S/2\), where it is zero. Indeed, the first and third cases have strictly positive factors except for the constant sign, and the middle case has its sole zero at \(2n=S\).

**3. Triangular support of an arbitrary pair.** The commutator is alternating and bilinear in its symbols; adding constants has no effect. If \(f,g\) are linearly independent, Gaussian elimination on their coefficient vectors produces \(u,v\) in their span with distinct positive degrees \(r>s\ge1\), and a nonzero determinant \(\eta\) such that \([T_f,T_g]=\eta[T_u,T_v]\). Write \(S=r+s\). In the finite matrix of \([T_u,T_v]\) from inputs \(\overline z^{\,n}\), \(1\le n\le S-1\), to outputs \(z^k\), \(1\le k\le S-1\), every entry with \(k+n>S\) vanishes. Moreover, on the anti-diagonal \(k+n=S\), the only possible contribution comes from the unique highest-degree pair \(z^r,z^s\); its coefficient is the nonzero product of the two leading coefficients and the monomial coefficient from Step 2, except for the central position when \(S\) is even.

If \(S\) is odd, reversing the order of the rows gives an upper-triangular square matrix of size \(S-1\) with all diagonal entries nonzero. Hence its rank is \(S-1\). If \(S\) is even, deleting the central input and output indices \(S/2\) gives an invertible anti-triangular submatrix of order \(S-2\), so rank is at least \(S-2\).

**4. Sharp even-rank obstruction.** On harmonic polynomials introduce the nondegenerate symmetric complex-bilinear pairing \(B(h,k)=\int_{\mathbb D}h(z)k(z)\,dA(z)\). The harmonic projection has a real/conjugation-invariant kernel, hence \(B(Qh,k)=B(h,Qk)\). Multiplication operators are symmetric for \(B\). Consequently, \(B(T_a h,k)=B(h,T_a k)\), and \(B([T_a,T_b]h,k)=-B(h,[T_a,T_b]k)\). If the matrix from Step 3 is \((M_{k,n})\), pairing its analytic output against \(\overline z^{\,j}\) gives
\[
\frac{M_{k,n}}{k+1}=-\frac{M_{n,k}}{n+1}.
\]
Thus an invertible diagonal row scaling converts \(M\) into a skew-symmetric matrix over \(\mathbb C\). Every skew-symmetric matrix over a field of characteristic different from two has even rank. For even \(S\), its size \(S-1\) is odd, so its rank is at most \(S-2\); the lower bound in Step 3 is therefore exact. The resulting rank is \(2\lfloor(S-1)/2\rfloor\) in both parity cases.

**5. Wronskian degree and square zero.** The Wronskian changes only by the nonzero determinant under a basis change of the two centered polynomials. With the row-reduced basis, the leading term of \(u'v-uv'\) is \((r-s)u_rv_s z^{r+s-1}\), which cannot cancel. Therefore \(\deg W_{a,b}=r+s-1\), proving the stated rank formula. If \(W_{a,b}=0\) and neither centered polynomial is zero, their ratio is constant wherever defined (since its derivative is zero), so the symbols are affinely dependent and the commutator is zero. Finally, Step 1 proves that every commutator maps into the analytic summand and vanishes there, whence its square is zero.

## Verification

The accompanying standalone script `check_rank.py` uses only Python's standard library. It constructs each Toeplitz composition directly from the projected monomial action, forms the finite anti-analytic-to-analytic matrix with exact rational coefficients, and computes its rank by exact Gaussian elimination. It computes the centered Wronskian degree independently by polynomial arithmetic, checks the rank identity, and verifies the weighted skew-symmetry identity. Its deterministic suite contains \(729\) pairs of degree-at-most-two polynomials with coefficients in \(\{-1,0,1\}\) and \(576\) seeded integer-coefficient polynomial pairs of degrees one through eight, for \(1305\) exact checks in total. Successful finite diagnostics do not establish the theorem for arbitrary degrees; Steps 1–5 do.

## Relationship to prior work

Cui, Huang, Lu, and Zu (2026), Theorem 1.1 and Corollary 3.1, characterize which bounded harmonic symbols have finite-rank commutators and prove square-zero in that general setting. Their Example 3.4 states the \([T_z,T_{z^2}]\) rank-two case, and Example 3.5 treats a rational symbol. The present polynomial-pair formula adds the exact rank for every pair, including cancellations between many monomial contributions, rather than a criterion for mere finiteness.

Dong and Zhou (2014/2016), particularly their Section 4, obtain ranks and canonical forms for quasihomogeneous Toeplitz operators; individual analytic monomials lie in that family. Their results do not directly treat simultaneous lower-degree polynomial perturbations of both symbols. Chen, Koo, and Lee (2013) establish even-rank necessity and realizability of every nonnegative even rank. That parity fact is used here only as motivation: the proof of the formula gives an independent skew-symmetry argument.

## Limitations

The result is confined to analytic polynomials on the unweighted harmonic Bergman disk. It does not classify exact ranks for nonpolynomial rational primitives, mixed analytic/coanalytic symbols, or other underlying measures. No optimal singular-value law is claimed. The 2013 rank paper was accessible only by its abstract in the available comparison; its full text could contain an equivalent polynomial-pair calculation. The comparisons support a qualified originality assessment, not a universal priority guarantee. The verification code is finite and is not a substitute for the proof. No independent mathematical audit has been performed.

## References

1. P. Cui, Z. Huang, Y. Lu, C. Zu, *Finite-rank Toeplitz commutators on the harmonic Bergman space*, arXiv:2611.08988v1 (first public version, 6 November 2026). https://arxiv.org/html/2611.08988v1
2. X.-T. Dong and Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213v3. https://arxiv.org/html/1411.0213v3
3. Y. Chen, H. Koo and Y. J. Lee, *Ranks of commutators of Toeplitz operators on the harmonic Bergman space*, Integral Equations and Operator Theory 75 (2013), 31–38, doi:10.1007/s00020-012-2020-6. https://doi.org/10.1007/s00020-012-2020-6
