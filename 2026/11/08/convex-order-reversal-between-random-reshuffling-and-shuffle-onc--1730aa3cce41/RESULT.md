# Convex-order reversal between random reshuffling and shuffle-once on scalar-affine epochs

## Finding
For every completed epoch \(m\ge2\), the ordering of random reshuffling (RR) and shuffle-once (SO) is determined by the **sign** of the common scalar epoch multiplier. For positive \(A\), RR has smaller convex risk; for negative \(A\), SO has smaller convex risk **for every convex test function**, not merely for squared error. The two laws coincide for \(A=0\) or \(m=1\):
\[
0<A<1:\quad X_m^{\mathrm{RR}}\preceq_{\mathrm{cx}}X_m^{\mathrm{SO}},
\qquad -1<A<0:\quad X_m^{\mathrm{SO}}\preceq_{\mathrm{cx}}X_m^{\mathrm{RR}}.
\]
This sharp sign reversal includes fixed-step stochastic gradient descent (SGD) on finite sums of isotropic, strongly convex quadratics.

## Assumptions and scope
Fix a dimension \(d\ge1\), an integer \(n\ge2\), and real-affine component maps \(T_i(x)=q_i x+c_i\) on \(\mathbb R^d\), where \(q_i\in\mathbb R\) is a scalar and \(c_i\in\mathbb R^d\). For a permutation \(\pi\) of the components, its full-epoch composition is
\[
T_{\pi(n)}\circ\cdots\circ T_{\pi(1)}(x)=Ax+B_\pi,
\qquad A=\prod_{i=1}^n q_i.
\]
The scalar coefficient \(A\) is independent of permutation. Assume \(-1<A<1\). The offset \(B\) has the distribution of \(B_\pi\) for a uniform permutation \(\pi\); because the permutation support is finite, \(B\) is bounded. Assume \(\operatorname{tr}(C)>0\), where \(C=\operatorname{Cov}(B)\), only when making strictness claims.

RR draws a fresh independent uniform permutation each epoch. SO draws one uniform permutation and reuses it in all epochs. Both start from the same deterministic vector \(x_0\). Observations are only at *completed epoch endpoints*, not individual gradient steps or randomized temporal phase. Convex order \(U\preceq_{\mathrm{cx}}V\) means that \(\mathbb E\varphi(U)\le\mathbb E\varphi(V)\) for every finite convex \(\varphi:\mathbb R^d\to\mathbb R\); the variables here have bounded support at every fixed epoch. This comparison automatically entails equal means.

## Proof
**Epoch decomposition.** Write \(B_0,B_1,\ldots\) for independent identically distributed copies of \(B\), and set \(S_m=\sum_{j=0}^{m-1}A^j=(1-A^m)/(1-A)>0\). Since the recursion is \(x\mapsto Ax+B\), the two random endpoints have laws
\[
X_m^{\mathrm{RR}}\stackrel d=A^mx_0+\sum_{j=0}^{m-1}A^jB_j,
\qquad X_m^{\mathrm{SO}}\stackrel d=A^mx_0+S_mB_0.
\]
Thus their common mean is \(A^mx_0+S_m\mathbb EB\). Translating both laws by \(A^mx_0\) and multiplying their offsets by the same positive scalar \(S_m\) does not change convex-order direction.

**Positive product.** If \(0<A<1\), the normalized coefficients \(w_j=A^j/S_m\) are positive and sum to one. Pointwise Jensen's inequality and identical distribution give, for each convex \(\varphi\),
\[
\mathbb E\varphi\!\left(\sum_{j=0}^{m-1}w_jB_j\right)
\le\sum_{j=0}^{m-1}w_j\mathbb E\varphi(B_j)
=\mathbb E\varphi(B_0).
\]
This proves RR below SO in multivariate convex order.

**Negative product.** If \(-1<A<0\) and \(m\ge2\), the alternating geometric sum satisfies \(0<S_m<1\). For even \(m\), write \(S_m=(1-|A|^m)/(1+|A|)\); for odd \(m\ge3\), write \(S_m=(1+|A|^m)/(1+|A|)<1\). Hence the first weight \(w_0=1/S_m>1\). Since \(\sum_j w_j=1\), the coefficient vector \(w\), sorted in decreasing order, majorizes \(e_1=(1,0,\ldots,0)\): every proper leading partial sum is at least one (all positive entries precede all negative entries), and total sums agree.

For any exchangeable \((B_0,\ldots,B_{m-1})\), the functional \(F(v)=\mathbb E\varphi(\sum_jv_jB_j)\) is convex and permutation-invariant in \(v\). By the finite Hardy–Littlewood–Pólya majorization principle (equivalently, by writing \(e_1\) as a convex combination of permutations of \(w\) and applying Jensen), \(F(e_1)\le F(w)\). Therefore SO is below RR in multivariate convex order. This argument does not require symmetry of the offset law or of the objective.

**Equality, strictness and limits.** For \(A=0\), both outputs equal \(B\) in law after the first epoch; at \(m=1\), both use the same single-epoch distribution. For any \(m\ge2\), the covariance matrices are
\[
\operatorname{Cov}(X_m^{\mathrm{RR}})
=C\sum_{j=0}^{m-1}A^{2j},
\quad
\operatorname{Cov}(X_m^{\mathrm{SO}})=C S_m^2.
\]
For \(A>0\), the first scalar coefficient is strictly smaller than the second, because at least two positive geometric weights contribute to the square. For \(A<0\), \(w_0>1\) forces \(\sum_jw_j^2>1\), so the inequality reverses strictly whenever \(\operatorname{tr}(C)>0\). Thus squared Euclidean risk about any deterministic point is strictly ordered; the means are identical.

Since \(B\) is bounded and \(|A|<1\), the random series \(\sum_{j\ge0}A^jB_j\) converges absolutely almost surely and in every finite moment. The SO limit is \(B/(1-A)\), and finite-epoch convex orders pass to limits on the common compact bounded-support region. Covariances converge exactly to
\[
\operatorname{Cov}(X_\infty^{\mathrm{RR}})=\frac{C}{1-A^2},
\qquad
\operatorname{Cov}(X_\infty^{\mathrm{SO}})=\frac{C}{(1-A)^2}.
\]
For nondegenerate \(C\), the stationary trace-variance ratio is \((1-A)/(1+A)\), giving a sharp reversal at \(A=0\).

**Stochastic-gradient realization.** For component functions \(f_i(x)=a_i\|x\|^2/2-\langle b_i,x\rangle+\mathrm{const}\), with \(a_i>0\), SGD with common step \(\eta>0\) has \(q_i=1-\eta a_i\) and \(c_i=\eta b_i\). The full-epoch scalar coefficient is exactly \(A=\prod_i(1-\eta a_i)\); hence the theorem applies whenever \(|A|<1\). In particular, a negative stable product is possible when an odd number of component steps overshoots its individual minimizer.

For the explicit one-dimensional instance \(f_1(x)=(x-1)^2\), \(f_2(x)=(x+1)^2/2\), \(\eta=3/4\), the two permutation offsets are \(-3/8\) and \(15/8\), and \(A=-1/8\). Thus \(\operatorname{Var}(B)=81/64\), giving stationary \(\operatorname{Var}(X^{\mathrm{RR}})=9/7\) and \(\operatorname{Var}(X^{\mathrm{SO}})=1\). The same mean is \(2/3\); for the average objective \(F=(f_1+f_2)/2\), the RR stationary expected objective exceeds SO by precisely \(3/14\).

## Verification
The accompanying standalone Python 3 program `verify.py` checks both convex-order directions via exact-rational stop-loss inequalities for all support breakpoints in one dimension; it covers six step sizes, up to seven epochs, a three-component variant, and the rational stationary witness. It passes 50 exact finite-horizon comparisons. Every infinite-horizon and arbitrary-convex-loss conclusion is proved above and does not follow from finite enumeration.

## Relationship to prior work
Safran and Shamir (arXiv:1908.00045) study performance lower bounds for random reshuffling versus single shuffling, deriving common scalar sweep products in a quadratic analysis, but do not give this all-convex-loss sign reversal. Mishchenko, Khaled and Richtárik (arXiv:2006.05988) provide rate bounds for RR and SO in a small-step regime; their sufficient stepsize bounds exclude negative component multipliers. Rajput, Lee and Papailiopoulos (arXiv:2102.09718) study arbitrary permutations and the FlipFlop variant rather than sharp epoch-endpoint convex ordering at a fixed step. Domingo-Enrich (arXiv:2206.00632), Sections 4–6, gives power-spectral covariance results for the iteration-time/phase-averaged noise model and an experimentally different RR/SO relationship; those results do not imply an epoch-endpoint all-convex-loss comparison for the exact scalar-affine component model. The central probabilistic majorization tool is classical; novelty is asserted only for the complete algorithmic sign-frontier and the strict risk reversal, not for the majorization theorem itself.

## Limitations
The analysis requires a permutation-independent *scalar* epoch multiplier and independent fresh permutation draws for RR. General noncommuting component Hessians, momentum, nonconvex component functions, correlated reshuffling across epochs, all intermediate iterations, and time-averaged stationary risks are not covered. Strictness fails when the permutation offsets coincide. Published specialist precedence for the exact convex-order specialization has not been exhaustively established; a mathematically equivalent statement could occur in more general stochastic-affine-recursion literature. The proof uses ideal exact arithmetic and exact convex functions, not empirical training guarantees.

## References
1. I. Safran and O. Shamir, *How Good is SGD with Random Shuffling?* arXiv:1908.00045, first submitted 2019-07-31. https://arxiv.org/abs/1908.00045
2. K. Mishchenko, A. Khaled and P. Richtárik, *Random Reshuffling: Simple Analysis with Vast Improvements*, arXiv:2006.05988, 2020. https://arxiv.org/abs/2006.05988
3. S. Rajput, K. Lee and D. Papailiopoulos, *Permutation-Based SGD: Is Random Optimal?*, arXiv:2102.09718, 2021. https://arxiv.org/abs/2102.09718
4. C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632, 2022. https://arxiv.org/html/2206.00632v1
5. Hardy–Littlewood–Pólya, classical majorization principle (used as a standard lemma, not claimed as new).
