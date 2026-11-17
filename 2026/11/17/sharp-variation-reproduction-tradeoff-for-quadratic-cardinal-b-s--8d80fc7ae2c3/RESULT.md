# Sharp variation–reproduction tradeoff for quadratic cardinal B-spline quasi-interpolation

## Finding
Let \(\beta\) denote the centered cardinal quadratic B-spline and let \(a\geq0\). For every real bi-infinite sequence \(f=(f_j)_{j\in\mathbb Z}\) of finite discrete variation, define
\[
(Q_a f)(x)=\sum_{j\in\mathbb Z}\left(f_j-a(f_{j-1}-2f_j+f_{j+1})\right)\beta(x-j).
\]
Then the **exact** operator norm from discrete total variation to continuous total variation is
\[
\boxed{\quad K(a)=1+2a+\frac{2a^2}{1+3a},\qquad a\ge0.\quad}
\]
Equivalently, \(\operatorname{Var}(Q_a f-Q_a h)\le K(a)\sum_j|(f_{j+1}-h_{j+1})-(f_j-h_j)|\), with a sharp coefficient for every \(a\). A single step at any integer attains equality. In the three-point symmetric stencil family displayed above, quadratic polynomial reproduction holds if and only if \(a=1/8\); its sharp variation gain is therefore \(K(1/8)=14/11\). The positive B-spline sampling member \(a=0\) is the unique variation-nonexpansive member of this nonnegative correction family.

## Assumptions and scope
The centered quadratic spline is the nonnegative \(C^1\) function
\[
\beta(t)=\begin{cases}3/4-t^2,&|t|\le1/2,\\ (3/2-|t|)^2/2,&1/2\le|t|\le3/2,\\0,&|t|\ge3/2.\end{cases}
\]
For polynomial reproduction alone, the same locally finite formula is also defined on polynomial-growth input sequences, which need not have finite total variation. The input seminorm is \(V_d(f)=\sum_{j\in\mathbb Z}|f_j-f_{j-1}|\), and the output seminorm is classical Jordan total variation on \(\mathbb R\), equivalently \(\int_{\mathbb R}|(Q_af)'(x)|\,dx\). The finite-variation sequences need not have finite support or be summable. Constants are quotiented out in both seminorms. The sample spacing is one; a simultaneous positive rescaling of the grid does not change the stated ratio. The operator is not assumed to interpolate its sample values.

## Proof
**Spline identities.** Put \(T(t)=(1-|t|)_+\). Direct differentiation of the two pieces of \(\beta\) gives \(\beta'(t)=T(t+1/2)-T(t-1/2)\). Also, the partition-of-unity and centered moment identities hold:
\[
\sum_{j\in\mathbb Z}\beta(x-j)=1,\quad
\sum_j j\beta(x-j)=x,\quad
\sum_j j^2\beta(x-j)=x^2+1/4.
\]
They can be checked on the two half-unit subintervals between successive shifted knots, where the sums are finite polynomials. The discrete second difference annihilates constants and affine sequences and equals \(2\) on the sample sequence \(j^2\); hence \(Q_a\) reproduces constants and affine polynomials, and \(Q_a(j^2)(x)=x^2+1/4-2a\). Thus the degree-two reproduction condition is exactly \(a=1/8\).

**Sharp jump response.** Let \(H_j=\mathbf1_{\{j\ge0\}}\) and \(R_a=Q_aH\). Summation by parts using the spline derivative identity yields
\[
R_a'(x)=g_a(x):=-aT(x+3/2)+(1+2a)T(x+1/2)-aT(x-1/2).
\]
This continuous piecewise-linear function has successive values \(0,-a,1+2a,-a,0\) at \(-5/2,-3/2,-1/2,1/2,3/2\) and vanishes elsewhere. Its integral is \(1\). For \(a\ge0\), each of the two outer negative triangles has area \(a/2\). Each inner negative triangle has height \(a\), base \(a/(1+3a)\), and area \(a^2/(2(1+3a))\). The total negative integral is therefore \(a+a^2/(1+3a)\). Since the signed integral is \(1\),
\[
\int_{\mathbb R}|g_a(x)|\,dx=1+2a+\frac{2a^2}{1+3a}=K(a).
\]
This calculation also holds at \(a=0\), when the negative intervals collapse.

**All inputs and sharpness.** Every sequence of finite discrete variation has the absolutely convergent representation
\[
f_j=c+\sum_{k\le j}d_k,\qquad d_k=f_k-f_{k-1},\quad \sum_k|d_k|=V_d(f),
\]
where \(c=\lim_{j\to-\infty}f_j\). Since the stencil is finite, the spline is locally finite, and \(Q_a\) preserves constants, differentiation and absolute convergence give
\[
(Q_af)'(x)=\sum_{k\in\mathbb Z}d_k g_a(x-k).
\]
The triangle inequality and Tonelli's theorem imply \(\operatorname{Var}(Q_af)\le\sum_k|d_k|\,\|g_a\|_{L^1}=K(a)V_d(f)\). Choosing \(f=H\) gives equality, so no smaller coefficient is possible. Applying this to \(f-h\) proves the two-input assertion. Finally \(K(0)=1\) and \(K(a)>1\) for every \(a>0\), establishing the nonexpansive classification.

## Verification
The standalone program `verify_quadratic_bv.py` uses Python's standard-library exact rational arithmetic. Run `python3 verify_quadratic_bv.py`. It checks the spline derivative and cardinal moments at rational sites, the exact step norm for six correction strengths, the special value \(14/11\), 960 nontrivial rational multi-jump inequalities and 18 translated sharp step witnesses. The computation checks finite examples and identities; the infinite-sequence theorem is proved above by the absolute-convergence argument and exact triangular integration.

## Relationship to prior work
Quadratic spline quasi-interpolants and polynomial reproduction are classical. Sablonnière's April and December 2005 manuscripts develop bounded-interval quadratic spline quasi-interpolation, including the exact interior three-tap coefficients, uniform-grid maximum-norm estimates and quadrature applications. Dũng's 2010 work studies B-spline quasi-interpolant representations and sampling recovery of mixed-smoothness functions. Classical variation-diminishing spline approximation explains the \(a=0\) baseline. These results motivate the operator, but the sharp \(V_d\)-to-variation tradeoff \(K(a)\), its exact \(14/11\) quadratic-reproducing specialization and step extremizers are the claim here. The present theorem is on the bi-infinite uniform grid, not the boundary-modified finite-interval formulas.

## Limitations
The formula assumes the centered quadratic cardinal B-spline, the stated symmetric three-sample correction and \(a\ge0\). It does not characterize arbitrary higher-order splines, boundary treatments, nonlinear limiters, variable knot spacings or higher-dimensional variation. The 2005-04-01 first-public date is for the earliest day-verified preprint defining the same interior coefficient stencil located here; its author cites related work from 2003 whose first-public day was not established. The relevant historical literature may contain an unindexed equivalent exact BV formula.

## References
1. P. Sablonnière, *Univariate spline quasi-interpolants and applications to numerical analysis*, public preprint dated 2005-04-01, https://arxiv.org/abs/math/0504022. Section 3.1 supplies the interior coefficients \(\mu_j(f)=(-f_{j-1}+10f_j-f_{j+1})/8\).
2. P. Sablonnière, *A quadrature formula associated with a univariate quadratic spline quasi-interpolant*, public preprint dated 2005-12-19, https://arxiv.org/abs/math/0512439. Sections 2–3 on the discrete quasi-interpolant and uniform grids.
3. D. Dũng, *B-spline quasi-interpolant representations and sampling recovery of functions with mixed smoothness*, public preprint dated 2010-09-22, https://arxiv.org/abs/1009.4389. Section 2, formula (2.2) and the reproduction framework.
4. M. J. Marsden, *A Voronovskaya theorem for variation-diminishing spline approximation*, Canadian Journal of Mathematics 38 (1986), 1081–1093, https://doi.org/10.4153/CJM-1986-053-0. Background for positive variation-diminishing spline approximation; only abstract/metadata was available for this comparison.
