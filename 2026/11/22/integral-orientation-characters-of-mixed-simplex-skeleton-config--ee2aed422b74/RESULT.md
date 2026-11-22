# Integral orientation characters of mixed simplex-skeleton configuration manifolds

## Finding
For all integers \(p,q\ge1\), write \(N=p+q+3\) and define the ordered two-particle, mixed-skeleton deleted product
\[
M_{p,q}=\operatorname{DConf}\bigl(\operatorname{sk}_p\Delta^{N-1},\operatorname{sk}_q\Delta^{N-1}\bigr).
\]
It is a closed, connected PL manifold of dimension \(p+q\) by González, González and Pérez-Morales, Theorem 1.3 (2026). **Its integral orientation and its complete top-homology permutation character** are as follows.

For each top cell indexed by disjoint \(S,T\subset[N]\) with \(|S|=p+1\) and \(|T|=q+1\), let \(w\) be the unique vertex outside \(S\cup T\). Order \(S\) and \(T\) increasingly and let \(\varepsilon(S,T,w)\in\{+1,-1\}\) be the sign of the full permutation formed by listing \(S\), then \(T\), then \(w\). With the usual oriented product cell \([S]\times[T]\), the explicit cellular chain
\[
\boxed{\Omega_{p,q}=\sum_{S,T}\varepsilon(S,T,w)[S]\times[T]}
\]
is an integral fundamental cycle. In particular, each \(M_{p,q}\) is **orientable even when \(p\ne q\)**. The full vertex-symmetry action on its top integral homology is
\[
\boxed{H_{p+q}(M_{p,q};\mathbb Z)\cong\mathbb Z_{\operatorname{sgn}}\quad\text{as an }S_N\text{-module}.}
\]
When \(p=q=d\), interchange of the two particles is a free PL involution \(\tau\) satisfying \(\tau_*[\Omega_{d,d}]=-[\Omega_{d,d}]\). Consequently
\[
\boxed{M_{d,d}/\langle\tau\rangle\ \text{is a connected nonorientable closed PL }2d\text{-manifold},\quad d\ge1.}
\]
This determines orientation, the integral orientation character, and the orientation obstruction of the unlabeled quotient, without assuming a connected-sum classification.

## Assumptions and scope
Fix the vertex ordering \(1<\cdots<N\). A cell of \(M_{p,q}\) is the product of relative interiors of nonempty disjoint simplex faces \(S,T\) with \(|S|\le p+1\) and \(|T|\le q+1\). Its dimension is \(|S|+|T|-2\). Orient a simplex by increasing vertex order and a product by the first-factor-then-second-factor convention. For all \(p,q\ge1\), Theorem 1.3 in the motivating paper establishes that this is a connected closed combinatorial manifold. The new assertions above are about integral orientation and symmetry; a particle swap is an action on the same space only for \(p=q\).

## Proof
**1. Top facets and ridges.** A top cell has \(|S|=p+1\), \(|T|=q+1\), and there is exactly one unused vertex \(w\), since \(N=p+q+3\). Every ridge is made by deleting one element of either factor and has exactly two incident facets: reinserting the removed element, or substituting the formerly unused vertex \(w\). There are no cells of dimension greater than \(p+q\).

**2. An explicit integral orientation cycle.** Form \(\Omega_{p,q}\) with coefficient \(\varepsilon(S,T,w)\) defined in the finding. The boundary of \([S]\times[T]\) is \(\partial[S]\times[T]+(-1)^p[S]\times\partial[T]\). Consider a ridge made by deleting the \(i\)-th element of \(S\). The two adjacent facets differ by exchanging that deleted element and \(w\), followed by reordering the first factor. The full-permutation sign changes by minus the reordering sign. The two cellular incidence coefficients for the ridge differ precisely by the same reordering sign. Thus their contributions to \(\partial\Omega_{p,q}\) cancel. The same argument applies to a deletion in \(T\), with the common product-boundary factor \((-1)^p\). Every ridge has exactly these two incidences, so \(\partial\Omega_{p,q}=0\) over \(\mathbb Z\).

**3. Primitivity and orientability.** Every facet appears in \(\Omega_{p,q}\) with coefficient \(\pm1\). No higher-dimensional cellular chain exists, so \(\Omega_{p,q}\) is nonzero in top homology; its coefficient vector is primitive. Since \(M_{p,q}\) is a connected closed PL manifold, top homology of an oriented manifold is \(\mathbb Z\), and existence of a nonzero top integral cycle with coefficient \(\pm1\) on every facet supplies a coherent global orientation. Hence \(\Omega_{p,q}\) is a generator of \(H_{p+q}(M_{p,q};\mathbb Z)\cong\mathbb Z\).

**4. Vertex permutations.** For \(\sigma\in S_N\), the cellular action sends \([S]\times[T]\) to the product cell on \(\sigma S,\sigma T\), multiplied by the sign needed to sort the vertices in each factor. In the full list \((S,T,w)\), applying \(\sigma\) changes permutation sign by \(\operatorname{sgn}(\sigma)\). The two sorting signs cancel exactly with the local orientation factors, giving
\[
\sigma_*\Omega_{p,q}=\operatorname{sgn}(\sigma)\,\Omega_{p,q}.
\]
This proves the integral sign-lattice representation, not just a rational character.

**5. Particle interchange and its quotient.** If \(p=q=d\), the swap \(\tau\) sends each oriented product \([S]\times[T]\) to \((-1)^{d^2}[T]\times[S]\). Exchanging the two full vertex blocks in \((S,T,w)\) changes \(\varepsilon\) by \((-1)^{(d+1)^2}\). Therefore
\[
\tau_*\Omega_{d,d}=(-1)^{d^2+(d+1)^2}\Omega_{d,d}=-\Omega_{d,d}.
\]
The involution has no fixed point: the supports of the two particles lie in disjoint faces, so they cannot be equal. A free PL involution on a closed PL manifold has a closed PL manifold quotient. A connected orientable manifold has orientable quotient under a free involution precisely when the involution preserves the orientation. Here it reverses orientation; thus \(M_{d,d}/\langle\tau\rangle\) is nonorientable in every positive dimension parameter.

## Verification
The standalone Python 3 file `orientation_checker.py` enumerates all top facets and ridges and computes their exact integer signs. It verifies \(\partial\Omega=0\) coefficient-by-coefficient; every adjacent transposition acts by \(-1\) after incorporating factor-orientation signs; and particle interchange acts by \(-1\) in balanced cases. Tests pass for nine pairs: \((1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(1,4),(4,1),(2,4)\). The finite tests corroborate but do not replace the all-parameter proof. Run `python3 orientation_checker.py` from the extracted package directory.

## Relationship to prior work
González, González and Pérez-Morales (arXiv:2611.12847v1, first public 2026-11-09), Theorems 1.1 and 1.3 and Proposition 2.5, establish that the balanced spaces are orientable and all mixed-skeleton spaces are closed PL manifolds. Their Remark 1.5 treats **mixed-skeleton orientability as a conditional expected consequence** of the connected-sum conjecture (Conjecture 1.6); no explicit mixed orientation or vertex-permutation character appears in those stated results. The present proof supplies these conclusions without the conjecture and adds the free-exchange nonorientability obstruction in all balanced dimensions.

González and González (arXiv:2307.14454v1; Selecta Mathematica 31, Article 60, 2025) compute homology for **equal** skeleta, including the balanced manifold homology; these results do not classify the mixed-skeleton orientation character or the free-exchange quotient. Earlier deleted-product sphere models for complete simplices give related sign-orientation ingredients but do not themselves assert a cellular fundamental class for this mixed truncation. The published published-finding corpus finding `SCOPE-integral-vertex-and-swap-homology-of-two-point-simplex-skeleton--f489646eedaa` instead treats the \((n-3)\)-skeleton on \(n\) vertices, with a different dimension and a non-one-dimensional top homology lattice, so neither theorem implies the other.

## Limitations
The result addresses orientation and integral top-dimensional symmetry only. It does not prove the conjectured connected-sum homotopy equivalence, compute all middle-dimensional cup products, classify arbitrary automorphisms, or analyze manifolds with a zero skeleton parameter. For \(p\ne q\), particle interchange identifies different ordered mixed spaces rather than defining a self-involution. A full external priority review and independent mathematical validation have not been performed.

## References
1. E. J. González, J. González, and M. C. Pérez-Morales, *Discrete Configuration Spaces of Simplex Skeleta: a Middle-Dimensional Manifold Phenomenon*, arXiv:2611.12847v1, 2026-11-09, Theorems 1.1, 1.3; Proposition 2.5; Remark 1.5. https://arxiv.org/abs/2611.12847
2. E. J. González and J. González, *An algorithmic discrete gradient field for non-colliding cell-like objects and the topology of pairs of points on skeleta of simplexes*, arXiv:2307.14454v1 (2023-07-26); *Selecta Mathematica* 31, Article 60 (2025), Theorem 1.2. https://arxiv.org/abs/2307.14454
3. A. Abrams, D. Gay, and V. Hower, *Discretized configurations and partial partitions*, arXiv:1009.2935. https://arxiv.org/abs/1009.2935
4. *Integral vertex-and-swap homology of two-point simplex-skeleton configurations*, published published-finding corpus research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-vertex-and-swap-homology-of-two-point-simplex-skeleton--f489646eedaa
