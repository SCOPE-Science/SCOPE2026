# Exact von Neumann--Jordan constant of the cubic two-dimensional Cesàro space
## Finding
Let \(X=\mathrm{ces}_3^{(2)}\) be \(\mathbb R^2\) with
\[
\|(x,y)\|_X=
\left(
|x|^3+\left(\frac{|x|+|y|}{2}\right)^3
\right)^{1/3}.
\]
Let \(\tau>0\) be the unique solution of
\[
3^{4/3}(1+\tau)^2
=
\tau\bigl((1+\tau)^2+8\bigr).
\]
Then the classical von Neumann--Jordan constant is
\[
C_{\mathrm{NJ}}(X)
=
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}
{3^{4/3}+\tau^2}
=
1.29958204360103898476109693949\ldots .
\]
An extremizing pair is
\[
x=(1,0),\qquad y=(0,\tau).
\]

Numerically,
\[
\tau
=
2.76673988007870113906853704996\ldots .
\]

## Assumptions and scope
The scalar field is real and the dimension is exactly two. The norm is the canonical two-dimensional section of the classical Cesàro sequence space at exponent \(3\).

The classical von Neumann--Jordan constant is
\[
C_{\mathrm{NJ}}(X)
=
\sup_{(u,v)\ne(0,0)}
\frac{\|u+v\|_X^2+\|u-v\|_X^2}
{2(\|u\|_X^2+\|v\|_X^2)}.
\]
The theorem determines this invariant only for \(\mathrm{ces}_3^{(2)}\). It does not assert a formula for all exponents \(p>2\) or for higher-dimensional Cesàro spaces.

## Proof
Put
\[
r_0=3^{-4/3}
\]
and define the Hilbert norm
\[
H(x,y)^2=x^2+r_0y^2.
\]
Because the Cesàro norm is absolute and homogeneous, every nonzero direction with first coordinate nonzero can be represented by \((1,t)\), where
\[
t=\frac{|y|}{|x|}\in[0,\infty).
\]
Define
\[
F(t)
=
\frac{\|(1,t)\|_X^2}{H(1,t)^2}
=
\frac{\bigl(8+(1+t)^3\bigr)^{2/3}}
{4(1+r_0t^2)}.
\]
The endpoint values agree:
\[
F(0)
=
\frac{3^{4/3}}4,
\qquad
\lim_{t\to\infty}F(t)
=
\frac{3^{4/3}}4.
\]

For \(t>0\),
\[
\frac12\frac{d}{dt}\log F(t)
=
\frac{(1+t)^2}{8+(1+t)^3}
-
\frac{r_0t}{1+r_0t^2}.
\]
Thus an interior critical point satisfies
\[
r_0
=
R(t)
:=
\frac{(1+t)^2}
{t\bigl((1+t)^2+8\bigr)}.
\]
A direct differentiation gives
\[
R'(t)
=
-\frac{(t+1)(t^3+3t^2-5t+9)}
{t^2(t^2+2t+9)^2}.
\]
The cubic factor is strictly positive for \(t>0\), because
\[
t^3+3t^2-5t+9
=
t(t-1)^2
+
5\left(t-\frac35\right)^2
+
\frac{36}{5}.
\]
Hence \(R\) decreases strictly from \(+\infty\) to \(0\). There is a unique critical point \(\tau>0\), characterized by
\[
3^{4/3}(1+\tau)^2
=
\tau\bigl((1+\tau)^2+8\bigr).
\]
Moreover, \(F\) increases on \((0,\tau)\) and decreases on \((\tau,\infty)\). Therefore
\[
m:=\inf F=\frac{3^{4/3}}4,
\qquad
M:=\sup F=F(\tau),
\]
and for every \(w\in\mathbb R^2\),
\[
mH(w)^2
\le
\|w\|_X^2
\le
MH(w)^2.
\]

For arbitrary \(u,v\in X\), the parallelogram identity for \(H\) gives
\[
\begin{aligned}
\|u+v\|_X^2+\|u-v\|_X^2
&\le
M\left(H(u+v)^2+H(u-v)^2\right)\\
&=
2M\left(H(u)^2+H(v)^2\right)\\
&\le
2\frac{M}{m}
\left(\|u\|_X^2+\|v\|_X^2\right).
\end{aligned}
\]
Thus
\[
C_{\mathrm{NJ}}(X)\le\frac{M}{m}.
\]

Now choose
\[
u=(1,0),
\qquad
v=(0,\tau).
\]
By absoluteness,
\[
\|u+v\|_X=\|u-v\|_X=\|(1,\tau)\|_X.
\]
Also
\[
\|u\|_X^2=\frac{3^{4/3}}4,
\qquad
\|v\|_X^2=\frac{\tau^2}{4},
\]
while
\[
\|(1,\tau)\|_X^2
=
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}4.
\]
Therefore the von Neumann--Jordan ratio of this pair is
\[
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}
{3^{4/3}+\tau^2}
=
\frac{M}{m}.
\]
The upper and lower bounds coincide.

## Verification
The directional optimization is exhaustive: absolute homogeneity reduces all nonzero directions to \(t\in[0,\infty]\), including the second coordinate axis as the endpoint \(t=\infty\). The critical equation has exactly one positive solution because \(R'(t)<0\) on \((0,\infty)\), so there are no unexamined local extrema.

The numerical values
\[
\tau
=
2.76673988007870113906853704996\ldots
\]
and
\[
C_{\mathrm{NJ}}(X)
=
1.29958204360103898476109693949\ldots
\]
are consistency checks only. The theorem is proved symbolically.

## Relationship to prior work
Maligranda, Petrot, and Suantai studied the James constant and convexity of Cesàro and Cesàro--Orlicz sequence spaces and supplied the archival two-dimensional Cesàro setting.

Saejung later gave a short calculation of the James and von Neumann--Jordan constants of the two-dimensional Cesàro space in the range \(1<p\le2\). The full text states this exponent restriction explicitly, so the cubic exponent \(p=3\) is not covered by that theorem.

Nikolova and Varošanec subsequently treated geometric constants of absolute normalized norms and revisited Cesàro examples. In their Cesàro discussion, the quadratic case is explicit and the case \(p\ne2\) is identified as remaining unsolved for the relevant von Neumann--Jordan calculation. The present theorem supplies the first cubic exact value.

## Limitations
The result is restricted to the real two-dimensional cubic Cesàro norm. It does not classify \(C_{\mathrm{NJ}}(\mathrm{ces}_p^{(2)})\) for arbitrary \(p>2\).

The literature comparison cannot exclude a later equivalent computation under different notation. No such statement was located in the checked exact-formula searches or in the inspected primary sources.

## References
1. L. Maligranda, N. Petrot, and S. Suantai, “On the James constant and B-convexity of Cesàro and Cesàro--Orlicz sequence spaces,” *Journal of Mathematical Analysis and Applications* 326 (2007), 312--331, DOI 10.1016/j.jmaa.2006.02.085; available online 2006-04-17.
2. S. Saejung, “Another look at Cesàro sequence spaces,” *Journal of Mathematical Analysis and Applications* 366 (2010), 530--537, DOI 10.1016/j.jmaa.2010.01.029; available online 2010-01-25.
3. L. Nikolova and S. Varošanec, “Geometric constants for Banach spaces with absolute normalized norms which corresponding functions are comparable,” *Journal of Nonlinear and Convex Analysis* 14 (2013), 529--549.
