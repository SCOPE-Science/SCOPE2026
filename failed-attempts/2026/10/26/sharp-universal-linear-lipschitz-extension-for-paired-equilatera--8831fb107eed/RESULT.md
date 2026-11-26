# Sharp universal linear Lipschitz extension for paired equilateral layers

## Finding
For every integer \(n\ge3\) and every admissible metric on \(X\sqcup Y\) consisting of matched equilateral layers, the smallest norm of a real-linear Lipschitz extension operator from functions on \(X\) to functions on \(X\sqcup Y\) is explicitly computable, simultaneously for **every nonzero real Banach target space**.

Let \(X=\{x_1,\ldots,x_n\}\), \(Y=\{y_1,\ldots,y_n\}\), with distances \(d(x_i,x_j)=1\), \(d(y_i,y_j)=s\) for distinct indices, \(d(x_i,y_i)=a\), and \(d(x_i,y_j)=b\) for distinct indices. Put \(D=(n-1)b+a\). Then the exact optimal extension norm is
\[
\Lambda_n(a,b,s)=\begin{cases}
\max\left\{1,\dfrac{n-1}{D}\right\},&a\le\dfrac{n-1}{n-2}b,\\[5pt]
\max\left\{1,\dfrac{n-2}{(n-1)b}\right\},&a\ge\dfrac{n-1}{n-2}b.
\end{cases}
\]
The two formulas agree at the threshold. In particular, **the answer is completely independent of the within-target-layer distance** \(s\), as long as the distances form a metric.

An optimal, positive, constant-preserving extension is given by \((Ef)(x_i)=f(x_i)\), and
\[
(Ef)(y_i)=\begin{cases}
\dfrac{\big((n-1)b-(n-2)a\big)f(x_i)+a\sum_{j\ne i}f(x_j)}{(n-1)b+a},& a\le\dfrac{n-1}{n-2}b,\\[7pt]
\dfrac1{n-1}\sum_{j\ne i}f(x_j),&a\ge\dfrac{n-1}{n-2}b.
\end{cases}
\]
At the threshold, the coefficient on the matched source point becomes zero; further increasing \(a\) does not change the optimal kernel or the optimal norm. This is a genuine **support-loss and norm-saturation transition**.

For \(n=3\), the saturation plateau always equals one by metric feasibility. Beginning with \(n=4\), it can exceed one. For example, fixing \(n=4\), \(b=13/20\) and \(s=1\), the admissible interval \(39/40\le a\le33/20\) has the exact positive plateau \(\Lambda=40/39>1\); the optimal values at all target points omit their matched sources entirely.

## Assumptions and scope
Let \(n\ge3\) be an integer and \(a,b,s>0\) real. The displayed distances form a metric precisely when
\[
|a-b|\le\min\{1,s\},\qquad 1\le\min\{a+b,2b\},\qquad s\le\min\{a+b,2b\}.
\]
These inequalities include all triangle types; there are no unstated Euclidean-realization requirements. The operator acts on scalar-valued or real Banach-valued Lipschitz functions, with norm the least \(L\) such that \(\operatorname{Lip}(Ef)\le L\operatorname{Lip}(f)\). Equivalently, the spaces are quotiented by constants. The claim is about the infimum among **all bounded real-linear right inverses to restriction**, not merely symmetric or positive ones. For a nonzero real Banach target \(Z\), the same scalar coefficient matrix acts on \(Z\)-valued data and is simultaneously sharp.

## Proof
**1. Metric and dual norm.** There are only four kinds of triangles up to swapping layers and relabeling: those with three points in one layer, with two source points and one target, and with two target points and one source (each with matched or unmatched vertex). Their triangle inequalities are exactly those displayed above. If \(c_1,\ldots,c_n\in\mathbb R\) sum to zero, then the sharp norm of \(f\mapsto\sum_j c_jf(x_j)\) over real \(1\)-Lipschitz functions on the unit equilateral source is
\[
\frac12\sum_{j=1}^n|c_j|.
\]
Indeed, the source Lipschitz unit ball consists of real vectors of oscillation at most one. Assigning value one to indices with positive coefficients and zero to indices with negative coefficients achieves the bound. The same upper bound holds for Banach-valued data: move the total positive coefficient mass to the negative coefficients at unit cost, or equivalently use a coupling between the positive and negative parts. Consequently the total-variation formula proves sharp scalar lower bounds and universal Banach-valued upper bounds for every constant-preserving coefficient matrix.

**2. Unrestricted operators reduce to one parameter.** Let \(E\) be any bounded linear extension. Constants have zero source seminorm; boundedness and restriction imply that \(E\) preserves each constant. Average \(E\) over simultaneous permutations of all matched pairs \((x_i,y_i)\). The average remains a linear extension and cannot increase its operator norm. Every such equivariant extension has
\[
(E_\theta f)(y_i)=\theta f(x_i)+(1-\theta)\overline f,
\qquad \overline f=\frac1n\sum_{j=1}^n f(x_j),\quad \theta\in\mathbb R.
\]
This reduction is valid for scalar data and gives a sharp lower bound for Banach data by composing with a norming functional on a one-dimensional subspace of the target.

**3. Exact pair-type costs.** Source–source pairs contribute exactly one. Target–target pairs contribute \(|\theta|/s\). Matched source–target pairs contribute \((n-1)|1-\theta|/(na)\). For a mismatched pair \((x_j,y_i)\) with \(i\ne j\), the zero-sum coefficient vector has coordinates
\[
\frac{n-1+\theta}{n}\text{ at }j,\quad
-\frac{1+(n-1)\theta}{n}\text{ at }i,\quad
-\frac{1-\theta}{n}\text{ at all other indices}.
\]
Its sharp norm is half the sum of these absolute values, divided by \(b\). For \(-1/(n-1)\le\theta\le1\), this simplifies to \((n-1+\theta)/(nb)\). If \(\theta<-1/(n-1)\), all the matched and mismatched pair costs weakly decrease when \(\theta\) is replaced by \(-1/(n-1)\); if \(\theta>1\), they weakly decrease when it is replaced by one. The target–target cost also decreases under these clippings. Therefore a minimizer exists within \([-1/(n-1),1]\).

**4. Two-branch minimax.** On this interval set
\[
A(\theta)=\frac{(n-1)(1-\theta)}{na},\qquad
B(\theta)=\frac{n-1+\theta}{nb}.
\]
The first term decreases and the second increases. Their intersection is
\[
\theta_0=\frac{(n-1)(b-a)}{(n-1)b+a}.
\]
It is always at most one; it is at least \(-1/(n-1)\) exactly when \(a\le(n-1)b/(n-2)\). In that case the minimum of \(\max\{A,B\}\) is \((n-1)/D\), attained at \(\theta_0\). The target–target constraint does not increase it because
\[
\frac{|\theta_0|}{s}=\frac{(n-1)|b-a|}{Ds}\le\frac{n-1}{D},
\]
using the metric inequality \(s\ge|a-b|\).

If \(a\ge(n-1)b/(n-2)\), the minimum of \(\max\{A,B\}\) is attained at \(\theta_*=-1/(n-1)\) and equals \((n-2)/((n-1)b)\). Here \(s\ge a-b\ge b/(n-2)\) ensures that \(|\theta_*|/s\) is no greater than that value. Including the inescapable source–source cost one proves the stated exact piecewise \(\Lambda\).

**5. Positivity, sharpness for all real Banach targets, and phase boundary.** Both minimizers are within \([-1/(n-1),1]\), where the coefficients in \(E_\theta\) are nonnegative and sum to one. Substitution yields the stated two positive kernels. The universal coefficient transportation bound in step 1 proves their norm is at most \(\Lambda\) for every real Banach target; scalar-valued extremal indicators give the matching lower bound. Conversely, fixing a unit vector \(z\) in any nonzero real Banach target and a norm-one functional satisfying \(\varphi(z)=1\), composition of any Banach-valued extension with scalar embedding \(f\mapsto fz\) and \(\varphi\) gives a scalar extension of no larger norm. Hence the same \(\Lambda\) is the unrestricted optimum for each nonzero real Banach target.

At \(a=(n-1)b/(n-2)\), the matched coefficient \(((n-1)b-(n-2)a)/D\) vanishes and the kernels on both sides agree. Finally, the metric condition \(b\ge1/2\) implies the plateau \((n-2)/((n-1)b)\le1\) when \(n=3\); for \(n\ge4\), choosing \(1/2<b<(n-2)/(n-1)\) and admissible \(a\) beyond the threshold produces a plateau strictly above one. For \(n=4,b=13/20,s=1\), feasibility gives \(7/20\le a\le33/20\), so the claimed positive plateau is attained throughout \(39/40\le a\le33/20\).

## Verification
An independently formulated finite-dimensional unrestricted linear program was solved for fourteen admissible rational parameter configurations, including both sides of the support-loss threshold and different admissible values of \(s\) for the same \((n,a,b)\). The numerical LP optimizes all \(n^2\) target coefficient entries simultaneously (subject only to constant preservation), not merely the equivariant family. For the analytic optimizer, an exact-rational verification checks every unordered pair and its full coefficient total-variation norm. The standalone script `checker.py` implements both checks and reports `TWINNED_METRIC_EXTENSION_EXACT_OK 14` on success. These finite checks corroborate but do not replace the infinite-parameter proof above.

## Relationship to prior work
Bruè–Di Marino–Stra [1], Theorem 4.1, give general existence and logarithmic-in-doubling bounds for linear Lipschitz extension via random projections. Their result does not give sharp norms for matched two-layer finite metrics, nor a support-loss transition. Cavagnari–Savaré–Sodini [2], Theorem 2.13, establish an equivariant **nonlinear** Lipschitz extension for Hilbert-space maps; it does not determine unrestricted linear operator norms in this Banach-valued finite metric problem. Related equilateral one-point and two-center extension classifications do not imply a complete matched \(n\)-target configuration, whose inter-target constraints require joint verification. The proof supplies that joint verification directly. Published bibliographic search has not established absolute priority for these formulas.

## Limitations
Only *linear* extensions of real Banach-valued Lipschitz data are optimized; nonlinear scalar extensions can have constant one and are a different question. The source and target layers must be matched, internally equilateral and constant on each cross-distance orbit. The theorem does not classify all nonsymmetric minimizers or extensions to general asymmetric metrics, complex-linear operators, or arbitrary target pseudometrics. Bibliographic searches cannot rule out equivalent formulas in older or less-indexed sources, and no independent mathematical audit has been performed.

## References
1. Bruè, E.; Di Marino, S.; Stra, F. *Linear Lipschitz and \(C^1\) extension operators through random projection*. arXiv:1801.07533v1 (2018-01-23). https://arxiv.org/html/1801.07533v1
2. Cavagnari, G.; Savaré, G.; Sodini, G. E. *Extension of monotone operators and Lipschitz maps invariant for a group of isometries*. arXiv:2305.04678 (2023-05-08). https://arxiv.org/abs/2305.04678
