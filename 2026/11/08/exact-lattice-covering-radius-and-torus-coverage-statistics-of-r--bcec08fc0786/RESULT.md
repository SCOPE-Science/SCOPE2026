# Exact lattice covering radius and torus coverage statistics of Reeve tetrahedra

## Finding
For every integer \(q\geq1\), put
\[
R_q=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(1,1,q)\}\subset\mathbb R^3.
\]
For \(p=(x,y,z)\in\mathbb R^3\), define its entry scale under integer translates by
\[
\tau_q(p)=\inf\{t\geq0:p\in tR_q+\mathbb Z^3\}.
\]
With \(\{a\}=a-\lfloor a\rfloor\in[0,1)\), set
\[
w=\frac{\{z\}}q,\qquad u=\{x-w\},\qquad v=\{y-w\}.
\]
The *pointwise exact formula*, valid for every real \(p\), is
\[
\boxed{\tau_q(p)=w+\max(u,v)+\frac{\{q\min(u,v)\}}q.}\tag{1}
\]
Consequently the lattice covering radius with respect to \(\mathbb Z^3\) is
\[
\boxed{\mu(R_q,\mathbb Z^3)=1+\frac2q.}\tag{2}
\]
The exact fraction of a fundamental unit cube *not* covered by the unscaled integer translates \(R_q+\mathbb Z^3\) equals
\[
\boxed{\operatorname{vol}_3\{p\in[0,1)^3:\tau_q(p)>1\}=\begin{cases}
5/6,&q=1,\\[2pt]2/q-4/(3q^2),&q\geq2.
\end{cases}}\tag{3}
\]
Moreover the average pointwise entry scale is
\[
\boxed{\int_{[0,1)^3}\tau_q(p)\,dp=\frac23+\frac1q-\frac1{6q^2}.}\tag{4}
\]
For independent uniform random variables \(U,V\) on \([0,1]\), the law of \(\tau_q\) at a uniform point of the torus converges to the law of \(\max(U,V)\); the latter has cumulative distribution function \(s\mapsto s^2\) on \([0,1]\). The convergence admits an explicit coupling error bounded by \(2/q\).

## Assumptions and scope
The dimension is three, \(q\) is an arbitrary *positive integer*, the ambient lattice is exactly \(\mathbb Z^3\), and the covering radius uses *all* integer translations, not an optimized choice of lattice. The simplex \(R_q\) is full-dimensional and has Euclidean volume \(q/6\). All fractions of a fundamental domain are Lebesgue fractions; there are no randomness or general-position assumptions in (1)–(3). Formula (4) is an integral with normalized unit-cube volume. The weak limit is for \(q\to\infty\) through positive integers.

## Proof
**Reduction to a finite cyclic minimization.** Fix \(p=(x,y,z)\). Any point of \(tR_q+\mathbb Z^3\) can be written
\[
p=(n_1,n_2,n_3)+\alpha(1,0,0)+\beta(0,1,0)+\gamma(1,1,q),
\]
where \(n_i\in\mathbb Z\), \(\alpha,\beta,\gamma\geq0\), and \(\alpha+\beta+\gamma\leq t\). Necessarily \(n_3\leq z\). Write \(n_3=\lfloor z\rfloor-j\) for an integer \(j\geq0\). Then \(\gamma=w+j/q\). For this fixed \(\gamma\), the largest admissible first two lattice coordinates are \(n_1=\lfloor x-\gamma\rfloor\) and \(n_2=\lfloor y-\gamma\rfloor\). These minimize \(\alpha+\beta+\gamma\) and yield
\[
F_j=w+\frac jq+\{u-j/q\}+\{v-j/q\}.\tag{5}
\]
Replacing \(j\) by \(j+q\) raises \(F_j\) by exactly one; hence it suffices to minimize over \(j=0,\ldots,q-1\). On this range,
\[
F_j=w+u+v-\frac jq+\mathbf1_{u<j/q}+\mathbf1_{v<j/q}.\tag{6}
\]
If \(j/q>\min(u,v)\), at least one indicator is one and \(F_j>F_0\), because \(j/q<1\). Otherwise both vanish and \(F_j\) decreases as \(j\) increases. Thus a minimizing index is precisely \(j=\lfloor q\min(u,v)\rfloor\). Substitution into (6) proves (1) for *all* real points, including boundary ties.

**Sharp radius.** From (1), \(0\leq w<1/q\), \(\max(u,v)<1\), and \(0\leq\{q\min(u,v)\}<1\); therefore \(\tau_q(p)<1+2/q\) at every point. Conversely \(w\) may approach \(1/q\) from below, \(\max(u,v)\) may approach \(1\), and \(\min(u,v)\) may approach \(1/q\) from below when \(q\geq2\), or \(1\) from below when \(q=1\). These conditions can be imposed simultaneously because \((w,u,v)\) ranges independently over \([0,1/q)\times[0,1)^2\) modulo the lattice. Thus the supremum of \(\tau_q\) is \(1+2/q\). Since \(tR_q+\mathbb Z^3\) covers all space exactly when \(t\geq\sup_p\tau_q(p)\), this is the claimed covering radius.

**Mean scale.** A uniformly distributed point in \([0,1)^3\) makes \(w\), \(u\), and \(v\) independent; \(w\) is uniform on \([0,1/q)\), while \(u,v\) are uniform on \([0,1)\). Therefore \(\mathbb E w=1/(2q)\), \(\mathbb E\max(u,v)=2/3\), and, writing \(a=\min(u,v)\) with density \(2(1-a)\),
\[
\mathbb E\{qa\}=\sum_{k=0}^{q-1}\int_0^1 s\,\frac2q\left(1-\frac{k+s}{q}\right)\,ds
=\frac{3q-1}{6q}.
\]
Taking expectations in (1) gives (4).

**Exact unit-scale uncovered fraction.** With \(a=\min(u,v)\) and \(b=\max(u,v)\), the joint density of \((a,b)\) is two on \(0\leq a\leq b\leq1\). Write \(qa=k+s\), \(k\in\{0,\ldots,q-1\}\), \(s\in[0,1)\), and put \(t=qw\in[0,1)\). Condition \(\tau_q>1\) becomes \(b>1-(s+t)/q\). Integrating over \(b\) shows that the uncovered fraction is
\[
\frac2{q^2}\sum_{h=1}^{q}J_h,\qquad
J_h=\int_0^1\int_0^1\min\{s+t,h-s\}\,dt\,ds.\tag{7}
\]
The separating line \(2s+t=h\) gives by elementary integration
\[
J_1=\frac5{12},\qquad J_2=\frac{11}{12},\qquad J_h=1\quad(h\geq3).
\]
For \(q=1\), (7) equals \(5/6\). For \(q\geq2\), the sum is \(q-2+5/12+11/12=q-2/3\), giving (3).

**Limit law.** Equation (1) supplies a coupling with independent uniform \(U=u,V=v\) in which
\[
0\leq \tau_q-\max(U,V)<\frac2q.
\]
The limit in distribution follows, and \(\Pr(\max(U,V)\leq s)=s^2\) for \(0\leq s\leq1\).

## Verification
The standalone standard-library verifier `verify_reeve.py` independently minimizes (5) over all admissible cyclic third-coordinate shifts on a rational \(13\times13\times13\) grid for each \(q=1,\ldots,9\), giving 19,773 exact rational pointwise comparisons. It also computes \(J_1\), \(J_2\), and \(J_h\) for \(3\leq h\leq11\) by an independent rational polygon-clipping/integration routine, and checks the resulting coverage and moment identities. These finite tests are supplementary checks; the proof above establishes the claims for arbitrary integer \(q\) and arbitrary real points.

## Relationship to prior work
The Reeve tetrahedra are classical empty lattice simplices used to distinguish higher-dimensional lattice-point enumeration from planar Pick theory. The covering radius is a central invariant of lattice geometry. Codenotti, Freyer, and Krivokuća (2026) investigate minimal covering bodies and sharp covering-radius inequalities for planar Minkowski sums; their work motivates examining exact coverage for natural explicit three-dimensional lattice polytopes. Codenotti, Santos, and Schymura (2021/2022) develop covering-radius bounds for non-hollow lattice simplices, whereas the Reeve tetrahedra here are hollow. Lian and Xue (2026) use Reeve-type constructions for minimal covering bodies with more vertices. The accessible abstract of that paper does not state the present exact Reeve-tetrahedron pointwise formula or its torus coverage statistics; a full-text comparison remains outstanding. No claimed result follows just from the general existence or computation algorithms for a polytope's covering radius.

## Limitations
The formulas concern only \(R_q\) and its integer translates, not all empty tetrahedra, all covering lattices, arbitrary lattice simplices, or higher-dimensional Reeve analogues. The result does not classify minimal covering bodies, and the example is not asserted to optimize covering density over all lattices. The historical-priority comparison is provisional, particularly for inaccessible Reeve-related portions of Lian–Xue (2026), and an independent mathematical audit has not been performed.

## References
1. G. Codenotti, A. Freyer, and K. Krivokuća, *Minimal covering bodies and Brunn–Minkowski type inequalities for the covering radius*, arXiv:2606.14442v1, submitted 2026-06-12, https://arxiv.org/abs/2606.14442.
2. Y. Lian and F. Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584v1, submitted 2026-06-12, https://arxiv.org/abs/2606.14584.
3. G. Codenotti, F. Santos, and M. Schymura, *The covering radius and a discrete surface area for non-hollow simplices*, Discrete & Computational Geometry 67 (2022), 65–111, https://doi.org/10.1007/s00454-021-00330-3 (first online 2021-11-17).
4. J. E. Reeve, *On the volume of lattice polyhedra*, Proceedings of the London Mathematical Society 7 (1957), 378–395, https://doi.org/10.1112/plms/s3-7.1.378.
