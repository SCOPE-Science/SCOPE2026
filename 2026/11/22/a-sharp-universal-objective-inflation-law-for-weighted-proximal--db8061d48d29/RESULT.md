# A sharp universal objective-inflation law for weighted proximal optimization with convex gauges

## Finding

Let \(d\ge1\), \(0<\kappa<1\), \(r>0\), and let \(H:\mathbb R^d\to[0,\infty)\) be finite, convex, positively one-homogeneous, and not identically zero. For arbitrary \(b\in\mathbb R^d\), define
\[
 f_b(x)=\tfrac12\|x-b\|_2^2+\tfrac r2\|x\|_2^2+H(x),\qquad
 F_{\kappa,b}(x)=\tfrac\kappa2\|x-b\|_2^2+\tfrac r2\|x\|_2^2+H(x).
\]
Write \(x_*\) and \(x_\kappa\) for their unique minimizers. For every \(b\ne0\), the sharp, dimension-independent comparison is
\[
 1\le \frac{f_b(x_\kappa)}{f_b(x_*)}
 \le \boxed{\frac{1+r}{r+\kappa(2-\kappa)}}.
\]
**The upper bound is attained for every fixed nonzero gauge \(H\), in every dimension, by a nonzero choice of data \(b\).** Specifically, if \(C\) is the compact dual convex set of \(H\), any point \(p\in C\) of maximal Euclidean norm gives equality for \(b=p/\kappa\). More generally, equality holds precisely when \(\kappa b\in C\) and \(\Pi_C(b)=\kappa b\). The objective-inflation coefficient therefore depends on neither the dimension nor the geometry of the individual gauge.

For the weighted proximal-gradient recurrence
\[
 x_{j+1}=\operatorname{prox}_{\beta( H+r\|\cdot\|_2^2/2)}
 \big(x_j-\kappa\beta(x_j-b)\big),\qquad 0<\beta<1/\kappa,
\]
every initial vector converges linearly to \(x_\kappa\), with Lipschitz contraction factor at most \((1-\kappa\beta)/(1+r\beta)\). Consequently the same sharp bound applies to its limiting *unweighted* objective value.

## Assumptions and scope

The Euclidean dimension is any positive integer. The gauge-like penalty \(H\) is finite everywhere, nonnegative, convex, positively homogeneous of degree one, and nonzero; symmetry, strict convexity, smoothness, separability, and coercivity of \(H\) are **not** assumed. The ridge curvature \(r>0\) is fixed. The two optimization objectives are explicitly distinguished: the iteration optimizes \(F_{\kappa,b}\), but the quality measure is \(f_b\). The comparison denominator is strictly positive whenever \(b\ne0\), because \(f_b(x)\ge r\|b\|_2^2/[2(1+r)]\). For \(b=0\) both optima vanish and no ratio is defined.

Under the strong-quasar-convexity definition in [1], the regularizer \(h(x)=H(x)+r\|x\|_2^2/2\) satisfies the global \((\kappa,\gamma)\)-condition at its unique minimizer zero with \(\gamma=r(2-\kappa)/\kappa>0\). Indeed, substituting \(h((1-t)x)=(1-t)H(x)+r(1-t)^2\|x\|^2/2\) into that definition leaves the nonnegative slack \((1-\kappa)tH(x)\). Thus this family falls within the stated quasar-convex regularizer framework, not merely an excluded zero-strong-convexity limit.

## Proof

**Dual representation.** Because \(H\) is finite convex and positively homogeneous, \(H=\sigma_C\) is the support function of the nonempty compact convex set
\[
 C=\{p\in\mathbb R^d:\langle p,x\rangle\le H(x)\ \forall x\}.
\]
Nonnegativity of \(H\) implies \(0\in C\), and \(H\not\equiv0\) implies \(C\ne\{0\}\). Set
\[
 A=1+r,\quad B=r+\kappa,\quad D=r+\kappa(2-\kappa)>0,\quad
 p=\Pi_C(\kappa b),\quad q=\kappa b-p.
\]
The projection variational inequality makes \(q\in N_C(p)\), so \(T:=\langle p,q\rangle\ge0\) (take the competitor zero). It also yields \(H(q)=\langle p,q\rangle\). Completing the square in the Fenchel dual gives the exact true optimal value
\[
 f_b(x_*)=\frac{\|b\|^2}{2}-\frac{\operatorname{dist}(b,C)^2}{2A}.
\]
The weighted minimizer is exactly \(x_\kappa=q/B\), since the weighted stationarity condition is \(0\in Bx_\kappa-\kappa b+\partial H(x_\kappa)\), and \(p\in\partial H(q/B)\).

**Sharp comparison.** Put \(P=\|p\|^2\), \(Q=\|q\|^2\), \(T=\langle p,q\rangle\ge0\). Since \(p\in C\), the preceding dual formula gives the lower bound
\[
 f_b(x_*)\ge L:=\frac{\|b\|^2}{2}-\frac{\|b-p\|^2}{2A}
 =\frac{DP+2BT+rQ}{2A\kappa^2}.
\]
Directly evaluating the original objective at \(q/B\), using \(H(q)=T\), gives
\[
 f_b(x_\kappa)=\frac{P}{2\kappa^2}
 +\frac{r+\kappa^2}{\kappa^2 B}T
 +\frac{r(r+\kappa^2)}{2\kappa^2B^2}Q.
\]
The identity
\[
 B^2-D(r+\kappa^2)=\kappa^2(1-\kappa)^2
\]
therefore supplies the **exact nonnegative slack identity**
\[
 \frac AD L-f_b(x_\kappa)
 =\frac{(1-\kappa)^2}{DB^2}\left(BT+\frac r2Q\right)\ge0.
\]
It follows that \(f_b(x_\kappa)\le(A/D)L\le(A/D)f_b(x_*)\). The lower ratio bound follows from optimality of \(x_*\).

**Equality and attainment.** Since \(r>0\), \(0<\kappa<1\), and \(Q\ge0\), equality in the slack inequality forces \(q=0\). Equality in the dual lower bound forces \(p=\Pi_C(b)\). Consequently equality is equivalent to \(\kappa b=p\in C\) and \(p=\Pi_C(b)\). For any nonzero \(C\), compactness supplies a nonzero maximizer \(p\) of \(\|\cdot\|\) on \(C\). For any \(c\in C\), the identity
\[
 2\langle p,c-p\rangle=\|c\|^2-\|p\|^2-\|c-p\|^2\le0
\]
shows \(p\in N_C(p)\). Choosing \(b=p/\kappa\) makes \(p=\Pi_C(b)=\Pi_C(\kappa b)\). All inequalities then become equalities, proving both sharpness and the equality characterization for **each** admissible penalty.

**Iterates.** With \(h(x)=H(x)+r\|x\|^2/2\), completion of the square gives
\[
 \operatorname{prox}_{\beta h}(z)=\operatorname{prox}_{\beta H/(1+r\beta)}\!\left(\frac z{1+r\beta}\right).
\]
Its global Lipschitz constant is at most \(1/(1+r\beta)\). The gradient step \(x\mapsto(1-\kappa\beta)x+\kappa\beta b\) is \((1-\kappa\beta)\)-Lipschitz for the stated range, hence their composition is a contraction. Its unique fixed point satisfies \(0\in\kappa(x-b)+\partial h(x)\) and is precisely \(x_\kappa\). Banach's theorem gives the rate and convergence for every start.

## Verification

The standalone standard-library script `verify.py` uses exact rational arithmetic for 1,728 parameter instances of weighted two-coordinate \(\ell_1\) gauges, checking the dual optimum, projected decomposition, scalar objective evaluation, exact slack identity, nonnegativity, sharp inequality and an attaining datum. It passes 10,368 recorded test tallies. The algebraic identity was independently simplified symbolically for general \(r,\kappa\). Numerical or finite tests are supplementary: the argument above applies to every dimension, every admissible gauge and all real parameters in scope.

## Relationship to prior work

Brito, Lara and Yuan [1] distinguish the weighted objective \(F_\kappa=\kappa g+h\) optimized by their proximal-gradient iteration from the unweighted objective \(g+h\) used for comparison, and establish distance-to-minimizer bounds, including a scalar quadratic example demonstrating displacement (Example 3.16). They do not give the universal sharp *objective-value ratio*, an equality characterization, or its geometry-independence for gauges with ridge regularization. The current finding is not a claim about their nonconvex \(\ell_p\) theory.

The classical elastic-net paper of Zou and Hastie [2] gives explicit orthogonal-design shrinkage structure; that narrower model is included here by choosing a box dual set. Orthogonal elastic-net formulas do not supply the stated all-gauge, all-dimension sharp comparison. Balcan and coauthors [3] analyze piecewise-rational validation loss as elastic-net hyperparameters vary across instances, not the infimum-normalized within-objective ratio used here. Combettes and Pesquet [4] provide general proximal-thresholding foundations rather than this exact scale-mismatch factor. The computations here use standard convex duality and metric projection; equivalent prior formulations remain a historical priority risk.

## Limitations

This theorem requires the same isotropic quadratic data term in both objectives, a constant ridge curvature \(r>0\), and a nonnegative finite convex one-homogeneous penalty. It does not cover correlated design matrices, general nonconvex quasar-convex penalties, stochastic gradients, approximate proximal subproblem solutions, the transient unweighted objective along iterates, or statistical prediction risk. The coefficient assesses a deliberate mismatch \(\kappa<1\) between the actual optimized objective and the unweighted target; rescaling the regularizer as suggested in [1] removes this mismatch. The bound is a universal worst-case comparison, not a prediction that typical data achieve the extremizer.

## References

1. J. M. M. Brito, F. Lara and Y. Yuan, *A Proximal Gradient Method for Nonconvex Nonsmooth Optimization with Applications*, arXiv:2610.32750, first publicly submitted 2026-10-23, https://arxiv.org/abs/2610.32750.
2. H. Zou and T. Hastie, *Regularization and Variable Selection via the Elastic Net*, *Journal of the Royal Statistical Society B* **67** (2005), 301–320, https://doi.org/10.1111/j.1467-9868.2005.00503.x.
3. M.-F. Balcan, M. Khodak, D. Sharma and A. Talwalkar, *Provably Tuning the ElasticNet across Instances*, NeurIPS 2022, https://papers.nips.cc/paper_files/paper/2022/hash/b21a34c4e8dba253f05f4a5adc68ba73-Abstract-Conference.html.
4. P. L. Combettes and J.-C. Pesquet, *Proximal Thresholding Algorithm for Minimization over Orthonormal Bases* (2006), https://optimization-online.org/wp-content/uploads/2006/09/1470.pdf.
