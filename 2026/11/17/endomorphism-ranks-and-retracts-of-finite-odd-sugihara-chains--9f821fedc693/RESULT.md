# Endomorphism ranks and retracts of finite odd Sugihara chains

## Claim and domain

Let \(S_{2m+1}\), for an integer \(m\ge1\), denote the standard odd Sugihara chain with universe \(\{-m,\ldots,0,\ldots,m\}\), lattice order the integer order, involution \(\neg x=-x\), fusion
\[
 x\cdot y=\begin{cases}x,&|x|>|y|,\\ y,&|y|>|x|,\\ \min(x,y),&|x|=|y|,\end{cases}
\]
and implication \(x\to y=\max(-x,y)\) when \(x\le y\), and \(x\to y=\min(-x,y)\) otherwise; the monoid identity is \(0\). Homomorphisms preserve all these operations.

**Theorem (rank and retract classification).** The endomorphisms of \(S_{2m+1}\) are in bijection with subsets \(A=\{j_1<\cdots<j_r\}\) of \(\{1,\ldots,m\}\), with \(r\) allowed to be zero. Writing \(h_A\) for the corresponding endomorphism, its values on the positive indices are
\[
 h_A(1)=\cdots=h_A(m-r)=0,\qquad
 h_A(m-r+s)=j_s\quad (1\le s\le r),
\]
with \(h_A(0)=0\) and \(h_A(-i)=-h_A(i)\). Its image is \(\{0\}\cup\{\pm j:j\in A\}\). Consequently, the image-cardinality enumerator is
\[
\boxed{\sum_{h\in\mathrm{End}(S_{2m+1})}z^{|\mathrm{im}\,h|}=z(1+z^2)^m.}
\]
All \(2^m\) symmetric subchains \(\{0\}\cup\{\pm j:j\in A\}\) are subalgebras and images of exactly one endomorphism.

Exactly \(m+1\) endomorphisms are idempotent. They correspond precisely to the terminal subsets \(A_r=\{m-r+1,\ldots,m\}\), for \(0\le r\le m\). Thus the **retract subalgebras** of \(S_{2m+1}\) are exactly
\[
\boxed{R_r=\{0\}\cup\{\pm(m-r+1),\ldots,\pm m\},\quad0\le r\le m,}
\]
one of each odd cardinality \(2r+1\). In particular, a symmetric subalgebra need not be a retract.

## Proof

First, a homomorphism \(h:S_{2m+1}\to S_{2n+1}\) necessarily fixes \(0\), is monotone, and commutes with negation. Therefore the images \(c_i=h(i)\) of the positive indices satisfy \(0\le c_1\le\cdots\le c_m\le n\). If \(i<j\) and \(c_i=c_j=c>0\), then \(j\to i=-j\), whereas \(c\to c=c\). Preservation of implication would say \(-c=c\), a contradiction. Thus every repetition in the sequence \((c_i)\) occurs at zero, and the positive tail is strictly increasing. In particular, for selfmaps the positive images determine a unique subset \(A\) and the displayed formula.

Conversely any such subset map preserves order, lattice operations, identity, and negation. Fusion chooses the input with larger absolute value, choosing the negative input at equal nonzero absolute value; a strictly increasing positive tail preserves comparisons, and pairs collapsed to zero have zero output on both sides. For implication, when the source inputs are ordered and their images differ, the same branch of the displayed implication formula applies in source and target; when different indices have equal image they both lie in the collapsed central block, so both sides evaluate to zero. The equal-input case is also preserved. Hence all listed maps are homomorphisms.

An endomorphism of rank \(2r+1\) corresponds to an \(r\)-subset of the \(m\) positive target positions, hence contributes \(\binom mr z^{2r+1}\) to the rank polynomial. The algebra operations on any symmetric subset select one of the arguments or the negation of one, so symmetric subsets are subalgebras. The normal form shows exactly one endomorphism has each such subset as its image.

Finally, \(h^2=h\) holds exactly when every element of \(\mathrm{im}\,h\) is fixed. The nonzero domain positions are the terminal \(r\) positions \(m-r+1,\ldots,m\), so an idempotent must have its \(r\) positive image points among those positions; necessarily its image subset is the entire terminal interval. Every terminal-interval map fixes its image, so precisely these \(m+1\) maps are idempotent. The image of an idempotent endomorphism is a retract, and any retraction is idempotent, proving the classification.

## Previously known hom-set enumeration

Aguzzoli and Mordonini [1, Theorem 5 and Proposition 2] already supply a recurrence computing the **number of homomorphisms between any two finite odd Sugihara monoids**, using the duality with finite rooted trees. Accordingly, neither the general availability of a hom-set count nor that broader recurrence is claimed as new here. As an elementary specialization of the normal form above for \(h:S_{2m+1}\to S_{2n+1}\), one obtains
\[
|\mathrm{Hom}(S_{2m+1},S_{2n+1})|=\sum_{r=0}^{\min(m,n)}\binom nr.
\]
Embeddings number \(\binom nm\) if \(m\le n\), and surjections number one if \(m\ge n\). These contextual counts are consequences of the same direct proof but are **not** offered as an original general hom-set counting method.

## Verification and limits

An independently implemented exhaustive checker enumerated all \(11{,}080\) identity- and involution-preserving maps for \(1\le m,n\le4\), compared actual homomorphisms with the normal form, and verified endomorphism/rank/idempotent assertions for \(m\le10\). These are finite corroborations; the unrestricted theorem follows from the algebraic proof, not from enumeration. The results concern only standard finite odd Sugihara chains, not arbitrary odd Sugihara monoids, other chains, or monoid generators.

The remaining claim is the explicit morphism normal form together with the **rank-resolved endomorphism census, unique-image realization and complete retract classification**. The possibility of an earlier implicit or unindexed derivation from finite-tree duality remains a priority qualification.

## References

1. S. Aguzzoli and M. Mordonini, *Counting Homomorphisms Between Finite Gödel Algebras*, proceedings of IPMU 2024, Springer LNNS, 2025, pp. 365–377, DOI:10.1007/978-3-031-74000-8_30. Author preprint: https://ipmu2024.inesc-id.pt/files/paper_1057.pdf. See Theorem 5 and Proposition 2 (finite odd Sugihara monoids).
2. N. Galatos and J. G. Raftery, *A Category Equivalence for Odd Sugihara Monoids and Its Applications*, Journal of Pure and Applied Algebra 216 (2012), 2177–2192, DOI:10.1016/j.jpaa.2012.02.006.
3. A. Craig and C. Robinson, *Representing Sugihara Monoids via Weakening Relations*, arXiv:2310.12935, DOI:10.46298/fi.12451. Standard finite-chain operations.
