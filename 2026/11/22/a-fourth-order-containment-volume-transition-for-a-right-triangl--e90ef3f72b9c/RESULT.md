# A fourth-order containment-volume transition for a right triangle in rectangles

## Finding
Let \(T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\) and \(Q_{a,b}=[0,a]\times[0,b]\), for arbitrary \(a,b>0\). Define their **four-dimensional orientation-preserving similarity-containment polytope** by
\[
\mathcal C(a,b)=\left\{(s,t,u,v)\in\mathbb R^4:\ (x,y)\longmapsto(sx-ty+u,tx+sy+v)\ \text{maps }T\text{ into }Q_{a,b}\right\}.
\]
Its ordinary four-dimensional Lebesgue volume has the following **complete exact shape law**:
\[
\operatorname{vol}_4\mathcal C(a,b)=
\begin{cases}
 a^3b-\frac58a^4,&b\ge2a,\\[3pt]
 \frac{a^4+b^4-8ab(a^2+b^2)+24a^2b^2}{24},&\frac12a\le b\le2a,\\[5pt]
 ab^3-\frac58b^4,&a\ge2b.
\end{cases}
\tag{1}
\]
At the boundaries, the adjacent formulas agree. Put \(r=\max(a,b)/\min(a,b)\). The **exact number of vertices** of this full-dimensional four-polytope is
\[
 f_0(\mathcal C(a,b))=
 \begin{cases}
 12,&r=1,\\
 20,&1<r<2,\\
 16,&r=2,\\
 18,&r>2.
 \end{cases}
\tag{2}
\]
For fixed \(b>0\), the volume is \(C^3\) but not \(C^4\) across \(a=2b\), with a jump of \(1\) in the fourth derivative \(\partial_a^4\operatorname{vol}_4\mathcal C(a,b)\) from the middle branch to the outer branch. Symmetrically the same holds across \(b=2a\). Remarkably, the combinatorial collapse from \(20\) vertices to \(12\) at the square \(a=b\) does **not** alter the volume polynomial.

## Assumptions and scope
Both source and target are the exact Euclidean sets displayed above. The area of the source triangle is \(1/2\); the target rectangle need not have unit area. Transformation coordinates are the real numbers \((s,t,u,v)\), with the scale-rotation multiplier \(s+it\). The inclusion is closed and allows zero scale; the zero-scale subset has four-volume zero. Reflections are excluded. All volumes use unweighted Lebesgue measure in these four coordinates, **not** the Haar density in polar scale-angle coordinates. The theorem classifies this natural one-parameter rectangle-shape family, not arbitrary source triangles or target polygons. The primary geometric object is a four-dimensional polytope (MSC2020 52B11).

## Proof
**1. Exact fibers.** Since \(T\) is the convex hull of three points, an image of \(T\) lies in the convex rectangle precisely when the images of all three vertices lie there. Thus the exact inequalities are
\[
0\le u,u+s,u-t\le a,\qquad 0\le v,v+t,v+s\le b.
\tag{3}
\]
They also show that \(\mathcal C(a,b)\) is a bounded, full-dimensional intersection of twelve halfspaces: its point \((s,t,u,v)=(0,0,a/2,b/2)\) satisfies them strictly, and boundedness follows from the bounded images of the three noncollinear vertices. For fixed \((s,t)\), allowable \(u\) form an interval of length \((a-W_x(s,t))_+\), and allowable \(v\) form one of length \((b-W_y(s,t))_+\), where
\[
\begin{aligned}
W_x&=\max\{0,s,-t\}-\min\{0,s,-t\},\\
W_y&=\max\{0,t,s\}-\min\{0,t,s\},\\
z_+&=\max\{z,0\}.
\end{aligned}
\]
Fubini therefore gives the exact four-volume integral
\[
\operatorname{vol}_4\mathcal C(a,b)
=\int_{\mathbb R^2}(a-W_x)_+(b-W_y)_+\,ds\,dt.
\tag{4}
\]

**2. Orthant reduction.** When \(s\) and \(t\) have the same sign, writing \(p=|s|\), \(q=|t|\) gives \((W_x,W_y)=(p+q,\max(p,q))\). When the signs differ, the two widths swap. Set
\[
J(A,B)=\int_{p,q\ge0}(A-p-q)_+\bigl(B-\max(p,q)\bigr)_+\,dp\,dq.
\]
Accounting for both quadrants in each sign class yields
\[
\operatorname{vol}_4\mathcal C(a,b)=2J(a,b)+2J(b,a).
\tag{5}
\]
On the half-domain \(p\ge q\), substitute \(m=p\). Symmetry gives the elementary exact integral
\[
J(A,B)=2\int_0^{\min(A,B)}(B-m)\int_0^{\min(m,A-m)}(A-m-q)\,dq\,dm,
\tag{6}
\]
where an inner interval with negative upper bound is interpreted as empty; the outer range is nonnegative since \(m\le A\). The inner integral changes expression only at \(m=A/2\). Direct polynomial integration produces
\[
J(A,B)=\begin{cases}
\dfrac{B^3(4A-3B)}{12},&B\le A/2,\\[4pt]
\dfrac{A^4-8A^3B+24A^2B^2-16AB^3+4B^4}{48},&A/2\le B\le A,\\[4pt]
\dfrac{A^3(8B-3A)}{48},&A\le B.
\end{cases}
\tag{7}
\]
Substitution into (5), distinguishing the three aspect-ratio regimes, proves (1), including both interfaces. For example, \(\operatorname{vol}_4\mathcal C(1,1)=5/12\), and \(\operatorname{vol}_4\mathcal C(2,1)=11/8\).

**3. Fourth-order transition.** Fix \(b=1\). On \(1<a<2\), (1) gives
\[
V(a)=\frac{a^4-8a^3+24a^2-8a+1}{24}
=a-\frac58+\frac{(2-a)^4}{24}.
\]
For \(a>2\), \(V(a)=a-5/8\). Hence the first three derivatives match at \(a=2\) and the fourth derivative jumps from \(1\) to \(0\). Using the degree-four homogeneity \(V(a,b)=b^4V(a/b,1)\) proves the same unit fourth-derivative jump in \(a\) at \(a=2b\) for every fixed \(b>0\). The central polynomial covers both \(a<b\) and \(a>b\), showing the absence of a volume singularity at \(a=b\).

**4. Complete vertex enumeration.** With \(b=1\), the twelve inequalities (3) have constant normals and right-hand sides affine in \(a\). Every vertex of this four-dimensional bounded polytope is the unique intersection of some four linearly independent active supporting hyperplanes. There are exactly \(\binom{12}{4}=495\) candidate quartets; thus enumerating them is exhaustive even when the polytope has nonsimple vertices. For each nonsingular quartet, solve its rational linear system in the form \(z_0+a z_1\), and impose all twelve remaining affine inequalities. Each candidate's feasible \(a\)-set is an exact rational interval. The standalone `checker.py` carries out this **symbolic interval enumeration**, as opposed to evaluating only sampled aspect ratios. On \(a\ge1\), the endpoints of nonempty feasible intervals belong to \(\{1,2\}\), and the unique feasible vertices at representative interior/boundary values have counts \(12,20,16,18\) for \(a=1\), \(1<a<2\), \(a=2\), \(a>2\), respectively. There are no other interval boundaries, hence the counts hold throughout each open regime. For \(a<b\), conjugating the transformation by reflection across \(x=y\) exchanges the rectangle side lengths and maps \((s,t,u,v)\) bijectively by a linear transformation, preserving vertex counts. This proves (2).

## Verification
Run `python3 checker.py` from this directory. It uses only standard-library `fractions` and `itertools`. It exactly enumerates all \(495\) hyperplane quartets, checks feasible parameter intervals, asserts that the only transitions for \(a/b\ge1\) are at \(1\) and \(2\), and verifies the four claimed vertex counts. It evaluates the integrated expressions (7) against (1) at five distinct rational values in each of four polynomial regimes. Because both sides are polynomials of degree at most four on each regime, these five-point exact tests also certify each polynomial identity. The proof of (1) is independently given by (4)–(7), without numerical integration or reliance on test output. Separate independent floating-point four-dimensional convex-hull calculations at eleven aspect ratios agreed with (1) and (2); these are corroboration, not mathematical proof.

## Relationship to prior work
The four-coordinate configuration polytope of planar polygon similarity containment is due to the computational-geometry framework of Agarwal, Amenta and Sharir (1998), and is studied in detail by Choi and Choi (2026). Their conclusions concern algorithms, optimal placements and the silhouette. The new statement concerns the **Lebesgue four-volume over all placements** and the **exact aspect-dependent vertex stratification**, including a fourth-derivative discontinuity. Chan and Hair (2024) study faster maximal-placement algorithms, not this volume invariant. A separate published published-finding corpus finding, *A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes* (2026; identifier 0f26f49ae237), gives an exact self-containment volume for source equal to target, both triangles. The present source is a right triangle and the target is a variable rectangle, so that theorem's homothetic triangular translation-fiber identity and universal gauge law do not apply. Searches of the relevant literature and exact-record database did not identify this specific spline law or the complete vertex phase diagram; absence from searches is not proof of historical priority.

## Limitations
The phase diagram is particular to a right isosceles unit-leg triangle and rectangles, under the stated four-parameter measure. It does not classify arbitrary triangle-rectangle pairs or nonrectangular containers. The vertex count is established by reproducible exact finite enumeration, not a closed-form hand classification of each individual vertex. No application to motion-planning complexity is proved. No independent external mathematical audit has been performed. Earlier unindexed or inaccessible geometric-computation sources may contain an equivalent formula.

## References
- Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, arXiv:2611.08556v1 (first public 2026-11-05), https://arxiv.org/abs/2611.08556.
- P. K. Agarwal, N. Amenta and M. Sharir, *Largest Placement of One Convex Polygon Inside Another*, Discrete & Computational Geometry **19** (1998), 95–104, https://doi.org/10.1007/PL00009337; lawful preprint at https://www.math.tau.ac.il/~michas/nina.pdf.
- T. M. Chan and I. M. Hair, *Convex Polygon Containment: Improving Quadratic to Near Linear Time*, SoCG 2024, https://doi.org/10.4230/LIPIcs.SoCG.2024.34.
- *A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes*, publicly available published-finding corpus mathematical record (2026), identifier 0f26f49ae237.
