# Exact logarithmic repair threshold for the weighted segment multiplier

## Finding

Fix \(1<p<\infty\). For \(\gamma\in\mathbb R\), define
\[
w_\gamma(x)=
\begin{cases}
|x|^{p-1}\bigl(\log(e/|x|)\bigr)^\gamma,&0<|x|<1,\\
1,&|x|\ge1,
\end{cases}
\qquad
w_\gamma(0)=1.
\]
Let \(S\) denote the segment multiplier on the line.

Then
\[
S:L^p(w_\gamma)\longrightarrow L^p(w_\gamma)
\]
is bounded if and only if
\[
\gamma>p-1.
\]
Equivalently,
\[
w_\gamma\in A_{p,1}
\quad\Longleftrightarrow\quad
\gamma>p-1,
\]
where \(A_{p,1}\) is the truncated Muckenhoupt class obtained by testing the usual \(A_p\) expression only on intervals of length at least one.

In the bounded regime, the classical Hilbert transform is still unbounded on \(L^p(w_\gamma)\). Indeed, \(w_\gamma\notin A_p\) for every \(\gamma\). When \(\gamma>p-1\), the failure is quantified on
\[
I_r=(0,r)
\]
by
\[
\left(\frac1r\int_0^r w_\gamma(x)\,dx\right)
\left(\frac1r\int_0^r
w_\gamma(x)^{-1/(p-1)}\,dx\right)^{p-1}
\sim
\frac1p
\left(\frac{p-1}{\gamma-p+1}\right)^{p-1}
\bigl(\log(e/r)\bigr)^{p-1}
\]
as \(r\downarrow0\).

The large-scale characteristic also records the phase transition sharply:
\[
[w_\gamma]_{A_{p,1}}
\asymp_p
(\gamma-p+1)^{-(p-1)}
\]
as \(\gamma\downarrow p-1\).

## Assumptions and scope

The large-scale class \(A_{p,1}\) uses the normalization of the cited source:
\[
[w]_{A_{p,1}}
=
\sup_{|I|\ge1}
\left(\frac1{|I|}\int_Iw\right)
\left(\frac1{|I|}\int_Iw^{-1/(p-1)}\right)^{p-1}.
\]
The source proves that the segment multiplier is bounded on \(L^p(w)\) exactly for \(w\in A_{p,1}\).

The finding concerns the critical local power \(p-1\) with a logarithmic modifier. It does not classify arbitrary slowly varying corrections, and it does not claim an exact operator norm for \(S\).

## Proof

Put
\[
\sigma_\gamma=w_\gamma^{-1/(p-1)}.
\]
For \(0<|x|<1\),
\[
\sigma_\gamma(x)
=
|x|^{-1}
\bigl(\log(e/|x|)\bigr)^{-\gamma/(p-1)}.
\]
Set
\[
q=\frac{\gamma}{p-1}.
\]
By the substitution
\[
u=\log(e/x),
\]
one obtains
\[
\int_0^1\sigma_\gamma(x)\,dx
=
\int_1^\infty u^{-q}\,du.
\]
Therefore
\[
\sigma_\gamma\in L^1((-1,1))
\quad\Longleftrightarrow\quad
q>1
\quad\Longleftrightarrow\quad
\gamma>p-1.
\]

The weight \(w_\gamma\) itself is locally integrable for every real \(\gamma\), since the positive power \(x^{p-1}\) dominates every logarithmic factor at the origin.

Assume first that
\[
\gamma>p-1.
\]
Both
\[
\int_{-1}^1w_\gamma
\quad\text{and}\quad
\int_{-1}^1\sigma_\gamma
\]
are finite. Since \(w_\gamma=\sigma_\gamma=1\) outside \([-1,1]\), every interval \(I\) with \(|I|\ge1\) satisfies
\[
\int_Iw_\gamma
\le
|I|+C_1
\]
and
\[
\int_I\sigma_\gamma
\le
|I|+C_2.
\]
Consequently
\[
[w_\gamma]_{A_{p,1}}<\infty.
\]
By the source's characterization theorem, \(S\) is bounded on \(L^p(w_\gamma)\).

If
\[
\gamma\le p-1,
\]
then every interval of length at least one containing the origin has
\[
\int_I\sigma_\gamma=\infty.
\]
Hence
\[
w_\gamma\notin A_{p,1},
\]
and the same characterization theorem shows that \(S\) is unbounded.

It remains to compare with the classical \(A_p\) condition. Suppose
\[
\gamma>p-1
\]
and let
\[
L_r=\log(e/r).
\]
Standard endpoint integration gives
\[
\int_0^r
x^{p-1}\bigl(\log(e/x)\bigr)^\gamma\,dx
=
\frac1p r^pL_r^\gamma(1+o(1)).
\]
On the reciprocal side, because \(q>1\),
\[
\int_0^r
x^{-1}\bigl(\log(e/x)\bigr)^{-q}\,dx
=
\frac{L_r^{1-q}}{q-1}.
\]
Therefore
\[
\left(\frac1r\int_0^rw_\gamma\right)
\left(\frac1r\int_0^r\sigma_\gamma\right)^{p-1}
\sim
\frac1p
(q-1)^{-(p-1)}
L_r^{p-1}.
\]
Since
\[
q-1=\frac{\gamma-p+1}{p-1},
\]
this is exactly
\[
\frac1p
\left(\frac{p-1}{\gamma-p+1}\right)^{p-1}
L_r^{p-1},
\]
which tends to infinity. Thus \(w_\gamma\notin A_p\), and the classical Hilbert-transform characterization implies that \(H\) is unbounded on \(L^p(w_\gamma)\). For \(\gamma\le p-1\), failure of local integrability of \(\sigma_\gamma\) already excludes \(A_p\).

Finally, let
\[
\varepsilon=\gamma-p+1\downarrow0.
\]
Then
\[
\int_{-1}^1\sigma_\gamma
=
\frac{2(p-1)}{\varepsilon}.
\]
For \(\gamma\) in a fixed right-neighborhood of \(p-1\), the integral of \(w_\gamma\) over \((-1,1)\) remains bounded above and below by positive constants depending only on \(p\). The preceding large-interval estimate gives
\[
[w_\gamma]_{A_{p,1}}
\lesssim_p
\varepsilon^{-(p-1)}.
\]
Testing the single interval
\[
I=(-1/2,1/2)
\]
gives the reverse bound, because its \(\sigma_\gamma\)-integral is comparable to \(\varepsilon^{-1}\) while its \(w_\gamma\)-integral stays bounded below. Hence
\[
[w_\gamma]_{A_{p,1}}
\asymp_p
\varepsilon^{-(p-1)}.
\]

## Verification

The proof uses the exact large-scale Muckenhoupt characterization from the primary source and elementary one-dimensional integrals.

The critical reciprocal integral is
\[
\int_0^1
x^{-1}
\bigl(\log(e/x)\bigr)^{-q}\,dx
=
\int_1^\infty u^{-q}\,du,
\]
so its threshold is exactly \(q=1\).

The classical small-interval obstruction is not inferred from a numerical experiment. The reciprocal integral on \((0,r)\) is exact, and the weighted integral has the elementary asymptotic
\[
\int_0^r
x^{p-1}
\bigl(\log(e/x)\bigr)^\gamma\,dx
\sim
\frac1p r^p
\bigl(\log(e/r)\bigr)^\gamma.
\]
Combining these expressions yields the stated \(A_p\)-product asymptotic.

No finite enumeration, numerical fit, or unproved asymptotic assumption is used.

## Relationship to prior work

Barea-Fernández, Lang, and Soria prove that boundedness of the segment multiplier on \(L^p(w)\) is equivalent to \(w\in A_{p,1}\), where only intervals of length at least one are tested. They also prove that \(A_p\) is strictly contained in \(A_{p,1}\) by constructing a weight with rapidly oscillating behavior concentrated near the origin.

Their Example 3.15 tests the critical pure power
\[
w(x)=x^{p-1}
\]
on \((0,1)\), patched by \(1\) outside, and shows that it fails the truncated condition because the reciprocal behaves like \(1/x\). The present finding asks the natural endpoint question suggested by that example: how much logarithmic damping of the reciprocal is needed to cross into \(A_{p,1}\)? The answer is the exact threshold \(\gamma>p-1\).

The same family never enters classical \(A_p\). Thus it gives a monotone, nonoscillatory separation between boundedness of the segment multiplier and boundedness of the Hilbert transform, complementary to the oscillatory separation constructed in the source.

Targeted searches for the segment multiplier together with power-log weights, the critical exponent \(p-1\), truncated \(A_p\), and logarithmic corrections did not locate a covering statement.

## Limitations

The result treats one canonical power-log family and does not classify all slowly varying modifications of the critical power.

The source's characterization is qualitative, so no sharp dependence of the segment-multiplier operator norm on
\[
[w_\gamma]_{A_{p,1}}
\]
is asserted here.

The exact divergence rate for the classical \(A_p\) expression is proved in the bounded segment-multiplier regime \(\gamma>p-1\); for \(\gamma\le p-1\), failure already occurs because the reciprocal weight is not locally integrable.

## References

1. M. F. Barea-Fernández, J. Lang, and J. Soria, *Characterization of the boundedness of the segment multiplier on weighted Lebesgue spaces*, arXiv:2609.32039v1, 2026.
2. R. A. Hunt, B. Muckenhoupt, and R. L. Wheeden, *Weighted norm inequalities for the conjugate function and Hilbert transform*, Transactions of the American Mathematical Society 176 (1973), 227--251.
