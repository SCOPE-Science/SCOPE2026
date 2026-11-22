# Facet-area laws and reversal asymmetry of linked symmetric-snake polytopes

## Finding
For every integer \(n\ge3\) and every \(S\subseteq[n-1]\), the standard Euclidean feasible polytope of the linked type-\(C\) snake interval \([S,S\cup\{n\}]\) has a complete, explicit Euclidean facet-area measure computed from linear extensions of three elementary path-poset minors. In the notation below, every facet, its primitive outward normal, and its \((n-1)\)-dimensional area are specified in the theorem.

The area formula implies a strict reversal phenomenon in every dimension \(n\ge4\). The profiles \(S=\{1\}\) and \(T=\{n-1\}\) have affinely unimodularly equivalent polytopes, identical face lattices, and equal Euclidean volume \((n-1)/n!\), yet
\[
\operatorname{Area}_{n-1}(\partial P_T)-\operatorname{Area}_{n-1}(\partial P_S)
=\frac{(n-3)(\sqrt n-1)-(n-1)(\sqrt{n-1}-\sqrt2)}{(n-1)!}>0.
\]
At \(n=3\), their areas are equal. For increasing \(n\), the positive area difference is asymptotic to \((\sqrt2-1)n/(n-1)!\).

## Assumptions and scope
Use ordinary Lebesgue measure and standard Euclidean surface measure in the displayed \(x\)-coordinates (not a metric transported from an order polytope). Define \(b_i=\mathbf1_{i\in S}\) for \(1\le i<n\), \(b_n=0\), and \(c_i=\sum_{j=i}^{n-1}b_j\). By the linked-snake inequality description of Chen--Sanchez--Veliz--Ying, the polytope is
\[
P_S=\left\{x\in[0,1]^n:c_i\le\sum_{j=i}^{n}x_j\le c_i+1\quad(1\le i\le n)\right\}.
\]
Define the \(n\)-element path poset \(Q_S\) by taking the transitive closure of the relations \(i\prec i+1\) if \(i\in S\), and \(i+1\prec i\) otherwise, for \(1\le i<n\). Each such relation is a cover. Write \(e(Q)\) for the number of linear extensions of a finite poset \(Q\). Let \(Q_S\setminus\{i\}\) be the induced poset after deleting \(i\); let \(Q_S/(i,i+1)\) be the poset obtained by identifying the endpoints of their cover edge, retaining the induced relations and transitive closure. Because the underlying Hasse graph is a path, this contraction is a poset with \(n-1\) elements.

## Proof
**Complete facet-area measure.** For every \(1\le i<n\), there is exactly one coordinate facet \(x_i=b_i\), whose Euclidean area is
\[
A_i^{\mathrm{cover}}=\frac{e(Q_S/(i,i+1))}{(n-1)!}.
\]
Its primitive outward normal is \(-\mathbf e_i\) when \(b_i=0\) and \(+\mathbf e_i\) when \(b_i=1\). For each minimal element \(i\) of \(Q_S\), there is exactly one lower-suffix facet \(\sum_{j=i}^n x_j=c_i\) with outward normal \(-\sum_{j=i}^n\mathbf e_j\). For each maximal element \(i\), there is exactly one upper-suffix facet \(\sum_{j=i}^n x_j=c_i+1\) with outward normal \(+\sum_{j=i}^n\mathbf e_j\). Each of these has area
\[
A_i^{\mathrm{end}}=\frac{\sqrt{n-i+1}\,e(Q_S\setminus\{i\})}{(n-1)!}.
\]
These are all facets, with no repetitions. In particular,
\[
\operatorname{Area}_{n-1}(\partial P_S)=\frac{\displaystyle\sum_{i=1}^{n-1}e(Q_S/(i,i+1))+
\displaystyle\sum_{i\in\operatorname{Min}(Q_S)\cup\operatorname{Max}(Q_S)}\sqrt{n-i+1}\,e(Q_S\setminus\{i\})}{(n-1)!},
\]
while \(\operatorname{Vol}_n(P_S)=e(Q_S)/n!\).

To prove the formulas, introduce the affine unimodular change of coordinates
\[
y_i=\sum_{j=i}^n x_j-c_i,\qquad x_i=b_i+y_i-y_{i+1}\ (i<n),\quad x_n=y_n.
\]
Here \(y_{n+1}=0\), and the linear change has determinant one. The suffix inequalities become \(0\le y_i\le1\); the coordinate inequalities for \(i<n\) become \(y_i\le y_{i+1}\) when \(b_i=1\) and \(y_i\ge y_{i+1}\) otherwise. Therefore \(P_S\) is an affine unimodular image of the order polytope \(\mathcal O(Q_S)\).

The irredundant facets of an order polytope are its lower-coordinate hyperplanes at minimal elements, upper-coordinate hyperplanes at maximal elements, and equality hyperplanes along covers. Fixing a minimal coordinate to zero, a maximal coordinate to one, or contracting a cover yields an \((n-1)\)-element order polytope. Its \((n-1)\)-dimensional lattice-normalized volume equals the corresponding linear-extension count divided by \((n-1)!\), by the canonical unimodular triangulation. In the \(x\)-lattice, the facet's primitive normal has Euclidean norm \(\sqrt{n-i+1}\) for a suffix facet and norm one for a coordinate facet. The fundamental covolume of the integer lattice in a primitive-normal hyperplane is exactly the norm of that normal. Multiplying normalized facet volumes by these covolumes gives the stated formulas.

**The reversal gap.** Let \(S=\{1\}\) and \(T=\{n-1\}\). The two path posets are identified by reversing labels and dualizing order; the map \(y_i\mapsto1-y_{n+1-i}\) therefore identifies the order polytopes. Their respective \(x\)-polytopes are consequently affinely unimodularly equivalent. Each poset has \(n-1\) linear extensions, proving equal volume. In both cases the sum of the cover-contraction extension counts is \(1+(n-2)^2\).

For \(S\), the deleted-element contributions, before their normal-length weights, are \(1\) at position \(1\), \(n-1\) at position \(2\), and \(n-2\) at position \(n\). For \(T\), they are \(n-2\) at position \(1\), \(n-1\) at position \(n-1\), and \(1\) at position \(n\). Hence
\[
\begin{aligned}
(n-1)!\operatorname{Area}_{n-1}(\partial P_S)&=1+(n-2)^2+\sqrt n+(n-1)\sqrt{n-1}+n-2,\\
(n-1)!\operatorname{Area}_{n-1}(\partial P_T)&=1+(n-2)^2+(n-2)\sqrt n+(n-1)\sqrt2+1.
\end{aligned}
\]
Subtracting gives the formula in the Finding section. For real \(t\ge4\), define \(f(t)=(t-3)(\sqrt t-1)-(t-1)(\sqrt{t-1}-\sqrt2)\). Direct differentiation yields
\[
f'(t)=\sqrt2-1+\frac32\left(\frac1{\sqrt t+\sqrt{t-1}}-\frac1{\sqrt t}\right)
>\sqrt2-1-\frac3{4\sqrt t}\ge\sqrt2-\frac{11}{8}>0.
\]
Also \(f(4)=1-3/(\sqrt3+\sqrt2)>0\). Thus every integer \(n\ge4\) has a strict gap. Expansion of the radical terms gives \(f(n)=(\sqrt2-1)n+O(\sqrt n)\).

## Verification
The companion `verify_snake_area.py` independently enumerates binary order-polytope vertices, transforms them to \(x\)-coordinates, and compares exact extension-count predictions with Euclidean volumes and surface areas computed from convex hulls. All \(124\) profiles in dimensions \(3\) through \(7\) passed; further exact count identities and positive-gap inequalities were checked. The proof, not these finite computations, establishes the statement for all \(n\).

## Relationship to prior work
Chen, Sanchez, Veliz, and Ying (arXiv:2311.15441v1, first posted 2023-11-26) provide the linked type-\(C\) snake inequality description and their unimodular volume formula; those are inputs, not claimed discoveries. Stanley's classical order-polytope theory provides the cover/minimal/maximal facet classification and the linear-extension volume formula. The new statements here are the **complete facet-area measure in the original Euclidean coordinates** and the explicit, dimension-uniform reversal gap between equal-volume unimodularly equivalent members. Earlier work on ordinary snake matroids and on distance spectra of linked type-\(C\) snakes concerns different invariants.

## Limitations
The result is for linked type-\(C\) snake intervals with \(n\ge3\) in the standard displayed Euclidean metric. It does not determine intrinsic volumes beyond surface area, nor an isoperimetric ordering among all profiles \(S\). The prior-art comparison cannot exclude inaccessible or unindexed equivalent facet-measure treatments; independent verification and external historical-priority review have not been performed.

## References
- D. M. Chen, M. Sanchez, J. Veliz, and Z. Ying, *Lattice Path Delta Matroids*, arXiv:2311.15441v1 (2023), especially Theorem A, Proposition 5.3, Corollary 5.4, and Corollary 5.10. https://arxiv.org/pdf/2311.15441
- R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. https://doi.org/10.1007/BF02187680
- C. Benedetti, K. Knauer, J. Valencia-Porras, *On lattice path matroid polytopes: alcoved triangulations and snake decompositions*, arXiv:2303.10458 (first posted 2023-03-18), for the ordinary snake-order-polytope relationship. https://arxiv.org/abs/2303.10458
