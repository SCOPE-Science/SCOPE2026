# Sharp two-midline envelope on the regular octagonal Banach plane
## Finding
Let
\[
X_8=(\mathbb R^2,N_8),
\qquad
N_8(s,t)
=
\max\left\{
|s|,
|t|,
\frac{|s|+|t|}{\sqrt2}
\right\}.
\]
For every pair
\[
x,y\in S_{X_8},
\qquad
N_8(x-y)=1,
\]
the two equilateral-midline lengths satisfy the simultaneous sharp bounds
\[
\boxed{
N_8(x+y)\le 2\sqrt2-1,
\qquad
N_8(2x-y)\le 2\sqrt2-1
}.
\tag{1}
\]

Both inequalities are attained at the same pair. One choice is
\[
x=(1,1-\sqrt2),
\qquad
y=(3-2\sqrt2,-1).
\tag{2}
\]
For (2),
\[
N_8(x)=N_8(y)=N_8(x-y)=1
\]
and
\[
N_8(x+y)=N_8(2x-y)=2\sqrt2-1.
\tag{3}
\]

Consequently, for the equilateral-midline constants introduced by Chen, Yang, Liu and Li,
\[
M_1(X_8)=2\sqrt2-1,
\]
\[
M_2(X_8)=9-4\sqrt2,
\]
and
\[
M_3(X_8)=\sqrt{2\sqrt2-1}.
\tag{4}
\]

## Assumptions and scope
All scalars are real.

The three constants are
\[
M_1(X)
=
\sup_{\substack{\|x\|=\|y\|=\|x-y\|=1}}
\frac{\|x+y\|+\|2x-y\|}{2},
\]
\[
M_2(X)
=
\sup_{\substack{\|x\|=\|y\|=\|x-y\|=1}}
\frac{\|x+y\|^2+\|2x-y\|^2}{2},
\]
and
\[
M_3(X)
=
\sup_{\substack{\|x\|=\|y\|=\|x-y\|=1}}
\frac{\|x+y\|^{1/2}+\|2x-y\|^{1/2}}{2}.
\]

Put
\[
r=\sqrt2-1,
\qquad
b=r^2=3-2\sqrt2,
\qquad
c=2\sqrt2-1=1+2r.
\tag{5}
\]
The unit ball of \(X_8\) is the regular octagon with vertices
\[
(1,r),\ (r,1),\ (-r,1),\ (-1,r),
\]
and their negatives.

## Proof
Set
\[
z=x-y.
\]
Then
\[
N_8(x)=N_8(z)=N_8(x-z)=1,
\tag{6}
\]
while the two quantities in (1) become
\[
A=N_8(2x-z),
\qquad
B=N_8(x+z).
\tag{7}
\]

The dihedral isometry group of the regular octagon acts transitively on its eight edges. Hence, after applying a common isometry to \(x\) and \(z\), assume
\[
x=(1,a),
\qquad
-r\le a\le r.
\tag{8}
\]
Exchanging
\[
z\longleftrightarrow x-z
\]
preserves (6) and interchanges \(A\) and \(B\). Thus it is enough to keep one representative from each such pair.

Intersecting the eight edges of the unit sphere with the translate
\[
x-S_{X_8}
\]
gives exactly the following three branches.

For
\[
-r\le a\le-b,
\]
one may take
\[
z=(r-a,1+a).
\tag{9}
\]
For
\[
-b\le a\le b,
\]
one may take
\[
z=
\left(
\frac{1-a}{2},
\frac{1+2r+a}{2}
\right).
\tag{10}
\]
For
\[
b\le a\le r,
\]
one may take
\[
z=(1-r-a,1).
\tag{11}
\]
The other feasible point is \(x-z\) and therefore only swaps \(A\) and \(B\).

We now evaluate (7).

On branch (9),
\[
A=c,
\qquad
B=\sqrt2-a.
\tag{12}
\]
Because
\[
a\ge-r,
\]
one has
\[
B\le\sqrt2+r=2\sqrt2-1=c.
\tag{13}
\]

On branch (10),
\[
A
=
\frac{2+r-a}{\sqrt2},
\qquad
B
=
\frac{2+r+a}{\sqrt2}.
\tag{14}
\]
Since
\[
|a|\le b
\]
and
\[
\frac{2+r+b}{\sqrt2}=c,
\]
both quantities in (14) are at most \(c\).

On branch (11),
\[
A=\sqrt2+a,
\qquad
B=c.
\tag{15}
\]
Because
\[
a\le r,
\]
one has
\[
A\le\sqrt2+r=c.
\tag{16}
\]

Equations (12)--(16), together with the exchange symmetry, prove (1).

At the endpoint
\[
a=-r,
\]
take
\[
x=(1,-r),
\qquad
z=(2r,1-r).
\]
Then
\[
y=x-z=(b,-1),
\]
which is exactly (2), and direct substitution gives (3). Therefore the envelope is sharp.

Each function
\[
(s,t)\longmapsto \frac{s+t}{2},
\qquad
(s,t)\longmapsto \frac{s^2+t^2}{2},
\qquad
(s,t)\longmapsto \frac{\sqrt{s}+\sqrt{t}}{2}
\]
is coordinatewise increasing on the nonnegative quadrant. Hence (1) gives the upper bounds in (4), while the common equality pair (2) attains all three simultaneously. This proves (4).

## Verification
The branch decomposition is finite and exact: for fixed \(x=(1,a)\), the condition (6) says that \(z\) belongs to the intersection of the octagonal boundary with its translate
\[
x-S_{X_8}.
\]
Solving the corresponding edge-pair equations gives (9)--(11), plus the exchanged point \(x-z\).

The bundled `verify.py` independently reconstructs those boundary intersections on a rational grid of \(a\)-values, checks that no sampled intersection is missed by the three formulas and their exchanged versions, and verifies the norms and the envelope. It also checks the sharp pair and all three values in (4).

These finite checks are reproducibility aids only. The continuum statement follows from the exhaustive edge intersection and the exact formulas (12)--(16).

## Relationship to prior work
Chen, Yang, Liu and Li introduced \(M_1\), \(M_2\) and \(M_3\) in 2022 for equilateral triples on the unit sphere. Their paper establishes general bounds, uniform-nonsquareness consequences, Hilbert-space values, and calculations for selected standard examples. The inspected full text contains no regular-octagonal calculation.

A later equilateral-pair geometric constant,
\[
T_G(X)
=
\sup
\sqrt{\|x+y\|\,\|2x-y\|},
\]
uses the same admissible equilateral pairs but a geometric-mean objective. A published research record computes
\[
T_G(X_8)=2\sqrt2-1.
\]
That product statement does not imply (1): bounding the geometric mean does not bound each factor separately. The present result supplies the stronger coordinatewise envelope, from which the arithmetic, quadratic and subduplicate midline constants all follow at once.

Public searches under the exact \(M_1,M_2,M_3\) notation, the regular-octagon alias, the candidate value \(2\sqrt2-1\), and equilateral-midline terminology located no statement covering (1) or (4).

## Limitations
The proof is specific to the regular octagonal plane and exploits its finite dihedral edge structure.

No classification of all maximizing equilateral pairs is claimed. The theorem exhibits one common maximizing pair and proves the exact supremum.

The equality of the extremal scale \(2\sqrt2-1\) with the known geometric-mean constant on the same plane does not imply equality of the underlying invariants on other Banach spaces.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent octagonal computation may exist under a linearly equivalent normalization or a different notation for the same two midline lengths.

## References
1. B. Chen, Z. Yang, Q. Liu and Y. Li, “Some Geometric Constants Related to the Midline of Equilateral Triangles in Banach Spaces,” *Symmetry* 14 (2022), 348, doi:10.3390/sym14020348. Published 9 February 2022.
2. A. Ahmad, H. Xie and Y. Li, “Some new geometric constants in Banach spaces,” *Advances in Fixed Point Theory* 12 (2022), Article 9, doi:10.28919/afpt/7588.
