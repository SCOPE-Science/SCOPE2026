# Uniform-sample variance separates exactly into range and normalized shape

## Finding

Let
\[
X_1,\ldots,X_n,
\qquad
n\ge2,
\]
be independent and identically distributed uniformly on
\[
[a,b],
\qquad
w=b-a>0.
\]
Write
\[
R=X_{(n)}-X_{(1)}
\]
for the sample range and
\[
S^2
=
\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\]
for the unbiased sample variance.

Since a continuous sample has \(R>0\) almost surely, define
\[
Q=\frac{S^2}{R^2}.
\]

Then
\[
\boxed{
Q\ \text{is independent of}\ (X_{(1)},X_{(n)}).
}
\tag{1}
\]
In particular, \(Q\) is independent of \(R\).

Its mean is
\[
\boxed{
\mathbb EQ
=
\frac{(n+1)(n+2)}{12n(n-1)}.
}
\tag{2}
\]

Therefore the conditional regression of sample variance on range is exactly quadratic:
\[
\boxed{
\mathbb E[S^2\mid R]
=
\frac{(n+1)(n+2)}{12n(n-1)}R^2
\quad\text{a.s.}
}
\tag{3}
\]

More generally, for every real
\[
q>0,
\]
the covariance is
\[
\boxed{
\operatorname{Cov}(R^q,S^2)
=
w^{q+2}
\frac{
q(2n^2+2nq+2n+q-1)
}{
6(n+q-1)(n+q)(n+q+1)(n+q+2)
}
>0.
}
\tag{4}
\]

The ordinary range-variance covariance is the particularly simple case
\[
\boxed{
\operatorname{Cov}(R,S^2)
=
\frac{w^3}{3(n+1)(n+3)}.
}
\tag{5}
\]

Thus, under a continuous uniform parent law, all dependence of the sample variance on the extrema factors through the squared range. After dividing by \(R^2\), the remaining shape statistic is exactly independent of both sample endpoints.

## Assumptions and scope

The observations are iid from a nondegenerate continuous uniform law on a finite interval.

The sample variance uses divisor \(n-1\).

The independence statement in (1) is stronger than uncorrelatedness. It concerns the normalized statistic \(S^2/R^2\), not \(S^2\) itself.

Equation (4) is stated only for \(q>0\), where the covariance sign is strictly positive. The range moment formula used in the proof actually exists on the wider domain \(q>-(n-1)\), but no sign claim outside \(q>0\) is made here.

## Proof

By positive affine transformation it is enough to prove the structural statement for a sample from the uniform law on \([0,1]\). Write the ordered sample as
\[
0<U_{(1)}<\cdots<U_{(n)}<1.
\]

Introduce
\[
u=U_{(1)},
\qquad
r=U_{(n)}-U_{(1)},
\]
and normalized interior coordinates
\[
z_i
=
\frac{U_{(i)}-U_{(1)}}{R},
\qquad
2\le i\le n-1.
\]
The ordered-sample density is the constant \(n!\) on the simplex. The transformation
\[
(U_{(1)},\ldots,U_{(n)})
\longmapsto
(u,r,z_2,\ldots,z_{n-1})
\]
has Jacobian
\[
r^{n-2}.
\]
Hence the transformed joint density is
\[
n!r^{n-2}
\mathbf 1_{\{0<u<1-r\}}
\mathbf 1_{\{0<z_2<\cdots<z_{n-1}<1\}}.
\tag{6}
\]

The right-hand side factors into a function of \((u,r)\) times a function of the normalized shape vector
\[
Z=(z_2,\ldots,z_{n-1}).
\]
Therefore \(Z\) is independent of
\[
(U_{(1)},R),
\]
and hence independent of the equivalent endpoint pair
\[
(U_{(1)},U_{(n)}).
\]

After translating by the minimum and dividing by the range, the sample becomes
\[
0,z_2,\ldots,z_{n-1},1.
\]
Sample variance is translation invariant and homogeneous of degree two, so
\[
Q=\frac{S^2}{R^2}
\]
is a function of \(Z\) alone. This proves (1).

Conditional on the endpoints, the unordered interior normalized observations are iid uniform on \([0,1]\). To compute \(\mathbb EQ\), take
\[
Y_1=0,
\qquad
Y_n=1,
\]
and let
\[
Y_2,\ldots,Y_{n-1}
\]
be iid uniform on \([0,1]\). Then
\[
Q
\stackrel{d}{=}
\frac1{n-1}
\left(
\sum_{i=1}^nY_i^2
-
\frac1n\left(\sum_{i=1}^nY_i\right)^2
\right).
\tag{7}
\]

Now
\[
\mathbb E\sum_iY_i^2
=
1+\frac{n-2}{3}
=
\frac{n+1}{3},
\]
while
\[
\mathbb E\left(\sum_iY_i\right)^2
=
\left(\frac n2\right)^2+\frac{n-2}{12}.
\]
Substitution into (7) gives
\[
\mathbb EQ
=
\frac{(n+1)(n+2)}{12n(n-1)},
\]
proving (2). Independence of \(Q\) and \(R\) then yields (3).

For the uniform law on \([0,1]\), the sample range has the beta density
\[
f_R(r)
=
n(n-1)r^{n-2}(1-r),
\qquad
0<r<1.
\]
Hence, for every real \(t>-(n-1)\),
\[
\mathbb E[R^t]
=
\frac{n(n-1)}{(n+t-1)(n+t)}.
\tag{8}
\]

Since
\[
S^2=QR^2
\]
with \(Q\) independent of \(R\),
\[
\operatorname{Cov}(R^q,S^2)
=
\mathbb EQ
\left(
\mathbb E[R^{q+2}]
-
\mathbb E[R^q]\mathbb E[R^2]
\right).
\tag{9}
\]
Insert (2) and (8). Straight algebra gives
\[
\operatorname{Cov}(R^q,S^2)
=
\frac{
q(2n^2+2nq+2n+q-1)
}{
6(n+q-1)(n+q)(n+q+1)(n+q+2)
}.
\tag{10}
\]
Every factor in (10) is positive for \(n\ge2\) and \(q>0\).

Finally, restoring interval width multiplies \(R^qS^2\) by
\[
w^{q+2},
\]
which proves (4). Setting \(q=1\) simplifies (4) to (5).

## Verification

The accompanying exact-rational checker verifies the algebraic identities for a wide grid of integer \(n\) and positive integer \(q\).

It independently reconstructs the mean of the normalized variance from the endpoint-plus-interior representation, checks the beta range moments, checks the covariance formula from the unsimplified moment expression, and verifies the \(q=1\) simplification.

These finite checks are supplementary. The universal statements are proved analytically by the transformed joint density, exact independence factorization, and beta-moment calculation above.

## Relationship to prior work

Papadatos studies sharp expectation bounds for sample ranges under moment information and reviews the long line of range inequalities for order statistics. That work is about optimizing expected range over classes of distributions and dependence structures; it does not study the same-sample stochastic dependence between the range and sample variance under a uniform parent law.

Cheng, Hu, and Lin study deterministic inequalities connecting sample range and sample standard deviation and explicitly discuss the fact that the two statistics calculated from one sample are generally dependent. They also record the beta law and power moments of the range under the uniform distribution. Their article does not state that \(S^2/R^2\) is independent of the extrema, does not give the conditional regression (3), and does not derive the covariance family (4).

The factorization in (6) is consistent with classical uniform-spacing geometry. The potentially new content is therefore not the existence of normalized uniform spacings, but the explicit consequence for same-sample variance: exact endpoint independence of \(S^2/R^2\), the quadratic regression, and the closed all-power covariance law.

## Limitations

The exact factorization relies on the constant density of the uniform parent law. For a general continuous distribution, normalizing the sample by its own minimum and range does not make the interior shape independent of the endpoints.

The result concerns sample variance rather than sample standard deviation. Taking a square root destroys the linear moment calculation used in (3)--(5).

The normalized-shape factorization is elementary once the correct coordinates are chosen, so older spacing or invariant-statistic literature may contain an equivalent statement under different notation. The principal originality risk is prior recognition of the specific sample-variance consequence.

## References

1. N. Papadatos, “Maximizing the expected range from dependent observations under mean-variance information,” arXiv:1405.6884, first submitted 2014-05-27.
2. T.-L. Cheng, C.-Y. Hu, and G. D. Lin, “On the Sample Range Inequalities,” *Sankhya A* (2026), DOI 10.1007/s13171-026-00457-6.
