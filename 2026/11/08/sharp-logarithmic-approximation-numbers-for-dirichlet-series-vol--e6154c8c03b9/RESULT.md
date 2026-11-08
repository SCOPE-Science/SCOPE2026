# Sharp logarithmic approximation numbers for Dirichlet-series Volterra operators

## Finding
Let \(\mathscr H^2\) be the Hardy Hilbert space of ordinary Dirichlet series with orthonormal basis \(e_n(s)=n^{-s}\), \(n\ge1\). Let \(g(s)=b_1+\sum_{m\in F}b_m m^{-s}\), where \(F\) is a nonempty finite subset of the integers \(m\ge2\), the coefficients are complex and at least one \(b_m\ne0\). Let
\[
(T_gf)(s)=-\int_s^{+\infty}f(w)g'(w)\,dw.
\]
If \(p_1,\ldots,p_r\) are the distinct primes dividing members of \(F\), write \(m=p_1^{\alpha_1(m)}\cdots p_r^{\alpha_r(m)}\) and define the polynomial
\[
P_g(z_1,\ldots,z_r)=\sum_{m\in F}b_m(\log m)z_1^{\alpha_1(m)}\cdots z_r^{\alpha_r(m)}.
\]
Set \(C_g=\max_{|z_1|=\cdots=|z_r|=1}|P_g(z)|>0\). If \(s_n(T_g)\) denotes the \(n\)-th singular value in nonincreasing order, with multiplicity, then
\[
\boxed{\lim_{n\to\infty}(\log n)s_n(T_g)=C_g.}
\]
Consequently, with \(N_g(t)=\#\{n\ge1:s_n(T_g)>t\}\),
\[
\boxed{\lim_{t\downarrow0}t\log N_g(t)=C_g.}
\]
In particular \(T_g\) is compact, but belongs to no finite Schatten class \(\mathcal S_p\) with \(p>0\). This last non-Schatten conclusion was previously known; the sharp coefficient and counting asymptotic are the new assertions.

For a single nonconstant monomial \(g(s)=b m^{-s}\), the exact sequence is \(s_n(T_g)=|b|\log(m)/\log(mn)\), \(n\ge1\). For \(g(s)=2^{-s}+3^{-s}\), the theorem gives the nontrivial two-prime coefficient \(C_g=\log6\).

## Assumptions and scope
The coefficients \(b_m\) are arbitrary complex numbers and \(F\) is finite and nonempty. The constant term of \(g\) does not affect \(T_g\). All logarithms are natural, and \(\mathscr H^2\) has the usual coefficient norm \(\|\sum_{n\ge1}a_n n^{-s}\|^2=\sum_{n\ge1}|a_n|^2\). The conclusion concerns approximation numbers of the compact operator on this Hilbert space; these equal its singular values. It does not assert the same constant on Banach Hardy spaces or on weighted Bergman spaces of Dirichlet series.

## Proof
**1. Exact operator factorization.** For each \(n\ge1\), direct integration gives
\[
T_ge_n=\sum_{m\in F}\frac{b_m\log m}{\log(mn)}e_{mn}.
\]
Let \(B\) denote multiplication by the Dirichlet polynomial \(\sum_{m\in F}b_m(\log m)m^{-s}\), or equivalently the finite multiplicative shift \(Be_n=\sum_{m\in F}b_m(\log m)e_{mn}\). Let \(D e_1=0\), \(D e_k=(\log k)^{-1}e_k\) for \(k\ge2\). Then \(T_g=DB\). The diagonal operator \(D\) is compact. Hence \(T_g\) is compact.

**2. The sharp multiplier norm.** Set \(Q=p_1\cdots p_r\). Every positive integer has a unique factorization \(n=au\), where \(\gcd(a,Q)=1\) and \(u\) has prime factors only among \(p_1,\ldots,p_r\). Accordingly, \(\ell^2(\mathbb N)\) is the orthogonal sum over such \(a\) of spaces \(\mathcal H_a\), each unitarily identified with \(H^2(\mathbb D^r)\) by \(e_{au}\mapsto z^{\alpha(u)}\). On every \(\mathcal H_a\), the restriction of \(B\) is multiplication by \(P_g\). Thus
\[
\|B\|=\|M_{P_g}\|=\max_{z\in\mathbb T^r}|P_g(z)|=C_g.
\]
For the last equality, the upper bound follows from Hardy-space boundary integration; for the lower bound use normalized reproducing kernels at \(\rho z\) and let \(\rho\uparrow1\), where \(z\in\mathbb T^r\) maximizes \(|P_g|\).

**3. Singular-value upper bound.** Denote by \(E_N\) the projection onto the span of \(e_1,\ldots,e_N\). Since every multiplier index \(m\ge2\), the outputs of \(B(I-E_N)\) are supported on integers at least \(2(N+1)\). Hence
\[
\|T_g(I-E_N)\|\le\frac{C_g}{\log(2N+2)}.
\]
Since \(T_gE_N\) has rank at most \(N\), the min-max/approximation-number formula gives
\[
s_{N+1}(T_g)\le\frac{C_g}{\log(2N+2)}.
\]
Therefore \(\limsup_{n\to\infty}(\log n)s_n(T_g)\le C_g\).

**4. Lower bound from positive-density copies of one near-extremizer.** Fix \(\varepsilon>0\). By density of polynomials in \(H^2(\mathbb D^r)\), choose a finite-support vector \(h=\sum_{u\in U}c_u e_u\), supported on integers whose prime factors divide \(Q\), such that \(\|h\|=1\) and \(\|Bh\|>C_g-\varepsilon\). The vector \(Bh\) also has finite support \(V\). For every \(a\ge1\) coprime to \(Q\), define \(h_a=\sum_{u\in U}c_u e_{au}\). Then \(\|h_a\|=1\), and distinct such \(a\) have mutually orthogonal supports, both before and after applying \(T_g\), because the prime-free factor \(a\) is unique.

Let \(a\in[N,2N]\) and \(\gcd(a,Q)=1\). By the finite support of \(Bh\), uniformly in these \(a\),
\[
(\log N)T_gh_a=\sum_{v\in V}d_v\frac{\log N}{\log(av)}e_{av},
\qquad Bh=\sum_{v\in V}d_v e_v.
\]
Thus \(\inf_{a\in[N,2N],\gcd(a,Q)=1}(\log N)\|T_gh_a\|\ge C_g-2\varepsilon\) for all sufficiently large \(N\).

The number \(q_N\) of such \(a\) is \(q_N=(\varphi(Q)/Q)N+O_Q(1)\), by inclusion-exclusion. On the \(q_N\)-dimensional span of their orthonormal \(h_a\), the images are orthogonal, and every unit vector therefore satisfies \(\|T_gx\|\ge(C_g-2\varepsilon)/\log N\). By the compact-operator min-max principle,
\[
s_{q_N}(T_g)\ge\frac{C_g-2\varepsilon}{\log N}.
\]
For arbitrary large \(n\), take \(N=\lceil 2Qn/\varphi(Q)\rceil\), so \(q_N\ge n\) eventually. Since \(\log N/\log n\to1\), monotonicity of singular values yields \(\liminf_{n\to\infty}(\log n)s_n(T_g)\ge C_g-2\varepsilon\). Letting \(\varepsilon\downarrow0\) proves the first boxed limit.

**5. Counting law and endpoints.** The first limit means that for every \(\varepsilon\in(0,C_g)\) and all large \(n\), \((C_g-\varepsilon)/\log n\le s_n(T_g)\le(C_g+\varepsilon)/\log n\). Counting indices above \(t\) between the corresponding exponentials, then multiplying logarithms by \(t\), gives \(\lim_{t\downarrow0}t\log N_g(t)=C_g\). Since \(C_g>0\), \(\sum_n s_n(T_g)^p\) diverges for every finite positive \(p\), using divergence of \(\sum_n(\log n)^{-p}\).

## Verification
The standalone standard-library program `check.py` checks the exact coefficient formula against the factorization for the two-prime symbol, the exact single-monomial singular-value formula, disjointness of distinct prime-free blocks, and finite-support norm comparisons. Its verified output is `DIRICHLET_VOLTERRA_CHECK_OK 323 finite checks`. These are finite corroborations of explicit formulas, not a substitute for the infinite-dimensional approximation-number proof in Steps 2–5.

## Relationship to prior work
Brevig, Perfekt and Seip (first made public in 2016), Section 7, prove compactness for polynomial symbols and show no nonconstant Volterra operator on \(\mathscr H^2\) is in any finite Schatten class; their proof uses a weaker column-norm lower bound and does not supply a sharp logarithmic singular-value coefficient. Bommier-Hato (2020), Section 6, establishes the corresponding no-Schatten statement for weighted Hilbert spaces. Tong, Wang and Yuan (2026) establish compactness and essential-norm phenomena on \(BMOA_{\mathcal D}\) and Bergman spaces; their studied norms and operators do not entail this Hilbert-space singular-value limit. The new theorem identifies the constant as the sup norm of the derivative's finite Bohr lift and gives the exponential counting exponent. It is not a claim of novelty for compactness or failure of Schatten membership alone.

## Limitations
No statement is made for general infinite Dirichlet-series symbols, other sequence-space weights, or non-Hilbert Hardy exponents. An older broad approximation-number result for multiplicative Toeplitz/multiplier operators might imply this formula under different notation; that publication-priority possibility is not independently resolved. The supporting finite checker covers selected symbols and does not enumerate all coefficients or establish an asymptotic by experiment. No independent audit has been performed.

## References
1. C. Tong, M. Wang and Z. Yuan, *Volterra operators on the BMOA space of Dirichlet series*, arXiv:2610.21873v1 (first public 2026-10-15), https://arxiv.org/html/2610.21873.
2. O. F. Brevig, K.-M. Perfekt and K. Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729 (first public 2016-02-15); accepted full text https://centaur.reading.ac.uk/71297/1/volterra_final4.pdf, Section 7.
3. H. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, Monatshefte für Mathematik (2020), https://link.springer.com/article/10.1007/s00605-020-01396-6, Sections 5–6.
