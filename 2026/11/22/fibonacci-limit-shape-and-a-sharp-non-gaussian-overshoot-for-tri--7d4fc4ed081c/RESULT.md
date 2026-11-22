# Fibonacci-limit shape and a sharp non-Gaussian overshoot for triangle-free exponential sticks

## Finding
Let \(X_1,\ldots,X_n\) be independent exponential lengths with common rate \(\lambda>0\). Let \(Y_1\le\cdots\le Y_n\) be their order statistics, \(S_n=\sum_{i=1}^{n}Y_i\), and let \(A_n\) be the event that **no three lengths form a nondegenerate triangle**. Write \(\varphi=(1+\sqrt5)/2\), and set \(c_j=\varphi^{-j-2}\) for integers \(j\ge0\).

**Conditional Fibonacci-shape and overshoot theorem.** For every fixed nonnegative integer \(m\), as \(n\to\infty\), conditionally on \(A_n\),
\[
\left(\frac{Y_{n-j}}{S_n}\right)_{j=0}^{m}\ \xrightarrow{\mathbb P}\ (c_j)_{j=0}^{m},
\qquad
\left(n\left[\frac{Y_{n-j}}{S_n}-c_j\right]\right)_{j=0}^{m}
\ \Longrightarrow\ (R_j)_{j=0}^{m},
\]
where all \(R_j\) are constructed from a common independent sequence of rate-one exponential random variables \((E_r)_{r\ge1}\):
\[
R_j=\sum_{r=1}^{\infty}a_{j,r}E_r,\qquad
a_{j,r}={\mathbf{1}}_{\{r>j\}}\frac{F_{r-j}}{G_r}-c_j,
\quad G_r=F_{r+2}-1,
\]
with \(F_0=0,F_1=F_2=1\) and \(F_{r+2}=F_{r+1}+F_r\). Each series is absolutely convergent almost surely and in \(L^1\).

For the **largest stick**, \(R_0\) is nondegenerate, non-Gaussian and strictly positive almost surely, and
\[
\mathbb E e^{-sR_0}=\prod_{r=1}^{\infty}(1+s b_r)^{-1},\quad
b_r=\frac{F_r}{G_r}-\varphi^{-2}
=\frac{1-(-\varphi^{-1})^r}{\varphi^2G_r}>0,\qquad s\ge0.
\]
Its upper tail has the **exact leading coefficient**
\[
\boxed{\mathbb P(R_0>t)\sim\frac{\varphi^3}{\sqrt5}e^{-\varphi t}\qquad (t\to\infty).}
\]
In particular, \(\mathbb ER_0\simeq0.98369455639074\), \(\operatorname{Var}(R_0)\simeq0.41375352870235\), and \(\varphi^3/\sqrt5\simeq1.894427191\).

## Assumptions and scope
The lengths are independent identically distributed continuous exponential variables; the common rate is arbitrary and cancels from the normalized statements. All limits concern the conditional distributions given \(A_n\); the index \(m\) is fixed, not increasing with \(n\). Boundary equalities have probability zero. The event has strictly positive probability for every finite \(n\ge3\). The result concerns normalized top-order statistics, not the unconditional law of exponential order statistics or the already-known probability of \(A_n\).

## Proof
**1. Exact conditional representation (existing finite-dimensional reduction).** The no-triangle event is equivalent to \(Y_i\ge Y_{i-1}+Y_{i-2}\) for all \(3\le i\le n\); the two largest members of any chosen triple give its most restrictive possible triangle inequality. Define slacks
\[
Z_1=Y_1,\quad Z_2=Y_2-Y_1,\quad Z_i=Y_i-Y_{i-1}-Y_{i-2}\quad(i\ge3).
\]
The transformation is triangular with determinant one. On \(A_n\), every slack is nonnegative, and the inverse recurrence yields
\[
Y_i=\sum_{k=1}^{i}F_{i-k+1}Z_k,
\quad S_n=\sum_{k=1}^{n}G_{n-k+1}Z_k,
\quad G_r=\sum_{a=1}^{r}F_a=F_{r+2}-1.
\]
The ordered exponential density is \(n!\lambda^n e^{-\lambda S_n}\), so conditioning on the slack orthant makes \(Z_k\) independent exponentials of rates \(\lambda G_{n-k+1}\). The associated integral recovers \(\mathbb P(A_n)=n!/\prod_{r=1}^{n}G_r\), a known formula **not claimed as new**.

Introduce \(E_r=\lambda G_r Z_{n-r+1}\). For each \(n\), these are independent rate-one exponentials; the coupling uses one infinite sequence. Reversing the slack sum gives the exact identities, under conditioning,
\[
\lambda S_n=\sum_{r=1}^{n}E_r,\qquad
\lambda Y_{n-j}=\sum_{r=j+1}^{n}\frac{F_{r-j}}{G_r}E_r
\quad (0\le j<n).
\]
Equivalently the vector \((E_r/\sum_{a=1}^{n}E_a)_{r=1}^{n}\) has the uniform Dirichlet distribution on the simplex. Both identities are exact for all finite \(n\).

**2. Joint conditional limit.** Binet's formula gives, for every fixed \(j\),
\[
\frac{F_{r-j}}{G_r}=c_j+O_j(\varphi^{-r})\quad(r\to\infty),
\]
so \(\sum_{r\ge1}|a_{j,r}|<\infty\). Thus the series defining \(R_j\) converges absolutely almost surely and in \(L^1\), since \(\mathbb E E_r=1\). The strong law gives \(n^{-1}\sum_{r=1}^{n}E_r\to1\) almost surely. Consequently,
\[
n\left(\frac{Y_{n-j}}{S_n}-c_j\right)
\overset{d}=\frac{n}{\sum_{r=1}^{n}E_r}\sum_{r=1}^{n}a_{j,r}E_r
\longrightarrow R_j
\]
almost surely under this coupling, jointly for any fixed finite set of \(j\). Dividing by \(n\) also proves the deterministic top-stick proportions.

**3. One-sided overshoot and exact tail.** For \(j=0\), put \(b_r=F_r/G_r-\varphi^{-2}\). Binet's formula yields the displayed identity \(b_r=(1-(-\varphi^{-1})^r)/(\varphi^2G_r)>0\) and \(\sum b_r<\infty\). Moreover \(b_1=\varphi^{-1}\), and \(b_r<\varphi^{-1}\) for every \(r\ge2\) (indeed \(F_r/G_r\le1/2\) for \(r\ge2\)). Hence \(R_0=b_1E_1+T\), where \(T=\sum_{r\ge2}b_rE_r\) is independent of \(E_1\); this proves non-Gaussianity and positivity.

The key exact telescope uses the Fibonacci relation \(F_{r+1}=F_r+F_{r-1}\):
\[
1-\varphi b_r=\frac{\varphi G_{r-1}}{G_r}\quad(r\ge2),
\qquad
\prod_{r=2}^{N}(1-\varphi b_r)^{-1}
=\frac{G_N}{\varphi^{N-1}}
\longrightarrow\frac{\varphi^3}{\sqrt5}.
\]
Since \(\sup_{r\ge2}b_r<\varphi^{-1}\) and \(\sum b_r<\infty\), there exists \(\varepsilon>0\) such that \(\mathbb E e^{(\varphi+\varepsilon)T}<\infty\). Conditioning on \(T\) shows
\[
\mathbb P(R_0>t)=e^{-\varphi t}\mathbb E[e^{\varphi T}{\mathbf{1}}_{\{T\le t\}}]+\mathbb P(T>t).
\]
The first term divided by \(e^{-\varphi t}\) tends to \(\mathbb E e^{\varphi T}=\varphi^3/\sqrt5\), and the second is smaller order by the stronger exponential moment. This proves the sharp tail equivalent. The Laplace product follows by independence and absolute convergence. Finally, \(\mathbb ER_0=\sum b_r\) and \(\operatorname{Var}(R_0)=\sum b_r^2\).

## Verification
The standalone Python 3 file `check.py` uses only the standard library. Run `python3 check.py`; it tests exact Fibonacci slack reconstruction, exact normalizers, finite conditioned Dirichlet moments, Cassini-derived monotonicity, the positive overshoot coefficients and the finite telescoping product, and prints numerical limiting constants. In this package, **6,966 assertions passed**. These finite symbolic and numerical checks corroborate formulas but do **not** establish the infinite-dimensional convergence, exponential moment or exact tail; those follow from the analytical proof above.

## Relationship to prior work
Barczy and Lovas (arXiv:2611.04436) study exponential and Pareto stick-sample triangle avoidance probabilities and explicitly give the Fibonacci product for exponentials. Mukerjee (arXiv:2207.07879) already derives the same triangular linear slack change of variables and exact probability, so the finite transformation is prior work, not the new theorem. Brennan, Callow and Lin (arXiv:2604.27573) generalize probability calculations to polygons; Verreault (arXiv:2107.10318) gives a discrete partition-analysis treatment. The present result is specifically the joint conditional asymptotic **top-length shape**, its order-\(1/n\) non-Gaussian fluctuations, and the exact exponential overshoot tail coefficient. Published published-finding corpus work on Pareto triangle-free sticks gives a quadratic rarity exponent for a different length distribution, not these conditional exponential shape limits.

## Limitations
The theorem treats fixed indices of the largest lengths only; it does not claim a full process-level limit for a growing number of ranks or a universal distribution-class extension. The tail equivalent is for the limiting overshoot variable, not a uniform-in-\(n\) finite-sample tail estimate. Earlier general Dirichlet or conditioned-cone results could imply special cases; historical priority remains a risk despite the targeted comparisons. No independent mathematical audit has been performed.

## References
- M. Barczy and R. Lovas, *Pick-up sticks problems for exponential and Pareto distributions*, arXiv:2611.04436, first public November 3, 2026. https://arxiv.org/abs/2611.04436
- S. Mukerjee, *A Statistical Approach to Broken Stick Problems*, arXiv:2207.07879 (2022). https://arxiv.org/abs/2207.07879
- C. Brennan, A. Callow and J. Lin, *Fibonacci numbers and the probability of polygon formation using random length sticks*, arXiv:2604.27573 (2026). https://arxiv.org/abs/2604.27573
- S. Verreault, *MacMahon Partition Analysis: A discrete approach to broken stick problems*, arXiv:2107.10318 (2021). https://arxiv.org/abs/2107.10318
- published-finding corpus, *Sharp quadratic decay for triangle-free Pareto stick samples* (November 8, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-quadratic-decay-for-triangle-free-pareto-stick-samples--8d0ac1d44459
