# Steady-word compactness resolves the quaternary bifurcate-chain conjecture
## Finding
Fix a four-letter alphabet \(\mathcal A\). There exists a right-infinite word
\[
\mathbf x=x_1x_2x_3\cdots
\]
over \(\mathcal A\) such that every finite factor of \(\mathbf x\) is steady. Consequently every finite factor of \(\mathbf x\) is bifurcate.

In particular, if
\[
W_n=x_1x_2\cdots x_n,
\]
then every \(W_n\) is a quaternary bifurcate word and
\[
W_{n+1}=W_nx_{n+1}
\]
is a single-letter extension of \(W_n\). Hence Conjecture 2 of Dębski, Grytczuk, and Pawlik is true.

## Assumptions and scope
A finite word is square-free if it contains no nonempty factor of the form \(XX\). A square-free word is steady if deleting any one of its letters leaves a square-free word. A square-free word over a fixed alphabet is bifurcate if, at every insertion position, at least one letter of that alphabet can be inserted while preserving square-freeness.

The proof uses two results from Dębski, Grytczuk, and Pawlik. Their Theorem 1 states that arbitrarily long steady words exist over a four-letter alphabet. Their Theorem 3 states that over any fixed alphabet of at least three letters, every steady word is bifurcate.

The conclusion is stronger than the published chain conjecture because every finite factor of the resulting infinite word is steady, not merely its prefixes.

## Proof
We first record a hereditary property that is not stated as a separate lemma in the source.

**Lemma.** Every factor of a steady word is steady.

Let \(W\) be steady and let \(U\) be a factor of \(W\). Since \(W\) is square-free, \(U\) is square-free. Choose any occurrence of a letter of \(U\), and let the corresponding occurrence in \(W\) be deleted. The word obtained by deleting that letter from \(U\) is a factor of the corresponding one-letter deletion of \(W\). The latter word is square-free because \(W\) is steady, so the former is square-free as well. This holds for every letter of \(U\), proving that \(U\) is steady.

Now fix a four-letter alphabet \(\mathcal A\). Form a rooted tree \(T\) whose vertices at depth \(n\) are the steady words of length \(n\) over \(\mathcal A\), with an edge from \(u\) to \(ua\) whenever both words are steady. By the lemma, every prefix of a steady word is steady, so every vertex has its complete prefix chain back to the root.

The source's Theorem 1 gives steady words of arbitrarily large length over a four-letter alphabet. Relabeling letters if necessary, they may all be regarded as words over the fixed alphabet \(\mathcal A\). Therefore \(T\) has vertices at arbitrarily large depths. Each vertex has at most four children. By König's infinity lemma, \(T\) has an infinite ray
\[
x_1,\quad x_1x_2,\quad x_1x_2x_3,\quad\ldots.
\]
Thus every prefix \(W_n=x_1\cdots x_n\) of the resulting infinite word \(\mathbf x\) is steady.

Any finite factor \(F\) of \(\mathbf x\) is contained in some prefix \(W_N\). Applying the lemma once more shows that \(F\) is steady. Finally, the source's Theorem 3 implies that every such factor \(F\), and in particular every prefix \(W_n\), is bifurcate over \(\mathcal A\).

Since \(W_{n+1}\) is obtained from \(W_n\) by inserting one letter at the right end, the sequence \((W_n)_{n\ge1}\) is exactly the infinite chain required by Conjecture 2.

## Verification
The critical source statements were checked in the full public preprint, not from snippets: Theorem 1 gives arbitrarily long quaternary steady words; Theorem 3 gives the implication steady \(\Rightarrow\) bifurcate over every fixed alphabet of size at least three; and Conjecture 2 asks for an infinite chain of quaternary bifurcate words related by one-letter extensions.

The new ingredient is the factor-heredity lemma above. Its proof uses only the definitions: deleting a selected letter from a factor produces a factor of the word obtained by deleting the corresponding letter from the ambient word.

The remaining compactness step is König's infinity lemma applied to the finitely branching prefix tree of steady words. No finite experiment is used as evidence for the infinite conclusion.

## Relationship to prior work
Dębski, Grytczuk, and Pawlik introduced steady and bifurcate square-free words in this setting. Their Theorem 1 proves arbitrarily long steady words over four letters, while their Theorem 3 proves that every steady word over a fixed alphabet of at least three letters is bifurcate. In the same paper they nevertheless state as Conjecture 2 that an infinite chain of quaternary bifurcate words should exist.

The two published theorems do not by themselves explicitly state a nested chain. The missing link is that steadiness is inherited by factors, hence by prefixes. This makes the family of steady quaternary words a finitely branching prefix-closed tree with unbounded depth, and König's infinity lemma supplies a branch.

Targeted searches for the conjecture by name, for quaternary bifurcate chains, for infinite words all of whose factors are steady, and for compactness or prefix-tree formulations did not locate a published resolution. A current public problem index still lists the conjecture as open.

## Limitations
The argument resolves the infinite-chain conjecture but does not resolve the source's stronger Conjecture 3 about a complete bifurcate tree over five letters. A single infinite branch is much weaker than a complete tree in which every insertion position continues recursively.

The originality search cannot exclude an unindexed note or an unpublished observation of the same compactness argument. The mathematical conclusion depends on the source's Theorems 1 and 3; those were inspected in the full public preprint, while their proofs are not reproduced here.

## References
1. M. Dębski, J. Grytczuk, and B. Pawlik, “Extensions and reductions of square-free words,” arXiv:2209.08507, first public version 2022-09-18; Discrete Mathematics 347(3), 113825 (2024), DOI 10.1016/j.disc.2023.113825.
2. D. König, classical infinity lemma for finitely branching rooted trees.
