# Parity-resolved first variation of diagonal coverings of the square flat torus

## Finding

Let \(T=(\mathbb R/\mathbb Z)^2\) and \(C_n=\{(j/n,j/n):j=0,\ldots,n-1\}\). If \(d_{S^1}(u,v)=\min_{m\in\mathbb Z}|u-v-m|\), let \(d_p((x,y),(u,v))=[d_{S^1}(x,u)^p+d_{S^1}(y,v)^p]^{1/p}\) for real \(p\ge1\). Define the **fixed-site** covering radius \(R_n(p)=\max_{z\in T}\min_{c\in C_n}d_p(z,c)\).

For every integer \(n\ge4\), the radius obeys \(R_n(1)=1/2\) and \(R_n(p)<1/2\) for all finite \(p>1\). More sharply,
\[
R_n(1+\varepsilon)=\frac12-\kappa_n\varepsilon+o(\varepsilon),\qquad\varepsilon\downarrow0,
\]
where \(H(t)=-t\log t-(1-t)\log(1-t)\), continuously extended by \(H(0)=H(1)=0\), and
\[
\kappa_n=\begin{cases}\displaystyle\frac12H\!\left(\frac12+\frac1n\right),&n\text{ even},\[4pt]\displaystyle\frac14\left[\log2+H\!\left(\frac12+\frac1n\right)\right],&n\text{ odd}.\end{cases}
\]
The parity distinction survives at the first finite-size correction:
\[
\begin{aligned}
\kappa_n&=\frac{\log2}{2}-\frac1{n^2}-\frac2{3n^4}+O(n^{-6})&& (n\text{ even}),\
\kappa_n&=\frac{\log2}{2}-\frac1{2n^2}-\frac1{3n^4}+O(n^{-6})&&(n\text{ odd}).
\end{aligned}
\]
Here \(n=3\) matches a previously obtained three-site coefficient, and \(n=2\) is exceptional: \(R_2(p)=1/2\) for every finite \(p\ge1\). The new result is the complete parity-sensitive formula for all integers \(n\ge4\).

## Assumptions and scope

All circle lengths are exactly one, the sites lie on the stated diagonal at equal arclength spacing, logarithms are natural, and the centers do **not** vary when minimizing the radius. No statement is made about globally optimal placements of \(n\) freely chosen centers, or about the exact covering radius at general fixed \(p>1\). The asymptotic limit takes \(p\downarrow1\) with the positive integer \(n\) fixed. The displayed large-\(n\) expansion is an expansion of the resulting coefficient \(\kappa_n\), not a uniform two-parameter expansion of \(R_n(p)\).

## Proof

**1. Exact additive endpoint and its maximizing set.** Set \(F_p(x,y)=\min_{s\in\{0,1/n,\ldots,(n-1)/n\}}[d_{S^1}(x,s)^p+d_{S^1}(y,s)^p]^{1/p}\). If \(y=x+1/2\pmod1\), then for every \(s\) the two coordinate distances add to \(1/2\), hence \(F_1(x,y)=1/2\). Conversely, if \(x,y\) are not antipodal, let their shorter circular separation be \(\ell<1/2\). If a site lies on a shortest arc between them, the sum of distances to that site equals \(\ell\). If none does, both endpoints lie inside one open grid gap of length \(1/n\). The sums to its two endpoints have minimum at most \(1/n<1/2\), because the two endpoint sums add to \(2/n\). Thus \(F_1(x,y)<1/2\) off the antipodal circle. The equality locus of the entire additive covering functional is therefore exactly \(\{(x,x+1/2):x\in S^1\}\). Since \(F_p\le F_1\), this proves \(R_n(p)\le1/2\). For \(p>1\), off-antipodal points have strict inequality already at \(p=1\). At antipodal points, at least one of the \(n\ge3\) sites has both coordinate distances positive; its strict \(\ell_p\)-versus-\(\ell_1\) inequality makes \(F_p<1/2\). Compactness yields \(R_n(p)<1/2\).

**2. Uniform first variation and localization.** For nonnegative \(a,b\) with \(a+b\) near \(1/2\), uniformly as \(\varepsilon\downarrow0\),
\[
(a^{1+\varepsilon}+b^{1+\varepsilon})^{1/(1+\varepsilon)}
=(a+b)-\varepsilon(a+b)H\!\left(\frac a{a+b}\right)+o(\varepsilon).
\]
Continuity of \(t\log t\) at zero makes the remainder uniform on the compact relevant domain. At an antipodal test point, every site distance is \(1/2+O(\varepsilon)\) in the \(\ell_{1+\varepsilon}\) metric, so \(R_n(1+\varepsilon)\ge1/2-O(\varepsilon)\). Take any maximizing point, write \(y=x+1/2+\delta\pmod1\) with \(|\delta|\le1/2\). Uniqueness of the \(p=1\) maximizing locus first implies \(\delta=o(1)\). For \(|\delta|<1/2-1/n\), a shortest arc from \(x\) to \(y\) has length \(1/2-|\delta|>1/n\) and contains a grid site. Thus \(F_1(x,y)\le1/2-|\delta|\). Combining with \(F_{1+\varepsilon}\le F_1\) gives \(|\delta|=O(\varepsilon)\).

**3. Sharp two-sided local optimization.** Denote the two open semicircles from \(x\) to \(x+1/2\) and back by plus and minus. For a site strictly inside the positive semicircle, the additive sum at \(y=x+1/2+\delta\) equals \(1/2+\delta\), whereas on the negative semicircle it equals \(1/2-\delta\), for sufficiently small \(\delta\). The largest entropy penalties on these two arcs are
\[
h_\pm(x)=\frac12\max_{s\text{ in the respective open semicircle}}H\bigl(2d_{S^1}(x,s)\bigr).
\]
Each arc contains a grid site within \(1/(2n)\) of its midpoint, hence the maximizing sites can be chosen a fixed positive distance from both arc endpoints. In particular, this argument remains uniform in \(x\), including when a site lies at an arc endpoint. Writing \(\delta=\varepsilon z\) with \(z\) bounded, the two chosen sites give the upper bound
\[
F_{1+\varepsilon}(x,y)\le\min\!\left\{\frac12+\varepsilon(z-h_+(x)),\frac12+\varepsilon(-z-h_-(x))\right\}+o(\varepsilon)
\le\frac12-\frac\varepsilon2(h_+(x)+h_-(x))+o(\varepsilon).
\]
Consequently \(\liminf_{\varepsilon\downarrow0}(1/2-R_n(1+\varepsilon))/\varepsilon\ge\frac12\min_x(h_+(x)+h_-(x))\).

For the reverse inequality, choose a point \(x\) minimizing \(h_+(x)+h_-(x)\) as explicitly characterized below and put \(\delta=\varepsilon[h_+(x)-h_-(x)]/2\). Every site in either open semicircle has entropy penalty no greater than the respective \(h_\pm(x)\), so its distance is at least \(1/2-\varepsilon[h_+(x)+h_-(x)]/2+o(\varepsilon)\). If \(n\) is odd, the chosen \(x\) is not a grid site, hence there are no endpoint sites. If \(n\) is even, the chosen \(x\) has \(h_+(x)=h_-(x)\), so \(\delta=0\): any site exactly at \(x\) or its antipode has distance exactly \(1/2\) and cannot reduce this lower bound. As the site set is finite, all remainders are simultaneous. This proves the exact identity
\[
\kappa_n=\frac12\min_{x\in S^1}\bigl(h_+(x)+h_-(x)\bigr).
\]

**4. Parity reduction.** Let \(e_+(x)\) and \(e_-(x)\) be the distances from \(x+1/4\) and \(x+3/4\), respectively, to the circular grid \((1/n)\mathbb Z/\mathbb Z\). The entropy penalty is maximal for a site closest to the midpoint of its semicircle; therefore
\[
h_\pm(x)=\frac12H\bigl(1/2+2e_\pm(x)\bigr).
\]
If \(n\) is even, the midpoint targets differ by an integral number of grid steps, so \(e_+=e_-\). The entropy decreases strictly as its argument runs from \(1/2\) to \(1\), so the sum is smallest at \(e_+=e_-=1/(2n)\), giving \(\kappa_n=\frac12H(1/2+1/n)\). If \(n\) is odd, the midpoint targets differ by a half-step modulo the grid, whence \(e_++e_-=1/(2n)\). The sum \(H(1/2+2e_+)+H(1/2+1/n-2e_+)\) is strictly concave on the full allowed interval and is minimized at either endpoint; this gives \(\kappa_n=[\log2+H(1/2+1/n)]/4\). The minimizing phases may be taken as \(x=-1/4+1/(2n)\) for even \(n\), and \(x=-1/4\) for odd \(n\), modulo one. Finally, Taylor expansion of binary entropy,
\[
H(1/2+u)=\log2-2u^2-\frac43u^4+O(u^6),
\]
proves the two size expansions.

**5. Exceptional two-site boundary.** For \(n=2\), the two diagonal sites are \((0,0)\) and \((1/2,1/2)\). Their additive covering radius is \(1/2\), while \((0,1/2)\) has \(\ell_p\) distance exactly \(1/2\) to both sites for every finite \(p\ge1\). Therefore \(R_2(p)=1/2\). Substituting \(n=3\) in the odd formula recovers the previously established three-site value \(\log12/4-5\log5/24\); the new classification begins at \(n=4\).

## Verification

The accompanying standalone `verify.py` evaluates the explicit minimizing phases, confirms their finite-difference slopes against the closed entropy formulas for all integer sizes from 3 through 16 at three small exponent increments, checks the exceptional two-site configuration, and samples thousands of further torus points. Run `python3 verify.py` with Python's standard library. These finite numerical tests are corroboration only: the compactness, uniform first-variation, and parity-concavity arguments above establish the infinite statements.

## Relationship to prior work

Cieliebak and Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1 (first posted 11 November 2026), investigate product-metric covering numbers and provide a finite four-cycle product-covering counterexample for every exponent above one (Example 3.4). Their result concerns discrete spaces and unrestricted covering numbers; it neither states nor implies the continuous square-torus fixed-design parity derivative. A separate previous calculation already handled precisely three diagonal sites. The present claim is the sharp formula and distinct parity-dependent finite-size corrections simultaneously for every integer \(n\ge4\). Related two-disk covering results for well-rounded flat tori study unrestricted Euclidean placements and do not give this prescribed-site derivative.

## Limitations

No general formula for \(R_n(p)\) at finite \(p>1\), nor any optimality statement among arbitrary \(n\)-point designs, is proved here. The asymptotic is taken at fixed size first, and its error term is not asserted uniform in growing size. The literature comparison is based on accessible primary texts and searchable records and cannot exclude unindexed historical equivalents; independent mathematical review remains unperformed.

## References

1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1, posted 11 November 2026. https://arxiv.org/html/2611.15599v1
2. *Sharp two-disk covering of all well-rounded flat tori*, public mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-disk-covering-of-all-well-rounded-flat-tori--559d72822a1a
