# Square-root triangle rigidity and paired three-cycles in a nilpotent-Jacobian polynomial family

## Finding
For any real polynomial \(P\) and \(A>0\), define the polynomial self-map of \(\mathbb R^3\)
\[
F_{A,P}(x,y,z)=\bigl(H,\ z-2AxH,\ AH^2\bigr),\qquad H=P(y+Ax^2).
\]
The Jacobian of this map is pointwise nilpotent. Let \((x_i,y_i,z_i)\), with indices modulo three, be a periodic orbit of *least* period three, and write its **heights** as \(h_i=y_i+Ax_i^2\). If \(h_0,h_1,h_2\) are pairwise distinct, then they are all positive and, after arranging them as \(0<h_{(0)}<h_{(1)}<h_{(2)}\),
\[
\boxed{\sqrt{h_{(2)}}=\sqrt{h_{(0)}}+\sqrt{h_{(1)}}.}
\]
Conversely, for every real \(A>0\) and every \(0<r<s\), there is a real polynomial \(P\) of degree **exactly two** for which the map has **two distinct prime three-cycles**, with opposite cyclic order and the same three distinct heights \(r^2,s^2,(r+s)^2\). Thus the square-root triangle relation is an exact *realizability classification* of the unordered distinct-height triples across this family, not merely a necessary inequality. For a fixed triple and \(A\), the two sign orientations of the three values of \(P\), modulo their common additive constant, give the two quadratic interpolation classes.

In particular, take \(A=1\) and \(P(t)=(-3t^2+35t-32)/20\). Two disjoint prime three-cycles are
\[
(2,-3,4)\to(0,4,0)\to(3,0,9)\to(2,-3,4)
\]
and
\[
(3,-8,9)\to(0,9,0)\to(2,0,4)\to(3,-8,9).
\]
Both have three distinct heights, unlike the two-equal-height cycles constructed in the preceding nilpotent-Jacobian literature.

## Assumptions and scope
The phase space is all of \(\mathbb R^3\); \(A>0\) is real and \(P\) is any real polynomial. The Jacobian statement holds without the sign restriction on \(A\). Height rigidity concerns only cycles with three *pairwise distinct* heights; it is not a classification of all periodic orbits of a fixed map. The converse allows \(P\) to depend on \(r,s,A\). Nonzero three distinct heights rule out fixed-point and shorter cycles automatically.

## Proof
**1. Nilpotent Jacobian and the two-dimensional return.** Set \(t=y+Ax^2\), \(p=P'(t)\), and \(H=P(t)\). Differentiation gives
\[
DF_{A,P}=\begin{pmatrix}
2Axp&p&0\\
-2AH-4A^2x^2p&-2Axp&1\\
4A^2xHp&2AHp&0
\end{pmatrix}.
\]
Its trace and determinant vanish (the last row is \(2AH\) times the first), and direct multiplication yields \(\operatorname{tr}(DF_{A,P}^2)=0\). Newton's identities imply the characteristic polynomial is \(\lambda^3\), so Cayley–Hamilton gives \((DF_{A,P})^3=0\) at every point.

Write \(h_n=y_n+Ax_n^2\). The coordinate recurrence is
\[
x_{n+1}=P(h_n),\qquad z_{n+1}=Ax_{n+1}^2,
\qquad h_{n+1}=z_n-2Ax_nx_{n+1}+Ax_{n+1}^2.
\]
On any periodic orbit, the equality \(z_n=Ax_n^2\) holds at every index. Consequently,
\[
h_{n+1}=A(x_n-x_{n+1})^2
=A\bigl(P(h_{n-1})-P(h_n)\bigr)^2.
\]
For a period-three orbit, this means, with \(q_i=P(h_i)\),
\[
h_i=A(q_{i+1}-q_{i+2})^2 \quad (i\bmod3).
\]

**2. Necessity.** Each height is nonnegative. If one height vanishes, the corresponding pair of \(q\)-values coincides; the other two displayed squared differences are then equal, so the two other heights coincide. This contradicts pairwise distinctness. Hence all heights, and all three pairwise \(q\)-differences, are nonzero. Three distinct real points \(q_0,q_1,q_2\) have pairwise distances whose maximum is the sum of the other two. Since their squared pairwise distances are exactly the heights divided by \(A\), taking square roots yields the asserted equality.

**3. Complete converse and the paired cycles.** Choose \(0<r<s\), put \(t=r+s\), and define \(P\) as the unique interpolating polynomial of degree at most two with
\[
P(r^2)=0,\qquad P(s^2)=t/\sqrt A,\qquad P(t^2)=s/\sqrt A.
\]
The secant slopes of these prescribed values over the two adjacent intervals have opposite signs (respectively positive and negative), so \(P\) actually has degree two. Its three pairwise squared differences satisfy
\[
A(P(s^2)-P(t^2))^2=r^2,\quad
A(P(t^2)-P(r^2))^2=s^2,\quad
A(P(r^2)-P(s^2))^2=t^2.
\]
Therefore the height recurrence closes with height itinerary \((r^2,s^2,t^2)\), and also with its reversal \((r^2,t^2,s^2)\). For either itinerary, reconstruct the coordinates from
\[
x_n=P(h_{n-1}),\qquad z_n=Ax_n^2,\qquad y_n=h_n-Ax_n^2.
\]
The identities just established show by substitution that each reconstructed triple maps to its successor. Because the heights are all distinct, both orbits have least period three; the reversal is not a cyclic permutation, so they are distinct. Conversely, for a fixed increasing triple, the pairwise distances determine the three numbers \(q_i\) up to translation and simultaneous sign reversal, and quadratic interpolation is unique. This proves the two interpolation classes modulo an additive constant.

**4. Rational exact witness.** With \(r=1\), \(s=2\), \(A=1\), the interpolating polynomial is \(P(t)=(-3t^2+35t-32)/20\), giving \(P(1)=0\), \(P(4)=3\), \(P(9)=2\). Substitution into \(F_{1,P}\) gives both displayed cycles exactly.

## Verification
Run `python check.py` with SymPy. It checks symbolic Jacobian nilpotence, both three-step rational cycles, pairwise disjointness, their height itineraries, and the quadratic interpolation identities for five additional rational parameter pairs. This finite script verifies the example and algebraic identities only; the universal quantifiers follow from the proof above.

## Relationship to prior work
Castañeda and Rebollo–Perdomo (arXiv:2209.06986v1, 15 September 2022) classify a larger family of pointwise nilpotent-Jacobian polynomial maps; their Theorem 1.1 supplies a three-cycle constructed from a scalar equation. The displayed constructed cycle has **two equal heights** and belongs to a different branch from the three-distinct-height cycles classified here. They explicitly raise questions about three-cycle uniqueness and further periods. Chamberland's earlier study of nilpotent-Jacobian maps gives a general reduction and constructs zero-coordinate three-cycles, and analyzes the linear reduced map; it does not supply this square-root height spectrum or the quadratic interpolation converse. A mathematical-record search for equivalent statements found a closest result about a four-cycle degree threshold, which does not imply the distinct-height three-cycle classification.

## Limitations
No total count, stability classification, or basin description for all prime three-cycles of a fixed polynomial is claimed. The additive-height equality relies on \(A>0\); negative and zero values lie outside that assertion. A polynomial interpolated here is selected to realize a prescribed height triple, rather than asserting that an arbitrary fixed \(P\) realizes every such triple. Literature indexing is not exhaustive, and independent audit has not been performed.

## References
Castañeda, Á. and Rebollo–Perdomo, S. *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1, first submitted 2022-09-15, https://arxiv.org/html/2209.06986v1. Chamberland, M., *Dynamics of Maps with Nilpotent Jacobians*, preprint dated 2005-05-17, https://chamberland.math.grinnell.edu/papers/nilpotent.pdf (later published in Journal of Difference Equations and Applications 12 (2006), 49–56).
