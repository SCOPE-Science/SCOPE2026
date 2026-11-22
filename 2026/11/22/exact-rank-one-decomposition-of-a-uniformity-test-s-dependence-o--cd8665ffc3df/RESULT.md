# Exact rank-one decomposition of a uniformity test's dependence on Cramér–von Mises and Watson statistics

## Finding

Let \(n\ge2\) and let \(U_1,\ldots,U_n\) be independent uniform random variables on \((0,1)\). Consider the characterization-based omnibus statistic introduced by Ebner, Liebenberg and Visagie [1],
\[
T_n=n\int_0^1\left\{\frac1n\sum_{i=1}^n(2U_i-1)\mathbf1_{\{U_i\ge t\}}-t(1-t)\right\}^{2}\,dt.
\]
Let \(F_n\) be the empirical CDF and define the conventional simple-null Cramér–von Mises statistic, its Watson-centered counterpart, and the empirical-mean component by
\[
W_n=n\int_0^1\{F_n(t)-t\}^{2}\,dt,\quad
V_n=W_n-M_n,\quad
M_n=n\left(\overline U_n-\frac12\right)^2.
\]
Then, *for every finite integer* \(n\ge2\),
\[
\boxed{\operatorname{Cov}(T_n,W_n)=\frac{26n-17}{1260n},\qquad
\operatorname{Cov}(T_n,V_n)=\frac{n-1}{210n},\qquad
\operatorname{Cov}(T_n,M_n)=\frac{20n-11}{1260n}.}
\]
Their exact variances are
\[
\boxed{\operatorname{Var}(T_n)=\frac{218n-49}{8100n},\quad
\operatorname{Var}(W_n)=\frac{4n-3}{180n},\quad
\operatorname{Var}(V_n)=\frac{n-1}{360n}.}
\]
Consequently, the two positive null correlations are
\[
\rho_{TW}(n)=\frac{3\sqrt5(26n-17)}{7\sqrt{(218n-49)(4n-3)}},\qquad
\rho_{TV}(n)=\frac{18\sqrt{10}}7\sqrt{\frac{n-1}{218n-49}}.
\]
Both correlations are strictly increasing in \(n\ge2\), and \(\rho_{TW}(n)>\rho_{TV}(n)\) at every such \(n\). Their respective limits are approximately \(0.84376852785\) and \(0.550739\). Moreover, the mean-shift component accounts for a strictly decreasing but universally bounded fraction of the covariance with Cramér–von Mises:
\[
\boxed{\frac{\operatorname{Cov}(T_n,M_n)}{\operatorname{Cov}(T_n,W_n)}=\frac{20n-11}{26n-17}\in\left(\frac{10}{13},\frac{29}{35}\right]\quad(n\ge2).}
\]
Thus over \(76.9\%\) of the exact cross-covariance at every sample size is attributable to the squared empirical-mean discrepancy, not to the Watson-centered residual.

## Assumptions and scope

The null distribution must be fully specified and continuous, so the probability integral transforms are independent uniform observations. The definitions use the standard unweighted integral normalization with the leading factor \(n\); the Watson term is the exact subtraction \(n(\overline U_n-1/2)^2\). Ties have null probability zero. The covariance formulas also make sense at \(n=1\), but \(V_1=1/12\) is deterministic, so its correlation is undefined there. No parameters are estimated from the sample.

## Proof

For an independent uniform variable \(U\), set
\[
f_t(U)=(2U-1)\mathbf1_{\{U\ge t\}}-t(1-t),\qquad
h_t(U)=\mathbf1_{\{U\ge t\}}-(1-t),\qquad
m(U)=U-\tfrac12.
\]
Each is centered. The statistics are squared norms of the empirical averages of these functions, multiplied by \(n\), with \(W_n\) using \(h\), \(T_n\) using \(f\), and \(M_n\) using \(m\). The pointwise identity \(V_n=W_n-M_n\) follows from \(\int_0^1h_t(U)\,dt=U-1/2\).

For any two centered feature maps \(a(U)\) and \(b(U)\) into real Hilbert spaces, define \(k_a(u,v)=\langle a(u),a(v)\rangle\) and the diagonal \(d_a(u)=k_a(u,u)\); similarly for \(b\). Expanding the double sums and using conditional centering to eliminate all cross-pair terms with only one shared index gives the exact identity
\[
\operatorname{Cov}\!\left(\frac1n\sum_{i,j}k_a(U_i,U_j),\frac1n\sum_{i,j}k_b(U_i,U_j)\right)
=\frac{\operatorname{Cov}(d_a(U),d_b(U))}{n}
+\frac{2(n-1)}n\mathbb E[k_a(U,U')k_b(U,U')],
\tag{1}
\]
where \(U,U'\) are independent uniform variables. This is an exact finite-sample combinatorial identity, not a Gaussian approximation.

Elementary one-variable integration yields the diagonal polynomials
\[
d_f(u)=\frac{40u^4+40u^3-90u^2+30u+1}{30},\quad
d_h(u)=u^2-u+\tfrac13,\quad d_m(u)=(u-\tfrac12)^2.
\]
In particular, \(d_h-d_m\equiv1/12\). For the mixed off-diagonal contraction, define \(C(s,t)=\mathbb E[f_s(U)h_t(U)]\). Direct integration of \((2u-1)\) over the upper tail gives
\[
C(s,t)=
\begin{cases}
t s(1-s),&0\le t\le s\le1,\\
(1-t)(t-s+s^2),&0\le s<t\le1.
\end{cases}
\]
By independence and Fubini,
\[
\mathbb E[k_f(U,U')k_h(U,U')]
=\int_0^1\int_0^1 C(s,t)^2\,dt\,ds=\frac{13}{1260}.
\]
Likewise, for the empirical-mean mode,
\[
\mathbb E[f_s(U)m(U)]=\frac1{12}-\frac23(s-\tfrac12)^3,\qquad
\mathbb E[k_f(U,U')m(U)m(U')]=\frac1{126}.
\]
The remaining rational contractions, obtained by integrating polynomials on the triangles \(0\le t\le s\le1\) and \(0\le s\le t\le1\), are summarized here. The diagonal column is the covariance of the two diagonal kernel functions, and the pair column is the mean product of the two degenerate pair kernels evaluated at independent \(U,U'\).

| Feature pair | Diagonal contraction | Pair contraction |
|---|---:|---:|
| \((f,f)\) | \(169/8100\) | \(109/8100\) |
| \((h,h)\) | \(1/180\) | \(1/90\) |
| Watson kernel \(k_V\) | \(0\) | \(1/720\) |
| \((f,h)\) | \(1/140\) | \(13/1260\) |
| \((f,m)\) | \(1/140\) | \(1/126\) |
| Mixed kernel \((k_f,k_V)\) | \(0\) | \(1/420\) |

The Watson rows use the genuine centered feature map \(v_t(u)=h_t(u)-m(u)\), with \(m(u)\) regarded as a constant function of \(t\). Hence its kernel is \(k_V(u,v)=k_h(u,v)-m(u)m(v)\). For example, \(\mathbb E k_h(U,U')m(U)m(U')=1/120\) and \(\mathbb E[m(U)^2m(U')^2]=1/144\), whence \(1/90-2/120+1/144=1/720\). Substitution into (1) proves all six variance/covariance formulas.

For completeness, exact differentiation of the two squared-correlation rational functions gives
\[
\frac{d}{dn}\rho_{TW}(n)^2=
\frac{90(26n-17)(3774n-3403)}{49(4n-3)^2(218n-49)^2}>0,
\]
\[
\frac{d}{dn}\rho_{TV}(n)^2=\frac{547560}{49(218n-49)^2}>0
\quad(n\ge2).
\]
The strict squared-correlation gap equals
\[
\rho_{TW}(n)^2-\rho_{TV}(n)^2
=\frac{45(388n^2-380n+73)}{49(4n-3)(218n-49)}>0.
\]
The covariance-share ratio has derivative \(-54/(26n-17)^2<0\), equals \(29/35\) at \(n=2\), and tends to \(10/13\). Positivity of both correlations completes the stated ordering and sharp bounds.

## Verification

The accompanying `check.py` is a standard-library-only exact-rational checker. It independently constructs polynomial representations for the diagonal kernels and the two triangular pieces of \(C(s,t)\), performs every monomial integral in rational arithmetic, and verifies all contractions and final formulas for sample sizes \(1\) through \(1000\). It also checks the computational forms of the statistics against an independent interval-by-interval antiderivative implementation for 1500 pseudo-random samples, and verifies positive finite-size inequalities. Its execution completed with `PASS 13510 checks`. The finite set of numerical checks corroborates the symbolic proof; the proof covers all \(n\) by the formulas and factorizations displayed above.

## Relationship to prior work

Ebner, Liebenberg and Visagie [1] introduced \(T_n\) and gave its limiting null Gaussian-square distribution and first four limiting cumulants. In particular, the limit variance \(109/4050\) matches the large-sample limit of the exact variance above. Their reported empirical power comparisons put this statistic alongside Cramér–von Mises and Watson tests but do not state exact same-sample cross-covariances or the mean-mode share. Hwang and Kuriki [2] develop and analyze generalized classical EDF quadratic statistics, including Watson/Cramér–von Mises, but do not analyze the characterization-based kernel \(f\) in this cross-test coupling. Established exact covariance formulas for pairs of classical EDF statistics similarly lack the weighted-indicator feature map in [1]. The method of centered-kernel contraction is standard; the specific cross-kernel integrals, finite-size rational laws, monotonicity and mean-mode decomposition are the claimed contribution, not the general contraction identity.

## Limitations

These are null covariances, not independence results, joint CDFs, critical-value guarantees or proofs that combining tests improves power. Pearson correlation alone does not measure all dependence. For fitted composite nulls, transformed observations may be dependent and the formulas need not apply. The first-public date and literature comparison establish a relevant starting point, not an exhaustive guarantee of historical priority; equivalent analyses in broader empirical-process literature remain possible. No independent mathematical audit has been carried out.

## References

1. B. Ebner, S. C. Liebenberg, I. J. H. Visagie, *A new omnibus test of fit based on a characterisation of the uniform distribution*, arXiv:2108.06391, first posted 2021-08-13, https://arxiv.org/abs/2108.06391. See equations (4)–(5), Theorem 2.1 and Section 4.
2. H.-K. Hwang and S. Kuriki, *Integrated empirical measures and generalizations of classical goodness-of-fit statistics*, arXiv:2404.06040, first posted 2024-04-09, https://arxiv.org/abs/2404.06040. See Sections 1, 3–4.
