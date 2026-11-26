# A complete fixed-rank singular-value hierarchy for high-order Volterra integration

## Finding

Let \(I^\alpha\) denote Riemann–Liouville integration of real order \(\alpha>1\) on \(L^2(0,1)\), and let \(T_\alpha=\Gamma(\alpha+1)I^\alpha\). Denote its singular values, with multiplicity and in nonincreasing order, by \(s_1(T_\alpha),s_2(T_\alpha),\ldots\). For every **fixed** integer \(j\ge1\),

\[
\lim_{\alpha\to+\infty}\alpha^{j(j-1)/2}\prod_{r=1}^{j}s_r(T_\alpha)
=\frac{\prod_{k=0}^{j-1}k!}{2^{j^2}}.
\tag{1}
\]

Consequently, for every fixed integer \(j\ge1\),

\[
\boxed{\displaystyle\lim_{\alpha\to+\infty}\alpha^{j-1}s_j(T_\alpha)
=\frac{(j-1)!}{2^{2j-1}}.}
\tag{2}
\]

The contribution considered here begins at \(j=3\): \(s_3(T_\alpha)\sim(16\alpha^2)^{-1}\) and \(s_4(T_\alpha)\sim 3/(64\alpha^3)\). The leading rank-one and second-rank statements are included in (1)–(2) to express the complete hierarchy, but are known and are not asserted to be original.

## Assumptions and scope

For each real \(\alpha>1\) define the bounded compact operator on real or complex \(L^2(0,1)\)

\[
(I^\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}f(t)\,dt,
\qquad 0<x<1.
\]

Here \(\Gamma\) is Euler's gamma function. All asymptotics take \(\alpha\to+\infty\) with the singular-value rank \(j\) held fixed. For integer \(\alpha=m\), the operator \(I^m\) is the \(m\)-th power of the classical Volterra integration operator. No uniform statement for ranks increasing with \(\alpha\) is made.

## Proof

**1. Symmetric boundary-layer normal form.** Multiplication by \(\Gamma(\alpha+1)\) gives the kernel \(\alpha(x-t)^{\alpha-1}\mathbf1_{0<t<x<1}\). Use \(u=\alpha(1-x)\) in the output and \(v=\alpha t\) in the input. The corresponding coordinate maps (including unitary square-root Jacobians), followed by zero extension outside \((0,\alpha)\), preserve nonzero singular values and produce a real symmetric Hankel operator \(K_\alpha\) on \(L^2(0,\infty)\) with kernel

\[
h_\alpha(u+v)=\left(1-\frac{u+v}{\alpha}\right)_+^{\alpha-1},\quad u,v\ge0.
\tag{3}
\]

Thus \(s_r(K_\alpha)=s_r(T_\alpha)\) for each \(r\). For \(\alpha\ge2\), \(0\le h_\alpha(s)\le e^{-s/2}\) for all \(s\ge0\), ensuring Hilbert–Schmidt bounds and exponential localization.

**2. The exterior-power determinant.** Fix \(j\ge1\) and write \(J=j(j-1)/2\). Use the ordered simplex

\[
\Omega_j=\{(u_1,\ldots,u_j):0<u_1<\cdots<u_j<\infty\}.
\]

In its usual normalized antisymmetric representation, the operator \(\bigwedge^j K_\alpha\) has the integral kernel

\[
D_{\alpha,j}(U,V)=\det[h_\alpha(u_a+v_b)]_{a,b=1}^{j}
\quad(U,V\in\Omega_j),
\tag{4}
\]

and operator norm

\[
\|\bigwedge^j K_\alpha\|=\prod_{r=1}^j s_r(K_\alpha).
\tag{5}
\]

(The determinant in (4) is **not** multiplied by \(1/j!\): restricting the antisymmetric tensor to \(\Omega_j\) supplies the normalization.)

**3. Vandermonde determinant limit.** Define \(\Delta(U)=\prod_{a<b}(u_b-u_a)\). The crucial fixed-dimensional limit is

\[
\alpha^J D_{\alpha,j}(U,V)\longrightarrow
\frac{(-1)^J}{\prod_{k=0}^{j-1}k!}
\,e^{-\sum_a u_a-\sum_b v_b}\Delta(U)\Delta(V)
\tag{6}
\]

in \(L^2(\Omega_j\times\Omega_j)\), not merely at individual tuples. Here is a detailed justification of the nonstandard determinant step.

For \(u+v<\alpha\), factor \(h_\alpha(u+v)=a_\alpha(u)a_\alpha(v)g_\varepsilon(u,v)\), where \(a_\alpha(u)=h_\alpha(u)\) and \(\varepsilon=1/\alpha\). At \(\varepsilon=0\) the remaining kernel extends analytically on each bounded rectangle, with

\[
\log g_\varepsilon(u,v)
=\sum_{r\ge1}\varepsilon^r Q_r(u,v),\qquad
Q_1(u,v)=-uv,
\tag{7}
\]

Indeed, the exact expression is

\[
\log g_\varepsilon=(\varepsilon^{-1}-1)
\left[\log(1-\varepsilon(u+v))
-\log(1-\varepsilon u)-\log(1-\varepsilon v)\right].
\tag{8}
\]

At order \(\varepsilon^r\), the bracket and prefactor in (8) give mixed monomials of total degree \(r+1\) or \(r\); each therefore has degree at most \(r\) in **each** variable. Both degrees can equal \(r\) only when \(r=1\), for the term \(-\varepsilon uv\). This bound in each variable is preserved by exponentiation: the coefficient of \(u^a v^b\) in the resulting formal series starts at order at least \(\max(a,b)\). Attaining bidegree \((k,k)\) at order \(\varepsilon^k\) requires every factor to attain equality in both degrees, so the leading diagonal coefficient is \((-1)^k/k!\). Pure coefficients vanish except for the constant \(1\).

Apply Cauchy–Binet to the finite monomial coefficient matrix of the kernel truncated in \(\varepsilon\) through order \(J\). Given distinct row degrees \(a_1<\cdots<a_j\) and column degrees \(b_1<\cdots<b_j\), a matching \(\sigma\) contributes only at order at least \(\sum_i\max(a_i,b_{\sigma(i)})\), which is at least each of \(\sum_i a_i\) and \(\sum_i b_i\). Both sums are at least \(J\), with equality only for the degree set \(0,1,\ldots,j-1\). For these sets the bound equals \(J\) only for the diagonal matching. Thus the determinant has no coefficients below order \(J\), and at that order its coefficient is \((-1)^J\Delta(U)\Delta(V)/\prod_{k<j}k!\).

For a uniform remainder, take \(0\le u_a,v_b\le R\) and the complex disc \(|\varepsilon|\le \rho_R=[8(1+R)^2]^{-1}\). Then \(|\varepsilon|(u+v)\le 1/4\), and the bracket in (8) has no linear term. The sum of the absolute values of its terms is \(O(|\varepsilon|^2 R^2)\) by the logarithm series. Consequently \(|\log g_\varepsilon|\le C|\varepsilon|R^2\), with absolute \(C\), so \(\det[g_\varepsilon(u_a,v_b)]\) is bounded by a constant depending only on \(j\) on the disc. Cauchy's coefficient estimate and a geometric sum bound the remainder after order \(J\) by \(O_j(|\varepsilon|^{J+1}(1+R)^{2J+2})\) for \(|\varepsilon|\le\rho_R/2\).

Now take \(R=R_\alpha=C_j\log\alpha\), with \(C_j>2J+2\). For sufficiently large \(\alpha\), \(2R<\alpha\) and \(\varepsilon=1/\alpha\le\rho_R/2\). The same logarithm series gives \(\log a_\alpha(u)+u=O(\alpha^{-1}(1+R)^2)\) uniformly for \(0\le u\le R\). Hence, after factoring out \(e^{-\sum_a u_a-\sum_b v_b}\), the difference between the scaled determinant and the right side of (6) is uniformly \(O_j(\alpha^{-1}(1+R)^{2J+2})\) on this box, using \(|\Delta(U)\Delta(V)|\le (1+R)^{2J}\). The error on the box tends to zero in \(L^2\) because the extracted exponential is square-integrable on the entire orthant.

For the complement where any variable exceeds \(R_\alpha\), the determinant bound \(|D_{\alpha,j}(U,V)|\le j!e^{-(\sum_a u_a+\sum_b v_b)/2}\) yields a squared tail for the scaled determinant bounded by \(O_j(\alpha^{2J}e^{-R_\alpha})=o(1)\). The limiting right side of (6) is an exponential times a polynomial and is square-integrable, so its squared tail also tends to zero. This proves (6) in Hilbert–Schmidt kernel norm.

**4. An exact Laguerre norm.** The operator with limiting kernel (6) is rank one. Let \(F_j(U)=e^{-\sum_a u_a}\Delta(U)\). The squared \(L^2(\Omega_j)\)-norm is the Hankel moment determinant

\[
\|F_j\|_2^2
=\det\left[\int_0^\infty u^{a+b}e^{-2u}\,du\right]_{a,b=0}^{j-1}
=\det\left[\frac{(a+b)!}{2^{a+b+1}}\right]_{a,b=0}^{j-1}.
\tag{9}
\]

Andréief's determinant identity gives the first equality (the ordered simplex absorbs the factorial). Orthogonalizing \(1,u,\ldots,u^{j-1}\) against \(e^{-2u}\,du\) gives monic scaled Laguerre polynomials with squared norms \((k!)^2/2^{2k+1}\), hence

\[
\|F_j\|_2^2=\frac{\prod_{k=0}^{j-1}(k!)^2}{2^{j^2}}.
\tag{10}
\]

By (6), (5), and the Hilbert–Schmidt bound on operator norm, the limit of \(\alpha^J\prod_{r\le j}s_r(T_\alpha)\) is \(\|F_j\|^2/\prod_{k<j}k!\), namely the right side of (1). For \(j=1\) the same calculation yields \(1/2\). Dividing (1) for rank \(j\) by (1) for rank \(j-1\) establishes (2), completing the proof.

## Verification

The accompanying standalone `check_spectrum.py` computes the exact-rational Gram determinants in (9) for ranks \(1\) through \(8\), and separately performs finite Gauss–Laguerre Nyström computations of the Hankel operator (3) at orders \(\alpha=80,160,320\). It tests the first four scaled singular values against the constants in (2), and checks the exact Hilbert–Schmidt squared mass \(\|T_\alpha\|_{\mathcal S_2}^2=(4-2/\alpha)^{-1}\). The checks passed in the prepared package. Run `python check_spectrum.py` with Python 3, SymPy, NumPy and SciPy installed. All finite tests are diagnostic; the proof for every fixed rank is (6)–(10).

## Relationship to prior work

Eveson's 2003 and 2004 papers establish the leading rank-one behavior of large Volterra powers, and Ransford–Walsh (first posted 20 June 2022) studies norms of polynomials of the same operator. Those findings are not claimed as original here. The dated public summary in reference 4 gives \(s_2(T_\alpha)\sim1/(8\alpha)\) and an \(O(\alpha^{-2})\) rank-two approximation error in Hilbert–Schmidt norm; those statements imply only an *upper bound* on the third singular value, not the exact coefficient \(1/16\) or the subsequent hierarchy. The distinction from these results is the sharp law at every fixed rank \(j\ge3\), obtained by an exterior-power determinant limit. Classical Tuan–Gorenflo singular-value asymptotics take the singular-value **index** to infinity at fixed integration order, not the limit proved here.

## Limitations

Rank is fixed before the integration order tends to infinity. No uniformity in growing rank, no finite-order exact singular spectrum, and no rate in (2) beyond the established convergence is asserted. The method uses antisymmetric tensor powers and does not directly provide individual eigenvalue signs. A potentially relevant historical article by Dostanić (2001) was accessible only in abstract form; an equivalent specialization in unindexed literature cannot be excluded.

## References

1. T. Ransford and N. Walsh, *Norms of polynomials of the Volterra operator*, arXiv:2206.09947v1 (20 June 2022), https://arxiv.org/abs/2206.09947.
2. S. P. Eveson, *Norms of iterates of Volterra operators on* \(L^2\), J. Operator Theory 50 (2003), 369–386, https://jot.theta.ro/jot/archive/2003-050-002/2003-050-002-010.pdf.
3. S. P. Eveson, *Asymptotic behaviour of iterates of Volterra operators on* \(L^p(0,1)\), arXiv:math/0409516v1 (27 September 2004), https://arxiv.org/abs/math/0409516.
4. *Sharp second singular asymptotics and rank-two collapse for high Volterra powers*, public result summary (18 October 2026), https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-sharp-second-singular-asymptotics-and-rank-two-collapse-for-high--3619ccb23ef6.
5. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numer. Funct. Anal. Optim. 17 (1996), 453–461, https://doi.org/10.1080/01630569608816704.
6. M. R. Dostanić, *Estimates for the norm of powers of Volterra's operator through its singular values*, Math. Z. 236 (2001), https://doi.org/10.1007/PL00004837 (abstract consulted; full text not assessed).
