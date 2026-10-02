# An exact area-theorem Hilbert envelope lowers a polylogarithmic reciprocal univalence threshold

## Statement

Let \(\mathcal S\) be the normalized schlicht class in the unit disk \(\mathbb D\), and write
\[
q_f(z):=\frac{z}{f(z)}=1+\sum_{n\ge 1}b_nz^n,\qquad f\in\mathcal S.
\]
For a complex multiplier sequence \(c=(c_n)_{n\ge1}\), define
\[
Q_c(z)=1+\sum_{n\ge1}c_nb_nz^n,
\qquad
F_c(z)=\frac{z}{Q_c(z)}.
\]
Recall the class \(\mathcal U\) of normalized analytic functions \(F\) satisfying
\[
\left|F'(z)\left(\frac{z}{F(z)}\right)^2-1\right|<1
\quad(z\in\mathbb D),
\]
with \(F(z)/z\ne0\). Functions in \(\mathcal U\) are univalent.

### Theorem 1 — reciprocal multiplier criterion

If
\[
2|c_1|+
\left(\sum_{n=2}^{\infty}\frac{|c_n|^2}{n-1}\right)^{1/2}\le1
\tag{A}
\]
and
\[
\sum_{n=2}^{\infty}(n-1)|c_n|^2\le1,
\tag{B}
\]
then \(F_c\in\mathcal U\) for every \(f\in\mathcal S\).

Moreover, the left side of (A) is the exact support function obtained from only the two universal coefficient constraints
\[
|b_1|\le2,
\qquad
\sum_{n=2}^{\infty}(n-1)|b_n|^2\le1.
\tag{C}
\]
Thus (A) is sharp inside the relaxed coefficient body (C): improving the zero-free conclusion by this absolute-value route requires additional schlicht information beyond Bieberbach for \(b_1\) and the area theorem for the tail.

### Corollary 2 — polylogarithmic reciprocal transform

Ali, Obradović and Ponnusamy (2013) considered
\[
\frac{z}{F_\sigma(z)}
=
\frac{z}{f(z)}*\frac{\operatorname{Li}_\sigma(z)}{z},
\qquad
\operatorname{Li}_\sigma(z)=\sum_{m=1}^{\infty}\frac{z^m}{m^\sigma},
\tag{1}
\]
where \(*\) is Hadamard convolution. Equivalently,
\[
\frac{z}{F_\sigma(z)}
=1+\sum_{n\ge1}\frac{b_n}{(n+1)^\sigma}z^n.
\tag{2}
\]
Define
\[
R(\sigma):=
\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+1)^{2\sigma}}
\tag{3}
\]
and let \(\sigma_*\) be the unique solution of
\[
2^{1-\sigma}+\sqrt{R(\sigma)}=1.
\tag{4}
\]
Then
\[
1.413519<\sigma_*<1.413520,
\tag{5}
\]
and for every \(f\in\mathcal S\),
\[
\boxed{\ \sigma\ge\sigma_*\quad\Longrightarrow\quad F_\sigma\in\mathcal U\subset\mathcal S.\ }
\tag{6}
\]
This lowers the universal sufficient bound \(\sigma\ge3/2\) stated in Corollary 1.7 of Ali–Obradović–Ponnusamy. Their paper ends by asking for the smallest \(\sigma\) for which \(F_\sigma\) is always in \(\mathcal U\) or \(\mathcal S\); (6) is a new upper bound for that problem, not a determination of the exact minimum.

## Proof of Theorem 1

For \(f\in\mathcal S\), Bieberbach gives \(|b_1|=|a_2|\le2\), while the area theorem gives
\[
\sum_{n=2}^{\infty}(n-1)|b_n|^2\le1.
\tag{7}
\]
For \(r=|z|<1\), Cauchy–Schwarz gives
\[
\begin{aligned}
|Q_c(z)-1|
&\le 2|c_1|r
 +\sum_{n=2}^{\infty}|c_n||b_n|r^n\\
&\le 2|c_1|r
+\left(\sum_{n=2}^{\infty}(n-1)|b_n|^2\right)^{1/2}
 \left(\sum_{n=2}^{\infty}\frac{|c_n|^2r^{2n}}{n-1}\right)^{1/2}.
\end{aligned}
\tag{8}
\]
Under (A), the right side is strictly below \(1\) for every \(r<1\). Hence \(Q_c\) has no zero in \(\mathbb D\), so \(F_c=z/Q_c\) is normalized and analytic there.

Because \(z/F_c=Q_c\),
\[
F_c'(z)\left(\frac{z}{F_c(z)}\right)^2-1
=Q_c(z)-zQ_c'(z)-1
=-\sum_{n=2}^{\infty}(n-1)c_nb_nz^n.
\tag{9}
\]
A second Cauchy–Schwarz estimate yields
\[
\begin{aligned}
\left|F_c'(z)\left(\frac{z}{F_c(z)}\right)^2-1\right|
&\le
\left(\sum_{n=2}^{\infty}(n-1)|b_n|^2\right)^{1/2}
\left(\sum_{n=2}^{\infty}(n-1)|c_n|^2r^{2n}\right)^{1/2}\\
&<1
\end{aligned}
\tag{10}
\]
by (B), again with strictness for \(r<1\). Thus \(F_c\in\mathcal U\).

For the sharpness assertion inside (C), maximize the absolute-value majorant over the relaxed product body. The \(b_1\) term contributes exactly \(2|c_1|\). The tail is the support function of a weighted Hilbert ball:
\[
\sup_{\sum_{n\ge2}(n-1)|b_n|^2\le1}
\sum_{n=2}^{\infty}|c_n||b_n|
=
\left(\sum_{n=2}^{\infty}\frac{|c_n|^2}{n-1}\right)^{1/2},
\tag{11}
\]
with equality attained in the relaxed body by the Cauchy–Schwarz extremal direction. This proves the stated method barrier. It does **not** assert that every extremal point of the relaxed body is realized by a schlicht function.

## Proof of Corollary 2

In (2), take
\[
c_n=(n+1)^{-\sigma}.
\]
Condition (A) becomes precisely
\[
H(\sigma):=2^{1-\sigma}+\sqrt{R(\sigma)}\le1.
\tag{12}
\]
For \(\sigma>0\), the series in (3) converges, every term decreases strictly with \(\sigma\), and hence \(H\) is continuous and strictly decreasing. Also \(H(\sigma)\to\infty\) as \(\sigma\downarrow0\) and \(H(\sigma)\to0\) as \(\sigma\to\infty\), so (4) has a unique solution.

The exact tail can also be written as the positive zeta-series
\[
R(\sigma)=
\sum_{k=0}^{\infty}2^k
\left[
\zeta(2\sigma+k+1)-1-2^{-(2\sigma+k+1)}
\right],
\tag{13}
\]
obtained from
\(
[(m-2)m^{2\sigma}]^{-1}
=m^{-(2\sigma+1)}(1-2/m)^{-1}
\)
for \(m\ge3\).

The standalone verifier in `artifacts/verify_threshold.py` uses only positive partial sums and an integral tail majorant. It checks
\[
H(1.413519)>0,
\qquad
H(1.413520)<0,
\]
which establishes the displayed numerical enclosure, with the truncation error controlled explicitly.

It remains to check (B). For \(\sigma\ge\sigma_*>1.4\),
\[
\begin{aligned}
\sum_{n=2}^{\infty}\frac{n-1}{(n+1)^{2\sigma}}
&=\sum_{m=3}^{\infty}\frac{m-2}{m^{2\sigma}}\\
&<\sum_{m=3}^{\infty}m^{-1.8}\\
&\le3^{-1.8}+\int_3^\infty x^{-1.8}\,dx\\
&=3^{-1.8}+\frac{3^{-0.8}}{0.8}
<0.658<1.
\end{aligned}
\tag{14}
\]
Thus (B) is automatic throughout the range in (6), and Theorem 1 applies.

## Where the improvement comes from

The 2013 proof already uses the area theorem and Cauchy–Schwarz. Its nonvanishing step, however, separates \(b_2\) and then replaces the remaining exact weighted square sum by a larger zeta tail before maximizing over \(|b_2|\le1\). Keeping the exact Hilbert norm from the outset collapses this two-stage estimate to (11), eliminating that loss. The improvement is therefore structural rather than a change of special function: it identifies the exact zero-free envelope supplied by the same two universal coefficient constraints.

## Limitations

- The true smallest universal \(\sigma\) remains undetermined; only its known upper bound is lowered.
- The support-function sharpness is only for the relaxed coefficient body (C), not for the actual coefficient body of \(\mathcal S\).
- Stronger schlicht information coupling \(b_1\) to the area-theorem tail could lower the threshold further.
- The literature search cannot rule out an equivalent result under different transform notation or in an inaccessible source; the review file records the main residual risks.


## References

1. R. M. Ali, M. Obradović, S. Ponnusamy, “Necessary and sufficient conditions for univalent functions,” *Complex Variables and Elliptic Equations* **58** (2013), 611–620. DOI: https://doi.org/10.1080/17476933.2011.599116 . Theorem 1.6, Corollary 1.7, and the terminal open problem are the direct source.
2. M. Obradović, S. Ponnusamy, P. Vasundhra, “Univalence and starlikeness of nonlinear integral transform of certain class of analytic functions,” *Proceedings - Mathematical Sciences* **119** (2009), 593–610. DOI: https://doi.org/10.1007/s12044-009-0057-5 . Its abstract treats a more general integral kernel but assumes the input lies in a restricted \(\mathcal U(\lambda,\mu)\) class.
3. M. Obradović, S. Ponnusamy, “Univalence and starlikeness of certain transforms defined by convolution of analytic functions,” *Journal of Mathematical Analysis and Applications* **336** (2007), 758–767. DOI: https://doi.org/10.1016/j.jmaa.2007.03.020 . The accessible abstract treats hypergeometric convolution transforms of inputs in \(\mathcal U(\lambda)\).
