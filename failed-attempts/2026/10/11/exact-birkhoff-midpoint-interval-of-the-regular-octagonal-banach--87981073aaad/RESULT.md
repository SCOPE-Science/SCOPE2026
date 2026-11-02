# Exact Birkhoff midpoint interval of the regular octagonal Banach plane
## Finding
Let \(X_8=(\mathbb R^2,N_8)\), where
\[
N_8(s,t)=
\max\left\{
|s|,\ |t|,\ \frac{|s|+|t|}{\sqrt2}
\right\}.
\]
For unit Birkhoff-orthogonal pairs, the complete oriented sum-length range is
\[
\left\{
N_8(x+y):
x,y\in S_{X_8},\ x\perp_B y
\right\}
=
\left[
\frac{3\sqrt2}{2}-1,\
1+\frac1{\sqrt2}
\right].
\]
Therefore the Birkhoff moduli introduced by Du and Li are
\[
\delta_B(X_8)=\frac{2-\sqrt2}{4},
\qquad
\rho_B(X_8)=\frac{3(2-\sqrt2)}{4}.
\]
In particular,
\[
\rho_B(X_8)=3\,\delta_B(X_8).
\]

## Assumptions and scope
All scalars are real. Birkhoff orthogonality means
\[
x\perp_B y
\quad\Longleftrightarrow\quad
N_8(x+\lambda y)\ge N_8(x)
\quad\text{for every }\lambda\in\mathbb R.
\]
In a finite-dimensional normed space this is equivalent to the supporting-functional condition: there exists a norming functional \(f\) for \(x\) such that \(f(y)=0\).

Put
\[
r=\sqrt2-1,\qquad
q=\frac1{\sqrt2},\qquad
d=2-\sqrt2.
\]
A fundamental octagonal edge is
\[
E=[a,b],
\qquad
a=(1,r),\quad b=(r,1).
\]
The dihedral symmetries of \(N_8\), together with \(y\mapsto-y\), reduce every unit Birkhoff-orthogonal pair to either an interior point of \(E\) or the vertex \(a\).

Du and Li define
\[
\delta_B(X)
=
\inf_{\substack{x,y\in S_X\\x\perp_B y}}
\left(1-\frac{\|x+y\|}{2}\right),
\qquad
\rho_B(X)
=
\sup_{\substack{x,y\in S_X\\x\perp_B y}}
\left(1-\frac{\|x+y\|}{2}\right).
\]

## Proof
First suppose that \(x\) lies in the relative interior of \(E\). Write
\[
x_t=(1-t)a+tb,\qquad 0\le t\le1.
\]
The unique norming functional on that edge is
\[
f(s,t)=\frac{s+t}{\sqrt2}.
\]
Hence Birkhoff orthogonality forces
\[
y=\pm(q,-q).
\]
Direct substitution gives
\[
N_8\bigl(x_t+(q,-q)\bigr)
=
1+\frac1{\sqrt2}-dt,
\]
and
\[
N_8\bigl(x_t-(q,-q)\bigr)
=
\frac{3\sqrt2}{2}-1+dt.
\]
Since
\[
\left(1+\frac1{\sqrt2}\right)
-
\left(\frac{3\sqrt2}{2}-1\right)
=
2-\sqrt2=d,
\]
the interior-edge cases fill the entire interval
\[
\left[
\frac{3\sqrt2}{2}-1,\
1+\frac1{\sqrt2}
\right].
\]

It remains to check that a nonsmooth vertex cannot escape this interval. At
\[
a=(1,r),
\]
the norming functionals form the segment between
\[
f_0(s,t)=s
\quad\text{and}\quad
f_1(s,t)=\frac{s+t}{\sqrt2}.
\]
The unit vectors annihilated by some functional in this segment form, up to sign, the boundary arc from \((0,-1)\) to \((q,-q)\). This arc has two pieces:
\[
C_1=\{(s,-1):0\le s\le r\},
\]
and
\[
C_2=\{(s,s-\sqrt2):r\le s\le q\}.
\]

For \(y=(s,-1)\in C_1\),
\[
N_8(a+y)
=
\frac{3-\sqrt2+s}{\sqrt2},
\]
which increases from
\[
\frac{3\sqrt2}{2}-1
\]
to \(\sqrt2\). For \(y=(s,s-\sqrt2)\in C_2\),
\[
N_8(a+y)=1+s,
\]
which increases from \(\sqrt2\) to
\[
1+\frac1{\sqrt2}.
\]

The opposite arc gives the remaining orientations. For \(y=(s,-1)\in C_1\),
\[
N_8(a-y)
=
1+\frac{1-s}{\sqrt2},
\]
which decreases from
\[
1+\frac1{\sqrt2}
\]
to \(\sqrt2\). For \(y=(s,s-\sqrt2)\in C_2\),
\[
N_8(a-y)
=
2\sqrt2-1-s,
\]
which decreases from \(\sqrt2\) to
\[
\frac{3\sqrt2}{2}-1.
\]
Thus no vertex-support choice produces a value outside the interval already obtained from edge pairs.

Both endpoints are attained by explicit Birkhoff-orthogonal pairs:
\[
x=(1,r),\qquad y=(0,-1)
\]
gives
\[
N_8(x+y)=\frac{3\sqrt2}{2}-1,
\]
while
\[
x=(1,r),\qquad y=(q,-q)
\]
gives
\[
N_8(x+y)=1+\frac1{\sqrt2}.
\]

Finally, because \(z\mapsto1-z/2\) is decreasing,
\[
\delta_B(X_8)
=
1-\frac12\left(1+\frac1{\sqrt2}\right)
=
\frac{2-\sqrt2}{4},
\]
and
\[
\rho_B(X_8)
=
1-\frac12\left(\frac{3\sqrt2}{2}-1\right)
=
\frac{3(2-\sqrt2)}{4}.
\]

## Verification
The bundled `verify.py` works exactly in \(\mathbb Q(\sqrt2)\). It reconstructs the eight signed supporting facets of the regular octagon and verifies the unit vertices and active supports.

For each of the six one-parameter pieces used in the proof—two smooth-edge orientations and four vertex-arc orientations—the checker certifies the claimed norm formula on the whole segment. It does this by checking every signed facet inequality at both endpoints; because every facet difference is affine in the segment parameter, endpoint validity proves the inequality throughout the segment. A common active facet at both endpoints supplies equality throughout.

The checker also verifies the endpoint Birkhoff witnesses and the algebraic conversions to \(\delta_B\) and \(\rho_B\). No floating-point sampling is used as proof.

## Relationship to prior work
Du and Li introduced \(\delta_B\) and \(\rho_B\), established their universal bounds and structural relations, proved
\[
\rho_B(X)=1-\frac1{\mu'(X)},
\]
and treated Hilbert, square and affine-regular-hexagonal examples. Their inspected full text contains no regular-octagonal computation.

Baronti and Papini had earlier computed the orthogonal James and Schäffer constants of the same regular octagonal plane:
\[
J_\perp(X_8)=g_\perp(X_8)=\sqrt2.
\]
Those quantities use
\[
\min\{\|x+y\|,\|x-y\|\}
\quad\text{and}\quad
\max\{\|x+y\|,\|x-y\|\},
\]
so their equality does not determine the separate oriented extrema of \(\|x+y\|\). The present interval is therefore strictly more specific information about Birkhoff-orthogonal midpoint geometry.

The closest public regular-octagon records located in the research index concern other objectives, including a unit-separation angle modulus and a Birkhoff-orthogonal geometric-mean constant; neither implies this oriented sum interval.

## Limitations
The proof is specific to the regular octagonal plane. It does not give a formula for \(\delta_B\) or \(\rho_B\) for every regular polygonal norm.

The result determines the complete range of the single oriented quantity \(N_8(x+y)\). It does not classify the joint two-coordinate set
\[
\bigl(N_8(x+y),N_8(x-y)\bigr)
\]
for all Birkhoff-orthogonal pairs.

Bibliographic and research-index searches cannot prove absolute novelty. An equivalent calculation could appear under the older \(\mu'(X)\) notation or another sum-length parameter, although targeted searches for those formulations and inspection of the closest same-space primary paper found no such result.

## References
1. D. Du and Y. Li, “Some Moduli and Inequalities Related to Birkhoff Orthogonality in Banach Spaces,” Australian Journal of Mathematical Analysis and Applications 20 (2023), No. 1, Art. 2, 15 pp. Published 31 January 2023. Primary MSC 46B20.
2. M. Baronti and P. L. Papini, “Parameters in Banach Spaces and Orthogonality,” Constructive Mathematical Analysis 5 (2022), 37–45, doi:10.33205/cma.1067323.
