# Signed-cut enumeration of commuting tuples and centralizers in Coxeter type-B face monoids

## Finding

Let \(\mathcal F_n^B\) denote the Tits face monoid of the real type-\(B_n\) reflection arrangement \(x_i=0\) and \(x_i=\pm x_j\), for every integer \(n\ge0\). Let \(T_{n,t}\), for each integer \(t\ge1\), count ordered \(t\)-tuples of **pairwise commuting** faces, with repetitions allowed. Then
\[
T_{n,t}=\sum_{z=0}^{n}\binom nz 2^{n-z}\sum_{r=0}^{n-z}r!\left\{\begin{matrix}n-z\\r\end{matrix}\right\}(2^t-1)^r,
\qquad
\sum_{n\ge0}T_{n,t}\frac{u^n}{n!}=\frac{e^u}{2^t-(2^t-1)e^{2u}}.
\]
Here braces are Stirling numbers of the second kind, with \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1\). For fixed \(t\), set \(\rho_t=\tfrac12\log(1+1/(2^t-1))\). Then
\[
T_{n,t}\sim\frac{e^{\rho_t}}{2^{t+1}\rho_t^{n+1}}\,n!\quad(n\to\infty).
\]

A face \(\alpha\) has a uniquely determined central zero block of size \(z\), and \(r\) ordered positive-magnitude signed blocks, of cardinalities \(b_1,\ldots,b_r\) (so \(z+\sum_i b_i=n\)). Its **complete element centralizer** has cardinality
\[
|C_{\mathcal F_n^B}(\alpha)|=2^r F^B_z\prod_{i=1}^r F_{b_i},\quad
F_m=\sum_{k=0}^m k!\left\{\begin{matrix}m\\k\end{matrix}\right\},\quad
F^B_m=\sum_{j=0}^m\binom mj2^{m-j}F_{m-j}.
\]
Thus the centralizer-size multiset is explicit by grouping the faces over all \(z,r\) and ordered block sizes, weighted by the corresponding multinomial and sign counts.

The maximal cliques of the full commuting graph (one vertex per face, including the identity) are exactly the face intervals below individual chambers: there are \(2^n n!\) of them, each of cardinality \(2^n\). Write chambers as signed permutations \(\sigma=(\sigma_1,\dots,\sigma_n)\) with entries arranged by *increasing* coordinate magnitude. Then their clique intersection has size
\[
|\mathcal C_\sigma\cap\mathcal C_\tau|=2^{d(\sigma,\tau)},\quad
d(\sigma,\tau)=\#\{j:0\le j<n,\ \{\sigma_{j+1},\ldots,\sigma_n\}=\{\tau_{j+1},\ldots,\tau_n\}\}.
\]
In particular, the shared signed-suffix cuts, rather than ordinary permutation cuts, determine every pairwise maximal-clique overlap.

## Assumptions and scope

The arrangement lives in \(\mathbb R^n\). Every relatively open face has one central block \(Z\), consisting of coordinates zero on that face, and an ordered list \(B_1,\ldots,B_r\) of nonempty signed blocks with strictly increasing positive absolute coordinate values. Within each signed block, each indexed coordinate is assigned its own sign. The unsigned sets \(Z, |B_1|,\ldots,|B_r|\) form a partition of \([n]\). A face is uniquely identified by its sign vector on the arrangement hyperplanes. In the Tits multiplication, a nonzero sign in the left factor is retained and a zero is replaced by the sign in the right factor. Two elements commute exactly when they have no hyperplane coordinate with opposite nonzero signs. This includes \(n=0\), when the monoid consists only of its identity.

A face \(\beta\) lies *below* \(\gamma\) when \(\beta\) is in the closure of \(\gamma\). For a face \(\gamma\) with \(r\) noncentral signed blocks, the faces below it are uniquely obtained by retaining or deleting any of the \(r\) boundaries: the first separates the zero block from the first signed block, and the remaining ones separate consecutive signed blocks. If the first boundary is deleted, the signed entries in the initial block become zero. Hence that interval contains exactly \(2^r\) faces. A chamber is a face with no central block and all \(n\) signed blocks singletons.

## Proof

**1. Commutation and joins.** On each defining hyperplane \(H\), the product sign is \(\epsilon_H(\alpha)\) unless this is zero, in which case it is \(\epsilon_H(\beta)\). Thus the products in both orders agree if and only if there is no \(H\) carrying opposite nonzero signs. For a pairwise-commuting tuple, successive products are independent of their ordering; the resulting sign vector specifies a face \(\gamma\) whose closure contains every tuple entry. This face is the unique smallest common containing face. Conversely, two faces contained in the closure of any one face have no opposite nonzero signs, and therefore commute. As a result, tuples can be enumerated by their unique common product \(\gamma\).

**2. Signed cuts and the exact tuple count.** Suppose \(\gamma\) has \(r\) noncentral blocks. Each tuple entry is a coarsening of \(\gamma\), obtained by selecting a subset of the \(r\) boundaries that survive. Its common product is \(\gamma\) if and only if every boundary survives in at least one tuple entry. For each of the \(r\) boundaries choose its nonempty set of surviving tuple positions in \(2^t-1\) ways, independently. Hence precisely \((2^t-1)^r\) tuples have common product \(\gamma\). Given \(z\) zero coordinates, there are \(\binom nz\) choices of the zero block, \(2^{n-z}\) choices of signs, and \(r!\left\{\begin{smallmatrix}n-z\\r\end{smallmatrix}\right\}\) ordered partitions into noncentral blocks. Summing over \(z,r\) proves the first display. Applying the ordered-partition exponential formula \(\sum_{m\ge0}\sum_{r\ge0}r!S(m,r)v^r(2u)^m/m!=(1-v(e^{2u}-1))^{-1}\), and inserting the free central-block factor \(e^u\), gives the generating function with \(v=2^t-1\).

**3. Centralizers.** Classify the commuting faces \(\beta\) by the common product \(\gamma=\alpha\beta\). For any fixed refinement \(\gamma\) of \(\alpha\), the cut set of \(\alpha\) inside the interval below \(\gamma\) has size \(r\). A face \(\beta\) below \(\gamma\) has common product \(\gamma\) with \(\alpha\) exactly when it retains every cut of \(\gamma\) that \(\alpha\) does not retain. The other \(r\) cuts are independently optional. This gives \(2^r\) faces over each such \(\gamma\), including coarsenings that merge across several consecutive cuts. The product uniquely recovers \(\gamma\), so these fibers are disjoint.

To count the refinements \(\gamma\), the boundaries retained by \(\alpha\) must separate the original blocks. The coordinates in \(Z\) can split into a central zero block followed by an arbitrary list of signed magnitude blocks, giving \(F_z^B\) choices. Each original noncentral block \(B_i\) can split into an arbitrary ordered partition of its coordinates, with the signs unchanged, giving \(F_{b_i}\) choices. These choices are independent: concatenate the initial signed refinement of \(Z\) and then the ordered refinements of the \(B_i\). Hence the number of refinements is \(F_z^B\prod_i F_{b_i}\), and multiplying by the fiber size proves the centralizer formula. The formula for \(F_z^B\) follows by choosing the internal zero subset, the signs, and an ordered partition of its complement.

**4. Maximal cliques and overlaps.** Every commuting family has a common product face, which is contained in the closure of a chamber refining it. Therefore every clique lies in some chamber interval. Such an interval has \(2^n\) mutually commuting faces, and contains its unique chamber, so it is maximal; different chambers define different maximal cliques. There are \(2^n n!\) signed-permutation chambers. A coarsening of \(\sigma\) is determined by a subset of its \(n\) cuts, including the zero-to-first boundary. For the same coarsened face to lie below \(\tau\), every kept cut must yield exactly the same **signed suffix set** in both chambers. Conversely any chosen collection of common signed-suffix cuts determines one face below both chambers. The cardinality of the intersection is therefore \(2^d\), proving the final assertion.

**5. Asymptotics.** For fixed \(t\ge1\), the generating function has simple poles at \(\rho_t+\pi i k\), \(k\in\mathbb Z\), with \(\rho_t>0\) the unique one of smallest modulus. Its principal part at \(\rho_t\) is \(e^{\rho_t}/[2^{t+1}(\rho_t-u)]\); all other poles have larger modulus. Coefficient extraction proves the stated asymptotic.

## Verification

The standalone `verify_type_b_faces.py` enumerates every signed face for dimensions \(0\) through \(4\), then constructs each sign vector independently from actual coordinate representatives. It checks the centralizer formula for **every** face in dimensions \(1\) through \(4\), and the full ordered commuting-pair counts \(1,7,97,2023,56257\) in dimensions \(0\) through \(4\). It independently enumerates ordered commuting triples for \(n=1,2,3\) and quadruples for \(n=1,2\); those counts match the formulas. Finally it checks all chamber intervals, commuting-pair compatibility, and every maximal-chamber-clique overlap for \(n=1,2,3\). The successful output ends with `VERIFY_OK`. The proof covers all dimensions and arities; finite computations serve as reproducible checks, not as an infinite proof.

## Relationship to prior work

The face sign-product construction and left-regular-band context are foundational (Saliola; Margolis–Saliola–Steinberg). The type-A braid-face result [3] gives the corresponding tuple, centralizer and clique-overlap formulas for ordinary ordered set partitions. The rank-three chamber-polygon census [4] already covers the tuple count in rank three. More generally, for a simplicial arrangement the common-product argument makes the tuple count a weighted face vector, with weight \((2^t-1)^r\) on dimension \(r\); the type-B tuple series here is its explicit specialization. The structural formulas of interest are the exact type-B element centralizers and the overlap test from signed suffix sets. The type-A numerical formulas do not count involution-fixed coarsenings or distinguish the signs on a suffix. The signed central-block factor is obtained here by counting refinements and the product fibers in the type-B chamber fan. This comparison does not rule out earlier equivalent Coxeter formulas.

## Limitations

Only the real Coxeter type-B face monoid is treated. The result concerns the full graph including the identity and allows repeated faces in tuples, not the graph obtained after deleting central elements. The centralizer formula determines numerical centralizer multiplicities implicitly by face parameters, but it does not give an expanded closed univariate degree polynomial. The low-dimensional enumeration does not prove the general formulas. The signed ordered Bell count is classical, and an earlier equivalent general formula for Coxeter face monoids may exist.

## References

1. F. V. Saliola, *The Face Semigroup Algebra of a Hyperplane Arrangement*, first posted 2005-11-29, https://arxiv.org/abs/math/0511717, especially the face-product definition and structural setup.
2. S. Margolis, F. V. Saliola and B. Steinberg, *Semigroups embeddable in hyperplane face monoids*, first posted 2012-12-30, https://arxiv.org/abs/1212.6683, especially the face-sign construction and semigroup embedding context.
3. *Complete commuting-clique geometry of the braid face monoid*, published research record (2026-10-26), https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-complete-commuting-clique-geometry-of-the-braid-face-monoid--493f7b5a1c64.
4. *Rank-three face-monoid commuting spectra are chamber-polygon spectra*, published research record (2026-11-02), https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-rank-three-face-monoid-commuting-spectra-are-chamber-polygon-spe--8c75760483b9.
