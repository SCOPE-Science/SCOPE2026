# Arithmetic persistence of Comon rank gaps two and three
## Finding
Let \(T\in\operatorname{{Sym}}^3(\mathbb Q^{{27}})\) be the explicit rational tensor of Lovitz, with symmetric rank defined by decompositions into scalar-weighted cubes \(\lambda v^{{\otimes3}}\). For \(k\in\{{2,3}}\), put \(V_k=T^{{\oplus k}}\).

Li proved over \(\mathbb R\) and \(\mathbb C\) that
\[
r(V_k)=55k,\qquad s(V_k)=56k.
\]
The same exact equalities hold over every field \(K\) of characteristic \(0\). In addition, there is a finite set of primes \(S\) such that, for every field \(K\) of characteristic \(p\notin S\), the reduction \(\overline V_k\) of the rational model satisfies
\[
r_K(\overline V_k)=55k,\qquad s_K(\overline V_k)=56k.
\]
Consequently, the Comon rank gaps \(2\) and \(3\) supplied by the double and triple direct sums persist over every characteristic-zero field and over all but finitely many positive characteristics.

## Assumptions and scope
Tensor rank is the least number of pure tensors in a decomposition. Symmetric rank is the least number of scalar-weighted symmetric rank-one tensors \(\lambda v^{{\otimes3}}\); this is exactly the convention used by Lovitz over \(\mathbb Q,\mathbb R,\mathbb C\). The tensor \(T\) is the rational \(27\)-dimensional example in arXiv:2609.28292v1, and \(V_k\) is the direct sum of \(k\) independent copies.

The positive-characteristic assertion is cofinite rather than explicit: it proves existence of a finite exceptional set \(S\), but does not determine the primes in \(S\) or claim the result in characteristics \(2\) or \(3\).

## Proof
Lovitz proves
\[
r_{\mathbb Q}(T)=55,\qquad s_{\mathbb Q}(T)=56,
\]
and, more importantly for upper bounds, gives rational decompositions of lengths \(55\) and \(56\). Concatenating those decompositions on independent blocks gives rational decompositions
\[
r_{\mathbb Q}(V_k)\le 55k,\qquad s_{\mathbb Q}(V_k)\le56k.
\]
Li proves the matching lower bounds over \(\mathbb C\) for \(k=2,3\):
\[
r_{\mathbb C}(V_k)=55k,\qquad s_{\mathbb C}(V_k)=56k.
\]

For the characteristic-zero transfer, let \(K\) be any field of characteristic \(0\). The rational decompositions give the same upper bounds after scalar extension to \(K\). Suppose, conversely, that \(V_k\) had a \(K\)-decomposition with fewer than \(55k\) pure tensors. All coordinates of the finitely many factors lie in a finitely generated subfield \(E/\mathbb Q\) of \(K\). Every finitely generated characteristic-zero field embeds into \(\mathbb C\): choose a transcendence basis, send it to an algebraically independent tuple in \(\mathbb C\), and extend across the remaining finite algebraic extension. Applying such an embedding coefficientwise would produce a complex decomposition with the same number of terms, contradicting Li's lower bound. The same argument, now retaining the scalar coefficients \(\lambda_i\), applies to a hypothetical symmetric decomposition with fewer than \(56k\) terms. Hence
\[
r_K(V_k)=55k,\qquad s_K(V_k)=56k
\]
for every characteristic-zero field \(K\).

For the cofinite positive-characteristic statement, clear denominators simultaneously in the rational coordinates of \(V_k\) and in the rational upper decompositions, obtaining an integral model over \(\mathbb Z[1/N]\) for some nonzero integer \(N\). A CP decomposition of length at most \(55k-1\) is the solution set of a finite polynomial system: its variables are the coordinates of \(55k-1\) triples of factor vectors and its equations equate the resulting coordinatewise sum to \(V_k\). Likewise, a symmetric decomposition of length at most \(56k-1\) is a finite polynomial system in the scalar weights and vector coordinates.

Neither system has a complex solution, by Li's exact complex lower bounds. Since the systems have coefficients in \(\mathbb Q\), faithful flatness of \(\mathbb C/\mathbb Q\) and Hilbert's Nullstellensatz give certificates
\[
1=\sum_j h_j f_j
\]
with rational coefficients for each forbidden-rank system. Clearing the finitely many denominators appearing in these certificates and in the upper decompositions excludes only finitely many additional primes. Outside the resulting finite set \(S\), reducing the certificates modulo \(p\) proves that the forbidden decomposition systems have no solution even over an algebraic closure of the residue field, while the reduced rational decompositions give the matching upper bounds. Therefore every field \(K\) of characteristic \(p\notin S\) satisfies the stated exact ranks.

## Verification
The proof uses two published exact-rank inputs and then only field-theoretic and algebraic-geometric transfer. The source inputs were checked in the primary full texts: Li's Theorem 1.1 gives the ranks \(110,112\) and \(165,168\) over \(\mathbb R\) and \(\mathbb C\); Lovitz's Theorem 1.1 and explicit formulas give exact single-copy ranks and rational decompositions of lengths \(55\) and \(56\). The accompanying `transfer_check.py` verifies the rank/gap arithmetic and the finite polynomial-system sizes used in the reduction argument. It does not purport to recompute either source's tensor-rank lower bound or construct the Nullstellensatz certificates.

## Relationship to prior work
Li, arXiv:2610.01660v1, fixes the ground field to \(\mathbb R\) or \(\mathbb C\) and proves exact additivity for two and three copies. Lovitz, arXiv:2609.28292v1, proves the single-copy example over \(\mathbb Q,\mathbb R,\mathbb C\), and explicitly supplies rational decompositions of lengths \(55\) and \(56\). Lovitz also records earlier order-three counterexamples over arbitrary infinite fields of characteristic different from \(2\) and \(3\), but those are different large-dimensional examples and do not give these exact double- and triple-copy ranks.

The new statement is an arithmetic persistence result for Li's specific low-dimensional gap-two and gap-three tensors. It combines the rational upper decompositions with the complex lower bounds to obtain every characteristic-zero field, then uses finite polynomial encodings plus Nullstellensatz certificates to obtain all but finitely many positive characteristics. Targeted searches did not locate this field-transfer statement for these tensors.

## Limitations
The exceptional set of positive characteristics is proved finite but is not made explicit. The argument does not show that the same ranks hold at every prime, and it does not replace the substantial complex lower-bound proofs in Li's work. It also concerns only \(k=2\) and \(k=3\), because those are the direct sums for which the required complex lower bounds are currently available.

## References
1. Jianze Li, *The Comon Rank Gap of a Third-Order Symmetric Tensor Can Exceed One*, arXiv:2610.01660v1, first public 2026-10-01, Theorem 1.1; primary MSC 15A69.
2. Benjamin Lovitz, *A 27 x 27 x 27 counterexample to Comon's conjecture*, arXiv:2609.28292v1, first public 2026-09-23, Theorem 1.1 and the rational decompositions in Section 4.
3. Xiaoyu Song, Baodong Zheng, and Riguang Huang, *Maximal Rank of m x n x 2 Tensors over Arbitrary Fields*, SIAM Journal on Matrix Analysis and Applications, DOI:10.1137/21M1431424, for context that tensor rank can depend on the ground field.
