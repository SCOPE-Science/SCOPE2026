# Exact norm and essential norm of every harmonic Cesàro commutator

## Finding
Let \(1<p<\infty\) and let \(r\) be any nonnegative integer. On finitely supported real or complex sequences indexed by positive integers, put
\[
(Cf)_i=\frac1i\sum_{j=1}^i f_j,\qquad
H_i=\sum_{k=1}^i\frac1k,\qquad
(M_Hf)_i=H_if_i,
\]
and define \(K_0=C\) and \(K_r=\operatorname{ad}_{M_H}^{r}(C)\) for \(r\ge1\), using the commutator convention \(\operatorname{ad}_{M_H}(A)=M_HA-AM_H\). Every \(K_r\) has a unique bounded extension to \(\ell^p(\mathbb N)\). Both its exact operator norm and its distance from the compact operators are
\[
\boxed{\|K_r\|_{\ell^p\to\ell^p}=\|K_r\|_{\mathrm{ess},\ell^p}
=r!\left(\frac{p}{p-1}\right)^{r+1}.}
\]
The diagonal \(M_H\) itself is unbounded; the boundedness and exact constants concern its formally iterated commutator on the dense finitely supported domain. No compact perturbation can reduce the optimal constant. In particular, on \(\ell^2\), the first three positive orders have exact operator and essential norms \(4\), \(16\), and \(96\).

As a consequence, the operator-valued Taylor series \(\sum_{r\ge0}z^r K_r/r!\), interpreted in the operator norm, has the exact convergence radius \((p-1)/p\). This is a consequence of the norm identity, not an independently claimed classification of analytic continuations.

## Assumptions and scope
All sequences have indices \(i,j\in\{1,2,\ldots\}\). The norm is the usual counting-measure \(\ell^p\) norm, and the essential norm is distance to compact bounded operators on that same Banach space. For \(r=0\), adopt the polynomial convention that every zeroth power occurring in a matrix coefficient is \(1\), including on the diagonal. Let \(C^{r+1}\) mean composition, not entrywise powering. There is no assertion for \(p=1\), \(p=\infty\), noninteger order, or different diagonal symbols. For every fixed \(r\), the constants hold uniformly over the entire infinite sequence space.

## Proof
**1. Domain and exact kernel.** For finitely supported \(f\), each composition \(M_H^aCM_H^b f\) is well defined and in \(\ell^p\) because its tail is bounded by a constant times \((1+\log i)^a/i\); this is \(\ell^p\)-summable when \(p>1\). Since \(M_H\) is diagonal, binomial expansion of the iterated commutator gives
\[
(K_rf)_i=\sum_{j=1}^i k_r(i,j)f_j,\qquad
k_r(i,j)=\frac{(H_i-H_j)^r}{i}\quad(j\le i),
\]
with \(k_r(i,j)=0\) when \(j>i\). For \(r=0\), this is the usual Cesàro matrix. Every coefficient is nonnegative.

**2. Coefficient domination, including diagonal and boundary cases.** Fix \(i\ge j\ge1\) and integer \(r\ge1\). Write \(b_k=1/k\) for \(j<k\le i\). Expanding the power \((\sum_{k=j+1}^ib_k)^r\) into ordered tuples and sorting each tuple shows
\[
(H_i-H_j)^r\le r!
\sum_{i\ge k_1\ge\cdots\ge k_r\ge j+1}
\frac1{k_1\cdots k_r}.
\]
Every sorted tuple has at most \(r!\) preimages; equality of indices only reduces that number. The right-hand sum occurs among the nonnegative summands of the exact matrix product
\[
i(C^{r+1})_{ij}
=\sum_{i\ge k_1\ge\cdots\ge k_r\ge j}\frac1{k_1\cdots k_r}.
\]
Consequently \(0\le K_r\le r!C^{r+1}\) entrywise, for all orders \(r\ge1\); for \(r=0\), \(K_0=C\) exactly. For every finitely supported real or complex \(f\), positivity gives \(|K_rf|\le r!C^{r+1}|f|\) coordinatewise. The sharp classical discrete Hardy inequality, \(\|C\|_{\ell^p\to\ell^p}=p/(p-1)\) for \(1<p<\infty\), therefore proves
\[
\|K_r\|\le r!\left(\frac p{p-1}\right)^{r+1}.
\]
It also gives the unique bounded extension by density. The estimate uses no assumption of boundedness of \(M_H\).

**3. Sharpness via a one-sided logarithmic kernel.** Fix a positive integer \(m\), and for \(N\ge m\) set \(f_j^{(m,N)}=j^{-1/p}\) for \(m\le j\le N\), and zero otherwise. For \(m\le i\le N\), multiplication by \(i^{1/p}\) gives the exact identity
\[
i^{1/p}(K_rf^{(m,N)})_i
=\frac1i\sum_{j=m}^i (j/i)^{-1/p}(H_i-H_j)^r.
\]
For each fixed \(0<\delta<1\), the relation \(H_i-H_j=\log(i/j)+O(1/j)\) holds uniformly when \(\delta i\le j\le i\). Hence the corresponding restricted Riemann sum converges to the integral over \([\delta,1]\) of \(t^{-1/p}(-\log t)^r\). For the omitted small indices, \(0\le H_i-H_j\le\log(i/j)\), and \(t^{-1/p}(-\log t)^r\) is nonnegative, decreasing and integrable on \((0,1]\). Comparison of its right-endpoint Riemann sums to its integral controls the portion \(j<\delta i\) by \(\int_0^\delta t^{-1/p}(-\log t)^r\,dt\), uniformly in \(i\). Removing the fixed first \(m-1\) terms does not change the limit. Letting \(\delta\downarrow0\) gives
\[
\lim_{i\to\infty}i^{1/p}(K_rf^{(m,N)})_i
=\int_0^1 t^{-1/p}(-\log t)^r\,dt
=\frac{r!}{(1-1/p)^{r+1}}
\]
when the left-hand expression is understood through the infinite prefix formula, or equivalently for all \(i\le N\) with \(N\) subsequently tending to infinity. The final equality follows from \(t=e^{-u}\) and the elementary gamma integral.

Put \(c_{p,r}=r!(p/(p-1))^{r+1}\). Given \(\epsilon>0\), there is an integer \(I\ge m\) such that for every \(N\ge i\ge I\),
\[
(K_rf^{(m,N)})_i\ge(c_{p,r}-\epsilon)i^{-1/p}.
\]
Since \(\|f^{(m,N)}\|_p^p=\sum_{j=m}^N1/j\), we conclude
\[
\liminf_{N\to\infty}
\frac{\|K_rf^{(m,N)}\|_p^p}{\|f^{(m,N)}\|_p^p}
\ge(c_{p,r}-\epsilon)^p
\lim_{N\to\infty}\frac{\sum_{i=I}^N1/i}{\sum_{j=m}^N1/j}
=(c_{p,r}-\epsilon)^p.
\]
Sending \(\epsilon\downarrow0\) proves \(\|K_rQ_m\|=c_{p,r}\) for every \(m\ge1\), where \(Q_m\) erases the first \(m-1\) coordinates. In particular, it proves the matching full operator-norm lower bound. Notice that the finite test vectors depend on \(N\); no nonzero extremizer is claimed.

**4. Essential norm.** Let \(B\) be any compact operator on \(\ell^p\). Because \(1<p<\infty\), the dual is \(\ell^{p'}\) and \(Q_m^*\) tends strongly to zero on the dual as \(m\to\infty\). Compactness of \(B^*\) makes this convergence uniform on the image of its unit ball, so \(\|BQ_m\|=\|Q_m^*B^*\|\to0\). Therefore
\[
\|K_r-B\|\ge\|(K_r-B)Q_m\|
\ge\|K_rQ_m\|-\|BQ_m\|=c_{p,r}-o(1).
\]
Taking \(m\to\infty\) gives \(\|K_r\|_{\mathrm{ess}}\ge c_{p,r}\). The reverse bound follows by choosing the zero compact operator. Thus both sharp norms coincide.

**5. Operator-series radius.** The norm formula yields \(\|K_r/r!\|=(p/(p-1))^{r+1}\) for every \(r\). The Banach-space Cauchy–Hadamard formula proves that the power series in the finding converges absolutely in operator norm for \(|z|<(p-1)/p\). For \(|z|\ge(p-1)/p\), the norms of its individual terms do not tend to zero, so it cannot converge in operator norm.

## Verification
The standalone file `check_harmonic_commutators.py` computes exact rational matrices for every dimension from \(1\) through \(22\) and orders \(0\) through \(5\). It independently constructs powers of the Cesàro matrix, iterates the commutator definition, checks the closed kernel and the coefficient domination, and tests numerical Riemann-sum saturation for \(p\in\{3/2,2,3\}\) and orders \(0\) through \(3\) at three increasing cutoffs. It prints `ALL_HARMONIC_CESARO_CHECKS_PASS` only after all assertions pass. The checker supports finite algebraic steps; it is not a proof of the infinite-dimensional norm, its essential norm, or the limit integral. Those follow from Steps 2–5.

## Relationship to prior work
The classical discrete Hardy inequality supplies the exact norm of \(C\) and is a **used antecedent**, not claimed as new. Long and Wang (2002), Komori (2003), Zhao (2012), and Fu–Lu–Yuan (2012) study commutators of Hardy-type operators and symbol-space boundedness; the accessible 2012 discussion includes higher-order commutators and logarithmic test symbols. These precedents motivate the question and prevent claiming novelty for Hardy commutators in general. The claim here is the simultaneous all-order, all-interior-exponent **exact** norm and **exact essential norm** for the specific *integer-harmonic* diagonal symbol on the classical discrete prefix-Cesàro matrix; the proof requires coefficientwise domination and sharp tail concentration, not just boundedness or continuous Hardy analogues.

Related published analyses of generalized Cesàro operators with compact power diagonals establish Hilbert–Schmidt cusp behavior, while periodic diagonal symbols yield different endpoint noncompactness and operator-ideal laws. Neither of the two inspected statements covers an unbounded harmonic symbol, the factorial \(\ell^p\) constants, or equality of essential and full norms. The comparison is by operator kernels, domains, and claimed implications, not titles alone. No historical-priority guarantee is asserted: the full 2002 paper and some older symbol literature were not accessible for complete inspection.

## Limitations
The multiplier \(M_H\) is unbounded, so only its iterated commutators on the finitely supported core and their bounded extensions are defined; this is not a claim that the derivation acts boundedly on all operators. The result does not treat \(p=1\) or \(p=\infty\), arbitrary diagonal symbols, nonintegral iterates, or compact perturbations that change the underlying Banach space. The operator-series claim is about its norm-convergence radius and does not exclude analytic continuations beyond that disk by other methods. Available searches and source inspections do not prove universal historical uniqueness. Independent mathematical validation has not been performed.

## References
1. F. Zhao, *A note on commutators of Hardy operators*, Mathematische Nachrichten **285** (2012), 1294–1298, first publicly dated March 5, 2012, DOI: 10.1002/mana.201100160. https://doi.org/10.1002/mana.201100160
2. Z. W. Fu, S. Z. Lu, W. Yuan, *A Weighted Variant of Riemann-Liouville Fractional Integrals on Rn*, Abstract and Applied Analysis **2012**, 780132, first publicly dated September 12, 2012, DOI: 10.1155/2012/780132. https://doi.org/10.1155/2012/780132
3. X. Nie and D. Yan, *Sharp constant of Hardy operators corresponding to general positive measures*, Journal of Inequalities and Applications **2018**, article 78, DOI: 10.1186/s13660-018-1660-8. https://doi.org/10.1186/s13660-018-1660-8
4. S. Long and J. Wang, *Commutators of Hardy operators*, Journal of Mathematical Analysis and Applications **274** (2002), 626–644, DOI: 10.1016/S0022-247X(02)00321-9 (precise original public-release day not established).
5. Y. Komori, *Notes on commutators of Hardy operators*, International Journal of Pure and Applied Mathematics **7** (2003), 329–334 (precise original public-release day not established).
6. G. H. Hardy, J. E. Littlewood, G. Pólya, *Inequalities*, 2nd ed., 1952 (classical discrete Hardy inequality; no new priority assertion).
