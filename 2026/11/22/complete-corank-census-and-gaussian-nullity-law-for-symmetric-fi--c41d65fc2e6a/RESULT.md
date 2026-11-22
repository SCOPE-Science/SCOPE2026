# Complete corank census and Gaussian nullity law for symmetric finite-field tridiagonal matrices

## Finding

For each prime power \(q\ge2\), let \(\mathcal T_n(q)\) consist of all symmetric \(n\times n\) matrices over \(\mathbb F_q\) whose entries vanish outside the three central diagonals. All \(2n-1\) free entries are unrestricted. Define the corank polynomial

\[
Z_{n,q}(t)=\sum_{A\in\mathcal T_n(q)}t^{\dim_{\mathbb F_q}\ker A},\qquad Z_{0,q}(t)=1.
\]

For every \(q\) and all \(n\ge0\), the complete corank census is

\[
\boxed{\sum_{n\ge0}Z_{n,q}(t)z^n=
\frac{1-(q-1)^2z-q(q-1)^2z^2}
{1-\big(q(q-1)+t\big)z-q^2(q-1)z^2}.}
\]

In particular, \(Z_{1,q}(t)=q-1+t\), \(Z_{2,q}(t)=q^2(q-1)+(q^2-1)t+t^2\), and for every \(n\ge3\)

\[
Z_{n,q}(t)=\big(q(q-1)+t\big)Z_{n-1,q}(t)+q^2(q-1)Z_{n-2,q}(t).
\]

The coefficient \([t^k]Z_{n,q}(t)\) counts exactly the matrices of nullity \(k\), for every \(0\le k\le n\). In particular \(Z_{n,q}(1)=q^{2n-1}\) for \(n\ge1\).

Let \(K_{n,q}\) be the nullity of a uniformly chosen matrix from \(\mathcal T_n(q)\), with \(q\) fixed. Put

\[
\delta_q=q^2+q-1,\qquad
\mu_q=\frac1{\delta_q},\qquad
\sigma_q^2=\frac1{\delta_q}-\frac{q^2-q+1}{\delta_q^3}>0.
\]

Then

\[
\mathbb E K_{n,q}=\mu_q n+O_q(1),\qquad
\operatorname{Var}(K_{n,q})=\sigma_q^2n+O_q(1),
\]

and the central limit theorem holds:

\[
\frac{K_{n,q}-\mu_q n}{\sigma_q\sqrt n}
\xrightarrow[n\to\infty]{\mathrm{law}}\mathcal N(0,1).
\]

Thus the corank of a uniformly chosen sparse symmetric tridiagonal matrix grows linearly with dimension and fluctuates on the square-root scale, in contrast with the tight corank of uniformly chosen dense symmetric matrices.

## Assumptions and scope

The field has arbitrary prime-power size \(q\ge2\) and arbitrary characteristic. Symmetry requires each subdiagonal entry to equal its corresponding superdiagonal entry. Entries on the diagonal and on the subdiagonal are independent and uniform; *zero offdiagonal entries are included*. The corank is taken over the same field. The generating function is a formal identity in \(\mathbb Z[t][[z]]\) for each fixed \(q\). The asymptotic limit holds with \(q\) fixed and \(n\to\infty\); no simultaneous field-size limit is claimed.

## Proof

**Step 1: irreducible tridiagonal blocks have corank at most one.** Fix \(\ell\ge1\) and nonzero offdiagonal entries \(b_1,\ldots,b_{\ell-1}\in\mathbb F_q^\times\). Let \(d_i\) denote the determinant of the leading \(i\times i\) block, with \(d_0=1\) and \(d_1=a_1\). Expansion along the final row gives

\[
d_i=a_i d_{i-1}-b_{i-1}^2d_{i-2}\quad (i\ge2).
\]

If \(d_{i-1}=0\), then \(d_{i-2}\ne0\), by induction: two consecutive continuants cannot vanish because \(b_{i-1}\ne0\), and the initial \(d_0=1\). Equivalently, the homogeneous equation \(A v=0\) successively determines all coordinates of \(v\) from its first coordinate since each \(b_i\) is invertible. Hence the kernel has dimension at most one, and it is one-dimensional precisely when \(d_\ell=0\).

**Step 2: exact singular-block count.** For each fixed sequence of nonzero offdiagonal entries, the diagonal coefficients are independent uniform variables. Conditional on \(d_{i-1}\ne0\), exactly one value of \(a_i\) makes \(d_i=0\); conditional on \(d_{i-1}=0\), none does. Thus if \(p_i=\Pr(d_i=0)\), then \(p_0=0\) and

\[
p_i=\frac{1-p_{i-1}}q,
\qquad p_i=\frac{1-(-q^{-1})^i}{q+1}.
\]

For each prescribed nonzero offdiagonal sequence, the numbers of diagonal choices giving corank one and zero are respectively

\[
s_\ell=\frac{q^\ell-(-1)^\ell}{q+1},\qquad
r_\ell=\frac{q^{\ell+1}+(-1)^\ell}{q+1}.
\]

These are nonnegative integers and sum to \(q^\ell\). The values are independent of the fixed nonzero offdiagonal coefficients, even in characteristic two.

**Step 3: unique block decomposition.** Every matrix in \(\mathcal T_n(q)\) splits uniquely at its zero offdiagonal entries into a nonempty ordered sequence of maximal irreducible tridiagonal blocks of positive lengths summing to \(n\). A block of size \(\ell\) has \((q-1)^{\ell-1}\) choices for its nonzero internal offdiagonal coefficients, and has corank generating weight

\[
w_\ell(t)=(q-1)^{\ell-1}(r_\ell+s_\ell t).
\]

The intervening zero offdiagonal entries contribute exactly one choice; block nullities add. Thus for

\[
B_q(z,t)=\sum_{\ell\ge1}w_\ell(t)z^\ell,
\]

we have \(\sum_{n\ge0}Z_{n,q}(t)z^n=(1-B_q(z,t))^{-1}\). Summing the two geometric series gives

\[
B_q(z,t)=\frac{z\big(q-1+t+q(q-1)z\big)}
{\big(1+(q-1)z\big)\big(1-q(q-1)z\big)},
\]

and algebraic simplification yields the displayed rational bivariate generating function. Coefficient comparison gives the initial cases and recurrence; substituting \(t=1\) recovers \(q^{2n-1}\).

**Step 4: quantitative Gaussian limit.** Let

\[
a_q(t)=q(q-1)+t,\qquad
\lambda_\pm(t)=\frac{a_q(t)\pm\sqrt{a_q(t)^2+4q^2(q-1)}}2.
\]

Choose the positive real square root near \(t=1\). There \(\lambda_+(1)=q^2\) and \(\lambda_-(1)=-(q-1)\), with \(|\lambda_-(1)|<\lambda_+(1)\). Partial fractions of the rational generating function consequently give

\[
Z_{n,q}(t)=c_q(t)\lambda_+(t)^n+d_q(t)\lambda_-(t)^n,
\]

for analytic coefficient functions near \(t=1\), with \(c_q(1)\ne0\). The latter follows directly from the numerator evaluated at \(z=q^{-2}\): \((1+(q-1)q^{-2})(1-(q-1)q^{-1})\ne0\). Therefore, uniformly in a complex neighborhood of \(s=0\),

\[
\mathbb E e^{sK_{n,q}}
=\frac{c_q(e^s)}{c_q(1)}
\left(\frac{\lambda_+(e^s)}{q^2}\right)^n(1+O_q(\rho^n))
\]

for some \(0<\rho<1\). Implicit differentiation of \(\lambda^2-a_q(t)\lambda-q^2(q-1)=0\) gives \(\lambda_+'(1)/\lambda_+(1)=1/\delta_q\) and

\[
\left.\frac{d^2}{ds^2}\log\lambda_+(e^s)\right|_{s=0}
=\frac1{\delta_q}-\frac{q^2-q+1}{\delta_q^3}=\sigma_q^2.
\]

The variance constant is positive because \(\delta_q^2>q^2-q+1\) for \(q\ge2\). Differentiating the moment generating function gives the stated mean and variance with bounded errors. For fixed real \(u\), insert \(s=iu/(\sigma_q\sqrt n)\), subtract the linear term and expand the analytic logarithm to third order. The centered characteristic functions tend to \(e^{-u^2/2}\), proving the central limit theorem by the continuity theorem.

## Verification

The standalone script `check_tridiagonal.py` constructs every symmetric tridiagonal matrix at 18 finite field-size and matrix-size pairs, computes its rank by Gaussian elimination independently of the continuant derivation, and compares the complete histogram to the polynomial recurrence. It covers field orders \(2,3,4,5,7\), including the nonprime extension field \(\mathbb F_4\), and checks 9,887 matrices in total. Its captured, independently replayable output is `check_output.txt`.

To reproduce, run `python3 check_tridiagonal.py` in a directory containing that script. The checker is finite evidence only; the arbitrary-size and asymptotic assertions are established by the algebraic and analytic proof above.

## Relationship to prior work

Fulman and Goldstein, first circulated in November 2012, study the rank distributions of full finite-field random-matrix ensembles, including unrestricted symmetric matrices, where the nullity has a tight limiting law. The banded symmetric family here is not one of their ensembles, and instead has positive corank density.

Safarji, O'Brien and Quinlan (2025), Theorem 2.2, already determine the two possible ranks for matrices representing the connected path graph over \(\mathbb F_2\) (equivalently this construction conditional on every offdiagonal being nonzero when \(q=2\)); this conditional binary result is credited and not claimed as new. The unrestricted-zero-edge all-field composition, its rational bivariate polynomial, and its central limit law are different claims.

Martínez-Moro, Rodnit and Jitman (arXiv September 2025; journal 2026), Theorems 2.1–2.2, determine the *invertible* symmetric tridiagonal counts (precisely the specialization \(t=0\) here) and extend prescribed determinant counts to chain rings. Their manuscript's finite-field determinant-value theorem does not state or imply the coefficients of positive powers of \(t\), because all singular coranks are aggregated at determinant zero. Jitman and Sricharoen (2024) likewise study prescribed determinants, generally for nonsymmetric tridiagonal matrices. No priority is claimed for the already known invertible specialization or the connected-path binary case.

## Limitations

The result only concerns symmetric tridiagonal matrices over finite *fields* with uniform unrestricted entries, not general zero-pattern graphs, fixed nonzero offdiagonals, nonsymmetric matrices, finite chain rings, or simultaneous field-size and dimension limits. The proposed historical distinction concerns the full corank polynomial and its Gaussian law; the invertible specialization and connected-path binary rank counts are known. An unindexed or indirectly equivalent all-rank formula could narrow historical originality. The computational tests do not certify the infinite theorem independently.

## References

1. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, first posted 2012-11-02; *Annals of Probability* 43 (2015), 1274–1314. https://arxiv.org/abs/1211.0504
2. B. Safarji, C. O'Brien and R. Quinlan, *The rank distribution of matrices representing graphs with a long induced path over the field of two elements*, arXiv:2509.10332, 2025-09-12, especially §2 and Theorem 2.2. https://arxiv.org/html/2509.10332v1
3. E. Martínez-Moro, N. Rodnit and S. Jitman, *On the enumeration of symmetric tridiagonal matrices with prescribed determinant over commutative finite chain rings*, arXiv:2509.17719, 2025-09-22, especially §2, Theorems 2.1–2.2 and Corollary 2.3. https://www.degruyterbrill.com/document/doi/10.1515/spma-2025-0049/html
4. S. Jitman and Y. Sricharoen, *Determinants of tridiagonal matrices over some commutative finite chain rings*, *Special Matrices* 12 (2024). https://www.degruyterbrill.com/document/doi/10.1515/spma-2023-0114/html
