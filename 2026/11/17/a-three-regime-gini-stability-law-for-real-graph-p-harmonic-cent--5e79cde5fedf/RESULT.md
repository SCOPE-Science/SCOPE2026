# A three-regime Gini stability law for real graph \(p\)-harmonic centers

## Finding
Fix an integer \(m\ge 3\) and \(1<p<\infty\). For leaf data \(a=(a_1,\ldots,a_m)\in\mathbb R^m\), define the unique real \(p\)-harmonic center \(c_p(a)\) as the minimizer of \(\sum_{i=1}^m|a_i-c|^p\). Insert it into the data to obtain \(E_p(a)=(a_1,\ldots,a_m,c_p(a))\). For every integer \(r\ge2\), define the unnormalized complete-pair Gini seminorm
\[
G_r(x)=\sum_{1\le i<j\le r}|x_i-x_j|.
\]
The exact two-input Gini Lipschitz coefficient is
\[
\boxed{\sup_{G_m(a-b)>0}\frac{G_{m+1}(E_p(a)-E_p(b))}{G_m(a-b)}
=\begin{cases}
2,&1<p<2,\\
1+2/m,&p=2,\\
1+\dfrac{m}{2(m-1)},&2<p<\infty.
\end{cases}}
\]
At \(m=2\), the coefficient is \(2\) for every \(p>1\). For \(m\ge3\), the coefficient jumps twice in the exponent parameter at \(p=2\): the limits from below and above are respectively \(2\) and \(1+m/[2(m-1)]\), whereas the value at \(2\) is \(1+2/m\). Both non-Hilbert constants are sharp as local perturbation limits.

## Assumptions and scope
The graph is an unweighted star with \(m\) distinct leaves and one unlabeled hub. The leaves carry arbitrary real values; there are no constraints beyond \(1<p<\infty\). The center is variational (not a game-theoretic normalized \(p\)-Laplacian center). Both source and target use unweighted **complete-pair** variation, not the star's edge variation, its Lipschitz seminorm, or a normalized mean difference. Constant input differences have zero variation and produce constant output differences by translation equivariance. Accordingly the displayed supremum excludes only zero-denominator pairs.

## Proof
**Step 1: a cut formula for inserting a linear barycenter.** Let \(w=(w_i)\) be nonnegative with \(\sum_iw_i=1\), and set \(A_w z=(z_1,\ldots,z_m,\sum_iw_i z_i)\). Decompose any real vector, after sorting its coordinates, into a constant plus nonnegative multiples of nested indicator cuts. The triangle inequality for the output Gini seminorm, together with the exact additivity of \(G_m\) on the nested input cuts, proves
\[
\|A_w\|_{G_m\to G_{m+1}}=1+
\max_{\varnothing\ne S\subsetneq\{1,\ldots,m\}}
\frac{k+(m-2k)w(S)}{k(m-k)},
\quad k=|S|,\ w(S)=\sum_{i\in S}w_i.
\]
Indeed, for \(z=\mathbf 1_S\), the new hub value is \(w(S)\), its additional variation is \(k(1-w(S))+(m-k)w(S)\), and its original variation is \(k(m-k)\). Thus the indicator-cut bound is also attained.

**Step 2: two elementary sharp cases.** For the uniform vector \(w_i=1/m\), every nontrivial cut gives added/original variation \(2/m\). Thus \(\|A_w\|=1+2/m\). More generally, if every \(w_i\le1/2\), singleton and complementary singleton cuts contribute at most \(m/[2(m-1)]\). For a cut with both \(k\ge2\) and \(m-k\ge2\), its added variation is at most \(\max\{k,m-k\}\), giving ratio at most \(1/\min\{k,m-k\}\le1/2\). Therefore
\[
\|A_w\|\le1+\frac{m}{2(m-1)}.
\]
Equality holds for \(w=(1/2,1/2,0,\ldots,0)\), by choosing \(S=\{1\}\). Without the restriction \(w_i\le1/2\), the upper bound \(\|A_w\|\le2\) holds: every hub average lies between the minimum and maximum entries, and its added complete-pair variation is at most the original complete-pair variation.

**Step 3: the \(p\)-center derivative.** Its defining balance equation is
\[
F(c,a)=\sum_i(c-a_i)|c-a_i|^{p-2}=0.
\]
When \(p>2\) and \(a\) is nonconstant, implicit differentiation gives
\[
D c_p(a)[z]=\sum_i w_i z_i,\qquad
w_i=\frac{|c_p(a)-a_i|^{p-2}}{\sum_j|c_p(a)-a_j|^{p-2}}.
\]
The same formula holds at nonzero residuals for \(1<p<2\). For \(p>2\), write \(q=p-1\) and \(\alpha=(p-2)/(p-1)\in(0,1)\). The balance equation says the \(q\)-th power of any one nonzero residual cannot exceed the sum of \(q\)-th powers of the residuals of opposite sign. Subadditivity of the \(\alpha\)-th power implies that the derivative weight of this coordinate cannot exceed the sum of the weights of opposite-sign coordinates. Consequently **every derivative weight is at most \(1/2\)**. The same claim is true for zero residuals, whose derivative weights are zero.

The center map is monotone in every coordinate and translation-equivariant, hence globally \(1\)-Lipschitz in the sup norm. On the nonconstant data it is continuously differentiable for \(p>2\). Apply Step 2 to its Jacobian, then integrate on line segments, approximating a segment through constant vectors if needed, to obtain the global \(1+m/[2(m-1)]\) bound. Sharpness follows at \(a=(1,-1,0,\ldots,0)\): the Jacobian has weights \((1/2,1/2,0,\ldots,0)\), and perturbing the first coordinate realizes the cut ratio infinitesimally. At \(p=2\), the center is the arithmetic mean, so Step 2 gives \(1+2/m\) with exact equality for any binary nonconstant difference vector.

**Step 4: the subquadratic regime.** For arbitrary \(p>1\) and vectors \(a,b\), monotonicity and translation equivariance imply
\[
\min_i(a_i-b_i)\le c_p(a)-c_p(b)\le\max_i(a_i-b_i).
\]
For any scalar in this interval, the sum of its distances from the \(m\) input differences is at most their complete-pair Gini variation (maximize the convex sum at an endpoint; all endpoint-to-other distances already occur among the pairs). Therefore the two-input coefficient is never larger than \(2\).

For \(1<p<2\), set \(t=(m-2)^{-1/(p-1)}\) and take \(a=(0,1,-t,\ldots,-t)\). The balance equation gives \(c_p(a)=0\). Increase only the first coordinate by \(h>0\), and denote the new center by \(c_h\). Then \(0<c_h<h\). The contribution of the remaining \(m-1\) residuals to the balance equation is \(O(c_h)\) near zero, whereas the first contribution has absolute value \((h-c_h)^{p-1}\). Hence \(h-c_h=O(h^{1/(p-1)})=o(h)\). Dividing the output Gini variation of the two-input difference by its input variation \((m-1)h\) now gives the limit \(2\). This proves sharpness without claiming an attained nonconstant pair.

Finally, for two leaves the unique variational center is exactly their midpoint for every \(p>1\). Inserting that midpoint doubles the complete-pair variation, which proves the separate \(m=2\) assertion.

## Verification
A standalone checker `check_gini_pcenter.py` enumerates all indicator cuts for exact rational barycenter weights, including the uniform and two-extreme derivative weights. It tests the capped-weight bound on a rational grid, samples genuine nonlinear two-input data in all three regimes, and checks the subquadratic near-sharp perturbations. Run it with `python check_gini_pcenter.py` (Python 3, SciPy). Its finite calculations corroborate but are not used to infer the all-dimensional and all-exponent theorem.

## Relationship to prior work
Kyng, Rao, Sachdeva and Spielman (2015) study graph Lipschitz learning and the limit of finite-\(p\) graph energy minimizers; their Theorem 7 gives **supremum-norm** stability of the absolutely minimal Lipschitz extension. It does not give a complete-pair Gini two-input coefficient for finite \(p\). Marano, Navas and Quesada (2002) study convergence of finite-dimensional \(p\)-best approximants to best uniform approximants, a distinct exponent-asymptotics question. Existing graph \(p\)-harmonic extension stability statements formulated using leaf and edge **Lipschitz** seminorms also do not imply these Gini formulas: the underlying source/target seminorms and the subquadratic/superquadratic constants are different. The result is a metric-specific operator-stability classification rather than a new existence or convergence theorem for \(p\)-harmonic functions.

## Limitations
The theorem is for unweighted real stars, equal edge lengths, complete-pair Gini seminorms, and \(p>1\). It does not give weighted-star constants, general-tree constants, game-theoretic normalized \(p\)-harmonic centers, higher-dimensional values, or general graph variation. The non-Hilbert coefficients are supremal and are exhibited by infinitesimal families; no global equality classification for arbitrary finite differences is claimed. Priority cannot be guaranteed against unindexed sources or treatments that disguise the same seminorm under other terminology.

## References
1. R. Kyng, A. Rao, S. Sachdeva and D. A. Spielman, *Algorithms for Lipschitz Learning on Graphs*, Proceedings of Machine Learning Research **40** (2015), 1190–1223. Public metadata date 2015-06-26. https://proceedings.mlr.press/v40/Kyng15.html ; full text https://proceedings.mlr.press/v40/Kyng15.pdf . In particular Section 3, Theorems 7–8, and Appendix A.
2. M. Marano, J. Navas and J. M. Quesada, *Rate of convergence of the discrete Pólya algorithm from convex sets: A particular case*, Journal of Inequalities in Pure and Applied Mathematics **3** (2002), article 50; accessible full text https://studylib.net/doc/10709111/j-i-p-a .
