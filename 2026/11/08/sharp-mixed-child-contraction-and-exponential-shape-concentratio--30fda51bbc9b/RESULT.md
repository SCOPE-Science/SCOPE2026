# Sharp mixed-child contraction and exponential shape concentration for largest-angle bisection

## Finding

For every nondegenerate Euclidean triangle, put its angles in nonincreasing order \(\alpha\ge\beta\ge\gamma>0\), normalize \(x=\beta/\alpha\) and \(y=\gamma/\alpha\), and let \(L,R\) denote the two children produced by bisecting the largest angle, with each child normalized again. Define the projective shape distortion
\[
H(x,y)=\frac{\max\{x,1/2\}}{\min\{y,1/2\}}\ge1.
\]
The unique zero of \(H-1\) is the right-isosceles shape \((x,y)=(1/2,1/2)\). Every single child satisfies \(H(Lz)\le H(z)\) and \(H(Rz)\le H(z)\). **Every two consecutive unequal child choices satisfy the sharp universal bound**
\[
\boxed{\ H(RLz)-1\le\frac34(H(z)-1),\qquad H(LRz)-1\le\frac34(H(z)-1).\ }
\]
Here \(RLz=R(Lz)\) and \(LRz=L(Rz)\). The factor \(3/4\) is optimal even when one restricts to nondegenerate triangles.

For any finite word of child choices containing \(k\) pairwise disjoint, adjacent, unequal pairs, the resulting shape obeys
\[
H(z_n)-1\le(3/4)^k\,[H(z_0)-1].
\]
In particular, on a random refinement branch whose independent child choices are \(L\) with probability \(p\in[0,1]\) and \(R\) with probability \(1-p\), with \(m=\lfloor n/2\rfloor\),
\[
\mathbb E[H(z_n)-1]\le\left(1-\frac{p(1-p)}2\right)^m[H(z_0)-1].
\]
For the complete binary refinement tree (\(p=1/2\)), the proportion of depth-\(n\) triangles whose distortion exceeds \(1+\varepsilon\), for every \(\varepsilon>0\), is bounded by
\[
\boxed{\ \frac{H(z_0)-1}{\varepsilon}\left(\frac78\right)^{\lfloor n/2\rfloor}.\ }
\]
These bounds hold with multiplicity when distinct descendant triangles have the same similarity class.

## Assumptions and scope

Angles are strictly positive and sorted at each step. The bisection is performed at any largest-angle vertex; if largest angles are tied, choose either maximizer and label its two descendants consistently. The inequality is insensitive to swapping labels. In each step a child is obtained by dividing the largest angle and retaining either of the two sides. The domain of normalized shapes is \(\{(x,y):0<y\le x\le1\}\). The extremal parameter value \(3/4\) is a supremum achieved at interior, nondegenerate shapes, not at a degenerate boundary. Only the two-letter mixed-block constant is claimed sharp; the \(7/8\) expectation factor is a valid upper bound, not asserted to be an optimal asymptotic rate.

## Proof

**Exact child recurrence.** Write \((a,b,c)=(\alpha/2,\beta,\gamma)\), without assuming these three entries are sorted. Then \(2a\ge b\ge c>0\). For any positive triple \(t=(a,b,c)\), let \(m(t)=\min\{a,b,c\}\), \(M(t)=\max\{a,b,c\}\), and \(V(t)=M(t)-m(t)\). For the parent, \(H=M(t)/m(t)\), hence \(H-1=V(t)/m(t)\). The unsorted angular triples of the two children are \((a,b,a+c)\) and \((a,c,a+b)\). In each case sort descending and halve only the largest component, obtaining the new triple \((a',b',c')\) representing the next triangle.

On a region where the relevant ordering comparisons hold, the complete piecewise-linear recurrences are:

\[
L(a,b,c)=\begin{cases}
(b/2,a+c,a),&b\ge a+c,\\
((a+c)/2,b,a),&a+c\ge b\ge a,\\
((a+c)/2,a,b),&a\ge b,
\end{cases}
\]
\[
R(a,b,c)=\begin{cases}
((a+b)/2,a,c),&a\ge c,\\
((a+b)/2,c,a),&c\ge a.
\end{cases}
\]
Every new raw angular triple contains a component \(a+b\) or \(a+c\), which is at least \(2m(t)\), and every other component is at least \(m(t)\). Therefore the newly halved largest component is at least \(m(t)\), as are the two remaining components. Thus **\(m(t')\ge m(t)\) for either child**.

**Exact spread certificate.** By scale invariance set \(a=1/2,b=x,c=y\), \(0\le y\le x\le1\). The original spread \(V\) is affine on three closed polyhedra: it equals \(x-1/2\) when \(x\ge1/2,y\ge1/2\); equals \(x-y\) when \(x\ge1/2\ge y\); and equals \(1/2-y\) when \(1/2\ge x\ge y\). Intersect these regions with each permissible first-child and second-child ordering region in the displayed recurrence. The intersections form 31 nonempty closed rational polygons (some may be lower-dimensional), with 61 total vertices counted by region, including repeated boundary vertices.

On each such polygon, each component of the one-step and two-step triples is affine in \((x,y)\). Because a maximum of affine functions minus a minimum of affine functions is convex, \(V(t_1)-V(t_0)\) and \(V(t_2)-(3/4)V(t_0)\) are convex on each cell, with the affine original spread \(V(t_0)\). A convex function on a bounded polygon never exceeds its largest vertex value. Exact rational enumeration of every polygon vertex shows
\[
V(t_1)-V(t_0)\le0,\qquad V(t_2)-\frac34 V(t_0)\le0
\]
for both \(L\!\to\!R\) and \(R\!\to\!L\). The largest gap in the latter inequality is exactly zero. This is an exhaustive finite polyhedral proof, **not** a finite sampling of input triangles. The complete standard-library rational certificate is `verify.py`, supplied with this result. Its branch inequalities, vertex intersections, and assertion of 31 enumerated cells are visible in the code. Combined with the minimum monotonicity, it yields
\[
H(t_1)-1\le H(t_0)-1,\qquad
H(t_2)-1\le\frac34[H(t_0)-1].
\]
The closure \(y=0\) is used only to verify a polynomial inequality; division by \(m\) is used solely for strictly positive triangle angles.

**Sharpness.** Take \((x,y)=(t,t)\) with \(0<t<1/2\). A direct application of the two branches gives
\[
(RL)(t,t)=\left(\frac{t+1/2}{t+3/2},\frac{2t}{t+3/2}\right),
\]
and hence \(H(t,t)=1/(2t)\), \(H((RL)(t,t))=1/4+3/(8t)\), and
\[
\frac{H((RL)(t,t))-1}{H(t,t)-1}=\frac34.
\]
Every such shape represents a genuine triangle after multiplying the angular ratios by the unique positive normalization whose angles sum to \(\pi\).

**Paths and tree probabilities.** A disjoint mixed pair multiplies \(H-1\) by at most \(3/4\); every intervening singleton or equal pair is nonexpanding. Iterate to obtain the deterministic \((3/4)^k\) bound. For independent choices, disjoint position pairs are mixed with probability \(2p(1-p)\); conditioning on their past, the mean multiplier is at most \(1-2p(1-p)/4=1-p(1-p)/2\). An unpaired final choice is nonexpanding. For \(p=1/2\), all \(2^n\) depth-\(n\) nodes have equal probability; Markov's inequality applied to \(H-1\) gives the stated proportion bound. This also proves exponential shape concentration without assuming a quantitative lower bound on angular separation.

## Verification

Run `python3 verify.py` using Python's standard library. The checker performs exact rational polygon-vertex enumeration for both mixed branch orders, verifies 31 nonempty ordering cells and 61 exact vertex checks, checks nondecrease of the minimal triple coordinate on both successive steps and nonincrease of single-step spread, verifies the mixed-block coefficient exactly, and tests the claimed sharpness identity on five nondegenerate rational parameters. The executed output was

`VERIFY_OK rational_cells=31 vertex_checks=61 minimum_checks=122 one_step_width_checks=61 maximal_linear_gap=0 sharp_isosceles_cases=5`

The asserted global inequalities follow from the explicit polyhedral exhaustiveness argument, rather than from the five illustrative sharpness evaluations. This is a reproducible exact rational certificate, not an independently reviewed proof.

## Relationship to prior work

Ismailescu, Kim, Kim, and Lee (2019) established nondegeneracy and diameter decay for the largest-angle bisection tree. Michaud and Korotov (2026, initially publicly posted July 28) extended geometric regularity and mesh decay to largest-angle \(n\)-section. Neither of those analyzed results states the mixed-child distortion contraction or an exponential finite-level shape-concentration bound.

Michaud (first posted November 4, 2026) subsequently established the projective Lyapunov picture: pure branches can behave exceptionally, while infinitely alternating branches converge qualitatively to right-isosceles shape and full refinement levels concentrate. Its statements and proofs were inspected and compared at the level of implication. In particular, that analysis does not provide a universal sharp mixed-block factor or an explicit exponential concentration estimate; its conclusion identifies such quantitative estimates as a subsequent direction. The earlier July 28 work is the date-eligible motivating source for the present result; the November 4 work is cited as a later comparison and is not used to backdate the research anchor. The present claim concerns only the new quantitative rate and sharpness, not the previously known qualitative convergence.

## Limitations

The theorem applies to Euclidean planar largest-angle bisection and the specified projective distortion, not to tetrahedral largest-dihedral-angle bisection or arbitrary mesh-refinement procedures. The two-step coefficient is sharp but the random-path expectation factor is only guaranteed, not claimed optimal. The estimates give convergence in the projective shape metric, not a particular spatial diameter rate. Historical priority beyond inspected sources remains provisional. No independent audit has been performed.

## References

1. D. Ismailescu, J. Kim, K. Kim, and J. Lee, *The largest angle bisection procedure*, arXiv:1908.02749v1, first posted August 6, 2019, https://arxiv.org/abs/1908.02749 .
2. J. Michaud and S. Korotov, *On Triangulations Generated by the Largest-Angle \(n\)-Section Algorithm*, arXiv:2607.25457v1, first posted July 28, 2026, https://arxiv.org/abs/2607.25457 .
3. J. Michaud, *Largest-Angle Bisection and Statistical Regularization of Triangle Shapes*, arXiv:2611.06492v1, first posted November 4, 2026, https://arxiv.org/abs/2611.06492 (subsequent comparison).
