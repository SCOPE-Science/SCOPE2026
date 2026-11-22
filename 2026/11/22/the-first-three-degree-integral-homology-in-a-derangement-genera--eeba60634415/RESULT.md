# The first three-degree integral homology in a derangement-generated permutation complex

## Finding

Let \(D_n\subseteq S_n\) be the set of derangements, namely permutations \(p=p_1\cdots p_n\) satisfying \(p_i\ne i\) for all \(1\le i\le n\). Let \(X_n\) be the geometric realization of the ordered-word (semisimplicial) complex consisting of every nonempty subsequence of at least one \(p\in D_n\). Distinct ordered words, even with the same underlying letter set, determine distinct cells.

**Theorem (exact first three-degree threshold).** For all \(2\le n\le6\), the reduced integral homology of \(X_n\) is free abelian and is completely given by

| \(n\) | Nonzero reduced integral homology groups |
|---|---|
| 2 | None |
| 3 | \(\widetilde H_1\cong\mathbb Z\) |
| 4 | \(\widetilde H_2\cong\mathbb Z^3\), \(\widetilde H_3\cong\mathbb Z\) |
| 5 | \(\widetilde H_3\cong\mathbb Z^{13}\), \(\widetilde H_4\cong\mathbb Z^3\) |
| 6 | \(\widetilde H_3\cong\mathbb Z\), \(\widetilde H_4\cong\mathbb Z^{74}\), \(\widetilde H_5\cong\mathbb Z^{20}\) |

Consequently, \(n=6\) is the first alphabet size \(n\ge2\) with three separate positive degrees of nonzero reduced homology. In particular, \(X_6\) does not have its homology confined to the two highest degrees, unlike the preceding noncontractible cases.

## Assumptions and scope

The permutations are one-line permutations of the **labelled** alphabet \([n]\). A subword is a subsequence, not necessarily consecutive; the no-fixed-point condition is imposed on a *full generating permutation*, not on the shorter subsequence. The topology is the standard geometric realization of the ordered-word complex, equivalently the order complex of its nonempty word-poset after barycentric subdivision. Homology is untwisted, integral, and reduced. The theorem is finite and applies to precisely \(n=2,3,4,5,6\), not all \(n\).

## Proof

The free abelian cellular group \(C_k(X_n;\mathbb Z)\) has as basis all distinct words of length \(k+1\) which are subsequences of a derangement. With the word's given order as its orientation, the differential is

\[\partial_k(w_0w_1\cdots w_k)=\sum_{j=0}^{k}(-1)^j w_0\cdots\widehat{w_j}\cdots w_k.\]

The differentials satisfy \(\partial_{k-1}\partial_k=0\) by pairwise cancellation. This cellular chain complex computes the homology of the semisimplicial realization (see Chachólski–Levi–Meshulam, Section 1, and Libman, Section 2).

For the six-letter case, all \(6!\) permutations are explicitly tested for fixed points. Exactly 265 are derangements. Enumerating all of their distinct subwords, the chain group ranks, in degrees \(0\) through \(5\), are exactly

\[(6,30,120,351,574,265).\]

In dimensions \(1\) through \(5\), the signed deletion matrices have exact integral ranks

\[(5,25,95,255,245).\]

Crucially, **every nonzero Smith invariant factor of each matrix is \(1\)**. This is verified by finite exact integer matrix reduction, rather than estimated from finite-field ranks: repeatedly choose a nonzero entry \(a=\pm1\), clear its row and column by elementary integral operations, split off the diagonal block \([a]\), and continue. At each step, the remaining entry \(b_{ij}\) is replaced with \(b_{ij}-b_{ip}a b_{qj}\), where \((q,p)\) is the pivot. The procedure terminates with an identically zero residual matrix for each of the five boundaries, proving both the ranks and unit Smith factors. The supplied standalone checker implements these operations on the complete, freshly generated matrices without external algebra libraries.

Because each image \(\operatorname{im}\partial_{k+1}\) is primitive in \(C_k\) (its Smith factors are units), the quotient \(C_k/\operatorname{im}\partial_{k+1}\) is torsion-free. Its subgroup \(\ker\partial_k/\operatorname{im}\partial_{k+1}\) is therefore torsion-free. The Betti number is \(\operatorname{rank} C_k-\operatorname{rank}\partial_k-\operatorname{rank}\partial_{k+1}\), with one additional subtraction in degree zero for reduced homology. This yields the nonzero six-letter ranks \(1,74,20\) in degrees \(3,4,5\), and zero elsewhere.

The identical exact algorithm applied to sizes two through five produces the smaller-case homology groups in the theorem. Since none of those four cases has three positive degrees, six is the first size with that property.

## Verification

Run `python3 derangement_homology_check.py` with Python 3 (standard library only). It enumerates the full derangement sets, all distinct subsequences, and every integer differential, checks all boundary compositions, performs deterministic unimodular unit-pivot reductions to zero residual matrices, and compares integral ranks with independent finite-field eliminations modulo \(2\), \(3\), and \(101\). It checks Euler characteristics and the exact cell counts and ranks for each \(2\le n\le6\). The captured execution output is included as `derangement_homology_check_output.txt`. All of the stated integral groups are consequences of the exact integer reductions; modular experiments are auxiliary.

## Relationship to prior work

Chachólski, Levi and Meshulam establish the general definition and cellular chain complex for permutation complexes, along with a theorem for complexes generated by two permutations. Govc's 2026 paper proves that **every** permutation complex has free fundamental group, a statement about \(\pi_1\), not the higher integral homology of the particular 265-generator complex here. Libman proves the complementary complex generated by **non-derangements** is contractible. The full injective-word complex has a top-dimensional sphere-wedge classification. None of those statements determines the homology of the derangement-generated subcomplex: in particular, contractibility of one subcomplex does not give the homology of its complementary generating family. Elizalde, Hanlon and Hersh study subcomplexes avoiding **relative-order permutation patterns**, not the present restriction on fixed positions of generating permutations.

The contribution is the first exact natural finite threshold at which this fixed-point-free restriction exhibits nonzero integral homology in three consecutive degrees. It is not a general homotopy-type classification and does not claim that all such complexes are wedges of spheres.

## Limitations

The proof relies on a complete, small finite integer certificate, not an all-size recurrence or a homotopy equivalence. In particular, it makes no assertion for \(n\ge7\), no claim about a canonical basis or equivariant homology representation, and no claim of torsion-freeness outside the verified range. Independent mathematical validation has not been performed. Publication-priority searches are incomplete in principle; a not-indexed equivalent computation might exist.

## References

1. D. Govc, *Fundamental Groups of Permutation Complexes* (first submitted 8 November 2026), arXiv:2611.11362v1, https://arxiv.org/abs/2611.11362.
2. W. Chachólski, R. Levi and R. Meshulam, *On the topology of complexes of injective words* (2019), arXiv:1908.03394v1, https://arxiv.org/abs/1908.03394.
3. A. Libman, *The complex of injective words of permutations which are not derangements is contractible* (2023), arXiv:2309.06808v1, https://arxiv.org/abs/2309.06808.
4. S. Elizalde, P. Hanlon and P. Hersh, *Complexes of pattern-avoiding injective words* (2026), arXiv:2610.07303v1, https://arxiv.org/abs/2610.07303.
