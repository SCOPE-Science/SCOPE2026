# Unique fixed-volume surface minimizers for weighted lecture-hall simplices

## Finding

For every integer \(n\ge2\), consider the Euclidean lecture-hall simplex
\[
P_n(s)=\{x\in\mathbb R^n:0\le x_1/s_1\le\cdots\le x_n/s_n\le1\},\qquad s_i>0.
\]
Among **all** positive weights with a prescribed positive Euclidean volume, exactly one weight profile up to common scaling minimizes ordinary Euclidean surface area. Its reciprocal weights \(y_i=1/s_i\), normalized by \(\prod_{i=1}^n y_i=1\), are the unique positive solution of the following system. Set
\[
q_1=y_1,\quad q_i=\sqrt{y_{i-1}^2+y_i^2}\ (2\le i\le n),\quad q_{n+1}=y_n,
\]
and let \(M_n=\sum_{j=1}^{n+1}q_j\). Then
\[
\boxed{\quad y_i^2\left(\frac1{q_i}+\frac1{q_{i+1}}\right)=\frac{M_n}{n}\quad(1\le i\le n),\qquad \prod_{i=1}^n y_i=1.\quad}
\]
The minimizer is reversal-symmetric, \(s_i=s_{n+1-i}\). For \(n=2\), its two weights agree. For **every** \(n\ge3\), the end weights are strictly greater than their immediate neighbors:
\[
s_1>s_2,\qquad s_n>s_{n-1}.
\]
In particular, equal weights are **never** surface-optimal for \(n\ge3\), despite defining an important standard orthoscheme. The optimal three-dimensional proportions are explicit:
\[
\boxed{\quad(s_1,s_2,s_3)=\left((\sqrt5/2)^{1/3},(\sqrt5/2)^{-2/3},(\sqrt5/2)^{1/3}\right),\quad M_3=5(2/\sqrt5)^{1/3}.\quad}
\]
The normalization is \(\prod s_i=1\). The all-dimensional sharp isoperimetric inequality, including its equality condition, is
\[
\boxed{\frac{\mathcal H^{n-1}(\partial P_n(s))}{\operatorname{Vol}_n(P_n(s))^{(n-1)/n}}\ \ge\ \frac{(n!)^{(n-1)/n}}{(n-1)!}\,M_n^*.}
\]
Here \(M_n^*\) is \(\sum q_j\) at the unique product-one solution above, and equality holds precisely at its positive scalar multiples. The previously established exact surface-area formula is credited below; the contribution here is its sharp global constrained optimization and rigorous shape classification.

## Assumptions and scope

Euclidean volume and surface measure use the standard metric in \(\mathbb R^n\), not an Ehrhart or unimodular normalization. Weights are arbitrary positive real numbers; integer weights are included but discreteness is not imposed in the optimization. \(n\ge2\) is an arbitrary integer. Write \(V_n(s)=\prod_i s_i/n!\) and \(A_n(s)=\mathcal H^{n-1}(\partial P_n(s))\). Under rescaling \(s\mapsto cs\), volume scales by \(c^n\), area by \(c^{n-1}\), and the quotient in the displayed inequality is unchanged. No global minimum is claimed under the additional constraint that all weights must be integers.

The exact area identity from prior metric-Steiner work on this family is
\[
A_n(s)=\frac{\prod_i s_i}{(n-1)!}\left(\frac1{s_1}+\frac1{s_n}+\sum_{i=1}^{n-1}\sqrt{\frac1{s_i^2}+\frac1{s_{i+1}^2}}\right).
\]
It is restated to specify geometric normalization and to make the optimization self-contained, not as a novelty claim.

## Proof

**1. The known area expression, directly recovered.** Introduce \(z_i=x_i/s_i\). The \(n+1\) barycentric coordinates of the simplex are \(z_1,z_2-z_1,\ldots,z_n-z_{n-1},1-z_n\). Their inward gradients are respectively \(y_1e_1\), \(y_ie_i-y_{i-1}e_{i-1}\) for \(2\le i\le n\), and \(-y_ne_n\). Their lengths are precisely \(q_1,\ldots,q_{n+1}\). Every facet of an \(n\)-simplex has area \(nV_n\) times the length of the opposite barycentric gradient, by the height-volume identity. Summing the \(n+1\) areas yields \(A_n=nV_n M_n\). The edge matrix of the vertices is triangular with diagonal \(s_1,\ldots,s_n\); hence \(V_n=\prod_i s_i/n!\). This proves the stated formula without presupposing any characterization of its optimizer.

**2. Existence, strict uniqueness, and first-order equations.** Normalize \(\prod_i s_i=1\), equivalently \(\prod_i y_i=1\). Put \(t_i=\log y_i\), so \(\sum_i t_i=0\). It suffices to minimize
\[
F_n(t)=e^{t_1}+e^{t_n}+\sum_{i=1}^{n-1}\sqrt{e^{2t_i}+e^{2t_{i+1}}}
\]
on that affine hyperplane. For the summand \(g(u,v)=\sqrt{e^{2u}+e^{2v}}\), set \(a=e^u,b=e^v\) and let \((h,k)\) be an arbitrary direction. Direct differentiation and weighted Cauchy--Schwarz give
\[
\frac{d^2}{d\varepsilon^2}g(u+\varepsilon h,v+\varepsilon k)\bigg|_{\varepsilon=0}
=\frac{2(a^2h^2+b^2k^2)}{\sqrt{a^2+b^2}}-
\frac{(a^2h+b^2k)^2}{(a^2+b^2)^{3/2}}
\ge\frac{a^2h^2+b^2k^2}{\sqrt{a^2+b^2}}.
\]
This is strictly positive whenever \((h,k)\ne(0,0)\). Since every coordinate occurs in at least one edge summand, \(F_n\) has positive-definite Hessian and is strictly convex. Furthermore \(F_n(t)\ge\max_i e^{t_i}\). Every unbounded sequence on \(\sum t_i=0\) has \(\max_i t_i\to+\infty\) along an unbounded subsequence; thus \(F_n\) is coercive on the hyperplane. It therefore has exactly one minimizer.

The unconstrained derivative with respect to \(t_i\) is
\[
\frac{\partial F_n}{\partial t_i}=y_i^2\left(\frac1{q_i}+\frac1{q_{i+1}}\right).
\]
Summing these derivatives yields \(F_n\), because every edge norm occurs exactly once in the sum. At the constrained minimum all derivatives are equal, necessarily to \(M_n/n\), giving the claimed finite system. Conversely, any positive product-one solution is stationary in the log hyperplane and, by strict convexity, must be the unique global minimum. This also establishes that the system has exactly one solution for every \(n\ge2\).

**3. Reversal and strict end inequalities.** The objective and product constraint are invariant under \((t_1,\ldots,t_n)\mapsto(t_n,\ldots,t_1)\). Uniqueness implies \(t_i=t_{n+1-i}\). Suppose \(n\ge3\) and \(y_1\ge y_2\). The first two stationarity derivatives would satisfy
\[
\frac{\partial F_n}{\partial t_1}-\frac{\partial F_n}{\partial t_2}
=y_1+\frac{y_1^2-y_2^2}{\sqrt{y_1^2+y_2^2}}-\frac{y_2^2}{\sqrt{y_2^2+y_3^2}}>0,
\]
since the middle term is nonnegative and the last term has magnitude less than \(y_2\le y_1\). This contradicts the equal stationarity derivatives. Thus \(y_1<y_2\), or \(s_1>s_2\). Reversal proves \(s_n>s_{n-1}\). When \(n=2\), reversal itself forces \(s_1=s_2\). The strict end inequalities show the equal-weight simplex cannot be the optimizer in any dimension \(n\ge3\).

**4. The three-dimensional exact solution and sharp constant.** For \(n=3\), reversal yields \(y_1=y_3=a\), \(y_2=b\). Write \(r=b/a>0\). The product-one constraint gives \(a=r^{-1/3}\), and the objective becomes \(F_3=2r^{-1/3}(1+\sqrt{1+r^2})\). Differentiating gives the positive critical-point equation \(2r^2-1=\sqrt{1+r^2}\). Its only positive solution satisfying the unsquared equation is \(r=\sqrt5/2\). Hence \(a=(2/\sqrt5)^{1/3}\), the claimed weight ratios and \(M_3=5a\). Strict convexity makes this the globally sharp value. For \(n=2\), the normalized optimum is \(y_1=y_2=1\), with \(M_2=2+\sqrt2\).

**5. Arbitrary prescribed volume.** The normalized minimum of \(M_n\) is \(M_n^*\). For arbitrary weights let \(g=(\prod_i s_i)^{1/n}\), so the normalized scaled weights \(s_i/g\) have product one and the corresponding sum of reciprocal-gradient lengths equals \(gM_n(s)\). Therefore \(M_n(s)\ge M_n^*/g\). Substituting into \(A_n=(\prod s_i)M_n(s)/(n-1)!\) and \(V_n=\prod s_i/n!\) proves the displayed sharp quotient inequality. Equality occurs if and only if \(s/g\) is the unique normalized optimizer.

## Verification

The standalone standard-library file `CHECK.py` calculates squared facet areas twice: from exact rational Gram determinants of actual vertices and from the formula in the proof. It verified 900 rational weight profiles in dimensions 2--5. A separate constrained projected-gradient computation checked stationarity, reversal symmetry, strict end inequalities and strict improvement over equal weights for dimensions 2--12, including the exact three-dimensional radical target to numerical tolerance. Run `python3 CHECK.py` from the directory containing this file. These tests are finite diagnostics, not substitutes for the unrestricted convexity proof.

## Relationship to prior work

McCabe Olsen's 2018 survey defines and contextualizes the lecture-hall simplex and focuses on its polyhedral/Ehrhart theory. Brändén and Solus (2019) establish algebraic and triangulation properties for the same class. Most directly, the 2026 published result *A critical exponent and universal curvature-to-surface law for power lecture-hall simplices* already establishes the **arbitrary-weight Euclidean surface-area formula** and a second Steiner-coefficient formula and asymptotics for power weights. The present theorem **does not claim those formulas or asymptotics as new**. It treats the separate global fixed-volume boundary-minimization problem, proves all-dimensional strict uniqueness, reversal and strict endpoint-length inequalities, and determines the exact three-dimensional optimizer. Searches also compared anisotropic surface minimizers for even-cycle edge polytopes and cyclic chainlink polytopes; their underlying convex bodies and optimality claims differ. Search and inspection cannot exclude all historically unindexed general orthoscheme optimization theorems.

## Limitations

The optimization is over arbitrary positive **real** weights, not over prescribed integer weights. The dimension-dependent sharp constant for \(n\ge4\) is characterized exactly and uniquely by an explicit tridiagonal nonlinear system but is not asserted to have a radical closed form. Strict end-length inequalities do not assert global monotonicity of the entire optimal weight profile. The 900 finite Gram tests and 11 numerical optimization diagnostics do not establish the infinite-dimensional-parameter claim; strict convexity and coercivity establish it. Originality is best-knowledge, not an independent historical-priority certification.

## References

1. McCabe Olsen, *Polyhedral geometry for lecture hall partitions*, arXiv:1808.06131v1, first publicly posted 2018-08-18. https://arxiv.org/abs/1808.06131
2. Petter Brändén and Liam Solus, *Some Algebraic Properties of Lecture Hall Polytopes*, arXiv:1911.12459v1, first publicly posted 2019-11-27. https://arxiv.org/abs/1911.12459
3. *A critical exponent and universal curvature-to-surface law for power lecture-hall simplices*, 2026, public record: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-critical-exponent-and-universal-curvature-to-surface-law-for-p--6acb2545362c
