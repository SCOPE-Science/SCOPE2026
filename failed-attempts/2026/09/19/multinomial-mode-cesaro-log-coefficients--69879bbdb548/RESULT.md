# Universal Cesàro law for all logarithmic coefficients at multinomial modes

Let
\[
X\sim\operatorname{Mult}(N;p_1,\ldots,p_n),\qquad p_i>0,\quad \sum_i p_i=1,
\]
and assume that \(p_1,\ldots,p_n\) are linearly independent over \(\mathbb Q\).  For each \(N\), let \(m(N)\) be the unique multinomial mode and put
\[
t_i(N)=m_i(N)-Np_i.
\]
Elezović's complete local expansion writes
\[
\Pr\{X=m\}=(2\pi N)^{-(n-1)/2}\Bigl(\prod_i p_i\Bigr)^{-1/2}
\exp\!\left(\sum_{k\ge1}c_k(t;p)N^{-k}\right),
\]
with
\[
c_k(t;p)=\frac{(-1)^{k+1}}{k(k+1)}
\left[B_{k+1}-\sum_{i=1}^n p_i^{-k}B_{k+1}(t_i+1)\right].
\]
The source paper derives Cesàro averages for a floor reference that is generally off the multinomial slice, and explicitly leaves the corresponding on-slice mode averages open.

## Theorem

For every fixed integer \(k\ge1\), the actual-mode Cesàro mean exists and depends only on the number of categories \(n\), not on \(p\):
\[
\boxed{
\lim_{M\to\infty}\frac1M\sum_{N=1}^M c_k(t(N);p)
=
\frac{(-1)^{k+1}}{k(k+1)}\bigl(B_{k+1}-A_{k+1}(n)\bigr)
}
\]
where
\[
\boxed{
A_m(n)=\frac{m!(n-2)!}{(m+n-2)!}
\left\{\begin{matrix}m+n-1\\ n-1\end{matrix}\right\}
}
\]
and \(\left\{\begin{smallmatrix}a\\b\end{smallmatrix}\right\}\) is a Stirling number of the second kind.

Equivalently,
\[
\boxed{
\overline c_k=
(-1)^{k+1}
\left[
\frac{B_{k+1}}{k(k+1)}
-
\frac{(k-1)!(n-2)!}{(n+k-1)!}
\left\{\begin{matrix}n+k\\n-1\end{matrix}\right\}
\right].
}
\]
The first four values are
\[
\overline c_1=-\frac{(n-1)(3n+4)}{24},
\]
\[
\overline c_2=\frac{n(n-1)(n+2)}{48},
\]
\[
\overline c_3=-\frac{(n-1)(15n^3+45n^2-10n-32)}{2880},
\]
\[
\overline c_4=\frac{n(n-1)(n+4)(3n^2+n-6)}{1920}.
\]

## Proof

Elezović identifies the multinomial mode with Jefferson--D'Hondt apportionment.  Under the stated rational-independence hypothesis, no two relevant Jefferson quotients can tie, so the mode is unique.  Thus the displacement \(t_i(N)\) is precisely the Jefferson seat excess \(\Delta_i\) for party \(i\) at house size \(N\).

Janson's theorem for the \(\beta\)-linear divisor method, specialized to Jefferson (\(\beta=1\)), says that when \(N\) is uniform on \(\{1,\ldots,M\}\) and \(M\to\infty\),
\[
t_i(N)\ \Rightarrow\ T_i
:=\frac{np_i-1}{2}+\widetilde U_0
+p_i\sum_{j=1}^{n-2}\widetilde U_j,
\]
where the \(\widetilde U_j\) are independent \(\operatorname{Unif}(-1/2,1/2)\).  The seat excesses are uniformly bounded; Janson consequently obtains convergence of all moments.  Since \(B_{k+1}(x+1)\) is a polynomial, its Cesàro mean is therefore its expectation under \(T_i\).

Let
\[
\phi(z)=\mathbb E e^{z\widetilde U}=\frac{\sinh(z/2)}{z/2}.
\]
The Bernoulli-polynomial generating function gives
\[
\sum_{m\ge0}\mathbb E[B_m(T_i+1)]\frac{z^m}{m!}
=\frac{z}{e^z-1}\,\mathbb E e^{z(T_i+1)}.
\]
Using the displayed law of \(T_i\), the right side is
\[
\frac{z}{e^z-1}
\exp\!\left(\frac{np_i+1}{2}z\right)
\phi(z)\phi(p_i z)^{n-2}.
\]
The identity
\[
\frac{z}{e^z-1}e^{z/2}\phi(z)=1
\]
cancels the factor not involving \(p_i\).  Hence, with \(w=p_i z\),
\[
\sum_{m\ge0}\mathbb E[B_m(T_i+1)]\frac{z^m}{m!}
=F_n(p_i z),
\]
where
\[
F_n(w)=e^{nw/2}\phi(w)^{n-2}
=e^w\left(\frac{e^w-1}{w}\right)^{n-2}.
\]
Writing \(F_n(w)=\sum_{m\ge0}A_m(n)w^m/m!\), we obtain
\[
\mathbb E[B_m(T_i+1)]=A_m(n)p_i^m.
\]
To evaluate \(A_m(n)\), note that
\[
e^w(e^w-1)^{n-2}=\frac1{n-1}\frac{d}{dw}(e^w-1)^{n-1}
\]
and use
\[
(e^w-1)^{n-1}=(n-1)!\sum_{r\ge n-1}
\left\{\begin{matrix}r\\n-1\end{matrix}\right\}\frac{w^r}{r!}.
\]
After differentiation and division by \(w^{n-2}\), coefficient extraction yields
\[
A_m(n)=\frac{m!(n-2)!}{(m+n-2)!}
\left\{\begin{matrix}m+n-1\\n-1\end{matrix}\right\}.
\]
Finally, for \(m=k+1\),
\[
\sum_{i=1}^n p_i^{-k}\mathbb E[B_{k+1}(T_i+1)]
=A_{k+1}(n)\sum_i p_i=A_{k+1}(n),
\]
and substitution into Elezović's coefficient formula proves the theorem.

## Numerical check

For
\[
p=\left(\frac{\sqrt2}{4},\frac{\pi}{12},1-\frac{\sqrt2}{4}-\frac{\pi}{12}\right),
\qquad n=3,
\]
the theorem predicts
\[
(\overline c_1,\overline c_2,\overline c_3,\overline c_4)
=\left(-\frac{13}{12},\frac58,-\frac{187}{360},\frac{21}{40}\right).
\]
A direct sequential Jefferson computation through \(N=300000\) gives
\[
(-1.083333541441,\ 0.624999524646,\ -0.519442279598,\ 0.524993603403),
\]
with absolute discrepancies below \(6.4\times10^{-6}\).  The standalone verification script is in `artifacts/verify_modal_cesaro.py`.

## Interpretation and relation to prior work

The underlying ingredients are prior results: Elezović supplies the all-orders Bernoulli-polynomial local coefficients and the identification of multinomial modes with Jefferson--D'Hondt allocations; Janson supplies the fixed-\(p\), random-house-size asymptotic distribution of Jefferson seat excesses and convergence of their moments.  The contribution here is the bridge between these two results and the resulting all-orders closed Cesàro formula for the coefficients evaluated at the actual multinomial mode.

This also explains why the apparent on-slice coupling simplifies after averaging: each individual Bernoulli polynomial acquires exactly one factor \(p_i^{k+1}\); the \(p_i^{-k}\) weight in the local coefficient leaves a single \(p_i\), and the sum over bins collapses to \(1\).

## Limitations

The theorem assumes rational independence of \(p_1,\ldots,p_n\), equivalently the generic fixed-\(p\) regime used in the cited divisor-method limit theorem.  Rational or otherwise resonant vectors can have periodic arithmetic effects and ties and are not classified here.  The result concerns the logarithmic coefficients \(c_k\).  It does not claim that all multiplicative coefficients obtained after exponentiating the series have universal modal Cesàro means, because products of different \(c_j\) require joint moments.  No uniformity in \(k\) or in \(p\) near resonant vectors is asserted.

## References

1. N. Elezović, *Multinomial probabilities near the mode: integer modes and the complete local expansion*, arXiv:2609.20229v1 (2026). https://arxiv.org/abs/2609.20229
2. S. Janson, *Asymptotic bias of some election methods*, arXiv:1110.6369; published in *Annals of Operations Research* 215 (2014), 89--136, DOI 10.1007/s10479-012-1141-2. https://arxiv.org/abs/1110.6369
3. U. Schwingenschlögl and M. Drton, *Seat excess variances of apportionment methods for proportional representation*, Statistics & Probability Letters 76 (2006), 1723--1730. https://doi.org/10.1016/j.spl.2006.04.014
4. M. Drton and U. Schwingenschlögl, *Surface volumes of rounding polytopes*, Linear Algebra and its Applications 378 (2004), 71--91. https://doi.org/10.1016/j.laa.2003.09.005
