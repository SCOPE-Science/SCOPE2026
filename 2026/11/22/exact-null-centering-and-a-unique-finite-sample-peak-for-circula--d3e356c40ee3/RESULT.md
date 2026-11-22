# Exact null centering and a unique finite-sample peak for circularized logarithmic goodness-of-fit scores

## Finding

Let \(n\ge1\) be an integer and put \(N=n+1\). Under a fully specified continuous null distribution, define the average-pooled circularized logarithmic score \(\widetilde W_n^2\) in the next section, with exactly the normalization of equation (4.8) of Liu (2022/2023). Its exact null expectation is

\[
 m_N:=\mathbb E\widetilde W_n^2
 =N+1-\frac2N+\frac4N\sum_{j=1}^{N-1}j\log\frac jN.
\]

This expectation is strictly increasing for \(2\le N\le55\) and strictly decreasing for \(N\ge55\); the **unique maximizing sample size is \(n=54\)**, where \(m_{55}=1.006014499509\ldots\). It crosses the reference value one exactly once: \(m_N<1\) for \(2\le N\le20\), and \(m_N>1\) for every \(N\ge21\). Equivalently, the sign change occurs between sample sizes \(n=19\) and \(n=20\). Finally,

\[
 m_N=1+\frac{\log N}{3N}+O(N^{-1})\qquad(N\to\infty).
\]

Thus the asymptotic unit-mean normalization has a precisely characterized, nonmonotone finite-sample discrepancy. Division by \(m_N\) produces an exactly null-mean-one score without changing within-\(n\) rejection ordering; it does not by itself yield exact critical values.

## Assumptions and scope

For \(n\ge1\), let \(U_1,\ldots,U_n\) be independent \(\operatorname{Uniform}(0,1)\) variables obtained by the probability integral transform under a **known, continuous, fully specified** null. Write \(0=U_{(0)}<U_{(1)}<\cdots<U_{(n)}<U_{(N)}=1\) almost surely and define spacings \(D_k=U_{(k)}-U_{(k-1)}\), \(1\le k\le N\). For every cyclic origin \(c\in\{0,\ldots,N-1\}\) and \(1\le j\le N-1\), set

\[
 V_{c,j}=\sum_{k=1}^{j}D_{1+((c+k-1)\bmod N)},\qquad \mu_j=j/N.
\]

The precise statistic is

\[
 \widetilde W_n^2=-\frac2N\sum_{c=0}^{N-1}\sum_{j=1}^{N-1}
 \left[\mu_j\log\frac{V_{c,j}}{\mu_j}
 +(1-\mu_j)\log\frac{1-V_{c,j}}{1-\mu_j}\right].
\]

All logarithms are natural. This is the **average-pooled modified log-score**, not the max-pooled version, the ordinary classical Anderson–Darling integral statistic, nor the separately normalized circularized \(\widetilde R_n^2\). It is defined for arbitrary continuous null models only when parameters are fully specified, so the transformed observations are exactly uniform.

## Proof

**Exact mean.** The vector of \(N\) spacings has the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution and is invariant under cyclic rotation. Each sum of \(j\) consecutive spacings, regardless of origin, has law \(\operatorname{Beta}(j,N-j)\). Writing \(H_r=\sum_{k=1}^r1/k\) for \(r\ge1\) and \(H_0=0\), beta differentiation gives

\[
 \mathbb E\log V_{c,j}=H_{j-1}-H_{N-1},\qquad
 \mathbb E\log(1-V_{c,j})=H_{N-j-1}-H_{N-1}.
\]

The two weighted harmonic-number sums are equal by \(j\leftrightarrow N-j\). Interchanging finite sums yields

\[
 \sum_{j=1}^{N-1}\frac jN(H_{N-1}-H_{j-1})
 =\frac1N\sum_{k=1}^{N-1}\frac1k\sum_{j=1}^{k}j
 =\frac{(N-1)(N+2)}{4N}.
\]

The corresponding logarithmic reference terms also pair by \(j\leftrightarrow N-j\), giving

\[
 m_N=\frac{(N-1)(N+2)}N+
 4\sum_{j=1}^{N-1}\frac jN\log\frac jN,
\]

which is the stated closed formula.

**Unique unit-mean crossing.** Define

\[
 F_N=N(m_N-1)=N^2-2+4\sum_{j=1}^{N-1}j\log(j/N).
\]

Direct subtraction gives

\[
 \Delta F_N:=F_{N+1}-F_N=2N+1-2N(N+1)\log(1+1/N).
\]

The trapezoidal-rule remainder for the strictly convex function \(x\mapsto1/x\) has the positive integral representation

\[
 \Delta F_N=2N(N+1)\int_0^1\frac{t(1-t)}{(N+t)^3}\,dt>0.
\]

Thus \(F_N\) strictly increases. Rigorous rational logarithm enclosures supplied in `checker.py` give \(F_{20}\in(-0.006391,-0.006390)\) and \(F_{21}\in(0.009871,0.009872)\). These two verified signs and strict monotonicity prove the unique crossing.

**Unique maximum.** Differentiating the integrand factor \(N(N+1)/(N+t)^3\) with respect to its real argument shows strict decrease for all \(N>1\), \(0\le t\le1\):

\[
 \frac1N+\frac1{N+1}-\frac3{N+t}
 \le\frac1N-\frac2{N+1}<0.
\]

Therefore \(\Delta F_N>0\) is strictly decreasing. Define \(G_N=N\Delta F_N-F_N\). Then

\[
 m_{N+1}-m_N=\frac{G_N}{N(N+1)},\qquad
 G_{N+1}-G_N=(N+1)(\Delta F_{N+1}-\Delta F_N)<0.
\]

The exact-rational interval checker certifies \(G_{54}\in(0.005599,0.005601)\) and \(G_{55}\in(-0.000463,-0.000460)\). Strict decrease of \(G_N\) proves increase through \(m_{55}\), decrease thereafter, and uniqueness of its maximum.

**Asymptotic.** Uniform expansion of the positive integral above yields \(\Delta F_N=1/(3N)+O(N^{-2})\). Summing these differences establishes \(F_N=(\log N)/3+O(1)\), and division by \(N\) gives the displayed null-mean expansion. No finite enumeration is used to infer either infinite-range monotonicity statement.

## Verification

The standalone `checker.py` independently evaluates the expectation in both beta-digamma and collapsed logarithmic-sum forms, confirms finite sample values by seeded simulation of normalized exponentials, and produces **exact rational logarithm enclosures** for the only four finite boundary signs required by the analytic argument: \(F_{20}\), \(F_{21}\), \(G_{54}\), \(G_{55}\). The logarithm enclosure uses a convergent \(\operatorname{atanh}\) series with an explicit positive rational remainder after powers-of-two range reduction. It requires only Python 3 standard-library modules, both for rational certification and optional stochastic corroboration. Run `python checker.py` from this directory. Full observed outputs and limitations are summarized in `VERIFICATION.md`.

## Relationship to prior work

Liu's circularization method and the exact form of the log-score are prior work, specifically the modified score in equation (2.2), its average pooling in equation (4.8), and the Gaussian-kernel large-sample approximation in Section 6.3.2 of *Reweighted and Circularized Anderson-Darling Tests of Goodness-of-Fit*, arXiv:2209.08050. In Remark 6.3 the mean is described through a **Gaussian approximation** as approximately one; the exact finite-sample mean and the two global sample-size classifications are the present subject, not the statistic's construction or its asymptotic spectral limit. Zhang's 2002 likelihood-ratio goodness-of-fit framework is earlier methodological background. Earlier equivalent exact mean calculations under alternative score notation have not been ruled out absolutely.

## Limitations

The theorem concerns an exact mean, not a null CDF, quantile, power function, or practical improvement in size from simply rescaling the statistic. The maximum overshoot above one is approximately \(0.0060145\); the below-one discrepancy is substantially larger for very small samples. The derivation requires known null parameters, continuous observations and the specific average pooling and normalization stated above. A distinct contemporaneous circularization preprint, arXiv:2209.08150, was accessible only at abstract level; its potential bearing on historical priority is unresolved.

## References

1. Chuanhai Liu, *Reweighted and Circularized Anderson-Darling Tests of Goodness-of-Fit*, first posted 2022-09-16, arXiv:2209.08050, https://arxiv.org/abs/2209.08050; journal DOI 10.1080/10485252.2023.2213782.
2. Chuanhai Liu, *Circularly Symmetric Tests of Goodness-of-Fit*, first posted 2022-09-16, arXiv:2209.08150, https://arxiv.org/abs/2209.08150 (abstract inspected; full text not available).
3. Jin Zhang, *Powerful goodness-of-fit tests based on the likelihood ratio*, Journal of the Royal Statistical Society Series B 64 (2002), 281–294, https://doi.org/10.1111/1467-9868.00337 (abstract and publication information inspected).
