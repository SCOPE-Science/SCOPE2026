# Sharp atom-profile refinement of the Gini–variance inequality

## Finding

Let \(X\) be a nondegenerate square-integrable discrete random variable with
distinct ordered atoms
\[
x_1<\cdots<x_m
\]
and positive masses
\[
p_i=\Pr(X=x_i).
\]
Let \(X'\) be an independent copy, and define the Gini mean difference
\[
\Delta=\mathbb E|X-X'|
\]
and variance
\[
\sigma^2=\operatorname{Var}(X).
\]
Put
\[
S_3=\sum_{i=1}^m p_i^3.
\]

Then
\[
\boxed{
\Delta^2\le \frac43(1-S_3)\sigma^2.
}
\tag{1}
\]

This is sharp for every fixed probability profile. Define the mid-distribution
values
\[
q_i=\sum_{j<i}p_j+\frac{p_i}{2}.
\]
Equality in (1) holds if and only if there are constants
\[
a\in\mathbb R,\qquad b>0
\]
such that
\[
x_i=a+bq_i
\qquad(1\le i\le m).
\tag{2}
\]
Equivalently,
\[
x_{i+1}-x_i
=
\frac b2(p_i+p_{i+1}).
\tag{3}
\]
Thus the atom probabilities determine, up to location and scale, the unique
support geometry maximizing standardized Gini dispersion.

If \(X\) has at most \(N\ge2\) atoms, then
\[
\boxed{
\Delta^2
\le
\frac{4(N^2-1)}{3N^2}\sigma^2.
}
\tag{4}
\]
Equality in (4) holds exactly for a uniform law on an \(N\)-point arithmetic
progression.

There is also a direct order-statistic consequence. Suppose the probability
profile is reflection-symmetric,
\[
p_i=p_{m+1-i},
\]
and optimize over reflection-symmetric ordered supports carrying this profile.
For two iid draws \(X_1,X_2\), put
\[
Y=\min(X_1,X_2),
\qquad
Z=\max(X_1,X_2).
\]
Then
\[
\boxed{
\operatorname{Corr}(Y,Z)
\le
\frac{1-S_3}{2+S_3},
}
\tag{5}
\]
and equality is attained exactly by the support (2). For equal masses this
reduces to
\[
\frac{N^2-1}{2N^2+1},
\]
the familiar discrete-uniform min–max constant.

## Assumptions and scope

The main theorem is for a finite discrete distribution with positive masses
on its distinct atoms. The atom locations may be arbitrary real numbers and
need not be equally spaced or nonnegative.

The probability-profile inequality (1) is stronger than a support-cardinality
bound: it retains the complete cubic collision statistic \(S_3\).

The order-statistic corollary (5) assumes reflection symmetry of both the
probability profile and the support. No claim is made here for arbitrary
nonsymmetric probability vectors in the min–max optimization problem.

## Proof

Define the mid-distribution transform
\[
M=F(X)-\frac12\Pr(X=X),
\]
more explicitly,
\[
M=q_i
\quad\text{when }X=x_i.
\]
It is convenient to verify its variance by randomized probability
integral transformation. Let \(U\) be independent uniform on \([0,1]\) and set
\[
V=F(X^-)+U\Pr(X=X).
\]
Conditional on \(X=x_i\), the variable \(V\) is uniform on an interval of
length \(p_i\), and these intervals partition \([0,1]\). Hence
\[
V\sim{\rm Unif}(0,1),
\qquad
\mathbb E(V\mid X)=M,
\]
and
\[
\operatorname{Var}(V\mid X=x_i)=\frac{p_i^2}{12}.
\]
The law of total variance gives
\[
\operatorname{Var}(M)
=
\frac1{12}
-\frac1{12}\sum_i p_i^3
=
\frac{1-S_3}{12}.
\tag{6}
\]

Next let \(X'\) be an independent copy. Conditional on \(X=x_i\),
\[
\mathbb E[\operatorname{sgn}(X-X')\mid X=x_i]
=
2q_i-1.
\]
By exchangeability,
\[
\begin{aligned}
\Delta
&=
\mathbb E[(X-X')\operatorname{sgn}(X-X')]\\
&=
2\mathbb E[X\operatorname{sgn}(X-X')]\\
&=
2\mathbb E[X(2M-1)]\\
&=
4\operatorname{Cov}(X,M),
\end{aligned}
\tag{7}
\]
because \(\mathbb E M=1/2\).

Cauchy--Schwarz, (6), and (7) yield
\[
\Delta^2
=
16\operatorname{Cov}(X,M)^2
\le
16\sigma^2\operatorname{Var}(M)
=
\frac43(1-S_3)\sigma^2,
\]
proving (1).

Equality in Cauchy--Schwarz holds exactly when
\[
X-\mathbb E X=b(M-1/2)
\]
almost surely for some nonzero \(b\). Since the atom ordering agrees with the
ordering of the \(q_i\), necessarily \(b>0\). This is precisely (2), and
subtracting adjacent equations gives (3). Conversely, (2) makes
\(X\) affine in \(M\), so equality is attained.

Now suppose there are \(m\le N\) atoms. Convexity gives
\[
S_3=\sum_{i=1}^m p_i^3
\ge
m\left(\frac1m\right)^3
=
\frac1{m^2}
\ge
\frac1{N^2}.
\tag{8}
\]
Combining (1) with (8) gives (4). Equality in (8) requires
\[
m=N,\qquad p_i=\frac1N.
\]
Under equal masses, (3) requires constant adjacent spacings. Thus equality in
(4) is exactly the uniform law on an \(N\)-point arithmetic progression.

For the order-statistic consequence, let
\[
G=\Delta.
\]
Since
\[
YZ=X_1X_2,
\qquad
Y+Z=X_1+X_2,
\]
one obtains
\[
\operatorname{Cov}(Y,Z)=\frac{G^2}{4}.
\tag{9}
\]
Under reflection symmetry, \(Y\) and \(Z\) have the same variance. Using
\[
\operatorname{Var}(Y+Z)=2\sigma^2
\]
together with (9) gives
\[
\operatorname{Var}(Y)=\operatorname{Var}(Z)
=
\sigma^2-\frac{G^2}{4}.
\]
Therefore
\[
\operatorname{Corr}(Y,Z)
=
\frac{G^2}{4\sigma^2-G^2}.
\tag{10}
\]
The right side is increasing in \(G^2/\sigma^2\). Substituting (1) into
(10) gives (5).

If the probability profile is symmetric, then
\[
q_{m+1-i}=1-q_i.
\]
Consequently the equality support \(x_i=a+bq_i\) is itself reflection
symmetric. Hence the upper bound (5) is attained and is sharp.

## Verification

The accompanying exact-rational checker verifies (6)--(8) for thousands of
random rational discrete laws. It constructs the equality support from the
mid-distribution values and checks exact equality in (1).

It also tests the support-cardinality bound, its uniform arithmetic-progression
equality case, and the reflection-symmetric min–max corollary by direct
enumeration of the two-sample order-statistic law.

The computation is supplementary. The theorem for arbitrary positive masses
and real support locations follows from the analytic argument above.

## Relationship to prior work

Čiginas and Pumputis compare Gini mean difference and variance for finite
populations and give exact gap-coordinate formulas for both scale measures.
Their 2014 preprint treats sampling and estimation questions; it does not
state the fixed-probability-profile sharp inequality (1), its cubic atom
correction, or the equality geometry (2)--(3).

La Haye and Zizler give a short Cauchy--Schwarz proof of the classical sharp
inequality
\[
\Delta\le \frac{2}{\sqrt3}\sigma
\]
and characterize the continuous uniform equality case. Their full 2019 paper
also discusses finite point masses in its Lorenz framework, but the displayed
variance--Gini inequality retains the continuous constant. It does not
subtract the exact atom term \(S_3\), optimize over support geometry for a
fixed mass profile, or give (2)--(4).

The identity
\[
\operatorname{Var}(F_{\rm mid}(X))
=
\frac{1-\sum_i p_i^3}{12}
\]
belongs to the established mid-distribution literature. The contribution
here is to combine that discrete tie correction with the Gini covariance
identity and carry the equality conditions through to an exact support
optimization.

Papadatos proved that, for equal probabilities on \(N\) prescribed support
points, the two-sample min--max correlation is at most
\[
\frac{N^2-1}{2N^2+1},
\]
with equality exactly on an arithmetic progression. That theorem is broader
than (5) in support asymmetry when the weights are equal. The new
order-statistic consequence here instead allows arbitrary reflection-symmetric
probability profiles and gives the profile-specific constant
\[
\frac{1-S_3}{2+S_3}.
\]

Targeted searches using Gini mean difference, mid-distribution, atom
probabilities, finite support, variance, and arithmetic-progression equality
did not locate (1)--(3) as a sharp fixed-profile theorem.

## Limitations

The atom correction is for finite discrete laws. Extending it to mixed
discrete--continuous distributions would require separating the continuous
and atomic parts of the randomized probability transform.

The min--max corollary is restricted to reflection-symmetric profiles and
supports. Papadatos's equal-weight theorem does not need this restriction.

The originality assessment is targeted. Older L-moment, midrank, or
inequality literature could contain an equivalent atom-profile inequality
under different terminology.

## References

1. A. Čiginas and D. Pumputis, “Gini's mean difference and variance as
   measures of finite populations scales,” arXiv:1406.2275, first submitted
   2014-06-09.
2. R. La Haye and P. Zizler, “The Gini mean difference and variance,”
   *METRON* 77 (2019), 43--52, DOI 10.1007/s40300-019-00149-2.
3. E. Parzen, “Quantile Probability and Statistical Data Modeling,”
   *Statistical Science* 19 (2004), 652--662, DOI
   10.1214/088342304000000387.
4. N. Papadatos, “A discrete analogue of Terrell's characterization of
   rectangular distributions,” arXiv:2205.14360, first submitted 2022-05-28.
