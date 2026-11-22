# A second-order radius transition and contact nucleation in weighted complete-split discotopes

## Finding

Let \(a\ge2\) and \(b\ge1\) be integers. Let \(A\) and \(B\) be disjoint coordinate sets of cardinalities \(a\) and \(b\). For distinct coordinates \(i,j\), write
\[
D_{ij}=\{x e_i+y e_j:x^2+y^2\le1\}\subset\mathbb R^{a+b}.
\]
For every real \(\tau>0\), the **weighted complete-split discotope** is the centrally symmetric full-dimensional Minkowski sum
\[
K_{a,b}(\tau)=\sum_{\{i,j\}\subset A}D_{ij}
+\tau\sum_{i\in A,\ j\in B}D_{ij}.
\]
Thus the underlying graph is the join of an \(a\)-vertex clique and a \(b\)-vertex independent set, with unit clique-edge disks and radius-\(\tau\) cross-edge disks. Let \(R\) be the minimum enclosing Euclidean-ball radius. The unique center is the origin.

If \(b\ge a\), put \(s=1\) for every \(\tau>0\). If \(b<a\), set \(\lambda=a-b\) and \(\tau_c=(a-1)/(\sqrt2\lambda)\), and define
\[
s=\begin{cases}
1,&0<\tau\le\tau_c,\\
\displaystyle\frac{a(a-1)^2}{\lambda((a-1)^2+2b\lambda\tau^2)},&\tau>\tau_c.
\end{cases}
\]
The exact squared radius is
\[
\boxed{R^2=\begin{cases}
a\bigl((a-1)/\sqrt2+b\tau\bigr)^2,& b\ge a\text{ or }(b<a,\ 0<\tau\le\tau_c),\\
a^2\bigl((a-1)^2/(2(a-b))+b\tau^2\bigr),& b<a,\ \tau>\tau_c.
\end{cases}}
\]
The **complete** set of outer-sphere contacts is
\[
K_{a,b}(\tau)\cap R S^{a+b-1}=
\left\{R u:\ u_i=\varepsilon_i\sqrt{s/a}\ (i\in A),\quad
u_j=\eta_j\sqrt{(1-s)/b}\ (j\in B)\right\},
\]
where all signs can be chosen independently (and the signs \(\eta_j\) are immaterial when \(s=1\)). Hence precisely \(2^a\) points contact the sphere at and below the transition and precisely \(2^{a+b}\) contact it above. Every diametral pair is a pair of antipodal contacts, so the numbers of unordered diametral pairs are respectively \(2^{a-1}\) and \(2^{a+b-1}\).

For fixed \(b<a\), the squared radius as a function of \(\tau\) is continuously differentiable but not twice differentiable at \(\tau_c\): the right second derivative minus the left is exactly \(2ab(a-b)\). The newly activated coordinates have square-root onset,
\[
|u_j|\sim \left(\frac{2\sqrt2(a-b)}{a(a-1)}\right)^{1/2}\sqrt{\tau-\tau_c}
\quad (j\in B,\ \tau\downarrow\tau_c\text{ from above}).
\]

## Assumptions and scope

All disk summands are filled centered Euclidean disks in the indicated two-coordinate planes and all sums use the standard ambient Euclidean metric. The graph is simple and the clique and independent classes are fixed. The parameter \(\tau\) is positive; at \(\tau=0\), the body loses full dimensionality, so that endpoint is excluded. The exact geometry is asserted for every integer \(a\ge2,b\ge1\) and all real \(\tau>0\), not just the finite configurations checked computationally. The phase transition occurs only when \(b<a\). The result concerns the minimum enclosing *ball*, not the generally different minimum-volume enclosing ellipsoid.

## Proof

**1. Support and the unique center.** For \(u\in S^{a+b-1}\), Minkowski additivity of supports gives
\[
h_K(u)=\sum_{\{i,j\}\subset A}\sqrt{u_i^2+u_j^2}
+\tau\sum_{i\in A,j\in B}\sqrt{u_i^2+u_j^2}.
\tag{1}
\]
Since \(K\) is compact and centrally symmetric, its Euclidean circumradius centered at the origin is \(\max_{\|u\|=1}h_K(u)\). If \(x\in K\) has \(\|x\|=R\), then any enclosing ball with center \(c\) and radius \(r\) contains \(x\) and \(-x\); therefore \(r^2\ge (\|x-c\|^2+\|-x-c\|^2)/2=R^2+\|c\|^2\). Thus the origin is the unique optimal center.

**2. Strictly concave squared-coordinate optimization.** Set \(z_i=u_i^2\). Then \(z_i\ge0\) and \(\sum z_i=1\); conversely every such \(z\) has unit-direction lifts with arbitrary independent signs. The objective (1) is a sum of \(\sqrt{z_i+z_j}\) with strictly positive weights. It is concave. It is in fact *strictly* concave on the simplex: equality along a nontrivial segment would force \(z_i+z_j\) to be identical at its two endpoints for every clique or cross edge. Their difference would solve \(v_i+v_j=0\) on every edge. The complete-split graph is connected and contains a triangle for \(a\ge2,b\ge1\), so those equations force \(v=0\). Thus the optimizing \(z\) is unique. Permuting coordinates separately in \(A\) and \(B\) leaves (1) unchanged; uniqueness forces
\[
z_i=s/a\ (i\in A),\qquad z_j=(1-s)/b\ (j\in B)
\]
for one \(s\in[0,1]\). This reduces the exact global problem, without an assumption of symmetric optimizers, to
\[
\Phi(s)=(a-1)\sqrt{a/2}\,\sqrt{s}
+\tau\sqrt{ab}\sqrt{a+(b-a)s},\qquad 0\le s\le1.
\tag{2}
\]
Here \(\Phi'(s)\to+\infty\) as \(s\downarrow0\), and \(\Phi\) is strictly concave.

**3. Exact transition and radius.** If \(b\ge a\), both terms of (2) are nondecreasing, and the first is strictly increasing, so \(s=1\). Suppose \(b<a\), and put \(\lambda=a-b\), \(\alpha=(a-1)\sqrt{a/2}\), and \(\beta=\tau\sqrt{ab}\). Then
\[
\Phi'(1)=\frac{\sqrt a}{2}\left(\frac{a-1}{\sqrt2}-\tau\lambda\right).
\]
Strict concavity puts the maximum at \(s=1\) exactly for \(0<\tau\le\tau_c\). Above that value, it is interior and satisfies
\[
\frac{\alpha}{\sqrt{s}}=\frac{\beta\lambda}{\sqrt{a-\lambda s}},
\]
which solves uniquely to the formula for \(s\) in the finding. In the endpoint case, (2) gives the first squared-radius branch. In the interior case, Cauchy–Schwarz applied to
\[
\Phi(s)=\alpha\sqrt{s}+\beta\sqrt{a-\lambda s},
\qquad \lambda s+(a-\lambda s)=a,
\]
gives the attained maximum \(\Phi^2=a(\alpha^2/\lambda+\beta^2)\), yielding the second branch.

The two *algebraic branch expressions*, interpreted on either side of the threshold, satisfy the exact identity
\[
R_{\mathrm{interior},\mathrm{formal}}^2-R_{\mathrm{endpoint},\mathrm{formal}}^2
=ab(a-b)(\tau-\tau_c)^2.
\tag{3}
\]
Consequently the values and first derivatives match at \(\tau_c\), whereas the second derivative jumps by \(2ab(a-b)>0\). Also, for \(\tau>\tau_c\), direct rearrangement gives
\[
\frac{1-s}{b}
=\frac{2(a-b)^2\tau^2-(a-1)^2}
{(a-b)((a-1)^2+2b(a-b)\tau^2)}.
\]
Its right-hand derivative at \(\tau_c\) is \(2\sqrt2(a-b)/(a(a-1))\), proving the stated square-root contact onset.

**4. All contacts and all diameters.** For every maximizing unit direction \(u\), select an exposed point \(x\in K\) with \(u\cdot x=h_K(u)=R\). Since every point in \(K\) has norm at most \(R\), Cauchy–Schwarz forces \(x=Ru\). Conversely, a point of norm \(R\) yields the maximizing direction \(u=x/R\). Therefore outer contacts are in bijection with all maximizing unit directions. Step 2 gave a *unique vector of squared coordinates*, and sign changes preserve the objective. Precisely the sign patterns stated in the finding occur, with the indicated counts. Finally \(\operatorname{diam}(K)=2R\) by symmetry and the triangle inequality. Equality \(\|x-y\|=2R\) requires \(y=-x\) and both points outer contacts, proving the diametral-pair assertion.

## Verification

The standalone standard-library script `verify.py` checks both radius branches directly against the full edge-disk support expression, performs a dense independent one-dimensional grid check, and samples unsymmetrized simplex points in each tested configuration. Running `python verify.py` produced:

`SPLIT_DISCOTOPE_PASS cases=560 one_variable_grid=560560 full_simplex_tests=16800 max_grid_excess=1.42e-14`

A separate symbolic check confirmed equality and first-derivative matching at \(\tau_c\) and the exact second-derivative jump; independent constrained optimizations over all squared coordinates found no larger support on 210 configurations. These computations are corroboration only; Steps 1–4 prove the claim for all stated dimensions and weights.

Two exact examples at unit cross weight distinguish the phases: for \((a,b)=(4,2)\), the radius squared is \(34+24\sqrt2\), and there are \(16\) contacts; for \((a,b)=(5,2)\), \(s=20/21\), \(R^2=350/3\), and there are \(128\) contacts.

## Relationship to prior work

The works of Mathis–Meroni and Gesmundo–Meroni develop fiber bodies and the geometric/algebraic structure of discotopes. They furnish the underlying natural class, but their inspected relevant sections do not classify Euclidean outer spheres of weighted complete-split coordinate-disc sums.

Two relevant previous geometric classifications cover regular graphical discotopes (both extremal ellipsoids and contact topology), and all-graph John ellipsoids together with biregular bipartite outer ellipsoids. For the genuinely new regime \(a\ge3,b\ge2\), the split graph is nonregular and nonbipartite, and arbitrary positive cross weight varies its disk radii. Neither comparison provides the nonlinear support optimizer or the sharp radius/contact transition above. The regular complete-graph specialization \(b=1,\tau=1\) is already covered and is not claimed as new. The strict-concavity method and elementary inequalities are standard; the explicit classification and contact onset are the present mathematical claim.

## Limitations

This is an exact theorem for a specified two-parameter graph family with one additional positive edge-disk weight. It does not classify arbitrary weighted graphical discotopes, their full algebraic boundaries, volumes, or minimum-volume ellipsoids. Priority relative to unindexed equivalent treatments of coordinate-disk sums remains provisional. The finite computation alone cannot establish the all-parameter theorem. Independent mathematical audit and independent validation have not been performed.

## References

1. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, first posted 2021-05-26, especially Section 5.2. https://arxiv.org/abs/2105.12406
2. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, first posted 2021-11-01, especially Sections 2–3, 6–8. https://arxiv.org/abs/2111.01241
3. *Spherical extremal ellipsoids and bipartite outer-contact topology of regular graphical discotopes*, published mathematical record, 2026; accessible scientific statement: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-spherical-extremal-ellipsoids-and-bipartite-outer-contact-topolo--29a07695a757
4. *Degree-ellipsoid rigidity and complete contact graphs of bipartite graphical discotopes*, published mathematical record, 2026; accessible scientific statement: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-degree-ellipsoid-rigidity-and-complete-contact-graphs-of-biparti--5cadf5d3fdbb
