# A width-invisibility transition in boundary-distance statistics of flat Möbius bands

## Finding
Let \(M_{a,b}\) be the compact flat Möbius band obtained from the Euclidean rectangle \([0,a]\times[-b,b]\), with \(a,b>0\), by identifying \((0,y)\sim(a,-y)\). Its single boundary has intrinsic arclength \(2a\). For independent arclength-uniform boundary points \(X,Y\), let \(D=d_{M_{a,b}}(X,Y)\) be their **ambient intrinsic shortest-path distance in the band**, not their boundary-only distance. Put
\[
 c=2b,\qquad r_*=\frac a2+\frac{c^2}{2a}=\frac a2+\frac{2b^2}{a}.
\]

**Complete distribution.** If \(c\ge a\), then \(D\) is uniform on \([0,a]\). If \(0<c<a\), its cumulative distribution function for all real \(r\) is
\[
 F_{a,b}(r)=\Pr(D\le r)=
 \begin{cases}
 0,&r\le0,\\[2pt]
 r/a,&0<r<c,\\[2pt]
 \bigl(r+\sqrt{r^2-c^2}\bigr)/a,&c\le r<r_*,\\[2pt]
 1,&r\ge r_*.
 \end{cases}
\]
The density is \(1/a\) on \((0,c)\), and is
\[
 f_{a,b}(r)=\frac1a\left(1+\frac{r}{\sqrt{r^2-c^2}}\right)
 \quad(c<r<r_*).
\]
It therefore has the integrable one-sided singularity
\[
 f_{a,b}(r)\sim\frac{\sqrt b}{a\sqrt{r-2b}}
 \quad\text{as }r\downarrow 2b\text{ from above}.
\]
There are no atoms. The support endpoint is \(r_*\) in the narrow regime and \(a\) in the wide regime.

**Sharp inverse classification.** The probability law \(\mathcal L(D)\) determines \(a\). For \(0<b<a/2\) it also determines \(b\), by
\[
 a=\bigl(F_{a,b}'(0+)\bigr)^{-1},\qquad
 b=\frac12\sqrt{a(2r_*-a)}.
\]
However, for **every** pair \(b,b'\ge a/2\), the complete boundary-distance functions of \(M_{a,b}\) and \(M_{a,b'}\), identified by boundary arclength, are identical even though the bands have different areas when \(b\ne b'\). Thus the probability laws are identical precisely when the horizontal lengths agree and either the two widths agree in the narrow regime or both widths are in the wide regime.

The fraction of random endpoint pairs whose minimizing path crosses the interior rather than following a boundary arc is exactly
\[
 \Pr(\text{interior shortcut})=
 \begin{cases}
 \dfrac12-\dfrac{2b^2}{a^2},&0<b<a/2,\\[2pt]
 0,&b\ge a/2.
 \end{cases}
\]
The expectation, a further exact summary of the transition, is \(\mathbb ED=a/2\) when \(b\ge a/2\). When \(0<b<a/2\), it is
\[
 \mathbb ED=\frac{r_*}{2}+\frac{2b^2}{a}
 \operatorname{arsinh}\!\left(\frac{a-r_*}{2b}\right)
 <\frac a2.
\]

## Assumptions and scope
The metric is the quotient **intrinsic path metric** inherited from the Euclidean rectangle, with the flat product metric and the stated orientation-reversing end identification; it is not the Euclidean distance in a particular three-dimensional embedding. Both \(a\) and \(b\) are strictly positive and finite. The boundary points are independent and uniform with respect to the one-dimensional arclength measure on the single boundary component. All formulas concern distances between boundary points measured by paths allowed anywhere in the band. The threshold case \(2b=a\) belongs to the wide regime and has a uniform distance law. The degenerate limit \(b\downarrow0\) is not itself part of the theorem.

## Proof
Write the flat universal cover as the convex Euclidean strip \(\mathbb R\times[-b,b]\), with deck isometry \(g(x,y)=(x+a,-y)\). Each boundary point has infinitely many lifts; among all lifted pairs, the shortest possible path is a straight segment, because the covering strip is convex. Taking the infimum over deck translates is therefore an exact, exhaustive distance computation.

Give the unique boundary circle arclength coordinate \(t\in\mathbb R/(2a\mathbb Z)\). For points \(p,q\) let \(u\in[0,a]\) be their shorter boundary arc length. The endpoint lifts with the *same* vertical coordinate have horizontal separations congruent to \(u\) modulo \(2a\), hence their minimum Euclidean separation is exactly \(u\). The lifts with *opposite* vertical coordinates have vertical separation \(2b\) and horizontal separations congruent to \(a-u\) modulo \(2a\), hence their minimum Euclidean separation is \(\sqrt{(a-u)^2+4b^2}\). Any additional even or odd deck translate has no shorter horizontal separation. Consequently the full boundary-distance kernel is
\[
 d_{M_{a,b}}(p,q)=\min\left\{u,\sqrt{(a-u)^2+4b^2}\right\}. \tag{1}
\]
In particular it depends only on the boundary arclength separation and not on the base point.

For two independent arclength-uniform boundary points, their oriented arclength difference modulo \(2a\) is uniform on \([0,2a)\). Folding that difference at \(a\) proves \(U=u(X,Y)\sim\operatorname{Uniform}[0,a]\).

Comparing the squared competitors in (1) gives
\[
 u\le\sqrt{(a-u)^2+4b^2}\quad\Longleftrightarrow\quad
 u\le\frac{a^2+4b^2}{2a}=r_*.
\]
If \(2b\ge a\), this inequality holds throughout \([0,a]\), so \(D=U\) and the full boundary-distance kernel equals the metric of the circle of circumference \(2a\). For \(2b<a\), the graph of \(D\) as a function of \(u\) is the increasing line \(D=u\) on \([0,r_*]\), followed by the strictly decreasing branch \(D=\sqrt{(a-u)^2+4b^2}\) on \([r_*,a]\), whose endpoint values are \(r_*\) and \(2b\).

For \(0<r<2b\), only the increasing branch contributes to \(\{D\le r\}\); its total \(u\)-length is \(r\). For \(2b\le r<r_*\), the increasing branch contributes length \(r\), and the decreasing branch contributes precisely the interval \([a-\sqrt{r^2-4b^2},a]\), of length \(\sqrt{r^2-4b^2}\). Dividing by \(a\) gives the stated distribution. Differentiation gives the density. Since \(r^2-4b^2\sim4b(r-2b)\) as \(r\downarrow2b\), the density has exactly the stated square-root singularity. Continuity of the piecewise CDF at both junctions proves the absence of atoms.

The short-distance law \(F(r)=r/a\) yields \(a=1/F'(0+)\). For \(2b<a\), the support endpoint \(r_*<a\) determines \(b\) from \(4b^2=a(2r_*-a)\). For \(2b\ge a\), (1) proves that the *entire* boundary-distance kernel, hence its probability law, is independent of \(b\). This establishes the exact inverse equivalence classes. Distinct widths yield nonisometric flat bands because their areas \(2ab\) differ.

The interior shortcut wins precisely for \(u>r_*\), a set with uniform probability \((a-r_*)/a=1/2-2b^2/a^2\) when \(2b<a\), and probability zero otherwise. Finally integrate (1) against \(du/a\). In the narrow case,
\[
 \mathbb ED=\frac1a\left(\frac{r_*^2}{2}
 +\int_0^{a-r_*}\sqrt{z^2+4b^2}\,dz\right).
\]
The elementary antiderivative and the identity \(\sqrt{(a-r_*)^2+4b^2}=r_*\) simplify this integral to the displayed expression. Strictly positive shortcut probability gives \(\mathbb ED<a/2\), completing the proof.

## Verification
A standalone standard-library Python verifier is supplied as `verify_mobius.py`. Its independently enumerated deck-transformation distances agreed with formula (1) on 210,000 randomly selected endpoint pairs across seven aspect ratios, including the threshold. It also compared the analytic CDF against 68 independent midpoint-integral estimates (using 25,000 offset points per estimate), compared seven analytic means with separate midpoint integrations, and checked narrow-width inversion and wide-width collapse. The executed output was:

```text
MOBIUS_BOUNDARY_LAW_OK deck_pairs=210000 independent_cdf_checks=68 mean_quadratures=7 inverse_checks=7
```

These finite tests are consistency checks; the above universal-cover argument and exact integration prove the results for all positive \(a,b\).

## Relationship to prior work
Croke and Herreros, *Lens rigidity with trapped geodesics in two dimensions* (arXiv:1108.4938v1, first posted 24 August 2011), prove that a flat Möbius strip is determined by its **lens data**. Their Section 3 uses oriented double covers and geodesic rigidity; it does not give this boundary-pair distance probability law, the singularity, or the sharp width-invisibility threshold for boundary-distance information. Lens data includes travel times and directions and is strictly richer than the unlabeled pair-distance histogram. Croke, *Boundary and lens rigidity of finite quotients* (2005), studies boundary/lens rigidity and constructs nonrigidity examples under quotients; those results also do not supply the explicit flat-Möbius distance law or its phase boundary. Granata and Carnevale (2016) analyze pairwise distance profiles for noisy embedded point clouds including a multiply twisted Möbius surface, a different sampling/metric problem. The present result is limited to the explicit canonical flat rectangular quotient; no broader boundary-rigidity assertion is made.

## Limitations
The geometry is the abstract flat rectangular Möbius band. The formula need not hold for elastically deformed or intrinsically curved Möbius surfaces, arbitrary nonuniform boundary sampling, interior sampling, or extrinsic Euclidean distances. The inverse classification is **within this two-parameter flat family**; it is not a rigidity theorem among arbitrary Riemannian surfaces. Existing literature may contain an equivalent expression under a different boundary-distance or glide-reflection parametrization; publication priority has not been independently certified. No independent audit has been performed.

## References
- C. B. Croke and P. Herreros, *Lens rigidity with trapped geodesics in two dimensions*, arXiv:1108.4938v1 (24 August 2011), sections 1 and 3. https://arxiv.org/html/1108.4938v1
- C. B. Croke, *Boundary and lens rigidity of finite quotients*, *Proceedings of the American Mathematical Society* **133** (2005), 3663–3668. https://doi.org/10.1090/S0002-9939-05-07927-X
- D. Granata and V. Carnevale, *Accurate Estimation of the Intrinsic Dimension Using Graph Distances: Unraveling the Geometric Complexity of Datasets*, *Scientific Reports* **6**, 31377 (2016). https://doi.org/10.1038/srep31377
