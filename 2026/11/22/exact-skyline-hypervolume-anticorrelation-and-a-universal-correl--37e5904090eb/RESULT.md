# Exact skyline–hypervolume anticorrelation and a universal correlation limit

## Finding

For each integer \(n\ge 2\), take \(n\) independent uniform points \((X_i,Y_i)\) in \([0,1]^2\). Let \(K_n\) be their number of coordinatewise Pareto maxima, and let \(A_n\) be the area of the dominated set
\[
\mathcal D_n=\bigcup_{i=1}^n [0,X_i]\times[0,Y_i].
\]
Writing \(H_r=\sum_{j=1}^rj^{-1}\) and \(H_r^{(2)}=\sum_{j=1}^rj^{-2}\), there is an exact strict anticorrelation:
\[
\boxed{\operatorname{Cov}(K_n,A_n)
=-\frac{(n+2)H_n-(n+1)H_n^{(2)}-n}{(n+1)^2}<0.}
\]
The exact area variance is
\[
\boxed{\operatorname{Var}(A_n)=
\frac{(n+1)\bigl(2(n+3)H_{n+1}-2(n+1)-(n+2)H_{n+1}^{(2)}\bigr)
-(n+2)H_{n+1}^{2}}{(n+1)^2(n+2)^2}.}
\]
In particular,
\[
\boxed{\lim_{n\to\infty}\operatorname{Corr}(K_n,A_n)=-\frac1{\sqrt2}.}
\]
Thus skyline cardinality and the dominated hypervolume retain a nonzero negative standardized dependence as the sample grows, even though the unstandardized covariance tends to zero.

## Assumptions and scope

The points are independent, each with two independent \(\operatorname{Uniform}(0,1)\) coordinates. Dominance is coordinatewise maximization; an observed point is maximal when no different observed point dominates it in both coordinates. Ties have probability zero. The hypervolume reference point is the origin, and \(A_n\) is two-dimensional Lebesgue area. All exact formulas are valid for every integer \(n\ge2\); the variance formula also holds for \(n=1\). The limiting statement is an ordinary Pearson correlation limit, not a statement of distributional independence or of conditional stochastic ordering.

## Proof

**1. Coupling with permutation records.** Sort the sample by decreasing first coordinate, and write \(Y_1,\ldots,Y_n\) for the second coordinates in this order. These are independent uniform variables, independent of the ordered first coordinates. Let \(\pi_t\) be the rank of \(Y_t\) among all \(n\) second coordinates, \(L_t=\max_{1\le j\le t}\pi_j\), and \(I_t=\mathbf1\{\pi_t>L_{t-1}\}\), with \(I_1=1\). Then \(K_n=\sum_{t=1}^n I_t\).

Put the ordered first-coordinate spacings, including the gap from the maximum to one, into a vector \((D_0,\ldots,D_n)\). It has the \(\operatorname{Dirichlet}(1,\ldots,1)\) law, independently of the \(Y\)'s. If \(U_t=\max_{j\le t}Y_j\), slicing \(\mathcal D_n\) into vertical strips gives \(A_n=\sum_{t=1}^nD_tU_t\). Given the rank permutation, \(\mathbb E U_t=L_t/(n+1)\); thus
\[
\mathbb E[A_n\mid\pi]=\frac1{(n+1)^2}\sum_{t=1}^nL_t.
\]

**2. Exact mixed covariance.** For \(t\le s\), the event \(I_t=1\) depends only on the relative order of the first \(s\) ranks; this relative order is independent of their maximum \(L_s\), so \(\operatorname{Cov}(I_t,L_s)=0\). For \(t>s\), the event \(I_t=1\), of probability \(1/t\), places the greatest of the first \(t\) ranks at time \(t\). Conditional on this event, the first \(s\) internal ranks form a uniformly selected \(s\)-subset of \(\{1,\ldots,t-1\}\), whose expected maximum is \(st/(s+1)\). The expected global rank of internal rank \(j\) in a uniform \(t\)-subset of \(\{1,\ldots,n\}\) is \(j(n+1)/(t+1)\). Consequently
\[
\begin{aligned}
\mathbb E[L_s\mid I_t=1]&=\frac{st(n+1)}{(s+1)(t+1)},\\
\mathbb E L_s&=\frac{s(n+1)}{s+1},\\
\operatorname{Cov}(I_t,L_s)&=-\frac{s(n+1)}{t(s+1)(t+1)}\qquad(t>s).
\end{aligned}
\]
Taking the covariance of the conditional expectation in step 1 with \(K_n\), and telescoping \(\sum_{t=s+1}^n1/[t(t+1)]=1/(s+1)-1/(n+1)\), gives
\[
\operatorname{Cov}(K_n,A_n)=-\frac1{n+1}\sum_{s=1}^{n-1}\frac{s}{s+1}\left(\frac1{s+1}-\frac1{n+1}\right).
\]
Each term is positive for \(n\ge2\). The identities \(\sum_{s=1}^{n-1}s/(s+1)^2=H_n-H_n^{(2)}\) and \(\sum_{s=1}^{n-1}s/(s+1)=n-H_n\) yield the displayed exact formula.

**3. Exact hypervolume variance.** Let \(W_n=1-A_n\), and define \(V_0=1\) and \(V_t=1-U_t=\min_{j\le t}(1-Y_j)\) for \(t\ge1\). Then \(W_n=\sum_{t=0}^nD_tV_t\). Elementary minimum-order-statistic integration gives, for \(0\le s\le t\le n\),
\[
\mathbb E V_t=\frac1{t+1},\quad
\mathbb E V_t^2=\frac2{(t+1)(t+2)},\quad
\operatorname{Cov}(V_s,V_t)=\frac{s}{(s+1)(t+1)(t+2)}.
\]
The last identity follows by conditioning on \(V_s=z\) and using \(\mathbb E[V_t\mid V_s=z]=\int_0^z(1-u)^{t-s}\,du\). Write \(T=\sum_{t=0}^nV_t\). Summing this covariance kernel gives
\[
\mathbb E T=H_{n+1},\quad
\operatorname{Var}(T)=\frac{2(n+3)}{n+2}H_{n+1}-H_{n+1}^{(2)}-\frac{4(n+1)}{n+2}.
\]
Also \(\mathbb E\sum_{t=0}^nV_t^2=2(n+1)/(n+2)\). The Dirichlet second-moment formula implies
\[
\mathbb E[W_n^2\mid V_0,\ldots,V_n]=\frac{T^2+\sum_{t=0}^nV_t^2}{(n+1)(n+2)}.
\]
Subtracting \((\mathbb EW_n)^2=H_{n+1}^2/(n+1)^2\) establishes the exact variance stated above.

**4. Correlation limit.** Upper-record indicators for a uniform permutation are independent Bernoulli variables with success probabilities \(1/t\), giving \(\operatorname{Var}(K_n)=H_n-H_n^{(2)}\). From the proved formulas and \(H_n=\log n+\gamma+O(n^{-1})\), \(H_n^{(2)}=\pi^2/6+O(n^{-1})\),
\[
\operatorname{Cov}(K_n,A_n)=-\frac{\log n+O(1)}n,\quad
\operatorname{Var}(K_n)=\log n+O(1),\quad
\operatorname{Var}(A_n)=\frac{2\log n+O(1)}{n^2}.
\]
The quotient is \(-1/\sqrt2\), as claimed.

## Verification

The accompanying `checker.py` uses only the Python standard library. It compares the harmonic-number covariance formula against the unsimplified record/running-maximum covariance kernel and complete rank-permutation enumeration for \(2\le n\le8\); independently compares the area-variance formula against the complete running-minimum kernel for \(1\le n<80\); verifies strict finite signs and selected numerical asymptotic diagnostics. A successful run prints `PASS 325 exact and consistency checks`. These computations corroborate the formulas but are not substitutes for the general arguments in steps 1–4.

## Relationship to prior work

Classical work on planar maxima and records determines the distribution and asymptotics of skyline cardinality. Bai, Hwang, Liang and Tsai (2001) and Barbour and Xia (2001) analyze maxima in planar samples; Hwang and Tsai (2010) systematically study dominance-based records and use sorting to connect maxima to one-dimensional record processes. Hypervolume is a standard Pareto-front quality statistic. The contribution here is a *joint* finite-sample covariance formula and a nonzero limiting correlation of cardinality with the dominated area. Marginal results about either quantity, or fixed-threshold skyline-versus-corner-count covariances, do not by themselves give this joint statistic. The references below should not be interpreted as claiming historical priority; specialized earlier work could contain an equivalent joint formula.

## Limitations

The theorem concerns iid uniform points in the square and the origin-anchored dominated area. It does not assert the same constant for nonuniform or dependent coordinates, different reference-point conventions, more than two objectives, or random sample sizes. A numerical or bibliographic absence of matches is not a proof that no equivalent result was previously published. The older Barbour–Xia paper was inspected through accessible author-manuscript excerpts rather than a fully retrieved PDF. Independent validation of the result has not been performed.

## References

- Z.-D. Bai, H.-K. Hwang, W.-Q. Liang and T.-H. Tsai, *Limit Theorems for the Number of Maxima in Random Samples from Planar Regions*, Electronic Journal of Probability **6** (2001), 1–41, https://doi.org/10.1214/EJP.v6-76.
- A. D. Barbour and A. Xia, *The Number of Two-Dimensional Maxima*, Advances in Applied Probability **33** (2001), 727–750, https://doi.org/10.1239/aap/1011994025.
- H.-K. Hwang and T.-H. Tsai, *Multivariate Records Based on Dominance*, Electronic Journal of Probability **15** (2010), 1863–1892, https://arxiv.org/abs/1003.6119 (first public version 2010-03-30).
- P. K. Shukla, N. Doll and H. Schmeck, *A Theoretical Analysis of Volume Based Pareto Front Approximations*, GECCO (2014), 1415–1422, https://doi.org/10.1145/2576768.2598348.
