# Sharp seven-tap fourth-difference smoothing with a sign-changing Fourier multiplier

## Finding
For real symmetric kernels \(u\) supported on \(\{-3,-2,-1,0,1,2,3\}\) and normalized by \(\sum_j u(j)=1\), put
\[
\mathcal C(u)=\sup_{0\ne f\in\ell^2(\mathbb Z)}\frac{\|\nabla^4(u*f)\|_2}{\|f\|_2},\qquad (\nabla f)(j)=f(j+1)-f(j).
\]
There is exactly one minimizing kernel \(u_*\). Set \(q(y)=y^2+a y^3+b y^4+c y^5\). The six real algebraic unknowns \((r,t,s,a,b,c)\) are characterized uniquely by \(0<r<t<s<1\) and
\[
q'(r)=q'(t)=q'(s)=0,\quad q(r)+q(t)=q(t)+q(s)=q(s)+q(1)=0.
\]
Then the exact sharp norm is
\[
\inf_u\mathcal C(u)=16q(r)\in
(0.20298508386415523565,\ 0.20298508386415523872).
\]
The unique minimizer is given by the Fourier symbol
\[
\widehat u_*(\theta)=1+a y+b y^2+c y^3,\quad
 y=\sin^2(\theta/2),
\]
with the exact coefficient formulas
\[
\begin{aligned}
u_*(0)&=1+a/2+3b/8+5c/16,\\
u_*(\pm1)&=-a/4-b/4-15c/64,\\
u_*(\pm2)&=b/16+3c/32,\\
u_*(\pm3)&=-c/64.
\end{aligned}
\]
**Every one of these seven time-domain weights is strictly positive**, despite \(\widehat u_*\) taking strictly negative values. Thus even ordinary nonnegative averaging gains from allowing a sign-changing Fourier multiplier. The sharp Fourier-nonnegative benchmark for the same support is \(\frac{64}{25}\tan^2(\pi/10)=0.270266391040\ldots\), so the optimal norm is smaller by \(24.8944\ldots\%\).

## Assumptions and scope
Only symmetry, real coefficients, support radius three, and unit total mass are imposed in the minimization. Entrywise nonnegativity is a *conclusion* for the unique optimizer, not a constraint. Fourier-transform nonnegativity is not required; indeed it is violated by the minimizer. No claim is made for longer supports or different derivative orders.

## Proof
**Fourier reduction.** Write \(P(x)=u(0)+2\sum_{j=1}^3u(j)T_j(x)\). This is a polynomial of degree at most three satisfying \(P(1)=1\), and conversely every such polynomial determines a unique eligible symmetric kernel. Fourier–Plancherel and \(|e^{i\theta}-1|^4=16\sin^4(\theta/2)\) give
\[
\mathcal C(u)=16\max_{0\le y\le1}|y^2P(1-2y)|.
\]
Every candidate is therefore \(q(y)=y^2+a y^3+b y^4+c y^5\).

**Existence, uniqueness, and alternation.** The minimum of \(\|q\|_\infty\) exists because evaluation at three distinct positive nodes controls its three variable coefficients and bounded sublevel sets are compact. The space of perturbations is \(y^3\operatorname{span}\{1,y,y^2\}\), a Haar space on every compact subinterval of \((0,1]\). Its best uniform approximation therefore has four alternating contacts: otherwise a polynomial of degree at most two whose sign switches across the at-most-two alternation boundaries would decrease the norm on the full compact extremal set. The positive initial behavior \(q(y)/y^2\to1\) and \(q'(y)>0\) for small positive \(y\) force the first contact to be a positive interior maximum. At least three extrema are interior (Rolle's theorem); since \(q'(y)/y\) has degree three, there are exactly three stationary points \(r<t<s\) in \((0,1)\), and the fourth contact is the endpoint \(1\). Their values alternate \(+M,-M,+M,-M\), giving the displayed algebraic equations. Conversely, any solution of those equations with this ordering has all three stationary points and no others on \((0,1)\); its four values of equal alternating absolute size imply global minimality. If \(q_1,q_2\) were different minimizers, their difference would be \(y^3\) times a polynomial of degree at most two. At the four alternating contacts of \(q_1\), comparison with \(q_2\) and the strictly positive dual weights below forces that difference to vanish at all four nodes; hence it is identically zero. This also proves uniqueness of the ordered algebraic solution.

**Exact dual and numerical enclosure.** For *arbitrary* \(0<x_1<x_2<x_3<x_4\le1\), put \(D_i=\prod_{j\ne i}(x_i-x_j)\) and \(\lambda_i=1/(x_i^3D_i)\). Lagrange interpolation gives
\[
\sum_i\lambda_i x_i^k=0\quad(k=3,4,5),\qquad
\sum_i\lambda_i x_i^2=-\frac1{\prod_i x_i}.
\]
Consequently every admissible \(q\) satisfies
\[
\|q\|_\infty\ge
\frac{(\prod_i x_i)^{-1}}{\sum_i|\lambda_i|}.
\]
Use the rational nodes \(x_1=0.232153505742839771\), \(x_2=0.599390549762174356\), \(x_3=0.889568489524926657\), \(x_4=1\) and rational coefficients
\[
a_0=-4.733331041291834190,\quad b_0=6.952079757871099737,\quad c_0=-3.231435284320775249.
\]
The bundled `checker.py` performs these operations in exact rational arithmetic. It isolates the three roots of \(q_0'(y)/y\) in disjoint rational intervals of width \(10^{-12}\) and bounds each true stationary value by exact Taylor remainders. This supplies the displayed strict enclosure, not merely sampled maxima. In addition, the four dual inequalities at the rational nodes bound the coefficient discrepancies \((a-a_0,b-b_0,c-c_0)\) by less than \(10^{-12}\) each, using quadratic Lagrange interpolation of the difference divided by \(y^3\).

**Positive coefficients and negative Fourier symbol.** Substituting the rational coefficient enclosures into the four Fourier coefficient formulas proves strictly positive lower bounds for \(u_*(0),u_*(\pm1),u_*(\pm2),u_*(\pm3)\). Their approximate values are \(0.2305408622055,0.2026804656179,0.1315579269619,0.0504911763175\), respectively. At the rational interior test point \(y=0.599390549762174356\), the symbol \(1+ay+by^2+cy^3\) is strictly negative, again certified by the coefficient bounds. The Fourier-nonnegative benchmark and its unique optimizer follow from Theorem 1.4 of Gaitán–Garzón–Madrid; its value exceeds the present sharp norm.

## Verification
Run `python checker.py` (standard Python only; no external libraries). Its exact-rational tests establish: the interpolation dual identity; all stationary-root sign brackets; upper/lower sharp-norm enclosures; error bounds on the true optimizer's polynomial coefficients; strict positivity of all tap weights; and a negative Fourier-symbol witness. Existence, extremal classification, and minimax uniqueness come from the preceding analytic argument, not from finite numerical sampling. The checker does not purport to certify higher tap radii or all orders.

## Relationship to prior work
Gaitán–Garzón–Madrid (first public April 28, 2026) prove a sharp fourth-difference bound with a **nonnegative Fourier transform** for all radii. Their Table 2 explicitly leaves fourth-difference optimization without that restriction open; the fixed seven-tap case here lies in that open column. Richardson's 2023 preprint solves the analogous unrestricted **second**-difference problem, not the fourth. The classical theory of Chebyshev alternation supplies the minimax principle; the seven-tap algebraic norm, positive-coefficient/negative-multiplier coexistence, and sharp quantitative comparison are the specific contribution.

## Limitations
The algebraic constant is given by an exact uniquely solvable six-equation system, not a low-degree radical expression. Decimal enclosures are derived from exact rational tests. Claims concern the unique seven-tap symmetric minimizer, not every support radius. Older approximation-theory formulations, including possible unindexed exact fixed-degree calculations, remain a bibliographic originality risk. Independent external validation has not occurred.

## References
1. J. Gaitán, C. Garzón, J. Madrid, *The smoothest average and some extremal problems for polynomials*, arXiv:2604.25074 (first public April 28, 2026), https://arxiv.org/abs/2604.25074 . Theorem 1.4, Table 2, and Section 3.
2. S. Richardson, *A Sharp Fourier Inequality and the Epanechnikov Kernel*, arXiv:2310.09713 (first public October 15, 2023), https://arxiv.org/abs/2310.09713 . Theorem 1, second-difference result.
3. C. Kravitz, S. Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev* (2021), as referenced in [1] and [2].
