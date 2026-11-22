# Sharp dependence-region geometry of a nonexchangeable trivariate copula

## Finding

Consider the second three-dimensional polynomial copula of Chesneau (2024),
\[
C(x,y,z)=xyz\{1+\lambda[1-\alpha x-\beta y-(1-\alpha-\beta)xy](1-z)\},
\qquad 0\le x,y,z\le1,
\]
with arbitrary real finite parameters \(\lambda,\alpha,\beta\). Its **complete** admissible parameter condition is
\[
|\lambda|\,\max\{1,|1-2\alpha|,|1-2\beta|,|2\alpha+2\beta-3|\}\le1. \tag{1}
\]
Let \(\mathcal M=\{8C(1/2,1/2,1/2)-1\}/3\) denote the trivariate medial correlation and let \(\rho=8\int_{[0,1]^3} C-1\) denote the trivariate Spearman coefficient, using the normalizations in the originating paper. Set
\[
a=\lambda,\qquad b=\lambda[2(\alpha+\beta)-3].
\]
Then the **exact joint attainable dependence region** is
\[
\boxed{\left\{(\rho,\mathcal M)=\left(\frac{2a-b}{27},\frac{3a-b}{48}\right): -1\le a,b\le1,\quad (a\ne0\ \text{or}\ b=0)\right\}.} \tag{2}
\]
The closure is a parallelogram. Its entire central diameter corresponding to \(a=0\), except its origin, is absent for finite parameters. Thus the attainable set is not closed, even though each of its four vertices is attained. In particular,
\[
-\frac19\le\rho\le\frac19,\qquad -\frac1{12}\le\mathcal M\le\frac1{12}, \tag{3}
\]
and each endpoint of both intervals is attained simultaneously. The upper endpoints are attained precisely by \(\lambda=1\), \(\alpha+\beta=1\), \(0\le\alpha\le1\), while the lower endpoints are attained precisely with \(\lambda=-1\) and the same condition on \(\alpha,\beta\).

## Assumptions and scope

All three copula coordinates range independently over \([0,1]\); the three parameters are finite real numbers and the coefficient of \(xy\) inside the square brackets is constrained to be \(1-\alpha-\beta\). Positivity of the trivariate density, not merely the pointwise sign of the cumulative distribution, is required. The coefficients \(\rho\) and \(\mathcal M\) are the three-dimensional definitions above, not the ordinary bivariate Spearman coefficient. The result concerns **only the second**, polynomial, nonexchangeable construction in the cited paper; its distinct first polynomial-power construction is excluded.

## Proof

Write \(\gamma=1-\alpha-\beta\) and \(Q(x,y)=1-\alpha x-\beta y-\gamma xy\). The displayed polynomial has grounded zero boundaries and exactly uniform one-dimensional margins, because \(Q(1,1)=0\) and \(1-z=0\) at \(z=1\). Direct differentiation gives the density
\[
c(x,y,z)=\frac{\partial^3 C}{\partial x\partial y\partial z}=1+\lambda(1-2z)F(x,y),\qquad F(x,y)=1-2\alpha x-2\beta y-4\gamma xy. \tag{4}
\]
For each \((x,y)\), the factor \(1-2z\) traverses the entire interval \([-1,1]\). Hence \(c\ge0\) throughout the cube if and only if \(|\lambda F(x,y)|\le1\) throughout the unit square. The bilinear function \(F\) is an affine interpolation in each coordinate, so its values lie between its four corner values, while every corner is achieved. Those values, in order \((0,0),(1,0),(0,1),(1,1)\), are
\[
1,\quad 1-2\alpha,\quad1-2\beta,\quad2(\alpha+\beta)-3.
\]
Taking absolute maxima proves necessity and sufficiency of (1), including equality. If (1) fails, continuity produces a negative density in an interior neighborhood of an adverse corner and adverse \(z\)-endpoint. Thus (1) exactly characterizes copulas, not just a sufficient subfamily.

Direct integration and substitution in \(C(1/2,1/2,1/2)\) produce
\[
\rho=\frac{\lambda[5-2(\alpha+\beta)]}{27},\qquad
\mathcal M=\frac{\lambda[3-\alpha-\beta]}{24}. \tag{5}
\]
Substitution of \(a,b\) gives \(\rho=(2a-b)/27\) and \(\mathcal M=(3a-b)/48\). From (1), every admissible triple satisfies \(|a|\le1\) and \(|b|\le1\); moreover \(a=0\) forces \(b=0\).

Conversely, given any \(a\ne0\) with \(|a|\le1\) and any \(b\) with \(|b|\le1\), choose
\[
\lambda=a,\qquad \alpha=\beta=\frac{3+b/a}{4}.
\]
Then \(\lambda[2(\alpha+\beta)-3]=b\) and the other two corner contributions both equal \(-(a+b)/2\), whose absolute value is at most one. Thus (1) holds. The point \((a,b)=(0,0)\) is realized by \(\lambda=0\), while \((0,b)\) with \(b\ne0\) cannot occur at finite parameters. This proves exact equality in (2), not merely density in its closure.

The linear map in (2) has nonzero determinant. The image of the closed square is therefore a genuine parallelogram. Fixing any \(b\in[-1,1]\) and allowing nonzero \(a\to0\) proves that each omitted diameter point is a limit of attainable pairs. Linear forms reach their extrema on square vertices, yielding (3). The common positive maximizer is \((a,b)=(1,-1)\); the common negative minimizer is \((-1,1)\). Translating the equality case back through (1) yields exactly \(\alpha+\beta=1\) with \(0\le\alpha\le1\) and the stated signs of \(\lambda\).

## Verification

The accompanying stand-alone `checker.py` uses exact symbolic differentiation and integration to verify (4), (5), the uniform margins, all four corner values, the constructive inverse for (2), and its extreme values. It also performs 160 seeded rational-parameter tests of the density inequality. Those finite tests support but do not substitute for the global bilinear-interpolation proof above. An explicit strict improvement over the article's reported sufficient range is \((\alpha,\beta)=(5,2)\): the exact range is \(|\lambda|\le1/11\), whereas its Table 2 offers only \(|\lambda|\le1/25\).

## Relationship to prior work

Chesneau (2024), Proposition 3.1 and its Equations (6)--(9), introduces exactly this second copula and gives a sufficient, non-optimal, absolute-value condition involving \(\Omega\) and \(\Xi\). Its Remark 3.2 explicitly notes that this condition is not optimal. Its Equations for the trivariate medial correlation and Spearman coefficient are precisely (5), which are acknowledged as known. The present claim is the **complete necessary-and-sufficient validity criterion and the induced exact simultaneous dependence region**, including its missing diameter and sharp jointly attained extremes. The article's first polynomial-power copula is a different object and neither derives nor implies this result.

A related paper, Chesneau (2024), *Three-Dimensional Copulas: A Generalized Convex Mixture Copulas Strategy*, studies different product Ali--Mikhail--Haq and FGM mixed families. Its accessible full text does not establish an exact phase diagram for the polynomial function (6) above. Searches for the source formula, its aliases, necessary/sufficient admissibility, vertex bounds, and the joint medial/Spearman envelope found no direct equivalent; this is an evidence-bounded priority assessment, not a guarantee of global novelty.

## Limitations

The classification applies exactly to the specified polynomial family, not to arbitrary trivariate copulas or general multivariate concordance measures. The missing diameter of the attainable image is a finite-parameter restriction; its points are limits, not non-copula limits. A source outside the inspected literature might independently contain an equivalent calculation; historical priority remains provisional. No independent mathematical audit has been performed.

## References

1. C. Chesneau, *On Two Simple, Three-Parameter, Three-Dimensional, Non-Exchangeable Copulas*, Contemporary Mathematics 5 (2024), 874--887, DOI: [10.37256/cm.5120242507](https://doi.org/10.37256/cm.5120242507). First verified public posting: 2024-02-29. Proposition 3.1, Remark 3.2, Table 2, medial and rho formulas.
2. C. Chesneau, *Three-Dimensional Copulas: A Generalized Convex Mixture Copulas Strategy*, Computational Journal of Mathematical and Statistical Sciences 3 (2024), 240--257, DOI: [10.21608/CJMSS.2024.272790.1042](https://doi.org/10.21608/CJMSS.2024.272790.1042).
3. R. B. Nelsen, *An Introduction to Copulas*, 2nd ed., Springer (2006), DOI: [10.1007/0-387-28678-0](https://doi.org/10.1007/0-387-28678-0).
