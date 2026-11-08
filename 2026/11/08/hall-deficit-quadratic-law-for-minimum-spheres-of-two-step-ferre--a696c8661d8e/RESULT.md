# Hall-deficit quadratic law for minimum spheres of two-step Ferrers root polytopes

## Finding

Let \(p,q\ge2\) and \(1\le a<p\), \(1\le b<q\) be integers. Start with \(K_{p,q}\), choose left and right vertex subsets \(A\), \(B\) of sizes \(a\) and \(b\), and delete exactly the \(ab\) edges joining \(A\) to \(B\). Orient every surviving edge from left to right. Its root polytope is
\[
P_{p,q;a,b}=\operatorname{conv}\{e_i-e_{p+j}:(i,j)\in E\}\subset\mathbb R^{p+q}.
\]
Writing
\[
\theta=\frac ap+\frac bq,\qquad
u=\frac{p}{a(p-a)},\qquad
v=\frac{q}{b(q-b)},\qquad h=\frac{uv}{u+v},
\]
the squared radius of the unique minimum enclosing Euclidean ball is
\[
\boxed{R^2=2-\frac1p-\frac1q-h\bigl(\max\{0,\theta-1\}\bigr)^2.}
\]
Its unique center has positive left coordinates and negative right coordinates. Within \(A\), \(A^c\), \(B\), and \(B^c\), these positive magnitudes are respectively \(x/a\), \((1-x)/(p-a)\), \(y/b\), and \((1-y)/(q-b)\), where
\[
\delta=\max\{0,\theta-1\},\qquad
x=\frac ap-\frac{v}{u+v}\delta,\qquad
y=\frac bq-\frac{u}{u+v}\delta.
\]
When \(\theta\le1\), **all** \(pq-ab\) edge roots touch this sphere. When \(\theta>1\), precisely the roots corresponding to \(A\times B^c\) and \(A^c\times B\) touch it; the \((p-a)(q-b)\) roots corresponding to \(A^c\times B^c\) lie strictly inside, each with squared-distance clearance \(2h(\theta-1)\). Thus the contact number is \(a(q-b)+(p-a)b\) above the threshold.

For example, at \((p,q,a,b)=(4,4,3,3)\), one has \(\theta=3/2\), \(h=2/3\), \(R^2=4/3\), and exactly six of the seven vertices touch the sphere; the remaining vertex has squared-distance clearance \(2/3\).

## Assumptions and scope

All dimensions and block sizes are integers with \(p,q\ge2\), \(1\le a<p\), and \(1\le b<q\). Distances are measured in the original ambient Euclidean metric, or equivalently in the inherited metric of the affine hull of the roots. The graph has two nested left-neighborhood classes; after relabeling it is a two-step Ferrers (chain) graph. Every surviving root \(e_i-e_{p+j}\) has squared norm two, and the graph is connected. No fractional edge multiplicities, vertex weights, or affine changes of metric are assumed.

## Proof

**1. General equal-norm minimum-sphere lemma.** Let \(V\) be a finite nonempty subset of a Euclidean space and assume \(\|w\|^2=L\) for all \(w\in V\). Let \(z\) be the unique minimum-norm point of \(Q=\operatorname{conv}(V)\). Projection optimality gives \(z\cdot(w-z)\ge0\) for every \(w\in V\), hence
\[
\max_{w\in V}\|w-z\|^2\le L-\|z\|^2.
\]
For any center \(c\), choose convex coefficients with \(z=\sum_w\alpha_w w\). Then
\[
\begin{split}
\max_{w\in V}\|w-c\|^2
&\ge\sum_w\alpha_w\|w-c\|^2\\
&=L+\|c\|^2-2c\cdot z\\
&=L-\|z\|^2+\|c-z\|^2.
\end{split}
\]
Therefore the unique minimum enclosing ball is centered at \(z\) and has squared radius \(L-\|z\|^2\). An edge root belongs to its boundary exactly when \(z\cdot w=\|z\|^2\). This proves uniqueness even if the affine hull is proper.

**2. Reduction to a two-variable convex problem.** Change signs on all right coordinates by an orthogonal map. The roots become the \(0/1\) edge incidence vectors \(e_i+e_{p+j}\). The squared norms and enclosing spheres do not change. The minimizing norm point is invariant under permutations within the four blocks \(A\), \(A^c\), \(B\), \(B^c\). Write \(x\) for its total mass on \(A\) and \(y\) for the mass on \(B\). Its other two block masses are \(1-x\) and \(1-y\). Because there are no edges between \(A\) and \(B\), the full feasible region is
\[
\{(x,y):x\ge0,\ y\ge0,\ x+y\le1\}.
\]
Indeed the masses \(x\), \(y\), and \(1-x-y\) can be placed on the three complete edge classes \(A\times B^c\), \(A^c\times B\), and \(A^c\times B^c\), respectively. Uniform redistribution within each class gives the required block-constant point. Conversely, the class masses of every convex combination of roots have precisely these signs and sum one.

The squared norm of the unique block-constant point with masses \((x,1-x;y,1-y)\) is
\[
F(x,y)=\frac{x^2}{a}+\frac{(1-x)^2}{p-a}
+\frac{y^2}{b}+\frac{(1-y)^2}{q-b}.
\]
Completing squares,
\[
F(x,y)=\frac1p+\frac1q
+u\left(x-\frac ap\right)^2
+v\left(y-\frac bq\right)^2.
\]
This is strictly convex because \(u,v>0\).

**3. Sharp Hall-type threshold and center.** The unconstrained minimizer is \((a/p,b/q)\). It is feasible exactly when \(\theta\le1\). In this regime \(\|z\|^2=1/p+1/q\), and \(x=a/p,y=b/q\).

If \(\theta>1\), the constrained minimizer lies on \(x+y=1\) and satisfies
\[
x=\frac ap-\frac{v}{u+v}(\theta-1),\qquad
 y=\frac bq-\frac{u}{u+v}(\theta-1).
\]
For completeness, it lies in the *relative interior* of that segment: minimizing \(F(x,1-x)\) over \(0\le x\le1\) gives
\[
x=\frac{\frac1{p-a}+\frac1b}{\frac1a+\frac1{p-a}+\frac1b+\frac1{q-b}},
\]
which lies strictly between zero and one. Substituting yields
\[
\|z\|^2=\frac1p+\frac1q+\frac{uv}{u+v}(\theta-1)^2.
\]
The lemma with \(L=2\) gives the stated squared radius and unique center. In the original signed root coordinates, negate the right-side entries of the computed center.

**4. Boundary contacts and exact clearance.** Let the four *positive magnitudes* at the center be
\[
\alpha=\frac xa,\quad \beta=\frac{1-x}{p-a},\quad
\gamma=\frac yb,\quad\eta=\frac{1-y}{q-b}.
\]
For an edge between a left and right block, the signed Euclidean inner product of the center with its root equals the sum of the relevant two magnitudes. When \(\theta\le1\), all left magnitudes are \(1/p\) and all right magnitudes are \(1/q\). Every edge root therefore has inner product \(1/p+1/q=\|z\|^2\) and is a contact.

If \(\theta>1\), direct subtraction gives
\[
\beta-\alpha=u\left(\frac ap-x\right)=h(\theta-1),\qquad
\eta-\gamma=v\left(\frac bq-y\right)=h(\theta-1).
\]
Since \(x+y=1\), the minimizing point is a positive convex combination of roots only in \(A\times B^c\) and \(A^c\times B\). These two edge classes have equal center inner product \(\alpha+\eta=\beta+\gamma\); averaging shows that common value is \(\|z\|^2\). They are all contacts. Every remaining edge is in \(A^c\times B^c\), with center inner product \(\beta+\eta=\|z\|^2+h(\theta-1)\). Its squared distance to the center is therefore smaller than \(R^2\) by exactly \(2h(\theta-1)\). There are \((p-a)(q-b)\) such roots, and the two contacting classes contain \(a(q-b)+(p-a)b\) roots. All root points are distinct vertices, as the coordinate functional summing their own two nonzero coordinates strictly exposes each incidence vector (then transfer back by the orthogonal sign change).

This establishes every assertion for all admissible parameters. \(\square\)

## Verification

The standalone script `check_biclique_root.py` constructs the edge incidence vectors and independently solves the minimum-norm convex-combination problem by constrained numerical optimization. It compares the closed formulas with the computed optimum, checks the predicted touching edge classes and squared-distance clearances, and covers 441 integer parameter quadruples with \(2\le p,q\le7\), including 205 strict-screening cases. Successful output:

`BICLIQUE_ROOT_MINIMUM_SPHERE_CHECKS_PASSED 441 screened_cases 205`

This finite numerical check is reproducibility evidence, not a substitute for the proof covering all dimensions.

## Relationship to prior work

Kálmán and Tóthmérész develop directed-graph root polytopes and their Jaeger-type dissections, with special discussion of layer-complete graphs. Setiabrata studies the face structure of the closely related polytope that also contains the origin. Rietsch and Williams investigate root, flow, and order polytopes and their toric links. Corso and Nagel provide foundational Ferrers-graph algebraic context. These results motivate the natural bipartite root configuration but do not, in the portions materially inspected, state the present sharp Euclidean enclosing-ball, Hall-deficit, and contact-screening formulas.

The general equal-norm minimum-sphere lemma is elementary and **not claimed as new**. The proposed contribution is the all-parameter exact specialization and the sharp contact phase of the specified two-step Ferrers root family. Established descriptions via graph edge polytopes or least-energy fractional matchings could conceivably contain an equivalent formula under different terminology; historical priority remains provisional.

## Limitations

Only two-step Ferrers graphs obtained by removing a *single proper nonempty biclique* from a complete bipartite graph are covered. The Euclidean metric is the canonical root-coordinate metric; arbitrary affine equivalence need not preserve the result. No general characterization for arbitrary Ferrers diagrams, weighted roots, or multiple forbidden rectangles is established. The review is not an independent mathematical audit.

## References

1. T. Kálmán and L. Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960v1 (first posted 2021-05-03), https://arxiv.org/abs/2105.00960.
2. L. Setiabrata, *Faces of root polytopes*, arXiv:2001.05191v1 (first posted 2020-01-15), https://arxiv.org/abs/2001.05191.
3. K. Rietsch and L. Williams, *Root polytopes, flow polytopes, and order polytopes*, arXiv:2406.15803v1 (first posted 2024-06-22), https://arxiv.org/abs/2406.15803.
4. A. Corso and U. Nagel, *Monomial and toric ideals associated to Ferrers graphs*, arXiv:math/0609371v1 (first posted 2006-09-13), https://arxiv.org/abs/math/0609371.
