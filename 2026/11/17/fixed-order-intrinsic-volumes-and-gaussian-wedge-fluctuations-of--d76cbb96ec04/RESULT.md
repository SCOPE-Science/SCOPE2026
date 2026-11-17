# Fixed-order intrinsic volumes and Gaussian wedge fluctuations of the White Whale zonotope

## Finding

Let \(d\ge 1\), and define the **White Whale zonotope** in its unscaled canonical Euclidean realization by
\[
W_d=\sum_{\varnothing\ne S\subseteq[d]}[0,\mathbf1_S]\subset\mathbb R^d.
\]
Its intrinsic volumes \(V_k\) are normalized by the Steiner polynomial
\[
\operatorname{Vol}_d(W_d+tB_d)=\sum_{k=0}^d\kappa_{d-k}V_k(W_d)t^{d-k}.
\]
For each fixed integer \(k\ge1\), as \(d\to\infty\) through integers with \(d\ge k\),
\[
\boxed{V_k(W_d)=\frac{2^{dk}\sqrt{k+1}}{2^k k!}\,d^{k/2}\left(1-\frac{k^3}{4(k+1)d}+O_k(d^{-2})\right).}
\tag{1}
\]
For \(k\) independent, uniformly chosen Boolean column vectors \(B_1,\ldots,B_k\in\{0,1\}^d\), let \(T_{d,k}=\|B_1\wedge\cdots\wedge B_k\|\), with zero wedge volume for dependent columns. Then
\[
\boxed{\frac{T_{d,k}-2^{-k}\sqrt{k+1}\,d^{k/2}}{d^{(k-1)/2}}\ \Longrightarrow\ N\left(0,\frac{k}{2\cdot4^k}\right).}
\tag{2}
\]
These statements include an exact finite-dimensional reduction, valid for every integer \(1\le k\le d\): if \(\epsilon\in\{0,1\}^k\) and \(n_\epsilon\) are nonnegative integers summing to \(d\), then
\[
\boxed{V_k(W_d)=\frac1{k!}\sum_{\sum_\epsilon n_\epsilon=d}\frac{d!}{\prod_\epsilon n_\epsilon!}\sqrt{\det\left(\sum_\epsilon n_\epsilon\,\epsilon\epsilon^{\mathsf T}\right)}.}
\tag{3}
\]
The determinant is interpreted as zero for singular matrices. The unscaled formula (3) is an application of the established general zonotope intrinsic-volume identity, rather than an independently new identity; the explicit asymptotic constants and Gaussian law in (1)-(2) are the present mathematical contribution.

As a geometric consequence, for every fixed \(k\ge1\),
\[
\boxed{\frac{k!V_k(W_d)}{V_1(W_d)^k}=\frac{\sqrt{k+1}}{2^{k/2}}\left(1-\frac{k(2k+1)(k-1)}{8(k+1)d}+O_k(d^{-2})\right).}
\tag{4}
\]
In particular, the two-dimensional normalized intrinsic-volume ratio tends to \(\sqrt3/2\), and its first correction is \(-5/(12d)\) relative to that limit. The persistence of a non-unit limiting ratio records macroscopic angular alignment among the subset generators, rather than asymptotic orthogonality.

## Assumptions and scope

All distances, wedge volumes, balls and intrinsic volumes use the standard Euclidean structure of \(\mathbb R^d\). The generators are the \(2^d-1\) nonzero Boolean vectors, each occurring once and with segment length equal to its Euclidean norm; no unit-length normalization is imposed. The random columns in (2) are sampled with replacement from all \(2^d\) Boolean vectors, including zero. This convention is exact for intrinsic-volume averages because a repeated or zero column contributes zero wedge volume. The order \(k\) is held fixed throughout the asymptotic claims. Neither a uniform estimate in growing \(k\) nor the regime \(k/d\to\rho>0\) is asserted.

## Proof

**1. Exact reduction.** The known zonotope formula (see Joós--Lángi, Corollary 1, and Breiding--Bürgisser--Lerario--Mathis, Theorem 5.2) is
\[
V_k\!\left(\sum_j[0,v_j]\right)=\sum_{j_1<\cdots<j_k}\|v_{j_1}\wedge\cdots\wedge v_{j_k}\|.
\]
Because repeated and zero Boolean columns contribute zero, replacing distinct unordered tuples by all ordered tuples with replacement gives exactly
\[
V_k(W_d)=\frac{2^{dk}}{k!}\,\mathbb E T_{d,k}.
\tag{5}
\]
Arrange the \(k\) random Boolean columns into a \(d\times k\) matrix \(B\). Its \(d\) rows \(\xi_1,\ldots,\xi_d\) are independent and uniform on \(\{0,1\}^k\), and
\[
T_{d,k}=\sqrt{\det(B^{\mathsf T}B)},\qquad B^{\mathsf T}B=\sum_{a=1}^d\xi_a\xi_a^{\mathsf T}.
\]
Grouping the rows by their \(2^k\) possible patterns gives (3), since a prescribed pattern-count vector has multinomial multiplicity \(d!/\prod n_\epsilon!\).

**2. Mean matrix and scalar moments.** Set \(G_d=d^{-1}B^{\mathsf T}B\), and let \(f(H)=\sqrt{\det H}\) on positive definite symmetric matrices. Direct computation gives
\[
M=\mathbb E(\xi\xi^{\mathsf T})=\frac14(I_k+\mathbf1\mathbf1^{\mathsf T}),
\quad M^{-1}=4\left(I_k-\frac{\mathbf1\mathbf1^{\mathsf T}}{k+1}\right),
\quad f(M)=\frac{\sqrt{k+1}}{2^k}.
\tag{6}
\]
Put \(X=\xi\xi^{\mathsf T}-M\), and \(U=\xi^{\mathsf T}M^{-1}\xi\). If \(R=\sum_i\xi_i\sim\operatorname{Bin}(k,1/2)\), then
\[
U=\frac{4R(k+1-R)}{k+1},\quad
\mathbb EU=k,\quad
\mathbb EU^2=\frac{k(k^2+k+2)}{k+1},\quad
\operatorname{Var}(U)=\frac{2k}{k+1}.
\tag{7}
\]
These identities follow by expanding the fourth-degree polynomial in \(R\) and using the first four binomial factorial moments. Also,
\[
\operatorname{tr}(M^{-1}X)=U-k,\quad
\operatorname{tr}\bigl((M^{-1}X)^2\bigr)=U^2-2U+k.
\tag{8}
\]

**3. Gaussian fluctuations.** The matrices \(\xi_a\xi_a^{\mathsf T}\) are bounded and independent, so \(G_d\to M\) almost surely. The ordinary scalar central limit theorem applied to \(\operatorname{tr}(M^{-1}X_a)=U_a-k\), combined with the first derivative
\[
Df(M)[H]=\tfrac12 f(M)\operatorname{tr}(M^{-1}H),
\]
shows that \(\sqrt d\,(f(G_d)-f(M))\) converges in law to a centered Gaussian with variance
\[
\frac{f(M)^2}{4}\operatorname{Var}(U)=\frac{k}{2\cdot4^k}.
\]
Since \(T_{d,k}=d^{k/2}f(G_d)\), this proves (2). The possible singularity of \(G_d\) at finite \(d\) is harmless: convergence to the positive definite \(M\) places \(G_d\) in a positive definite neighborhood with probability tending to one.

**4. Two-term expectation expansion.** On a small fixed positive definite neighborhood of \(M\), the Taylor expansion is
\[
\frac{f(M+H)}{f(M)}=1+\tfrac12\operatorname{tr}(M^{-1}H)
+\tfrac18\operatorname{tr}(M^{-1}H)^2
-\tfrac14\operatorname{tr}((M^{-1}H)^2)+\text{terms of degree at least three}.
\tag{9}
\]
Here \(H=d^{-1}\sum_{a=1}^dX_a\). The linear expectation vanishes. Independence and centering imply that the expected quadratic contribution is \(d^{-1}\) times
\[
\frac18\mathbb E(U-k)^2-\frac14\mathbb E(U^2-2U+k)
=\frac{k}{4(k+1)}-\frac{k(k^2+1)}{4(k+1)}
=-\frac{k^3}{4(k+1)}.
\tag{10}
\]
For completeness, fixed \(k\) guarantees each row matrix is uniformly bounded. Matrix Hoeffding bounds show that \(\Pr(\|G_d-M\|>\delta)\le C_k e^{-c_kd}\) for any sufficiently small constant \(\delta>0\). The determinant square root is bounded on the compact set of possible \(G_d\), so the complement contributes exponentially little to its expectation. Within the neighborhood, Taylor expansion through degree four has a uniformly bounded fifth-order remainder; centered independence gives expected cubic and quartic terms \(O_k(d^{-2})\) and expected absolute fifth-order remainder \(O_k(d^{-5/2})\). Hence
\[
\mathbb Ef(G_d)=f(M)\left(1-\frac{k^3}{4(k+1)d}+O_k(d^{-2})\right).
\]
Multiplying by \(2^{dk}d^{k/2}/k!\) as in (5) proves (1). Finally the \(k=1\) case yields
\[
V_1(W_d)=2^d\sqrt{d/2}\left(1-\frac1{8d}+O(d^{-2})\right),
\]
and division proves (4). This also checks the normalization at the first intrinsic volume.

## Verification

The accompanying standalone \`verify.py\` checks the exact combinatorial identity by two distinct finite procedures: (i) enumerating all sets of \(k\) distinct, nonzero Boolean generators and computing integer Gram determinants; (ii) enumerating all \(2^k\)-pattern compositions of \(d\) and computing their multinomial-weighted Gram determinants. The procedures agree for all \(2\le d\le6\), \(1\le k\le\min(3,d)\), and additionally \((d,k)=(4,4)\), totaling 15 comparisons. Independent finite binomial sums reproduce (7), the Gaussian variance and correction (10) for \(1\le k\le10\); several larger two-column cases check convergence toward the correction \(-2/3\). The computation is finite corroboration, not a substitute for the analytic proof for all \(d\) and fixed \(k\).

To reproduce from a Python 3 standard-library environment, run \`python3 verify.py\`. Its successful final marker is \`BOOLEAN_INTRINSIC_PASS\`.

## Relationship to prior work

Deza--Hao--Pournin introduced efficient vertex and edge enumeration for the same all-nonzero-Boolean-generator zonotope. Their 2022 preprint establishes the exact generator convention and studies chamber, edge, and degree counts, not the fixed-index Euclidean intrinsic-volume expansion or generator-parallelotope Gaussian law. Joós--Lángi explicitly prove the general intrinsic-volume formula (already independently available in related work), which *does* imply the starting exact sum (5); the exact sum alone is therefore not claimed as original. Breiding--Bürgisser--Lerario--Mathis put random determinant and wedge expectations in a general zonoid framework, but do not compute the pattern-specific constants (6)-(10) for the White Whale. The new asymptotic is not obtained by renaming a published result: a noncentral Boolean Gram moment calculation and a second-order expectation expansion are required. The adjacent prior mathematical record on White Whale spherical widths and incenters concerns different Euclidean invariants, and its statements do not determine these \(V_k\) asymptotics.

## Limitations

All probabilistic and expansion statements hold with fixed \(k\), not uniformly over the full intrinsic-volume sequence. The short finite tests cannot establish any infinite-dimensional limit or historical uniqueness. No claim is made that the general zonotope intrinsic-volume identity is new. Historical priority for the specific constants remains provisional; unindexed work on noncentral Bernoulli Gram determinants may contain equivalent formulas. Independent mathematical audit has not been performed.

## References

1. A. Deza, M. Hao, L. Pournin, *Sizing the White Whale*, arXiv:2205.13309, first public 2022-05-26. https://arxiv.org/abs/2205.13309
2. A. Joós, Z. Lángi, *Isoperimetric Problems for Zonotopes*, arXiv:2206.03204, first public 2022-06-07. https://arxiv.org/abs/2206.03204
3. P. Breiding, P. Bürgisser, A. Lerario, L. Mathis, *The Zonoid Algebra, Generalized Mixed Volumes, and Random Determinants*, arXiv:2109.14996, first public 2021-09-30. https://arxiv.org/abs/2109.14996
