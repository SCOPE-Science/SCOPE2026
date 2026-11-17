# Exact outer shell, cyclic-order contacts, and spectral gap of two-dimensional acyclohedra

## Finding

**Theorem.** For every integer \(n\ge3\), let \(B=\partial_2\) denote the oriented triangle-to-edge boundary matrix of the full simplex on \(\{0,1,\ldots,n-1\}\), with the standard orthonormal edge and triangle bases. Define the centered two-dimensional acyclohedron
\[
Z_n=\sum_{0\le i<j<k<n}\left[-\tfrac12 B e_{ijk},\tfrac12 B e_{ijk}\right]\subset\mathbb R^{\binom n2}.
\]
Its Euclidean smallest enclosing ball is unique, centered at the origin, and has squared radius
\[
R_n^2=\frac n4\binom n3=\frac{n^2(n-1)(n-2)}{24}.
\]
Exactly \((n-1)!\) **vertices** of \(Z_n\) contact this ball. They are indexed bijectively by circular orders of the \(n\) labeled vertices (with a choice of orientation; rotations identified, reflections not identified). The Euclidean diameter is
\[
\operatorname{diam}(Z_n)=\sqrt{n\binom n3},
\]
and there are precisely \((n-1)!/2\) unordered diametral pairs of vertices, all antipodal.

For every \(n\ge4\), the **second largest distinct squared norm among the vertices** is exactly
\[
R_n^2-(n-3).
\]
This gap is sharp: flipping any single triangle orientation in a contacting vertex gives a distinct exposed vertex at this second radius. For \(n=3\), both vertices are outer contacts and no second squared norm exists.

This is a statement about the standard *Euclidean* coordinate normalization of the simplex boundary matrix, not an arbitrary affine realization or the lattice-normalized volume.

## Assumptions and scope

A labeled oriented \(k\)-simplex is the basis vector \(e_{i_0\ldots i_k}\) for strictly increasing indices; its boundary is the usual alternating sum. Write \(B=\partial_2:C_2\to C_1\) and \(D=\partial_3:C_3\to C_2\), and equip all chain spaces with the Euclidean metric in which these oriented simplex bases are orthonormal. For a triangle signing \(\sigma\in\{-1,1\}^{\binom n3}\), let
\[
p_\sigma=\tfrac12 B\sigma.
\]
Every such point belongs to \(Z_n\), although not every signing need give an exposed vertex. A vertex means a zero-dimensional face of \(Z_n\). The word "circular order" means a cyclic permutation modulo rotation, *not* modulo reversal. There are \((n-1)!\) such orders.

The uncentered acyclohedron of Pohoata and Zhu is a translation of this centered sum of triangle-boundary segments, so the Euclidean distances, shell multiplicities, and diameter agree under this translation. The result is asserted for every \(n\ge3\). The shell-gap statement requires \(n\ge4\).

## Proof

**1. Orthogonal chain identity.** With the preceding signed incidence conventions,
\[
B^{\mathsf T}B+DD^{\mathsf T}=nI_{\binom n3}.
\]
The diagonal of the first summand is \(3\), since each triangle has three edges. The diagonal of the second is \(n-3\), since each triangle is contained in \(n-3\) tetrahedra. For two distinct triangles sharing a common edge, the signed edge overlap in \(B^{\mathsf T}B\) cancels the unique signed tetrahedron overlap in \(DD^{\mathsf T}\); for triangles meeting in at most one vertex, both off-diagonal terms are zero. This proves the identity for all \(n\ge3\), with an empty tetrahedron block when \(n=3\). Consequently
\[
4\|p_\sigma\|^2=\|B\sigma\|^2=n\binom n3-\|D^{\mathsf T}\sigma\|^2.
\tag{1}
\]

**2. Equality and circular orders.** Equality in the upper bound of (1) holds precisely when \(D^{\mathsf T}\sigma=0\), namely when on each ordered tetrahedron \(0\le a<b<c<d<n\) the signed relation
\[
\sigma_{bcd}-\sigma_{acd}+\sigma_{abd}-\sigma_{abc}=0
\]
holds. Distinguish the label \(0\), and put \(x_{ij}=\sigma_{0ij}\) for \(1\le i<j<n\). Every tetrahedron \(0ijk\) forces
\[
\sigma_{ijk}=x_{jk}-x_{ik}+x_{ij}.
\tag{2}
\]
Give the edge \(ij\) of the complete graph on \(\{1,\ldots,n-1\}\) the orientation \(i\to j\) when \(x_{ij}=1\), and \(j\to i\) otherwise. The right side of (2) belongs to \(\{-1,1\}\) exactly when that directed triple is *not* a directed three-cycle. A tournament without directed three-cycles is transitive, and hence is uniquely determined by a linear order of the \(n-1\) remaining labels. Conversely, any linear order gives \(x_{ij}\) and, via (2), every triangle signing. The tetrahedron relations not containing \(0\) then follow by taking the alternating coboundary of (2), because coboundaries square to zero. Thus the equality signings are in bijection with the \((n-1)!\) linear orders of the nonzero labels, or equivalently the circular orders of all labels with \(0\) fixed at the start.

Every equality signing yields a **distinct exposed vertex**. Indeed, since \(DD^{\mathsf T}\sigma=0\), the chain identity gives \(B^{\mathsf T}B\sigma=n\sigma\). Set \(u=B\sigma/n\). Then \(B^{\mathsf T}u=\sigma\), so the linear functional \(x\mapsto\langle u,x\rangle\) uniquely selects the positive endpoint of every segment whose triangle sign is \(\sigma\), exposing \(p_\sigma\). Conversely, if \(p_\sigma=p_\tau\) for two equality signings, the same exposing functional forces \(\sigma=\tau\). Since the norm is convex and the zonotope is the convex hull of its signed segment endpoints, these are all points of maximal norm and establish the stated radius and contact count.

**3. Diameter and uniqueness of the center.** The set is centrally symmetric, so \(-p_\sigma\) is a vertex whenever \(p_\sigma\) is. For any center \(c\) and an outer contact \(p\),
\[
\max\{\|p-c\|^2,\|-p-c\|^2\}\ge R_n^2+\|c\|^2.
\]
Thus the unique center of the smallest enclosing sphere is \(0\). The triangle inequality gives diameter at most \(2R_n\); an antipodal outer pair attains it. Equality in the Euclidean triangle inequality for a pair at distance \(2R_n\) requires both endpoints to be outer contacts and opposite one another. Counting the \((n-1)!\) outer vertices in opposite pairs yields \((n-1)!/2\) diametral pairs.

**4. Sharp gap to the next vertex shell.** Assume \(n\ge4\). For any signing \(\sigma\) with \(t=D^{\mathsf T}\sigma\ne0\), each coordinate of \(t\) is an even integer (a sum of four signs), hence any nonzero coordinate has squared magnitude at least \(4\). Choose a tetrahedron \(T\) with \(t_T\ne0\). For each label \(v\notin T\), the five tetrahedron coefficients on the boundary of the five-vertex simplex \(T\cup\{v\}\) satisfy a signed linear relation, since \(\partial_3\partial_4=0\). Thus some tetrahedron other than \(T\) inside \(T\cup\{v\}\) has nonzero \(t\). It contains \(v\) and cannot be supplied by any different outside label. There are \(n-4\) outside labels, hence at least \(n-3\) nonzero components of \(t\), and
\[
\|t\|^2\ge4(n-3).
\]
Equation (1) now shows \(\|p_\sigma\|^2\le R_n^2-(n-3)\) whenever the sign pattern is not an outer signing. Every vertex has some signed-endpoint representation, so this bound applies to all other vertices.

For sharpness, start with any outer signing \(\sigma\) and reverse exactly one sign \(\sigma_j\), obtaining \(\sigma'\). Only the \(n-3\) tetrahedra containing triangle \(j\) acquire nonzero coboundary entries, each of magnitude \(2\). Hence (1) gives the claimed squared norm. It is necessary to show that this endpoint is actually a **vertex**. Let \(b_j=Be_j\) and \(u=B\sigma/n\) as above. The witness
\[
u'=u-\tfrac12\sigma_j b_j
\]
has \(\langle b_j,u'\rangle=-\sigma_j/2\), because \(\|b_j\|^2=3\). For any other triangle \(i\ne j\), two distinct triangle boundaries share at most one edge, so \(|\langle b_i,b_j\rangle|\le1\), and \(\langle b_i,u'\rangle\) retains the strict sign \(\sigma_i\). Therefore \(u'\) uniquely exposes \(p_{\sigma'}\), finishing the sharp second-shell argument.

## Verification

The standalone `acyclohedron_verify.py` uses Python's standard library only. Invoke `python3 acyclohedron_verify.py`. It recomputes the two incidence matrices from the oriented simplex definitions; checks every entry of the finite chain identity for orders \(3\) through \(8\); tests all \((n-1)!\) circular-order outer signings for those orders; and exhaustively enumerates all \(2^{\binom n3}\) endpoint signings for \(n=3,4,5,6\), verifying the radius, multiplicity, and second shell. In total, there are \(1,049,618\) exhaustive endpoint configurations and \(22,618\) additional exact identity/order assertions. Beyond order six the sampling of endpoints is *not exhaustive*, and the infinite theorem is certified by the algebraic proof above rather than by enumeration.

For \(n=6\), the exact output includes squared radius \(30\), \(120\) outer signings, and second squared radius \(27\).

## Relationship to prior work

Pohoata and Zhu introduced hypergraphic zonotopes and acyclohedra and proved their Ehrhart/volume and face-sign-pattern results. In particular, their vertex–acyclic-hypertournament correspondence and adjacency characterization are preexisting results, not claimed here. Linial and Morgenstern introduced and investigated high-dimensional acyclic tournaments, including the classical transitive-tournament criterion used in step 2. The present result determines the **Euclidean outermost vertex shell and exact next-shell gap**, not the entire vertex enumeration or the preexisting acyclicity correspondence.

An existing exact result on *near-top acyclohedra* \(\mathcal A_{n,n-3}\) gives their Euclidean enclosing sphere and contact classification. When \(n=5\), \(n-3=2\), so that theorem already implies the radius and outer contacts of the single overlapping instance \(\mathcal A_{5,2}\). The present theorem addresses the fixed two-dimensional acyclohedra \(\mathcal A_{n,2}\) for **all** \(n\), especially \(n\ge6\), and adds the sharp next-shell gap. This is a nontrivial restriction on the historical-priority claim, not a claim of a completely separate family at \(n=5\).

## Limitations

The theorem is specific to the standard simplex-coordinate Euclidean metric, uniform generator segments, and dimension parameter \(d=2\). It does not compute all intermediate vertex shells, general higher-dimensional acyclohedra, or uniform-volume covariance. The proof is mathematical and complete for the stated assertions, but no independent mathematical audit has been performed. Unindexed prior Euclidean computations and alternative equivalent formulations remain possible, so historical priority is provisional.

## References

- Cosmin Pohoata and Daniel G. Zhu, *Hypergraphic zonotopes and acyclohedra*, arXiv:2503.21752 (first posted 2025-03-27): https://arxiv.org/abs/2503.21752 .
- Nati Linial and Avraham Morgenstern, *On high-dimensional acyclic tournaments*, Discrete & Computational Geometry 50 (2013), 1085–1100, arXiv:1302.1684: https://arxiv.org/abs/1302.1684 .
- *Cycle-length facet shells and tournament contacts in near-top acyclohedra*, recorded mathematical finding, 2026-11-08: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cycle-length-facet-shells-and-tournament-contacts-in-near-top-ac--32c5a604eada .
