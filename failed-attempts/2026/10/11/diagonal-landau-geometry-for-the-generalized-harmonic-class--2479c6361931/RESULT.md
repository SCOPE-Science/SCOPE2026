# Diagonal Landau geometry for the generalized harmonic class

## Finding

For every
\[
\gamma>0,
\]
the diagonal parameter class
\[
\mathcal{BH}^{0}(\gamma,\gamma)
\]
is independent of the value of \(\gamma\). Indeed, its defining differential inequality reduces exactly to
\[
\operatorname{Re}\!\left(
\frac{h(z)}{z}+h'(z)
\right)
>
\left|
\frac{g(z)}{z}+g'(z)
\right|,
\qquad z\in\mathbb D.
\]
Denote this common class by
\[
\mathcal D.
\]

Let
\[
f=h+\overline g\in\mathcal D
\]
satisfy
\[
f(0)=0,
\qquad
J_f(0)=1,
\qquad
|f(z)|<M
\quad(z\in\mathbb D).
\]
Define
\[
a=\frac{\pi}{4M}
\]
and
\[
S(r)
=
4\sum_{n=2}^{\infty}
\frac{n}{n+1}r^{n-1}.
\]
Then
\[
S(r)
=
4\left(
\frac{r}{1-r}
+\frac1r
+\frac12
+\frac{\log(1-r)}{r^2}
\right),
\qquad
0<r<1.
\]
The function \(S\) is strictly increasing, satisfies
\[
S(0+)=0,
\]
and tends to infinity as
\[
r\uparrow1.
\]
Hence there is a unique
\[
\rho_M\in(0,1)
\]
such that
\[
S(\rho_M)=a.
\]

Every such \(f\) is univalent on
\[
\mathbb D_{\rho_M},
\]
and its image contains the Euclidean disk centered at the origin with radius
\[
R_M
=
a\rho_M
+
\frac{4\log(1-\rho_M)}{\rho_M}
+
4+2\rho_M.
\]
Equivalently,
\[
R_M
=
\int_0^{\rho_M}(a-S(t))\,dt,
\]
so
\[
R_M>0.
\]

As
\[
M\to\infty,
\]
the two radii have the explicit asymptotics
\[
\rho_M
\sim
\frac{3\pi}{32M},
\qquad
R_M
\sim
\frac{3\pi^2}{256M^2}.
\]

The result is a guaranteed diagonal Landau and covering theorem. No optimality assertion is made.

## Assumptions and scope

The unit disk is
\[
\mathbb D=\{z\in\mathbb C:|z|<1\}.
\]
The harmonic maps use the normalization
\[
h(z)=z+\sum_{n=2}^{\infty}a_nz^n,
\qquad
g(z)=\sum_{n=2}^{\infty}b_nz^n.
\]

The source class is defined, for
\[
\delta\ge\gamma\ge0,
\]
by
\[
\operatorname{Re}\!\left[
\gamma\frac{h(z)}z
+\delta h'(z)
+\frac{\delta-\gamma}{2}zh''(z)
\right]
>
\left|
\gamma\frac{g(z)}z
+\delta g'(z)
+\frac{\delta-\gamma}{2}zg''(z)
\right|.
\]
On the positive diagonal
\[
\delta=\gamma>0,
\]
division by \(\gamma\) gives the parameter-free class \(\mathcal D\).

The source coefficient theorem gives, for
\[
n\ge2,
\]
\[
|a_n|+|b_n|
\le
\frac{4(\delta+\gamma)}
{(n+1)[n(\delta-\gamma)+2\gamma]}.
\]
On the diagonal this becomes
\[
|a_n|+|b_n|
\le
\frac4{n+1}.
\]

The boundedness assumption
\[
|f|<M
\]
is retained because the Landau estimate below uses the standard bounded-harmonic Schwarz estimate at the origin. The theorem does not claim that \(\rho_M\) is the largest possible univalence radius for \(\mathcal D\), nor that \(R_M\) is the optimal covering constant.

## Proof

For
\[
\delta=\gamma>0,
\]
the class-defining inequality is
\[
\gamma
\operatorname{Re}\!\left(
\frac{h(z)}z+h'(z)
\right)
>
\gamma
\left|
\frac{g(z)}z+g'(z)
\right|.
\]
Cancelling the positive factor \(\gamma\) proves the class identity.

Now let
\[
f\in\mathcal D
\]
satisfy the boundedness and Jacobian hypotheses. Write
\[
\lambda_f(0)
=
\bigl||h'(0)|-|g'(0)|\bigr|,
\qquad
\Lambda_f(0)
=
|h'(0)|+|g'(0)|.
\]
Since
\[
J_f(0)=\lambda_f(0)\Lambda_f(0)=1,
\]
and the bounded harmonic Schwarz estimate gives
\[
\Lambda_f(0)\le\frac{4M}{\pi},
\]
we obtain
\[
\lambda_f(0)\ge\frac{\pi}{4M}=a.
\]

Take two distinct points
\[
z_1,z_2\in\mathbb D_r.
\]
Integrating along the line segment joining them and separating the linear part gives
\[
|f(z_1)-f(z_2)|
\ge
|z_1-z_2|
\left[
\lambda_f(0)
-
\sum_{n=2}^{\infty}
n(|a_n|+|b_n|)r^{n-1}
\right].
\]
Using the diagonal coefficient bound yields
\[
|f(z_1)-f(z_2)|
\ge
|z_1-z_2|\,[a-S(r)],
\]
where
\[
S(r)
=
4\sum_{n=2}^{\infty}\frac{n}{n+1}r^{n-1}.
\]

Because every coefficient in this series is positive,
\[
S
\]
is strictly increasing on
\[
(0,1).
\]
Also
\[
S(0+)=0
\]
and
\[
S(r)\to\infty
\]
as
\[
r\uparrow1.
\]
Therefore there is a unique
\[
\rho_M
\]
with
\[
S(\rho_M)=a.
\]
For any two points in
\[
\mathbb D_{\rho_M},
\]
their joining segment is contained in some
\[
\mathbb D_r
\]
with
\[
r<\rho_M,
\]
so
\[
a-S(r)>0.
\]
Hence \(f\) is injective on
\[
\mathbb D_{\rho_M}.
\]

To sum \(S\), use
\[
\frac{n}{n+1}=1-\frac1{n+1}.
\]
The elementary geometric and logarithmic series give
\[
S(r)
=
4\left(
\frac{r}{1-r}
+\frac1r
+\frac12
+\frac{\log(1-r)}{r^2}
\right).
\]

For the covering radius, on
\[
|z|=\rho_M
\]
the coefficient estimate gives
\[
|f(z)|
\ge
a\rho_M
-
4\sum_{n=2}^{\infty}
\frac{\rho_M^n}{n+1}.
\]
Since
\[
4\sum_{n=2}^{\infty}\frac{r^n}{n+1}
=
-\frac{4\log(1-r)}r-4-2r,
\]
we obtain
\[
|f(z)|
\ge
a\rho_M
+
\frac{4\log(1-\rho_M)}{\rho_M}
+
4+2\rho_M
=
R_M.
\]
Injectivity and openness then give
\[
\mathbb D_{R_M}
\subset
f(\mathbb D_{\rho_M}).
\]

If
\[
T(r)=4\sum_{n=2}^{\infty}\frac{r^n}{n+1},
\]
then
\[
T'(r)=S(r).
\]
Since
\[
S(\rho_M)=a,
\]
we have
\[
R_M
=
a\rho_M-T(\rho_M)
=
\int_0^{\rho_M}(a-S(t))\,dt
>0.
\]

Finally,
\[
S(r)
=
\frac83r+3r^2+O(r^3)
\qquad(r\downarrow0).
\]
As
\[
M\to\infty,
\]
we have
\[
a\to0
\]
and therefore
\[
\rho_M
\sim
\frac{3a}{8}
=
\frac{3\pi}{32M}.
\]
Also
\[
T(r)=\frac43r^2+O(r^3).
\]
Substituting
\[
\rho_M\sim\frac{3a}{8}
\]
into
\[
R_M=a\rho_M-T(\rho_M)
\]
gives
\[
R_M
\sim
\frac{3a^2}{16}
=
\frac{3\pi^2}{256M^2}.
\]

## Verification

The class collapse is checked directly from the defining inequality before any coefficient summation.

The coefficient envelope is obtained by substituting
\[
\delta=\gamma>0
\]
into the published bound:
\[
\frac{4(\delta+\gamma)}
{(n+1)[n(\delta-\gamma)+2\gamma]}
=
\frac4{n+1}.
\]

The series identity was checked both coefficientwise and by differentiating
\[
4\sum_{n=2}^{\infty}\frac{r^n}{n+1}
=
-\frac{4\log(1-r)}r-4-2r.
\]
Its Taylor expansion starts
\[
S(r)
=
\frac83r+3r^2+\frac{16}{5}r^3+\frac{10}{3}r^4+\cdots,
\]
which confirms the small-radius coefficient used in the asymptotic inversion.

The proof of univalence uses the exact line-segment estimate and the strict inequality
\[
S(r)<S(\rho_M)
\]
for every
\[
r<\rho_M.
\]
The covering radius is positive by its integral representation, so positivity is not inferred from numerical evaluation.

No finite computation is used to establish the theorem or its asymptotic statements.

## Relationship to prior work

Wang, Han, Hossain, and Ahamed introduced recent Bohr and Landau-type results for
\[
\mathcal{BH}^{0}(\gamma,\delta)
\]
and stated their Landau theorem over the closed parameter range
\[
\delta\ge\gamma\ge0.
\]
Their proof proceeds first through the coefficient series
\[
\sum_{n=2}^{\infty}
\frac{4(\delta+\gamma)n r^{n-1}}
{(n+1)[n(\delta-\gamma)+2\gamma]},
\]
and then rewrites the off-diagonal expression using the Lerch transcendent.

The displayed Lerch representation contains the ratio
\[
\frac{2\gamma}{\delta-\gamma}
\]
and is therefore not the natural representation on the positive diagonal. The present theorem works at the series level before that reparametrization, where the diagonal is regular and collapses to the elementary envelope
\[
4/(n+1).
\]

Yalçın, Bayram, and Oros established the underlying class and its coefficient estimates in 2024. Their diagonal coefficient bound is the input used here, but their paper does not contain the 2026 bounded-harmonic Landau construction or the elementary diagonal radius formula and large-\(M\) asymptotics stated above.

Targeted searches for the diagonal class, equal-parameter Landau radii, the coefficient envelope
\[
4/(n+1),
\]
and equivalent logarithmic formulas did not locate a published result implying this theorem.

## Limitations

The theorem gives a guaranteed radius obtained from the published coefficient envelope and a bounded-harmonic Schwarz estimate. It does not establish optimality.

The case
\[
\gamma=\delta=0
\]
is excluded because the defining inequality degenerates and cannot be divided by the common parameter.

The asymptotic regime is
\[
M\to\infty
\]
with the diagonal class fixed. No claim is made about joint limits in which
\[
\delta-\gamma
\]
also approaches zero from the off-diagonal region.

The literature comparison focused on the defining class, its coefficient theorem, the recent Landau theorem, equal-parameter formulations, and the corresponding logarithmic series. Related results under substantially different harmonic normalizations remain a residual literature risk.

## References

1. X. Wang, X. Han, R. Hossain, and M. B. Ahamed, *Bohr, Bohr-Rogosinski, and Landau-Type Results for a Generalized Class of Harmonic Mappings*, arXiv:2606.02612v1, first posted 25 May 2026.
2. S. Yalçın, H. Bayram, and G. I. Oros, *Some Properties and Graphical Applications of a New Subclass of Harmonic Functions Defined by a Differential Inequality*, Mathematics 12 (2024), 2338, DOI: 10.3390/math12152338.
