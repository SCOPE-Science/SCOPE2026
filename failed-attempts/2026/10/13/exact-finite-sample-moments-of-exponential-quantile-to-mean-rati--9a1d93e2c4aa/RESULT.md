# Exact finite-sample moments of exponential quantile-to-mean ratios
## Finding
Let \(X_1,\ldots,X_n\) be independent with exponential distribution of rate \(\lambda>0\), and write \(X_{(k)}\) for the \(k\)-th order statistic. Define the scale-free statistic
\[
Q_{n,k}=\frac{X_{(k)}}{\bar X},
\qquad 1\le k\le n.
\]
For harmonic sums
\[
H_r=\sum_{j=1}^r\frac1j,\qquad
H_r^{(2)}=\sum_{j=1}^r\frac1{j^2},
\]
with \(H_0=H_0^{(2)}=0\), put
\[
A_{n,k}=H_n-H_{n-k},\qquad
B_{n,k}=H_n^{(2)}-H_{n-k}^{(2)}.
\]
Then \(Q_{n,k}\) is independent of \(\bar X\), and
\[
\mathbb E Q_{n,k}=A_{n,k},
\]
\[
\operatorname{Var}(Q_{n,k})
=\frac{nB_{n,k}-A_{n,k}^2}{n+1}.
\]
Equivalently,
\[
\mathbb E Q_{n,k}^2
=\frac{n\left(A_{n,k}^2+B_{n,k}\right)}{n+1}.
\]

If \(k/n\to p\in(0,1)\), then
\[
\mathbb E Q_{n,k}\longrightarrow-\log(1-p)
\]
and
\[
n\operatorname{Var}(Q_{n,k})
\longrightarrow
\frac{p}{1-p}-\log^2(1-p).
\]

For an odd sample \(n=2m+1\), let \(M_n=X_{(m+1)}\) be the sample median. Then
\[
\mathbb E\frac{M_n}{\bar X}=H_{2m+1}-H_m>\log2.
\]
These expectations are strictly decreasing in \(m\) and converge to \(\log2\). More precisely,
\[
H_{2m+1}-H_m
=\log2+\frac1{4m}+O(m^{-2}).
\]
The exact variance is
\[
\operatorname{Var}\!\left(\frac{M_n}{\bar X}\right)
=
\frac{(2m+1)\left(H_{2m+1}^{(2)}-H_m^{(2)}\right)
-\left(H_{2m+1}-H_m\right)^2}{2m+2},
\]
and
\[
n\operatorname{Var}\!\left(\frac{M_n}{\bar X}\right)
\longrightarrow1-(\log2)^2.
\]

## Assumptions and scope
The parent law is exactly exponential with an arbitrary positive rate. The result covers every finite sample size and every order statistic \(X_{(k)}\); the median corollary uses the ordinary middle order statistic for odd \(n\). It does not claim analogous formulas for gamma, Weibull, censored, truncated, or contaminated samples.

The statistic is dimensionless. Consequently all displayed moments are independent of the unknown exponential rate.

## Proof
Set \(X_{(0)}=0\) and define the spacings
\[
D_j=X_{(j)}-X_{(j-1)},\qquad 1\le j\le n.
\]
The exponential memoryless property gives independent spacings with
\[
D_j\sim\operatorname{Exp}((n-j+1)\lambda).
\]
Therefore
\[
E_j=(n-j+1)D_j,\qquad 1\le j\le n,
\]
are iid \(\operatorname{Exp}(\lambda)\).

The total sample sum can be rearranged exactly as
\[
T=\sum_{i=1}^nX_i
=\sum_{j=1}^n(n-j+1)D_j
=\sum_{j=1}^nE_j.
\]
Hence, with
\[
P_j=\frac{E_j}{T},
\]
the vector \((P_1,\ldots,P_n)\) has the \(\operatorname{Dirichlet}(1,\ldots,1)\) law and is independent of \(T\). Since \(\bar X=T/n\),
\[
Q_{n,k}
=n\sum_{j=1}^k\frac{P_j}{n-j+1}.
\]
Thus \(Q_{n,k}\) is a function only of the Dirichlet proportions and is independent of \(\bar X\).

For \(\operatorname{Dirichlet}(1,\ldots,1)\),
\[
\mathbb E P_i=\frac1n,\qquad
\mathbb E P_i^2=\frac{2}{n(n+1)},\qquad
\mathbb E P_iP_j=\frac1{n(n+1)}
\quad(i\ne j).
\]
Applying these identities to the preceding linear form gives
\[
\mathbb E Q_{n,k}
=\sum_{j=1}^k\frac1{n-j+1}
=A_{n,k}.
\]
Writing
\[
a_j=\frac1{n-j+1},
\]
one obtains
\[
\mathbb E Q_{n,k}^2
=\frac{n}{n+1}
\left[
\left(\sum_{j=1}^ka_j\right)^2
+\sum_{j=1}^ka_j^2
\right]
=
\frac{n(A_{n,k}^2+B_{n,k})}{n+1}.
\]
Subtracting \(A_{n,k}^2\) proves the variance formula.

For \(k/n\to p\in(0,1)\), the two harmonic tails are Riemann sums:
\[
A_{n,k}
=\frac1n\sum_{r=n-k+1}^n\frac{n}{r}
\longrightarrow
\int_{1-p}^1\frac{dx}{x}
=-\log(1-p),
\]
and
\[
nB_{n,k}
=\frac1n\sum_{r=n-k+1}^n\left(\frac{n}{r}\right)^2
\longrightarrow
\int_{1-p}^1\frac{dx}{x^2}
=\frac{p}{1-p}.
\]
Substitution into the exact variance proves the second limit.

For \(n=2m+1\) and \(k=m+1\),
\[
A_{n,k}=H_{2m+1}-H_m.
\]
The integral comparison for the decreasing function \(x\mapsto1/x\) gives
\[
H_{2m+1}-H_m
>
\int_{m+1}^{2m+2}\frac{dx}{x}
=\log2.
\]
Also
\[
\bigl(H_{2m+3}-H_{m+1}\bigr)
-\bigl(H_{2m+1}-H_m\bigr)
=
-\frac1{(2m+2)(2m+3)}<0,
\]
so the finite-sample expectation decreases strictly. The standard harmonic-number expansion yields the stated \(1/(4m)\) leading bias term. The variance limit is the case \(p=1/2\).

## Verification
The accompanying `checker.py` uses exact rational arithmetic. For every pair \(1\le k\le n\le300\), it independently expands the first and second Dirichlet moments of the weighted proportion vector and checks the compact harmonic formulas for the mean, second moment, and variance. It also checks the exact one-step decrement formula for the odd-sample median expectation through \(m=1000\), along with positivity of every finite variance in the nonconstant cases.

The analytic proof establishes all sample sizes. Finite computation is supplementary and is not used to turn a bounded check into an infinite statement.

## Relationship to prior work
Lin, Wu, and Ahmad developed the asymptotic joint distribution of sample quantiles and the sample mean, and explicitly treated ratios of sample quantiles to the sample mean. Inspection of the complete article shows that its results are asymptotic and distribution-generic; it does not state the exact exponential finite-sample moments above.

Scannell, Grant, Payne, and Baddeley used the sample median-to-mean ratio as a robust skew measure for data modeled by an exponential law. Their Figure 4 displays an expected finite-sample exponential median-to-mean curve and notes its limit \(\log2\). That graphical expectation is a genuine overlap with one special case of the first-moment phenomenon and is not claimed here as a new numerical observation. The result above supplies a closed form for every \(n\) in the odd-median case, extends it to every \(k\)-th order statistic, gives the exact finite variance, and identifies exact independence from the sample mean.

The Rényi representation of exponential order statistics and the gamma-Dirichlet normalization are classical ingredients. The finding is the resulting closed finite-sample quantile-to-mean moment identity and its finite-median calibration, not the representation itself.

## Limitations
The literature search cannot exclude an unindexed historical formula for the same normalized exponential order statistic. The most direct classical article found on quantile-to-mean ratios is asymptotic, while the directly relevant applied exponential paper supplies a plotted expected median-to-mean curve but not the general exact formulas or exact variance.

The result concerns ordinary iid exponential sampling. It does not address even-sample median conventions, censoring, dependence, or robustness under model misspecification.

## References
1. P.-E. Lin, K.-T. Wu, and I. A. Ahmad, “Asymptotic joint distribution of sample quantiles and sample mean with applications,” *Communications in Statistics — Theory and Methods* 9 (1980), 51–60. DOI: 10.1080/03610928008827858.
2. J. W. Scannell, S. Grant, B. R. Payne, and R. Baddeley, “On variability in the density of corticocortical and thalamocortical connections,” *Philosophical Transactions of the Royal Society B* 355 (2000), 21–35. DOI: 10.1098/rstb.2000.0547.
3. J.-M. Lévy, “Use of the median in Physics and Astronomy,” arXiv:0804.0606, first posted 3 April 2008.
