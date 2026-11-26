# Exact chord-quadrilateral area and optimizer classification for a regular nonagon

## Finding
Let \(P_9\) be the regular nonagon of circumradius \(1\), with vertices \((\cos(2j\pi/9),\sin(2j\pi/9))\), \(j=0,\ldots,8\). A chord quadrilateral is a convex polygon of at most four sides containing \(P_9\), with each side parallel to a side or diagonal of \(P_9\). Write \(q_{\mathrm{ch}}(P_9)\) for the minimum of its area, and put \(c=\cos(\pi/9)\), \(s=\sin(\pi/9)\). Then

\[
\boxed{q_{\mathrm{ch}}(P_9)=\frac{5-2c+8c^2}{8s}=3.72229265207569\ldots.}
\]

Since \(\operatorname{area}(P_9)=9sc\), the exact normalized minimum is

\[
\boxed{\frac{q_{\mathrm{ch}}(P_9)}{\operatorname{area}(P_9)}=\frac{5-2c+8c^2}{72c(1-c^2)}=1.28685763764035\ldots.}
\]

Exactly nine quadrilaterals achieve the minimum. They are one orbit under the dihedral symmetries of \(P_9\), each an isosceles trapezoid with exactly **one vertex-contact supporting line and three edge-contact supporting lines**. The same normalized statement and nine-optimizer classification hold for every nonsingular affine image of \(P_9\).

## Assumptions and scope
The regular nonagon is oriented as above; all angle and length statements refer to its Euclidean realization. The allowed side directions are *only* those parallel to chords joining its vertices. A candidate quadrilateral may be translated, and all its side supports are chosen as tightly as inclusion of \(P_9\) permits. The theorem concerns the chord-restricted minimum \(q_{\mathrm{ch}}\), **not** the unrestricted minimum over all circumscribed quadrilaterals. Area ratios and the chord-restricted problem are affine invariant.

## Proof
**Reduction to a finite complete set.** Put \(\alpha=\pi/9\) and \(u_k=(\cos(k\alpha),\sin(k\alpha))\) for \(0\le k<18\). A chord of \(P_9\) has a normal parallel to some \(u_k\), and every one of these unoriented normal directions is realized by a chord. The supporting half-plane with outer normal \(u_k\) is

\[
\langle u_k,x\rangle\le h_k,\qquad h_k=\begin{cases}1&k\text{ even},\\c&k\text{ odd}.\end{cases}
\]

Any area-minimizing chord quadrilateral can be taken with four supporting lines at these offsets: translating an outer line inward until it touches \(P_9\) does not increase its area. A triangle cannot minimize, since the intersection of the nine edge-supporting half-planes is \(P_9\), which is not a triangle; some additional chord-supporting line strictly truncates any enclosing triangle. Thus every minimum is represented by four distinct outward normals. A cyclically ordered quadruple \(0\le k_0<k_1<k_2<k_3<18\) bounds a compact polygon only if each of its four cyclic index gaps lies in \(\{1,\ldots,8\}\); otherwise all four normals lie in a closed semicircle and the half-plane intersection is unbounded.

**Exact area formula and feasibility.** For a quadruple with gaps \(d_i=k_{i+1}-k_i\) cyclically (where \(k_4=k_0+18\)), its successive support-line intersections are checked against the other two half-planes. Whenever these intersections are feasible, the quadrilateral area satisfies

\[
2s\,\operatorname{area}(Q)=\sum_{i=0}^{3}
\frac{2h_{k_i}h_{k_{i+1}}-(h_{k_i}^{2}+h_{k_{i+1}}^{2})\cos(d_i\alpha)}{U_{d_i-1}(c)},
\]

where \(U_m\) is the Chebyshev polynomial of the second kind and the cyclic support convention is used. This follows by decomposing the area into the signed triangles at adjacent tangent-line intersections, using \(\sin(d\alpha)=sU_{d-1}(c)\). For feasibility, the intersection of support lines \(i,j\), with \(0<j-i<9\), satisfies the constraint at \(k\) precisely when

\[
h_i\sin((j-k)\alpha)+h_j\sin((k-i)\alpha)
-h_k\sin((j-i)\alpha)\le0.
\]

Every trigonometric factor is an exact polynomial in \(c\) after division by \(s\).

**Exhaustive exact minimization.** The identity \(\cos(3\alpha)=1/2\) gives \(8c^3-6c-1=0\). Work therefore in the exact cubic field \(\mathbb Q[c]\), using the basis \(1,c,c^2\) and reduction \(c^3=(6c+1)/8\). The attached standard-library program `verify_nonagon.py` implements Chebyshev recurrences, exact rational field operations and inverses, and compares signs by isolating \(c\) between the rational numbers

\[
\frac{93969262078590838405}{10^{20}}<c<\frac{93969262078590838406}{10^{20}}.
\]

The polynomial \(8t^3-6t-1\) has opposite signs at these endpoints and is strictly increasing for \(t>1/2\), so interval evaluation with rational arithmetic rigorously decides every comparison without numerical tolerance.

All \(\binom{18}{4}=3060\) direction quadruples are examined. Precisely \(1548\) have all gaps smaller than \(9\), and all \(1548\) pass the exact feasibility test. The minimum exact cubic-field vector for \(2s\,\operatorname{area}(Q)\) is

\[
\left(\frac54,-\frac12,2\right),
\quad\text{meaning }\frac54-\frac12c+2c^2.
\]

Equality occurs for exactly the nine ordered normal-index quadruples

`(0,5,9,13), (1,5,9,14), (1,5,10,15), (1,6,11,15), (2,7,11,15), (3,7,11,16), (3,7,12,17), (3,8,13,17), (4,9,13,17)`.

Every other feasible quadruple gives a strictly larger algebraic area. For example, the first optimizer has supporting normals indexed by \((0,5,9,13)\): index \(0\) touches a vertex, while the other three indices touch edges. The others are its dihedral images. Dividing the minimum cubic-field expression by \(2s\) proves the two boxed formulas and the complete optimizer classification.

**Why the vertex-contact condition matters.** If all four normals are restricted to edge-normal directions, their cyclic gaps are positive even integers summing to \(18\). Convexity of \(\tan\) gives the minimum with gaps \((4,4,4,6)\), of area

\[
c^2\bigl(3\tan(2\pi/9)+\tan(\pi/3)\bigr)=3.75227021324910\ldots,
\]

strictly larger than the true optimum. The strict inequality is also checked in exact cubic-field arithmetic by the embedded verifier. Thus omitting the vertex-contact option loses a genuine area improvement, not merely another equality case.

## Verification
Run `python3 verify_nonagon.py` using Python 3 and no third-party packages. The program checks the rational isolating interval, implements all algebra exactly over fractions, tests every quadruple for boundedness and each relevant support-line vertex for feasibility, compares all eligible areas by certified rational interval signs, and asserts the closed formula and exactly nine optimizers. It prints `EXACT_NONAGON_CHORD_QUADRILATERAL_CERTIFICATE_OK` on success. The inequalities are finite and exhaustively checked, not sampled; the geometric reduction establishes why this finite comparison proves the full chord-restricted minimum. A separate direct numerical shoelace calculation for the representative optimizer agrees with the formula to floating-point precision, but is not needed for the proof.

## Relationship to prior work
Viktor Vígh's 2026 preprint [1] introduced this chord-restricted version of Kuperberg's quadrilateral conjecture, justified reduction to finitely many supporting-line candidates, proved a general \(\sqrt2\) bound, and gave the regular heptagon's ratio numerically. Its Section 4 illustrates a *nonregular* nonagon in an unrelated bound; it does not give the exact regular-nonagon minimum or classify its optimizers. Fodor and Grundbacher [2] proved a universal improvement to the unrestricted \(\sqrt2\) estimate using stability arguments, not the exact restricted nonagon problem. The earlier pentagon theorem quoted in [1] likewise has a different polygonal domain. No inspected result implies the exact nonagon expression or the nine trapezoidal equality cases. A previously unindexed exact treatment remains a literature risk.

## Limitations
The result is for the regular nonagon and its nonsingular affine images only. It does not determine the unrestricted best circumscribed quadrilateral, settle Kuperberg's conjecture, or give an all-sides formula for arbitrary regular polygons. The exact certificate establishes the finite algebraic comparisons only after the preceding geometric reduction; code execution alone would not prove that reduction. Absence of an equivalent result in searched literature is not proof that no such result exists.

## References
1. Viktor Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1 (first posted 6 October 2026), Sections 1–5.
2. Ferenc Fodor and Florian Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185v1 (5 June 2025), Sections 1–3.
3. D. E. Hong, D. Ismailescu, A. Kwak and G. Y. Park, *On the smallest area (n-1)-gon containing a convex n-gon*, *Periodica Mathematica Hungarica* 87 (2023), 394–403; pentagon theorem as reported in [1].
