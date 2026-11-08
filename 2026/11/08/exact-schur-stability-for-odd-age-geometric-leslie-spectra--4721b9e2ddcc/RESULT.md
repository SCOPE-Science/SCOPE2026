# Exact Schur stability for odd-age geometric Leslie spectra

## Finding
For every odd integer \(n\ge3\), every \(0<p<1\), and every real \(a\), define
\[
Q_{n,p,a}(z)=z^n+a\sum_{j=0}^{n-1}p^jz^{n-1-j},\qquad K_n(p)=\sum_{j=0}^{n-1}p^j.
\]
The polynomial is **strictly Schur stable** (all its zeros satisfy \(|z|<1\)) if and only if
\[
\boxed{-\frac{1}{K_n(p)}<a<\frac{1+p}{1+p^n}.}
\]
At the lower boundary the unique unit-modulus root is \(z=1\), simple; at the upper boundary the unique unit-modulus root is \(z=-1\), simple, and all other roots lie strictly inside the unit circle. The upper crossing is transverse: if \(z(a)\) is the real root near \(-1\),
\[
\left.\frac{dz}{da}\right|_{a=(1+p)/(1+p^n)}
=-\frac{1+p^n}{1+n p^n(1+p)/(1+p^n)}<0.
\]
In particular, for positive \(a\), the first loss of Schur stability is always by a simple negative real multiplier, not by a complex-conjugate unit-circle pair, for **every** \(p\in(0,1)\), including \(p>1/2\).

For the age-structured Leslie map of Wikan and Kristensen with equal fecundities and equal survivals, put \(X=\sum_{j=1}^n x_j\), \(F>0\), \(-1\le\gamma\le0\), \(0<p<1\), and
\[
(x_1,\ldots,x_n)\longmapsto
\big(F\,G_\gamma(X)X,\;px_1,\;px_2,\ldots,px_{n-1}\big),
\]
where \(G_\gamma(X)=(1-\gamma X)^{1/\gamma}\) for \(\gamma<0\), and \(G_0(X)=e^{-X}\). When \(FK_n(p)>1\), the positive equilibrium exists. Its Jacobian has characteristic polynomial \(Q_{n,p,a}\), with
\[
a=\frac{(1+\gamma)X^*-1}{K_n(p)(1-\gamma X^*)}.
\]
Define the dimensionless threshold
\[
B_n(p)=1+K_n(p)\frac{1+p}{1+p^n}
=\frac{2(1-p^{n+1})}{(1-p)(1+p^n)}.
\]
The equilibrium is linearly asymptotically stable for **every** finite positive total equilibrium population \(X^*\) if \(\gamma\le-1/B_n(p)\). If \(\gamma>-1/B_n(p)\), it is linearly asymptotically stable precisely for
\[
0<X^*<\frac{B_n(p)}{1+\gamma B_n(p)},
\]
is linearly nonhyperbolic with one simple multiplier \(-1\) at equality, and linearly unstable at larger \(X^*\). This sharp recruitment-parameter division is part of the same spectral theorem; it does not assert existence or supercriticality of a nonlinear period-two orbit.

## Assumptions and scope
The polynomial statement applies to all real \(a\), odd \(n\ge3\), and \(0<p<1\); there are no assumptions of simple interior roots. The biological corollary applies to \(F>0\), \(FK_n(p)>1\), \(-1\le\gamma\le0\), equal constant survival probabilities in each age transition, and equal density-dependent fecundity at every age. The normalization \(\alpha=1\) is the same rescaling of total population as in the originating paper. It concerns local spectral stability of the positive equilibrium, not global attractors or the direction of a nonlinear flip bifurcation. At \(p=1\) multiple unit-circle roots may coexist and the statement is not asserted.

## Proof
**1. Geometric telescoping.** For every complex \(z\), polynomial multiplication gives the exact identity
\[
(z-p)Q_{n,p,a}(z)=z^{n+1}+(a-p)z^n-ap^n.\tag{1}
\]
It is valid also at \(z=p\); multiplication introduces an auxiliary zero \(p\), strictly inside the unit circle, and never changes the stability of \(Q_{n,p,a}\).

**2. Negative-coefficient half.** For \(a=-c<0\), \(Q\) is the characteristic polynomial of the nonnegative primitive companion matrix with first row \((c,cp,\ldots,cp^{n-1})\) and unit subdiagonal. Its Perron radius \(r\) is the unique positive solution of
\[
1=c\sum_{j=0}^{n-1}\frac{p^j}{r^{j+1}},
\]
because the right-hand side decreases strictly from infinity to zero as \(r\) increases. Therefore \(r<1\) exactly when \(cK_n(p)<1\). At \(cK_n(p)=1\), the Perron root \(z=1\) is simple, and all other roots have modulus below one by primitivity. For \(cK_n(p)>1\), \(r>1\). At \(a=0\) all zeros are zero. This proves the lower boundary and the full \(a\le0\) classification.

**3. No complex crossing for positive coefficients.** Set \(a_+=(1+p)/(1+p^n)\) and suppose \(0<a<a_+\). If \(|z|=1\) and \(Q(z)=0\), (1) implies
\[
|z+a-p|=ap^n.\tag{2}
\]
If \(a\le p\), then \(|z+a-p|\ge1-p+a>ap^n\), a contradiction. If \(p<a<a_+\), then \(0<a-p<a_+-p=(1-p^{n+1})/(1+p^n)<1\), so
\[
|z+a-p|\ge1+p-a>ap^n,
\]
where the final strict inequality is equivalent to \(a(1+p^n)<1+p\). Thus no root meets the unit circle while \(0<a<a_+\). All roots start at zero when \(a=0\) and depend continuously, as a multiset, on \(a\); they therefore stay strictly inside the circle throughout this interval.

**4. Sharp upper boundary and transversality.** As \(n\) is odd,
\[
Q(-1)=-1+a\sum_{j=0}^{n-1}(-p)^j=-1+\frac{a(1+p^n)}{1+p}.
\]
Hence \(z=-1\) is a root exactly at \(a=a_+\). At this value, (1) is \(z^n(z+b)=1-b\), with \(b=a_+-p=(1-p^{n+1})/(1+p^n)\in(0,1)\). On \(|z|=1\), \(|z+b|\ge1-b\), with equality only at \(z=-1\). Thus there is no second unit-circle root, and all other zeros are inside by continuity from \(a<a_+\). Differentiating (1) at \((z,a)=(-1,a_+)\) yields
\[
\frac{dz}{da}=-\frac{1+p^n}{1+n(1-b)}<0,
\]
which equals the displayed formula and shows that the crossing is simple and outward. If \(a>a_+\), then \(Q(-1)>0\) while \(Q(x)\to-\infty\) as \(x\to-\infty\) (odd degree), so a real root lies below \(-1\). Combining with step 2 proves the if-and-only-if characterization, including all equality cases.

**5. Transfer to the population equilibrium.** The originating model's linearization yields precisely the displayed coefficient \(a\) and the above geometric companion characteristic polynomial. For any \(X^*>0\) with \(-1\le\gamma\le0\),
\[
a+\frac{1}{K_n(p)}=\frac{X^*}{K_n(p)(1-\gamma X^*)}>0.
\]
Thus the lower Schur boundary never binds at a positive equilibrium. Furthermore
\[
\frac{da}{dX^*}=\frac{1}{K_n(p)(1-\gamma X^*)^2}>0.
\]
The upper inequality \(a<a_+\) rearranges exactly to
\[
(1+\gamma B_n(p))X^*<B_n(p).
\]
When the multiplier of \(X^*\) on the left is nonpositive, this holds for all positive finite \(X^*\). Otherwise it holds precisely on the claimed finite interval. At equality the step-4 analysis supplies one simple multiplier \(-1\); above equality it supplies a real multiplier less than \(-1\). This finishes the biological corollary without extrapolating nonlinear dynamics from linearization.

## Verification
Run `python3 check_spectrum.py` with NumPy installed. The script checks 371 statements, including exact rational algebra at both boundaries, a strict-order phase separation, sample numerical root locations on both sides, simple critical multiplier, transverse derivative, and the originating paper's \(n=7\), \(p=4/5\), \(X^*\approx6.8795\) example. The infinite-dimensional family of odd integer degrees is proved analytically above; no finite numerical scan certifies that universal quantifier.

## Relationship to prior work
Wikan and Kristensen's 2023 preprint (DOI 10.21203/rs.3.rs-2815894/v1), and its 2024 journal revision (DOI 10.1007/s11071-023-09143-w), derived this geometric characteristic polynomial and the candidate flip boundary. They proved only a sufficient condition for general odd degree in the high-survival regime, stating the remaining case \(1/2<p<1\) as a conjecture supported by numerical experiments. Their \(n=3\) result already covers that low-degree case. Wikan's 2012 numerical analysis and Wikan--Kristensen (2017) previously asserted the same qualitative odd-age flip pattern; the priority claim here is **not** that the pattern or candidate threshold was first observed, but that the exact all-degree Schur stability interval, absence of earlier complex crossings, and the proof valid through all \(0<p<1\) are established rigorously. The recruitment-parameter division follows from that complete interval and the already-known linearization. No claim is made about the supercritical nature of the nonlinear bifurcation in all odd dimensions.

## Limitations
The proof addresses local eigenvalue stability, not global attraction, periodic-orbit existence, or the nonlinear direction of a flip. It excludes the degenerate endpoint \(p=1\). It assumes equal fecundity coefficients and common survival \(p\); heterogeneous survival can admit other instabilities. A pre-existing general Schur-polynomial theorem might supply an equivalent abstract statement, and the historical numerical claims limit novelty of the qualitative observation. No independent mathematical audit has been conducted.

## References
1. A. Wikan and Ø. Kristensen, *On bifurcations, resonances and chaos control in nonlinear Leslie matrix models*, 2023 preprint, posted 2023-04-27, DOI: 10.21203/rs.3.rs-2815894/v1, https://doi.org/10.21203/rs.3.rs-2815894/v1.
2. A. Wikan and Ø. Kristensen, *On bifurcations, resonances and dynamical behaviour in nonlinear iteroparous Leslie matrix models*, Nonlinear Dynamics 112 (2024), 2265–2288, DOI: 10.1007/s11071-023-09143-w, https://doi.org/10.1007/s11071-023-09143-w.
3. A. Wikan and Ø. Kristensen, *Nonstationary and Chaotic Dynamics in Age-Structured Population Models*, Discrete Dynamics in Nature and Society (2017), Article 1964286, DOI: 10.1155/2017/1964286, https://doi.org/10.1155/2017/1964286.
4. A. Wikan, *Towards Some General Ecological Principles*, Journal of Mathematics and Statistics 8 (2012), 446–460, DOI: 10.3844/jmssp.2012.446.460, https://doi.org/10.3844/jmssp.2012.446.460.
