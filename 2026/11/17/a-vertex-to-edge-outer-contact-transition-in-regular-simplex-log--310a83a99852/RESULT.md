# A vertex-to-edge outer-contact transition in regular-simplex log-cosh bodies

## Finding
For every integer \(N\ge4\), let \(H_N=\{x\in\mathbb R^N:\sum_i x_i=0\}\), and put
\[
 B_{N,b}=\left\{x\in H_N:\sum_{i=1}^N\log\cosh x_i\le b\right\}\qquad(b>0).
\]
These are the normalized Orlicz transition bodies associated with centered regular Euclidean \((N-1)\)-simplices. Each has a unique Euclidean minimum-volume enclosing ellipsoid, which is a centered ball. Its contact directions have a dimension-uniform, nontrivial level transition: for all sufficiently small \(b>0\), they are **exactly** the \(2N\) unit vectors obtained by permuting and negating
\[
 w_N=\left(\sqrt{\frac{N-1}{N}},-\frac1{\sqrt{N(N-1)}},\ldots,-\frac1{\sqrt{N(N-1)}}\right).
\]
For every \(b>0\), denote the set of outer contact unit directions by \(D_{N,b}\), and let \(E_N=\{(e_i-e_j)/\sqrt2:i\ne j\}\). If \(r_{N,b}\) is the enclosing-ball radius and \(\eta=N\log2/r_{N,b}\), then
\[
 \max_{u\in D_{N,b}}\operatorname{dist}_2(u,E_N)\le5\eta+\sqrt2\eta^2.
\]
In particular, \(D_{N,b}\) converges in one-sided Hausdorff distance to \(E_N\) as \(b\to\infty\); the rate is \(O_N(b^{-1})\). Therefore the set of maximum-radius directions cannot remain in the small-level vertex-normal orbit for all levels. The theorem does **not** claim a unique transition level or that all sufficiently large-level contacts are exactly in \(E_N\).

## Assumptions and scope
\(N\) is an integer at least four, the metric is Euclidean on \(H_N\), and \(b>0\). The logarithm is natural; \(\log\cosh\) is understood as its real even smooth function. The two orbit sets contain unit vectors. The exact small-level threshold is asserted to exist for each fixed \(N\), not uniformly in \(N\). An affine regular-simplex realization multiplies lengths and levels by explicit constants but does not change the intrinsic contact directions.

## Proof
Write \(f(t)=\log\cosh t\), \(S_N=H_N\cap S^{N-1}\), and \(F_r(u)=\sum_i f(ru_i)\). Since \(f\) is even and strictly increasing on the positive half-line, \(m_N(r)=\min_{u\in S_N}F_r(u)\) is continuous, strictly increasing from zero to infinity. Hence for each \(b>0\) the unique radius \(r=r_{N,b}\) with \(m_N(r)=b\) is the Euclidean circumradius of \(B_{N,b}\). The symmetric group acts irreducibly on \(H_N\) and preserves \(B_{N,b}\); uniqueness of the Löwner ellipsoid, central symmetry, and permutation invariance imply that ellipsoid is exactly the radius-\(r\) centered ball. Its contacts are \(r u\) for \(u\in\operatorname{argmin}_{S_N}F_r\).

**The small-radius quartic lemma.** For each \(N\ge4\), \(Q(u)=\sum_i u_i^4\) on \(S_N\) has precisely the \(2N\) vectors in the signed permutation orbit of \(w_N\) as its global maxima; all are nondegenerate strict maxima. To prove this, at any constrained critical point the multipliers give \(4u_i^3=\alpha+4Q(u)u_i\) for each coordinate. Hence at most three distinct coordinates occur. A coordinate of maximal absolute magnitude cannot repeat at a local maximum: the tangent perturbation \((1,-1)\) across two such coordinates has second variation \(2(12M^2-4Q)>0\), since \(Q\le M^2\). For a two-value critical point this forces one distinct value to have multiplicity one, so the vector is a signed permutation of \(w_N\). If the cubic has three distinct roots \(a<c<d\), then \(a+c+d=0\) because its quadratic coefficient is zero. For three distinct roots \(a<c<d\), the Lagrange polynomial is exactly \(4(t-a)(t-c)(t-d)\). Its derivatives at the two outer roots are strictly positive, so any repeated outer root produces a strictly positive constrained second variation along the difference of two coordinates with that value. Consequently each outer root occurs once and the middle root occurs \(N-2\) times. Then \(N>3\) and the zero-sum relation force \(c=0,d=-a\). At this two-sparse point, the tangent perturbation having values \(1,1,-2/(N-2),\ldots,-2/(N-2)\) has strictly positive second variation \(8-8/(N-2)>0\); it is a saddle. At \(w_N\), the tangent conditions give \(v_1=0\) and \(\sum_{i>1}v_i=0\), and the constrained second variation of \(Q\) equals \(-4(N-3)/(N-1)\|v\|_2^2<0\), proving nondegeneracy. Its value is \((N^2-3N+3)/(N(N-1))\).

Uniformly in \(C^2(S_N)\) as \(r\downarrow0\), the even Taylor expansion gives
\[
 F_r(u)=\frac{r^2}{2}-\frac{r^4}{12}Q(u)+O_N(r^6).
\]
Thus every global minimizer of \(F_r\) must lie near that finite orbit. Each \(w_N\) is an exact critical point for all \(r\) by permutation symmetry. The strict nondegenerate quartic Hessian remains positive for \(F_r\) on each sufficiently small fixed neighborhood for sufficiently small \(r\); consequently the only global minimizers are exactly the signed \(w_N\) orbit for all sufficiently small \(r\). This yields the small-\(b\) assertion.

**The large-radius localization.** For any \(u\in S_N\), write \(L(u)=\sum_i|u_i|\). Since the positive and negative coordinate masses each equal \(T=L/2\), and their squared masses total one, \(1\le2T^2\), with equality exactly when there is one nonzero coordinate of each sign. Therefore \(L(u)\ge\sqrt2\) with equality exactly at \(E_N\). The scalar inequalities \(|t|-\log2\le f(t)\le|t|\) show that a minimizing direction \(u\) satisfies
\[
 \sqrt2\le L(u)\le\sqrt2+\eta,\qquad \eta=\frac{N\log2}{r},
\]
by comparison with any member of \(E_N\). Define \(\delta=2T^2-1\); then \(0\le\delta\le\sqrt2\eta+\eta^2/2\). Select the largest positive coordinate \(p\) and the largest absolute negative coordinate \(q\). The total absolute mass in all other coordinates is at most \(\delta/T\): indeed \(T^2-\sum_{u_i>0}u_i^2\ge T(T-p)\), and similarly for negative coordinates, while the sum of these deficits is \(\delta\). With \(T\ge1/\sqrt2\) and \(|T-1/\sqrt2|\le\eta/2\), this gives
\[
 \left\|u-\frac{e_i-e_j}{\sqrt2}\right\|_2\le\eta+\frac{2\delta}{T}\le5\eta+\sqrt2\eta^2.
\]
Finally \(b=m_N(r)\le\sqrt2r\), so \(r\ge b/\sqrt2\), giving the claimed \(O_N(b^{-1})\) rate. The two orbit sets \(\{\pm\sigma w_N\}\) and \(E_N\) are disjoint for \(N\ge4\), forcing a change in contact directions between small and large levels.

For a centered regular \((N-1)\)-simplex \(K\) of facet height \(h\), outward unit facet normals \(\nu_i\), and equal facet areas \(A\), the covariogram transition functional from Haddad–Jiménez–Resende becomes \(Ah\sum_i f(\langle y,\nu_i\rangle/(2h))\). The linear map \(y\mapsto(\langle y,\nu_i\rangle/(2h))_i\) is a Euclidean similarity onto \(H_N\) because \(\sum\nu_i=0\) and \(\sum\nu_i\nu_i^T=(N/(N-1))I\). Hence the normalized theorem applies.

## Verification
The proof does not use numerical experiments. An accompanying standalone verifier performs 5,436 finite consistency checks of the two explicit symmetric orbits and the general \(\ell_1\) localization inequality; its finite checks are not an infinite-dimensional certification. The nonstandard quartic maximizer lemma, its nondegenerate Hessian, and all inequalities are proved above for arbitrary \(N\ge4\).

## Relationship to prior work
Haddad, Jiménez and Resende (arXiv:2610.11700v1, 2026-10-08) introduced the boundary-integral critical log-cosh transition body; they establish its existence and its projection-body limits, not the all-dimension regular-simplex contact-orbit phenomenon proved here. Prior mathematical records describe the cube/parallelotope and octahedron critical bodies, and related triangular log-cosh geometry; those have different facet-normal configurations. A prior exact real zero-sum fourth-moment inequality implies the quartic extremal value used here, but does not address the nonquadratic level-dependent Orlicz-contact transition. Originality is subject to independent priority verification.

## Limitations
No unique critical level or complete intermediate-level contact classification is claimed. The localization theorem gives inclusion near edge-normal directions, not equality to that orbit at finite large levels. The existence of a small-level threshold is nonconstructive and dimension-dependent. Independent external auditing has not been performed.

## References
1. J. Haddad, C. H. Jiménez and M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, first posted 2026-10-08, https://arxiv.org/html/2610.11700v1.
2. *Exact Euclidean distortion of zero-sum real \(\ell_4\) hyperplanes*, published-finding corpus record published-finding corpus published record 772cd27e83b1.
3. *Exact John–Löwner contact geometry of the octahedral critical Orlicz body*, published-finding corpus record published-finding corpus published record 7704ddae223b.
4. *Exact affine roundness of triangular log-cosh projection levels*, published-finding corpus record published-finding corpus published record e3865b37f90a.
