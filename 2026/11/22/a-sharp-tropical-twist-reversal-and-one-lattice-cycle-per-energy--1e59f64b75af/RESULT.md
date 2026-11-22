# A sharp tropical twist reversal and one lattice cycle per energy in three-season Lyness dynamics

## Finding

Let
\[
 T_a(x,y)=(y,\max\{a,y\}-x),\qquad F=T_1\circ T_0\circ T_0,
\]
with compositions executed from right to left, and put
\[
 H(x,y)=\max\{-x,-y,-x-y,x-y-1,x,y-1,y-x-1\}.
\]
Then \(H\circ F=H\) on the entire real plane. Every positive level \(C_h=\{(x,y):H(x,y)=h\}\) is a simple convex polygon on which \(F\) is conjugate to a rigid **counterclockwise** circle rotation with exact rotation number
\[
 \boxed{\rho(h)=
 \begin{cases}
 \displaystyle\frac{2h+1}{6h+2},&0<h\le1,\\[4pt]
 \displaystyle\frac{2h+1}{5h+3},&h\ge1.
 \end{cases}}
\]
The shared value at \(h=1\) is \(3/8\). The rotation number decreases strictly on \((0,1)\) and increases strictly on \((1,\infty)\). Thus the hexagon-to-heptagon transition at \(h=1\) is the **unique, sharp twist reversal**, with minimum \(3/8\), limiting inner frequency \(1/2\), and outer limiting frequency \(2/5\). Every frequency in \((3/8,2/5)\) occurs on exactly two distinct positive energy polygons. In particular, \(h=2/3\) and \(h=3\) have the same rotation number \(7/18\) and contain different families of primitive 18-cycles.

Every \(h=p/q>0\) in lowest positive terms has entirely periodic dynamics on \(C_h\), with the common least period
\[
 \boxed{P(p/q)=
 \begin{cases}
 (6p+2q)/\gcd(q,2),&p\le q,\\
 5p+3q,&p\ge q.
 \end{cases}}
\]
(the two branches agree at \(p=q=1\)). Every irrational \(h>0\) has irrational rotation and all its trajectories are dense in \(C_h\). For every integer \(m\ge1\), the exactly \(5m+3\) integer points of \(C_m\) constitute **one primitive \((5m+3)\)-cycle**. The zero level is the segment \(\{(0,t):0\le t\le1\}\), acted on by \(t\mapsto1-t\). Consequently every state in \(\mathbb Z^2\) is periodic immediately: there is one two-cycle at energy zero and one cycle per positive integer energy, and there are no transients.

## Assumptions and scope

All coordinates and levels are real, and only the displayed three-season schedule \((0,0,1)\) is asserted. The one-step map \(T_a\) is a global area-preserving piecewise-affine homeomorphism, with inverse \(T_a^{-1}(u,v)=(\max\{a,u\}-v,u)\). The rotation number is the fraction of a **counterclockwise** boundary turn per application of \(F\), which comprises three elementary seasonal updates. Switching lines and polygon vertices are included. Rational energy means \(p/q\) with \(p,q\) coprime positive integers, not necessarily integer initial coordinates. A circle conjugacy on \(C_h\) refers to the intrinsic boundary topology; no smoothness across its corners is asserted.

## Proof

**1. Exact conservation by tropicalizing a known rational integral.** For positive \(X,Y,a,b,c\), define the rational seasonal Lyness map \(R_a(X,Y)=(Y,(a+Y)/X)\). The classical three-season integral of Cima–Gasull–Mañosa [1, Section 2] is
\[
 V_{c,b,a}(X,Y)=\frac{cX^2Y+aXY^2+bX^2+bY^2+(a+bc)X+(c+ab)Y+ac}{XY},
\]
which is invariant under \(R_c\circ R_b\circ R_a\). This identity can also be checked directly by rational substitution; the accompanying script simplifies the general identity to zero.

For \(\epsilon>0\), set \(a=b=1\), \(c=e^{1/\epsilon}\), \(X=e^{x/\epsilon}\), and \(Y=e^{y/\epsilon}\). Under \((X,Y)\mapsto(\epsilon\log X,\epsilon\log Y)\), the three-step rational map converges, at every real point, to \(F=T_1\circ T_0\circ T_0\), since
\[
 \epsilon\log(e^{u/\epsilon}+e^{v/\epsilon})\longrightarrow\max\{u,v\}.
\]
All terms of \(V\) are positive. The same log-limit therefore sends \(\epsilon\log V\) to
\[
 \max\{1+x,y,x-y,y-x,1-y,1-x,1-x-y\}=H(x,y)+1.
\]
The convergence is locally uniform because each log-sum has finitely many positive terms. Passing to the limit in the exact rational conservation equation proves \(H(F(x,y))=H(x,y)\) for all real \((x,y)\), including the switching lines. The rational invariant itself, and its generic circle dynamics, are prior work; the remaining explicit tropical rotation and arithmetic classifications are the asserted contribution.

**2. Level geometry, area and intrinsic length.** As \(H\ge\max\{x,-x\}\), the zero set forces \(x=0\). Then the inequalities \(-y\le0\) and \(y-1\le0\) give precisely \(0\le y\le1\). For \(h>0\), intersecting the seven half-planes obtained from \(H\le h\) gives a convex polygon. In counterclockwise order its vertices for \(0<h\le1\) are
\[
 (-h,0),\ (0,-h),\ (h,-h),\ (h,h+1),\ (0,h+1),\ (-h,1).
\]
For \(h>1\) the vertices are
\[
 (-h,0),\ (0,-h),\ (1,-h),\ (h,-1),\ (h,h+1),\ (0,h+1),\ (-h,1).
\]
These vertices satisfy the appropriate active inequalities; the consecutive sides lie on the seven supporting lines and exhaust their convex intersection. Hence the boundary equals \(C_h\). Every side is parallel to one of the primitive integer vectors \((1,0),(0,1),(1,1),(1,-1)\). Define its *lattice arclength* by writing a directed side vector as \(\ell d\) with primitive \(d\in\mathbb Z^2\) and \(\ell>0\). Summing sides and applying the shoelace formula gives, without approximation,
\[
 L(h)=\begin{cases}6h+2,&0<h\le1,\\5h+3,&h\ge1,\end{cases}
\qquad
 A(h)=\begin{cases}3h^2+2h,&0<h\le1,\\(5h^2+6h-1)/2,&h\ge1.\end{cases}
\]
In both regimes, \(A'(h)=L(h)\). At \(h=1\), the heptagon loses its extra short edge and becomes a hexagon; both formulas agree continuously.

**3. Global rigid rotation from integral-affine arclength.** Each affine branch of \(T_a\) has derivative
\[
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}
 \quad\text{or}\quad
 \begin{pmatrix}0&1\\-1&1\end{pmatrix},
\]
which is an integer matrix of determinant \(1\). Its displayed inverse and continuity imply it is an orientation- and area-preserving homeomorphism. Thus \(F\), a composition of three such maps, preserves area, orientation and every \(C_h\). Along each polygon side, restrict to finitely many pieces separated by intersections with the switching lines of the composition. Its linear part on any such piece lies in \(\mathrm{SL}_2(\mathbb Z)\), so a primitive integer tangent \(d\) is carried to another primitive integer tangent \(Ad\). The parametrized displacement \(\ell d\mapsto\ell Ad\) has the same lattice arclength \(\ell\). By continuity the full boundary map preserves lattice arclength measure. An orientation-preserving arclength-preserving circle homeomorphism is a rigid rotation in the normalized cumulative arclength coordinate.

Choose base vertex \(z_h=(-h,0)\). The explicit three updates yield
\[
 F(z_h)=\begin{cases}(h,1-h),&0<h\le1,\\(h,0),&h\ge1.\end{cases}
\]
In both regimes the counterclockwise lattice arclength from \(z_h\) to its image is exactly \(2h+1\). Dividing by the total \(L(h)\) yields the asserted two-branch \(\rho(h)\), which lies strictly between zero and one. No further turns are concealed because the image lies on the third or fourth polygon edge as listed.

**4. The sharp twist reversal and double-energy resonance.** Differentiation gives
\[
 \rho'(h)=\begin{cases}
 -1/[2(3h+1)^2],&0<h<1,\\
 1/(5h+3)^2,&h>1.
 \end{cases}
\]
Both one-sided derivatives are nonzero with opposite signs. Relative to the area action \(I=A/(2\pi)\), the derivative \(d\rho/dI=2\pi\rho'(h)/A'(h)\) changes from negative to positive as well. Limits and continuity give the stated strict global minimum and limits. For each \(r\in(3/8,2/5)\), inverting the two branches produces exactly two distinct energy solutions,
\[
 h_-(r)=\frac{1-2r}{6r-2}\in(0,1),\qquad
 h_+(r)=\frac{1-3r}{5r-2}>1.
\]
In particular \(r=7/18\) yields \(h_-=2/3\) and \(h_+=3\).

**5. Rational and lattice orbit classification.** A rigid circle rotation of rational increment \(s/t\) in lowest terms has least period \(t\) at *every* point; an irrational rotation has no periodic points and all orbits are dense. If \(h=p/q>0\) is reduced, the rotation increment is
\[
 \frac{2p+q}{6p+2q}\quad(p\le q),\qquad
 \frac{2p+q}{5p+3q}\quad(p\ge q).
\]
For the first fraction, the common divisor is \(\gcd(q,2)\): it divides the determinant \(2\), and it is \(2\) precisely when \(q\) is even. For the second fraction, any common divisor divides both \(3(2p+q)-(5p+3q)=p\) and \(2(5p+3q)-5(2p+q)=q\), so it equals \(1\). These formulas prove the exact least periods. The two fractional-linear expressions have nonzero derivatives, so \(\rho(h)\) is rational exactly when \(h\) is rational.

For integer \(m\ge1\), all polygon vertices are integral. By subdividing each edge into primitive lattice intervals, its set of boundary lattice points has cardinality \(L(m)=5m+3\). The rotation translates arclength by the integer \(2m+1\); the displayed Bézout identity
\[
 2(5m+3)-5(2m+1)=1
\]
shows the translation acts transitively on those \(5m+3\) points. Every integer point lies on exactly one nonnegative integer energy shell because \(H\) is a maximum of integer-affine forms. On \(H=0\), direct substitution gives \(F(0,t)=(0,1-t)\), proving the final exceptional fixed point at \((0,1/2)\) and the unique integer two-cycle \((0,0)\leftrightarrow(0,1)\).

## Verification

The standalone `verify.py` is executable with Python 3 and SymPy and prints `VERIFY_OK` on success. It independently rechecks the general three-parameter rational first integral symbolically, conserves \(H\) on 6,241 rational samples, tests all rational energy levels \(p/q\) with \(1\le p\le29\), \(1\le q\le17\) in lowest terms, validates polygon perimeter/area and predicted primitive period, explicitly enumerates every boundary lattice point on each shell \(1\le m\le100\), and establishes that the 25,550 tested nonzero-shell lattice points form one orbit per shell. It also checks the distinct equal-frequency 18-cycles and the zero-level action. These finite computations verify the proof inputs and guard against algebraic mistakes; they are not substitutes for the all-level argument above.

## Relationship to prior work

Cima, Gasull and Mañosa [1] developed the **rational** three-periodic Lyness integral explicitly reused in Step 1. They classified rational positive ovals as circles and analyzed nonmonotone rotation for some **two-periodic rational** maps. The rational invariant and the general phenomenon that a rotation number may be nonmonotone are therefore **not** claimed as discoveries here. The new claim is an exact piecewise formula, singular minimum and double-energy rotation resonance for the specified **three-season tropical** system, together with its sharp complete arithmetic orbit census. Their inspected preprint contains neither this tropical update nor these formulas.

Cima, Gasull and Mañosa [2] treat integrability of rational periodic nonautonomous recurrences, not the present piecewise-linear map. Iwao and Takahashi [3] give methods for an **autonomous** piecewise-linear QRT-type map, but not the three-season composition or its change of twist sign. A published tropical Lyness overview [4] studies the autonomous tropical recurrence.

Two published database results on tropical dynamics were inspected in full: an autonomous max-plus QRT map has a different first integral and a monotone exterior rotation [5]; a positively homogeneous tropical rank-two mutation has an energy-independent rotation number [6]. A related earlier mathematical result, a **two-season** tropical Lyness map, has a different composition, invariant, energy domain and rotation expression. None implies the three-season result by simple restriction or parameter substitution; in particular they do not determine the newly located cusp \(h=1\) where the sign of twist changes. This is a claim-implication comparison, not a conclusion of novelty solely from unsuccessful title searches.

## Limitations

The theorem treats only the exact schedule \((0,0,1)\) and its three-update return map. It does not establish integrability for arbitrary forcing sequences, nonsmooth perturbations, nor KAM persistence. The energy-one transition is nonsmooth, so the twist derivatives are one-sided there. Arclength conjugacy is intrinsic lattice arclength, not Euclidean arclength; irrational orbit equidistribution is for normalized lattice arclength, not for ambient area on \(\mathbb R^2\). The proof is internal and has not undergone independent external review; unindexed earlier derivations remain a residual priority risk.

## References

1. A. Cima, A. Gasull, V. Mañosa, *On two and three periodic Lyness difference equations*, arXiv:0912.5031, first posted 2009-12-26; *Journal of Difference Equations and Applications* 18 (2012), 849–864. https://arxiv.org/abs/0912.5031 ; authorized preprint https://ddd.uab.cat/pub/artpub/2012/gsduab_2716/joudifequapp_a2012v18n5p849preprint.pdf .
2. A. Cima, A. Gasull, V. Mañosa, *Integrability and non-integrability of periodic non-autonomous Lyness recurrences*, arXiv:1012.4925 (2010). https://arxiv.org/abs/1012.4925 .
3. D. Takahashi, M. Iwao, *Geometrical Dynamics of an Integrable Piecewise-Linear Mapping*, proceedings (2007), author-posted PDF https://hakotama.jp/laboratory/works/public/2005-NATO-Science-Series.pdf .
4. S. Northshield, *Tropical Cycles*, *Mathematical Gazette* 104 (2020), 225–234, doi:10.1017/mag.2020.44. Abstract and introduction consulted.
5. *Exact action-twist and Pareto rotation spectrum of a max-plus QRT map*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-action-twist-and-pareto-rotation-spectrum-of-a-max-plus-qr--08992945e4c5 .
6. *Exact rotation number and full orbit classification for tropical rank-two mutations*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rotation-number-and-full-orbit-classification-for-tropical--7d107b663bc7 .
