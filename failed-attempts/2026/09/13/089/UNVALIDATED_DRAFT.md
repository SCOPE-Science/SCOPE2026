# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit proper 4-colouring of the \(1/\sqrt2\)-sphere orthogonality graph

Let \(r=1/\sqrt2\) and \(S=\{x\in\mathbb R^3:\lvert x\rvert=r\}\).
Join distinct \(x,y\) when \(\lvert x-y\rvert=1\).
Since \(\lvert x-y\rvert^2=\lvert x\rvert^2+\lvert y\rvert^2-2\langle x,y\rangle
=1-2\langle x,y\rangle\), for \(x,y\in S\) the edge condition is exactly
\(\langle x,y\rangle =0\).
Write \(G(S)\) for this graph. The triple
\((r,0,0),(0,r,0),(0,0,r)\) is a triangle, so \(\chi(G(S))\ge 3\).

**Theorem.** \(G(S)\) is properly colourable with \(4\) colours.
Hence \(\chi(G(S))\le 4\); in particular \(\chi(G(S))\ge 5\) is false,
and \(\chi(G(S))\in\{3,4\}\).

## 1. The colouring

Colours are \(\{1,2,3,4\}\). Put \(Z=\{x\in S:x_1x_2x_3=0\}\) (union of the
three coordinate great circles) and call \(S\setminus Z\) the interior.

(A) Interior (\(x_1,x_2,x_3\ne 0\)). Colour by octant up to antipode:
\[
\begin{array}{c|c}
\text{signs }\pm & \text{colour}\\ \hline
{+++}/{---} & 1\\
{++-}/{--+} & 2\\
{+-+}/{-+-} & 3\\
{-++}/{+--} & 4
\end{array}
\]
i.e. opposite open octants share a colour, giving four classes
\(O_s\cup O_{-s}\).

(B) Axes (two coordinates zero):
\(X_\pm=(\pm r,0,0)\mapsto 1\), \(Y_\pm=(0,\pm r,0)\mapsto 2\),
\(Z_\pm=(0,0,\pm r)\mapsto 3\).

(C) Open arcs (exactly one coordinate zero):
- \(C_{12}=\{x_3=0,\ x_1x_2\ne0\}\): colour \(1\) if \(x_1x_2>0\), \(4\) if
  \(x_1x_2<0\).
- \(C_{13}=\{x_2=0,\ x_1x_3\ne0\}\): colour \(1\) if \(x_1x_3>0\), \(4\) if
  \(x_1x_3<0\).
- \(C_{23}=\{x_1=0,\ x_2x_3\ne0\}\): colour \(4\) if \(x_2x_3>0\), \(2\) if
  \(x_2x_3<0\).

Every point of \(S\) falls in exactly one of (A),(B),(C).

## 2. Interior–interior pairs

If \(x,y\) lie in the same open octant \(O_s\), each product \(x_iy_i>0\),
so \(\langle x,y\rangle>0\). If \(x\in O_s,\ y\in O_{-s}\), each product
\(x_iy_i<0\), so \(\langle x,y\rangle<0\). In either case it is nonzero.
Hence each of the four sets \(O_s\cup O_{-s}\) is independent.

## 3. Interior–boundary pairs

Let \(z\in Z\) and let \(s\in\{\pm1\}^3\). A point \(y\in O_s\) with
\(\langle z,y\rangle=0\) exists iff \(\sum_i z_i s_i\lvert y_i\rvert=0\)
for some \(\lvert y_i\rvert>0\), i.e. iff the numbers \(s_iz_i\) take both
a strictly positive and a strictly negative value. Indeed, if they are
all \(\ge0\) with one \(>0\) (some \(z_i\ne0\) exists) the sum is \(>0\);
if all \(\le0\) with one \(<0\) it is \(<0\); if both signs occur choose
weights to cancel; zeros contribute nothing.

Consequently \(z\) can share the colour of the pair \(\{s,-s\}\) safely
iff \(s_iz_i\) does **not** take both signs. Axis points have only one
nonzero coordinate, so they never see both signs: they are orthogonal
only to points with a zero coordinate, i.e. to \(Z\), never to the
interior. Hence any colour is safe for axes against the interior.

For a point with exactly one zero, e.g. \(z=(z_1,z_2,0)\),
\(z_1,z_2\ne0\), the condition is that \(s_1z_1,s_2z_2\) have the same
(nonzero) sign. Hence exactly two of the four pairs are allowed:
- \(C_{12}\): \(z_1z_2>0\Rightarrow\{1,2\}\); \(z_1z_2<0\Rightarrow\{3,4\}\).
- \(C_{13}\): \(z_1z_3>0\Rightarrow\{1,3\}\); \(z_1z_3<0\Rightarrow\{2,4\}\).
- \(C_{23}\): \(z_2z_3>0\Rightarrow\{1,4\}\); \(z_2z_3<0\Rightarrow\{2,3\}\).

Our assignment (C) respects these lists:
\(1\in\{1,2\},\ 4\in\{3,4\}\); \(1\in\{1,3\},\ 4\in\{2,4\}\);
\(4\in\{1,4\},\ 2\in\{2,3\}\).
By the criterion above, no boundary point is orthogonal to any interior
point of the same colour. Explicitly, if \(z\) has colour \(c\) from an
allowed pair \(\{s,-s\}\), writing e.g. \(y_i=s_i\lvert y_i\rvert\) gives
\(\langle z,y\rangle=\sum (s_iz_i)\lvert y_i\rvert\ne0\) since all
summands share one sign with at least one nonzero.

## 4. Boundary–boundary pairs

Write the circles \(C_{12}\;(x_3=0)\), \(C_{13}\;(x_2=0)\),
\(C_{23}\;(x_1=0)\) of radius \(r\).

Lemma. Let \(z\in C_{12}\) be non-axial (\(z_1z_2\ne0\)). Its
\(Z\)-neighbours are: two points of \(C_{12}\) (rotation by \(\pm90^\circ\),
also non-axial) and the two poles \(Z_\pm\) (since \(\langle z,Z_\pm\rangle
=0\)). It is orthogonal to no other point of \(Z\): for
\(w=(w_1,0,w_3)\in C_{13}\) non-axial, \(\langle z,w\rangle=z_1w_1\ne0\);
for \(w\in C_{23}\) non-axial, \(\langle z,w\rangle=z_2w_2\ne0\); for
\(X_\pm,Y_\pm\), the dot is \(\pm r z_1\ne0\) resp. \(\pm r z_2\ne0\).
Cyclically: non-axial \(C_{13}\) points meet (in \(Z\)) only same-circle
mates and \(Y_\pm\); non-axial \(C_{23}\) points meet only same-circle
mates and \(X_\pm\). Axis \(X_\pm\) is orthogonal to all of \(C_{23}\);
\(Y_\pm\) to all of \(C_{13}\); \(Z_\pm\) to all of \(C_{12}\).

Proof is direct computation as above. ∎

Consequences for our colours. Same-circle mates by \(\pm90^\circ\) always
join opposite sign-quadrants: e.g. on \(C_{12}\),
\((z_1z_2)(w_1w_2)=(z_1w_1)(z_2w_2)=-(z_1w_1)^2<0\) when
\(z_1w_1+z_2w_2=0\) with all entries nonzero. So mates carry
\(1\)-vs-\(4\) (on \(C_{12}\) and \(C_{13}\)) or \(4\)-vs-\(2\) (on
\(C_{23}\)), hence different. Axis points rotated by \(90^\circ\) stay
axial (multiples of \(90^\circ\)), and the three axial colours
\(1,2,3\) are pairwise distinct, while opposite poles share a colour but
satisfy \(\langle X_+,X_-\rangle=-r^2\ne0\) (similarly \(Y,Z\)), so no
axial monochromatic edge.

Cross pairs: non-axial \(C_{12}\) colours \(\{1,4\}\) vs \(Z_\pm\) colour
\(3\) differ; non-axial \(C_{13}\) colours \(\{1,4\}\) vs \(Y_\pm\) colour
\(2\) differ; non-axial \(C_{23}\) colours \(\{4,2\}\) vs \(X_\pm\) colour
\(1\) differ. All other axial-vs-arc pairs are non-edges by the Lemma
(e.g. \(C_{12}\) arc vs \(X,Y\) has dot \(\pm rz_i\ne0\)), so coincident
colours there (e.g. arc colour \(1\) = \(X\) colour \(1\)) are harmless.
Non-axial arcs on distinct circles are never adjacent (dots \(z_1w_1\) etc.
nonzero), and each axis is adjacent exactly to its opposite circle
(colours differ: \(1\notin\{4,2\}\), \(2\notin\{1,4\}\),
\(3\notin\{1,4\}\)) plus the other four axes (colours distinct).

Thus no two orthogonal points of \(Z\) share a colour.

## 5. Conclusion

Sections 2–4 show no monochromatic pair \(x\ne y\) in \(S\) has
\(\langle x,y\rangle=0\), i.e. distance \(1\). This is an explicit proper
\(4\)-colouring of all of \(G(S)\). Therefore \(\chi(G(S))\le4\), the
claim \(\chi(G(S))\ge5\) is disproved, and with the triangle above
\(\chi(G(S))\in\{3,4\}\).

*Verification.* `output/artifacts/verify_coloring.py` checks octant-pair
independence, list membership, \(20000\) random orthogonal pairs (no
monochromatic edge), all axis–circle adjacencies, and the quadrant lemma
numerically. All checks pass.
