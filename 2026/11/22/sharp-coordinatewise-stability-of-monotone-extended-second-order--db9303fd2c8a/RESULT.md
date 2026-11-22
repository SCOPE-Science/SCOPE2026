# Sharp coordinatewise stability of monotone extended second-order-cone projection

## Finding
For integers \(p,q\ge1\), consider the monotone extended second-order cone
\[
C_{p,q}=\{(x,u)\in\mathbb R^p\times\mathbb R^q:x_1\ge\cdots\ge x_p\ge\|u\|_2\}.
\]
Let \(P_{p,q}\) be its **Euclidean** nearest-point projector, with input and output perturbations measured in the coordinate maximum norm. For \(q\ge2\), put
\[
G_q=\max_{0\le a\le1}\left[a-a^2+\sqrt{q-1}\,a\sqrt{1-a^2}\right].
\]
Then the exact all-input Lipschitz coefficient is
\[
\boxed{\operatorname{Lip}_{\infty}(P_{p,q})=\max\left\{\frac{1+\sqrt q}{2},\ 1+\frac{p}{p+1}G_q\right\}}\quad(q\ge2),
\]
and \(\operatorname{Lip}_{\infty}(P_{p,1})=1\). The maximizer defining \(G_q\) is unique and belongs to \((0,1)\) for each \(q\ge2\). In particular, \(\operatorname{Lip}_{\infty}(P_{2,6})=17/9\). The two competing terms arise respectively from a last-coordinate pool of size two and an all-coordinate pool of size \(p+1\).

## Assumptions and scope
The scalar cone variables are ordered as displayed; \(\|u\|_2\) is the ordinary Euclidean norm. The projector is Euclidean metric projection onto a closed convex cone, although Lipschitz constants are taken in \(\ell^\infty\). The supremum is over distinct points of \(\mathbb R^{p+q}\), and may be approached infinitesimally without a distinct attaining pair. All calculations are over real vectors. No claim is made for weighted ordering, other norms, or general linear images of this cone.

## Proof
**1. Reduction to a scalar isotonic projection.** Given input \((z,w)\), write \(r=\|w\|_2\). For any fixed admissible \(x\) and \(s=\|v\|_2\), the Euclidean distance to \((z,w)\) is minimized in the radial direction \(v=sw/r\) whenever \(r>0\). It follows that \((x,s)\) is the Euclidean projection of \((z_1,\ldots,z_p,r)\) onto \(x_1\ge\cdots\ge x_p\ge s\ge0\), i.e. the ordinary nonincreasing pool-adjacent-violators (PAVA) fit followed by a nonnegativity floor. When \(r=0\), the projected spatial vector is zero by radial minimization. The PAVA representation and its active-block formulas hold piecewise affinely; pooling blocks are consecutive, and each strictly positive pooled value is the arithmetic mean of its input block.

**2. Differential row bounds.** At a differentiability point with \(r>0\) and no active-block ties, either the final \(r\) input is a singleton or is pooled with precisely \(k\) trailing scalar inputs, \(1\le k\le p\). In the singleton case, \(s=r\), the spatial component is unchanged, and all scalar output derivatives are block-averaging rows with absolute sum at most one. In a positive pooled final block, write
\[
t=s=\frac{r+\sum_{j=p-k+1}^p z_j}{k+1},\qquad n=w/r,\qquad c=t/r\in(0,1).
\]
The bound \(c\le1\) follows because a nontrivial final pool can only be formed by joining preceding data whose resulting average does not exceed the last datum \(r\). A pooled scalar output row contains \(k\) coefficients \(1/(k+1)\) and the spatial input gradient \(n/(k+1)\). Its row sum is at most \((k+\sqrt q)/(k+1)\), which for \(q\ge2\) is no greater than \((1+\sqrt q)/2\). Every non-final pool has row sum one; zero-clamped pools have row sum zero.

For spatial output \(tn\), differentiating in the pooled regime yields the \(i\)-th row entries \(n_i/(k+1)\) in each of the \(k\) pooled scalar coordinates and the spatial derivative matrix
\[
 c(I-nn^{\mathsf T})+\frac{nn^{\mathsf T}}{k+1}.
\]
Let \(a=|n_i|\in[0,1]\) and \(B=\sum_{j\ne i}|n_j|\). The absolute row sum is exactly
\[
R_i(c)=\frac{ka}{k+1}+c(1-a^2)+\frac{a^2}{k+1}+\left|c-\frac1{k+1}\right|aB.
\]
This is convex in \(c\in[0,1]\), hence is at most the greater of its two endpoint values. At \(c=0\), it equals \(a(k+a+B)/(k+1)\le(k+\|n\|_1)/(k+1)\), which is bounded by the scalar-row maximum. At \(c=1\), it equals
\[
 1+\frac{k}{k+1}a(1-a+B)\le1+\frac{k}{k+1}\left[a-a^2+\sqrt{q-1}\,a\sqrt{1-a^2}\right]
 \le1+\frac{p}{p+1}G_q.
\]
The first inequality uses Cauchy--Schwarz on the other \(q-1\) unit-vector coordinates. Therefore all Jacobian rows have absolute sum bounded by the claimed coefficient. The projection is globally Euclidean one-Lipschitz, so it is locally Lipschitz in finite-dimensional maximum norm. An essential bound on its almost-everywhere derivative gives the global maximum-norm Lipschitz bound by standard line integration, or by mollification and passage to the limit. Nondifferentiable active-set boundaries do not increase this upper bound.

**3. Sharpness.** For the scalar-row branch, choose \(r=1\), let \(n\) have \(q\) equal positive coordinates, make \(z_p<1\) close to one, and choose all other \(z_j\) strictly decreasing and above one, so only \((z_p,r)\) is pooled. The derivative row for \(x_p\) has absolute sum \((1+\sqrt q)/2\). For the spatial branch, let \(a_*\) maximize \(G_q\), choose a unit vector \(n\) with \(|n_1|=a_*\) and all other coordinate magnitudes \(\sqrt{(1-a_*^2)/(q-1)}\), take \(r=1\), and take all \(z_j=1-\delta\) for \(\delta>0\). All \(p+1\) augmented coordinates form one positive pool, with \(c=1-p\delta/(p+1)\). As \(\delta\downarrow0\), the spatial output row norm approaches \(1+pG_q/(p+1)\). Each derivative row norm is attained as a limit of difference quotients using the signs of its coefficients, proving both branches sharp.

**4. Unique optimizer and scalar exception.** For \(q\ge2\), the function \(g_q(a)=a-a^2+\sqrt{q-1}\,a\sqrt{1-a^2}\) satisfies
\[
g_q''(a)=-2+\sqrt{q-1}\,\frac{a(2a^2-3)}{(1-a^2)^{3/2}}<-2\qquad(0<a<1).
\]
Its first derivative is positive at zero and tends to negative infinity at one. Hence there is exactly one interior maximizer. For \(q=1\), the unit spatial direction has only one coordinate, so \(a=1\) and \(B=0\); both scalar and spatial Jacobian rows have sums at most one, while the projector equals the identity on the cone, giving sharp constant one. For \(p=2,q=6\), \(g_6\) has its maximum \(4/3\) at \(a=2/3\), yielding the stated value \(17/9\). \(\square\)

## Verification
The standalone `checker.py` uses numerical PAVA, SciPy scalar maximization, and randomized perturbation tests as a finite supplement to the proof. Run `python3 checker.py` with NumPy and SciPy installed. It reports 5,675 successful numerical checks over selected dimensions and near-extremizing inputs. Finite tests cannot establish the universal bound or the uniqueness of the maximizing parameter; those are the analytic steps above.

## Relationship to prior work
Ferreira, Gao and Németh (first publicly posted February 3, 2021) reduce monotone extended second-order-cone projection to isotonic PAVA. Their formulas supply the structural starting point, but the material inspected does not state a sharp maximum-coordinate sensitivity coefficient. A published Lorentz-cone result determines the corresponding case with one scalar cone coordinate (\(p=1\)); that special case is subsumed by the formula here and is not claimed as new. The contribution for \(p\ge2\) is the exact competition between the shortest and longest possible terminal pools, including the \(p/(p+1)\) sharp branch and its all-dimensional optimizer. The published work on monotone extended cones and complementarity establishes the natural object, not this perturbation theorem. Literature checks do not certify exhaustive historical originality.

## Limitations
The result is limited to standard Euclidean projection and the coordinate maximum norm for the unweighted real cone defined above. The formula computes a sharp global supremum, not the exact modulus restricted to a particular compact input set. The finite checker is illustrative. An earlier equivalent full-cone coordinatewise conditioning theorem might exist beyond the primary sources inspected; independent specialist verification remains outstanding.

## References
1. R. Ferreira, N. Gao and S. Z. Németh, *Reducing the projection onto the monotone extended second-order cone to the pool-adjacent-violators algorithm of isotonic regression*, arXiv:2102.02040 (first public version 2021-02-03), https://arxiv.org/abs/2102.02040 .
2. N. Gao, S. Z. Németh and R. Sznajder, *The Monotone Extended Second-Order Cone and Mixed Complementarity Problems*, published online 2021, https://link.springer.com/article/10.1007/s10589-021-00342-6 .
3. *Sharp coordinatewise Lipschitz transition for Euclidean Lorentz-cone projection*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-coordinatewise-lipschitz-transition-for-euclidean-lorentz--2d1b9aa4230e .
