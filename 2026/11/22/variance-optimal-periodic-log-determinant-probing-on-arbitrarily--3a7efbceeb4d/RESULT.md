# Variance-optimal periodic log-determinant probing on arbitrarily weighted paths

## Finding

Let \(n\ge2\). Let \(A=\operatorname{diag}(q_1,\ldots,q_n)+L_c\), where \(q_i>0\) and \(L_c\) is the weighted path Laplacian with strictly positive consecutive-edge conductances \(c_1,\ldots,c_{n-1}\). For each integer budget \(1\le k\le n\), partition the vertices into exactly \(k\) nonempty classes and use one *independent* class-supported Rademacher vector per class to estimate \(\operatorname{tr}(\log A)=\log\det A\). Then the **unique unlabeled minimum-variance partition**, for every choice of the weights, is

\[
\mathcal C_k=\{\{i: i\equiv r\pmod k\}:r=1,\ldots,k\}.
\]

This classification remains valid for a larger, precisely defined class of spectral trace targets: any real symmetric matrix \(B\), with arbitrary diagonal and whose off-diagonal magnitudes satisfy

\[
|B_{ij}|=\int_{[0,\infty)} [(A+sI)^{-1}]_{ij}\,\rho(ds),\qquad i<j,
\]

where \(\rho\) is any nonzero positive Borel measure and every displayed integral is finite. Examples are \(B=\log A\) (Lebesgue measure; negative off-diagonals) and \(B=A^{-\alpha}\) for \(0<\alpha\le1\) (positive off-diagonals). The independent class-supported quadratic estimator is unbiased for the trace of \(B\), and the same periodic partition uniquely minimizes its variance.

For the special homogeneous path \(A_n=\mu I+L(P_n)\), with \(\mu>0\) fixed and unit edge conductances, the optimal log-determinant variance \(V_{n,k}\) has the explicit large-path density, for each fixed \(k\),

\[
\lim_{n\to\infty}\frac{V_{n,k}}n=\frac4{k^2}\operatorname{Li}_2(r^{2k}),\qquad
r=\frac{\mu+2-\sqrt{\mu(\mu+4)}}2\in(0,1),
\]

where \(\operatorname{Li}_2(z)=\sum_{j=1}^{\infty}z^j/j^2\) on \(0\le z<1\). These are exact quadratic-form variances; errors from approximating matrix logarithm actions are outside the claim.

## Assumptions and scope

Number vertices consecutively from \(1\) to \(n\), with \(c_i>0\) on edge \(i,i+1\), and let missing endpoint conductances be zero. Then \(A\) has diagonal \(q_i+c_{i-1}+c_i\), adjacent off-diagonals \(-c_i\), and all other off-diagonals zero. Positivity of every \(q_i\) ensures \(A\) is symmetric positive definite. The matrix logarithm is its real principal symmetric logarithm.

For a partition \(\mathcal C=\{C_1,\ldots,C_k\}\), independently choose signs \(\epsilon_i^{(r)}\in\{-1,1\}\) on \(C_r\), each with probability \(1/2\), and set \(z_i^{(r)}=\epsilon_i^{(r)}\) on \(C_r\) and zero elsewhere. Define \(\widehat\tau_B=\sum_{r=1}^k(z^{(r)})^TBz^{(r)}\). The budget counts class-supported quadratic forms; no claim is made about estimators based on jointly coupled probes, partial matrix-function evaluation, biased approximations, or a different cost model. Equal classes are *not* assumed.

## Proof

### 1. Exact trace variance

Independence and \(\mathbb E[\epsilon_i\epsilon_j]=\mathbf 1_{i=j}\) give \(\mathbb E\widehat\tau_B=\operatorname{tr}B\). Each unordered pair within one class contributes \(2B_{ij}\epsilon_i\epsilon_j\) to the centered quadratic form, and distinct unordered pairs are uncorrelated. Consequently

\[
V_B(\mathcal C):=\operatorname{Var}(\widehat\tau_B)
=4\sum_{1\le i<j\le n}\mathbf 1_{\mathcal C(i)=\mathcal C(j)}B_{ij}^{2}.
\]

### 2. Increasing/decreasing Green factors

For \(s\ge0\), write \(R_s=(A+sI)^{-1}\). Define left and right positive sequences \(u_s(i)\), \(v_s(j)\) as follows: \(u_s(1)=1\), \(v_s(n)=1\), and let each satisfy the homogeneous second-order difference equation associated with \(A+sI\) toward its corresponding interior. Set \(u_s(0)=0\) and \(v_s(n+1)=0\). Thus for \(1\le i<n\),

\[
c_i\bigl(u_s(i+1)-u_s(i)\bigr)
=c_{i-1}\bigl(u_s(i)-u_s(i-1)\bigr)+(q_i+s)u_s(i),
\]

with \(c_0=0\), and the reflected relation holds for \(v_s\). Positivity of the conductances and killing rates proves \(u_s(i)>u_s(i-1)\ge0\) and \(v_s(j)>v_s(j+1)\ge0\). The standard tridiagonal inverse formula, or a direct discrete-Wronskian calculation, gives

\[
R_s(i,j)=d_su_s(i)v_s(j),\qquad i\le j,\quad d_s>0.
\]

For completeness, if \(D_s=\det(A+sI)>0\), and \(\theta_{i-1}(s)\) and \(\phi_{j+1}(s)\) are the leading and trailing principal-minor determinants (empty minors equal one), then one may take

\[
u_s(i)=\frac{\theta_{i-1}(s)}{\prod_{t=1}^{i-1}c_t},\quad
v_s(j)=\frac{\phi_{j+1}(s)}{\prod_{t=j}^{n-1}c_t},\quad
d_s=\frac{\prod_{t=1}^{n-1}c_t}{D_s}.
\]

These expressions reconstruct every off-diagonal of \(R_s\), including the boundaries.

### 3. A strictly positive interval-square certificate

Let \(H_{ij}=|B_{ij}|\) for \(i<j\) and \(W_{ij}=H_{ij}^2\). By the positive-mixture hypothesis and Tonelli's theorem,

\[
W_{ij}=\int\!\int d_sd_t\,[u_s(i)u_t(i)]\,[v_s(j)v_t(j)]\,\rho(ds)\rho(dt),\qquad i<j.
\]

For \(1\le a<b\le n\), define the interval coefficient

\[
T_{ab}=\int\!\int d_sd_t\,
\bigl(u_s(a)u_t(a)-u_s(a-1)u_t(a-1)\bigr)
\bigl(v_s(b)v_t(b)-v_s(b+1)v_t(b+1)\bigr)
\,\rho(ds)\rho(dt).
\]

Every integrand is strictly positive, and the measure is nonzero, hence \(T_{ab}>0\). They are finite because \(0<T_{ab}\le W_{ab}<\infty\), as shown by the following telescoping identity:

\[
W_{ij}=\sum_{a=1}^{i}\sum_{b=j}^{n}T_{ab},\qquad 1\le i<j\le n.
\]

This crucial decomposition is for the **square of the entire mixture** and hence includes cross terms between different resolvent shifts. It is not obtained by merely averaging separate resolvent variances.

### 4. Simultaneous interval balance and uniqueness

For interval \([a,b]\), let \(N_r[a,b]=\#(C_r\cap[a,b])\), and set \(\ell=b-a+1\). Counting equal-color unordered pairs in each interval gives the exact identity

\[
V_B(\mathcal C)
=2\sum_{a<b}T_{ab}\left(\sum_{r=1}^{k}N_r[a,b]^2-\ell\right).
\]

For nonnegative integers \(N_r\) summing to \(\ell\), the minimum of \(\sum_rN_r^2\) is

\[
Q_k(\ell)=(k-t)h^2+t(h+1)^2,
\qquad h=\lfloor\ell/k\rfloor,\quad t=\ell-kh,
\]

attained exactly when the \(k\) counts differ by at most one. Every interval in the periodic partition \(\mathcal C_k\) has this property, so it minimizes every strictly positively weighted term simultaneously. Moreover,

\[
V_B(\mathcal C)-V_B(\mathcal C_k)
=2\sum_{a<b}T_{ab}\Bigl(\sum_rN_r[a,b]^2-Q_k(b-a+1)\Bigr)\ge0.
\]

Equality forces every interval to have balanced color counts. In particular, every length-\(k\) interval contains all \(k\) colors exactly once (if \(n=k\), the sole such interval does so). Comparing consecutive length-\(k\) windows forces the colors at positions \(i\) and \(i+k\) to coincide for all \(1\le i\le n-k\). Hence any minimizer equals \(\mathcal C_k\) up to relabeling. The cases \(k=1\) and \(k=n\) are included.

### 5. Application to the logarithm and fractional inverses

For any positive definite \(A\), scalar spectral calculus gives

\[
\log A=\int_0^\infty\left(\frac{1}{1+s}I-(A+sI)^{-1}\right)\,ds.
\]

For \(i<j\), the diagonal identity term vanishes; \((\log A)_{ij}=-\int_0^\infty R_s(i,j)\,ds\). Integrability follows from \(R_s(i,j)=O(s^{-2})\) as \(s\to\infty\) and nonsingularity at \(s=0\). This is exactly the positive-mixture hypothesis for off-diagonal magnitudes, with Lebesgue measure. Likewise, for \(0<\alpha<1\),

\[
A^{-\alpha}=\frac{\sin(\pi\alpha)}{\pi}\int_0^\infty s^{-\alpha}(A+sI)^{-1}\,ds,
\]

and \(A^{-1}=R_0\). Thus the stated applications follow.

### 6. Homogeneous-path variance density

Fix \(\mu>0\). The bilateral infinite path operator has Fourier symbol \(\mu+2-2\cos\theta=r^{-1}(1-2r\cos\theta+r^2)\). Expanding the logarithm gives off-diagonal Fourier coefficient \(-r^d/d\) at distance \(d\ge1\). Finite-path matrix logarithm entries converge to these coefficients when both endpoints recede, because for any fixed polynomial the relevant interior entries agree with those of the bilateral operator, and polynomials approximate \(\log\) uniformly on \([\mu,\mu+4]\). Analyticity on a complex neighborhood also yields uniform geometric off-diagonal decay: approximate \(\log\) by polynomials of degree \(d-1\) and use bandedness to obtain \(|(\log A_n)_{i,i+d}|\le C\eta^d\) for some \(C>0\), \(0<\eta<1\), independent of \(n,i,d\). Dominated convergence in the distance sum therefore gives

\[
\lim_{n\to\infty}\frac{V_{n,k}}n
=4\sum_{j=1}^\infty\frac{r^{2kj}}{(kj)^2}
=\frac4{k^2}\operatorname{Li}_2(r^{2k}).
\]

## Verification

`verify.py` uses only Python's standard library. It forms exact rational resolvent mixtures on fourteen heterogeneous killed paths of orders two through eight, checks all strictly positive interval coefficients and the telescoping identity, and exhaustively compares every unlabeled partition for each possible probe budget using exact fractions. It also checks the homogeneous logarithm's Fourier-series identity numerically at selected angles. The output is **21,587 passed assertions**. `verify_log_numeric.py` independently forms exact symmetric matrix logarithms up to floating-point eigensolver error for heterogeneous paths, enumerates the same partition objectives, and checks the homogeneous variance limit; its output is **21,184 passed comparisons**. Run:

```text
python verify.py
python verify_log_numeric.py
```

The second script needs NumPy and SciPy. These finite experiments independently exercise the formulae but do not replace the all-size analytic proof.

## Relationship to prior work

The 2013 hierarchical-probing work of Stathopoulos, Laeuchli, and Orginos develops distance-based colorings and variance reduction for inverse-matrix traces; it does not classify all fixed-budget log-determinant partitions of heterogeneous paths. Han, Malioutov, and Shin (first posted March 22, 2015) develop Chebyshev–Hutchinson log-determinant estimation and state the standard trace-variance formula, without a weighted-path optimum. Dorn and Enßlin (first posted April 10, 2015) develop an integral stochastic log-determinant method, without the present fixed-budget partition theorem. Benzi, Rinelli, and Simunec (2023), Section 3.1, study matrix-function probing and periodic distance colorings; the stated optimality minimizes the *number of colors* needed for a prescribed distance separation, not the *variance over every partition* at a prescribed number of independent Rademacher probes.

The standard one-resolvent case is already a natural special case of weighted-path Green probing. The new assertion requires controlling all **mixed-shift square cross terms** for matrix logarithms and positive resolvent mixtures; a minimization proved separately at each resolvent shift does not by itself imply minimization after squaring an integrated kernel. The interval-square decomposition supplies this missing implication.

## Limitations

The result compares independent, class-supported Rademacher probes with exact matrix-function quadratic evaluations, not arbitrary coupled-sign designs, deterministic biased graph-color estimators, or approximation/time-cost tradeoffs. On an isolated path, the ordinary determinant can already be found by a linear-time tridiagonal recurrence, so the logarithm theorem is a variance-design benchmark rather than a claim of a faster path log-determinant algorithm. Fractional inverse matrix-function traces need not have that simple determinant recurrence. Strictly positive conductances and killing rates are essential to the stated uniqueness proof; no statement about zero killing on singular paths is made. The infinite-volume density applies to fixed \(k\) and \(\mu>0\), not to budgets growing with path length. The underlying trace identity, tridiagonal Green factorization, and general graph-coloring principles are classical; independent validation and exhaustive publication-priority review have not been performed.

## References

1. A. Stathopoulos, J. Laeuchli, K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018, first posted 2013-02-17. https://arxiv.org/abs/1302.4018
2. I. Han, D. Malioutov, J. Shin, *Large-scale log-determinant computation through stochastic Chebyshev expansions*, arXiv:1503.06394, first posted 2015-03-22; ICML 2015. https://proceedings.mlr.press/v37/hana15.html
3. S. Dorn, T. A. Enßlin, *Stochastic determination of matrix determinants*, arXiv:1504.02661, first posted 2015-04-10. https://arxiv.org/abs/1504.02661
4. M. Benzi, M. Rinelli, I. Simunec, *Computation of the von Neumann entropy of large matrices via trace estimators and rational Krylov methods*, Numer. Math. 155 (2023), 377–414. https://doi.org/10.1007/s00211-023-01368-6
5. H. Avron, S. Toledo, *Randomized algorithms for estimating the trace of an implicit symmetric positive semi-definite matrix*, J. ACM 58 (2011), Article 8. https://doi.org/10.1145/1944345.1944349
