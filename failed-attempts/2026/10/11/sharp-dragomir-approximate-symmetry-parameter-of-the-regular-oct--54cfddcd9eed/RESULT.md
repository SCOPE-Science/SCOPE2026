# Sharp Dragomir approximate-symmetry parameter of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For \(\varepsilon\in[0,1)\), write \(u\perp_D^\varepsilon v\) when
\[
N(u+\lambda v)\ge \sqrt{1-\varepsilon^2}\,N(u)
\qquad(\lambda\in\mathbb R).
\]
Then the least \(\varepsilon\) such that
\[
x\perp_B y\Longrightarrow y\perp_D^\varepsilon x
\qquad(x,y\in X_8)
\]
is
\[
\varepsilon_D(X_8)=
\sqrt{\frac{5-2\sqrt2}{8}}.
\]
Equivalently,
\[
\inf_{\substack{x,y\in S_{X_8}\\x\perp_B y}}
\inf_{\lambda\in\mathbb R}N(y+\lambda x)
=
\frac{2+\sqrt2}{4}.
\]
Equality is attained by \(x=(1,\sqrt2-1)\), \(y=(0,-1)\), and their images under the dihedral norm symmetries.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
N(x+\lambda y)\ge N(x)
\qquad(\lambda\in\mathbb R).
\]
The approximate relation is the modified Dragomir relation
\[
u\perp_D^\varepsilon v
\quad\Longleftrightarrow\quad
N(u+\lambda v)\ge\sqrt{1-\varepsilon^2}\,N(u)
\qquad(\lambda\in\mathbb R).
\]
Only the regular-octagonal real plane is treated.

## Proof
Put
\[
a=\sqrt2-1.
\]
The unit ball has vertices
\[
(\pm1,\pm a),\qquad(\pm a,\pm1),
\]
with the signs arranged around the boundary. The norm is invariant under coordinate interchange and independent sign changes. Its dual norm is
\[
N^*(p,q)
=
\max\left\{
|p|+a|q|,
a|p|+|q|
\right\}.
\]

For a unit Birkhoff pair define
\[
d(x,y)=\inf_{\lambda\in\mathbb R}N(y+\lambda x).
\]
The optimal global parameter satisfies
\[
\sqrt{1-\varepsilon_D(X_8)^2}
=
\inf_{\substack{x,y\in S_{X_8}\\x\perp_B y}}d(x,y).
\]

Every smooth boundary point is carried by a norm symmetry to
\[
x_t=(1,t),
\qquad
0\le t<a.
\]
Its unique norming functional is \(f(s,r)=s\), hence every unit Birkhoff direction is \(y=(0,\pm1)\). It is enough to take \(y=(0,1)\).

The functional
\[
\phi_t(s,r)=r-ts
\]
annihilates \(x_t\). Since
\[
N^*(-t,1)=1+at,
\]
duality gives, for every \(\lambda\),
\[
N(y+\lambda x_t)
\ge
\frac{|\phi_t(y+\lambda x_t)|}{N^*(-t,1)}
=
\frac1{1+at}.
\]
Equality is attained at
\[
\lambda=-\frac{a}{1+at},
\]
because then
\[
y+\lambda x_t
=
\frac{(-a,1)}{1+at},
\]
whose norm is \(1/(1+at)\). Therefore
\[
d(x_t,y)=\frac1{1+at}
\ge
\frac1{1+a^2}.
\]

It remains to treat a vertex. By symmetry fix
\[
x=(1,a).
\]
The two adjacent norming functionals are
\[
f_0(s,t)=s,
\qquad
f_1(s,t)=\frac{s+t}{\sqrt2}.
\]
James' support-functional characterization says that \(x\perp_B y\) exactly when some norming functional at \(x\) annihilates \(y\). The kernels of the convex segment joining \(f_0\) and \(f_1\) give, up to sign and scale, precisely the directions
\[
d_r=(r,-1),
\qquad
0\le r\le1.
\]
Their norms are
\[
m(r)=N(d_r)
=
\begin{cases}
1,&0\le r\le a,\\[2mm]
(1+r)/\sqrt2,&a\le r\le1.
\end{cases}
\]
Thus set
\[
y_r=\frac{d_r}{m(r)}.
\]

The functional
\[
\psi(s,t)=t-as
\]
annihilates \(x\), and
\[
N^*(-a,1)=1+a^2.
\]
Hence
\[
d(x,y_r)
\ge
\frac{1+ar}{m(r)(1+a^2)}.
\]
This lower bound is exact. Indeed, if
\[
c_r=\frac{1+ar}{m(r)(1+a^2)},
\qquad
\lambda_r=ac_r-\frac r{m(r)},
\]
then
\[
y_r+\lambda_r x=c_r(a,-1),
\]
and \(N(a,-1)=1\).

Therefore
\[
d(x,y_r)=
\frac{1+ar}{m(r)(1+a^2)}.
\]
On \(0\le r\le a\), this increases with \(r\), so its minimum is
\[
\frac1{1+a^2}
\]
at \(r=0\). On \(a\le r\le1\),
\[
d(x,y_r)
=
\frac{\sqrt2(1+ar)}{(1+r)(1+a^2)},
\]
which decreases because \(a<1\), and at \(r=1\) again equals \(1/(1+a^2)\).

All smooth edge points and all vertices have now been exhausted by the dihedral symmetries. Consequently
\[
\inf_{\substack{x,y\in S_{X_8}\\x\perp_B y}}d(x,y)
=
\frac1{1+a^2}
=
\frac{2+\sqrt2}{4}.
\]
Thus
\[
\varepsilon_D(X_8)^2
=
1-\left(\frac{2+\sqrt2}{4}\right)^2
=
\frac{5-2\sqrt2}{8},
\]
which proves the claim.

For the explicit sharp pair
\[
x=(1,a),
\qquad
y=(0,-1),
\]
the functional \(f_0\) norms \(x\) and annihilates \(y\), so \(x\perp_B y\), and the reverse line distance equals \((2+\sqrt2)/4\).

## Verification
The unit sphere is polygonal, so every point is either in the relative interior of an edge or is a vertex. The dihedral symmetry reduces all smooth edge points to \(x_t=(1,t)\), \(0\le t<a\), and all vertices to \(x=(1,a)\).

The dual norm formula is obtained by maximizing a functional over the eight vertices. In each case the dual lower bound for distance to the line is accompanied by an explicit translate attaining equality; no compactness or numerical search is used to infer the exact distance.

The final radical identity is
\[
\frac1{1+(\sqrt2-1)^2}
=
\frac{2+\sqrt2}{4},
\qquad
1-\left(\frac{2+\sqrt2}{4}\right)^2
=
\frac{5-2\sqrt2}{8}.
\]

## Relationship to prior work
Komuro, Saito, and Tanaka identify the regular octagonal norm as a standard non-Euclidean example with James constant \(\sqrt2\). Their article was first published online on 19 November 2015.

Chmieliński, Khurana, and Sain define the modified Dragomir approximate relation, recall James' support-functional characterization of Birkhoff--James orthogonality, and prove that every finite-dimensional Banach space is globally D-approximately symmetric. Their full text also treats regular two-dimensional polyhedral spaces for the distinct C-approximate symmetry. It does not state a sharp D-parameter for the regular octagon.

Targeted searches for the regular octagonal norm, Birkhoff--James approximate symmetry, modified Dragomir symmetry, and the exact radical above did not locate an equivalent evaluation. Exact indexed results for the same octagon concern other invariants, while the closest exact D-symmetry calculation concerns different Hölder-dual planes.

## Limitations
The theorem determines the modified-Dragomir parameter only for the real regular octagonal plane. It does not determine the distinct C-approximate-symmetry parameter, nor the full family of regular \(2n\)-gonal norms.

The 2015 regular-octagon source was inspected through its publisher record and abstract rather than a complete article text in this run. The decisive approximate-symmetry source was inspected in full. A differently notated exact octagonal calculation remains a bibliographic risk.

## References
1. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” *Mathematische Nachrichten* 289 (2016), 1005--1020, DOI 10.1002/mana.201500238; first published online 2015-11-19.
2. J. Chmieliński, D. Khurana, and D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” arXiv:2012.08162, first posted 2020-12-15; later *Results in Mathematics* 76 (2021), DOI 10.1007/s00025-021-01437-y.
