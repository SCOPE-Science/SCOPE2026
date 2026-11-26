# The first path-homomorphism-indistinguishable trees and a twelve-vertex spectral coincidence

## Finding
For a finite undirected simple tree \(T\), let \(P_{k+1}\) denote the path with \(k\) edges, and define its path-homomorphism profile by
\[
W_k(T)=|\operatorname{Hom}(P_{k+1},T)|=\mathbf{1}^{\mathsf T}A_T^k\mathbf{1},\qquad k\ge0.
\]
Here homomorphisms need not be injective. The following finite-model-theoretic separation threshold is exact.

**Theorem.** Among all nonisomorphic finite unlabelled trees, the least order of a pair having equal \(W_k\) for *every* \(k\ge0\) is **12**. Every tree on at most 11 vertices is uniquely identified, among trees of its order, by its entire path-homomorphism profile. Among the 551 nonisomorphic twelve-vertex trees, there are precisely 550 distinct profiles: 549 singleton classes and one class consisting of two nonisomorphic trees. Moreover, for any two trees having at most twelve vertices, equality of their complete path-homomorphism profiles is equivalent to equality of their generalized adjacency spectra (the adjacency spectra of the trees and their complements).

This last equivalence is a small-order coincidence: path counts do not, as a general graph-theoretic principle, determine adjacency spectra.

## Assumptions and scope
Trees are finite, nonempty, connected, unlabelled, simple, undirected graphs. We compare graphs using all ordered homomorphisms from paths, including the one-vertex path; thus \(W_0(T)=|V(T)|\) and a cross-order collision cannot occur. Nonisomorphic refers to unrooted graph isomorphism. Generalized adjacency spectrum means the pair of eigenvalue multisets of a graph and its complement; equal characteristic polynomials are an equivalent formulation. The classification is complete only through order 12.

A specific nonisomorphic twelve-vertex pair, using vertices \(0,\ldots,11\), is given by the following edge sets (each unordered pair represents one edge):

```
A = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(4,7),(6,8),(7,9),(8,10),(8,11)]
B = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(6,7),(6,8),(7,9),(9,10),(10,11)]
```

Their center-rooted AHU canonical codes, respectively,

```
((((()())))(((()))())())
((((()())()))(((())))())
```

are unequal. This is an explicit finite nonisomorphism certificate.

## Proof
For every \(n\), exhaustive unlabelled-tree generation is proved complete inductively as follows. At order 1 there is one tree. Every tree of order \(n>1\) contains a leaf; deleting it produces a tree of order \(n-1\). Conversely, reattaching a new leaf to every vertex of every \((n-1)\)-vertex tree therefore generates every \(n\)-vertex tree, up to isomorphism. Discard repeated isomorphism classes by the canonical AHU center-rooting code: repeatedly delete all current leaves until one center or two centers remain, encode a rooted tree recursively as sorted child codes in parentheses, and choose the lexicographically least code among centers. This is a complete unrooted-tree isomorphism invariant. The standalone enumerator and verifier reproduce the following exact exhaustive table.

| Order | Trees | Path-profile classes | Nontrivial classes |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 0 |
| 2 | 1 | 1 | 0 |
| 3 | 1 | 1 | 0 |
| 4 | 2 | 2 | 0 |
| 5 | 3 | 3 | 0 |
| 6 | 6 | 6 | 0 |
| 7 | 11 | 11 | 0 |
| 8 | 23 | 23 | 0 |
| 9 | 47 | 47 | 0 |
| 10 | 106 | 106 | 0 |
| 11 | 235 | 235 | 0 |
| 12 | 551 | 550 | 1 (two trees) |

For each tree of order \(n\), the verifier computes \(W_0,\ldots,W_{2n}\) by repeated integer adjacency-matrix/vector multiplication, without numerical approximation. These finite prefixes decide equality of *infinite* profiles: if two trees of order \(n\) have adjacency matrices \(A\) and \(B\), their difference sequence is
\[
\mathbf{u}^{\mathsf T}\begin{pmatrix}A&0\\0&B\end{pmatrix}^{k}\mathbf{v},
\quad\mathbf{u}=(\mathbf{1},-\mathbf{1}),\quad\mathbf{v}=(\mathbf{1},\mathbf{1}).
\]
By Cayley–Hamilton this sequence satisfies a homogeneous recurrence of order at most \(2n\). Equality through \(k=2n-1\) therefore implies equality for every \(k\ge0\). Conversely, differing prefixes distinguish the profiles. Exhaustive grouping by these decisive prefixes proves the first two assertions, including uniqueness of the nontrivial class at order 12.

There is also a compact algebraic certificate for the displayed pair. Exact matching enumeration gives both trees the matching numbers \((m_0,\ldots,m_6)=(1,11,42,66,39,6,0)\). The tree matching-polynomial identity therefore gives their common adjacency characteristic polynomial
\[
\chi(t)=t^{12}-11t^{10}+42t^8-66t^6+39t^4-6t^2.
\]
Direct integer walk enumeration gives the same first twelve values
\[
(W_0,\ldots,W_{11})=(12,22,48,98,212,444,958,2028,4372,9302,20046,42760).
\]
Cayley–Hamilton applied separately to their common degree-12 characteristic polynomial extends this equality to *all* lengths. Their shared rational generating function, given as a further check, is
\[
\sum_{k\ge0}W_kz^k=\frac{12+22z-84z^2-144z^3+188z^4+290z^5-150z^6-192z^7+38z^8+32z^9-2z^{10}}{1-11z^2+42z^4-66z^6+39z^8-6z^{10}}.
\]

Finally, the matrix-determinant lemma shows generally that a graph's generalized spectrum is equivalent to the pair consisting of its adjacency spectrum and its entire walk profile: for \(\overline A=J-I-A\),
\[
\det(tI-\overline A)=\det((t+1)I+A)\bigl(1-\mathbf1^{\mathsf T}((t+1)I+A)^{-1}\mathbf1\bigr).
\]
The resolvent term is the signed generating function of \(W_k\) around infinity. In our exhaustive census the only non-singleton path-profile class has *identical adjacency characteristic polynomial*, as explicitly checked above. Consequently, through order 12, equality of path profiles forces equality of adjacency spectra and hence of generalized spectra. The converse follows from the same determinant identity. This completes the classification.

## Verification
Run `python3 verification/verify_walktree_census.py` using Python 3 standard library. It verifies generator completeness and isomorphism-code uniqueness at each order, the exact profile-class counts, the unique edge-list witness, the witness's matching-polynomial coefficients and its first twelve walk counts. Its transcript `verification/replay.txt` ends with `PATH_COUNT_THRESHOLD_AND_UNIQUE_CLASS_PASS`.

As a separate computational cross-check, the output was compared with NetworkX's independent `nonisomorphic_trees` enumeration for each order 1 through 12. Both methods returned the same unlabelled-tree counts and the same profile-class counts at every order. The main verifier does *not* require NetworkX.

## Relationship to prior work
Dell, Grohe and Rattan (2018) characterize equality of counts of all path homomorphisms for arbitrary graphs using an unconstrained real matrix-intertwining condition. Their path-query result does not identify the first pair of distinct trees that satisfies the condition, nor classify all such pairs through order 12. Fuhlbrück, Köbler, Verbitsky and Zhukovskii (2024) study single-*root*-vertex walk sequences and ambivalent rooted trees; those objects are distinct from our *total*, unrooted path-homomorphism profile.

A public generalized-spectrum census, *First generalized-cospectral pair of trees: exhaustive DGS census of unlabelled trees with \(n\le12\)*, identifies the same twelve-vertex pair up to isomorphism as the first pair with *both* tree and complement spectra equal. Crucially, distinct generalized spectra do **not** by themselves imply distinct path profiles: generalized spectra contain additional spectral information. The new classification independently establishes that the weaker path-profile partition coincides with this stronger partition throughout the entire first-occurrence window; it is not a renaming of the preexisting stronger-invariant census.

## Limitations
The classification is computational-exact and finite; it does not assert that path profiles determine adjacency spectra for trees of any order greater than 12, or determine all graphs. The proof of the finite census depends on the correctness of the supplied tree generator and integer computations, supported by its inductive completeness proof, AHU isomorphism canonicalization, independent enumeration comparison and standard sequence-count anchors. Similar total-walk reconstruction literature may contain uninspected numerical classifications; historical priority requires further human review. No independent scientific audit is claimed.

## References
1. H. Dell, M. Grohe, G. Rattan, *Lovász Meets Weisfeiler and Leman*, arXiv:1802.08876v1, first posted 2018-02-24. Section 4 studies path-homomorphism count equivalence. https://arxiv.org/abs/1802.08876
2. F. Fuhlbrück, J. Köbler, O. Verbitsky, M. Zhukovskii, *Gathering Information about a Graph by Counting Walks from a Single Vertex*, arXiv:2409.03690v1, first posted 2024-09-05. https://arxiv.org/abs/2409.03690
3. *First generalized-cospectral pair of trees: exhaustive DGS census of unlabelled trees with n ≤ 12*, public mathematical record and proof package, 2026. https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE045
4. C. Zhu, *A Sharp Matching-Number Threshold for Spectral-Walk Determination of Trees*, arXiv:2608.21851, 2026, on the strictly stronger joint adjacency-spectrum/walk invariant. https://arxiv.org/abs/2608.21851
5. W. Lv, F. Liu, W. Wang, W. Wang, *Which graphs are determined by their total number of walks?*, Discrete Applied Mathematics 378 (2026), 337–347, DOI:10.1016/j.dam.2025.08.007 (full text unavailable at review).
6. OEIS A000055, numbers of unlabelled trees, used as an independent census-count anchor. https://oeis.org/A000055
