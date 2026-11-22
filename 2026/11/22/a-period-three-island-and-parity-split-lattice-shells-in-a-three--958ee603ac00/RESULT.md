# A period-three island and parity-split lattice shells in a three-season tropical Lyness map

## Finding

Let \(T_a:\mathbb R^2\to\mathbb R^2\) be the max-plus Lyness step
\[
T_a(x,y)=(y,\max\{a,y\}-x),
\]
and take the three-season return map \(F=T_1\circ T_1\circ T_0\), with the rightmost map applied first. Define
\[
H(x,y)=\max\{x+1,\ y,\ x-y+1,\ y-x+1,\ 2-y,\ 1-x,\ 1-x-y\}.
\]
Then \(H\circ F=H\) everywhere, \(\min H=4/3\), and the minimum is attained only at \(p_*=(1/3,2/3)\), the unique fixed point of \(F\).

For each real \(h>4/3\), the level \(\Gamma_h=\{H=h\}\) is a simple closed polygon. Using counterclockwise primitive lattice arclength as a circle coordinate, \(F\vert_{\Gamma_h}\) is **exactly** a rigid rotation of fraction
\[
\rho(h)=\begin{cases}
1/3,&4/3<h\le2,\\[2pt]
(2h-2)/(5h-4),&h\ge2.
\end{cases}
\]
Thus the nonempty interior \(\{H<2\}\) is an *isochronous period-three island*: except for \(p_*\), every point there has least period three. The energy \(h=2\) is a sharp triangular-to-hexagonal boundary, after which \(\rho\) strictly increases from \(1/3\) to the unattained limit \(2/5\). Each \(r\in(1/3,2/5)\) occurs on exactly one energy level. If \(h>2\) is irrational then every orbit in \(\Gamma_h\) is dense and aperiodic; if \(h=p/q>2\), with coprime positive integers \(p,q\), all points in \(\Gamma_h\) have least period
\[
\frac{5p-4q}{\gcd(p,2)}.
\]

**Integer lattice law.** Every point of \(\mathbb Z^2\) is periodic. For each integer energy \(m\ge2\), the \(5m-4\) points of \(\Gamma_m\cap\mathbb Z^2\) split into exactly \(\gcd(m,2)\) primitive temporal orbits, each of period \((5m-4)/\gcd(m,2)\). Hence odd shells consist of one orbit and even shells of exactly two.

## Assumptions and scope

The domain is the entire real plane with the ordinary maximum, not the positive quadrant. Time is counted in three-step returns of the nonautonomous sequence \(0,1,1\); it is not the number of individual Lyness steps. Integer lattice points are labelled, not identified under sign, translation or spatial symmetry. Primitive temporal periods are the least positive return iterates under \(F\). At \(h=4/3\) the level reduces to the single fixed point; for \(4/3<h\le2\) the level is triangular, and for \(h>2\) it is hexagonal.

The parameter pattern is one of the two nonconstant binary three-season patterns up to cyclic phase permutation; the other is \((0,0,1)\). This result concerns the two-high-season pattern, not the other return map.

## Proof

**1. Conservation and minimum.** For \(q>0\), put \(R_a(u,v)=(v,(a+v)/u)\) on the positive quadrant. The rational three-step map \(R_q\circ R_q\circ R_1\) preserves the explicit positive Laurent function
\[
V_q(u,v)=\frac{q u^2v+uv^2+q u^2+q v^2+(1+q^2)u+2qv+q}{uv}.
\]
This is the three-periodic Lyness integral recorded in Cima, Gasull and Mañosa (2009); the identity can also be checked by direct common-denominator expansion. The complete symbolic equality is checked separately by the packaged script, which uses the independently computed rational iterates.

Set \(q=e^t\), \(u=e^{tx}\), and \(v=e^{ty}\). Positivity rules out leading-term cancellation. As \(t\to\infty\), the map of logarithmic coordinates tends to \(F\), while \(t^{-1}\log V_{e^t}(e^{tx},e^{ty})\) tends to the displayed seven-term maximum \(H\). By continuity and conservation at each \(t\), \(H(F(x,y))=H(x,y)\) for every real \((x,y)\).

The inequalities \(x+1\le h\), \(2-y\le h\), and \(y-x+1\le h\) require \(x\le h-1\), \(y\ge2-h\), and \(y\le x+h-1\), hence \(h\ge4/3\). Equality holds only at \((1/3,2/3)\), where each of the seven affine forms is at most \(4/3\). Substitution into \(F\) shows that this point is fixed.

**2. All invariant polygons.** Direct intersection of the seven half-planes \(H\le h\) gives, for \(4/3<h\le2\), the counterclockwise vertices
\[
A=(3-2h,2-h),\qquad B=(h-1,2-h),\qquad C=(h-1,2h-2).
\]
Their three primitive lattice lengths are all \(3h-4\), so the total affine perimeter is \(L(h)=9h-12\). For \(h>2\) the counterclockwise vertices are
\[
\begin{aligned}
A&=(1-h,0),&B&=(-1,2-h),&C&=(1,2-h),\\
D&=(h-1,0),&E&=(h-1,h),&G&=(1,h).
\end{aligned}
\]
The successive primitive lattice lengths are \(h-2,2,h-2,h,h-2,h\), summing to \(L(h)=5h-4\). At \(h=2\) the latter six-vertex expression degenerates to the former triangle and both perimeter formulas give six. These descriptions follow from the seven explicit supporting inequalities, not numerical polygon fitting.

**3. Rigid rotation rather than merely a rotation number.** On either affine branch, \(T_a\) has integer linear part
\[
\begin{pmatrix}0&1\\-1&1\end{pmatrix}
\quad\text{or}\quad
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
with determinant one. Every \(T_a\) is an orientation-preserving homeomorphism (its inverse is \(T_a^{-1}(u,v)=(\max\{a,u\}-v,u)\)). Therefore \(F\) preserves \(\Gamma_h\), its counterclockwise orientation and the primitive lattice arclength locally: an integral unimodular matrix sends any primitive integer tangent to another primitive integer tangent. Splitting an arc at branch intersections and adding its primitive lengths proves global arclength preservation. A circle orientation-preserving arclength isometry is a rigid rotation.

For the triangle \(F(A)=B\), giving counterclockwise displacement \(3h-4\) out of \(9h-12\). In fact throughout the closed sublevel \(\{H\le2\}\), each branch is fixed and
\[
F(x,y)=(1-y,1+x-y),
\]
whose nontrivial points have least period three. For the hexagon \(F(A)=D\); the counterclockwise path \(A\to B\to C\to D\) has length \((h-2)+2+(h-2)=2h-2\), out of \(5h-4\). This proves the displayed \(\rho(h)\), including all boundary points. Its outer derivative is \(2/(5h-4)^2>0\). The rational/irrational circle-rotation alternatives are now exact. If \(h=p/q>2\) is reduced, the rotation fraction is \(2(p-q)/(5p-4q)\); its numerator and denominator have gcd \(\gcd(p,2)\), yielding the exact least period claimed.

**4. Lattice classification.** For integer \((x,y)\), the maximum \(H(x,y)\) is an integer not less than two, so every lattice point lies on some \(\Gamma_m\), \(m\ge2\). The polygon vertices are integral and each edge displacement is an integer multiple of a primitive lattice vector. Consequently the number of distinct lattice points on \(\Gamma_m\) equals its integer primitive perimeter \(L(m)=5m-4\). The restriction of \(F\) rotates these evenly spaced lattice points by exactly \(2m-2\) steps. Its orbit count is
\[
\gcd(5m-4,2m-2)=\gcd(m,2),
\]
and each orbit has least period \((5m-4)/\gcd(m,2)\). This also covers \(m=2\) by the shared triangle/hexagon boundary formula.

## Verification

The included `verify.py` runs an exact SymPy polynomial identity for the rational first integral, including the explicit rational three-step map. Using rational arithmetic, it then verifies the claimed half-plane vertices and arclength shift on 502 rational energy levels, 3,536 off-level plane points, and all boundary sample positions; it exhaustively computes the lattice cycles at energies 2 through 50 (6,174 integer points). The accompanying `verification_output.txt` records a successful execution. All-level validity comes from the preceding analytic and integer-affine arguments, **not** from extrapolating these finite checks.

Representative integer levels: \(m=2\) has two three-cycles among six points; \(m=3\) has one eleven-cycle; \(m=4\) has two eight-cycles; \(m=5\) has one twenty-one-cycle; \(m=6\) has two thirteen-cycles.

Reproduce with Python 3 and SymPy installed using `python verify.py` from the extracted file directory.

## Relationship to prior work

Cima, Gasull and Mañosa (2009, arXiv:0912.5031) give the three-periodic rational Lyness invariant and circle-rotation framework for positive rational recurrences. The Laurent integral used above is credited to them. Their rational positive-quadrant results do not themselves specify the particular max-plus three-season return, its triangular isochronous island, its piecewise affine rotation fraction or its integer-shell parity decomposition. Their 2010 preprint arXiv:1012.4925 treats general nonautonomous rational Lyness integrability, not this exact lattice classification.

Autonomous max-type Lyness periodicity is addressed by De Angelis (2004) and by Gelisken, Cinar and Karatas (2007), but the single fixed coefficient in those recurrences does not supply the three-season return dynamics here. De Angelis gives an explicit circle-rotation conjugacy for one autonomous max map, not a rotation fraction for the nonautonomous composition studied here. Northshield's *Tropical cycles* (2020) discusses classical Lyness cycles. Earlier three-periodic max-recurrence work of Grove–Kent–Ladas–Radin (2001) studies a different update rule, \(u_{n+1}=\max\{-u_n,a_n-u_{n-1}\}\) in logarithmic variables, whereas the present rule is \(u_{n+2}=\max\{a_n,u_{n+1}\}-u_n\). Patula and Voulov (2004) establish eventual periodicity for another three-periodic max-type recurrence; the irrational polygon rotations proved here exclude direct equivalence to a theorem of that conclusion. The 1997 Grove–Kent–Ladas paper studies boundedness and persistence of nonautonomous Lyness and max equations. Their publicly accessible abstracts do not document this exact theorem. Full texts for the older nonautonomous-max articles could not all be inspected, so their historical comparison remains qualified. These are materially closer than autonomous Lyness results, but no identified statement implies the exact level rotation or the lattice parity law.

A different three-season threshold sequence \((0,0,1)\) has a different polygon geometry and nonmonotone rotation response; no identity, affine conjugacy or parameter reduction deriving this triangular island or the odd/even lattice orbit law has been established. The present result proves those phenomena specifically for \((0,1,1)\), not an arbitrary three-season coefficient sequence.

## Limitations

The theorem is exact for the specified three-season max-plus recurrence, not for arbitrary real parameter patterns, higher-dimensional recurrences or the unreduced rational maps. It does not assert equivalence between rational and tropical periods. Search results and accessible full texts cannot prove worldwide priority, especially given the unavailable full 1997 nonautonomous max-equation article and unindexed older literature. No external independent validation has been performed.

## References

1. A. Cima, A. Gasull, V. Mañosa, *On two and three periodic Lyness difference equations*, publicly posted 2009-12-26, arXiv:0912.5031, https://arxiv.org/abs/0912.5031 .
2. A. Cima, A. Gasull, V. Mañosa, *Integrability and non-integrability of periodic non-autonomous Lyness recurrences*, publicly posted 2010-12-22, arXiv:1012.4925, https://arxiv.org/abs/1012.4925 .
3. A. Gelisken, C. Cinar, R. Karatas, *A Note on the Periodicity of the Lyness Max Equation*, published 2007-12-30, https://doi.org/10.1155/2008/651747 .
4. E. A. Grove, C. M. Kent, G. Ladas, *Boundedness and Persistence of the Nonautonomous Lyness and Max Equations*, J. Difference Equations Appl. 3 (1997/1998), 241–258, https://doi.org/10.1080/10236199708808100 .
5. V. De Angelis, *Dynamics of the Lyness Max Map*, Journal of Difference Equations and Applications 10 (2004), 187–200, https://doi.org/10.1080/1023619031000148803 .
6. E. A. Grove, C. M. Kent, G. Ladas, M. A. Radin, *On* \(x_{n+1}=\max\{1/x_n,A_n/x_{n-1}\}\) *with a period 3 parameter*, Fields Institute Communications 29 (2001), 161–180, https://doi.org/10.1090/fic/029/13 .
7. W. T. Patula, H. D. Voulov, *On a Max Type Recurrence Relation with Periodic Coefficients*, Journal of Difference Equations and Applications 10 (2004), 329–338, https://doi.org/10.1080/10236190410001659741 .
8. H. D. Voulov, *On a difference equation with periodic coefficients*, Journal of Difference Equations and Applications 13 (2007), 443–452, https://doi.org/10.1080/10236190701264651 .
9. S. Northshield, *Tropical cycles*, Mathematical Gazette 104 (2020), 225–234, https://doi.org/10.1017/mag.2020.44 .
