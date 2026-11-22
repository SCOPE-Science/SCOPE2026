# Passive-retract complexes recover cycle types of one-column quandles

## Finding
For every integer \(n\ge2\) and every nonidentity permutation \(\sigma\in S_n\), let \(Q_\sigma=\{0,1,\ldots,n\}\) have the quandle operation
\[
x\triangleright y=\begin{cases}\sigma(x)&y=0,\ x\ne0,\\x&\text{otherwise}.\end{cases}
\]
(The permutation acts only on \(\{1,\ldots,n\}\).) The element \(0\) is the unique element whose right translation is not the identity, so it is characterized intrinsically by the quandle.

Call an image **passive** if it is the image of a quandle retraction \(f:Q_\sigma\to Q_\sigma\), i.e. an endomorphism with \(f^2=f\), and does not contain \(0\). Write the cycle lengths of \(\sigma\), with repetitions, as \(d_1,\ldots,d_r\). Then:

1. A nonempty subset \(T\subseteq\{1,\ldots,n\}\) is a passive retraction image **if and only if** it intersects each cycle of \(\sigma\) in at most one point. Consequently, adjoining the empty face makes the passive-image collection the independence complex of the disjoint union of cliques of orders \(d_1,\ldots,d_r\). Its face-count polynomial is
\[
I_\sigma(z)=\sum_{T\,\mathrm{passive}}z^{|T|}=\prod_{i=1}^{r}(1+d_i z)-1.
\]
2. For **each specified** passive image \(T\) of cardinality \(s\), exactly \(s^{r-s+1}\) quandle retractions have image \(T\). Thus the corresponding rank-generating polynomial is
\[
E_\sigma(z)=\sum_{\substack{f^2=f\\0\notin f(Q_\sigma)}}z^{|f(Q_\sigma)|}
=\sum_{s=1}^{r}s^{r-s+1}e_s(d_1,\ldots,d_r)z^s,
\]
where \(e_s\) is the degree-\(s\) elementary symmetric polynomial.
3. Either \(I_\sigma(z)\) or \(E_\sigma(z)\), **by itself**, determines the multiset \(\{d_1,\ldots,d_r\}\) and hence the quandle isomorphism class. In particular, this passive-retract invariant distinguishes cycle types that the ordinary quandle polynomial cannot distinguish.

## Assumptions and scope
All sets and maps are finite, and the permutation is **nonidentity**, allowing any mix of fixed points and longer cycles. The distinguished element \(0\) is not an extra chosen parameter: it is the unique active right-translation column for nonidentity \(\sigma\). A retraction means a composition-idempotent quandle endomorphism, not a homotopy-theoretic retraction. Rank denotes the cardinality of the image. Only images excluding \(0\) are counted by these polynomials; no claim is made here about the rank spectrum of all endomorphisms or images containing \(0\).

## Proof
**Intrinsic distinguished point.** For a positive argument \(y\), the right translation \(x\mapsto x\triangleright y\) is the identity. At \(y=0\), it restricts to \(\sigma\) on the positive elements, and is nonidentity by assumption. Consequently \(0\) is unique and any quandle isomorphism preserves it and preserves the family of passive retraction images.

**Necessity of partial transversality.** Let \(f\) be a retraction with \(0\notin f(Q_\sigma)\), and put \(T=f(Q_\sigma)\). All values of \(f\) are positive, including \(f(0)\). For each positive \(x\), the homomorphism law with second input \(0\) gives
\[
f(\sigma(x))=f(x\triangleright0)=f(x)\triangleright f(0)=f(x).
\]
Therefore \(f\) is constant on every cycle of \(\sigma\). Idempotence entails that every element of \(T\) is fixed by \(f\). Two distinct selected elements of the same cycle would have the same image, but would both have to be fixed: a contradiction. Thus \(T\) meets each cycle at most once.

**Sufficiency and exact fibers.** Conversely fix a nonempty partial transversal \(T\) of size \(s\). For each cycle meeting \(T\), prescribe the constant value equal to its unique point in \(T\). For each of the other \(r-s\) cycles, choose freely one of the \(s\) points of \(T\) as its constant image. Independently choose \(f(0)\) to be any of the \(s\) points of \(T\). All outputs are positive and \(f\) is constant on cycles, so for a positive second input \(y\), both sides of the homomorphism identity equal \(f(x)\), while for \(y=0\) both sides equal \(f(x)\) because \(f(\sigma x)=f(x)\). For \(x=0\) and \(y=0\), the operation gives \(0\triangleright0=0\) and \(f(0)\triangleright f(0)=f(0)\), so this case holds as well. The map fixes every point of \(T\), hence is idempotent and has image exactly \(T\). All possibilities are distinct and exhaustive, giving \(s^{r-s}\cdot s=s^{r-s+1}\) retractions onto each specified \(T\).

**Counts and reconstruction.** Selecting \(s\) different cycles and then one point in each contributes \(\prod_{i\in J}d_i\) image sets, whence the number of passive image sets of size \(s\) is \(e_s(d_1,\ldots,d_r)\). This proves both generating polynomials. Their largest nonzero degree is \(r\). From \(E_\sigma\), the coefficient at degree \(s\), divided by the known positive integer \(s^{r-s+1}\), yields \(e_s\); from \(I_\sigma\), it is obtained directly. All elementary symmetric functions therefore become known, and
\[
\prod_{i=1}^{r}(t-d_i)=t^r-e_1t^{r-1}+e_2t^{r-2}-\cdots+(-1)^re_r
\]
has the positive integer cycle lengths, with their multiplicities, as roots. The known cycle-type classification of these quandles then proves the isomorphism conclusion. Conversely, isomorphic quandles have the same intrinsic passive-retraction data.

As an example, cycle types \((4,4)\) and \((2,6)\) both have eight positive elements and no fixed points; their ordinary quandle polynomials coincide, but their passive-retraction map polynomials are respectively \(8z+32z^2\) and \(8z+24z^2\).

## Verification
The standalone Python 3 program `verify_one_column.py` constructs the quandle operation directly for each nonidentity permutation cycle type on \(2\le n\le5\), enumerates all maps with values in the positive elements, checks the quandle homomorphism and composition-idempotence identities element by element, and compares the resulting image-rank multiplicities to the formula. It exhaustively checks 13 cycle profiles, including profiles with fixed points and repeated lengths. The observed terminal line was `ONE_COLUMN_RETRACTION_EXHAUSTIVE_PASSED 13`. The brute-force search does not use the classification as its search space, but finite checks do not replace the general proof.

## Relationship to prior work
Cazet (2023), *Quandles with one non-trivial column* [1], introduces exactly this family. Its Theorem 3.3 already classifies quandle isomorphism by permutation conjugacy and Theorem 3.5 computes the ordinary quandle polynomial, which depends only on size and the number of fixed points. Theorem 3.8 describes Hom quandles for two full cycles. The present assertion is **not** a new isomorphism classification; it gives a different, complete **retraction-image invariant**, including all passive images and map multiplicities for arbitrary permutation cycle profiles. The detailed material inspected in sections 3.1–3.8 of [1] does not give these formulas.

The known rank enumeration for idempotents of the full transformation centralizer of a permutation [2] concerns equivariant maps \(g\sigma=\sigma g\), retaining *whole* image cycles and involving cycle-length divisibility. The passive quandle homomorphism equation instead forces \(f\sigma=f\), so the selected images are *partial transversals*, and the centralizer formula does not imply the asserted passive-image polynomial. The semisimple Alexander-quandle retraction classification [3] treats a distinct affine family and does not specialize to this arbitrary one-column construction.

## Limitations
The theorem counts the structurally intrinsic passive-retract stratum only; the full retraction spectrum, with images containing the active point, is not claimed. The component-cycle argument is self-contained but does not establish absolute historical priority against every unindexed formulation. Computational verification covers finite examples only.

## References
1. N. Cazet, *Quandles with one non-trivial column*, arXiv:2303.15815v1, first posted 28 March 2023, https://arxiv.org/abs/2303.15815 (full version: https://arxiv.org/html/2303.15815v3).
2. *Rank enumeration and minimum retraction size in permutation-centralizer monoids*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-enumeration-and-minimum-retraction-size-in-permutation-cent--46b24971b86b .
3. *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-semisimple-alexander-quandle-retractions-a-transformation-affine--117335b68a3e .
