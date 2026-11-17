# Exact near-cut-locus gap law on sheared flat tori and a sharp hexagonal intensity bound

## Finding
Let \(\Lambda\subset\mathbb R^2\) be a full-rank Euclidean lattice, \(A=\det\Lambda>0\), and \(T=\mathbb R^2/\Lambda\). For two independent Haar-uniform points of \(T\), list the squared lengths of their connecting geodesics in nondecreasing order, with multiplicity, as \(D_1^2\le D_2^2\le\cdots\). Define the *runner-up gap* \(G=D_2^2-D_1^2\). Equal-length ties occur with probability zero.

**Exact shear law.** For the area-one lattice
\[
\Lambda_t=\mathbb Z(1,0)+\mathbb Z(t,1),\qquad -\tfrac12\le t\le\tfrac12,
\]
put \(s=|t|\). For every \(0\le\varepsilon\le1\),
\[
\boxed{\Pr_{\Lambda_t}(G\le\varepsilon)
=1-(1-\varepsilon)(1+t^2-\varepsilon)
+\bigl(s-\varepsilon/2\bigr)_+^2.}
\]
The CDF equals zero for negative thresholds and one for thresholds at least one. Equivalently, for \(0<s<1/2\), it is
\[
\begin{cases}
(2-s+s^2)\varepsilon-\tfrac34\varepsilon^2,&0\le\varepsilon\le2s,\\
(2+t^2)\varepsilon-\varepsilon^2-t^2,&2s\le\varepsilon\le1.
\end{cases}
\]
Its first derivative is continuous across the geometric transition \(\varepsilon=2s\), but its second derivative jumps by \(-1/2\) (right derivative minus left derivative); for \(t=0\), the law is \(2\varepsilon-\varepsilon^2\). In particular the right-endpoint density is \(2-s+s^2\), which has a cusp as a function of signed shear at zero.

**Sharp general-lattice law.** Let \(V\) be the closed Voronoi cell of \(0\in\Lambda\). For each of its edges \(E\), write \(L_E\) for the edge length, \(v_E\in\Lambda\setminus\{0\}\) for its uniquely determined adjacent-cell displacement, and \(h_E=\|v_E\|/2\) for its distance from the origin. Then
\[
\Pr_\Lambda(G\le\varepsilon)=C(\Lambda)\varepsilon+O_\Lambda(\varepsilon^2),\qquad
C(\Lambda)=\frac1{4A}\sum_E\frac{L_E}{h_E}.
\]
The sharp area-normalized bound is
\[
\boxed{A C(\Lambda)\ge\sqrt3,}
\]
with equality **if and only if** \(\Lambda\) is similar to the equilateral triangular lattice. More precisely, if \(P=\sum_E L_E\), then the following exact nonnegative-defect decomposition holds:
\[
C(\Lambda)-\frac{\sqrt3}{A}=
\frac{P^2-8\sqrt3 A}{8A^2}+
\frac1{8A^2}\sum_{E<F}L_E L_F
\frac{(h_E-h_F)^2}{h_Eh_F}.
\]
For the triangular lattice with shortest-vector length \(\ell\), hence \(A=\sqrt3\ell^2/2\), its entire small-gap CDF is exactly \(2\varepsilon/\ell^2-\varepsilon^2/\ell^4\) for all sufficiently small nonnegative \(\varepsilon\).

**Conditional facet law.** For any fixed lattice, conditioned on \(0<G\le\varepsilon\), the facet approached by the minimizing displacement has limiting weight
\[
\Pr(E)=\frac{L_E/h_E}{\sum_F L_F/h_F}.
\]
Given that facet, the orthogonal projection position along it is asymptotically uniform in arclength, and \(G/\varepsilon\) is asymptotically independent and uniform on \([0,1]\). In these edge-index, along-edge, normalized-gap coordinates, convergence holds in total variation, with error \(O_\Lambda(\varepsilon)\). For points projecting outside an edge near a Voronoi vertex, choose an arbitrary fixed measurable assignment; its conditional probability is \(O_\Lambda(\varepsilon)\).

## Assumptions and scope
The metric is the Euclidean quotient metric of a fixed full-rank planar lattice. Points are sampled independently according to normalized flat area, not by boundary length or by a Gaussian distribution. Geodesics are distinguished by their lattice winding/displacement, so repeated lengths are counted separately. The \(O_\Lambda\) constants depend on the fixed lattice and need not be uniform in degenerating lattice shapes. The first formula is for precisely the specified area-one shears. The global inequality is for all two-dimensional lattices and fixed area \(A\).

## Proof
**1. Transfer to Voronoi power margins.** The difference of two independent Haar points is Haar. Choose its unique representative \(x\) inside the interior of \(V\). The shortest geodesic has squared length \(\|x\|^2\); geodesics indexed by nonzero \(v\in\Lambda\) have squared lengths \(\|x-v\|^2\). Thus
\[
G(x)=\min_{v\in\Lambda\setminus\{0\}}
\bigl(\|v\|^2-2x\cdot v\bigr).
\]
Consequently the superlevel set \(V_\varepsilon=\{x:G(x)\ge\varepsilon\}\) is exactly the intersection of all halfplanes
\[
x\cdot v\le\frac{\|v\|^2-\varepsilon}{2},\qquad 0\ne v\in\Lambda.
\]
By uniformity, \(\Pr(G\le\varepsilon)=1-\operatorname{area}(V_\varepsilon)/A\) (up to null boundaries).

**2. Reduction to six vectors for the shear family.** By reflecting one coordinate, take \(0\le t\le1/2\). Put \(u=(1,0)\), \(v=(t,1)\), and \(w=v-u\). The six signed vectors \(\pm u,\pm v,\pm w\), in their angular cyclic order, form adjacent unimodular cones covering \(\mathbb R^2\). Adjacent vectors have nonnegative dot product: \(u\cdot v=t\ge0\), \(v\cdot w=1+t^2-t>0\), and \(w\cdot(-u)=1-t>0\). Each lattice vector in one such cone is a nonnegative integer combination \(z=ma+nb\) of its two edge generators. Writing \(g_z(x)=\|z\|^2-2x\cdot z\),
\[
g_z=m g_a+n g_b+m(m-1)\|a\|^2+n(n-1)\|b\|^2+2mn\,a\cdot b.
\]
For \(m+n\ge1\) and \(\varepsilon\ge0\), the six inequalities \(g_a,g_b\ge\varepsilon\) therefore imply \(g_z\ge\varepsilon\). No omitted lattice vector produces another restriction, for any \(\varepsilon\ge0\).

**3. Exact rectangle-minus-two-triangles calculation.** Use area-preserving coordinates \(X=x\cdot u\), \(Y=x\cdot v\). The six conditions are
\[
|X|\le\frac{1-\varepsilon}{2},\quad
|Y|\le\frac{1+t^2-\varepsilon}{2},\quad
|Y-X|\le\frac{2-2t+t^2-\varepsilon}{2}.
\]
For \(0\le\varepsilon\le1\), the first two inequalities form a rectangle of area \((1-\varepsilon)(1+t^2-\varepsilon)\). The last inequality removes two congruent right triangles of total area \((t-\varepsilon/2)_+^2\). These triangles lie wholly in opposite rectangle corners; their legs equal \((t-\varepsilon/2)_+\), and for \(t\le1/2\) this fits within the rectangle side lengths throughout their nonzero regime. This yields the exact CDF. Since the constraints for \(\pm u\) are inconsistent for \(\varepsilon>1\), the support ends at one. Expanding the two branches proves the claimed derivative and second-derivative transition.

**4. General first-order coefficient.** Each Voronoi edge \(E\) has a unique relevant lattice vector \(v_E\); its supporting line is at distance \(h_E=\|v_E\|/2\). At an interior point of the edge the active affine margin is \(g_{v_E}=2\|v_E\|\delta\), where \(\delta\) is inward normal distance. Therefore the \(G\le\varepsilon\) strip has thickness \(\varepsilon/(2\|v_E\|)=\varepsilon/(4h_E)\) along that edge. The finitely many edge strips overlap only in vertex neighborhoods of area \(O_\Lambda(\varepsilon^2)\). Nonfacial vectors cannot contribute outside these neighborhoods, by compactness and positive slack along edge interiors. Hence
\[
\operatorname{area}\{x\in V:G(x)\le\varepsilon\}
=\frac\varepsilon4\sum_E\frac{L_E}{h_E}+O_\Lambda(\varepsilon^2).
\]
The same strip Jacobian and the negligible vertices give the conditional facet, arclength and normalized-gap laws and their total-variation error.

**5. Sharp optimization and exact defect.** Any planar lattice Voronoi cell is a centrally symmetric parallelogram or hexagon: it tiles the plane by translates and has at most six sides (equivalently, use its three nonzero lattice classes modulo \(2\Lambda\)). The classical polygonal isoperimetric inequality gives \(P^2\ge 8\sqrt3 A\), with equality exactly for a regular hexagon (for a parallelogram, \(P^2\ge16A\)). Set \(H=\sum_E L_E h_E=2A\) and \(J=\sum_E L_E/h_E\). The algebraic Cauchy identity
\[
HJ-P^2=\sum_{E<F}L_E L_F
\frac{(h_E-h_F)^2}{h_E h_F}
\]
is exact. Since \(C=J/(4A)=(P^2+(HJ-P^2))/(8A^2)\), the displayed defect identity follows. Equality forces a regular Voronoi hexagon, which tiles only by its equilateral triangular translation lattice (up to similarity). For this lattice all six relevant vectors have the same length \(\ell\), so for sufficiently small \(\varepsilon\) the shrunken halfplanes produce a homothetic hexagon of scale \(1-\varepsilon/\ell^2\), giving the stated exact quadratic CDF.

## Verification
The standalone `check_gap.py` uses exact rational halfplane clipping and checks the shear formula against the inequalities from every lattice vector with coordinates in a finite box \(|m|,|n|\le4\), for six rational shear values and nine rational thresholds. It additionally checks the branch junction and derivatives by exact rational arithmetic. The run returned `GEODESIC_GAP_RATIONAL_CLIPPING_OK 108 exact comparisons; no exhaustive-lattice claim`. The infinite-vector reduction in Proof Step 2 and the all-lattice inequality in Step 5 are mathematical arguments, not conclusions drawn from the finite checker. The proof and checked script assume no external files or packages.

## Relationship to prior work
The Voronoi-cell/relevant-vector framework and exact nearest-lattice-point algorithms are standard; the 2014 full texts by McKilliam–Grant–Clarkson and Bonifas–Dadush use this framework for closest-vector computation, not for a distribution of the *difference between the first and second squared distances*. The convex-polygon inequality used in Step 5 is classical, with a quantitative 2014 treatment by Indrei–Nurbekyan. Existing flat-torus random-distance results chiefly concern the *single* minimum geodesic length and its distribution. The exact shear CDF, its disappearing-facet transition at \(2|t|\), and the square-to-triangular optimization of the runner-up-gap intensity are the narrowly asserted contribution; no novelty is claimed for Voronoi halfplanes or polygonal isoperimetry themselves.

## Limitations
Only Euclidean flat two-tori and the squared-length runner-up gap are treated; a gap in unsquared lengths has a different weighting. The sharp global result concerns the leading coefficient, not a full CDF stochastic ordering among all lattices. Convergence constants depend on the lattice, and the conditional mark statement uses local facet coordinates, not total variation convergence of physical points to a measure on one-dimensional edges. No independent mathematical audit or definitive historical-priority certification has been performed.

## References
- R. G. McKilliam, A. Grant, I. V. L. Clarkson, *Finding a closest point in a lattice of Voronoi's first kind*, arXiv:1405.7014v1, first posted 27 May 2014. https://arxiv.org/html/1405.7014v1
- N. Bonifas, D. Dadush, *Short Paths on the Voronoi Graph and the Closest Vector Problem with Preprocessing*, arXiv:1412.6168, first posted 18 December 2014. https://arxiv.org/abs/1412.6168
- E. Indrei, L. Nurbekyan, *On the stability of the polygonal isoperimetric inequality*, arXiv:1402.4460, first posted 18 February 2014. https://arxiv.org/abs/1402.4460
