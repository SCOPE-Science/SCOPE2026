# Sharp vertex separation and metric-face crossings in hollow symmetric Monge simplices

## Finding

Let \(n\ge3\) be an integer and let \(\mathcal H_n\) be the polytope of nonnegative symmetric \(n\times n\) matrices \(C=(c_{ij})\) with zero diagonal, entry sum one, and the Monge inequalities
\[
c_{ij}+c_{k\ell}\le c_{i\ell}+c_{kj}\qquad(i<k,\ j<\ell).
\]
Distances are ambient Frobenius distances. The vertices are the normalized symmetric corner-rectangle matrices \(V_{a,b}\), indexed by positive integers \(a,b\) with \(a+b\le n\): the entries in the upper-right \(a\times b\) rectangle and its transpose equal \(1/(2ab)\), and all other entries are zero. These vertices, and the fact that \(\mathcal H_n\) is a simplex, are established in Erickson–Kretschmann (2023).

Define the **minimum squared vertex separation**
\[
\delta_n^2=\min_{\substack{(a,b)\ne(c,d)\\a,b,c,d\ge1\\a+b,c+d\le n}}\|V_{a,b}-V_{c,d}\|_F^2.
\]
Writing \(n=3k+r\), \(r\in\{0,1,2\}\), the exact result is
\[
\boxed{
\delta_n^2=
\begin{cases}
[4k^2(2k-1)]^{-1},&r=0,\\
[4k^2(2k+1)]^{-1},&r=1,\\
[4k(k+1)(2k+1)]^{-1},&r=2.
\end{cases}}
\]
For \(n\ge4\), **every** shortest vertex pair joins the distinguished metric face \(\operatorname{conv}\{V_{a,b}:a+b=n\}\) to a vertex outside that face. The nearest pairs are exactly
\[
\{V_{a,n-a-1},V_{a,n-a}\},\quad
\{V_{n-a-1,a},V_{n-a,a}\},
\]
where \(a=k\) for \(r=0,1\), and \(a\in\{k,k+1\}\) for \(r=2\); repeated unordered pairs are counted once. The numbers of shortest edges are respectively \(2,2,4\). At \(n=3\), all three pairs of the three simplex vertices are shortest, including the edge whose two endpoints are on the metric face.

Consequently \(\delta_n\sim\sqrt{27/8}\,n^{-3/2}\). The half-separation \(\delta_n/2\) is the sharp universal noise tolerance for recovering an **unknown vertex** of \(\mathcal H_n\) by nearest-vertex classification from an additive Frobenius perturbation; no analogous claim is made for arbitrary points in the polytope.

## Assumptions and scope

The normalization is the sum of all \(n^2\) matrix entries equal to \(1\), not a sum over the strict upper triangle. The metric is \(\|C\|_F^2=\sum_{i,j}c_{ij}^2\), including both symmetric off-diagonal entries. All index pairs satisfy \(a,b\ge1\), \(a+b\le n\). The theorem concerns straight-line Euclidean lengths of edges (every vertex pair is an edge because this polytope is a simplex), not graph shortest-path lengths or intrinsic distances on the boundary.

## Proof

**1. Exact distance identity.** A corner rectangle has \(2ab\) equal entries. Two such rectangles overlap in \(2\min(a,c)\min(b,d)\) entries. Hence
\[
\|V_{a,b}\|_F^2=\frac1{2ab},\qquad
\langle V_{a,b},V_{c,d}\rangle_F
=\frac1{2\max(a,c)\max(b,d)},
\]
so for distinct index pairs
\[
D((a,b),(c,d))
=\frac12\left(\frac1{ab}+\frac1{cd}
-\frac2{\max(a,c)\max(b,d)}\right).
\]

**2. Comparable pairs reduce to unit expansions.** If \(a\le c\) and \(b\le d\), then \(D=\frac12(1/(ab)-1/(cd))\). The rectangular indices can be increased one at a time along a monotone path from \((a,b)\) to \((c,d)\), all intermediate indices satisfying the bound on their sum. The squared distance telescopes as the sum of the positive one-step squared distances. Thus a comparable pair with at least two steps cannot attain the global minimum among comparable pairs. For a one-step increase in \(b\),
\[
D((a,b),(a,b+1))=\frac1{2ab(b+1)},\qquad a+b\le n-1.
\]
The formula for increasing \(a\) is its transpose. For fixed \(a\), the denominator increases strictly with \(b\), so the largest permissible \(b=n-a-1\) is necessary. Put
\[
M_n=\max_{1\le a\le n-2} f_n(a),\qquad
f_n(a)=a(n-a-1)(n-a).
\]
The minimum over comparable pairs is \(1/(2M_n)\). The finite difference factors as
\[
f_n(a+1)-f_n(a)=(a-n+1)(3a-n+2).
\]
It follows, including all integer ties, that the maximizing values of \(a\) are \(k\) when \(n=3k\) or \(3k+1\), and \(k,k+1\) when \(n=3k+2\). This gives
\[
M_{3k}=2k^2(2k-1),\quad
M_{3k+1}=2k^2(2k+1),\quad
M_{3k+2}=2k(k+1)(2k+1).
\]

**3. Incomparable pairs cannot shorten the distance.** Up to relabeling, suppose \(a<c\) and \(d<b\). Then
\[
D=\frac1{2cb}\left(\frac{c-a}{a}+\frac{b-d}{d}\right)
\ge \frac12\frac{1/a+1/d}{(n-a)(n-d)},
\]
because \(c-a,b-d\ge1\), \(c\le n-d\), and \(b\le n-a\). Set \(s=a+d\) and \(z=ad\). We have \(0<s<n\), \(z\le s^2/4\), and
\[
\frac12\frac{1/a+1/d}{(n-a)(n-d)}
=\frac{s}{2z(n^2-ns+z)}
\ge \frac{2}{s(n-s/2)^2}
\ge\frac{27}{4n^3}.
\]
The middle inequality uses that \(z\mapsto z(n^2-ns+z)\) is strictly increasing for \(z>0\). The last inequality follows by maximizing \(s(n-s/2)^2\) on \((0,n)\), where the maximum \(8n^3/27\) occurs at \(s=2n/3\).

The explicit values of \(M_n\) above give \(M_n\ge2n^3/27\), with equality only at \(n=3\). For example, after multiplication by \(27\), the three differences \(27M_n-2n^3\) are
\[
54k^2(k-1),\quad
2(27k^3-9k-1),\quad
2(27k^3+27k^2-9k-8),
\]
respectively; all are strictly positive when the corresponding \(n\ge4\). Thus for \(n\ge4\), every incomparable pair has squared distance \(>1/(2M_n)\). For \(n=3\), direct substitution gives the single additional shortest incomparable pair \(\{V_{1,2},V_{2,1}\}\).

**4. Equality and interpretation.** The only minimum-length comparable pairs are the unit-expansion pairs with denominator \(M_n\), giving the displayed equality list and counts. Their index sums are \(n-1\) and \(n\), so for \(n\ge4\) exactly one endpoint lies in the metric face. The asymptotic follows from \(M_n\sim4n^3/27\). Two different vertices have distance at least \(\delta_n\); Frobenius perturbation less than half that value preserves nearest-vertex identity by the triangle inequality. A midpoint of any shortest pair demonstrates sharpness of the half-separation bound.

## Verification

Run `python3 check_monge_shortest.py`. The checker constructs the normalized symmetric corner-rectangle matrices explicitly for \(3\le n\le9\) and compares every squared Frobenius distance with the closed overlap formula. It then enumerates every unordered vertex pair for all \(3\le n\le33\), using rational arithmetic, and verifies both the exact minimum and the entire equality set. The reported replay is:

`MONGE_MINIMUM_VERTEX_SEPARATION_CHECKS_PASSED n_range=3..33 all_pairs=973896 direct_matrices_pairs=1386`

The infinite-dimensional assertion rests on the preceding algebraic proof; finite checking is not substituted for any quantified step.

## Relationship to prior work

The normalized hollow symmetric Monge simplex and its rectangle-indexed vertices, together with its metric face, are established by Erickson and Kretschmann, *The structure and normalized volume of Monge polytopes* (arXiv:2311.07522, first submitted 2023-11-13), especially Proposition 4.1 and Section 4.3. Their analysis treats vertices, normalization, volumes, and the metric face, but does not evaluate the Frobenius pair-distance minimum, its congruence-class maximizers, or the face-crossing equality pattern. Rudolf and Woeginger (1995) supply the earlier extremal-ray decomposition of Monge cones, rather than the normalized Euclidean separation calculation.

## Limitations

The shortest-edge theorem concerns this specific Frobenius realization of the **hollow symmetric** Monge polytope. It does not address the full nonsymmetric Monge polytope, the non-hollow symmetric simplex, the distance from arbitrary nonmetric points to the metric face, or numerical stability of arbitrary convex combinations. Historical priority is provisional: older treatments of extremal Monge rays or cost-matrix approximation could contain an equivalent distance formula not located in the literature comparison.

## References

1. William Q. Erickson and Jan Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v2 (2023), https://arxiv.org/html/2311.07522v2 ; Proposition 4.1, Sections 3, 4.1, 4.3.
2. R. Rudolf and G. J. Woeginger, *The cone of Monge matrices: Extremal rays and applications*, Mathematical Methods of Operations Research 42 (1995), 161–168. DOI: 10.1007/BF01415751.
3. H.-C. Chang and T. A. E. Ophelders, *Planar Emulators for Monge Matrices*, CCCG (2020); a distinct notion of Monge distance matrices, not the Frobenius distances among normalized extreme costs.
