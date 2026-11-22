# Mass-concavity characterizes monotone jumps and irreversible fusion in weighted path TV denoising

## Finding
Let \(n\ge2\), let \(m_1,\ldots,m_n>0\), and let \(a_1,\ldots,a_{n-1}>0\). Set \(a_0=a_n=0\). For every datum \(y\in\mathbb R^n\) and \(\lambda\ge0\), denote by \(x(\lambda;y)\) the unique minimizer of
\[
\frac12\sum_{j=1}^{n}m_j(x_j-y_j)^2+\lambda\sum_{j=1}^{n-1}a_j|x_{j+1}-x_j|.
\]
The following three properties are equivalent:

1. **Mass-concavity:** for every \(1\le i<n\),
   \[
   (m_i+m_{i+1})a_i\ge m_{i+1}a_{i-1}+m_i a_{i+1}.
   \]
2. **Universal edgewise shrinkage:** for every \(y\in\mathbb R^n\) and every \(1\le i<n\), the function \(\lambda\mapsto |x_{i+1}(\lambda;y)-x_i(\lambda;y)|\) is nonincreasing on \([0,\infty)\).
3. **Universal irreversible fusion:** for every datum, edge, and \(0\le\lambda_0\le\lambda_1\), equality \(x_i(\lambda_0;y)=x_{i+1}(\lambda_0;y)\) implies equality at \(\lambda_1\).

If mass-concavity fails, an arbitrarily small positive regularization can **increase** some edge jump on strictly increasing data. Moreover, for some data, two adjacent coordinates are exactly fused over a nondegenerate positive interval of regularization strengths, then **unfuse** as regularization increases. Thus the same sharp inequalities govern both pointwise jump shrinkage and the absence of pathwise splitting for all data.

In geometric language, write \(t_i=\sum_{j=1}^i m_j\) and \(t_0=0\). Property 1 says precisely that the piecewise-linear curve through \((t_i,a_i)\), \(0\le i\le n\), is concave. The condition is on **cumulative fidelity mass**, not on uniformly spaced indices.

## Assumptions and scope
All dimensions are finite, the path has \(n\ge2\) ordered real sites, fidelity masses and interior penalty weights are strictly positive, and the quadratic loss and absolute first differences have the normalization displayed above. The datum is arbitrary real, with no monotonicity assumption in the equivalence. No free boundary weights are introduced: the two exterior penalty weights are exactly zero. The theorem concerns behavior as the **common regularization scalar** \(\lambda\) increases with masses, edge weights, and datum fixed; it does not compare different data or changing weights.

## Proof
**1. Optimality and affine blocks.** Let \(q_0=q_n=0\), with \(q_i\in[-1,1]\) and \(q_i=\operatorname{sign}(x_{i+1}-x_i)\) whenever the displayed gap is nonzero. Strict convexity gives a unique minimizer, characterized by
\[
 m_j(x_j-y_j)=\lambda(a_jq_j-a_{j-1}q_{j-1}),\qquad 1\le j\le n.
\]
For any maximal constant block of the solution, with vertices \(l+1,\ldots,r\), put \(M_{l,r}=\sum_{j=l+1}^{r}m_j\) and \(\bar y_{l,r}=M_{l,r}^{-1}\sum_{j=l+1}^{r}m_j y_j\). Summing optimality over that block yields the common value
\[
 v_{l,r}=\bar y_{l,r}+\frac{\lambda}{M_{l,r}}(a_r s_r-a_l s_l),
\]
where \(s_l,s_r\in\{-1,1\}\) are the signs of the nonzero gaps at internal block boundaries; at endpoints take \(a_0s_0=a_ns_n=0\). There are finitely many signed block patterns; on each fixed pattern the solution is affine in \(\lambda\), with validity given by linear inequalities. Continuity from strong convexity therefore yields a finite continuous piecewise-affine path on each bounded parameter interval (indeed finitely many intervals globally).

**2. Concavity implies edgewise shrinkage.** Consider a parameter interval with fixed blocks and a nonzero gap at edge \(i\), whose two neighboring constant blocks have left boundary \(l\), central boundary \(i\), and right boundary \(r\). Put \(P=\sum_{j=l+1}^{i}m_j\) and \(Q=\sum_{j=i+1}^{r}m_j\), and write \(s_i=\operatorname{sign}(x_{i+1}-x_i)\). Differentiation of the two block formulas gives
\[
 \frac{d}{d\lambda}|x_{i+1}-x_i|
 =\frac{a_rs_is_r}{Q}+\frac{a_ls_is_l}{P}
       -a_i\left(\frac1P+\frac1Q\right)
 \le \frac{a_r}{Q}+\frac{a_l}{P}
       -a_i\left(\frac1P+\frac1Q\right).
\]
Mass-concavity means that the piecewise-linear \(a(t)\) is concave; because \(t_i-t_l=P\) and \(t_r-t_i=Q\), its chord inequality is
\[
 a_i\ge\frac{Q a_l+P a_r}{P+Q}.
\]
Therefore the displayed derivative is nonpositive. For any zero gap the magnitude is already zero. Applying the derivative conclusion on each affine segment and using continuity forbids any later increase, including re-emergence after a zero. This proves property 2, and property 2 immediately gives property 3.

**3. Failure of concavity produces growing jumps.** If the inequality in property 1 fails at an edge \(i\), choose strictly increasing data (for example \(y_j=j\)). For all sufficiently small \(\lambda>0\), every gap is positive, so the optimality equations explicitly give
\[
 x_j=y_j+\frac\lambda{m_j}(a_j-a_{j-1}).
\]
Consequently,
\[
 \frac d{d\lambda}(x_{i+1}-x_i)
 =\frac{a_{i+1}}{m_{i+1}}+\frac{a_{i-1}}{m_i}
   -a_i\left(\frac1{m_i}+\frac1{m_{i+1}}\right)>0.
\]
Thus property 2 fails. This proves the equivalence of properties 1 and 2.

**4. Failure also produces genuine positive-interval unfusion.** For the same failed edge write \(p=m_i\), \(q=m_{i+1}\), \(A=a_{i-1}\), \(B=a_i\), \(C=a_{i+1}\), and
\[
 c=\frac{qA+pC}{p+q}>B.
\]
Fix \(\delta>0\); choose \(y_i-y_{i+1}=\delta\), while all other adjacent data gaps are sufficiently large and positive. The adjacent gaps outside \(i\) then remain positive through the finite parameter range used next. At first, the gap at \(i\) is negative; it reaches zero at
\[
 \lambda_-=\frac{pq\delta}{(p+q)(B+c)}.
\]
While the two vertices are fused, the unique required internal subgradient is
\[
 q_i(\lambda)=\frac cB-\frac{pq\delta}{(p+q)B\lambda}.
\]
It moves monotonically from \(-1\) at \(\lambda_-\) to \(+1\) at
\[
 \lambda_+=\frac{pq\delta}{(p+q)(c-B)}>\lambda_-.
\]
For the entire closed interval \([\lambda_-,\lambda_+]\), the block equations and \(|q_i|\le1\) satisfy every KKT equation, hence the unique solution is fused there. Immediately after \(\lambda_+\), the edge is positive and its gap grows with derivative \((p+q)(c-B)/(pq)>0\). The other gaps retain their positive signs by taking their initial sizes sufficiently large (the formula depends only on finitely many fixed masses, penalties and the finite \(\lambda_+\)). This is a genuine unfusion at a positive parameter, contradicting property 3. Thus property 3 implies property 1 and the equivalence is complete.

**5. Exact three-site witness.** With three unit fidelity masses, edge penalties \((1,4)\), and datum \((1,0,100)\), the minimizer is
\[
 x(\lambda)=
 \begin{cases}
 (1-\lambda,5\lambda,100-4\lambda),&0\le\lambda\le1/6,\\
 (1/2+2\lambda,1/2+2\lambda,100-4\lambda),&1/6\le\lambda\le1/2,\\
 (1+\lambda,3\lambda,100-4\lambda),&1/2\le\lambda\le100/7,\\
 (1+\lambda,50-\lambda/2,50-\lambda/2),&100/7\le\lambda\le98/3,\\
 (101/3,101/3,101/3),&\lambda\ge98/3.
 \end{cases}
\]
All pieces match at their endpoints and satisfy the displayed KKT equations. The first two sites fuse on \([1/6,1/2]\), separate on \((1/2,98/3)\), and ultimately re-fuse. The relevant mass-concavity inequality fails: \(2\cdot1<0+4\).

## Verification
The standalone `check.py` enumerates all signed block patterns up to six vertices, reconstructs their candidate solutions and validates both primal signs and dual KKT inequalities. It checked 3,864 edge-interval comparisons on randomly generated strictly mass-concave profiles; every sampled jump magnitude was nonincreasing. It also checks the exact rational three-site witness at nine parameter values against KKT equations, including all breakpoints, and independently verifies a locally growing jump for a nonconcave profile. The checker prints a PASS line when the tests succeed. The infinite all-data equivalence is proved above, not inferred from finite experiments.

## Relationship to prior work
Tibshirani and collaborators introduced fused-lasso regularization, while the one-dimensional solution path and taut-string dual formulation have long been studied. The classic unweighted path has irreversible fusion. Bento, Furmaniak and Ray (2018) showed that arbitrary unequal edge weights can cause repeated fusion and unfusion, gave a four-site example and quadratic worst-case path complexity, and explicitly listed weight-dependent restrictions on path complexity as future work. Their dual-boundary calculations contain a related necessary condition for an unfusing event. The present statement instead gives **necessary and sufficient inequalities simultaneously for all data on every finite path with arbitrary positive fidelity masses**, and strengthens fusion persistence to monotonicity of each individual jump magnitude. It is not a reproof of the general quadratic path-complexity bound.

Condat's 2013 direct algorithm concerns the standard equal-weight quadratic 1D TV problem and does not supply this weight-design classification. A separate published mass-concavity phenomenon for weighted isotonic regression concerns perturbation stability of a different projection, not evolution with the TV regularization parameter; neither assertion implies the present pathwise statement.

## Limitations
The claim is for finite paths and quadratic diagonal-fidelity weights with **one common regularization scalar**. It does not assert contraction between two different data sets, a similar law for cyclic graphs or general graphs, nor preservation under arbitrary nonquadratic fidelity. The fact that this property is not implied by the specific inspected references is not proof that no historical equivalent exists; unindexed or inaccessible equivalents remain possible. No independent mathematical audit has been performed.

## References
1. R. Tibshirani, M. Saunders, S. Rosset, J. Zhu and K. Knight, *Sparsity and smoothness via the fused lasso*, JRSS B **67** (2005), 91–108, first public online 13 December 2004. https://doi.org/10.1111/j.1467-9868.2005.00490.x
2. J. Friedman, T. Hastie, H. Höfling and R. Tibshirani, *Pathwise coordinate optimization* (2007). https://arxiv.org/abs/0708.1485
3. L. Condat, *A direct algorithm for 1D total variation denoising*, IEEE Signal Processing Letters **20** (2013), 1054–1057. https://lcondat.github.io/publis/Condat-fast_TV-SPL-2013.pdf
4. J. Bento, R. Furmaniak and S. Ray, *On the complexity of the weighted fused lasso* (2018). https://arxiv.org/abs/1801.04987 ; open full text https://www.jbento.info/papers/1dwfl.pdf
