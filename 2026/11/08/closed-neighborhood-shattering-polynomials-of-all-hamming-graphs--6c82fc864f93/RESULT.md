# Closed-neighborhood shattering polynomials of all Hamming graphs

## Finding
For integers \(d\ge1\) and \(q\ge2\), let \(X=[q]^d\), equipped with Hamming distance \(\delta\), and let \(\mathcal N_{d,q}=\{B_1(c):c\in X\}\), where \(B_1(c)=\{x\in X:\delta(x,c)\le1\}\). **The balls are closed and contain their centers.** A support \(S\subseteq X\) is shattered when \(\{B_1(c)\cap S:c\in X\}=2^S\). Write \(\Phi_{d,q}(z)=\sum_{k\ge0}s_k(d,q)z^k\) for the polynomial counting unordered shattered supports by cardinality. Then \(s_0=1\), every coefficient above degree three vanishes, and the remaining coefficients are as follows.

If \(d=1\), then \(s_1=s_2=s_3=0\). If \((d,q)=(2,2)\), then \((s_1,s_2,s_3)=(4,0,0)\). Otherwise, for \(d\ge2\),
\[
s_1=q^d,\qquad
s_2=\frac{q^d}{2}\left[d(q-1)+\binom d2(q-1)^2\right].
\]
For \(d=2\), \(s_3=0\) when \(q\le3\), and \(s_3=q^2(q-1)^2(q-2)\) when \(q\ge4\). For every \(d\ge3\),
\[
\boxed{s_3=q^d\left[\binom d2(q-1)^2+\binom d3(q-1)^3+d(d-1)\binom{q-1}{2}(q-1)\right].}
\]
Consequently,
\[
\operatorname{VCdim}(\mathcal N_{d,q})=
\begin{cases}
0,&d=1,\\
1,&(d,q)=(2,2),\\
2,&d=2,\ q=3,\\
3,&d\ge3\text{ or }(d=2,\ q\ge4).
\end{cases}
\]
In particular, the closed-neighborhood dimension of the binary three-cube is three, while the previously studied open-neighborhood dimension is two.

## Assumptions and scope
All alphabets have the same cardinality \(q\ge2\); the product has \(d\ge1\) coordinates. There are exactly \(q^d\) possible ball centers, with neither an artificially adjoined empty set nor a ball of larger radius. Distinct subsets of vertices, not ordered tuples or isomorphism types, are counted. Empty support is shattered vacuously. Statements include the complete graph \(H(1,q)\) and the four-cycle \(H(2,2)\). The natural graph relation is the reflexive radius-one relation \(\delta(x,c)\le1\), as opposed to the irreflexive adjacency relation \(\delta(x,c)=1\).

## Proof
**1. The geometry of a closed ball.** Fix a center \(c\). Every point in \(B_1(c)\setminus\{c\}\) differs from \(c\) in exactly one coordinate. Call that coordinate its *arm*. All vertices on the same coordinate line through \(c\) form a clique; different arms are Hamming distance two apart. If three distinct points lie on a single coordinate line \(L\), they cannot be shattered: any radius-one ball centered on \(L\) contains all of \(L\), whereas a radius-one ball centered off \(L\) meets \(L\) in at most one point. Hence no trace with exactly two of those three points is possible.

**2. No four-point support is shattered.** Suppose a four-point set \(S\) is shattered. Its full trace implies \(S\subseteq B_1(c)\) for some \(c\). If \(c\in S\) and two other members have the same arm, there is a forbidden collinear triple. Otherwise the three remaining members have different arms; their only common radius-one center is \(c\), making the trace containing those three but not \(c\) impossible. If \(c\notin S\), three members on one arm again give a forbidden collinear triple. With four arm points and at most two per arm, the arm multiplicities are \((1,1,1,1)\), \((2,1,1)\), or \((2,2)\). In the first two patterns, three points from distinct arms have exactly one common radius-one center, namely \(c\); in the last pattern, two points on one arm and one on another also have only \(c\) as a common center (a center covering the first two must lie on their coordinate line). Thus every pattern has a three-point subset that can only be covered by \(c\), which also covers the fourth point. This contradicts shattering. All supports of size at least four therefore fail by heredity.

**3. Classification of shattered triples.** A shattered triple lies in a ball, by its full trace. Step 1 excludes collinear triples, leaving precisely these shapes relative to a common center \(c\):

(A) \(c\) and two other points on different arms;

(B) three arm points on three distinct coordinates;

(C) two arm points on the same coordinate and a third on a different coordinate.

For (A), \(d\ge3\) is necessary because the singleton trace \(\{c\}\) needs a ball centered on a third arm. It is sufficient: write the triple as \(\{c,u,v\}\), with \(u\) and \(v\) differing from \(c\) on distinct coordinates \(i,j\); take a third coordinate \(k\). The full trace is obtained at \(c\). The two traces containing \(c\) and one of \(u,v\) are obtained at those arm points. The trace \(\{u,v\}\) is obtained by the two-coordinate hybrid. The singleton traces \(\{u\}\), \(\{v\}\) come from changing the \(k\)-coordinate of the corresponding arm point, and \(\{c\}\) from changing the \(k\)-coordinate of \(c\). Changing the \(i,j,k\) coordinates of \(c\), using the arm values on \(i,j\), provides the empty trace.

For (B), necessarily \(d\ge3\). The full trace is obtained at \(c\); each singleton by its own arm point; each pair by the hybrid with exactly its two arm values; and the empty trace by the point with all three arm values. Every other member of the triple has distance at least two from the respective non-covering witnesses.

For (C), write the triple as \(\{u,v,w\}\), with \(u,v\) on arm \(i\) at two different noncentral alphabet symbols and \(w\) on arm \(j\ne i\). Thus \(q\ge3\) is necessary. The full trace is obtained at \(c\). The pair \(\{u,v\}\) is realized at \(u\); the pairs \(\{u,w\}\), \(\{v,w\}\) at the corresponding two-coordinate hybrids. The singleton \(\{w\}\) is realized at \(w\). Each of \(\{u\}\), \(\{v\}\) is obtained by modifying that arm point on a third coordinate when \(d\ge3\), or (when \(d=2\)) by changing its \(j\)-coordinate to a symbol different from both the central and the \(w\)-symbol. The empty trace exists for \(d\ge3\): change the \(j\)-coordinate of \(c\) to a third symbol and modify an additional coordinate \(k\notin\{i,j\}\). For \(d=2\), a center is distance at least two from all three points exactly when its \(i\)-coordinate avoids the three distinct values occurring on that coordinate and its \(j\)-coordinate avoids the two values occurring there; this is possible exactly when \(q\ge4\). Thus (C) is shattered exactly for \(d\ge3\), or for \(d=2,q\ge4\).

Each of these three shapes has a **unique** common radius-one center \(c\). In (A), a common center of the two arms is either \(c\) or their hybrid, but only \(c\) covers the included center point; in (B), the three distinct arms force \(c\); in (C), covering both same-arm points forces a center on their line, and covering the other arm point forces that center to be \(c\). We may therefore count by choosing \(c\) without overcounting. Shape (A) contributes \(q^d\binom d2(q-1)^2\), shape (B) contributes \(q^d\binom d3(q-1)^3\), and shape (C) contributes \(q^dd(d-1)\binom{q-1}{2}(q-1)\), restricted to its validity range. This proves the formula for \(s_3\).

**4. Singles and pairs.** If \(d=1\), every ball equals \(X\) and no nonempty support is shattered. If \(d\ge2\), each singleton is shattered: one ball contains its point and a ball at Hamming distance two does not. Any shattered pair must have Hamming distance at most two to permit its full trace. For \(d\ge3\), every pair at distance one or two is shattered. At distance one, one may isolate either endpoint using a center that changes an additional coordinate; the empty trace comes from changing two coordinates distinct from the differing coordinate. At distance two, the full trace is realized at either two-coordinate hybrid, the singleton traces at the two endpoints, and the empty trace at a center that takes one differing coordinate from each endpoint and changes a third coordinate. For \(d=2,q\ge3\), the same singleton and full witnesses work; the empty trace for a pair at distance one comes from using a third symbol in the differing coordinate and modifying the other coordinate, and for a pair at distance two from using a third symbol in both differing coordinates. Thus every pair in the \(d=2,q\ge3\) graph is shattered. For \((d,q)=(2,2)\), any pair has no empty trace: the four closed neighborhoods of the four-cycle each omit exactly one vertex. The number of unordered pairs at distance one is \(q^dd(q-1)/2\), and the number at distance two is \(q^d\binom d2(q-1)^2/2\). This proves \(s_1\) and \(s_2\) including all exceptions.

**5. VC dimension.** The positive leading coefficient in each parameter regime, together with the four-point exclusion, gives the stated dimension table.

## Verification
`check_closed_hamming.py` constructs each radius-one closed ball directly from Hamming distance, enumerates actual Boolean traces without using the theorem's formulas to generate them, and compares with the claimed coefficients. It also cross-checks every three-point trace against the coordinate-pattern classification and verifies all tested four-point supports fail. Full testing covers \((d,q)=(1,2),(1,5),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(5,2)\); for \((4,3)\) all supports of sizes at most three are tested and a fixed-seed sample of four-point supports is tested. There are \(859801\) tested nonempty supports in total. Example polynomials are \(\Phi_{3,2}(z)=1+8z+24z^2+32z^3\) and \(\Phi_{2,4}(z)=1+16z+120z^2+288z^3\). The checker is finite corroboration: the universal claim is proved by Steps 1–5, not inferred from computation.

## Relationship to prior work
Adler, Benediktsson and Macpherson (first available as arXiv:2007.16042 on 2020-07-31) prove the open-neighborhood VC-dimension bound of three for Hamming graphs, characterize its sharpness, and observe that closed-neighborhood VC dimension is bounded. Their explicitly analyzed relation is irreflexive adjacency, not the inclusive relation counted here. The present result is a coefficientwise enumeration for the **closed** relation and a sharp dimension table, including \(H(3,2)\), where open and closed neighborhoods behave differently. The separate, later graph VC-dimension algorithm of Coudert, Csikós, Ducoffe and Viennot (2024) addresses general closed-neighborhood computation, without this all-parameter formula. The 2025 work of Housholder, Mangiapanello and Senger concerns open-neighborhood VC dimensions of induced subsets of Hamming graphs, not this enumeration. Results about radius-two Boolean balls and open Hamming neighborhoods do not imply these specific counts: both the geometric trace shapes and endpoint behavior change when the center is included.

## Limitations
The result concerns uniform alphabets and radius exactly one, not arbitrary unions of balls, balls of radius at least two, induced subgraphs with restricted possible centers, or Cartesian products with unequal alphabet sizes. The result does not assert a new general VC-density theorem. Historical priority remains subject to alternate terminology such as reflexive incidence matrices or dominating-set trace polynomials; no independent mathematical validation has been performed.

## References
1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv:2007.16042 (first submitted 2020-07-31), *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/abs/2007.16042 ; https://eprints.whiterose.ac.uk/id/eprint/178584/
2. D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, LIPIcs 301, article 8, https://doi.org/10.4230/LIPIcs.SEA.2024.8
3. C. Housholder, L. Mangiapanello, and S. Senger, *VC-dimension of subsets of Hamming graphs*, arXiv:2505.14641 (first submitted 2025-05-20), https://arxiv.org/abs/2505.14641
