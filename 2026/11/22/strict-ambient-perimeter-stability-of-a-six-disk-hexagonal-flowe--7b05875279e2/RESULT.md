# Strict ambient perimeter stability of a six-disk hexagonal flower

## Finding

Place six closed unit disks at centers
\[
c_0^*=(0,0),\qquad c_j^*=2\bigl(\cos((j-1)\pi/3),\sin((j-1)\pi/3)\bigr),\quad 1\le j\le5.
\]
Thus five centers occupy consecutive vertices of a regular hexagon, with one disk at its center. For a labeled nearby feasible configuration \(c=(c_0,\ldots,c_5)\), meaning \(\|c_i-c_j\|\ge2\) for every distinct pair, let \(P(c)\) be the perimeter of the convex hull of the centers. Put
\[
E=\{(0,j):1\le j\le5\}\cup\{(j,j+1):1\le j\le4\},\qquad
\delta_{ij}=\|c_i-c_j\|-2\ge0\quad ((i,j)\in E).
\]
For all feasible configurations sufficiently close to \(c^*\), the following *ambient*, not merely contact-class, expansion holds:
\[
\begin{aligned}
P(c)-(8+2\sqrt3)={}&\frac{2}{\sqrt3}(\delta_{01}+\delta_{05})
+\frac{1}{\sqrt3}(\delta_{02}+\delta_{03}+\delta_{04})\\
&+\left(1-\frac1{\sqrt3}\right)\sum_{j=1}^4\delta_{j,j+1}
+O\!\left(\left(\sum_{e\in E}\delta_e\right)^2\right).
\end{aligned}
\]
The remainder is uniform in a sufficiently small neighborhood, after fixing rigid motions. Consequently \(c^*\) is a strict isolated local minimum modulo Euclidean isometries. The optimal contact-gap stability coefficient is
\[
\liminf_{\substack{c\to c^*,\ c\ \mathrm{feasible}\\c\not\cong c^*}}
\frac{P(c)-P(c^*)}{\sum_{e\in E}\delta_e}
=1-\frac1{\sqrt3}>0.
\]
The same conclusions hold for the convex hull perimeter of the disks themselves after adding \(2\pi\) to both perimeters. Independently, among *all* six-disk configurations having one disk tangent to each of the five others, the sharp minimum disk-hull perimeter is \(8+2\sqrt3+2\pi\), and equality consists precisely of the above hexagonal flowers, up to relabeling and planar isometry.

## Assumptions and scope

The six disks have identical radius one and pairwise disjoint interiors, although tangency is allowed. Distances refer to their centers. The local statement allows **every** feasible displacement of all six centers, including breaking active contacts, changing relative angles, and moving the central center; it does not freeze the contact graph. The separate global flower-class statement fixes only the five tangencies to one selected central disk, but otherwise permits arbitrary angles. Labels are used to state the quantitative contact-gap formula; the geometric assertions are label-independent. No unrestricted global optimum for six disks is claimed.

## Proof

**1. Reference geometry and active contacts.** The outer centers \(c_1^*,\ldots,c_5^*\) are the five vertices of a strictly convex pentagon, with side lengths \(2,2,2,2,2\sqrt3\), so \(P(c^*)=8+2\sqrt3\). The central center lies strictly inside this pentagon. Exactly nine pair distances equal two, namely those in \(E\). All other pair distances are strictly greater than two. These statements persist locally at the level of hull membership and strictly inactive constraints. Hence near \(c^*\), the perimeter is the smooth sum of the same five outer hull edge lengths.

**2. Exact differential and rigidity.** Let \(g_e(c)=\|c_i-c_j\|-2\), for \(e=(i,j)\in E\), and \(G\) be the \(12\times9\) matrix with columns \(\nabla g_e(c^*)\). These columns have the block \(-(c_j^*-c_i^*)/2\) at vertex \(i\) and \((c_j^*-c_i^*)/2\) at vertex \(j\). A direct exact calculation gives
\[
\nabla P(c^*)=G\lambda,
\quad
\lambda=\left(\frac2{\sqrt3},\frac1{\sqrt3},\frac1{\sqrt3},\frac1{\sqrt3},\frac2{\sqrt3},1-\frac1{\sqrt3},1-\frac1{\sqrt3},1-\frac1{\sqrt3},1-\frac1{\sqrt3}\right)^{\!T},
\]
with the five spokes followed by the four rim contacts. All weights are strictly positive.

To remove the three infinitesimal rigid motions, fix \(c_0=(0,0)\) and \((c_1)_y=0\) with \((c_1)_x>0\). The nine free coordinates, in order, are
\[
(c_1)_x,(c_2)_x,(c_2)_y,\ldots,(c_5)_x,(c_5)_y.
\]
The Jacobian of the nine contact gaps with respect to these coordinates has exact determinant \(9/16\). In particular it is invertible. This also follows geometrically by adding the peripheral vertices in sequence, each new vertex sharing two noncollinear contacts with the already rigid triangle. The determinant and gradient equations are independently checked with exact symbolic arithmetic by the included \(verify.py\).

**3. Ambient Taylor expansion and sharp constant.** By the inverse function theorem, the nine contact gaps provide smooth local coordinates on the configuration space modulo rigid motions. Taylor expansion of the smooth perimeter in these coordinates, using the exact differential in step 2, yields the displayed formula, with remainder bounded in absolute value by \(C(\sum_e|g_e|)^2\). For feasible configurations all \(g_e\ge0\); therefore for sufficiently small nonzero gaps, the leading term is positive, proving strict local minimality. Invertibility also shows that all nine gaps can vanish locally only at a congruent configuration. The smallest coefficient is \(1-1/\sqrt3\), appearing on rim contacts. Turning on exactly one rim gap by \(t>0\), leaving the other eight gaps zero in the local gap coordinate chart, yields feasible configurations for all sufficiently small \(t\): the six previously inactive inequalities remain strict by continuity. This produces the matching upper bound for the stated liminf. Thus the coefficient is sharp.

**4. Optimality within all five-spoke flowers.** If one center is tangent to all five other centers, translate it to the origin; the five outer centers lie on the radius-two circle. Their cyclic angular gaps \(\theta_1,\ldots,\theta_5\) are each at least \(\pi/3\), because distinct outer disks do not overlap, and sum to \(2\pi\). Thus each gap is at most \(2\pi/3\), the central point lies inside the outer convex pentagon, and
\[
P=4\sum_{i=1}^5\sin(\theta_i/2).
\]
The function \(\sin(\theta/2)\) is strictly concave on \([\pi/3,2\pi/3]\). A concave function on the gap simplex has its minimum at a vertex; strict concavity ensures equality only at a vertex. The vertices have four gaps \(\pi/3\) and one gap \(2\pi/3\). Substitution gives \(P=8+2\sqrt3\), uniquely up to cyclic permutation and isometry. The Steiner perimeter identity \(\operatorname{Per}(\operatorname{conv}\bigcup_i B(c_i,1))=P(c)+2\pi\) concludes the disk-hull statements.

## Verification

Run \(python\ verify.py\) with Python 3.10+ and SymPy. It checks all nine active squared distances, absence of other contacts, the exact nine-parameter Jacobian determinant \(9/16\), the complete perimeter-gradient identity, positivity of the nine force multipliers, and the reference pentagon perimeter. Independently, local contact-gap coordinates were solved numerically for 160 positive-gap perturbations at four sizes, and their perimeter increments matched the linear formula with a quadratic-order error; these experiments supplement, rather than replace, the inverse-function-theorem proof. The finite calculations are identities at the specified six-center configuration, not an exhaustive search of the six-disk configuration space.

## Relationship to prior work

Hoffmann and Vilaxa (2026) develop contact and hull-class variational calculus and solve the **five**-disk global perimeter problem; their six-disk discussion counts possible penny graphs without establishing this six-disk flower's exact positive perimeter-force certificate or ambient sharp local stability. Kallrath and collaborators (2021) give numerical optimization methods and exact solutions for at most four arbitrary disks, rather than this six-disk local theorem. The present proof uses the standard Minkowski perimeter shift and first-variation contact framework, explicitly crediting them. The new assertion concerns an explicit stable six-disk contact stratum in the first not-yet-globally-classified size, with the sharp local contact-gap response.

## Limitations

This is **not** a proof of the unrestricted six-disk global minimum. The value \(8+2\sqrt3+2\pi\) is certified globally only when one disk touches all the other five, and is certified locally against all admissible perturbations around that flower. It does not classify other local minima or disconnected-contact configurations. The local \(O(\cdot^2)\) constant and neighborhood radius are asserted to exist by smooth inversion, not optimized numerically. Priority relative to harder-to-access older finite-packing literature remains a documented risk; the reviewed proof and overlap assessment are not an independent external audit.

## References

1. J. A. Hoffmann and F. H. Vilaxa, *Intrinsic Geometry of Hard Disk Clusters*, arXiv:2608.06513, first publicly posted 2026-08-06, https://arxiv.org/abs/2608.06513.
2. J. Kallrath, J. Ryu, C. Song, M. Lee, and D.-S. Kim, *Near optimal minimal convex hulls of disks*, Journal of Global Optimization 80 (2021), 551–594, https://doi.org/10.1007/s10898-021-01002-5.
3. A. Schürmann, *On Extremal Finite Packings*, Discrete & Computational Geometry 28 (2002), 389–403, https://doi.org/10.1007/s00454-002-0747-6 (abstract/metadata comparison only; full text not inspected).
