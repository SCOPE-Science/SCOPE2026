# Lattice-diameter segments of every hypersimplex: an exact Ehrhart decomposition and a degree drop

## Finding
For integers \(n\ge2\), \(1\le k<n\), and \(t\ge1\), let
\[\Delta_{n,k}=\left\{x\in[0,1]^n:\sum_{i=1}^n x_i=k\right\}.\]
A lattice segment has *lattice length* equal to the number of integer steps between its endpoints: if the endpoint difference is \(m u\) with primitive integral \(u\), its length is \(m\). Its lattice diameter is the maximum such length in the polytope. Distinct segments are treated as unoriented and counted once.

The lattice diameter of \(t\Delta_{n,k}\) is \(t\). Its complete maximal-segment count is
\[
D_{n,k}(t)=\sum_{p=1}^{\min(k,n-k)}
\frac{n!}{2(p!)^2(n-2p)!}
\,[z^{(k-p)t}]\,(1+z+\cdots+z^t)^{n-2p}.
\tag{1}
\]
The summands are lattice-point enumerators of lower-dimensional hypersimplices, with a singleton convention for dimension zero. Formula (1) is an exact polynomial for *all* integral \(t\ge1\). If \(k=1\) or \(k=n-1\), then \(D_{n,k}(t)=\binom n2\) is constant. For \(n\ge4\) and \(2\le k\le n-2\), its degree is exactly \(n-3\), with leading coefficient
\[
\frac{\binom n2}{(n-3)!}A(n-3,k-2),
\tag{2}
\]
where \(A(m,j)\) counts permutations of \(m\) elements having precisely \(j\) descents. Thus, although \(\Delta_{n,k}\) has intrinsic dimension \(n-1\), the number of maximal lattice segments grows with degree \(n-3\), not \(n-2\).

In rank two, for \(n\ge4\),
\[
D_{n,2}(t)=\binom n2\binom{t+n-3}{n-3}+3\binom n4.
\tag{3}
\]
For example, \(D_{4,2}(t)=6t+9\).

## Assumptions and scope
The ambient lattice is \(\mathbb Z^n\); the intrinsic affine lattice is its intersection with the hyperplane \(\sum_i x_i=kt\). The hypersimplex is integral and of dimension \(n-1\) for \(1\le k<n\). A primitive direction \(u\) is a nonzero vector of integers with coordinate gcd equal to one. The segment count is **not** the number of all lattice segments or the graph diameter of the polytope. We count only segments whose lattice length equals the global maximum \(t\), across all possible lattice directions and positions.

## Proof
**1. Sharp diameter and directions.** Every coordinate of a point of \(t\Delta_{n,k}\) lies between \(0\) and \(t\). If two distinct integer points differ by \(m u\) for primitive integral \(u\), then some \(|u_i|\ge1\), forcing \(m\le t\). Conversely, two vertices of \(\Delta_{n,k}\) corresponding to distinct \(k\)-element subsets that differ by replacing one element have difference \(e_i-e_j\); their \(t\)-multiples give a lattice segment of length exactly \(t\). Hence the maximum is \(t\).

For any segment of that maximum length, its endpoint difference is \(tu\). Every \(|tu_i|\le t\), so \(u_i\in\{-1,0,1\}\). Since the two endpoints have equal coordinate sums, \(\sum_i u_i=0\), and the numbers of \(+1\) and \(-1\) entries are equal, say \(p\). In all plus coordinates, the endpoints must be \(0,t\); in all minus coordinates they must be \(t,0\) in the opposite order. Every remaining coordinate is constant along the segment, with a common value in \(\{0,\ldots,t\}\). The residual constants have sum \((k-p)t\). Such a tuple exists precisely when \(p\le k\) and \(p\le n-k\), since there are \(n-2p\) free coordinates. This also shows that every direction listed in the finding does occur.

**2. Exact nonoverlapping count.** Fix \(p\). Choose \(p\) plus locations, \(p\) minus locations, and \(n-2p\) zero locations: there are \(n!/(p!^2(n-2p)!)\) ordered sign words. Reversal exchanges plus and minus and never fixes a nonzero sign word, so dividing by two counts unoriented directions exactly. The residual tuples are exactly the coefficient of \(z^{(k-p)t}\) in \((1+z+\cdots+z^t)^{n-2p}\). Different signs or residual tuples yield different lattice segments, and each maximal segment yields one such description. Summing gives (1), including the case of no free coordinates.

**3. Polynomiality at every dilation.** For \(q\ge1\) and \(0\le s\le q\), the bounded-composition count
\[H_{q,s}(t)=[z^{st}](1+z+\cdots+z^t)^q\]
is the lattice-point count of \(t\Delta_{q,s}\). This is a polynomial in \(t\) by Ehrhart's theorem (a singleton when \(s=0\) or \(s=q\)). It also has the explicit inclusion–exclusion formula, for \(s\ge1\),
\[
H_{q,s}(t)=\sum_{j=0}^{s-1}(-1)^j\binom qj
\binom{(s-j)t+q-1-j}{q-1},\qquad t\ge1.
\tag{4}
\]
The terms with \(j\ge s\) in the standard bounded-composition inclusion–exclusion formula have negative residual sum and are omitted; formula (4) is an ordinary polynomial on the given domain. Set \(H_{q,0}=1\), and \(H_{0,0}=1\). Substituting \(q=n-2p\), \(s=k-p\) into (1) proves all-dilation polynomiality.

**4. Exact degree and leading coefficient.** For \(k=1\) (and symmetrically \(k=n-1\)), only \(p=1\) is possible; its residual sum is zero, giving \(D_{n,k}=\binom n2\). If \(2\le k\le n-2\), the \(p=1\) contribution has \(q=n-2\) and \(s=k-1\), with \(0<s<q\). Its Ehrhart polynomial has degree \(q-1=n-3\) and strictly positive leading coefficient \(A(q-1,s-1)/(q-1)!\). This follows from the classical Eulerian-volume formula for hypersimplices (or directly by taking highest-degree terms in (4)). Contributions with \(p\ge2\) have \(q\le n-4\), hence degree at most \(n-5\) when full-dimensional, or degree zero for degenerate residuals. Thus the \(p=1\) term is the unique highest-degree term and gives (2) without cancellation. Finally, at \(k=2\), only \(p=1,2\) occur; their residual counts are respectively \(\binom{t+n-3}{n-3}\) and one, with direction multiplicities \(\binom n2\) and \(3\binom n4\), proving (3).

## Verification
The standalone `verify.py` (Python standard library only) independently enumerates integer pairs in dilated hypersimplices, computes the gcd of their coordinate differences, and counts the pairs whose length equals the predicted diameter. It compares this direct pair count to (1) for all \(2\le n\le7\), every rank, and \(t=1,2,3\). It separately checks polynomial finite differences and Eulerian leading coefficients for \(2\le n\le14\), and the rank-two formula for \(4\le n\le14\), \(1\le t\le8\). Running `python verify.py` produced `PASS 333 independent exact assertions`. This finite verification is corroborative; the preceding proof is valid for all stated parameters.

## Relationship to prior work
Averkov, Brose, De Loera, Lopez-Campos, and Torres, *On Lattice Diameter Segments: Algorithms and Structure*, arXiv:2508.20009 (originally public 27 August 2025), introduce the maximal-lattice-segment counting function and prove general eventual quasipolynomiality (Theorem 4.6). Their Example 4.7 exhibits a planar quasipolynomial with a genuine period. Their general theorem alone does not provide (1), (2), the hypersimplex direction classification, or polynomiality valid from the first dilation. Nan Li's *Ehrhart \(h^*\)-vectors of hypersimplices* analyzes ordinary lattice-point counts and Eulerian hypersimplex volumes; those are used here only after the new geometric reduction of maximal segments to lower hypersimplex enumerators. They do not themselves assert (1). The exact relationship is therefore a new **segment-count** invariant expressed through known **point-count** invariants.

## Limitations
This result concerns uniform-matroid base polytopes (hypersimplices) in their standard integral embedding, not arbitrary matroid base polytopes or general lattice polytopes. It does not imply polynomiality of maximal-segment counts for all polytopes: quasipolynomial behavior is known in the general setting. The use of classical hypersimplex Ehrhart volumes in (2) is acknowledged. Historical novelty is based on inspected available sources and indexed searches, not on exhaustive publication priority review; independent review has not been performed.

## References
1. G. Averkov, A. E. Brose, J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On Lattice Diameter Segments: Algorithms and Structure*, arXiv:2508.20009v2 (2026 revision); first public arXiv version dated 2025-08-27. https://arxiv.org/html/2508.20009 ; https://arxiv.org/abs/2508.20009
2. Nan Li, *Ehrhart \(h^*\)-vectors of hypersimplices*, Discrete Mathematics & Theoretical Computer Science, FPSAC proceedings (2013), 121–132; https://dmtcs.episciences.org/articles/12798
3. Classical Ehrhart polynomiality and the Eulerian normalized-volume formula for hypersimplices; see Reference 2, Introduction and Theorem 1.1.
