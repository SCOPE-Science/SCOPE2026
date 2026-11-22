# A sharp first-order dimensional gap for convex-body centroid displacement

## Finding

For each integer \(n\ge 3\), let \(D_n\) denote the smallest sharp constant in
\[
 |\langle c(\partial K)-c(K),u\rangle|\le D_n w_K(u)
\]
for all full-dimensional Euclidean convex bodies \(K\subset\mathbb R^n\) and all unit vectors \(u\). Here \(c(K)\) is the volume centroid, \(c(\partial K)\) is the surface-area centroid, and \(w_K\) is directional width. The existence and exact one-parameter variational characterization of \(D_n\) are established in [1]; the limit \(D_\infty\) is identified in [2].

Define, for \(s>0\),
\[
 J_k(s)=\int_0^1 t^k e^{-st}\,dt\quad(0\le k\le4),\qquad
 F(s)=\frac{J_2(s)}{J_1(s)}-\frac{J_1(s)}{J_0(s)}.
\]
There is exactly one positive maximizer \(s_*\) of \(F\). In fact it is the unique positive zero of
\[
\begin{split}
P(s)={}&e^{4s}+(-4-2s+2s^2-s^3)e^{3s}\\
&+(6+6s-4s^2)e^{2s}\\
&+(-4-6s+2s^2+s^3+s^4)e^s+1+2s.
\end{split}
\]
Put \(D_\infty=F(s_*)\) and
\[
 C=\frac{s_*^2}{2}\left(\frac{J_4}{J_1}-\frac{J_2J_3}{J_1^2}-\frac{J_3}{J_0}+\frac{J_1J_2}{J_0^2}\right)_{s=s_*}.
\]
Then \(C>0\), and the sharp dimensional refinement is
\[
\boxed{D_n=D_\infty-\frac{C}{n-2}+O((n-2)^{-2})\qquad(n\to\infty).}
\]
The maximizing affine profile from [1], once its value at the left endpoint is normalized to \(1\), is unique for all sufficiently large \(n\), and has slope
\[
 -\frac{s_*}{n-2}+O((n-2)^{-2}).
\]
For reference, \(s_*\approx2.35331738518\), \(D_\infty\approx0.20161927408\), and \(C\approx0.03826706098\). Rational enclosure establishes \(2.353317385<s_*<2.353317386\) and \(0.0382<C<0.0385\).

## Assumptions and scope

All limits are as positive integers \(n\to\infty\); no assumption of smoothness, central symmetry or strict convexity is made on \(K\). The main result is a quantitative analysis of the **already known** sharp constants rather than a new inequality for an individual body. For any positive integer \(m=n-2\), the prior work [1,2] characterizes the same \(D_n\) by
\[
D_n=\max_{-1\le a<\infty}\left(
\frac{\int_0^1 t^2(1+at)^m\,dt}{\int_0^1t(1+at)^m\,dt}
-\frac{\int_0^1t(1+at)^m\,dt}{\int_0^1(1+at)^m\,dt}\right).
\]
The case \(a=+\infty\) is interpreted as the limit. The branch \(a<0\) is parameterized by \(a=-s/m\), \(0\le s\le m\). The definition of \(D_\infty\) agrees with the known limiting sharp constant [2].

## Proof

**1. Reduction to decreasing affine weights and compactness.** For a probability density proportional to a nonnegative weight \(w\) on \([0,1]\), write \(\mu=\mathbb E_w t\) and \(\sigma^2=\operatorname{Var}_w(t)\). Then
\[
\frac{\int t^2w}{\int tw}-\frac{\int tw}{\int w}=\frac{\sigma^2}{\mu}.
\]
Reflection \(t\mapsto1-t\) preserves \(\sigma^2\) and changes \(\mu\) into \(1-\mu\). For a nonconstant increasing affine-power weight, \(\mu>1/2\), so its reflected decreasing weight gives a strictly larger quotient. Thus every maximizer for \(n>2\) lies on the decreasing branch (or is uniform). Put
\[
w_{m,s}(t)=(1-st/m)^m,\quad 0\le s\le m,\quad
F_m(s)=\frac{\int t^2w_{m,s}}{\int tw_{m,s}}-\frac{\int tw_{m,s}}{\int w_{m,s}}.
\]
For \(0<s\le m\), the logarithmic derivative satisfies \(-w'_{m,s}\ge s w_{m,s}\). Integrating the derivative of \(t^2w_{m,s}\), with nonnegative boundary value at \(t=1\), yields \(s\int t^2w_{m,s}\le2\int tw_{m,s}\). Hence \(0<F_m(s)\le2/s\). Since \(F_m(2)\to F(2)>0.19\), every maximum of \(F_m\) lies in \([0,11]\) for all sufficiently large \(m\). This uniform compactness prevents escape to the degenerate affine endpoint.

**2. The limiting maximizer is unique.** Let \(E=e^s\). Elementary integration gives
\[
J_0=\frac{1-E^{-1}}s,\quad
J_1=\frac{1-(1+s)E^{-1}}{s^2},\quad
J_2=\frac{2-(s^2+2s+2)E^{-1}}{s^3}.
\]
Direct differentiation and cancellation show that, for \(s>0\),
\[
 F'(s)=-\frac{P(s)}{s^2(e^s-1)^2(e^s-1-s)^2}.
\]
Write \(P(s)=\sum_{k=0}^\infty b_ks^k/k!\). Its coefficients vanish for \(0\le k\le7\). Those for \(8\le k\le13\) are strictly negative, namely
\[
\frac{b_k}{k!}=-\frac1{144},-\frac7{720},-\frac{29}{4320},-\frac{29}{10080},-\frac{659}{907200},-\frac1{181440}
\]
in increasing order of \(k\). For \(k\ge14\), writing
\[
 A_k=\frac{k^3-9k^2+26k+108}{27},\quad
 B_k=-k^2+4k+6,\quad
 C_k=k^4-5k^3+10k^2-12k-4,
\]
one has the exact coefficient identity
\[
b_k=4^k-3^k A_k+2^k B_k+C_k.
\]
Here \(C_k>0\) and \(B_k\ge-k^2\) for \(k\ge14\). Moreover
\[
4A_k-3A_{k+1}=\frac{k^3-18k^2+71k+54}{27}>0
\]
for all \(k\ge14\). Together with \(2(k+1)^2\le4k^2\), this inductively gives
\[
4^k-3^kA_k-2^kk^2>0\quad(k\ge14),
\]
starting from its strictly positive value \(8006748\) at \(k=14\). Thus every \(b_k\) with \(k\ge14\) is strictly positive. It follows that \(P(s)/s^{13}\) is strictly increasing for \(s>0\): each negative-power term from \(k=8,\ldots,12\) increases, the \(k=13\) term is constant, and every positive-power term increases. Its limits at zero and infinity have opposite signs. Therefore \(P\) has exactly one positive zero \(s_*\), and \(F\) increases before and decreases after that zero. The zero is simple, so \(F''(s_*)<0\). The exponential weight with positive exponent is never globally optimal by the reflection argument, and \(F(0)=1/6<F(s_*)\).

**3. Uniform expansion and optimization.** On each bounded interval of \(s\), uniformly together with two derivatives in \(s\),
\[
(1-st/m)^m=e^{-st}\left(1-\frac{s^2t^2}{2m}+O(m^{-2})\right),\quad0\le t\le1.
\]
Consequently, with \(J_k=J_k(s)\),
\[
F_m(s)=F(s)+\frac{G(s)}m+O(m^{-2}),
\]
where
\[
G(s)=-\frac{s^2}{2}\left(\frac{J_4}{J_1}-\frac{J_2J_3}{J_1^2}-\frac{J_3}{J_0}+\frac{J_1J_2}{J_0^2}\right).
\]
The compactness in step 1, uniform convergence, and strict uniqueness from step 2 imply that *every* maximizing \(s_m\) tends to \(s_*\). Strict negativity of \(F''\) on a neighborhood of \(s_*\), together with uniform convergence of second derivatives, makes \(F_m\) strictly concave there; hence its maximizer is unique for all sufficiently large \(m\). The critical-point equation and the first derivative expansion give \(s_m=s_*+O(m^{-1})\). Substituting this into the value expansion and using \(F'(s_*)=0\) gives
\[
 D_n=F_m(s_m)=D_\infty+\frac{G(s_*)}{m}+O(m^{-2}).
\]
Defining \(C=-G(s_*)\) gives the claimed asymptotic and the affine-slope formula. Strict positivity and the numerical enclosures for \(C\) are certified in step 4.

**4. Rational certificate.** The standalone script `check_centroid_rate.py` proves by exact integer/rational operations that \(P(2.353317385)<0<P(2.353317386)\) (and therefore brackets the unique zero), then bounds \(e^s\), the moments \(J_k\), \(F\), and \(-G\) by rational intervals over that bracket. Its output encloses \(0.20160<D_\infty<0.20163\) and \(0.0382<C<0.0385\). No floating-point calculation is relied upon for either strict inequality. Together with the analytic proof, this establishes \(C>0\).

## Verification

Run `python3 check_centroid_rate.py` from the directory containing the two files. The script uses only the Python standard library. It checks the low-order Taylor cancellations, the sign pattern through degree 59 and the induction base, and performs rational interval evaluations for the root and constants. The infinitely many higher-degree signs follow from the displayed induction, not from finite enumeration. Independent high-precision quadrature, not required for the proof, yielded \(s_*=2.3533173851806463\) and \(C=0.03826706097680694\), and finite-dimensional optimizations show convergence of \((n-2)(D_\infty-D_n)\) towards \(C\).

## Relationship to prior work

[1] proves the sharp body-boundary centroid inequality and its variational representation. [2] first studies the identical constants in centroid projection, proves their monotonicity and limiting value, and numerically locates the exponential maximizer near \(-2.35332\). Neither inspected primary text states the explicit positive first-order dimensional gap or establishes the displayed unique-zero coefficient argument. The finite-dimensional value of \(D_4\) has also been computed separately; it neither implies the asymptotic rate nor supplies the first-order coefficient. No new claim is made to the underlying sharp inequality, its extremizing-body construction, or the earlier limiting constant.

## Limitations

This result provides an asymptotic expansion as \(n\to\infty\), not a globally valid two-sided \(C/n\) bound at every small dimension. The displayed big-O term is not given an explicit numerical threshold. The numerical constant is defined through the unique transcendental root, not asserted to be algebraic. The scientific review was not independent and literature priority remains provisional.

## References

[1] S. Myroshnychenko, D. Ryabogin, K. Tatarko and V. Yaskin, *The sharp bound on the distance between the centers of mass of a convex body and its boundary*, arXiv:2611.11635v1 (first public 8 November 2026), https://arxiv.org/html/2611.11635v1.

[2] S. Myroshnychenko, K. Tatarko and V. Yaskin, *How far apart can the projection of the centroid of a convex body and the centroid of its projection be?*, arXiv:2212.14456v1 (first public 29 December 2022); later *Mathematische Annalen* 390 (2024), 1155–1169, https://arxiv.org/pdf/2212.14456.
