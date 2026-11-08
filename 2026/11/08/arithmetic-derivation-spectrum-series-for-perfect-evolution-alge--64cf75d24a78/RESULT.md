# Arithmetic derivation-spectrum series for perfect evolution algebras over finite fields

## Finding

Let \(q=p^e\) be a prime power and let \(n\geq0\). In a specified ordered natural basis \(e_1,\ldots,e_n\), every invertible matrix \(M=(M_{ij})\in\mathrm{GL}_n(\mathbb F_q)\) defines a perfect evolution algebra by \(e_i e_j=0\) for \(i\neq j\), and \(e_i^2=\sum_j M_{ij}e_j\). Define the **labeled derivation-dimension count**
\[
H_{n,k}(q)=\#\{M\in\mathrm{GL}_n(\mathbb F_q):\dim_{\mathbb F_q}\operatorname{Der}(E_M)=k\}.
\]
Set \(g_0(q)=1\), and for \(n\geq1\) set
\[
g_n(q)=|\mathrm{GL}_n(\mathbb F_q)|=\prod_{j=0}^{n-1}(q^n-q^j).
\]
If \(p=2\), then \(H_{n,0}(q)=g_n(q)\) and \(H_{n,k}(q)=0\) for \(k>0\). If \(p\) is odd, let \(h=\operatorname{ord}_{\mathbb F_p^{\times}}(2)\), a positive integer at least two. Then
\[
\boxed{\displaystyle
\sum_{n,k\geq0} H_{n,k}(q)u^k\frac{z^n}{n!}
=F_q(z)\,G_{q,h}(z)^{(u-1)/h}}
\]
where
\[
F_q(z)=\sum_{n\geq0}g_n(q)\frac{z^n}{n!},\qquad
G_{q,h}(z)=\sum_{m\geq0}\frac{g_m(q)^h}{(m!)^h}z^{hm}.
\]
Both series have constant coefficient one, and the rational exponent is interpreted formally by \(\exp((u-1)\log G_{q,h}(z)/h)\) in \(\mathbb Q[u][[z]]\). This is an *exact* formula for all coefficients and every finite field, not an asymptotic assertion.

In odd characteristic the realized derivation dimensions are exactly \(0,1,\ldots,\lfloor n/h\rfloor\). For \(n<h\) every derivation vanishes. If \(h\leq n<2h\), the nonzero-derivation matrices have precisely one derivation dimension and number
\[
\boxed{\displaystyle H_{n,1}(q)=\binom nh(h-1)!(q-1)^h g_{n-h}(q)};
\]
all remaining matrices have zero derivations. At the first possible size \(n=h\), this count becomes \((h-1)!(q-1)^h\).

For instance, over \(\mathbb F_3\), \(h=2\). Counts by derivation dimensions \(0,1,2\) for \(n=4\) are respectively \(24\,253\,200\), \(7\,872\), and \(48\); their sum is \(|\mathrm{GL}_4(\mathbb F_3)|=24\,261\,120\). For \(n=2\) the counts are \(44,4\), and for \(n=3\) they are \(11\,208,24\). For \(\mathbb F_5\), \(h=4\), and exactly \(1\,536\) invertible four-by-four matrices have nonzero derivations. For \(\mathbb F_7\), \(h=3\), and the analogous three-by-three count is \(432\).

## Assumptions and scope

All matrices are counted **relative to a fixed labeled ordered natural basis**. No quotient by algebra isomorphisms is taken. The graph of \(M\) has vertices \(1,\ldots,n\) and a directed edge \(i\to j\) exactly when \(M_{ij}\ne0\). Its connected components mean connected components after forgetting edge directions (loops do not join distinct vertices). The empty-algebra convention at \(n=0\) is used only to express the series compactly.

The base field is any finite field, with no assumption that \(q\) is prime. In particular, the order \(h\) is calculated in the prime subfield \(\mathbb F_p\), rather than from an arbitrary generator of \(\mathbb F_q^\times\).

## Proof

**1. Reduction to a weighted support condition.** Suppose \(D\) is a derivation. The \(n\) vectors \(e_i^2\) are linearly independent because \(M\) is invertible. For distinct \(i,j\), the equality \(0=D(e_i e_j)=D(e_i)e_j+e_iD(e_j)\) forces both off-diagonal coefficients \(D(e_i)_j\) and \(D(e_j)_i\) to vanish. Thus \(D(e_i)=d_i e_i\). Applying the derivation identity to \(e_i^2\) gives, for every \(i,j\),
\[
M_{ij}(d_j-2d_i)=0. \tag{1}
\]
Conversely every diagonal map satisfying (1) is a derivation. If \(p=2\), (1) forces \(d_j=0\) whenever some entry of column \(j\) is nonzero, hence all \(d_j=0\). Now suppose \(p\) is odd.

On each undirected connected support component, (1) forces either every \(d_i\) to be zero or every \(d_i\) to be nonzero. Once one \(d_i\) is specified, all other values are uniquely determined along paths because \(2\) is invertible. Consequently each connected component contributes either dimension zero or one to the total derivation space.

**2. Balanced cyclic colorings.** Consider a connected component with a nonzero derivation. Fix a vertex with value \(c\ne0\). Every other value is \(c2^a\) for a unique exponent residue \(a\in\mathbb Z/h\mathbb Z\), and (1) says that edges move from color \(a\) to color \(a+1\). Because \(M\) restricts to an invertible square block on each connected component, the numbers of vertices of the \(h\) colors must be equal. Indeed, its restriction maps the coordinate space of each color to that of the next color, so bijectivity forces equal dimensions and invertible inter-color blocks. All colors therefore appear, each with a common size \(m\geq1\), and the component has size \(hm\). Conversely a connected invertible matrix supported on a cyclic succession of \(h\) equally sized color classes has a nonzero diagonal derivation, obtained by assigning the value \(2^a\) to color \(a\). It has exactly one derivation dimension by step 1. For a connected matrix, its admissible ordered cyclic coloring is unique up to the \(h\) cyclic rotations: the color of one vertex fixes every other color along support paths.

**3. Connected cyclic-block enumeration.** For \(h\) fixed labeled color classes of size \(m\), a supported matrix has one independent \(m\)-by-\(m\) block from color \(a\) to color \(a+1\). It is invertible if and only if all \(h\) blocks are invertible. Hence the total number of block tuples is \(g_m(q)^h\). Let \(c_m(q,h)\) count such tuples whose undirected support graph is connected. Every disconnected tuple decomposes uniquely into connected components, each with the same number of vertices in each color (by invertibility of the component blocks). The ordinary labeled-component formula, applied simultaneously in all \(h\) color classes, gives
\[
\sum_{m\geq0}\frac{g_m(q)^h}{(m!)^h}t^m
=\exp\left(\sum_{m\geq1}\frac{c_m(q,h)}{(m!)^h}t^m\right). \tag{2}
\]
Thus \(c_m(q,h)\) is a well-defined nonnegative integer count, with \(c_1(q,h)=(q-1)^h\). Labeling the \(hm\) vertices, partitioning them into \(h\) ordered color classes of size \(m\), and dividing by the exactly \(h\) cyclic color rotations shows that the number of connected, invertible, eligible matrices on \(hm\) labeled vertices is
\[
b_{hm}(q,h)=\frac{(hm)!}{h(m!)^h}c_m(q,h). \tag{3}
\]
No eligible connected components have other sizes.

**4. All invertible matrices and dimension weighting.** Every invertible matrix decomposes uniquely into diagonal blocks indexed by connected components of its undirected support graph. For each such block the derivation-space dimension is zero or one, and dimensions add. Let \(a_s(q)\) denote the count of *all* connected invertible matrices on \(s\) labeled vertices. The exponential formula gives
\[
F_q(z)=\exp\left(\sum_{s\geq1}a_s(q)\frac{z^s}{s!}\right). \tag{4}
\]
To mark a block that contributes one derivation dimension by \(u\), replace its component weight one by \(u\). Equations (3) and (4) yield
\[
\sum_{n,k\geq0}H_{n,k}(q)u^k\frac{z^n}{n!}
=F_q(z)\exp\left((u-1)\sum_{m\geq1}\frac{c_m(q,h)}{h(m!)^h}z^{hm}\right).
\]
Substituting (2) with \(t=z^h\) proves the boxed generating identity.

**5. Boundaries and sharpness.** Since each positive derivation dimension requires an eligible connected component of at least \(h\) vertices, necessarily \(k\leq\lfloor n/h\rfloor\). Conversely, for any \(k\) in this range, take the direct sum of \(k\) weighted permutation matrices corresponding to directed \(h\)-cycles and an identity matrix of size \(n-kh\). Each cycle contributes one derivation dimension and each singleton loop contributes zero, realizing \(k\). When \(n<2h\), at most one cycle-type component occurs, and it must have size exactly \(h\), so (3) with \(m=1\) and an arbitrary invertible complementary block gives the displayed first-window count. In this range the complementary block has size less than \(h\) and hence has no nonzero derivations. This completes the proof.

## Verification

The standalone program `verify.py` constructs derivation equations directly from the Leibniz identity and exhaustively enumerates matrices over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\) in the small dimensions printed by the program. In particular all \(3^9\) matrices of size three over \(\mathbb F_3\) are processed, including all \(11\,232\) invertible matrices. It independently enumerates all \(48^2\) pairs of invertible two-by-two blocks over \(\mathbb F_3\), finding \(2\,272\) connected cyclic tuples and establishing the predicted four-dimensional positive-derivation counts \(7\,872\) and \(48\) via component decompositions.

The independent extension-field program `verify_extension.py` constructs \(\mathbb F_9\) as a quadratic extension of \(\mathbb F_3\), directly solves the derivation linear equations for every two-by-two invertible matrix, and obtains counts \(5\,696\) and \(64\). The exact-series program `verify_series.py` computes formal coefficients using rational arithmetic, verifies nonnegativity, integrality and normalization for several dimensions, and reproduces the tables in the finding. These are finite confirmations; the proof above handles unbounded dimensions and arbitrary prime powers.

Run the programs with Python 3; `verify.py` and `verify_extension.py` use the standard library, while `verify_series.py` additionally uses SymPy. Their expected completion markers are `VERIFY_OK`, `VERIFY_EXTENSION_OK`, and `VERIFY_SERIES_OK`.

## Relationship to prior work

Elduque and Labra (2019 preprint, subsequently published in 2021), especially Theorem 4.1 and Corollary 4.3, already characterize the derivation algebra of *each fixed* perfect evolution algebra using the balance of connected components of its support graph. The diagonal criterion in proof step 1 and its interpretation in terms of components are prior structural mathematics, not claimed new here. The present enumeration counts *all labeled invertible structure matrices* simultaneously, by derivation dimension, and removes the need to sum separately over support graphs. Its cyclic-block factor with powers of \(g_m(q)\) is the additional arithmetic counting step.

Bekbaev's 2024 preprint proves generic triviality of derivations among all finite-dimensional algebras in a geometric setting and gives low-dimensional isomorphism classifications. It does not present this finite-field labeled evolution-algebra series. The 2026 survey of Kaygorodov, Martín González, and Viruel discusses derivations of evolution algebras and averages of idempotents over finite fields but does not provide the present derivation-dimension census. Wei and Zou's 2023 work counts isomorphism classes of perfect evolution algebras, a different orbit-counting target. A previous labeled centroid-component enumeration determines support connectivity but not the new characteristic-dependent eligible-component weights.

## Limitations

This is a count of *labeled structure matrices*, not of algebra isomorphism classes. The result does not classify the individual derivation Lie algebras beyond their dimensions (though the cited graph theorem makes them abelian in odd characteristic). The formula is an exact formal-series coefficient formula, not a single elementary closed product for every coefficient. Scientific priority is provisional: another counting formula for cyclically colored invertible support matrices, perhaps under different terminology, might imply the same distribution. The computational checks cover only explicitly stated small fields and dimensions; no unbounded computation is claimed.

## References

1. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191, first posted February 6, 2019; later *Linear and Multilinear Algebra* 69 (2021), 331–342. https://arxiv.org/abs/1902.02191
2. U. Bekbaev, *On finite dimensional algebras with trivial derivation (automorphism)*, arXiv:2403.15104, first posted March 22, 2024. https://arxiv.org/abs/2403.15104
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first posted October 18, 2023. https://arxiv.org/abs/2310.12368
4. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first posted October 15, 2026. https://arxiv.org/abs/2610.22248
