# Exact upper copula capacity of superellipse contours

## Finding

Let \(U,V\) have uniform marginals on \([0,1]\), with arbitrary dependence. For \(p>0\), \(0<a,b\le 1/2\), and centers \(c,d\) satisfying \([c-a,c+a]\subseteq[0,1]\) and \([d-b,d+b]\subseteq[0,1]\), define the **contour event**

\[
E_{a,b,p}^{c,d}=\left\{(u,v)\in[0,1]^2:\left(\frac{|u-c|}{a}\right)^p+\left(\frac{|v-d|}{b}\right)^p=1\right\}.
\]

Its sharp upper copula capacity, including attainment, is

\[
\sup_{U,V\sim\operatorname{Unif}[0,1]}\Pr\!\left((U,V)\in E_{a,b,p}^{c,d}\right)=\begin{cases}
2\left(a^q+b^q\right)^{1/q},&0<p<1,\quad q=\frac{p}{p-1}<0,\\[3pt]
2\min(a,b),&p=1,\\[3pt]
2\left[a+b-\left(a^q+b^q\right)^{1/q}\right],&p>1,\quad q=\frac{p}{p-1}>1.
\end{cases}
\]

The value is independent of the admissible center. In any maximizing coupling, the restriction to the contour has a uniquely determined distribution for the folded first coordinate \(|U-c|\), with density

\[
f_*(u)=2\min\{1,|g'(u)|\},\qquad g(u)=b\left(1-(u/a)^p\right)^{1/p},\quad 0<u<a.
\]

Sign assignments and the distribution off the contour need not be unique. For fixed \(a,b\), the capacity is strictly less than \(2\min(a,b)\) for every \(p\ne1\), and equals that projection bound exactly at \(p=1\). In the equal-axis case \(a=b=r\), the capacity becomes

\[
4r\min\{2^{-1/p},1-2^{-1/p}\}.
\]

In particular, the circle \(p=2\) has capacity \(4r(1-1/\sqrt2)\), the diamond \(p=1\) has capacity \(2r\), and the one-sided derivatives of the capacity as a function of \(p\) at \(p=1\) are \(2r\log2\) and \(-2r\log2\).

## Assumptions and scope

All random variables are real-valued, with each one-dimensional marginal the Lebesgue-uniform probability law on \([0,1]\). No independence, exchangeability, absolute continuity, or density assumption is imposed on the joint law. The contour is defined by equality, not by the closed filled superellipse inequality. Parameters \(a,b\) are positive and at most \(1/2\); centers may vary freely as long as the two bounding coordinate intervals stay in \([0,1]\). The theorem applies to all real \(p>0\), including concave exponent contours for \(p<1\), but does not assert a formula for general exponents differing between axes.

## Proof

**1. Folding the contour submeasure.** Fix any coupling \(\pi\), and restrict it to the contour, obtaining a finite measure \(\nu(B)=\pi(B\cap E_{a,b,p}^{c,d})\). Let \(u=|x-c|\) and \(v=|y-d|\). On the contour, \(v=g(u)\) for the strictly decreasing bijection \(g:[0,a]\to[0,b]\) given in the finding. As \(U\) is uniform and both signs \(c\pm u\) are within \([0,1]\), the measure of \(u\) under \(\nu\) is bounded by \(2\,du\). Therefore it has a density \(f\) with \(0\le f\le2\) almost everywhere. The analogous statement for the second folded coordinate gives \(g_*(f\,du)\le2\,dv\). A change of variable on \((0,a)\), where \(g\) is continuously differentiable with \(g'<0\), yields \(f(u)\le2|g'(u)|\) almost everywhere. Endpoint atoms are impossible under the atomless uniform marginals. Hence

\[
\pi(E_{a,b,p}^{c,d})=\int_0^a f(u)\,du\le2\int_0^a\min\{1,|g'(u)|\}\,du.\tag{1}
\]

**2. Attaining the bound with an explicit copula.** Set \(f=f_*\) and put a subprobability measure \(\nu_*\) on the four contour quadrants by pushing \(f_*(u)\,du\) through \((u,\varepsilon,\delta)\mapsto(c+\varepsilon u,d+\delta g(u))\), where the signs \(\varepsilon,\delta\) are independent fair signs. Its mass is \(m=\int_0^a f_*\,du\), which is at most \(1\) by (1) and \(a\le1/2\). On \(c\pm(0,a)\), its first marginal density equals \(f_*(u)/2\le1\); on \(d\pm(0,b)\), its second marginal density equals \(f_*(u)/(2|g'(u)|)\le1\). Both marginals of \(\nu_*\) are thus dominated by Lebesgue probability measure \(\lambda\). Let \(\alpha=\lambda-(\nu_*)_1\) and \(\beta=\lambda-(\nu_*)_2\); each has mass \(1-m\). If \(m<1\), the probability measure

\[
\pi_* =\nu_*+\frac{\alpha\otimes\beta}{1-m}
\]

has both uniform marginals. Since \(\alpha\) and \(\beta\) have Lebesgue densities, the product term gives no mass to the one-dimensional contour. Thus \(\pi_*(E)=m\), attaining (1). If \(m=1\), simply use \(\pi_*=\nu_*\). Whenever equality holds in (1), the nonnegative integral of \(f_*-f\) vanishes, forcing \(f=f_*\) almost everywhere. This proves uniqueness of the folded contour submeasure, but not uniqueness of the entire coupling.

**3. Evaluating the integral.** For \(0<u<a\), direct differentiation gives

\[
|g'(u)|=\frac ba\left(\frac{u/a}{g(u)/b}\right)^{p-1}.
\]

For \(p\ne1\), this derivative crosses \(1\) once, at \(u=u_*\), \(g(u_*)=v_*\), where, with \(q=p/(p-1)\),

\[
u_* =\frac{a^q}{(a^q+b^q)^{1/p}},\qquad
v_* =\frac{b^q}{(a^q+b^q)^{1/p}},\qquad
u_*+v_*=(a^q+b^q)^{1/q}.
\]

These symbols \(u_*\), \(v_*\) designate the threshold coordinates and are unrelated to the measure \(\nu_*\) in Step 2. If \(p>1\), \(|g'|\) increases from zero to infinity, so (1) evaluates to

\[
2\left[\int_0^{u_*}|g'(u)|\,du+(a-u_*)\right]=2\left[b-v_*+a-u_*\right].
\]

If \(0<p<1\), \(|g'|\) decreases from infinity to zero, so (1) evaluates to

\[
2\left[u_*+\int_{u_*}^a|g'(u)|\,du\right]=2(u_*+v_*).
\]

At \(p=1\), \(g(u)=b(1-u/a)\), and (1) equals \(2a\min\{1,b/a\}=2\min(a,b)\). This proves the three branches.

**4. Sharp change at the diamond.** For \(p>1\), the \(\ell_q\) expression \((a^q+b^q)^{1/q}\) is strictly greater than \(\max(a,b)\) when \(a,b>0\). For \(p<1\), the negative-order expression \((a^q+b^q)^{1/q}\) is strictly below \(\min(a,b)\). Both give strict capacity loss relative to \(p=1\). For \(a=b=r\), the formulas simplify to the stated minimum of two elementary branches. Differentiation shows the opposite one-sided slopes and the unique maximizing exponent.

## Verification

The proof is analytical and valid over uncountable real parameter domains. The separately supplied `checks/verify.py` evaluates the formula against an independently partitioned one-dimensional integral, checks the circular and diamond specializations, and checks the shape and threshold identities at many admissible parameter values. Run `python checks/verify.py` with `mpmath` installed. Numerical checks corroborate arithmetic only; the universal upper bound, optimal construction, and uniqueness of the folded mass are all proved in Steps 1–3.

## Relationship to prior work

The immediate research motivation comes from Trutschnig and Úbeda-Flores (2026), *The closed convex hull of all associative copulas is a Z-set in the family of all bivariate Schur concave copulas, and related results*, first publicly posted October 24, 2026. Their Theorem 4.11 sharply restricts mass on staircase approximations to increasing chains for the **closed convex hull of associative copulas**, revealing the dependence of curve mass on both geometry and the admissible coupling family. This theorem instead optimizes the exact probability of a **nonlinear closed contour** over **all** copulas, independent of associativity or Schur concavity. Their curve and staircase results do not yield the capacity formula here. Omladič, Vuk and Zalar (2026), *A linear programming approach to finite copula interpolation*, publicly posted November 10, 2026, develop finite-grid compatibility certificates for prescribed copula values, but do not evaluate continuum equality-contour event capacities.

A subsequently posted study by Côté and Wang (November 18, 2026), *The upper copula capacity*, formalizes the general upper capacity and states a Kellerer-type covering characterization for every closed bivariate set (Proposition 6). That abstract characterization applies to this contour but does not itself state the evaluated \(L^p\)-contour formula, the explicit optimizer, or the diamond exponent classification. Its Theorem 2 evaluates **convex filled** sets via coordinate projection lengths, whereas our event is only their **boundary**, not a convex set. Perlman and Wellner (2011), *Squaring the Circle and Cubing the Sphere*, study circularly and elliptically symmetric copulas supported in filled geometric regions, not optimization of mass on a specified equality contour. General marginal compatibility results of Strassen and Kellerer are credited through the discussion in Côté and Wang; no originality is claimed for the general covering duality.

## Limitations

This theorem treats a specific natural symmetric-axis contour family and two uniform marginals. It does not provide general closed-set capacity solutions, uniqueness of full maximizing copulas, or formulas for three or more variables. An equivalent explicit result in literature not located by the stated comparisons remains a possible historical-priority risk. There has been no independent mathematical validation; the reported verification is a same-model analytical and computational review.

## References

1. Wolfgang Trutschnig and Manuel Úbeda-Flores, *The closed convex hull of all associative copulas is a Z-set in the family of all bivariate Schur concave copulas, and related results*, arXiv:2610.33646v1, October 24, 2026, https://arxiv.org/html/2610.33646v1 (especially Theorem 4.11).
2. Matjaž Omladič, Martin Vuk and Aljaž Zalar, *A linear programming approach to finite copula interpolation*, arXiv:2611.14008v1, November 10, 2026, https://arxiv.org/html/2611.14008v1.
3. Benjamin Côté and Ruodu Wang, *The upper copula capacity*, arXiv:2611.25237v1, November 18, 2026, https://arxiv.org/html/2611.25237v1 (subsequent general capacity work; in particular Proposition 6 and Theorem 2).
4. Michael D. Perlman and Jon A. Wellner, *Squaring the Circle and Cubing the Sphere: Circular and Spherical Copulas*, Symmetry 3 (2011), 574–599, doi:10.3390/sym3030574, https://pmc.ncbi.nlm.nih.gov/articles/PMC3369321/.
