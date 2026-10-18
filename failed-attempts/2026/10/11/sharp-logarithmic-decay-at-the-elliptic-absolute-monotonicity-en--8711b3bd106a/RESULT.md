# Sharp logarithmic decay at the elliptic absolute-monotonicity endpoint

## Finding

Let
\[
f(x)=\frac{\mathcal K(\sqrt{x})}{\log 4-\log\sqrt{1-x}},
\qquad
\frac{2}{\pi}f(x)=\sum_{n=0}^{\infty}a_n x^n.
\]
The recent endpoint absolute-monotonicity theorem proves
\[
a_n<0
\qquad
(n\ge3).
\]
The size of these coefficients is asymptotically exact:
\[
-a_n
\sim
\frac{1}{\pi n^2(\log n)^2}
\qquad
(n\to\infty).
\]
Equivalently,
\[
\lim_{n\to\infty}
\pi n^2\log^2(16n)(-a_n)
=1.
\]

The same law determines the singular growth of the absolutely monotone function singled out in the source theorem:
\[
-f'''(x)
\sim
\frac{1}{2(1-x)^2\log^2\!\bigl(16/(1-x)\bigr)}
\qquad
(x\uparrow1).
\]

Thus the endpoint theorem has a quantitative form: the negative Taylor coefficients decay at the borderline rate
\[
n^{-2}(\log n)^{-2},
\]
while the third derivative diverges at the reciprocal regularly varying rate.

## Assumptions and scope

The complete elliptic integral is
\[
\mathcal K(k)
=
\int_0^{\pi/2}
\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}}.
\]
The function \(f\) is the parameter value \(p=\log4\) in arXiv:2609.32366v1. The coefficients \(a_n\) use exactly the source normalization
\[
\frac{2}{\pi}f(x)=\sum_{n\ge0}a_nx^n.
\]

The coefficient asymptotic concerns \(n\to\infty\). The derivative asymptotic concerns the radial endpoint \(x\uparrow1\) inside \((0,1)\).

The factor \(16\) inside the logarithm is the natural one coming from
\[
\log4-\frac12\log(1-x)
=
\frac12\log\frac{16}{1-x}.
\]
At leading order it is equivalent to using \(\log n\), but retaining it keeps the formula aligned with the elliptic endpoint normalization.

## Proof

The source analytically continues the normalized function and obtains
\[
a_n
=
\frac{(-1)^nC}{15^{n+1}}-M_n,
\qquad
C>0,
\]
where
\[
M_n
=
\int_1^{\infty}\rho(t)t^{-n-1}\,dt
\]
for a positive density \(\rho\).

For \(t>1\), set
\[
r=t^{-1/2},
\qquad
r'=\sqrt{1-r^2},
\qquad
c=\log\frac{4r}{r'}.
\]
The boundary-value calculation gives
\[
\rho(t)
=
\frac{2r}{\pi^2}
\frac{(\pi/2)\mathcal K(r)-c\mathcal K(r')}
{c^2+\pi^2/4}.
\]

Write
\[
t=1+u.
\]
Then
\[
r=\frac1{\sqrt{1+u}},
\qquad
r'^2=\frac{u}{1+u},
\]
and, importantly,
\[
c
=
\log\frac{4r}{r'}
=
\frac12\log\frac{16}{u}.
\]

Let
\[
L=\log\frac4{r'}.
\]
The standard complete-elliptic expansions at complementary modulus zero are
\[
\mathcal K(r)
=
L+\frac{r'^2}{4}(L-1)+O(r'^4L)
\]
and
\[
\mathcal K(r')
=
\frac\pi2
\left(
1+\frac{r'^2}{4}+O(r'^4)
\right).
\]
Since
\[
L
=
c+\frac12\log(1+u)
=
c+\frac u2+O(u^2)
\]
and
\[
r'^2=u+O(u^2),
\]
we obtain
\[
\mathcal K(r)
=
c+u\left(\frac c4+\frac14\right)+O(u^2c)
\]
and
\[
c\mathcal K(r')
=
\frac{\pi c}{2}
+
\frac{\pi cu}{8}
+O(u^2c).
\]
Therefore
\[
\frac\pi2\mathcal K(r)-c\mathcal K(r')
=
\frac{\pi}{8}u+O(u^2c).
\]
Because
\[
c\to\infty,
\qquad
r\to1,
\]
it follows that
\[
\rho(1+u)
\sim
\frac{u}{\pi\log^2(16/u)}.
\]

It remains to convert this boundary density into coefficient asymptotics. Put
\[
L_n=\log(16n).
\]
For a fixed sufficiently small \(\delta>0\), the part of \(M_n\) with
\[
u\ge\delta
\]
is exponentially small. On
\[
0<u<\delta,
\]
the density ratio above is arbitrarily close to one. Thus it is enough to analyze
\[
I_n
=
\int_0^{\delta}
\frac{u(1+u)^{-n-1}}{\log^2(16/u)}\,du.
\]
With
\[
u=v/n,
\]
\[
n^2L_n^2 I_n
=
\int_0^{n\delta}
v
\left(1+\frac vn\right)^{-n-1}
\left(
\frac{L_n}{L_n-\log v}
\right)^2
\,dv.
\]
For each fixed \(v>0\), the integrand tends to
\[
ve^{-v}.
\]
On
\[
0<v\le\sqrt n,
\]
the logarithmic ratio is uniformly bounded and the kernel is dominated by an exponentially decaying function. On
\[
\sqrt n<v<n\delta,
\]
the kernel is exponentially small in \(\sqrt n\), while the logarithmic ratio grows at most polynomially in \(\log n\). Hence dominated convergence after this two-region split gives
\[
n^2L_n^2 I_n
\longrightarrow
\int_0^{\infty}ve^{-v}\,dv
=1.
\]
Therefore
\[
M_n
\sim
\frac{1}{\pi n^2\log^2(16n)}.
\]

The pole term satisfies
\[
15^{-n}
=o\!\left(n^{-2}(\log n)^{-2}\right),
\]
so
\[
-a_n
\sim
M_n
\sim
\frac{1}{\pi n^2\log^2(16n)}.
\]
This proves the coefficient law.

Finally, the source normalization gives
\[
-f'''(x)
=
\frac\pi2
\sum_{n\ge3}
(-a_n)n(n-1)(n-2)x^{n-3}.
\]
The positive coefficients on the right satisfy
\[
\frac\pi2(-a_n)n(n-1)(n-2)
\sim
\frac{n}{2\log^2(16n)}.
\]
The Abelian theorem for a regularly varying power series with index one therefore yields
\[
-f'''(x)
\sim
\frac{1}{2(1-x)^2\log^2\!\bigl(16/(1-x)\bigr)}.
\]

## Verification

The recent primary source was checked at the endpoint theorem, its analytic continuation across the cut, the pole at \(-15\), the positive moment representation for \(a_n\), and the boundary density used above. The source proves coefficient signs and strict log-convexity, but it does not state a large-\(n\) equivalent for \(a_n\).

The two elliptic-integral expansions used in the proof are standard and agree with NIST DLMF Sections 19.12 and 19.5. In particular, DLMF 19.12.1 gives the convergent logarithmic expansion of \(\mathcal K(k)\) near \(k=1\), and DLMF 19.5.1 gives its Maclaurin expansion near zero.

As an independent algebraic check, the normalized series can be reconstructed from
\[
\frac{2}{\pi}\mathcal K(\sqrt{x})
=
\sum_{n\ge0}
\left(
\frac{(1/2)_n}{n!}
\right)^2x^n
\]
and
\[
\log4-\frac12\log(1-x)
=
\log4+
\frac12\sum_{n\ge1}\frac{x^n}{n}.
\]
Formal power-series division reproduces the source coefficients and their negative sign for the tail. This finite calculation is only a sanity check; the infinite asymptotic follows from the branch-density analysis above.

## Relationship to prior work

Tian and Yang introduced the same quotient family and studied absolute monotonicity by coefficient recurrences. Their 2022 paper supplied the conjectural endpoint problem later solved by the recent source, but the accessible primary material inspected here does not state the coefficient asymptotic above.

The 2026 source proves the decisive new sign representation
\[
a_n
=
(-1)^nC15^{-n-1}-M_n
\]
with \(M_n\) a positive moment sequence. The present result identifies the precise boundary layer of that moment measure and converts it into the sharp coefficient decay.

A separate 2024 preprint on absolutely monotonic functions related to an asymptotic formula for \(\mathcal K\) studies the different family
\[
e^{\mathcal K(\sqrt{x})}-p(1-x)^{-1/2}.
\]
Its coefficient problem and endpoint singularity are not the quotient considered here.

Targeted searches for the quotient, the endpoint parameter \(\log4\), coefficient asymptotics, the rate \(n^{-2}(\log n)^{-2}\), and third-derivative endpoint growth did not locate an implication-equivalent statement.

## Limitations

The result concerns the \(a_n\) sequence for the endpoint quotient \(f_{\log4}\). No asymptotic is asserted here for the reciprocal coefficients \(b_n\).

Only the leading regularly varying term is claimed. Although the normalization \(\log(16n)\) is natural, fixed multiplicative changes inside the logarithm do not alter the leading equivalent.

The full 2022 publisher article was not available through the inspected full-text route; its abstract and publisher preview were checked. A differently worded coefficient asymptotic in inaccessible older material therefore remains a residual originality risk.

## References

1. Q. Deng, Y. Kou, and F. Zhong, *Endpoint Absolute Monotonicity for the Complete Elliptic Integral of the First Kind*, arXiv:2609.32366v1, 2026.
2. J.-F. Tian and Z.-H. Yang, *Several Absolutely Monotonic Functions Related to the Complete Elliptic Integral of the First Kind*, Results in Mathematics 77 (2022), 109, DOI: 10.1007/s00025-022-01641-4.
3. T. Zhao and Z.-H. Yang, *Absolutely monotonic functions related to the asymptotic formula for the complete elliptic integral of the first kind*, arXiv:2405.19651, 2024.
4. NIST Digital Library of Mathematical Functions, Chapter 19, Sections 19.5 and 19.12.
