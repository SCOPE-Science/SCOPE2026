# Critical inverse moments and logarithmic tails of random Fourier interpolation

## Finding

**Theorem (sharp heavy-tail hierarchy for square random Fourier sampling).** Fix an integer \(n\ge 2\). Let \(U_1,\ldots,U_n\) be independent uniform random variables on \([0,1)\), write \(z_j=e^{2\pi iU_j}\), and form the unnormalized square Fourier interpolation matrix
\[
V_{j,k}=z_j^k,\qquad 1\le j\le n,\quad 0\le k<n.
\]
The nodes are pairwise distinct with probability one, so the inverse is defined almost surely. Define the squared inverse-Frobenius amplification
\[
R_n=\operatorname{tr}((V^*V)^{-1})=\|V^{-1}\|_F^2,\qquad W_n=\sqrt{R_n}.
\]
For each fixed \(n\) there are constants \(0<c_n\le C_n<\infty\) such that, for all sufficiently large \(T\),
\[
c_n\frac{(\log T)^{n-2}}{T}
\le \mathbb P(W_n>T)\le
C_n\frac{(\log T)^{n-2}}{T}.
\]
Both exponents are sharp. In particular, for any real \(s\ge0\),
\[
\boxed{\mathbb E[R_n^s]<\infty\quad\Longleftrightarrow\quad 0\le s<\tfrac12.}
\]
At the critical exponent the truncated expectation has the dimension-dependent exact **power of the logarithm**
\[
\boxed{\mathbb E[\min\{W_n,T\}]\asymp_n (\log T)^{n-1}\quad(T\to\infty).}
\]
Here \(\asymp_n\) means upper and lower positive constant multiples depending only on \(n\), not a claimed leading-constant limit.

The theorem also identifies an exact nodal interpolation surrogate. Set
\[
P_j=\prod_{\ell\ne j}|z_j-z_\ell|^{-1}.
\]
For every \(0\le s<1\),
\[
\boxed{
\mathbb E[P_j^s]=
\left(2^{-s}\frac{\Gamma((1-s)/2)}{\sqrt\pi\,\Gamma(1-s/2)}\right)^{n-1}.
}
\]
Writing \(k=n-1\), its one-point tail and critical truncation even have explicit leading constants:
\[
\mathbb P(P_j>T)\sim
\frac{(\log T)^{k-1}}{\pi^k(k-1)!\,T},
\qquad
\mathbb E[\min\{P_j,T\}]\sim
\frac{(\log T)^k}{\pi^k k!}.
\]
The exact surrogate asymptotics imply, but do not assert exact leading constants for, the two-sided bounds on \(W_n\).

## Assumptions and scope

The sample locations are independent and exactly uniform on the circle. The frequency set is a consecutive block of \(n\) integers; replacing \(\{0,\ldots,n-1\}\) by any translated block multiplies the rows by unit-modulus scalars, leaving every singular value and the theorem unchanged. The matrix is not divided by \(\sqrt n\). For a \(1/\sqrt n\)-normalized matrix the same powers and thresholds hold, with fixed dimension-dependent scale factors. Expectations are with respect to the sampling nodes. All asymptotics take \(T\to\infty\) **at fixed \(n\)**; this result makes no claim of uniform constants as \(n\to\infty\).

The noise-amplification quantity \(R_n\) is the sum of reciprocal squared singular values for the square regression design. A consequence for ordinary mean-square reconstruction risk is its divergence, but the theorem resolves every nonnegative fractional moment and the precise logarithmic tail degree of its square root.

## Proof

**1. Exact Lagrange inverse and deterministic comparison.** For distinct nodes, the \(j\)-th column of \(V^{-1}\) is the coefficient vector of the Lagrange polynomial
\[
L_j(X)=\frac{\prod_{\ell\ne j}(X-z_\ell)}{\prod_{\ell\ne j}(z_j-z_\ell)}.
\]
Write \(k=n-1\). The numerator is monic, so its coefficient Euclidean norm is at least one. Its coefficient of degree \(r\) is an elementary symmetric sum of \(k-r\) unimodular numbers, bounded by \(\binom{k}{r}\) in absolute value. By Vandermonde's binomial identity the sum of squared coefficient bounds is \(\binom{2k}{k}\). Therefore **for every realization of distinct nodes**,
\[
\sum_{j=1}^n P_j^2\le R_n\le
\binom{2k}{k}\sum_{j=1}^n P_j^2.
\]
In particular, with \(B_k=\sqrt{\binom{2k}{k}}\),
\[
P_1\le W_n\le B_k\sum_{j=1}^{n}P_j.
\tag{1}
\]
These are deterministic, and do not use a probabilistic matrix estimate.

**2. Exact law of a single reciprocal chord.** Conditional on \(z_j\), all \(z_\ell/z_j\) for \(\ell\ne j\) are independent uniform points on the unit circle. Thus \(P_j\) is a product of \(k\) independent copies of \(X=|1-e^{2\pi iU}|^{-1}\). Its density is
\[
f_X(x)=\frac{1}{\pi x^2\sqrt{1-1/(4x^2)}}\mathbf 1_{\{x>1/2\}}.
\]
The beta integral gives, for \(0\le s<1\),
\[
\mathbb E[X^s]
=\int_0^1(2|\sin(\pi u)|)^{-s}\,du
=2^{-s}\frac{\Gamma((1-s)/2)}{\sqrt\pi\,\Gamma(1-s/2)}.
\]
The integral is infinite for \(s\ge1\), because \(\sin(\pi u)\) vanishes linearly at zero. Conditional independence yields the asserted exact formula for \(\mathbb E[P_j^s]\).

**3. Sharp logarithmic product-tail law.** Set \(Y=\log X\), supported on \(( -\log 2,\infty)\). The change of variables in the preceding density gives
\[
f_Y(y)=\frac{e^{-y}}{\pi\sqrt{1-e^{-2y}/4}}\mathbf1_{\{y>-\log2\}}.
\]
In particular \(e^y f_Y(y)\to 1/\pi\) as \(y\to\infty\). The function \(e^y f_Y(y)\) is integrable over every bounded interval starting at \(-\log2\), including the square-root singularity at the left endpoint.

For \(k\) independent copies \(Y_1,\ldots,Y_k\), convolution over the simplex \(\sum y_i=y\) shows that the density \(g_k\) of their sum satisfies
\[
g_k(y)\sim\frac{e^{-y}y^{k-1}}{\pi^k(k-1)!}\quad (y\to\infty).
\tag{2}
\]
To verify the constant, fix a large \(H\) and divide the simplex into the region where all \(y_i\ge H\) and its complement. On the former, every \(e^{y_i}f_Y(y_i)\) lies within any preassigned tolerance of \(1/\pi\); its \((k-1)\)-volume is \((y-kH)^{k-1}/(k-1)!\). On the complement, at least one coordinate is bounded above by \(H\). Integration of its locally integrable factor leaves at most \(O_H(y^{k-2})\) times \(e^{-y}\) for \(k\ge2\), using a global bound on \(e^u f_Y(u)\) for \(u\ge H\). Repeating this decomposition for multiple bounded coordinates handles the endpoint singularities. For \(k=1\), (2) is exactly the one-density asymptotic. Letting the tolerance tend to zero proves (2).

Now \(P_j=\exp(Y_1+\cdots+Y_k)\). Integrating (2) from \(\log T\) to infinity, and then integrating the resulting tail from a fixed starting point to \(T\), yields
\[
\mathbb P(P_j>T)\sim\frac{(\log T)^{k-1}}{\pi^k(k-1)!\,T},
\qquad
\mathbb E[\min\{P_j,T\}]\sim\frac{(\log T)^k}{\pi^k k!}.
\tag{3}
\]
No assumption of independence between distinct \(P_j\)'s is used.

**4. Tail and moment transfer to the actual matrix.** From (1), the union bound and exchangeability give
\[
\mathbb P(P_1>T)\le \mathbb P(W_n>T)
\le n\,\mathbb P\big(P_1>T/(nB_k)\big).
\]
Insert (3), with fixed \(n\), to obtain the two-sided \((\log T)^{n-2}/T\) tail bound. Finally, for any nonnegative random variable \(W\) and \(\rho>0\),
\[
\mathbb E[W^\rho]=\rho\int_0^\infty t^{\rho-1}\mathbb P(W>t)\,dt,
\qquad
\mathbb E[\min\{W,T\}]=\int_0^T\mathbb P(W>t)\,dt.
\]
The first integral for \(W=W_n\) is finite precisely when \(\rho<1\), and the second has order \((\log T)^{n-1}\). Since \(R_n=W_n^2\), substitute \(\rho=2s\). This proves all assertions. \(\square\)

## Verification

`CHECK.py` is a supplementary executable test using NumPy and SciPy. It tests the exact Lagrange coefficients against numerical inverse matrices for deterministic random nodes in each order from two through ten, checks the deterministic norm comparison, evaluates the Mellin integral by quadrature against the gamma formula, and verifies the explicit two-node identity. The extracted checker returned `CHECK_OK assertions=1015 dimensions=2..10`.

The infinite statements are proved by the integral, convolution and deterministic comparison arguments above. The checker is not a numerical demonstration of asymptotic tail constants; Monte Carlo estimates near critical tails are unreliable at feasible sample counts.

## Relationship to prior work

Xu and Shen (2026) study expected reconstruction risk of trigonometric regression with independent random or jittered nodes and prove divergence of the ordinary expected inverse spectral risk under independent uniform sampling. Their results motivate asking what fractional risks remain integrable and how the critical fluctuations behave. The exact sharp fractional threshold and the logarithmic degree of the fixed-size tail derived here are not among the inspected statements.

Tucci and Whiting (2012, later published in 2014) derive explicit inverse Vandermonde formulas and show nonexistence of positive integer-power inverse Gram moments. Their inverse formula is acknowledged as classical input: the present conclusion comes from a sharp independent reciprocal-chord product distribution and a deterministic norm comparison, extending from integer moment divergence to a complete fractional-moment threshold and all fixed-dimensional logarithmic tail exponents.

Kunis and Nagel (2019) provide deterministic smallest-singular-value bounds for clustered multivariate Vandermonde matrices. Their geometrical lower bounds do not provide the probability law of the inverse Frobenius norm under independent uniform random nodes.

Bass and Gröchenig (2004/05) established probability bounds on the condition numbers of random trigonometric sampling matrices. Only the accessible article abstract and first-page publisher preview could be read; a full theorem-level comparison with this potentially related source remains unresolved. The currently inspected material does not assert the fixed-square inverse-Frobenius logarithmic tail or the fractional moment threshold. This source is an explicit residual originality risk, not evidence of noncoverage.

The results are stated for unnormalized, square, consecutive-frequency matrices. Known general matrix inequalities or asymptotic large-dimension singular-value statements do not by themselves imply the sharp logarithmic tail degree at each fixed dimension. Earlier unindexed equivalent random interpolation estimates remain a novelty risk.

## Limitations

The theorem treats square matrices and independent uniform nodes. For overdetermined matrices, node collisions need not create a singular design, and the stated threshold cannot be transferred automatically. Constants hidden in \(\asymp_n\) are not uniform in the matrix size, and an exact leading tail constant for \(W_n\) is not claimed. No heavy-tail law is asserted for nonconsecutive frequency patterns or correlated sampling. The novelty comparison is based on the specifically inspected accessible sources and searches; absence of a match cannot establish exhaustive originality. Independent validation has not been performed.

## References

1. H. Xu and Y. Shen, *Non-asymptotic Analysis of Expected Reconstruction Risk for Trigonometric Polynomial Models*, arXiv:2609.29286, initially submitted 2026-09-24. https://arxiv.org/abs/2609.29286
2. G. H. Tucci and P. A. Whiting, *Asymptotic Behavior of the Maximum and Minimum Singular Value of Random Vandermonde Matrices*, arXiv:1202.3184, initially submitted 2012-02-15; *J. Theoret. Probab.* 27 (2014), 826–862. https://arxiv.org/abs/1202.3184
3. S. Kunis and D. Nagel, *On the smallest singular value of multivariate Vandermonde matrices with clustered nodes*, arXiv:1907.07119, initially submitted 2019-07-16. https://arxiv.org/abs/1907.07119
4. R. F. Bass and K. Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, *SIAM J. Math. Anal.* 36 (2004/05), 773–795, DOI:10.1137/S0036141003432316. https://doi.org/10.1137/S0036141003432316
