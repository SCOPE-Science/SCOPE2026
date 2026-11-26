# Exact joint ternary valuation law and covariance identity for central binomial and three-way multinomial coefficients

## Finding
For any integer \(L\ge1\), sample \(N\) uniformly from the integers \(0\le N<3^L\). Let
\[
X=\nu_3\!\left(\binom{2N}{N}\right),\qquad Y=\nu_3\!\left(\frac{(3N)!}{(N!)^3}\right).
\]
At \(N=0\), both valuations are zero. Define \(F_L(u,v)=\sum_{0\le n<3^L}u^{X(n)}v^{Y(n)}\). The **complete exact bivariate distribution** is
\[
F_L(u,v)=(1,0)\begin{pmatrix}1+v&uv^2\\1&u(v+v^2)\end{pmatrix}^{L}\binom11.
\]
The arithmetic valuation covariance satisfies the unexpectedly exact identity
\[
\boxed{\operatorname{Cov}(X,Y)=\mathbb EX=\frac L2-\frac{1-3^{-L}}4.}
\]
Moreover,
\[
\mathbb EY=L,\quad \operatorname{Var}Y=\frac{2L}3,\quad
\operatorname{Var}X=\frac L2-\frac7{16}+\frac{3^{-L}}2-\frac{3^{-2L}}{16}.
\]
The pair \(((X-L/2)/\sqrt L,(Y-L)/\sqrt L)\) converges in law to the centered Gaussian with covariance matrix
\[\Sigma=\begin{pmatrix}1/2&1/2\\1/2&2/3\end{pmatrix};\]
its correlation is \(\sqrt3/2\), strictly less than one.

## Assumptions and scope
\(L\) is any positive integer; \(\nu_3\) is the exponent of three in a positive integer. The random variable \(N\) is uniform over **exactly** the first \(3^L\) nonnegative integers. The three-way multinomial counts ordered assignments to three equal-size groups, **not** the coefficient of a power of a trinomial. No other primes or sampling intervals are asserted.

## Proof
Write the independent base-three digits of \(N\), least-significant first, as \(d_1,\ldots,d_L\in\{0,1,2\}\). By Legendre's factorial valuation formula, and \(s_3(3N)=s_3(N)\),
\[Y=\frac{3s_3(N)-s_3(3N)}2=s_3(N)=\sum_{j=1}^L d_j.\]
By Kummer's theorem, \(X\) is the number of carries when adding \(N+N\) in base three. With initial carry \(c_0=0\), the outgoing carry is \(c_j=\lfloor(2d_j+c_{j-1})/3\rfloor\in\{0,1\}\), so \(X=\sum_{j=1}^Lc_j\). A digit adds a factor \(u^{c_j}v^{d_j}\) and changes carry state; summing over all three possibilities gives the displayed \(2\)-state matrix, proving the exact joint generating polynomial.

For the covariance, \(\Pr(c_j=1)=(1-3^{-j})/2\), because the carry transition matrix is \(3^{-1}\begin{pmatrix}2&1\\1&2\end{pmatrix}\). For any \(i\ge j\), independence of \(d_j\) from the incoming carry gives \(\operatorname{Cov}(c_j,d_j)=1/3\). The conditional expectation \(\mathbb E(c_i\mid c_j)=1/2+(c_j-1/2)3^{-(i-j)}\) yields
\[
\operatorname{Cov}(c_i,d_j)=3^{-(i-j+1)}\ (i\ge j),\qquad \operatorname{Cov}(c_i,d_j)=0\ (i<j).
\]
Consequently
\[
\operatorname{Cov}(X,Y)=\sum_{i=1}^L\sum_{j=1}^i3^{-(i-j+1)}=\frac12\sum_{i=1}^L(1-3^{-i})=\mathbb EX.
\]
The ternary digits are independent with mean one and variance \(2/3\), yielding the formulas for \(\mathbb EY\) and \(\operatorname{Var}Y\). For \(i\le j\), \(\operatorname{Cov}(c_i,c_j)=3^{-(j-i)}(1-3^{-2i})/4\). Summing all pairs gives
\[
\operatorname{Var}X=\frac14\sum_{i=1}^L(1-3^{-2i})(2-3^{-(L-i)})=\frac L2-\frac7{16}+\frac{3^{-L}}2-\frac{3^{-2L}}{16}.
\]
For the joint central limit theorem, the polynomial matrix above is analytic near \((u,v)=(1,1)\). There its eigenvalues are \(3\) and \(1\); the simple dominant eigenvalue supplies, via analytic perturbation and the moment-generating function, a Gaussian limit with the displayed covariance matrix, as read from the just-computed exact second cumulants. Its determinant is \(1/12>0\), giving a nondegenerate limit. (Equivalently use the additive-functional CLT for the finite irreducible aperiodic carry chain.)

## Verification
A standalone integer-arithmetic verifier \(`verify.py`\) builds the full two-state transfer distribution for \(1\le L\le12\), checks the exact expectations, variances and covariance as rational numbers, and for \(1\le L\le7\) independently enumerates factorial valuations for every \(n<3^L\). It prints \(`VERIFY_OK`\). This finite check supports, but does not replace, the proof for all \(L\).

## Relationship to prior work
Kummer's carry theorem (1852) and Legendre's factorial-valuation formula are classical and not new. Barat and Grabner developed general digital-block machinery for binomial and multinomial coefficient valuations, and in their Section 5 explicitly discuss multinomial extensions. Straub, Amdeberhan and Moll treat distinct generalized central-binomial valuations. The contribution isolated here is the explicit **joint** coefficient law for the same \(n\) and the exact finite-length covariance identity (plus its limiting nontrivial correlation); general digital transfer machinery alone does not provide these evaluated constants. Priority risk remains from specialized carry-correlation literature not completely located.

## Limitations
The computation is restricted to the ternary prime and equal three-way multinomial counts over complete initial ternary blocks. The Gaussian limit is an asymptotic statement, not a finite sample normality claim. No independent mathematical audit has been performed. The literature survey cannot establish universal priority.

## References
1. E. E. Kummer, 1852, valuation of binomial coefficients via carries.
2. A.-M. Legendre, *Théorie des nombres*, 1798, factorial valuations.
3. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, J. London Math. Soc. 64 (2001), 523–547, DOI 10.1112/S0024610701002630, accessible manuscript https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf.
4. A. Straub, T. Amdeberhan and V. H. Moll, *The p-adic valuation of k-central binomial coefficients*, arXiv:0811.2028v1 (2008-11-13), https://arxiv.org/html/0811.2028v1.
