# Exact face vectors of generic central sections of type-D root polytopes in every rank

## Finding
For every integer \(n\ge5\), let
\[
P_n=\operatorname{conv}\{\varepsilon e_i+\delta e_j:
1\le i<j\le n,\ \varepsilon,\delta\in\{-1,1\}\}
\subset\mathbb R^n,
\]
where the basis and metric are the usual Euclidean ones. For every nonzero normal \(u\) satisfying \(|u_i|\ne |u_j|\) whenever \(i\ne j\), the central hyperplane section \(Q_n(u)=P_n\cap u^\perp\) has dimension \(n-1\). Its entire face vector is independent of \(u\), and in fact all such sections have combinatorially isomorphic face lattices. For \(0\le k\le n-3\), the exact number of \(k\)-faces is
\[
\boxed{f_k(Q_n(u))=(k+1)2^{k+3}\binom n{k+3}
 +(2^{k+2}-4)\binom n{k+2}.}
\]
The number of facets (\((n-2)\)-faces) is
\[
\boxed{f_{n-2}(Q_n(u))=2^n+2n-6.}
\]
In particular every generic central section has \(8\binom n3\) vertices. The first higher-rank examples are
\[
\begin{aligned}
n=5:&\quad (f_0,f_1,f_2,f_3)=(80,200,156,36),\\
n=6:&\quad (f_0,\ldots,f_4)=(160,560,756,424,70),\\
n=8:&\quad (f_0,\ldots,f_6)=(448,2464,6216,8736,6800,2528,266).
\end{aligned}
\]

## Assumptions and scope
The root polytope is the type-\(D_n\) root polytope, also described as the rectification of the \(n\)-dimensional cross-polytope. The normal is *generic for this central-section problem* precisely when the section contains no root vertex: its coordinates have pairwise distinct absolute values. These are open chambers of the type-\(D_n\) reflection arrangement. Neither a metric equivalence of differently oriented sections nor a classification of nongeneric sections is asserted. The \(n=4\) specialization is already covered by the known generic section of the regular \(24\)-cell and is excluded from the new claim.

## Proof
**1. Exposed-face classification of the root polytope.** For any nonzero \(w\in\mathbb R^n\), the support function is
\[
h_{P_n}(w)=|w|_{(1)}+|w|_{(2)},
\]
where \(|w|_{(1)}\ge |w|_{(2)}\ge\cdots\) are the descending absolute coordinate values. Consequently the entire set of positive-dimensional proper exposed faces comprises exactly three classes:

* **Coordinate faces:** when only one coordinate of \(w\) is nonzero, the face \(x_i=\sigma\) (\(\sigma\in\{-1,1\}\)) is an \((n-1)\)-dimensional cross-polytope, with vertices \(\sigma e_i\pm e_j\) for \(j\ne i\). There are \(2n\) such facets.
* **Fixed-coordinate simplex faces:** when \(|w_i|>|w|_{(2)}>0\), and \(J\subset[n]\setminus\{i\}\) is the set of indices tied at second-largest modulus, the face is the simplex \(\operatorname{conv}\{\sigma e_i+\tau_j e_j:j\in J\}\), of dimension \(|J|-1\). Every choice of \(i\), signed \(i\), nonempty \(J\), and independent signs \(\tau_j\) arises. For \(|J|\ge2\), this description is unique because its vertices have precisely one coordinate with fixed common nonzero sign.
* **Hypersimplex faces:** when the largest modulus is attained on a set \(I\subset[n]\) with \(|I|\ge2\), the face is \(\operatorname{conv}\{\tau_i e_i+\tau_j e_j:i,j\in I,\ i<j\}\), affinely a second hypersimplex. For \(|I|\ge3\), it has dimension \(|I|-1\), and its signed support uniquely determines the face because no coordinate is common with fixed nonzero sign to all its vertices. The \(|I|=2\) case is one vertex, not a positive-dimensional hypersimplex face.

These cases are exhaustive because a supporting face consists exactly of roots attaining the sum of the two largest coordinate moduli. They are distinct for positive dimension. In particular the original polytope has \(2n+2^n\) facets: \(2n\) coordinate facets and one \(n\)-coordinate hypersimplex facet for each sign word.

**2. Reduction to one generic normal.** The reflection group of the type-\(D_n\) roots acts transitively on the chambers of its reflection arrangement \(u_i=\pm u_j\). It preserves \(P_n\) and can move any generic normal into the standard chamber
\[
u_1>u_2>\cdots>u_{n-1}>|u_n|.
\]
Within this chamber the sign of the scalar product of \(u\) with each root \(\tau_i e_i+\tau_j e_j\) with \(i<j\) equals \(\tau_i\), because \(|u_i|>|u_j|\). Thus the vertex-sign partition is independent of the point in the chamber. The face lattice of a hyperplane section that contains no original vertex is determined by which original faces have vertices of both signs: each such original \(d\)-face contributes exactly one \((d-1)\)-face of the section. Hence all generic central sections have isomorphic face lattices; it remains to count the crossing faces in the displayed chamber.

**3. Counting crossing simplex faces.** Fix original dimension \(d\), with \(1\le d\le n-2\). Every fixed-coordinate \(d\)-simplex is specified by a support set \(A\subset[n]\) of size \(d+2\), a distinguished index \(i\in A\), and a sign on every coordinate of \(A\). Its vertices are \(\sigma_i e_i+\sigma_j e_j\) for \(j\in A\setminus\{i\}\). Write \(t=d+1\), and let \(r\) be the number of members of \(A\setminus\{i\}\) larger than \(i\). For fixed \(A,i\), the section does **not** cross the relative interior of the face exactly when all vertex signs agree. If \(r=0\), this occurs for four sign assignments: two choices of common sign among the \(t\) earlier indices and an independent sign at \(i\). If \(r\ge1\), it occurs for \(2^{r+1}\) assignments: the sign at \(i\) fixes the signs at all earlier indices, whereas the \(r\) later signs are unrestricted. For each fixed \(A\), its \(t+1\) choices of distinguished \(i\) give \(r=0,1,\ldots,t\) exactly once. Therefore the number of noncrossing signed simplex faces supported on \(A\) is
\[
4+\sum_{r=1}^t2^{r+1}=2^{t+2}.
\]
There are \((t+1)2^{t+1}\) signed simplex faces supported on \(A\) in total; thus the exact number of crossing \(d\)-simplex faces is
\[
\big((t+1)2^{t+1}-2^{t+2}\big)\binom n{t+1}
=d\,2^{d+2}\binom n{d+2}.
\]

**4. Counting crossing hypersimplex faces.** A positive-dimensional hypersimplex \(d\)-face is specified by \(I\subset[n]\) with \(|I|=d+1\ge3\) and independent signs on \(I\). In the standard normal chamber, a root with indices \(i<j\) has sign equal to its sign at \(i\). Every pair of roots in this face has the same sign **if and only if** the signed coordinates at the first \(d\) indices of \(I\) all agree; the sign at the largest index of \(I\) is irrelevant. Exactly four of the \(2^{d+1}\) sign words are noncrossing, leaving
\[
(2^{d+1}-4)\binom n{d+1}
\]
crossing hypersimplex \(d\)-faces for \(2\le d\le n-1\). For \(d=1\) the same expression vanishes, correctly reflecting that the two-coordinate case is just a vertex rather than a positive-dimensional face.

**5. Counting crossing coordinate facets and assembling dimensions.** For \(u\) in the standard chamber, neither facet \(x_1=1\) nor \(x_1=-1\) crosses the central hyperplane: its vertices all have the same strict sign. Both coordinate facets with index \(i\ge2\) cross, because their vertices using a coordinate \(j=1\) have opposite signs. Hence exactly \(2(n-1)\) coordinate facets cross. For each section face dimension \(0\le k\le n-3\), set \(d=k+1\), and add the two formulae from Steps 3 and 4. The asserted first boxed expression results. At the top dimension, \(d=n-1\), the simplex type is absent; the \(2^n-4\) crossing hypersimplex facets and the \(2(n-1)\) crossing coordinate facets give the second boxed expression. All the steps apply for every \(n\ge5\), proving the theorem.

## Verification
The accompanying pure-Python file `verify_droot_sections.py` reconstructs the roots, all \(2n+2^n\) facet vertex sets, and the complete face lattice by repeated nonempty facet intersections. It determines affine face dimensions using exact rational row reduction, independently of the proof's face classification. For \(n=4,5,6\), it compares the count of strictly sign-crossing faces against the theorem's formula for six generic normals in distinct sign/permutation chambers, and checks the Euler relation. It returns `VERIFY_OK`. These are **finite consistency checks**, not a substitute for the all-dimensional counting proof. The known \(n=4\) row serves only as an overlap/control case.

## Relationship to prior work
Daniele Corradetti, *Integral Shell Polytopes of Composition Algebras* (arXiv:2605.09458v1, publicly released 2026-05-10), identifies a normalized Okubo shell with the \(D_8\) root system in Proposition 4.5 and in its shell table, but studies lattice shells and their root-system identifications rather than central-section face enumerators. Anna Birkemeyer, Anouk E. Brose, Marie-Charlotte Brandenburg, and Niklas Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices* (arXiv:2609.16195v1, publicly released 2026-09-14), investigate the general question of what central section combinatorics reveals. The full preprint could not be inspected; its available abstract does not state a type-\(D_n\) enumeration, but this is a residual historical-priority risk.

The generic central section of the regular \(24\)-cell (the \(D_4\) root polytope) has previously been classified as having \((32,48,18)\) faces, and a published complete seven-type classification covers its singular sections as well. That \(n=4\) case is not claimed as new. A separate published classification determines generic central section face lattices for **type-\(A\)** root polytopes, but does not imply the type-\(D_n\) counts: the root set, face types, dimension, and section numbers differ. Neither the known all-rank cross-polytope section face enumerator nor results on illumination and root-polytope radial geometry imply these numbers. The result claimed here is the complete all-rank \(n\ge5\) type-\(D\) generic section face vector and its chamber invariance. Priority is assessed against inspected and retrieved sources, not proved by unsuccessful searching.

## Limitations
This theorem concerns central hyperplanes only, not translated affine cuts, and excludes all normals with equal absolute coordinate values. No classification of the nongeneric section face vectors, metric areas, or section volumes is asserted. The original root-polytope face classification is elementary, while the specific cancellation to the displayed full section formula is the contribution. The source comparison is not an independent literature certification; equivalent formulae using terminology such as rectified orthoplexes may remain in unindexed sources.

## References
1. D. Corradetti, *Integral Shell Polytopes of Composition Algebras*, arXiv:2605.09458v1, 2026-05-10, https://arxiv.org/abs/2605.09458 (especially Proposition 4.5 and Table 5).
2. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195v1, 2026-09-14, https://arxiv.org/abs/2609.16195.
3. *Seven combinatorial types of all central sections of the regular 24-cell*, published research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-seven-combinatorial-types-of-all-central-sections-of-the-regular--7f0cd1aa480e (\(D_4\) only).
4. *Complete face-lattice law for generic central sections of type-A root polytopes*, published research record, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-face-lattice-law-for-generic-central-sections-of-type-a--a5e29bc260de (type \(A\), not \(D\)).
