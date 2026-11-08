# Complete automorphism-type spectrum of five-dimensional perfect binary evolution algebras

## Finding

Let \(k=\mathbb F_2\). An *evolution algebra* with natural basis \(e_1,\dots,e_5\) has \(e_i e_j=0\) when \(i\ne j\), and \(e_j^2=\sum_{i=1}^{5}M_{ij}e_i\) for a binary structure matrix \(M\). It is *perfect* (also called idempotent as an algebra, in the sense \(E^2=E\)) precisely when \(M\in\operatorname{GL}_5(k)\).

**Theorem.** Up to \(k\)-algebra isomorphism, the complete distribution of the **abstract full automorphism-group type** among these algebras is:

| Full automorphism group | Isomorphism classes |
|:---|---:|
| Trivial group | 81,408 |
| \(C_2\) | 3,694 |
| \(C_3\) | 80 |
| \(C_4\) | 8 |
| \(C_2\times C_2\) | 113 |
| \(C_5\) | 3 |
| \(C_6\) | 8 |
| \(S_3\) | 73 |
| \(D_8\) (order 8) | 8 |
| \(D_{10}\) (order 10) | 1 |
| \(S_3\times C_2\) (order 12) | 7 |
| \(S_4\) | 7 |
| \(S_5\) | 1 |
| **Total** | **85,411** |

There are exactly \(81{,}408\) rigid isomorphism classes, exactly \(4{,}003\) nonrigid classes, and exactly \(9{,}999{,}360\) labeled perfect structure matrices. Thus \(9{,}768{,}960\) labeled structures are rigid. No other abstract automorphism-group type occurs. In particular the \(C_4\) and \(C_2\times C_2\) strata and the \(C_6\) and \(S_3\) strata genuinely differ, despite having the same respective orders.

The general isomorphism criterion, the overall Burnside method, and the fully symmetric \(S_5\) case are established prior mathematics; the independent classification here is the **entire finite automorphism-type distribution**, especially its intermediate-symmetry strata and exact rigid/nonrigid totals.

## Assumptions and scope

The ground field is exactly \(\mathbb F_2\); dimensions and natural-basis labels are fixed at five. All algebra automorphisms are \(\mathbb F_2\)-linear. A group type denotes abstract isomorphism, not an embedding conjugacy class inside \(S_5\). The dihedral notation \(D_m\) means the group of order \(m\). The algebras are commutative but need not be associative. No loops or off-diagonal support patterns are forbidden: all binary matrices of size \(5\times5\) are considered and only the invertible ones retained.

## Proof

**1. Rigidity of natural bases and the acting group.** Suppose \(E_M\) and \(E_N\) are perfect evolution algebras and \(\varphi:E_M\to E_N\) is an isomorphism with matrix \(P\). Since \(\varphi(e_i)\varphi(e_j)=0\) for \(i\ne j\), the invertibility of \(N\) forces \(P_{ri}P_{rj}=0\) for all rows \(r\) and distinct columns \(i,j\). Thus every row of \(P\) has at most one nonzero entry; invertibility forces exactly one nonzero entry in every row and column. Over \(\mathbb F_2\) every nonzero scalar equals \(1\), hence \(P\) is a permutation matrix. Compatibility with squares is exactly \(NP=PM\) (because the entrywise square \(P^{(2)}=P\)). Therefore two such algebras are isomorphic if and only if their matrices are related by simultaneous permutation of rows and columns, \(N=PMP^{-1}\). The full algebra automorphism group is exactly the vertex-permutation stabilizer \(\operatorname{Stab}_{S_5}(M)\). These principles were already established in the cited evolution-algebra literature.

**2. Exhaustive orbit decomposition.** A binary \(5\times5\) matrix is represented by the integer \(\sum_{i,j=0}^{4}M_{ij}2^{5i+j}\), between \(0\) and \(2^{25}-1\). The rank routine in `verify_orbits.cpp` performs exact Gaussian elimination over \(\mathbb F_2\); there are \((2^5-1)(2^5-2)(2^5-2^2)(2^5-2^3)(2^5-2^4)=9{,}999{,}360\) nonsingular matrices. Enumerate every integer in this finite range. For each unvisited nonsingular matrix, traverse its full \(S_5\)-orbit under the adjacent transposition \((1\ 2)\) and the 5-cycle \((1\ 2\ 3\ 4\ 5)\). These generate \(S_5\), so traversal is exhaustive. If the resulting orbit has \(m\) matrices, its full stabilizer has order \(120/m\). For each representative, test all \(120\) permutations directly and record the element-order spectrum of the resulting subgroup. This distinguishes \(C_4\) from \(C_2\times C_2\), \(C_6\) from \(S_3\), and \(A_4\) from \(S_3\times C_2\). The remaining occurring orders \(1,2,3,5,8,10,24,120\) have the corresponding subgroup types listed in the table. The recorded type counts are exactly those in the theorem.

The group-type identifications use elementary subgroup facts for \(S_5\): an order-eight subgroup is Sylow-two and is \(D_8\); an order-ten subgroup is \(D_{10}\); an order-twenty-four subgroup has index five and is \(S_4\). Among order-twelve subgroups, the \(A_4\) option has no element of order six, whereas \(S_3\times C_2\) does. For order four, the presence of an element of order four determines \(C_4\); for order six, the presence of an element of order six determines \(C_6\). Every tested stabilizer satisfies these cases.

**3. Independent orbit enumeration.** `verify_canonical.cpp` re-enumerates all \(2^{25}\) binary matrices and uses exact Gaussian elimination again. It constructs every element of \(S_5\) independently via lexicographic permutations, and declares \(M\) an orbit representative exactly when \(M\) is lexicographically minimal among all \(PMP^{-1}\). Its direct permutation-stabilizer computation reproduces *every row* of the abstract-group table. Both programs verify the independent checks \(\sum_H c_H=85{,}411\) and \(\sum_H (120/|H|)c_H=9{,}999{,}360\).

**4. Independent Burnside check.** `verify_burnside.cpp` computes the invertible fixed-matrix counts for the seven conjugacy classes of \(S_5\). For a representative permutation, invariance under simultaneous row/column relabeling means entries are constant on orbits of ordered pairs. The program constructs these orbits explicitly, enumerates every assignment of binary values to them, and checks invertibility exactly; for the identity it uses the closed \(\operatorname{GL}_5(2)\) product. The results are:

| Cycle type | Permutations | Fixed invertible matrices |
|:---|---:|---:|
| \(1^5\) | 1 | 9,999,360 |
| \(2\,1^3\) | 10 | 21,504 |
| \(2^2\,1\) | 15 | 1,536 |
| \(3\,1^2\) | 20 | 504 |
| \(3\,2\) | 20 | 24 |
| \(4\,1\) | 30 | 32 |
| \(5\) | 24 | 15 |

Burnside's lemma gives \((9{,}999{,}360+10(21{,}504)+15(1{,}536)+20(504)+20(24)+30(32)+24(15))/120=85{,}411\), agreeing with both orbit methods. The Burnside total alone does **not** determine the group-type distribution.

As a further structural cross-check, \(A_4\) in its natural action on four points is 2-transitive; any binary \(5\times5\) matrix fixed by that subgroup (fixing the fifth point) is also fixed by \(S_4\). This explains why the order-twelve \(A_4\) type does not appear as an *exact* automorphism group, although \(A_4\) embeds in \(S_5\).

## Verification

The three self-contained C++17 programs `verify_orbits.cpp`, `verify_canonical.cpp`, and `verify_burnside.cpp` require only a standard C++17 compiler. Compile each with `g++ -std=c++17 -O3 -o program source.cpp` and execute. The first performs exhaustive group-generator orbit traversal; the second independently selects orbit minima by testing all permutations; the third independently checks the group-action Burnside sum via binary orbital matrices. All three terminated with `VERIFY_OK` and produced the counts above. The two orbit programs also independently reproduce the **13 group-type multiplicities**, not just the aggregate 85,411. Their loops range over every binary matrix or every relevant invariant binary matrix, not randomized samples.

## Relationship to prior work

Sriwongsa and Zou, arXiv:2202.01333 (first publicly posted February 2, 2022), establish the monomial automorphism criterion and classify the full \(S_n\) automorphism case. Wei and Zou, arXiv:2310.12368 (2023), establish general finite-field orbit counting and work out dimension-two, -three, and -four class-count formulas. Neither work, in the inspected relevant sections, provides the displayed **five-dimensional binary distribution by abstract automorphism-group type**; the total Burnside class count is not independently claimed as a new general method. Hu's October 2026 preprint on triply transitive permutation images classifies a special \(A_5\) case over fields of characteristic other than two, and does not give the present binary census. Established results on random binary evolution-algebra symmetries provide asymptotic information but do not determine these finite five-dimensional multiplicities.

## Limitations

The result concerns one first-uncovered finite dimension and the smallest finite field. It is a complete **finite** exact census, not a formula for arbitrary dimensions or arbitrary fields. The displayed data do not classify embeddings of a given abstract automorphism group into \(S_5\) up to conjugacy. The exhaustive verifiers give a finite certificate for this fixed domain and do not constitute an infinite-dimensional theorem. Earlier theory already gives the action, some extreme stabilizers, and an implicit total-orbit formula. Novelty of the *complete stabilizer-type table* is relative to the literature and mathematical records inspected, not a guarantee that no equivalent table exists elsewhere.

## References

1. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, first posted 2022-02-02, https://arxiv.org/abs/2202.01333.
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, https://arxiv.org/abs/2310.12368; Linear Algebra Appl. 675 (2023), 142–178.
3. A. Elduque and A. Labra, *Evolution algebras and graphs*, J. Algebra Appl. 14 (2015), article 1550103.
4. X. Hu, *Triply Transitive Natural Permutation Images of Idempotent Evolution Algebras*, posted 2026-10-13, https://www.preprints.org/manuscript/202610.0914.
