# The eight-vertex incenter transition for squared-cycle graphical zonotopes

## Finding
For every integer \(n\ge6\), let \(G_n=C_n^2\) be the graph on \(\mathbb Z/n\mathbb Z\) having undirected edges between vertices at cyclic distances one and two. In the zero-sum Euclidean space \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\), form its centered graphical zonotope
\[
K_n=\sum_{i=0}^{n-1}\sum_{j=1}^{2}\left[-\frac{e_i-e_{i+j}}2,\frac{e_i-e_{i+j}}2\right].
\]
For \(n\ge6\), the edge list has exactly \(2n\) distinct edges. The intrinsic Euclidean inradius is
\[
\rho_n=\begin{cases}
2\sqrt{\dfrac n{n-1}},&n=6,7,\\[4pt]
3\sqrt{\dfrac n{\lfloor n^2/4\rfloor}},&n\ge8.
\end{cases}
\]
The radius itself is a specialization of the established graphical-zonotope cut formula. The **new classification** is the following complete set of centers of contained balls of this maximum radius.

If \(n=6,7\), or \(n\ge9\) is odd, the center is unique and equals \(0\). If \(n=2m\ge8\), the centers form precisely
\[
\mathcal I_{2m}=\left\{(y_0,\ldots,y_{m-1},y_0,\ldots,y_{m-1}):
\sum_{j=0}^{m-1}y_j=0,\quad |y_j|\le b_m\ (0\le j<m)\right\},
\]
where
\[
b_m=\begin{cases}
2-\dfrac{3\sqrt7}{4},&m=4,\\[4pt]
3\left(1-\sqrt{1-\dfrac1{m^2}}\right),&m\ge5.
\end{cases}
\]
Thus the incenter is nonunique exactly when \(n\ge8\) is even. Its locus then has affine dimension \(m-1\), and its number of vertices is
\[
\#\operatorname{vert}(\mathcal I_{2m})=\begin{cases}
\binom{m}{m/2},&m\text{ even},\\[4pt]
m\binom{m-1}{(m-1)/2},&m\text{ odd}.
\end{cases}
\]
At eight vertices, the width of the center locus is controlled by singleton-cut inequalities, whereas for every larger even order it is controlled by near-balanced cyclic intervals. The two obstructions are genuinely distinct.

## Assumptions and scope
All edges of \(G_n\) carry unit weight. Coordinates are indexed modulo \(n\). Every ball is taken in the intrinsic \((n-1)\)-dimensional Euclidean space \(H_n\), not in ambient \(\mathbb R^n\), and the zonotope is explicitly centered at zero. The usual graph zonotope obtained by summing edge segments \([e_i,e_j]\) differs by a translation, so its centers are the stated ones translated by its symmetry center. All inequalities and equalities include the indicated parameter endpoints. The claim is only for \(n\ge6\), since smaller cycle squares have different edge multiplicities or graph identifications.

For a vertex subset \(S\), let \(\partial S\) denote the set of edges with exactly one endpoint in \(S\), and write \(s=|S|\). The centered cut normal is \(v_S=\mathbf1_S-(s/n)\mathbf1\), of Euclidean norm \(\sqrt{s(n-s)/n}\).

## Proof
**1. All cut inequalities describe the zonotope.** Each generator corresponding to an edge contributes at most \(1/2\) in absolute value to the cut sum across \(S\). Thus \(K_n\) satisfies
\[
\left|\sum_{i\in S}x_i\right|\le\frac{|\partial S|}{2}
\quad(\varnothing\ne S\subsetneq\mathbb Z/n\mathbb Z).\tag{1}
\]
Conversely, for any \(u\in H_n\), sorting its coordinates and integrating the indicators \(\mathbf1_{\{i:u_i>t\}}\) over their nontrivial level sets shows that any \(x\in H_n\) satisfying (1) obeys
\[
u\cdot x\le\frac12\sum_{\{i,j\}\in E(G_n)}|u_i-u_j|=h_{K_n}(u).
\]
Equality of all support-function upper bounds proves that (1) is an exact halfspace description, not merely a list of necessary constraints. Consequently, the ball \(c+rB_{H_n}\) lies in \(K_n\) if and only if, for every such \(S\),
\[
\left|\sum_{i\in S}c_i\right|+r\sqrt{\frac{s(n-s)}n}\le\frac{|\partial S|}{2}.\tag{2}
\]
The central symmetry of \(K_n\) implies that if a radius-\(r\) ball centered at \(c\) fits then a radius-\(r\) ball centered at \(-c\) fits, and their Minkowski midpoint is the centered radius-\(r\) ball. Thus zero is a maximum-radius center.

**2. Exact cut classification.** Encode \(S\) by its circular zero-one word and let \(t_i\) indicate a change between positions \(i\) and \(i+1\). The number of crossing distance-one edges is \(\sum_i t_i\). The number of crossing distance-two edges is \(\sum_i|t_i-t_{i+1}|\). Indeed, the parity of the two consecutive changes gives the difference between the endpoint bits. A nonempty proper circular word has \(2q\) changes for a positive integer \(q\), the number of runs of ones. If \(q=1\), the cut has four edges when one of the two runs has length one, and six edges otherwise. If \(q=2\), its four change indicators contribute at least two more distance-two crossings; equality, producing six crossing edges, occurs only when the four change indicators are consecutive, which means a pair of selected vertices at cyclic distance two or the complement of such a pair. If \(q\ge3\), there are at least six distance-one crossings. If the change indicators are not all one, there are at least two distance-two crossings; if they are all one then there are \(n\ge8\) distance-one crossings. Therefore for \(n\ge8\), every cut has size four (singleton or complement), six (a proper cyclic interval of size between two and \(n-2\), or a distance-two pair or its complement), or at least eight. For \(n=6,7\), every nonsingleton cut has at least six edges: by complementation take \(s\le\lfloor n/2\rfloor\), and use \(|\partial S|=4s-2|E(S)|\), with \(|E(S)|\le1\) for \(s=2\) and \(|E(S)|\le3\) for \(s=3\).

**3. Radius and the active cut families.** By (2) at the origin, the radius is \(\frac12\min_S|\partial S|/\|v_S\|\). The denominator is largest at a balanced cardinality. A singleton has ratio \(4/\sqrt{n-1}\), whereas a balanced cyclic interval has ratio \(6/\sqrt{\lfloor n^2/4\rfloor}\). For \(n=6,7\) the singleton is strictly better; for all \(n\ge8\) the balanced interval is strictly better, since \(4\lfloor n^2/4\rfloor>9(n-1)\). Cuts of size at least eight cannot compete, and an unbalanced six-edge cut has a smaller normal norm. The cut classification thus establishes the radius and shows that all active cut normals are exactly the singleton normals when \(n\le7\), or the balanced cyclic-interval normals when \(n\ge8\).

**4. Forced center subspaces.** Every active cut has zero right-hand slack in (2), so its center sum must vanish. At \(n=6,7\), singleton sums imply \(c=0\). For \(n=2m+1\ge9\), the length-\(m\) cyclic-interval sums vanish. Subtracting consecutive sums gives \(c_i=c_{i+m}\). Since \(\gcd(m,2m+1)=1\), all coordinates are equal and the zero-sum condition makes them zero. For \(n=2m\ge8\), all length-\(m\) interval sums vanish; their consecutive differences give \(c_i=c_{i+m}\). Thus any optimal center must be \(c=(y,y)\) with \(\sum_i y_i=0\).

**5. Sharp coordinate bounds.** Substitute \(n=2m\) into (2) with \(r=\rho_n=3\sqrt{2m}/m\). Singleton cuts of size four force
\[
|y_i|\le \gamma_m:=2-\frac{3\sqrt{2m-1}}m.
\]
Cyclic intervals of lengths \(m-1\) or \(m+1\) have six crossing edges and their sums reduce to a single \(\pm y_i\); they force
\[
|y_i|\le\beta_m:=3\left(1-\sqrt{1-\frac1{m^2}}\right).
\]
Therefore \(|y_i|\le b_m:=\min\{\beta_m,\gamma_m\}\). Direct radical comparison gives \(\gamma_4<\beta_4\), while \(\gamma_5=1/5>\beta_5\). For real \(m>1\), the function \(\gamma_m\) strictly increases, while \(\beta_m\) strictly decreases, so the stated piecewise formula follows for all integers \(m\ge4\).

**6. Sufficiency of those bounds.** Conversely, assume \(c=(y,y)\), \(\sum_i y_i=0\) and \(|y_i|\le b_m\). Every singleton/complement cut satisfies (2) by the bound \(b_m\le\gamma_m\). For six-edge cyclic intervals of length \(m\pm d\), where \(0\le d\le m-2\), the center sum is, up to sign, a sum of \(d\) consecutive entries of \(y\), of absolute value at most \(db_m\). The available slack equals
\[
f_m(d)=3\left(1-\sqrt{1-\frac{d^2}{m^2}}\right).
\]
This function is convex on \([0,m)\) and vanishes at zero, so for integers \(d\ge1\), \(f_m(d)\ge d f_m(1)=d\beta_m\ge db_m\). The exceptional six-edge distance-two pairs and their complements have absolute center sum at most \(2b_m\); their cardinalities are two or \(2m-2\), and their slack is \(f_m(m-2)\ge(m-2)\beta_m\ge2b_m\). All six-edge inequalities are therefore satisfied.

For every cut of size at least eight, the ball term in (2) is at most three, and the cut right-hand side is at least four, so its available slack is at least one. In any subset, the coefficient of each repeated value \(y_i\) lies in \(\{0,1,2\}\); since \(\sum_i y_i=0\), the absolute subset sum is no greater than \(\sum_i|y_i|\le m b_m\). This is strictly less than one: for \(m=4\), \(4b_4=8-3\sqrt7<1\); for \(m\ge5\), \(mb_m=3/[m(1+\sqrt{1-m^{-2}})]<1\). Hence all remaining inequalities (2) hold, establishing the claimed exact incenter locus.

**7. Dimension and vertices.** The map \(y\mapsto(y,y)\) is injective. Its domain is a nondegenerate central hyperplane section of the cube \([-b_m,b_m]^m\), so it has affine dimension \(m-1\). At a vertex at least \(m-1\) coordinate bounds must be active; otherwise a two-coordinate zero-sum perturbation preserves feasibility. Conversely these constraints suffice. If \(m\) is even, every vertex has exactly half of the coordinates at each of the two endpoints. If \(m\) is odd, exactly one coordinate is zero, the others split equally among positive and negative endpoints. The stated binomial vertex counts follow.

## Verification
The seven analytical steps establish the all-order claim, including the nontrivial sufficiency of all cut inequalities. Running the accompanying standalone `verify.py` verifies by exact integer cut arithmetic all \(130986\) nonempty proper cut masks for orders \(6\) through \(16\) and compares the predicted complete active normal family and its exact rational rank. It then checks \(21752\) cut constraints on all predicted vertices of the incenter loci for orders \(8,10,12,14\) using 65-decimal-place arithmetic. These tests corroborate the symbolic proof; finite tests alone do not establish the theorem for arbitrary order. Command: `python3 verify.py`.

## Relationship to prior work
Eisenbrand, Rothvoss, Russo, and Skorupinski study zonotope containment, approximation, and sparsification, rather than explicit optimal-center sets of this cyclic graphical family. Padrol, Pilaud, and Poullot develop the graphical-zonotope construction and its deformation cone. The general weighted graphical-zonotope Euclidean-inradius formula was already established in the mathematical record and implies the *radius* given above when combined with a cut minimization. A separate exact incenter classification for the **ordinary** cycle graphical zonotope shows a parity-dependent central cube section, but the graph is not \(C_n^2\): its cut distances, radii, and especially the exceptional order-eight singleton constraint differ. No novelty is claimed for the general cut halfspace description, the established general radius formula, or the ordinary-cycle incenter classification. The specific complete incenter locus for the squared cycle, including its sharp exceptional scale at eight vertices and vertex census, is the contribution.

## Limitations
This classification is for the unweighted graph square of the ordinary cycle with at least six vertices, in the standard intrinsic Euclidean realization. It does not extend automatically to higher cycle powers, arbitrary edge weights, or different norms. Novelty assessment is based on inspected mathematical sources and search, and is not a proof that an equivalent statement has never appeared under a different name. Independent mathematical assessment has not been performed.

## References
1. F. Eisenbrand, T. Rothvoss, M. Russo, R. Skorupinski, *Nearly-Tight Bounds for Zonotope Containment and Beyond*, arXiv:2605.04183, first public version 2026-05-05, https://arxiv.org/abs/2605.04183.
2. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first public version 2021-11-24, https://arxiv.org/abs/2111.12422.
3. *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, published mathematical finding, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab.
4. *Complete Euclidean incenter loci of cycle graphical zonotopes*, published mathematical finding, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-euclidean-incenter-loci-of-cycle-graphical-zonotopes--977e1f3aebef.
