# Three halving-chord moments reconstruct a parallelogram and have a sharp feasible region

## Finding

Let \(Q\subset\mathbb R^2\) be any nondegenerate Euclidean parallelogram, with perimeter \(P\), area \(A>0\), and adjacent side lengths \(a,b>0\). Draw a boundary point \(X\) uniformly by arclength. Its **perimeter-halving partner** \(X^\sharp\) is the point halfway around the boundary in either direction, and let \(H=\|X-X^\sharp\|_2\). Define \(m_{2j}=\mathbb E[H^{2j}]\) for \(j=1,2,3\), and put \(s=P/2=a+b\). Then
\[
\boxed{\begin{aligned}
m_2&=\frac{s^2}{3},\\
m_4&=\frac{s^4}{5}-\frac43 A^2,\\
m_6&=\frac{s^6}{7}-\frac{12}{5}s^2A^2+\frac{16}{5}abA^2.
\end{aligned}}\tag{1}
\]
**The first three even halving-chord moments determine \(Q\) up to Euclidean congruence, and three are necessary among initial even moments.** Explicitly, recover
\[
s=\sqrt{3m_2},\quad A=\sqrt{\frac34\left(\frac{s^4}{5}-m_4\right)},\quad
r=ab=\frac{5}{16A^2}\left(m_6-\frac{s^6}{7}+\frac{12}{5}s^2A^2\right).
\tag{2}
\]
The unordered side lengths are the roots of \(z^2-sz+r=0\). Their acute *edge-line angle* \(\phi\in(0,\pi/2]\) is uniquely determined by \(\sin\phi=A/r\). Edge-vector sign changes and swapping the two sides yield the same congruence class.

There is an exact characterization of all feasible moment triples. Choose any \(s>0\) and \(0<A\le s^2/4\), prescribe \(m_2,m_4\) by (1), and write
\[
L(s,A)=\frac{s^6}{7}-\frac{12}{5}s^2A^2+\frac{16}{5}A^3,\qquad
U(s,A)=\frac{s^6}{7}-\frac85s^2A^2.
\]
Then the possible values of \(m_6\) are **exactly**
\[
\boxed{L(s,A)\le m_6\le U(s,A).}\tag{3}
\]
At fixed \(s,A\), equality on the left characterizes rectangles, equality on the right characterizes rhombi, and both occur together only for squares. Every intermediate value is attained by a nondegenerate parallelogram.

## Assumptions and scope

The boundary sampling measure is normalized Euclidean arclength; there is one random point, not two independent random endpoints and not an invariant-random-line chord. The paired point is deterministically \(P/2\) arclength away. Vertex choices have probability zero and do not affect definitions. All objects are nondegenerate parallelograms, including rectangles and rhombi. The result is exact, with no asymptotic limit. \(A\) denotes the usual unsigned Euclidean area; \(r\) denotes the positive product of adjacent side lengths, not a radius. The inverse reconstruction uses exact population moments, not empirical estimates.

## Proof

Translate the center of symmetry of \(Q\) to the origin, and let the two nonparallel edge vectors be \(u,v\), with \(\|u\|=a\), \(\|v\|=b\), and \(q=u\cdot v\). Then
\[
A^2=a^2b^2-q^2>0,\qquad s=a+b.
\tag{4}
\]
The half-perimeter arclength translation is the central reflection \(X\mapsto-X\), because each opposite side is its parallel translate under central symmetry, and each boundary half-cycle has length \(a+b\). Thus \(H=2\|X\|\).

The two sides parallel to \(u\) account for probability \(a/s\). Conditional on these sides, the vector \(2X\) has the same norm distribution as \(v+Tu\), where \(T\) is uniform on \([-1,1]\). Analogously, sides parallel to \(v\) have probability \(b/s\) and the norm distribution of \(u+Tv\). Hence for every positive integer \(j\),
\[
 m_{2j}=\frac{a}{2s}\int_{-1}^{1}(b^2+a^2t^2+2qt)^j\,dt
 +\frac{b}{2s}\int_{-1}^{1}(a^2+b^2t^2+2qt)^j\,dt.
\tag{5}
\]
All integrals are elementary polynomials. Odd powers of \(t\) vanish; \(\mathbb E T^{2k}=1/(2k+1)\). For the first power this gives
\[
 m_2=\frac{a(b^2+a^2/3)+b(a^2+b^2/3)}s=\frac{s^2}{3}.
\]
For the second power, the two conditional integrals are
\[
 b^4+\frac{2a^2b^2+4q^2}{3}+\frac{a^4}{5},\qquad
 a^4+\frac{2a^2b^2+4q^2}{3}+\frac{b^4}{5}.
\]
Their arclength-weighted mean simplifies by (4) to \(s^4/5-4A^2/3\). For the third power, the first conditional integral equals
\[
 b^6+a^2b^4+\frac35a^4b^2+\frac17a^6
 +q^2\left(4b^2+\frac{12}{5}a^2\right),
\]
and the second is obtained by interchanging \(a\) and \(b\). Multiply by the respective weights \(a/s\) and \(b/s\), use \(q^2=a^2b^2-A^2\), and collect symmetric terms to obtain the third identity in (1). The accompanying symbolic checker verifies these polynomial identities for formal indeterminates, not merely particular shapes.

Since \(A>0\), formulas (1) invert to (2) without division by zero. The roots of \(z^2-sz+r\) are exactly \(a,b\). The area relation \(A=ab\sin\phi\) determines the acute angle between the unoriented edge lines. These data determine a parallelogram up to rigid motion and reflection. This proves sufficiency of three moments, including equal-side and right-angle cases.

For the complete attainable region, elementary geometry gives
\[
 0<A\le ab\le\frac{(a+b)^2}{4}=\frac{s^2}{4}.
\tag{6}
\]
Conversely fix \(s,A\) with \(0<A\le s^2/4\), and choose any \(r\in[A,s^2/4]\). The positive roots of \(z^2-sz+r\) supply side lengths, and an angle with \(\sin\phi=A/r>0\) supplies a nondegenerate parallelogram of those side lengths and area. For fixed \(s,A\), the third identity (1) is strictly increasing affine in \(r\). Substituting the two endpoint values gives exactly (3). The case \(r=A\) is equivalent to \(\sin\phi=1\), hence to a rectangle, whereas \(r=s^2/4\) is equivalent to \(a=b\), hence to a rhombus. Both can coincide only when \(A=s^2/4\), yielding a square. This proves sharpness and all equality cases.

Finally, fix \(s=1\) and \(A=3/16\). The rectangle with adjacent sides \(3/4,1/4\) and the rhombus with adjacent sides \(1/2,1/2\) and acute angle \(\arcsin(3/4)\) have the same \(m_2=1/3\) and \(m_4=49/320\) (since \(1/5-3/64=49/320\)); but their products \(ab\) differ, and (1) gives different \(m_6\). Therefore two initial even moments cannot determine the congruence class. This proves minimality.

## Verification

The self-contained `verify.py` reproduces the three polynomial identities by exact symbolic integration and cancellation; checks inversion on four rational parameter shapes, including a rhombus and a negative-dot-product generator; verifies 187 rational instances of the claimed interval; and independently evaluates Euclidean norm integrals by a high-resolution midpoint rule. Its recorded successful terminal line is:

`VERIFY_OK symbolic_moment_identities=3 rational_inverse_shapes=4 feasibility_cases=187 midpoint_quadratures=3`

Run `python verify.py` with the declared `requirements.txt`. The analytic identities, inversion, and attainability arguments above prove the universal statements; finite computations serve as reproduction checks, not as proof by enumeration.

## Relationship to prior work

Halving chords are classical objects in geometric dilation and convex geometry. Dumitrescu, Ebbers-Baumann, Grüne, Klein and Rote (public arXiv preprint 2004) analyze halving-pair distances, their extrema, and Zindler curves [1]. Grüne, Klein, Miori and Segura Gomis (2007) study primarily **area-halving chords** and geometric inequalities [2]. Neither establishes reconstruction or the sharp three-even-moment region here.

A published 2026 mathematical result on independent boundary and interior chord pairs in parallelograms [3] contains exact formulas for \(\mathbb E\|S\|^2\) and \(\mathbb E\|S\|^4\), where \(S\) is a centered, arclength-uniform boundary point. Because \(H=2\|S\|\), these imply the first **two** identities of (1), including their area dependence after algebra. **Those two identities are not claimed as new.** Its pair-of-independent-endpoints fourth-moment ratio does not supply the sixth one-point/halving-chord identity, the three-moment inverse, minimality, or the complete sharp feasible third-moment interval.

Another published parallelogram reconstruction [4] uses random **projection widths in unlabeled directions**, together with a maximum; its input is mathematically distinct from the three halving-chord length moments here. It does not imply this exact sixth-moment factorization or the moment-region equality classification. The comparison is about implication between statements, not coincident wording. A general earlier integral formula for higher moments of all perimeter-halving chords cannot be excluded from the historical record; independent priority verification has not been performed.

## Limitations

The claim concerns Euclidean parallelograms and the deterministic perimeter-halving partner under uniform arclength sampling. It makes no claim about arbitrary quadrilaterals, independent random chord endpoints, or invariant random-line sampling. The inverse degenerates as \(A\to0\); quantitative stability and finite-sample estimation are not established. The already known second- and fourth-moment formulas are included only as ingredients of the new minimal inverse and sharp sixth-moment region.

## References

[1] A. Dumitrescu, A. Ebbers-Baumann, A. Grüne, R. Klein and G. Rote, *On the geometric dilation of closed curves, graphs, and point sets*, arXiv:math/0407135, first posted 2004-07-08, https://arxiv.org/abs/math/0407135. In particular, the halving-pair definitions and extremal-distance sections.

[2] A. Grüne, R. Klein, C. Miori and S. Segura Gomis, *Chords halving the area of a planar convex set*, Mathematical Inequalities & Applications 10 (2007), 205–216, https://files.ele-math.com/articles/mia-10-17.pdf, especially pp. 205–210.

[3] *Fourth-chord moment amplification and angular phase transition for parallelograms*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e, especially displayed boundary moments in its Proof.

[4] *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928.
