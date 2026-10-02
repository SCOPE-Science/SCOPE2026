# Tensor amplification of the strong maximal \(A_2\) obstruction

## Statement

Let \(M_d^{\mathrm{str}}\) be the strong maximal operator on \(\mathbb R^d\),
with averages over axis-parallel rectangles, and let
\([w]_{A_2^{\mathrm{str}}}\) denote the corresponding rectangular
\(A_2\) characteristic.

Set
\[
m=\left\lfloor \frac d2\right\rfloor .
\]
For every \(d\ge 2\) there are constants \(c_d>0\) and weights
\(W\in A_2^{\mathrm{str}}(\mathbb R^d)\) with arbitrarily large
\(A=[W]_{A_2^{\mathrm{str}}}\) such that
\[
\boxed{
\|M_d^{\mathrm{str}}\|_{L^2(W)\to L^2(W)}
\ge c_d\,A(\log A)^{m/2}.
}
\]
Consequently, if an estimate of the near-linear form
\[
\|M_d^{\mathrm{str}}\|_{L^2(w)\to L^2(w)}
\le C_d [w]_{A_2^{\mathrm{str}}}
\bigl(\log(e+[w]_{A_2^{\mathrm{str}}})\bigr)^\gamma
\]
holds for every rectangular \(A_2\) weight, then necessarily
\[
\boxed{\gamma\ge \frac12\left\lfloor\frac d2\right\rfloor.}
\]

More generally, the construction is multiplicative. If
\(1\le r\le \lfloor d/2\rfloor\) and
\(\theta_1,\ldots,\theta_r>0\) are sufficiently small, there is a weight
\(W_{\boldsymbol\theta}\) on \(\mathbb R^d\) satisfying
\[
[W_{\boldsymbol\theta}]_{A_2^{\mathrm{str}}}
\asymp_r \prod_{j=1}^r \theta_j^{-1}
\]
and
\[
\|M_d^{\mathrm{str}}\|_{L^2(W_{\boldsymbol\theta})\to
L^2(W_{\boldsymbol\theta})}
\gtrsim_r
\prod_{j=1}^r
\left(\theta_j^{-1}\sqrt{\log\frac1{\theta_j}}\right).
\]

## Input from the recent two-dimensional result

Lerner proved that for all sufficiently small \(\theta>0\) there is
\(w_\theta\in A_2^{\mathrm{str}}(\mathbb R^2)\) such that
\[
c\theta^{-1}\le [w_\theta]_{A_2^{\mathrm{str}}}\le C\theta^{-1}
\]
and
\[
\|M_2^{\mathrm{str}}\|_{L^2(w_\theta)\to L^2(w_\theta)}
\ge c\theta^{-1}\sqrt{\log(1/\theta)}.
\]
See A. K. Lerner, *Failure of the linear \(A_2\) bound for the strong
maximal operator*, arXiv:2609.14008.

The point here is that this two-dimensional logarithmic obstruction can be
amplified independently in disjoint coordinate pairs.

## Product lemma

Let \(d_1,d_2\ge1\), let \(w_i\) be weights on \(\mathbb R^{d_i}\), and set
\[
W(x,y)=w_1(x)w_2(y).
\]
Then
\[
\boxed{
[W]_{A_2^{\mathrm{str}}}
=
[w_1]_{A_2^{\mathrm{str}}}
[w_2]_{A_2^{\mathrm{str}}}.
}
\]
Indeed, every axis-parallel rectangle in
\(\mathbb R^{d_1+d_2}\) is \(R_1\times R_2\), and both the \(W\) and
\(W^{-1}\) averages factor. Taking suprema over \(R_1,R_2\) gives equality.

For tensor products \(F(x,y)=f_1(x)f_2(y)\), one likewise has the exact
pointwise identity
\[
\boxed{
M_{d_1+d_2}^{\mathrm{str}}F(x,y)
=
M_{d_1}^{\mathrm{str}}f_1(x)\,
M_{d_2}^{\mathrm{str}}f_2(y).
}
\]
The average of \(|F|\) over \(R_1\times R_2\) is the product of the two
averages, and the two rectangle choices are independent. Weighted \(L^2\)
norms also factor. Therefore
\[
\|M_{d_1+d_2}^{\mathrm{str}}\|_{L^2(W)\to L^2(W)}
\ge
\|M_{d_1}^{\mathrm{str}}\|_{L^2(w_1)\to L^2(w_1)}
\,
\|M_{d_2}^{\mathrm{str}}\|_{L^2(w_2)\to L^2(w_2)}.
\]
The same characteristic identity and tensor lower bound hold for general
\(A_p^{\mathrm{str}}\) and \(L^p\), although only the \(p=2\) consequence is
used below.

## Proof of the dimension-dependent lower bound

First take \(d=2m\). On the \(j\)-th coordinate pair choose Lerner's weight
\(w_{\theta_j}\), and define
\[
W_{\boldsymbol\theta}(x_1,\ldots,x_{2m})
=
\prod_{j=1}^m
w_{\theta_j}(x_{2j-1},x_{2j}).
\]
Repeated application of the product lemma gives
\[
[W_{\boldsymbol\theta}]_{A_2^{\mathrm{str}}}
=
\prod_{j=1}^m [w_{\theta_j}]_{A_2^{\mathrm{str}}}
\asymp_m \prod_{j=1}^m\theta_j^{-1},
\]
and, using tensor products of the test functions in Lerner's theorem,
\[
\|M_{2m}^{\mathrm{str}}\|_{L^2(W_{\boldsymbol\theta})\to
L^2(W_{\boldsymbol\theta})}
\gtrsim_m
\prod_{j=1}^m
\left(\theta_j^{-1}\sqrt{\log\frac1{\theta_j}}\right).
\]

Now take all \(\theta_j=\theta\). If
\[
A_\theta=[W_\theta]_{A_2^{\mathrm{str}}},
\]
then
\[
A_\theta\asymp_m\theta^{-m}
\]
and
\[
\|M_{2m}^{\mathrm{str}}\|
\gtrsim_m
\theta^{-m}\bigl(\log(1/\theta)\bigr)^{m/2}.
\]
For sufficiently small \(\theta\), the two-sided comparison
\(A_\theta\asymp_m\theta^{-m}\) implies both
\(\theta^{-m}\gtrsim_m A_\theta\) and
\[
\log(1/\theta)\gtrsim_m \log A_\theta.
\]
Hence
\[
\|M_{2m}^{\mathrm{str}}\|
\gtrsim_m
A_\theta(\log A_\theta)^{m/2}.
\]

For \(d=2m+1\), use the same weight, independent of the last coordinate.
Its rectangular \(A_2\) characteristic is unchanged. Tensor the previous
test function with any nonzero compactly supported \(h\in L^2(\mathbb R)\).
Since the one-dimensional maximal function satisfies \(M_1h\ge |h|\)
almost everywhere, the additional coordinate cannot decrease the norm
ratio. This gives the same lower bound in dimension \(2m+1\).

The stated necessity of
\(\gamma\ge m/2\) follows by comparing the lower family with any proposed
linear-times-logarithmic upper bound and sending \(A\to\infty\).

## Relation to current upper bounds

Ombrosi and Rey, *Improved weighted bounds for the strong maximal function*,
arXiv:2609.17246, prove new power-type upper bounds in every dimension.
Their argument also groups coordinates in pairs, but it is an upper-bound
mechanism and does not state the tensor-amplified logarithmic lower bound
above.

The present result does **not** improve the known lower bound on the
infimum of admissible pure power exponents: logarithmic factors do not force
a power strictly larger than \(1\). Its content is instead a
dimension-dependent obstruction inside the linear-power scale.

## Originality scope and limitations

The two-dimensional lower bound is Lerner's theorem and is not claimed as
new. The factorization identities for product weights and tensor-product
functions are elementary. The claimed contribution is their use to amplify
the recent two-dimensional obstruction into the explicit all-dimensional
lower family
\[
A(\log A)^{\lfloor d/2\rfloor/2}
\]
and the corresponding necessary logarithmic exponent for any near-linear
weighted estimate.

To the best of our knowledge, searches for higher-dimensional, tensorized,
and logarithmic versions of the September 2026 strong-maximal \(A_2\)
counterexample did not locate this statement. The source papers are very
recent, so contemporaneous or not-yet-indexed observations remain the main
originality risk.

No claim is made that the logarithmic exponent above is sharp, nor that an
upper bound of linear power times a logarithm exists. The gap to the current
power-type upper bounds remains large.

## Sources

- A. K. Lerner, *Failure of the linear \(A_2\) bound for the strong maximal
  operator*, arXiv:2609.14008, https://arxiv.org/abs/2609.14008
- S. Ombrosi and G. Rey, *Improved weighted bounds for the strong maximal
  function*, arXiv:2609.17246, https://arxiv.org/abs/2609.17246
