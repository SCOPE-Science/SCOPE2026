# The first image-rank gap for retractions of free left-regular bands

## Finding

**Theorem (first gap and complete three-generator census).** For \(n\in\{1,2,3\}\), let \(F_n\) be the unital free left-regular band on \(n\) letters, and count **unit-preserving monoid endomorphisms** \(\varphi:F_n\to F_n\) for which \(\varphi^2=\varphi\). Their image-cardinality generating polynomials \(R_n(T)=\sum_{\varphi^2=\varphi}T^{|\operatorname{im}\varphi|}\) are exactly

\[
R_1(T)=T+T^2,
\]
\[
R_2(T)=T+10T^2+3T^3+2T^4+T^5,
\]
\[
\begin{aligned}
R_3(T)={}&T+90T^2+126T^3+143T^4+69T^5+45T^6\\
&+12T^7+27T^8+6T^9+9T^{10}+6T^{12}+T^{16}.
\end{aligned}
\]

In particular, there are exactly **535** retractions of the sixteen-element monoid \(F_3\), and their image cardinalities are precisely \(1,2,3,4,5,6,7,8,9,10,12,16\). Thus \(n=3\) is the **first generator rank at which the image-cardinality spectrum of retractions fails to be an interval**. Ranks \(11,13,14,15\) are impossible, whereas every positive rank up through \(10\), as well as \(12\) and \(16\), occurs. The proper-image maximum is \(12\), attained six times.

## Assumptions and scope

Here \(F_n\) consists of the empty word and all repetition-free words over the alphabet \(\{0,\ldots,n-1\}\). Its multiplication concatenates two words and retains only the first occurrence of each letter. The empty word is the identity. A monoid homomorphism in this result is **unit preserving**. An image rank means the cardinality of the image submonoid, not the number of letters in any generator image or a matrix rank. The finite cutoff \(n\in\{1,2,3\}\) is part of the claim: no unproved general-rank formula is asserted.

## Proof

**Normal-form lemma.** Every monoid endomorphism \(\varphi:F_n\to F_n\) is uniquely specified by the tuple \((w_0,\ldots,w_{n-1})\) of images of the \(n\) free generators, and each \(w_i\) can be an arbitrary element of \(F_n\). Conversely any such tuple extends uniquely to a unital monoid endomorphism by the free left-regular band property. Write \(E_w(u)\) for evaluating the word \(u\) after substituting the generator-image tuple \(w\), reducing each concatenation by first-occurrence normalization. Then \(\varphi^2=\varphi\) **if and only if** \(E_w(w_i)=w_i\) for all \(i\): these equalities are exactly \(\varphi^2(i)=\varphi(i)\), and two monoid homomorphisms that agree on generators agree everywhere.

**Exhaustive finite certificate.** The file `verify.py` implements the preceding equivalence literally. For each \(n=1,2,3\), it generates exactly all \(\sum_{j=0}^n n!/(n-j)!\) distinct normal-form words and enumerates **every** ordered tuple in their \(n\)-fold Cartesian power: respectively \(2\), \(25\), and \(4096\) assignments, with no sampling or pruning. For each tuple it tests the complete generator idempotence condition. For each passing tuple it evaluates the morphism on **all** elements of \(F_n\), counts the distinct results and increments that image-cardinality coefficient. This algorithm is a finite exhaustive proof of the displayed coefficients because every possible morphism and every word in its image is covered and the acceptance test is equivalent to idempotence. The bundled source contains a second implementation computing the multiplication table by index, the full map on all words, and checking its composition square. Both implementations independently return exactly the stated coefficient dictionaries.

For reproducibility, run `python3 verify.py` with Python 3. Its final line is `FIRST_FREE_LRB_RETRACTION_RANK_GAP_CERTIFIED`. The source uses no third-party packages. These finite counts are exact for the stated \(n\); they neither assert nor suggest an exhaustive theorem for larger \(n\).

**First-gap conclusion.** The rank supports for \(n=1\) and \(n=2\) are respectively \(\{1,2\}\) and \(\{1,2,3,4,5\}\), both intervals. The \(n=3\) support contains \(10\) and \(12\) but not \(11\), and contains \(12\) and \(16\) but none of \(13,14,15\). This proves the asserted first-gap threshold.

## Verification

Two independently written exact finite enumerators (`direct` and `tabular`) in `verify.py` produced identical image-rank dictionaries at each of \(n=1,2,3\). Their retraction totals are \(2,17,535\). Both methods generate the free-band word normal forms explicitly and exhaust their generator assignments. The first calculates substitutions directly from words; the second first constructs the entire multiplication table and represents every morphism as an index map. The latter independently tests \(\varphi(\varphi(i))=\varphi(i)\) from the full index map. No floating-point arithmetic, randomness, partial search or external packages are involved.

## Relationship to prior work

Brauner, Commins and Reiner, *Invariant Theory for the Free left-regular band and a q-analogue* (arXiv:2206.11406), define precisely these injective-word monoids and study invariant subalgebras, symmetric-group representations and related shuffling operators. This supplies the free-band normal form but does not state the image-rank census of composition-idempotent endomorphisms. Shevlyakov, *Finite Submonoids of Free Left Regular Bands with Unit* (2021), examines embeddings and structural properties of submonoids, a related but different question; only its abstract and bibliographic record could be inspected, so full-text comparison is a priority limitation. A published result for **free left legal semigroups** concerns a different variety, where generator squares need not equal generators, and explicitly calculates a commuting graph and Laplacian spectrum rather than retraction image ranks.

## Limitations

This is a **finite cutoff theorem** for the first three generator counts only, not an all-dimensional formula and not a classification of isomorphism types of retracts. The computation uses exhaustive finite enumeration of \(16^3\) possible morphisms rather than a closed symbolic generating function. Publication priority is assessed only relative to examined literature and accessible search records; a relevant older study of submonoids was not available in full text. General endomorphisms not idempotent under composition, semigroup morphisms that need not preserve the identity, and ranks for \(n\ge4\) lie outside the statement.

## References

1. S. Brauner, P. Commins and V. Reiner, *Invariant Theory for the Free left-regular band and a q-analogue*, arXiv:2206.11406, first posted 22 June 2022, Sections 1 and 2.1. https://arxiv.org/abs/2206.11406
2. A. N. Shevlyakov, *Finite Submonoids of Free Left Regular Bands with Unit*, Algebra and Logic 59 (2021), 456–470, published 19 March 2021. https://doi.org/10.1007/s10469-021-09619-x
