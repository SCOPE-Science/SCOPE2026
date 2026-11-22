# Three is the sharp maximum number of hazard turning points in the Chen–Perks lifetime family

## Finding
Consider the Chen–Perks hazard introduced by Méndez-González, Rodríguez-Picón, Rodríguez Borbón and Sohn (2023):
\[
h(x)=\beta\theta x^{\theta-1}\exp(x^\theta)+\frac{\alpha\lambda\exp(\lambda x)}{1+\alpha\exp(\lambda x)},\qquad x>0,
\]
with \(\alpha,\beta,\lambda,\theta>0\). Its number of **distinct interior stationary ages** (zeros of \(h'(x)\)) obeys the following sharp structural theorem.

1. If \(\theta\ge1\), the hazard is strictly increasing everywhere.
2. If \(0<\theta<1\), the hazard has **at least one and at most three** distinct interior stationary ages. In the generic (simple-root) case the number is one or three; the hazard initially decreases and eventually increases. Whenever three are present, their successive signs are decreasing, increasing, decreasing, increasing.
3. For **every** \(0<\theta<1\), there exist strictly positive \(\alpha,\beta,\lambda\) for which there are exactly three stationary ages. Indeed a nonempty open set of parameters has this property. Thus the universal bound three cannot be reduced, even at a fixed shape \(\theta\).

An explicit rational witness is \(\theta=1/5\), \(\beta=2\), \(\alpha=\lambda=1/100\). In this instance exactly three stationary ages occur, numerically near \(444.7749243139\), \(717.8834042860\), and \(986.5093765684\). The interval-sign certificate in `check.py` proves the three changes without relying on these decimal approximations.

## Assumptions and scope
All four parameters are strictly positive and the support is \((0,\infty)\). The underlying lifetime law is proper because its survival is
\[
S(x)=\frac{1+\alpha}{1+\alpha e^{\lambda x}}\exp\{-\beta(e^{x^\theta}-1)\},
\]
which decreases continuously from one to zero. A stationary age means a **distinct positive zero of the ordinary derivative** of the hazard; this is not a statement about the number of modes of the density or about arbitrary mixtures of lifetimes. Root multiplicities may create degenerate tangencies; only the generic classification asserts that the sign changes at each stationary age.

## Proof
For \(\theta\ge1\) differentiation of both positive hazard components gives strictly positive derivatives (including \(\theta=1\)). Now fix \(a=\theta\in(0,1)\), write \(A=1-a\), and put
\[
x_0=(A/a)^{1/a},\qquad
G(x)=a e^{x^a}x^{a-2}(A-a x^a),\qquad
Q(x)=\frac{\alpha\lambda^2e^{\lambda x}}{(1+\alpha e^{\lambda x})^2}.
\]
Then \(h'(x)=Q(x)-\beta G(x)\) on \((0,x_0)\), where \(G,Q>0\). For \(x\ge x_0\), \(h'(x)>0\). At \(x\downarrow0\), \(G(x)\to\infty\) and \(Q(x)\) remains finite, so \(h'(x)<0\) near zero. Thus at least one stationary age occurs, and all stationary ages lie in \((0,x_0)\).

The remaining task is to bound the number of intersections of \(K(x)=Q(x)/G(x)\) with a positive horizontal line. Set \(L=\log K\), \(u=\alpha e^{\lambda x}\), and
\[
R(x)=-\frac{G'(x)}{G(x)}=
\frac{2-a}{x}-a x^{a-1}+\frac{a^2x^{a-1}}{A-a x^a}.
\]
Since \(a x^a<A\), the first two terms give \(xR(x)>2-a-a x^a>1\), so \(R>0\). Direct differentiation yields
\[
L'(x)=R(x)+\lambda\frac{1-u}{1+u}
=R(x)-\lambda\tanh\!\left(\frac{\log\alpha+\lambda x}{2}\right).
\]
It follows that \(L'>0\) wherever \(u\le1\).

We prove the nonstandard curvature fact \(R''(x)>0\) throughout \((0,x_0)\). Let
\[
T(x)=\frac{x^{a-1}}{A-a x^a},\qquad
w=1-\frac{a x^a}{A}\in(0,1).
\]
Algebraic differentiation gives the identities
\[
R''(x)=\frac{(2-a)[2-aA x^a]}{x^3}+a^2T''(x),
\]
\[
x^{3-a}(A-a x^a)^3T''(x)
=A^2[2w^2-(a^2+3a)w+2a^2].
\]
The first term in \(R''\) is positive because \(aAx^a<A^2<1\). The bracketed quadratic has positive leading coefficient and discriminant \(a^2(a-1)(a+7)<0\), so \(T''>0\), whence \(R''>0\).

On the region \(u\ge1\), differentiating \(L'\) **twice** now gives
\[
(L')''(x)=R''(x)+\frac{\lambda^3}{2}\operatorname{sech}^2\!\left(\frac{\log u}{2}\right)
\tanh\!\left(\frac{\log u}{2}\right)>0.
\]
Consequently \(L'\) is strictly convex there. It is positive before this region, as noted, and tends to \(+\infty\) as \(x\uparrow x_0\) (the last term of \(R\) diverges). A strictly convex function has at most two zeros, so \(K\) changes monotonicity at most twice. Every horizontal line \(K=\beta\) therefore has at most three distinct intersections, proving the upper bound on zeros of \(h'\). This argument includes cases with tangencies and boundary values of \(u\).

To prove sharpness for **every** fixed \(a\in(0,1)\), choose \(x_1=x_0/3\), \(x_2=2x_0/3\), fix \(\beta=1\), and for each \(\lambda>0\) take \(\alpha=e^{-\lambda x_1}>0\). Then
\[
Q(x_1)=\lambda^2/4\longrightarrow\infty,
\qquad
Q(x_2)=\frac{\lambda^2e^{\lambda(x_2-x_1)}}{(1+e^{\lambda(x_2-x_1)})^2}\longrightarrow0
\]
as \(\lambda\to\infty\), whereas \(G(x_1),G(x_2)\) are fixed and strictly positive. Hence for sufficiently large \(\lambda\), the successive signs of \(h'\) at a point sufficiently near zero, \(x_1\), \(x_2\), and \(x_0\) are \(-,+,-,+\). Continuity forces at least three distinct stationary ages; the upper bound gives exactly three. Strict inequalities persist under sufficiently small perturbations of all parameters, proving the asserted nonempty open regime.

## Verification
The accompanying executable `check.py` independently differentiates the two critical rational-power identities symbolically and certifies the four alternating derivative signs in the rational witness using exact rational Taylor lower/upper bounds for each exponential, with a rigorous geometric bound on every omitted tail. It returns `PASS`. The sign checkpoints are \(x=1\), \(x=(7/2)^5\), \(x=(19/5)^5\), and \(x=(399/100)^5\). They certify \(-,+,-,+\); the general analytic upper bound, not the finite sign checks, establishes that there are exactly three zeros. Optional high-precision root locations are illustrations only.

## Relationship to prior work
Méndez-González et al. (2023) define exactly this four-parameter Chen–Perks hazard, show graphical shapes, and study reliability and estimation, but do not establish a universal stationary-age bound or attainment of three turns for each \(0<\theta<1\). The earlier pure Chen model has a monotone or classical one-minimum hazard, and the earlier additive Chen construction combines two Chen hazards rather than a Chen and a logistic-derivative Perks hazard. Other additive reliability models can have complex shapes, but those facts do not imply the stated **sharp bound for this exact formula**. Searches and closest-source comparisons are detailed in `AUDIT.json` and `REVIEW.md`.

## Limitations
The theorem counts zeros of the hazard derivative, not modes of the lifetime density. It does not provide a closed-form parameter-domain inequality separating one-turn and three-turn regimes, nor closed forms for the stationary ages. Degenerate stationary points may be tangencies. Originality is judged against identified accessible literature and mathematical records, not certified against all publications; independent audit has not occurred.

## References
- Méndez-González, L. C., Rodríguez-Picón, L. A., Rodríguez Borbón, M. I., and Sohn, H., "The Chen–Perks Distribution: Properties and Reliability Applications", *Mathematics* **11** (2023), 3001, first available 5 July 2023, https://doi.org/10.3390/math11133001.
- Méndez-González, L. C., Rodríguez-Picón, L. A., Pérez-Olguín, I. J. C., and Vidal Portilla, L. R., "An Additive Chen Distribution with Applications to Lifetime Data", *Axioms* **12** (2023), 118, https://doi.org/10.3390/axioms12020118.
- Zhang, Z. and Gui, W., "Statistical Analysis of the Lifetime Distribution with Bathtub-Shaped Hazard Function under Lagged-Effect Step-Stress Model", *Mathematics* **10** (2022), 674, https://doi.org/10.3390/math10050674.
- Rammadan, D. A. et al., "Modeling Physical and Medical Lifetime Data Using the Inverse Power Entropy Chen Distribution", *Mathematics* **13** (2025), 3743, https://doi.org/10.3390/math13233743 (related survey of Chen extensions; not a proof of this result).
