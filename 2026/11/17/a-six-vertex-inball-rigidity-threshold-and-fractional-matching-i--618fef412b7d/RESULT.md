# A six-vertex inball rigidity threshold and fractional-matching incenters for complete-graph spanning-tree polytopes

## Finding

Let \(n\ge4\) be an integer, put \(m=\binom n2\), and let \(P_n\subset\mathbb R^m\) be the convex hull of the edge-incidence vectors of all spanning trees of the complete graph on \(n\) labeled vertices. Equip its affine hull \(\sum_e x_e=n-1\) with the *intrinsic* Euclidean metric of \(\mathbb R^m\). The exact largest inscribed-ball radius is
\[
 r_n=\begin{cases}
 \sqrt{\dfrac{n-2}{n(n-1)}},&n=4,5,\\[3pt]
 \dfrac2n\sqrt{\dfrac{m}{m-1}},&n\ge6.
 \end{cases}
\]
The uniform edge-density vector \(\bar x_e=2/n\) is always an incenter, but its uniqueness changes sharply: all centers form a two-dimensional **regular hexagon** for \(n=4\), an affine image of the five-dimensional fractional perfect matching polytope of \(K_5\) for \(n=5\), and a **single point** for every \(n\ge6\).

For \(n=4\), put \(\ell_4=\sqrt5/6\) and \(h=(3-\sqrt5)/6\). All incenters have
\[
 x_{12}=x_{34}=a,\quad x_{13}=x_{24}=b,\quad x_{14}=x_{23}=c,
 \qquad a+b+c=3/2,\quad \ell_4\le a,b,c\le1-\ell_4.
\]
This is a regular hexagon in the intrinsic Euclidean metric on the center affine plane, with circumradius \(2h\) and area \(6\sqrt3\,h^2\). Its six vertices are the permutations of \((a,b,c)=(1/2+h,1/2-h,1/2)\).

For \(n=5\), put \(\ell_5=3\sqrt6/20\), \(\kappa=(8-3\sqrt6)/5>0\), and
\[
 F_5=\{y\in\mathbb R^{\binom52}: y_e\ge0,\ \sum_{e\ni v}y_e=1\ \text{for each vertex }v\}.
\]
All incenters, with no additional inequalities, are exactly \(x_e=\ell_5+\kappa y_e\) for \(y\in F_5\). The center locus has dimension five and exactly **22 vertices**: ten vertices whose positive weights are \(1/2\) on a triangle and \(1\) on the disjoint edge, and twelve vertices whose positive weights are \(1/2\) on a Hamiltonian five-cycle. A relative-interior inball contacts the five vertex-degree facets only; at a vertex of the center locus the ball additionally contacts five coordinate facets (five-cycle case) or six coordinate facets (triangle-plus-edge case). The hexagon for \(n=4\) has the four vertex-degree facets in contact throughout, and eight total contacts at each of its six vertices. For \(n\ge6\), the unique inball contacts exactly all \(m\) coordinate nonnegativity facets.

## Assumptions and scope

All graphs are simple, complete and unweighted; every spanning tree has \(n-1\) edges, each represented by its \(0\)-\(1\) edge indicator. Radius, center, tangent hyperplanes and hexagon area are **Euclidean in the stated affine hull**, not combinatorial or lattice-normalized. The statements are for all integers \(n\ge4\), with no asymptotic approximation or generic-position assumption. A tangent facet means its supporting hyperplane is exactly one inradius away from the center. The historical description of spanning-tree facets and the general fractional matching vertex theorem are prior results, not claimed here.

## Proof

**1. Facet halfspaces.** The standard spanning-tree/base-polytope description specializes, for \(K_n\), to the equality \(\sum_e x_e=n-1\), lower facets \(x_e\ge0\) for every edge, and upper facets
\[
  x(E(S))\le s-1\quad\text{for each }S\subsetneq[n],\ 2\le s=|S|\le n-1.
\]
Here \(E(S)\) consists of all \(q=\binom s2\) internal edges. These halfspaces suffice and are facets in this range (the largest subsets correspond to minimum-degree constraints). This specialization follows from the matroid base-polytope inequalities or the complete facet characterization of Chaourar (2019).

**2. Exact distances from the edge-uniform center.** Write \(H=\{z:\sum_e z_e=0\}\). The intrinsic norm of the projection of the indicator of any set of \(q\) edge coordinates onto \(H\) is \(\sqrt{q(1-q/m)}\). At \(\bar x_e=2/n\), the distance to a lower coordinate facet is
\[
 d_0=\frac{2/n}{\sqrt{1-1/m}},\qquad
 d_0^2=\frac{4(n-1)}{n(n-2)(n+1)}.
\]
For an upper subset facet with \(s\) vertices, the slack is \((s-1)(n-s)/n\) and the squared Euclidean distance is
\[
 d_s^2=\frac{2(n-1)(s-1)(n-s)}{n\,s(n+s-1)},\qquad2\le s\le n-1.
\]
For fixed \(n\), the function proportional to \((s-1)(n-s)/(s(n+s-1))\), extended to real \(s\in[2,n-1]\), has strictly decreasing logarithmic derivative
\[
 \frac1{s(s-1)}-\frac1{n-s}-\frac1{n+s-1}.
\]
It therefore has no interior minimum. The two endpoint values satisfy
\(d_2^2/d_{n-1}^2=(n-1)^2/(n+1)>1\) for every \(n\ge4\). Hence the closest upper facets always have \(s=n-1\), and
\[
 d_{n-1}^2=\frac{n-2}{n(n-1)}.
\]
Their squared distance relative to that of lower facets is
\[
 \frac{d_{n-1}^2}{d_0^2}=\frac{(n-2)^2(n+1)}{4(n-1)^2}.
\]
The difference of numerator and denominator in this comparison is \(n(n^2-7n+8)\), strictly negative at \(n=4,5\) and strictly positive for all integers \(n\ge6\). This proves the displayed piecewise formula at the uniform center.

**3. Global optimality and the forced equalities.** The radius feasible at a candidate center is the minimum of finitely many affine slacks divided by the corresponding fixed intrinsic normal norms, a concave function of the center. Averaging the center over all vertex permutations of \(K_n\) does not reduce that radius and gives \(\bar x\); thus \(\bar x\) attains the global optimum. There is also a direct certificate. For \(n=4,5\), sum the distances/slacks of the \(n\) size-\(n-1\) upper facets: their sum is constant on the affine hull, so a radius attaining \(d_{n-1}\) forces every such facet to be at exactly that distance, equivalently
\[
  \sum_{e\ni v}x_e=\frac{2(n-1)}n\quad\text{for every vertex }v.
\]
For \(n\ge6\), the coordinate lower facets give \(x_e\ge d_0\sqrt{1-1/m}=2/n\). Summing over all \(m\) edges forces equality for every edge, so the incenter is unique. In that case all coordinate facets and no upper facets contact its ball.

**4. The four-vertex locus.** In \(K_4\), the forced vertex-degree equations imply equal weights on opposite edges: \(x_{12}=x_{34}=a\), \(x_{13}=x_{24}=b\), \(x_{14}=x_{23}=c\), with \(a+b+c=3/2\). The remaining size-two upper facets require \(x_e\le1-\ell_4\); lower facets require \(x_e\ge\ell_4\), where the exact coordinate-normal clearance is \(\ell_4=\sqrt5/6\). Hence the entire center locus is the stated planar cube section. Translating \((a,b,c)\) by \((1/2,1/2,1/2)\) identifies it with \(\{u+v+w=0,\ |u|,|v|,|w|\le h\}\), a regular hexagon. The ambient edge-coordinate embedding doubles squared lengths; its circumradius is \(2h\), and regular-hexagon area is \(6\sqrt3 h^2\). At a hexagon vertex one opposite edge-pair reaches a lower facet and one reaches an upper facet, besides the four degree facets.

**5. The five-vertex locus.** The forced degree equations for \(K_5\) are \(\sum_{e\ni v}x_e=8/5\). Lower-coordinate clearance is \(x_e\ge\ell_5=3\sqrt6/20\). Consequently each center satisfying just these constraints is uniquely written \(x_e=\ell_5+\kappa y_e\), where \(\kappa=8/5-4\ell_5>0\) and \(y\in F_5\). It remains to prove that the omitted upper facets automatically contain the radius-\(r_5\) ball. Every \(y\in F_5\) satisfies \(y_e\le1\), implying
\[
 x_e\le\ell_5+\kappa=8/5-3\ell_5<1-\ell_5,
\]
which handles all size-two upper facets. For a triple \(S\), summing its degree equations gives \(y(E(S))\le3/2\); thus
\[
 x(E(S))\le3\ell_5+\frac32\kappa=\frac{12}5-3\ell_5
 <2-\frac{3\sqrt{14}}{20}.
\]
The right side is exactly the required upper threshold for the size-three facets at radius \(r_5=\sqrt{3/20}\), since their projected-normal norm is \(\sqrt{21/10}\). The strict inequality is equivalent to \(9\sqrt6-3\sqrt{14}>8\), which follows, for example, from \(\sqrt6>12/5\) and \(\sqrt{14}<4\). The size-four upper facets are already equalities of the degree conditions; hence no other restrictions remain and all stated contacts follow. The unsigned vertex-edge incidence matrix of \(K_5\) has rank five, so \(F_5\) has dimension \(10-5=5\), with positive interior point \(y_e=1/4\). The standard fractional perfect matching vertex criterion (also proved from linear independence of supported incidence columns) gives components consisting of single unit edges or odd cycles of half-weight edges. On five vertices the only possibilities are one triangle plus its disjoint edge (\(\binom53=10\)) or one Hamiltonian five-cycle (\(5!/10=12\)). Thus there are exactly 22 vertices. At any \(n=5\) center all non-degree upper facets remain strictly outside the ball; the lower coordinate facets contact exactly when \(y_e=0\), giving the stated extreme contact counts. This completes the classification.

## Verification

A standalone Python checker, `check.py`, verifies the exact rational facet-distance inequalities for every integer \(4\le n\le1000\), constructs all 22 fractional degree-one vertices of \(K_5\) with exact fractions, and checks the complete size-two/three/four facet inequalities for their corresponding centers. An optional independent linear-programming comparison (NumPy and SciPy if installed) agrees with the predicted optimal radius for \(4\le n\le7\). These are finite checks only; the proof above establishes the unrestricted quantifiers. Running `python3 check.py` requires only the Python standard library for the core exact and combinatorial checks.

## Relationship to prior work

Chaourar, *The facets of the spanning trees polytope* (arXiv:1903.07292, first submitted 18 March 2019), proves a general facet description for graphic matroid base polytopes; this work uses its specialization and does not claim that facet description. Behrend, *Fractional Perfect b-Matching Polytopes. I: General Theory* (arXiv:1301.7356, 2013), supplies the general fractional-matching vertex characterization; this work does not claim that characterization. The added statement is the all-order **Euclidean ball-center** classification of the complete-graph spanning-tree polytope and its low-order identifications. Related descriptions of Minkowski asymmetry centers and the inball of complete-bipartite spanning-tree polytopes address other metrics or other graph families, and do not provide this classification. Historical priority for an equivalent formulation elsewhere remains provisional.

## Limitations

The theorem does not address arbitrary host graphs, other norms or weighted trees. The five-vertex incenter locus is identified up to an explicit *similarity*, and its vertex and contact counts are exact, but a separate closed-form intrinsic five-volume is not claimed. Prior-literature equivalence searches cannot establish absolute historical novelty; a related record on Minkowski asymmetry was available in summary but not in full text. Independent validation has not been performed.

## References

1. B. Chaourar, *The facets of the spanning trees polytope*, arXiv:1903.07292 (first submitted 2019-03-18), https://arxiv.org/abs/1903.07292 . Full mathematical statements were inspected in the accessible HTML version, especially Theorem 2.3 and Corollary 2.4.
2. R. E. Behrend, *Fractional Perfect b-Matching Polytopes. I: General Theory*, arXiv:1301.7356 (2013), https://arxiv.org/abs/1301.7356 . See Theorem 22 and Corollary 19.
