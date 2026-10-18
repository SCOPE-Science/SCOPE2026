# Exact P-angle constant of the regular dodecagonal Banach plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\), where
\[
N_{12}(s,t)=
\max\left\{
|s|,|t|,
\left|\frac{\sqrt3s+t}{2}\right|,
\left|\frac{s+\sqrt3t}{2}\right|,
\left|\frac{-s+\sqrt3t}{2}\right|,
\left|\frac{-\sqrt3s+t}{2}\right|
\right\}.
\]
Then the Yang--Li P-angle constant is
\[
S_P(X_{12})=\frac{2-\sqrt3}{2}.
\]
The supremum is attained by
\[
x=(1,2-\sqrt3),\qquad y=(-1,2-\sqrt3).
\]

## Assumptions and scope
All scalars are real. For nonzero vectors \(u,v\), the P-angle is
\[
\cos\operatorname{ang}_P(u,v)
=
\frac{\|u\|^2+\|v\|^2-\|u-v\|^2}{2\|u\|\|v\|}.
\]
The Yang--Li constant is evaluated here through its displayed definition
\[
S_P(X)=\sup\{\cos\operatorname{ang}_P(x+y,x-y):x,y\in S_X,\ x\ne\pm y\}.
\]
The defining preprint has an earlier standing dimension convention, but Definition 3.1 itself is stated for a Banach space and the immediately following Remark 3.2 explicitly discusses the two-dimensional Euclidean plane. The present theorem directly evaluates that displayed formula on the two-dimensional dodecagonal norm above.

## Proof
Put \(r=\sqrt3\). Let \(E\) be the twelve signed facet functionals of the norm. Thus
\[
N_{12}(z)=\max_{f\in E}f(z),
\]
and the six unoriented members of \(E\) have coefficient vectors
\[
(1,0),\quad
\left(\frac r2,\frac12\right),\quad
\left(\frac12,\frac r2\right),\quad
(0,1),\quad
\left(-\frac12,\frac r2\right),\quad
\left(-\frac r2,\frac12\right).
\]
Their negatives supply the remaining six signed functionals. The dual unit ball is the convex hull of these twelve functionals.

For \(x,y\in B_{X_{12}}\), set
\[
A=N_{12}(x+y),\qquad B=N_{12}(x-y).
\]
Choose \(f,g\in E\) attaining these two maxima. Then
\[
A+rB
=(f+rg)(x)+(f-rg)(y)
\le \|f+rg\|_*+\|f-rg\|_*.
\]
Exact evaluation of the dual norms on the twelve vertices of the primal dodecagon gives, up to dihedral symmetry, the following table according to the relative signed-facet separation \(k=0,1,\ldots,6\):

\[
\begin{array}{c|c|c|c}
k&\|f+rg\|_*&\|f-rg\|_*&\text{sum}\\ \hline
0&1+r&r-1&2r\\
1&1+r&1&2+r\\
2&2r-1&5-2r&4\\
3&2&2&4\\
4&5-2r&2r-1&4\\
5&1&1+r&2+r\\
6&r-1&1+r&2r
\end{array}
\]
Because \(2r<4\) and \(2+r<4\), every case yields
\[
A+rB\le4.
\]
Interchanging the roles of the two selected facet functionals gives the companion inequality
\[
rA+B\le4.
\]
The triangle inequality also gives
\[
0\le A\le2,\qquad 0\le B\le2.
\]

Now take \(x,y\in S_{X_{12}}\) with \(x\ne\pm y\), so \(A,B>0\). Since
\[
(x+y)-(x-y)=2y,
\]
the P-angle expression is
\[
\cos\operatorname{ang}_P(x+y,x-y)
=
\frac{A^2+B^2-4}{2AB}.
\]
Let
\[
t=2-r.
\]
It is enough to prove
\[
A^2+B^2-tAB\le4.
\]
All feasible pairs \((A,B)\) lie in the convex polygon
\[
\mathcal P=
\{(A,B):0\le A,B\le2,\ A+rB\le4,\ rA+B\le4\}.
\]
The quadratic
\[
Q(A,B)=A^2+B^2-tAB
\]
is convex because its Hessian has eigenvalues \(2-t\) and \(2+t\), both positive. Hence its maximum on \(\mathcal P\) is bounded by its maximum at the vertices of \(\mathcal P\). Those vertices are
\[
(0,0),\ (2,0),\ (2,2t),\ (2(r-1),2(r-1)),\ (2t,2),\ (0,2).
\]
At \((2,0)\), \((0,2)\), \((2,2t)\), and \((2t,2)\), one has \(Q=4\). At the central vertex,
\[
Q(2(r-1),2(r-1))
=16r-24<4,
\]
while \(Q(0,0)=0\). Therefore \(Q(A,B)\le4\) throughout \(\mathcal P\), and so
\[
\cos\operatorname{ang}_P(x+y,x-y)
\le \frac t2
=\frac{2-\sqrt3}{2}.
\]

For sharpness, take
\[
x=(1,2-r),\qquad y=(-1,2-r).
\]
Direct substitution into the six defining absolute-value functionals gives
\[
N_{12}(x)=N_{12}(y)=1.
\]
Moreover,
\[
N_{12}(x+y)=2(2-r),\qquad N_{12}(x-y)=2.
\]
Thus
\[
\cos\operatorname{ang}_P(x+y,x-y)
=
\frac{2-r}{2},
\]
which proves the claimed equality.

## Verification
The bundled `verify.py` performs exact arithmetic in \(\mathbb Q(\sqrt3)\). It constructs all twelve signed facet functionals and all twelve primal vertices, verifies that the vertices are unit vectors, checks both weighted two-point inequalities for every ordered pair of signed facets, reproduces the seven-row dual-norm table, verifies the six vertices of \(\mathcal P\), and checks the attaining pair exactly.

The finite computation is not used as an infinite proof. The passage from arbitrary \(x,y\) to the weighted inequalities uses the dual representation of the norm, and the global quadratic bound follows analytically from convexity on the explicitly described feasible polygon.

## Relationship to prior work
Yang and Li introduced \(S_P(X)\), proved the universal bound
\[
0\le S_P(X)\le\frac12,
\]
and characterized Hilbert spaces by \(S_P(X)=0\). Their inspected full text treats classical \(\ell_p\) spaces but contains no regular-polygon or dodecagonal computation.

A later exact result determines \(S_P\) on real \(\ell_p\) sequence spaces. That theorem does not cover the regular dodecagonal plane, whose unit ball is a twelve-gon rather than an \(\ell_p\) ball. Exact P-angle values for other polygonal planes likewise do not imply the present statement because the weighted facet inequalities and feasible \((A,B)\)-region depend on the specific dodecagonal dual geometry.

## Limitations
The theorem concerns one canonical two-dimensional polyhedral norm and one angular constant. It does not classify \(S_P\) on all regular polygons, arbitrary dodecagonal norms, or general polyhedral Banach planes. The bibliographic search cannot prove absolute novelty; an equivalent computation under different coordinates or terminology could exist outside the inspected sources.

The earlier standing dimension convention in the defining preprint creates a notation-scope ambiguity, although the displayed definition is meaningful in dimension two and the paper immediately discusses the two-dimensional Euclidean case. The result here is explicitly a direct evaluation of that displayed formula.

## References
1. Z. Yang and Y. Li, “New Geometric Constant Related to the P-angle Function in Banach Spaces,” arXiv:2208.11239v1, first public version 24 August 2022. Mathematics Subject Classification 46B20.
