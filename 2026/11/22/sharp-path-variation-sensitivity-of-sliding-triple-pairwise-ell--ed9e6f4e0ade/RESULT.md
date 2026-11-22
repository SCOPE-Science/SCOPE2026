# Sharp path-variation sensitivity of sliding triple pairwise \(\ell_p\) dispersion

## Finding
For real \(1<p<\infty\), the sharp two-input path-variation Lipschitz coefficient of the sliding three-site pairwise \(\ell_p\)-dispersion filter is
\[
 K_{n,p}=2^{1/p}\begin{cases}
 0,&n=3,\\
 3/2,&n=4,\\
 5/2,&n=5,\\
 3,&n\ge6.
 \end{cases}
\]
At the two limiting exponents \(p=1,\infty\), the respective exact constants at lengths \(n=3,4,5,n\ge6\) are \((0,2,4,4)\) and \((0,1,2,2)\). In particular, despite pointwise convergence of these finite-dimensional filters as the exponent approaches either endpoint, their optimal variation coefficients have distinct one-sided limits.

## Assumptions and scope
For an integer \(n\ge3\), let \(x=(x_1,\ldots,x_n)\in\mathbb R^n\). Set
\[
 D_p(a,b,c)=\bigl(|a-b|^p+|a-c|^p+|b-c|^p\bigr)^{1/p},
 \qquad (T_{n,p}x)_i=D_p(x_i,x_{i+1},x_{i+2}),\quad 1\le i\le n-2.
\]
For any finite vector \(z\) of length \(m\ge1\), define adjacent path variation \(V_m(z)=\sum_{i=1}^{m-1}|z_{i+1}-z_i|\). We take the supremum of \(V_{n-2}(T_{n,p}x-T_{n,p}y)/V_n(x-y)\) over every pair \(x,y\in\mathbb R^n\) for which \(V_n(x-y)>0\). All windows are full and nonperiodic; the pairwise terms are unnormalized. At \(p=1\), the statistic equals twice the range of the triple, and at \(p=\infty\) it equals the range.

## Proof
**1. Gradient bounds.** Let \(1<p<\infty\) and put \(M=2^{1/p}\). Away from constant triples, \(D_p\) is differentiable. With \(\phi(t)=\operatorname{sgn}(t)|t|^{p-1}\) and \(R=D_p(a,b,c)^{p-1}\), its gradient is
\[
 (g_a,g_b,g_c)=R^{-1}\bigl(\phi(a-b)+\phi(a-c),\;-\phi(a-b)+\phi(b-c),\;-\phi(a-c)-\phi(b-c)\bigr).
\]
Every component has magnitude at most \(M\): the two terms affecting that component are controlled by Hölder's inequality against the vector of the three pairwise differences. Since the statistic is invariant under common translation, \(g_a+g_b+g_c=0\).

**2. Adjacent crossing windows.** Consider a unit step in input after edge \(k\). Only the two windows that cross this edge have nonzero directional derivatives; when both exist, write them as \(u=\partial_cD_p(a,b,c)\) and \(v=(\partial_c+\partial_d)D_p(b,c,d)=-\partial_bD_p(b,c,d)\) for four successive input values \((a,b,c,d)\). The two corresponding output derivatives are consecutive entries \((u,v)\), with zeros on both sides whenever the output vector is long enough. In all cases \(|u|,|v|\le M\).

There is a sharper *wrong-sign lemma*. If \(b<c\) and \(u<0\), then necessarily \(a>c\); with \(s=c-b>0\) and \(t=a-c>0\),
\[
 |u|=\frac{t^{p-1}-s^{p-1}}{(s^p+t^p+(s+t)^p)^{(p-1)/p}}
 \le\frac{t^{p-1}}{(2t^p)^{(p-1)/p}}=\frac M2.
\]
Similarly, \(b<c\) and \(v<0\) force \(d<b\), giving \(|v|\le M/2\) by the same calculation. Negating all four input values proves the analogous assertion with the signs reversed when \(b>c\). At \(b=c\), each existing nonzero crossing derivative has magnitude \(M/2\). Consequently, **whenever \(u\) and \(v\) have opposite signs**, \(\min\{|u|,|v|\}\le M/2\), and in every case \(|u-v|\le3M/2\).

**3. Finite-window upper estimates.** A step touching at most one output gives variation at most \(M\). For \(n=4\), the only central step has output variation \(|u-v|\le3M/2\). For \(n=5\), a central step contributes \(|u-v|+|v|\) or \(|u|+|v-u|\). If \(u,v\) have equal signs this is at most \(2M\). With opposite signs the expression is bounded by \(5M/2\), using the wrong-sign lemma. At \(n\ge6\), every step derivative has variation bounded by
\[
 |u|+|v-u|+|v|\le3M,
\]
with the same-sign case at most \(2M\) and the opposite-sign case at most \(2(M+M/2)=3M\). Missing boundary entries only decrease these estimates. These yield the asserted upper constants for all single-step directional derivatives.

For arbitrary \(x,y\), put \(h=x-y\), decompose \(h\) into its constant part and the sum of elementary steps with coefficients \(h_{k+1}-h_k\), and integrate the derivative of \(T_{n,p}(y+th)\) over \(0\le t\le1\). The map is Lipschitz and hence absolutely continuous along the segment. Its triples are differentiable for almost every parameter, except possibly triples identically constant along the segment; those have zero variation along that segment. Translation invariance removes the constant step. Integrating the single-step estimates and using the triangle inequality proves the global two-input inequality.

**4. Sharpness.** Fix a crossing edge \(k=2\) for \(n=4,5\) or \(k=3\) for \(n\ge6\). Choose the four successive baseline values around it as
\[
 (a,b,c,d)=(1,0,\varepsilon,\varepsilon),\qquad\varepsilon>0.
\]
Other input values can be chosen arbitrarily, e.g. by repeating an adjacent value. For this baseline the two crossing derivatives obey
\[
 \lim_{\varepsilon\downarrow0}u=-\frac M2,\qquad v=M.
\]
Therefore the variation of the output derivative of a unit step approaches respectively \(3M/2\), \(5M/2\), and \(3M\). At each fixed positive \(\varepsilon\) these derivatives are realized as limits of genuine quotients between the baseline and a positive-size step-perturbed signal. This proves equality of the suprema without asserting finite-pair attainment. For \(n=3\), the output has one entry and its variation is zero.

**5. Endpoint discontinuity.** For every real triple,
\[
 D_1(a,b,c)=2\bigl(\max\{a,b,c\}-\min\{a,b,c\}\bigr),\qquad
 D_\infty(a,b,c)=\max\{a,b,c\}-\min\{a,b,c\}.
\]
At any triple with a strict order, the range derivative in each coordinate belongs to \(\{-1,0,1\}\). For two crossing windows with shared middle observations \(b,c\), when \(b<c\) both directional derivatives \(u,v\) lie in \(\{0,1\}\), and when \(b>c\) both lie in \(\{-1,0\}\). Hence the sharp range coefficients are bounded by \(1\) for \(n=4\) and \(2\) for \(n\ge5\). Baselines \((1,0,\varepsilon,\varepsilon)\) with \(0<\varepsilon<1\), and a unit step through the central edge, give \(u=0,v=1\) and attain the corresponding derivative bounds; finite step perturbations sufficiently small preserve the strict order needed for equality. The stated endpoint constants follow by the factor two at \(p=1\). Since \(\lim_{p\downarrow1}M=2\) and \(\lim_{p\to\infty}M=1\), the interior sharp norms have different limits from these endpoint norms for each \(n\ge4\).

## Verification
Run the standalone script `python verify_lp_dispersion.py` with Python 3 and NumPy installed. It checks 21,000 randomly generated two-input inequalities across seven exponents and six lengths, plus 56 differentiable near-extremal step responses. Its reported success string is `CHECKS_COMPLETE 21000 LIPSCHITZ_PAIRS 56 SHARPNESS_DERIVATIVES`. These finite computations check examples and limits, not the universal inequality or originality.

## Relationship to prior work
The three-point \(p=1\) statistic is three times the usual sample Gini mean difference; the three-point \(p=2\) statistic is three times the population standard deviation. Sharp finite-length variation coefficients for these endpoint/special cases occur in related earlier findings (opaque identifiers `a89e9ca3-0f9b-487f-be6a-d2be1d31011a` and `e2ffeca0-87e4-4cab-8d56-eba50099a21e`). Those results alone give no inequalities at arbitrary nonquadratic finite exponents and no control of the nonuniform parameter limits. The present theorem's wrong-sign derivative argument establishes the continuum and the discontinuity. The 2014 studies of Gini dispersion and variance cited below focus on statistical efficiency, sampling and estimation rather than two-input path-variation stability of sliding power-dispersion filters.

## Limitations
This theorem concerns unweighted pairwise \(\ell_p\) dispersion on three-point consecutive windows and the ordinary open-path adjacent variation seminorm. It does not cover windows longer than three, arbitrary nonuniform pair weights, multidimensional neighborhoods, or cyclic boundary conditions. Sharpness for finite \(p\) is a limiting construction and finite-pair attainment is not asserted. Historical priority is not certified; unindexed sources and more general functional inequalities may contain equivalent statements. Independent mathematical review has not been performed.

## References
- C. Gerstenberger and D. Vogel, *On the efficiency of Gini's mean difference*, arXiv:1405.5027, first posted 20 May 2014. https://arxiv.org/abs/1405.5027
- A. Čiginas and D. Pumputis, *Gini's mean difference and variance as measures of finite populations scales*, arXiv:1406.2275, first posted 9 June 2014. https://arxiv.org/abs/1406.2275
