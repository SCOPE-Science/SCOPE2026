# Sharp Sobolev-exponent growth of isotonic regression sensitivity

## Finding
For each integer \(n\ge 2\), let \(P_n\) denote the unweighted Euclidean projection onto the nondecreasing cone of real \(n\)-tuples. For \(1\le p\le\infty\), put \(H_p(z)=\|(z_{i+1}-z_i)_{i=1}^{n-1}\|_{\ell_p}\), and define the sharp two-input coefficient
\[
K_{n,p}=\sup_{H_p(x-y)>0}\frac{H_p(P_nx-P_ny)}{H_p(x-y)}.
\]
Writing \(a_p=1-1/p\) (with \(1/\infty=0\)), for every \(n\ge3\) and every \(p\in[1,\infty]\),
\[
\boxed{\left(\frac{n-1}{2}\right)^{a_p}\le K_{n,p}\le\left(\frac n2\right)^{a_p}.}
\]
Both inequalities are global, and the lower inequality is attained by strictly complementary local input pairs. The endpoints are exactly \(K_{n,1}=1\) and \(K_{n,\infty}=n/2\) for all \(n\ge2\); also \(K_{2,p}=1\) for every \(p\). For every \(n\ge3\) and \(p>1\), \(K_{n,p}>1\). Consequently, uniformly over all \(p\in[1,\infty]\),
\[
0\le1-\frac{K_{n,p}}{(n/2)^{a_p}}\le\frac1n,
\qquad
\lim_{n\to\infty}\frac{K_{n,p}}{n^{a_p}}=2^{-a_p}.
\]
The equality at \(p=1\) is the known bounded-variation contractivity endpoint; the main contribution here is the all-exponent, uniform-in-exponent sharp leading constant, the exact \(p=\infty\) endpoint, and the instability threshold at every \(p>1\). This is an asymptotic characterization, not a claim that either finite bound equals \(K_{n,p}\) for every intermediate exponent.

## Assumptions and scope
All inputs are real, the sampling path is \(\{1,\ldots,n\}\) with unit edge spacing, the least-squares objective is \(\frac12\sum_i(u_i-x_i)^2\), and \(P_nx\) is its unique minimizer subject to \(u_1\le\cdots\le u_n\). Gradients are forward nearest-neighbor differences without mesh rescaling. The seminorm \(H_p\) vanishes exactly on constant vectors; since \(P_n(x+c\mathbf1)=P_nx+c\mathbf1\), it defines a meaningful two-input quotient. The supremum ranges over all \(x,y\in\mathbb R^n\) with positive denominator. Finite positive \(p\), \(p=1\), and \(p=\infty\) are covered.

## Proof
**Local block averaging.** The isotonic projector is continuous and piecewise affine. On a full-dimensional strict active-set chamber, it replaces each maximal constant fitted block \(I_s=[a_s,b_s]\) by the arithmetic mean of the input on that block; its derivative \(Q\) is the corresponding block averaging matrix. Every consecutive-block partition can be realized on such a chamber by giving each proposed block strictly decreasing centered raw observations and separating the fitted block means strictly. The assertions about global norms need only the fact that these are all possible local derivatives.

Let \(D:\mathbb R^n\to\mathbb R^{n-1}\) be \((Dz)_j=z_{j+1}-z_j\). The induced derivative on gradients, \(B=DQD^{-1}\), is independent of the choice of antiderivative, because \(Q\) preserves constants. Its nonzero rows are located at boundaries \(i=b_s\) between consecutive blocks \([a_s,b_s]\) and \([b_s+1,b_{s+1}]\). Put \(m=b_s-a_s+1\) and \(\ell=b_{s+1}-b_s\). Such a row, indexed by the input gradient position \(j\), is
\[
 B_{i,j}=\begin{cases}
 (j-a_s+1)/m,&a_s\le j<b_s,\\
 1,&j=b_s,\\
 (b_{s+1}-j)/\ell,&b_s+1\le j<b_{s+1},\\
 0,&\text{otherwise}.
 \end{cases}
\]
This follows by applying block averaging to the step inputs \(z_k=\mathbf1_{k>j}\). All its entries are nonnegative. Each row sum is exactly
\[
\frac{m-1}{2}+1+\frac{\ell-1}{2}=\frac{m+\ell}{2}\le\frac n2.
\]
For each input edge internal to a block, its two possible neighboring output rows have complementary coefficients whose sum is exactly one; at an edge separating blocks, its sole nonzero coefficient is one. At an endpoint block, a contribution may have only one of the two neighbors. Therefore all column sums are at most one. If the fitted vector is constant, \(B=0\), so both estimates still hold.

**All-exponent upper bound.** For finite \(1\le p<\infty\), positivity and the weighted Hölder inequality give
\[
 |(Bg)_i|^p\le\left(\sum_jB_{i,j}\right)^{p-1}\sum_jB_{i,j}|g_j|^p.
\]
Summing the rows, invoking the bounds on the row and column sums, yields \(\|Bg\|_p\le(n/2)^{1-1/p}\|g\|_p\). For \(p=\infty\), the same conclusion follows from the maximum row sum. Following a line segment between arbitrary inputs through the finitely many affine chambers and applying the triangle inequality proves the global upper bound.

**A two-boundary attaining family.** For \(n\ge3\), let \(m=n-2\), \(M=m+3\), and construct an input \(x^0\) with \(x^0_1=-M\), \(x^0_n=M\), and \(x^0_{r+1}=m+1-2r\) for \(1\le r\le m\). Its isotonic fit has blocks of sizes \(1,m,1\) and fitted values \(-M,0,M\); each internal pooled inequality has a strictly positive dual multiplier and the two block boundaries are separated. For the ramp direction \(h_i=i-1\), all sufficiently small positive \(t\) remain in this chamber. The input gradients \(Dh\) are identically one, while \(D(Qh)\) vanishes except at the two outside edges, where it equals \((n-1)/2\). Hence
\[
\frac{H_p(P_n(x^0+th)-P_nx^0)}{H_p(th)}
=\frac{2^{1/p}(n-1)/2}{(n-1)^{1/p}}
=\left(\frac{n-1}{2}\right)^{1-1/p}.
\]
The usual conventions apply at \(p=\infty\). This proves the claimed lower inequality by actual two-input pairs, not merely by a formal face Jacobian.

**Endpoints and strict expansion.** An entirely strictly increasing input has derivative \(Q=I\), so \(K_{n,1}=1\) follows from the upper bound, and \(K_{2,p}=1\). To attain the upper \(p=\infty\) bound, use a strictly complementary two-block chamber with block lengths \(1,n-1\). Its sole nonzero gradient row has sum \(n/2\), and a ramp input direction attains that row sum. For any \(n\ge3\), the same row has an entry one at its separating edge and at least one further positive entry; as a functional on input \(\ell_p\) it has norm strictly above one whenever \(p>1\), including \(p=\infty\). Thus the complete operator is expansive for every \(p>1\).

**Uniform sharpness.** Divide the two-sided inequality by \((n/2)^{a_p}\). Since \(0\le a_p\le1\) and \((1-1/n)^{a_p}\ge1-1/n\), the claimed uniform relative error is at most \(1/n\). The sharp leading coefficient \(2^{-a_p}\) follows, with no assumption that \(p\) is held fixed as \(n\) changes.

## Verification
The companion standalone program `check_isotonic_wp.py` independently constructs every consecutive-block averaging matrix by acting on discrete unit steps, checks nonnegativity and the exact row/column norm certificates for every partition at \(2\le n\le10\), verifies local two-input witnesses for \(3\le n\le54\), and tests 2,400 random input pairs for five exponents. Its output concludes `ALL_ISOTONIC_WP_CHECKS_PASS`. Exact rational matrix enumeration corroborates the block algebra; no finite enumeration is substituted for the proof for arbitrary \(n,p\).

## Relationship to prior work
Guyader, Jégou, Németh, and Németh (2012), arXiv:1211.3930, treats finite PAVA projection, order isotonicity, and Jordan variation in iterative monotone regression; it does not state the uniform \(\ell_p\)-gradient amplification asymptotic. Németh and Németh (2015), arXiv:1503.08458, treats coordinatewise isotone projection cones rather than Sobolev perturbation moduli. Yang and Barber (2017; revised 2018), arXiv:1706.01852, characterizes whether a seminorm is nonexpansive under isotonic regression, and proves value-space \(\ell_p\) nonexpansivity; its criterion alone does not quantify the sharp divergent growth in gradient \(\ell_p\) for \(p>1\). A previously catalogued exact \(p=2\) discrete-gradient sensitivity result (identifier `fcdc0a30-e6a2-48d5-98e9-6c97f0cbfe8c`) yields the Hilbert-exponent instance but neither the all-exponent uniform asymptotic nor the \(p=\infty\) endpoint. The \(p=1\) contractivity endpoint is not claimed as new.

## Limitations
The interior finite-size constants \(K_{n,p}\) for \(1<p<\infty\) are bounded but not determined exactly in general. The theorem is for Euclidean least-squares projection on an equally spaced one-dimensional chain and unweighted first-difference seminorms; unequal data masses, arbitrary partial orders, nonlinear losses, or higher difference orders are not covered. No independent validation or claim of universal literature priority is made; possible unindexed equivalent asymptotic results remain a risk.

## References
- Guyader, A., Jégou, N., Németh, A. B., Németh, S. Z. (2012), *A Geometrical Approach to Iterative Isotone Regression*, arXiv:1211.3930, https://arxiv.org/abs/1211.3930 (first public posting 2012-11-16).
- Németh, A. B., Németh, S. Z. (2015), *Isotonic regression and isotonic projection*, arXiv:1503.08458, https://arxiv.org/abs/1503.08458.
- Yang, F., Barber, R. F. (2017), *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, https://arxiv.org/abs/1706.01852.
- Pešta, M. (2006), *Isotonic Regression in Sobolev Spaces*, Charles University, https://dspace.cuni.cz/handle/20.500.11956/4483. This concerns smooth-function Sobolev regression rather than the discrete seminorm of the output perturbation, according to the accessible abstract and conference summary; the thesis full text was inaccessible.
