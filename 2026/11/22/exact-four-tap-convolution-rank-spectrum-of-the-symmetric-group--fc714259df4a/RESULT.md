# Exact four-tap convolution-rank spectrum of the symmetric group \(S_4\)

## Finding
Let \(G=S_4\), the group of all 24 permutations of four letters. For every four-element subset \(S\subset G\), define the unweighted complex convolution operator
\[
  T_S:\mathbb C[G]\longrightarrow\mathbb C[G],\qquad
  T_Su=\left(\sum_{s\in S}\delta_s\right)*u,
  \qquad \delta_s*\delta_x=\delta_{sx}.
\]
Among the \(\binom{24}{4}=10,626\) subsets, the **complete rank distribution** is

| \(\operatorname{rank}_{\mathbb C}T_S\) | 6 | 9 | 12 | 15 | 18 | 20 | 21 | 24 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Number of supports | 42 | 144 | 576 | 1,008 | 2,856 | 1,728 | 3,024 | 1,248 |

No other rank occurs. More precisely, put
\[
H(S)=\langle s_0^{-1}s:s\in S\rangle,
\]
where \(s_0\) is any one element of \(S\); the subgroup is independent of the chosen \(s_0\), so its order is well-defined. The following table gives every nonzero joint multiplicity; all missing combinations are impossible.

| \(|H(S)|\) | Rank | Number of supports |
|--:|--:|--:|
| 4 | 6 | 42 |
| 6 | 12 | 144 |
| 6 | 24 | 96 |
| 8 | 9 | 144 |
| 8 | 15 | 288 |
| 8 | 21 | 144 |
| 12 | 12 | 144 |
| 12 | 18 | 552 |
| 12 | 24 | 288 |
| 24 | 12 | 288 |
| 24 | 15 | 720 |
| 24 | 18 | 2,304 |
| 24 | 20 | 1,728 |
| 24 | 21 | 2,880 |
| 24 | 24 | 864 |

Under two-sided translation and inversion of supports, there are exactly 34 equivalence orbits. The complete representative, orbit-size and exact-rank table is embedded as `independent_orbits.tsv`. In the Fourier decomposition of \(\mathbb C[S_4]\), these have 18 different rank profiles; the explicit profiles are in `block_profiles.tsv`.

In particular, rank 20 occurs **only** for supports whose difference subgroup is all of \(S_4\); exactly 1,728 such supports occur. Exactly 1,248 four-tap convolutions are invertible, and only 864 of those 1,248 have a full difference subgroup. The rank-six supports are exactly the 42 cosets of the seven order-four subgroups.

## Assumptions and scope
All four coefficients are exactly one, and the four support elements must be distinct; they are otherwise arbitrary, not necessarily a generating set, inverse-closed set, or union of conjugacy classes. The convolution is on complex-valued functions with no \(1/|G|\) normalization (a nonzero scalar normalization would leave ranks unchanged). The count treats supports as labelled subsets of the fixed permutation group, not modulo symmetry. The word *rank* refers to complex-linear operator rank, equivalently rank-weighted Fourier support, **not** a numerical singular-value threshold. This is a finite exact classification, not a statement for general symmetric groups or arbitrary coefficients.

## Proof
**1. The operator has an integral permutation matrix.** Enumerate \(S_4\) lexicographically by the images of \((0,1,2,3)\). Compose permutations using \((pq)(i)=p(q(i))\). For \(S=\{s_1,s_2,s_3,s_4\}\), write
\[
 B_S(x,y)=\mathbf1\{y=s_1x\}+\mathbf1\{y=s_2x\}+\mathbf1\{y=s_3x\}+\mathbf1\{y=s_4x\},\qquad x,y\in G.
\]
This is the transpose of the matrix of \(T_S\) under the stated basis, hence has the same rank. Each row and each column has exactly four entries equal to one. The program `s4_census.c` constructs the multiplication table from the explicit 24 permutations, then constructs this matrix for every strictly increasing four-tuple of indices. No group multiplication table or rank list is imported.

**2. One modular rank computation is an exact characteristic-zero rank computation.** Put \(p=1,000,000,007\), a prime. A \(k\times k\) minor of \(B_S\) has row Euclidean norms at most two. By Hadamard's determinant inequality,
\[
 |\det M|\le 2^k\le 2^{24}=16,777,216<p.
\]
A minor is therefore zero over \(\mathbb Z\) **if and only if** it is zero modulo \(p\). The largest size of a nonzero minor, i.e. the rank, agrees over \(\mathbb Q\), \(\mathbb C\) and \(\mathbb F_p\). Consequently Gaussian elimination modulo \(p\) decides the ranks **without** numerical approximation, exceptional-prime ambiguity, or an unbounded search. The program uses ordinary modular field inversion, checks all \(\binom{24}{4}\) subsets, and accumulates the two tables in the Finding section. The displayed counts are exact outputs of an exhaustive finite algorithm, with the algorithm and its tight arithmetic correctness bound both supplied.

**3. The difference-subgroup split is exact.** For each \(S=\{s_0,s_1,s_2,s_3\}\), form the three group differences \(s_0^{-1}s_j\). Starting at identity, close under right-multiplication by these three generators; because the group is finite, this closure is precisely \(H(S)\). The program records its order and the computed rank. Replacing \(s_0\) by another element of \(S\) changes the generating family but not the cardinality of the subgroup of all pair differences (one obtains the same subgroup), so the table is intrinsic. The 15 displayed nonzero cells add to 10,626, and each rank column agrees with the first table.

**4. Separately implemented rational and representation checks.** Rank is invariant under \(S\mapsto aSb\) for \(a,b\in G\), since \(T_{aSb}=L_a T_S L_b\). It is invariant under \(S\mapsto S^{-1}\), since \(T_{S^{-1}}=T_S^*\). `independent_verify.py` reconstructs all 24 permutations from separate code and all 10,626 supports, partitions them under these exact symmetries into 34 disjoint orbits, and calculates the rank of a representative of each orbit over \(\mathbb Q\) using exact rational matrices. Its orbit-size-weighted totals coincide with the modular results. No ranks are taken from the first program.

There is a second representation-theoretic check. Over \(\mathbb C\),
\[
 \mathbb C[S_4]\simeq\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C)
 \oplus M_3(\mathbb C)\oplus M_3(\mathbb C).
\]
If the ranks of the five Fourier blocks are \((r_1,r_{\rm sgn},r_2,r_3,r_{3'})\), then
\[
 \operatorname{rank}T_S=r_1+r_{\rm sgn}+2r_2+3r_3+3r_{3'}.
\]
The program `block_verify.py` constructs the three-dimensional permutation action on the three pair-partitions of four letters, the four-dimensional permutation action on letters, and its sign twist. Taking out the constant summand gives the three irreducible blocks of dimensions 2, 3 and 3. Exact rational ranks on all 34 representatives give precisely 18 possible five-block profiles, with all ranks and orbit weights consistent with the census. The profile table is embedded as `block_profiles.tsv`.

Thus the entire finite space has been covered by two different exact methods and a third irreducible-block calculation, proving both existence and exclusion of every listed rank and subgroup cell.

## Verification
From the directory containing the supplied files, run

```sh
gcc -O3 -std=c11 -Wall -Wextra s4_census.c -o s4_census
./s4_census
python3 independent_verify.py
python3 block_verify.py
```

The C program is self-contained (C11 standard library). The two Python programs require Python 3 and SymPy for exact rational matrix ranks. `independent_verify.py` generates `independent_orbits.tsv`, which is then read by `block_verify.py`. The supplied `s4_census.out`, `independent_verify.out`, `block_verify.out`, `independent_orbits.tsv`, and `block_profiles.tsv` record the exact outputs that were checked. A nonzero C exit code or failed Python assertion signals a discrepancy. The separate programs use different multiplication/matrix conventions, connected by transposition and regular-representation duality, which preserve rank.

## Relationship to prior work
Alagic and Russell's *Uncertainty Principles for Compact Groups* (first public preprint 2006-08-28) proves the general rank-weighted uncertainty bound; for four-point supports on a group of order 24, it implies the rank lower bound six. Its subgroup extremizers explain the rank-six row. It does **not** classify the remaining rank values, multiplicities or 34 orbit types.

Pinner's *The integer group determinants for the symmetric group of degree four* (2018) factors the full \(S_4\) group determinant and classifies all integer determinant values. The group-determinant factorization controls the product of Fourier-block determinants and can detect invertibility after specialization, but does not give the **rank deficiencies**, 18 block-rank profiles, or a four-indicator support enumeration. In particular, all seven distinct singular ranks in the table have determinant zero, so determinant-value classification does not distinguish them.

Siemons and Zalesski's *Remarks on singular Cayley graphs and vanishing elements of simple groups* (first published 2018) studies singularity for inverse-closed, conjugacy-invariant connecting sets and related group characters. Our four-support family includes nonsymmetric and non-central subsets and asks for exact ranks, not only zero-eigenvalue occurrence. Earlier finite-group Fourier rank results for the quaternion, tetrahedral and odd-dihedral groups concern different groups or different coefficient constraints; they do not imply this \(S_4\) census. Similarity searches alone do not establish historical uniqueness.

## Limitations
The theorem applies only to four unweighted taps on \(S_4\). Coefficients with signs or arbitrary nonzero complex values can change ranks. This is an exact finite classification with a full self-contained computational certificate and a rational orbit cross-check; it is not a purely symbolic classification of the 34 orbits by an intrinsic formula, nor a theorem for larger groups. Mathematical correctness is checked by explicit finite proof and executable algorithms; an independent human audit has not been performed. An unindexed earlier group-algebra or Cayley-spectrum table could duplicate the census. The general group-determinant factorization remains a close conceptual predecessor.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, initial public preprint 2006-08-28, https://arxiv.org/abs/math/0608702 ; complete HTML https://arxiv.org/html/math/0608702v2 .
2. C. Pinner, *The integer group determinants for the symmetric group of degree four*, initial public preprint 2018-06-26, https://arxiv.org/abs/1806.10239 .
3. J. Siemons and A. Zalesski, *Remarks on singular Cayley graphs and vanishing elements of simple groups*, first published 2018-11-30, https://doi.org/10.1007/s10801-018-0860-0 .
4. Standard finite-group Fourier block decomposition and character data for \(S_4\): https://people.maths.bris.ac.uk/~matyd/GroupNames/1/S4.html .
