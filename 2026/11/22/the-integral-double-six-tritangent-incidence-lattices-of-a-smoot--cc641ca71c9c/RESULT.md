# The integral double-six–tritangent incidence lattices of a smooth cubic surface

## Finding
For every smooth cubic surface \(S\) over an algebraically closed field of characteristic zero, write \(\mathcal D\) for its \(36\) unordered Schläfli double-sixes and \(\mathcal T\) for its \(45\) tritangent planes. Let \(L(S)\) be the set of \(27\) lines; interpret a tritangent plane as the triple of lines it cuts out. Every double-six and tritangent triple have exactly zero or two lines in common. The integer incidence pairing
\[
B:\mathbb Z^{\mathcal T}\to\mathbb Z^{\mathcal D},\qquad B_{D,T}=\tfrac12|D\cap T|\in\{0,1\}
\]
and its complementary pairing \(C=J-B\) have rank \(21\) over \(\mathbb Q\) and complete cokernels
\[
\boxed{\begin{aligned}
\operatorname{coker}(B)&\cong\mathbb Z^{15}\oplus(\mathbb Z/3\mathbb Z)^5\oplus\mathbb Z/18\mathbb Z,\\
\operatorname{coker}(C)&\cong\mathbb Z^{15}\oplus(\mathbb Z/3\mathbb Z)^7.
\end{aligned}}
\]
Thus \(B\) has nonzero Smith invariant factors \(1\) fifteen times, \(3\) five times and \(18\) once; \(C\) has \(1\) fourteen times and \(3\) seven times. This is an integral comparison between two distinguished kinds of cubic-surface configurations, not an assertion about torsion in the surface's Picard group.

## Assumptions and scope
The field is algebraically closed of characteristic zero and \(S\) is geometrically smooth. Choose an arbitrary blowdown to six points of \(\mathbb P^2\) in general position; with \(H\) the plane hyperplane pullback and \(E_i\) the six exceptional classes, \(\operatorname{Pic}(S)=\mathbb ZH\oplus\bigoplus_{i=1}^6\mathbb ZE_i\) has \(H^2=1\), \(E_i^2=-1\), and all other basis pairings zero. The twenty-seven line classes are
\[
 E_i\ (1\le i\le6),\quad L_{ij}=H-E_i-E_j\ (i<j),\quad Q_i=2H-\sum_{j\ne i} E_j.
\]
The anticanonical class is \(-K_S=3H-\sum_iE_i\). A tritangent triple is a three-element subset of these classes whose sum is \(-K_S\). A double-six is the union of two sixers: a sixer consists of six pairwise disjoint lines, and its unique partner sixer has every line meeting five of the first six lines. Reordering lines, double-sixes or tritangents changes the matrices by unimodular permutation matrices only, leaving their Smith invariants and cokernels unchanged.

## Proof
**1. Geometric enumeration.** Classical cubic-surface geometry gives \(45\) tritangent triples (thirty of type \(\{E_i,L_{ij},Q_j\}\), \(i\ne j\), plus fifteen triples of the \(L_{ij}\) indexed by perfect matchings of six labels), and \(36\) double-sixes (the \(72\) sixers paired by their uniquely determined partner). An independent second description of double-sixes uses the \(36\) pairs of opposite roots in \(E_6\): for a root \(r\), take precisely the twelve lines \(\ell\) for which \(\ell\cdot r\ne0\). There are six with pairing \(1\), six with pairing \(-1\), and fifteen with pairing zero. A complete root-representative list consists of \(E_i-E_j\) for \(i<j\), \(H-E_i-E_j-E_k\) for triples of indices, and \(2H-\sum_iE_i\). The attached checker reconstructs both lists independently and verifies that they agree.

**2. Why the half-incidence entries are integers.** For each root \(r\), each line in the double-six has intersection \(1\) or \(-1\) with \(r\), and all other lines have intersection zero. If \(\ell_1+\ell_2+\ell_3=-K_S\), then
\[
 (\ell_1+\ell_2+\ell_3)\cdot r=(-K_S)\cdot r=0.
\]
The three summands are in \(\{-1,0,1\}\). Therefore they are either all zero or comprise one \(1\), one \(-1\), and one zero. Accordingly \(|D\cap T|\in\{0,2\}\), proving the half-incidence normalization without division in the integral matrix. Enumerating the fixed geometric configuration yields \(1080\) two-line pairs and \(540\) zero-line pairs; each double-six occurs with \(30\) two-line tritangents, each tritangent with \(24\) double-sixes.

**3. Integral Smith calculation.** Index line classes as \(E_1,\ldots,E_6\), then lexicographically by the fifteen \(L_{ij}\), then \(Q_1,\ldots,Q_6\). Generate all \(72\) sixers recursively by the exact disjointness test \(\ell\cdot\ell'=0\); deduplicate their paired unions to obtain \(36\) twelve-line sets. Generate all \(45\) anticanonical triples by testing all \(\binom{27}{3}\) choices. Construct \(B\) entrywise from the overlap rule and \(C=J-B\). These are complete finite enumerations, not sample surfaces.

Apply ordinary integral Smith reduction independently to both rectangular matrices. At stage \(k\), bring a nonzero entry to the current pivot by row and column swaps. Euclidean-divide lower entries by the pivot, subtract integer multiples of its row, and swap a row with a pivot row if a nonzero remainder persists; do the symmetric operation for entries to the pivot's right. When the pivot row and column are clear, if the pivot fails to divide an entry of the trailing submatrix, add that entry's row to the pivot row and continue Euclidean reduction. Otherwise the pivot divides every trailing entry; make the pivot positive and advance. All operations are invertible over \(\mathbb Z\) and the resulting diagonal satisfies consecutive divisibility. The standalone verifier implements exactly this algorithm, checks that all off-diagonal entries vanish, and returns
\[
 \operatorname{SNF}(B)=\operatorname{diag}(1^{[15]},3^{[5]},18,0^{[15]}),\qquad
 \operatorname{SNF}(C)=\operatorname{diag}(1^{[14]},3^{[7]},0^{[15]}).
\]
The displayed zeros count the remaining rows in the \(36\)-row rectangular presentation; extra zero columns are implicit. Thus \(\operatorname{rank}(B)=\operatorname{rank}(C)=21\), and the claimed free ranks and torsion factors follow directly from the structure theorem for finitely generated abelian groups.

**4. Independent exact spectral check.** Direct integer multiplication of the reconstructed matrices verifies the annihilating identities \((BB^\mathsf T)(BB^\mathsf T-18I)(BB^\mathsf T-720I)=0\) and \((CC^\mathsf T)(CC^\mathsf T-18I)(CC^\mathsf T-180I)=0\). Together with the row-sum and trace data, these give Gram eigenvalues \(720^{[1]},18^{[20]},0^{[15]}\) for \(B\) and \(180^{[1]},18^{[20]},0^{[15]}\) for \(C\), corroborating the rank but not replacing the integral Smith computation.

**5. Uniformity.** Every smooth cubic surface in the stated characteristic admits a blowdown onto six points in general position and has exactly the above line intersection configuration. The constructed incidence maps consequently differ only by permutations from those checked, for **every** such surface, with no genericity restriction beyond smoothness.

## Verification
Run `python3 verify_double_six_tritangent.py` with the standard Python library. The program reconstructs the \(27\) line divisor classes, independently enumerates double-sixes via \(72\) disjoint sixers and \(36\) root representatives, enumerates all tritangent triples, verifies every \(D\)-\(T\) overlap and both degree profiles, and implements unimodular Smith reduction on both exact matrices. Separate direct matrix multiplications confirm both Gram polynomial identities. A successful replay prints `DOUBLE_SIX_TRITANGENT_INTEGRAL_INCIDENCE_OK`. A separate exact computation using a different Smith implementation gave identical factors. The complete finite computation proves the fixed universal combinatorial incidence model; the classical classification of smooth cubic surfaces transports it to all \(S\) in scope.

## Relationship to prior work
Dolgachev–Kapranov (1993, §0) explain the \(27\)-line blowup geometry and the \(36\) Schläfli double-sixes. Van Geemen (2001, §1.8) explicitly lists the \(45\) tritangents and their root-system geometry. Alexeev–Donagi–Farkas–Izadi–Ortega (2015, §2) identify double-sixes with opposite \(E_6\) roots. Arap–Varley (2012, §2) work with rational line-class relations in a different Abel–Prym setting. These are established inputs, not newly claimed.

Two earlier integral calculations give, separately, the Smith invariants of the \(27\)-by-\(36\) line–double-six map and of the \(27\)-by-\(45\) line–tritangent map. The first has nonzero Smith factors \(1^{[6]},2^{[14]},4\); the second has \(21\) unit factors. The present maps are instead **cross-pairings between their columns**, of shape \(36\)-by-\(45\), and their full Smith forms do not follow just from the separate Smith lists (relative placement of the two lattices matters). In particular the explicit \(3\)-primary torsion and the contrasting complementary pairing are not results stated in those earlier reports. Search comparisons included historical aliases (Schläfli, root-pair incidence, cubic-surface double-sixes), normalizations and possible stronger modules.

## Limitations
The cokernels are quotients of **formal free configuration lattices**; they are not asserted to be Picard or Néron–Severi torsion or geometric Brauer groups. The result is about the complete smooth characteristic-zero cubic-surface configuration, not degenerate cubic surfaces or arithmetic Galois forms. No independent historical priority guarantee is made: a general \(E_6\) permutation-module or association-scheme computation could contain an equivalent integral matrix calculation under different terminology. The exact Smith calculation depends on the included readable, deterministic arithmetic verifier; a separate independent mathematical audit has not been performed.

## References
1. I. Dolgachev and M. Kapranov, *Schur quadrics, cubic surfaces and rank 2 vector bundles over the projective plane*, arXiv:alg-geom/9304005v1, first public 13 April 1993, §0; https://arxiv.org/abs/alg-geom/9304005.
2. B. van Geemen, *A linear system on Naruki's moduli space of marked cubic surfaces*, arXiv:math/0101161v1, first public 19 January 2001, §1.8; https://arxiv.org/abs/math/0101161.
3. V. Alexeev, R. Donagi, G. Farkas, E. Izadi and A. Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, arXiv:1507.05710v1, first public 21 July 2015, §2; https://arxiv.org/abs/1507.05710.
4. M. Arap and R. Varley, *On algebraic equivalences among the 27 Abel-Prym curves on a generic abelian 5-fold*, arXiv:1206.6517v1, first public 27 June 2012, §2; https://arxiv.org/abs/1206.6517.
5. Previously published integral calculations: *The order-four integral reconstruction obstruction for Schläfli double-sixes* and *Integral tritangent presentation of the \(E_6\) weight lattice* (2026); distinct separate line-incidence maps.
