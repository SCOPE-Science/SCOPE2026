# Exact angular exclusion law and a two-adic alignment transition for regular polygons

## Finding
For integers \(n,m\ge 3\), radii \(R,S>0\), and a real relative angle \(\phi\), define
\[
P_n(R)=\operatorname{conv}\{R(\cos(2\pi j/n),\sin(2\pi j/n)):0\le j<n\},
\]
and define \(P_m(S)\) similarly. Write \(\mathcal R_\phi\) for counterclockwise rotation by \(\phi\) and let the cross-species excluded area be
\[
E_{n,m}(\phi)=\operatorname{area}\big(P_n(R)+(-\mathcal R_\phi P_m(S))\big).
\]
Put \(g=\gcd(n,m)\), \(L=\operatorname{lcm}(n,m)=nm/g\),
\[
\alpha=\frac{\pi}{n}-\frac{\pi}{m}+\frac{\pi}{L}-\pi,
\qquad
C=\frac{2gRS\sin(\pi/n)\sin(\pi/m)}{\sin(\pi/L)},
\]
and let \(\delta(\phi)\in[0,\pi/L]\) be the circular distance from \(\phi\) to \(\alpha+(2\pi/L)\mathbb Z\). Then the exact profile for **every** \(\phi\in\mathbb R\) is
\[
\boxed{E_{n,m}(\phi)=\frac{nR^2}{2}\sin\frac{2\pi}{n}
+\frac{mS^2}{2}\sin\frac{2\pi}{m}+C\cos\delta(\phi).}
\]
Consequently the angular period is exactly \(2\pi/L\); there are precisely \(L\) strict global maxima and \(L\) strict global minima modulo \(2\pi\). The maxima occur at \(\phi\equiv\alpha\pmod{2\pi/L}\) and the minima at \(\phi\equiv\alpha+\pi/L\pmod{2\pi/L}\). Their respective values are \(A_n+A_m+C\) and \(A_n+A_m+C\cos(\pi/L)\), where \(A_n=nR^2\sin(2\pi/n)/2\) and \(A_m=mS^2\sin(2\pi/m)/2\).

The ordinary common-vertex orientation \(\phi=0\) is **a global minimum if and only if** \(n\) and \(m\) are both even and have the same exact power of two dividing them. In every other case it is a global maximum. In terms of the standard valuation \(\nu_2\), the minimum condition is \(\nu_2(n)=\nu_2(m)\ge1\).

The orientation-average and the exact normalized oscillation are
\[
\overline E=A_n+A_m+\frac{p_np_m}{2\pi},\qquad
\boxed{\frac{E_{\max}-E_{\min}}{\overline E-A_n-A_m}
=\frac{\pi}{L}\tan\frac{\pi}{2L}},
\]
where \(p_n=2nR\sin(\pi/n)\), \(p_m=2mS\sin(\pi/m)\) are the perimeters. In particular, along any sequence of side counts with \(L\to\infty\), this dimensionless angular oscillation is \(\pi^2/(2L^2)+O(L^{-4})\), independent of the individual side counts, areas, and their ratio.

## Assumptions and scope
All polygons are **filled**, nondegenerate, centered regular polygons. Their initial vertex directions are at \(2\pi j/n\) and \(2\pi j/m\); this convention fixes the meaning of \(\phi=0\) and the phase \(\alpha\). The radii \(R,S\) are arbitrary positive real numbers, so equal-area particle pairs follow by taking \(R=\sqrt{2A/(n\sin(2\pi/n))}\) and \(S=\sqrt{2B/(m\sin(2\pi/m))}\). No convexity or randomness assumptions beyond the specified regular polygons are needed. The result concerns the geometrical excluded-area kernel, not the random sequential adsorption process or its saturation probability.

## Proof
**1. A standard mixed-area identity.** For planar convex polygons \(P,Q\), the area polynomial under Minkowski addition gives
\[
\operatorname{area}(P+Q)=\operatorname{area}(P)+\operatorname{area}(Q)
+\sum_{e\text{ edge of }P}\operatorname{length}(e)\,h_Q(u_e),
\]
where \(u_e\) is its outer unit normal and \(h_Q(u)=\max_{x\in Q}\langle x,u\rangle\) is the support function. This follows, for instance, by varying the Minkowski coefficient of \(Q\) from zero and computing the first variation of the area through the edges of \(P\); the mixed-area polynomial makes that derivative the full cross coefficient.

For \(P=P_n(R)\), every edge has length \(\ell_n=2R\sin(\pi/n)\) and outward normal angle \(\theta_k=\pi/n+2\pi k/n\). For \(Q=\mathcal R_\psi P_m(S)\), the support in direction \(\theta\) is
\[
h_Q(\theta)=S\cos d_m(\theta-\psi),\qquad
 d_m(t)=\min_{j\in\mathbb Z}|t-2\pi j/m|\in[0,\pi/m].
\]
Thus the mixed cross coefficient of the two unreflected polygons is
\[
F(\psi)=2RS\sin(\pi/n)\sum_{k=0}^{n-1}
\cos d_m(\pi/n+2\pi k/n-\psi).
\]
The excluded-area coefficient equals \(F(\phi+\pi)\) because reflection is rotation by \(\pi\).

**2. Period, kink set and cosine arcs.** The sum defining \(F\) is invariant under \(\psi\mapsto\psi+2\pi/m\) (rotational symmetry of the second polygon) and \(\psi\mapsto\psi+2\pi/n\) (cyclic permutation of the first polygon's normal angles). Hence it is invariant under \(2\pi/L\), the additive generator of these two periods. A summand changes its closest supporting vertex only when
\[
\psi=\frac{\pi}{n}-\frac{\pi}{m}
+2\pi\left(\frac{k}{n}-\frac{j}{m}\right).
\]
As \(k,j\) range through integers, these are precisely the grid
\(\psi_c+(2\pi/L)\mathbb Z\), with \(\psi_c=\pi/n-\pi/m\). On every open interval between successive grid points each summand is a cosine of \(\psi\) with fixed phase; therefore \(F(\psi)=a\cos\psi+b\sin\psi\) on that interval.

Reflection in the horizontal coordinate axis preserves \(P_n(R)\) and sends \(\mathcal R_\psi P_m(S)\) to \(\mathcal R_{-\psi}P_m(S)\). Thus \(F\) is even. Its period \(2\pi/L\) then makes it even about every integer multiple of \(\pi/L\). The midpoint of the grid interval, \(\psi_0=\pi/n-\pi/m+\pi/L=(m/g-n/g+1)\pi/L\), is one such point. The sine coefficient on that interval must vanish, and positivity of the mixed coefficient gives \(F(\psi)=C\cos(\psi-\psi_0)\) there with \(C>0\). Periodicity extends this same cosine arc to all intervals. With \(L\ge3\), each arc has its strict maximum at its midpoint and its strict minimum at the endpoints; the derivative jumps upward at each endpoint. No additional extrema occur.

**3. Exact amplitude from angular averaging.** Over a full rotation, the mean support function of \(P_m(S)\) equals \(mS\sin(\pi/m)/\pi\). Averaging the support sum in step 1 therefore yields
\[
\frac{1}{2\pi}\int_0^{2\pi}F(\psi)\,d\psi
=\frac{2nmRS}{\pi}\sin\frac{\pi}{n}\sin\frac{\pi}{m}
=\frac{p_np_m}{2\pi}.
\]
On the other hand, the average of the cosine arc over a period is
\(C\sin(\pi/L)/(\pi/L)\). Equating the expressions gives the stated exact \(C\). Replacing \(\psi\) by \(\phi+\pi\) gives the displayed formula, extrema, and the universal oscillation ratio
\[
\frac{C(1-\cos(\pi/L))}{C\sin(\pi/L)/(\pi/L)}
=\frac{\pi}{L}\tan\frac{\pi}{2L}.
\]
The Taylor expansion follows from \(\tan t=t+O(t^3)\).

**4. The aligned-angle parity theorem.** Let \(n=gn'\), \(m=gm'\), where \(n',m'\) are coprime. With the excluded-area phase \(\alpha=\psi_0-\pi\), we have
\[
\frac{L\alpha}{\pi}=m'-n'+1-gn'm'\in\mathbb Z.
\]
Thus \(\phi=0\) is always one of the two extreme positions: it is a maximum if this integer is even, a minimum if odd. Because \(n',m'\) are coprime, the integer is odd precisely if both \(n',m'\) are odd and \(g\) is even. This is equivalent to \(\nu_2(n)=\nu_2(m)\ge1\), completing the classification.

## Verification
The accompanying standard-library Python verifier independently constructs Minkowski-sum convex hulls of all pairwise vertex sums and computes their areas by the shoelace formula. For all \(3\le n,m\le14\), it checks five angle/radius configurations for each ordered pair plus both extremal and parity comparisons. Its deterministic execution prints `MIXED_POLYGON_HULL_OK 1008`. These numerical comparisons check formulas and signs, **not** the infinite quantifiers, which are established by the proof above.

For equal-area triangle/square pairs in the common-vertex orientation, the theorem gives excluded area \(4.9357796500\ldots\) times the area of either constituent, agreeing with the \(3+4\) entry \(4.9358\) in the motivating paper's published cross-species table. For an equal-area regular hexagon/decagon pair, the common-vertex orientation instead achieves the minimum \(4.1280011341\ldots\), while the maximum is \(4.1397227593\ldots\). These are illustrations, not additional independent claims.

## Relationship to prior work
The recent binary-mixture RSA study by Abbasi Moud (arXiv:2606.21812, first posted 2026-06-20) computes fixed-orientation cross-species excluded areas for selected polygon pairs, gives the same-species even/odd formula, and relates excluded area to measured saturation. In its entire published text, including Section IV.1 and the cross-species table, it does not give the all-pairs and all-angles law or the binary-valuation criterion.

Geigenfeind and de las Heras (arXiv:1902.05961; *Journal of Chemical Physics* 150, 184906 (2019)) study orientation-dependent excluded areas, with numerical regular-polygon curves for selected identical species and analytic small-shape examples; the complete relevant body of their paper does not provide the cross-species least-common-multiple cosine law. The Minkowski sum algorithm and mixed-area identity are standard; they are **inputs**, not asserted as original. The result here is the explicit mixed-regular-polygon evaluation, its complete angular-extrema classification, and its universal arithmetic oscillation invariant.

## Limitations
This theorem concerns regular Euclidean polygons of arbitrary **positive** circumradii and independent integer side counts at least three. It does not extend to irregular polygons or determine the stochastic RSA saturation density. In particular, having smaller pairwise excluded area is not by itself a theorem about which mixture jams more densely. Historical originality has been checked against selected directly relevant sources and mathematical search records but may still be affected by poorly indexed prior results; no independent mathematical audit has been performed.

## References
1. Aref Abbasi Moud, *Saturation Coverage in Binary Mixtures of Oriented Regular Polygons via Random Sequential Adsorption*, arXiv:2606.21812 (first posted June 20, 2026). https://arxiv.org/abs/2606.21812
2. Thomas Geigenfeind and Daniel de las Heras, *Principal component analysis of the excluded area of two-dimensional hard particles*, J. Chem. Phys. 150, 184906 (2019), DOI:10.1063/1.5092865; preprint arXiv:1902.05961. https://arxiv.org/abs/1902.05961
3. Michał Cieśla, Piotr Kubala, Aref Abbasi Moud, *Random sequential adsorption of aligned regular polygons and rounded squares: Transition in the kinetics of packing growth*, Phys. Rev. E 107, 054904 (2023); arXiv:2304.14149. https://arxiv.org/abs/2304.14149
4. CGAL, *2D Minkowski Sums: User Manual*, section on convex polygon Minkowski sums. https://cgal.github.io/9465/doc/Minkowski_sum_2/index.html
