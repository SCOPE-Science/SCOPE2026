# The automorphism-group spectrum of five-dimensional perfect evolution algebras over \(\mathbb F_2\)

## Finding
Let \(K=\mathbb F_2\). For every five-dimensional evolution algebra \(E\) with \(E^2=E\), take isomorphisms and automorphisms as \(K\)-algebra maps. The exact number of isomorphism classes of such algebras is \(85{,}411\). More strongly, the complete number of isomorphism classes with each possible automorphism-group isomorphism type is:

| Automorphism group | Number of classes |
|:--|--:|
| trivial | 81,408 |
| \(C_2\) | 3,694 |
| \(C_3\) | 80 |
| \(C_4\) | 8 |
| \(C_2\times C_2\) | 113 |
| \(C_5\) | 3 |
| \(C_6\) | 8 |
| \(S_3\) | 73 |
| dihedral group of order \(8\) | 8 |
| dihedral group of order \(10\) | 1 |
| \(A_4\) | 0 |
| dihedral group of order \(12\) | 7 |
| Frobenius group of order \(20\) | 0 |
| \(S_4\) | 7 |
| \(A_5\) | 0 |
| \(S_5\) | 1 |

These are all subgroup isomorphism types of \(S_5\). In particular, \(A_4\), \(A_5\), and the order-\(20\) Frobenius subgroup do not occur as full automorphism groups in this family. The single class with full \(S_5\)-symmetry has structure matrix the identity. The values are counts of algebra isomorphism classes, not counts of labeled multiplication tables.

## Assumptions and scope
An evolution algebra has a natural basis \(e_1,\ldots,e_5\) such that \(e_i e_j=0\) whenever \(i\ne j\), and products \(e_i^2=\sum_j a_{ij}e_j\). It is *perfect* (also termed *idempotent* in the cited literature) when \(E^2=E\), equivalently \(A=(a_{ij})\in\operatorname{GL}_5(\mathbb F_2)\). This is **not** a classification of individual idempotent elements or of all evolution algebras of dimension five. The field is exactly \(\mathbb F_2\); no claim for larger fields is made. Each finite binary matrix defines a labeled multiplication table relative to a chosen natural basis.

## Proof
**Step 1: Reduce algebra isomorphisms to simultaneous row-column permutations.** The standard natural-basis rigidity theorem for perfect evolution algebras states that an isomorphism takes a natural basis to a monomial transformation of a natural basis (Wei--Zou, Theorem 1.1; earlier automorphism context in Sriwongsa--Zou). As \(\mathbb F_2^\times=\{1\}\), monomial transformations are exactly permutation matrices. Therefore two invertible structure matrices are isomorphic if and only if \(A'=P_\sigma^{-1}AP_\sigma\) for some \(\sigma\in S_5\), and \(\operatorname{Aut}(E_A)\cong\operatorname{Stab}_{S_5}(A)\). The latter is the automorphism group whose full isomorphism type is enumerated.

**Step 2: Enumerate all subgroups without relying on a subgroup catalogue.** Starting with the identity subgroup, adjoin each of the \(120\) permutations, take the closure under multiplication, and repeat for newly obtained subgroups. Represent a subgroup by a 120-bit membership mask. Exhaustion yields exactly \(156\) distinct subgroups of \(S_5\), including conjugates. The procedure discovers every subgroup: each finite subgroup has a generating set and is reachable by successive adjunctions. Classify subgroups by group order and the histogram of element orders; these signatures distinguish the \(16\) subgroup isomorphism types present in \(S_5\). The program `verify.py` gives the full literal lookup and checks every generated subgroup against it.

**Step 3: Count invariant invertible matrices exactly.** For each subgroup \(H\le S_5\), let \(F(H)\) be the number of matrices \(A\in\operatorname{GL}_5(\mathbb F_2)\) fixed under conjugation by every element of \(H\). The action of \(H\) on ordered index pairs \((i,j)\) partitions the 25 matrix-entry positions into orbital sets \(O_1,\ldots,O_d\). A binary matrix is fixed by \(H\) precisely when its entries are constant on each orbital. Thus there are exactly \(2^d\) candidates, constructed by assigning independent bits to the orbitals. Test each candidate's determinant by pivot elimination in \(\mathbb F_2\), counting those of rank five. Except for \(H=\{1\}\), where the standard product \(\prod_{j=0}^{4}(2^5-2^j)=9{,}999{,}360\) applies, this program enumerates every orbital-constant binary matrix. The largest such nontrivial enumeration has 17 free bits. Consequently every \(F(H)\) is an exact, finite, reproducible integer.

**Step 4: Invert the subgroup lattice.** Let \(E(H)\) count invertible binary matrices whose stabilizer is *exactly* \(H\) (as an embedded subgroup, not merely an isomorphic group). Then
\[
F(H)=\sum_{K\ge H}E(K),\qquad
E(H)=F(H)-\sum_{K>H}E(K).
\]
Process the 156 subgroups in descending order of cardinality. Every term on the right is already computed. Grouping the values of \(E(H)\) by the isomorphism type \(T\) of \(H\) gives the total number \(L(T)\) of labeled matrices whose stabilizer has type \(T\). Orbit-stabilizer then gives the sought number of algebra isomorphism classes,
\[
N(T)=\frac{|T|}{120}L(T).
\]
The exact calculations yield the 16-row table above, with nonnegative integers throughout. Their sum is \(85{,}411\). This is an exhaustive proof because all subgroups and all matrices fixed by each subgroup have been treated, and the stabilizer decomposition is a disjoint partition.

**Step 5: Independent total-orbit calculation.** Burnside's lemma gives \(N_{\rm total}=\frac1{120}\sum_{\sigma\in S_5}|C_{\operatorname{GL}_5(\mathbb F_2)}(P_\sigma)|\). For the seven cycle types, the number of permutations and invertible commuting matrices are:

| Cycle type | Multiplicity | Commuting invertible matrices |
|:--|--:|--:|
| \(1^5\) | 1 | 9,999,360 |
| \(2,1^3\) | 10 | 21,504 |
| \(2^2,1\) | 15 | 1,536 |
| \(3,1^2\) | 20 | 504 |
| \(3,2\) | 20 | 24 |
| \(4,1\) | 30 | 32 |
| \(5\) | 24 | 15 |

Each centralizer count is confirmed independently by direct orbital enumeration for the cyclic subgroup generated by the corresponding permutation. Their weighted sum is \(10{,}249{,}320\), hence \(N_{\rm total}=85{,}411\), agreeing with the detailed stabilizer spectrum.

## Verification
Run `python3 verify.py` with ordinary Python 3 and no third-party dependencies. The included program enumerates all 156 subgroups, constructs their ordered-pair orbitals, exhaustively rank-tests the corresponding binary matrices, applies descending subgroup inversion, and checks all 16 exact automorphism-type class counts. It also confirms all seven Burnside centralizer counts and their weighted sum. Finally, an independent brute-force simultaneous-permutation invariance test at dimensions three and four reproduces respectively \(33\) and \(908\) isomorphism classes; the latter is the published binary dimension-four benchmark in Wei--Zou. Expected final status: `VERIFY_OK`. The script's finite enumeration, not a statistical sample, certifies the 5-dimensional census conditional on the stated, standard natural-basis rigidity theorem. Its algorithm specifies a complete executable finite certificate.

## Relationship to prior work
Sriwongsa and Zou (2022) develop automorphism groups of idempotent evolution algebras and characterize full symmetric-group symmetry. Wei and Zou (2023) identify the monomial isomorphism action, derive Burnside counting methods, and evaluate low-dimensional examples through dimension four. Costoya and collaborators (2024) constrain permutation representations arising as automorphism groups. These established structural and counting tools are prerequisites, **not** new contributions claimed here. The additional statement is the *complete automorphism-group isomorphism-type spectrum* in the five-dimensional binary family, obtained by exact subgroup-poset inversion rather than merely applying the overall Burnside orbit count. The separate dimension-five total is supplied as a consistency check. Searches of available research records, equivalently phrased directed-matrix and permutation-similarity problems, and relevant full primary texts did not identify a stronger published result implying this complete spectrum; this is not proof of global priority.

## Limitations
The result is limited to dimension five over the two-element field and perfect evolution algebras; it does not classify imperfect algebras or automorphisms over extension fields. Exact integer enumeration is fully reproducible but depends on executing finite exhaustive code; the human proof establishes exhaustive coverage and the mathematical reduction. Published literature may contain an equivalent stabilizer census under the description of nonsingular binary adjacency matrices of five-vertex directed graphs with loops; no claim of exhaustive bibliographic completeness is made. Independent expert audit has not been performed.

## References
1. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, originally submitted 2022-02-02.
2. X. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, originally submitted 2023-10-18.
3. A. Costoya et al., *Permutation Representations and Automorphisms of Evolution Algebras*, arXiv:2401.05924 (2024).
