# A signed negative-binomial correction for heterogeneous geometric sums

## Finding

Let \(c\ge2\) and let \(X_1,\ldots,X_c\) be independent geometrically distributed random variables on \(\mathbb N_0\), with \(\Pr(X_j=k)=(1-y_j)y_j^k\), \(0\le y_j<1\). Put
\[
W=\sum_{j=1}^c X_j,\quad w=\frac1c\sum_{j=1}^c y_j\in(0,1),\quad a=1-\max_jy_j>0,
\quad S_2=\sum_j(y_j-w)^2,\quad S_3=\sum_j|y_j-w|^3.
\]
Write \(N_{r,w}\) for the negative-binomial probability mass function with generating function \(((1-w)/(1-wz))^r\), extended by zero to negative integers. Define the signed mass-one sequence
\[
H(k)=N_{c,w}(k)+\frac{S_2}{2(1-w)^2}\bigl[N_{c+2,w}(k-2)-N_{c,w}(k)\bigr],\qquad k\in\mathbb N_0.
\]
(The signed sequence need not be nonnegative.) For \(d_{\rm TV}(P,H)=\tfrac12\sum_{k\ge0}|P(k)-H(k)|\), the following **all-parameter** bounds hold:
\[
\boxed{d_{\rm TV}(\mathcal L(W),N_{c,w})\le \frac{S_2}{2a^2}},
\qquad
\boxed{d_{\rm TV}(\mathcal L(W),H)\le
\min\left\{\frac{S_2}{a^2},\ \frac{S_3}{3a^3}+\frac{S_2^2}{4a^4}\right\}}.
\]
The constants are independent of the number of geometric summands. In the second bound, the refined error is cubic in a fixed small parameter spread, whereas the uncorrected error is quadratic.

There is also an exact local leading constant. Fix \(c\ge2\), \(w\in(0,1)\), and real \(v_1,\ldots,v_c\) with \(\sum_jv_j=0\). Set \(y_j(h)=w+h v_j\) for sufficiently small real \(h\), and \(V_2=\sum_jv_j^2\). Let \(m\) be the largest integer \(k\ge1\) satisfying
\[
k(k-1)\le\theta:=\frac{c(c+1)w^2}{(1-w)^2}.
\]
Then, with \(Z_r\sim N_{r,w}\),
\[
\boxed{\lim_{h\to0}\frac{d_{\rm TV}(\mathcal L(W_h),N_{c,w})}{h^2}
=\frac{V_2}{2(1-w)^2}
\bigl[\Pr(Z_{c+2}\ge m-1)-\Pr(Z_c\ge m+1)\bigr].}
\]
This coefficient is strictly positive whenever \(V_2>0\). Equality at the threshold \(m(m-1)=\theta\) is permitted; the corresponding correction coefficient is exactly zero.

## Assumptions and scope

All statements are for finite \(c\ge2\), independent geometric variables supported on \(\mathbb N_0\), and \(0\le y_j<1\) with \(0<w<1\). The estimates are nonasymptotic, cover all heterogeneity sizes, and use the maximum parameter only through \(a>0\). They make no claim that the signed approximant \(H\) is a probability law. Total variation with a signed mass-one sequence means one-half its absolute difference norm, not the supremum over events formula for two probability measures. The local limit varies \(h\) through values keeping every \(y_j(h)\) in \([0,1)\).

## Proof

Work in the Banach algebra of absolutely summable real sequences on \(\mathbb N_0\), with convolution and norm \(\|\cdot\|_1\). For \(0\le y<1\), write \(G_y(z)=(1-y)/(1-yz)\) for the geometric generating function. Its logarithmic derivative in the parameter is the absolutely summable signed series
\[
A_y(z)=\frac{\partial_yG_y(z)}{G_y(z)}=-\frac1{1-y}+\frac z{1-yz},\quad
A'_y(z)=-\frac1{(1-y)^2}+\frac{z^2}{(1-yz)^2},\quad
A''_y(z)=-\frac2{(1-y)^3}+\frac{2z^3}{(1-yz)^3}.
\]
All nonconstant coefficients of \(A'_y\) and \(A''_y\) are nonnegative while their constant coefficients are negative, hence
\[
\|A'_y\|_1=\frac2{(1-y)^2},\qquad \|A''_y\|_1=\frac4{(1-y)^3}.
\]
Put \(\delta_j=y_j-w\) and, for \(0\le t\le1\), let \(P_t\) be the probability sequence with generating function \(F_t(z)=\prod_jG_{w+t\delta_j}(z)\). Differentiation is legitimate in \(\ell^1\) because all parameters on the segment stay at most \(1-a\). Since \(\sum_j\delta_j=0\),
\[
P'_t=tP_t*\sum_j\delta_j^2B_{j,t},\qquad
B_{j,t}:=\int_0^1 A'_{w+st\delta_j}\,ds.
\]
The integrals and derivatives are in \(\ell^1\). The derivative bounds imply
\[
\|B_{j,t}\|_1\le 2/a^2,\qquad
\|B_{j,t}-A'_w\|_1\le (2t/a^3)|\delta_j|.
\]
Consequently \(\|P'_t\|_1\le 2tS_2/a^2\), and integration yields
\[
\|P_t-P_0\|_1\le t^2 S_2/a^2.
\]
At \(t=0\), \(P_0=N_{c,w}\). Define \(Q=(S_2/2)P_0*A'_w\). The generating-function identity
\[
F_0(z)A'_w(z)=\frac{z^2}{(1-w)^2}G_w(z)^{c+2}-\frac{1}{(1-w)^2}G_w(z)^c
\]
shows that \(P_0+Q=H\) as defined in the finding. Comparing \(P'_t\) with \(tS_2P_0*A'_w\) gives, using the convolution norm inequality,
\[
\begin{aligned}
\|P'_t-tS_2P_0*A'_w\|_1
&\le t\|P_t-P_0\|_1\sum_j\delta_j^2\|B_{j,t}\|_1
+t\sum_j\delta_j^2\|B_{j,t}-A'_w\|_1\\
&\le 2t^3S_2^2/a^4+2t^2S_3/a^3.
\end{aligned}
\]
Integrating from \(0\) to \(1\) and dividing by two proves the refined bound. The first bound is half the earlier \(\|P_1-P_0\|_1\) bound. Since \(\|Q\|_1\le S_2/(1-w)^2\le S_2/a^2\), the triangle inequality gives the alternative \(S_2/a^2\) bound for \(H\). This concludes the nonasymptotic claims.

For the local constant, \(S_2=h^2V_2\), \(S_3=|h|^3\sum_j|v_j|^3\), and \(a\) is bounded away from zero for sufficiently small \(|h|\). Therefore the refined estimate yields \(\|P_h-P_0-Q_h\|_1=o(h^2)\). The coefficient of \(Q_h/h^2\) at \(k\) is
\[
\frac{V_2}{2}N_{c,w}(k)\left[\frac{k(k-1)}{c(c+1)w^2}-\frac1{(1-w)^2}\right].
\]
Its sign is negative or zero for \(k\le m\) and positive for \(k\ge m+1\). The total mass of \(Q_h\) is zero, because both negative-binomial sequences in its definition have mass one. The factorial-bias identity
\[
\frac{N_{c,w}(k)k(k-1)}{c(c+1)w^2}
=\frac{N_{c+2,w}(k-2)}{(1-w)^2}
\]
then expresses the positive mass as the difference of the two displayed upper tails, yielding the boxed limit. If \(V_2>0\), its strictly negative coefficient at \(k=0\) ensures a strictly positive total variation coefficient.

## Verification

The independent standalone program `check_geometric.py` uses standard-library exact fractions to test 3,873 coefficient identities, signed-correction comparisons and nonasymptotic inequalities on finite geometric and negative-binomial coefficient prefixes. Run with `python3 check_geometric.py`; expected output: `PASS: 3873 exact-rational assertions (finite coefficient diagnostics; not an infinite proof).` Exact finite-prefix checks do **not** certify the bounds for infinite supports or all parameters. Those conclusions depend on the \(\ell^1\) derivation above, the explicit norm identities, and the zero-mass and sign arguments. No external formal proof or independent mathematical audit is asserted.

## Relationship to prior work

DeSalvo (2026), arXiv:2611.00275v1, Section 2 and Open Problem 2, gives a first-order absolute-spread bound for heterogeneous geometric sums and explicitly calls for an explicit second-order signed correction. Here the correction is a difference of two negative-binomial laws, and a global quadratic bound and cubic-scale residual are proved. Kumar–Upadhye (2016), arXiv:1603.07464, addresses Stein-operator perturbations and moment-matched negative-binomial or convolution targets; its inspected results do not directly contain this fixed-arithmetic-mean signed correction. Earlier signed-compound-Poisson approximation theory of Barbour–Čekanavičius (2002) and Čekanavičius (1998) may yield related expansions. Their precise implication for these coefficients and constants has not been conclusively excluded.

## Limitations

The signed approximant can be negative at some indices, particularly when the spread is large. The bounds need not be numerically small for large heterogeneity or \(w\) near one. The local leading coefficient holds for fixed \(c,w,v\), not uniformly over growing dimension. Although the motivating open problem is addressed mathematically, historical originality is provisional pending comparison with inaccessible older general signed-measure expansions. Independent mathematical validation has not occurred.

## References

- Stephen DeSalvo (2026). *Stein's method for negative binomial and hyper-negative-binomial laws, with applications*. arXiv:2611.00275v1, posted 2026-10-30. https://arxiv.org/html/2611.00275v1
- A. N. Kumar and N. S. Upadhye (2016). *On Perturbations of Stein Operator*. arXiv:1603.07464. https://arxiv.org/abs/1603.07464
- A. D. Barbour and V. Čekanavičius (2002). *Total variation asymptotics for sums of independent integer random variables*. Annals of Probability 30, 509–545. https://doi.org/10.1214/aop/1023481001
- V. Čekanavičius (1998). *Estimates in total variation for convolutions of compound distributions*. Journal of the London Mathematical Society 58, 748–760. https://doi.org/10.1112/S0024610798006693
