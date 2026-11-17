# The sharp planar lattice-width cutoff for Ehrhart real-rootedness

## Finding

**Theorem.** Let \(P\subset\mathbb R^2\) be any full-dimensional lattice polygon and let its lattice width be \(w(P)\). If \(w(P)\ge4\), its Ehrhart \(h_P^*(z)\) has **two distinct strictly negative real roots**. The same conclusion holds for \(w(P)=3\), with exactly one affine-unimodular exception:
\[
T=\operatorname{conv}\{(0,0),(1,0),(3,7)\},\qquad h_T^*(z)=1+3z+3z^2.
\]
This exceptional polynomial has discriminant \(-3\) and hence two nonreal roots. Consequently the **smallest integer width guaranteeing two distinct strictly negative roots for every lattice polygon is \(4\)**. For the formulation \(w(P)>C_2\), the best nonnegative real cutoff is \(C_2=3\).

## Assumptions and scope

A *lattice polygon* means a compact convex two-dimensional polygon whose vertices lie in \(\mathbb Z^2\). Its lattice width is
\[
w(P)=\min_{(a,b)\in\mathbb Z^2\setminus\{(0,0)\}}
\left(\max_{x\in P}(ax_1+bx_2)-\min_{x\in P}(ax_1+bx_2)\right).
\]
Set \(L_P(n)=|nP\cap\mathbb Z^2|\) for every nonnegative integer \(n\). The Ehrhart \(h^*\)-polynomial is defined by \(\sum_{n\ge0}L_P(n)z^n=h_P^*(z)/(1-z)^3\). Equivalence means an integral translation followed by a matrix in \(\operatorname{GL}_2(\mathbb Z)\). The theorem concerns ordinary planar Ehrhart polynomials, not local box polynomials or rational (nonlattice) polygons.

## Proof

**1. Discriminant.** Write \(B\) for the total number of boundary lattice points and \(I\) for the number of interior lattice points. Pick's theorem and the Ehrhart series identity yield
\[
h_P^*(z)=1+(B+I-3)z+Iz^2,\qquad
\mathcal D=(B+I-3)^2-4I.
\]
Every full-dimensional lattice polygon has \(B\ge3\). If \(B\ge5\), then \(\mathcal D>0\) whenever \(I\ge1\). If \(B=4\), then \(\mathcal D=(I-1)^2\), which is strictly positive for \(I\ge2\). If \(B=3\), then \(\mathcal D=I(I-4)\). Thus, among polygons with \(I\ge2\), the only possible non-strict or negative discriminants have \(B=3\) and \(I\in\{2,3,4\}\).

**2. Eliminate low interior counts at large width.** The theorem of Averkov–Codenotti–Freyer–Huang states that a planar convex body containing at most one interior lattice point has width at most \(3\), with equality *only* for a unimodular image of \(3\Delta_2\). This triangle has \(B=9\), \(I=1\), and \(h^*(z)=1+7z+z^2\), whose discriminant is positive. Therefore, for width at least \(3\), all cases with \(I\le1\) are either excluded or already have two distinct negative roots.

**3. Exhaust all small-boundary candidates.** When \(B=3\), every triangle edge is primitive and its normalized area is \(D=2I+1\). By sending a primitive edge to \([(0,0),(1,0)]\) using a unimodular map, and then shearing, every such triangle has the form
\[
T_{r,D}=\operatorname{conv}\{(0,0),(1,0),(r,D)\},\quad
0\le r<D,\quad\gcd(r,D)=\gcd(r-1,D)=1.
\]
For the only relevant values \(I=2,3,4\), the integers \(D\) are \(5,7,9\). We also display \(D=3\) to handle the \(I=1\) case independently. The table lists every admissible \(r\) and a primitive integer covector \((a,b)\) achieving the stated width \(w\). A width upper bound is simply the range of \(0,a,ra+Db\).

| \(D\) | \(r\) | \(w\) | \((a,b)\) |
| ---: | ---: | ---: | :--- |
| 3 | 2 | 2 | (1,-1) |
| 5 | 2 | 2 | (1,0) |
| 5 | 3 | 2 | (2,-1) |
| 5 | 4 | 2 | (1,-1) |
| 7 | 2 | 2 | (1,0) |
| 7 | 3 | 3 | (1,0) |
| 7 | 4 | 2 | (2,-1) |
| 7 | 5 | 3 | (1,-1) |
| 7 | 6 | 2 | (1,-1) |
| 9 | 2 | 2 | (1,0) |
| 9 | 5 | 2 | (2,-1) |
| 9 | 8 | 2 | (1,-1) |

The displayed covectors suffice to prove width at most \(2\) in ten cases. To show that \(T_{3,7}\) has width at least \(3\), suppose that some nonzero integer covector \((a,b)\) has range at most \(2\) on \(0,a,3a+7b\). Then \(|a|\le2\). For \(a=0\), the range forces \(b=0\), a contradiction. For \(a=1\), the third value must lie in \([-1,2]\), contradicting congruence \(3a+7b\equiv3\pmod7\). For \(a=2\), it must lie in \([0,2]\), contradicting congruence to \(6\pmod7\). The cases \(a=-1,-2\) are obtained by negating the covector. Hence \(w(T_{3,7})=3\). The matrix
\[
U=\begin{pmatrix}5&-2\\-7&3\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z)
\]
sends the vertex triple of \(T_{3,7}\) to \((0,0),(5,-7),(1,0)\). Reflecting the second coordinate proves \(T_{3,7}\) is unimodularly equivalent to \(T_{5,7}\), so the latter also has width \(3\). All admissible \(r\)'s are exhausted by the displayed coprimality conditions. There is therefore exactly **one** exceptional width-three equivalence class, represented by \(T_{3,7}\), and **no** candidate with width at least \(4\).

**4. Root signs.** In the remaining cases of width at least \(3\), \(I>0\), \(B+I-3>0\), and \(\mathcal D>0\). Thus the quadratic \(h_P^*\) has two distinct real roots; their sum and product show both are strictly negative. The exceptional \(T\) has \((B,I)=(3,3)\), so \(h_T^*=1+3z+3z^2\) has negative discriminant. This proves the threshold, uniqueness, and sharpness. \(\square\)

## Verification

The included standalone Python script `verify_width.py` independently checks all primitive-edge normal-form classes at normalized areas \(3,5,7,9\), their stated covectors, exact minimal width within a sufficiently broad finite search window, lattice-point counts for the first seven dilations, the special lower-width obstruction, and the explicit unimodular equivalence. It is supporting arithmetic verification: the infinite polygon claim follows from the preceding proof and the cited flatness theorem, **not** from bounded enumeration. The script uses only Python's standard library.

## Relationship to prior work

Benjamin Nill [1], Theorem 1.1, proves the existence of a dimension-dependent large-width cutoff for distinct negative Ehrhart roots, but explicitly does not determine the optimal cutoff even in dimension two. Here that planar cutoff is sharp and the unique width-three obstruction is classified. The exact \(\mathrm{Flt}(2,1)=3\) theorem and its rigid equality case [2] are essential. Hamm's classification [3], and earlier work on possible Ehrhart pairs of lattice triangles [4], address geometric or arithmetic data that can imply parts of the small-normal-form analysis, but do not state this width-to-real-rootedness theorem. A more recent fixed-width multiplicity classification [5] may subsume the width-three triangle enumeration; its relevance is acknowledged explicitly. No historical claim of absolute priority is made.

## Limitations

The theorem is two-dimensional and applies only to lattice polygons. It does not determine an optimal large-width constant for local \(h^*\)-polynomials in other dimensions. The finite table is elementary, and historical equivalent formulations in older enumerative geometry or in detailed fixed-width tables cannot be ruled out solely by unsuccessful searches. Independent mathematical audit has not been performed.

## References

[1] B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart h*-polynomials*, arXiv:2608.03635 (first public 2026-08-04), Theorem 1.1 and discussion after Theorem 1.2. https://arxiv.org/abs/2608.03635

[2] G. Averkov, G. Codenotti, A. Freyer, and K. Huang, *Exact Flatness Constant for One-Point Convex Bodies and the Discrete Isominwidth Problem: The Planar Case*, arXiv:2604.27260 (2026), Theorem 1.1. https://arxiv.org/abs/2604.27260

[3] G. Hamm, *Classification of lattice triangles by their two smallest widths*, arXiv:2304.03007 (2023), Theorem 1.1 and §4. https://arxiv.org/abs/2304.03007

[4] J. Hofscheier, B. Nill, and D. Öberg, *On Ehrhart polynomials of lattice triangles*, arXiv:1609.09526 (2016), §1, especially Remark 1.4. https://arxiv.org/html/1609.09526v1

[5] R. J. Higuchi, *Fixed-Width Multiplicity Theory for Ehrhart Pairs of Lattice Triangles* (2026), DOI:10.13140/RG.2.2.11723.76324; indexed public abstract and initial sections examined, full access limited. https://www.researchgate.net/publication/403331264_Fixed-Width_Multiplicity_Theory_for_Ehrhart_Pairs_of_Lattice_Triangles
