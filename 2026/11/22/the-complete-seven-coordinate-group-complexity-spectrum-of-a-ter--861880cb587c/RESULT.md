# The complete seven-coordinate group-complexity spectrum of a ternary Fibonacci image

## Finding
Let \(f=0100101001001\cdots\) be the Fibonacci word, the fixed point beginning in \(0\) of \(\mu(0)=01\), \(\mu(1)=0\). Let \(\psi(0)=0\), \(\psi(1)=12\), and \(w=\psi(f)\). For \(G\le S_7\), let \(p_w^G(7)\) be the number of \(G\)-orbits intersecting the set \(F_w(7)\) of its contiguous seven-letter factors, where \(S_7\) permutes the seven coordinate positions. Then the **complete** group-complexity spectrum is
\[
\{p_w^G(7):G\le S_7\}=\{3,5,6,7,8,9\}.
\]
In particular, the intermediate value \(4\) cannot occur although \(p_w^{\mathrm{ab}}(7)=3\) and \(p_w(7)=9\). This resolves the length-seven instance of the intermediate-value question for this canonical ternary morphic image; it does not classify other lengths.

## Assumptions and scope
The words are one-sided and indexed from zero; a factor is contiguous, not scattered. Two seven-letter factors are \(G\)-equivalent precisely if an element of \(G\) maps one coordinate tuple to the other, whether or not every intermediate tuple in a generating sequence is itself a factor. The spectrum includes **all** subgroups \(G\le S_7\), transitive or intransitive. The group action never changes alphabet letters, only their positions. All numerical group classifications below concern actual permutation subgroups, not solely abstract isomorphism types.

The full factor set is
\[
\begin{aligned}
F_w(7)=\{&\mathtt{0012001},\mathtt{0012012},\mathtt{0120012},
\mathtt{0120120},\mathtt{1200120},\\
&\mathtt{1201200},\mathtt{2001200},\mathtt{2001201},\mathtt{2012001}\}.
\end{aligned}
\]
The factors \(\mathtt{0012001}\) and \(\mathtt{2001200}\) have distinct Parikh vectors \((4,2,1)\) and \((4,1,2)\). The remaining seven factors are the seven rotations of \(\mathtt{0012012}\), all with Parikh vector \((3,2,2)\). Thus the abelian and ordinary complexities are exactly \(3\) and \(9\).

## Proof
**Factor completeness.** Every two-letter factor of \(f\) lies in \(\{00,01,10\}\), and all three occur. In its decomposition into \(\mu^5\)-images, both images under \(\psi\mu^5\) have length at least \(11>7\). A seven-letter window of \(w\) therefore lies inside \(\psi\mu^5(ab)\) for some adjacent pair \(ab\in\{00,01,10\}\). Enumerating seven-letter subwords of just these three explicit finite strings gives precisely the nine factors displayed. Conversely every displayed factor occurs in one of the strings, and each such adjacent pair appears in \(f\). This establishes exactness without treating a long experimental prefix as exhaustive.

**Intransitive subgroups.** Every intransitive \(G\le S_7\) preserves some nonempty proper coordinate subset \(A\) and is contained in \(S_A\times S_{A^c}\). Two seven-letter factors are equivalent under this latter group exactly when their Parikh vectors restricted to \(A\) and \(A^c\) agree. The \(63\) unordered nontrivial bipartitions, represented by the unique block \(A\) containing coordinate zero, give the following exhaustive distribution of orbit counts:

| \(p_w^{S_A\times S_{A^c}}(7)\) | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|
| Number of bipartitions | 21 | 7 | 21 | 7 | 7 |

Consequently, any intransitive subgroup has at least five factor-orbits. Each value \(5,6,7,8,9\) is actually attained by these block groups. Explicit zero-based choices of \(A\) attaining them in that order are respectively \(\{0\}\), \(\{0,1\}\), \(\{0,1,3\}\), \(\{0,3\}\), \(\{0,1,4\}\).

**Transitive subgroups.** The established classification of transitive degree-seven permutation groups [2,3] says there are exactly seven conjugacy types: \(C_7\), \(D_7\), \(C_7\rtimes C_3\), \(\operatorname{AGL}(1,7)\), \(\operatorname{GL}(3,2)\), \(A_7\), \(S_7\). The first five types have orders \(7,14,21,42,168\), respectively. In each type the certificate independently generates an explicit representative, checks its group order and transitivity, constructs **every distinct conjugate subgroup within** \(S_7\), then counts its orbits on the actual nine-factor set. The complete histograms, with each pair meaning (complexity, number of conjugate subgroups), are:

| Type | Conjugates | Complexity histogram |
|---|---:|---|
| \(C_7\) | 120 | (3,1), (6,7), (7,14), (8,28), (9,70) |
| \(D_7\) | 120 | (3,1), (6,7), (7,14), (8,28), (9,70) |
| \(C_7\rtimes C_3\) | 120 | (3,1), (5,7), (6,28), (7,49), (8,35) |
| \(\operatorname{AGL}(1,7)\) | 120 | (3,1), (5,21), (6,35), (7,56), (8,7) |
| \(\operatorname{GL}(3,2)\) | 30 | (3,2), (5,28) |

In particular, no transitive subgroup in these five types gives complexity \(4\). The two remaining types \(A_7\) and \(S_7\) give complexity \(3\), because \(S_7\)-orbits are exactly Parikh classes and every factor here has repeated letters: an odd permutation matching two factors can be parity-corrected by a transposition of equal-letter coordinates. This exhausts all subgroup types and excludes complexity \(4\). The spectrum from the intransitive block groups together with complexity \(3\) now proves the claimed equality.

## Verification
The self-contained Python 3 standard-library script `verification/verify.py` supplies a finite certificate for every enumeration in the proof. From the three five-times substituted adjacent pairs it reconstructs the nine-factor set. It checks all \(63\) maximal intransitive block groups, generates the transitive representative groups from listed permutations, enumerates all \(5040\) ambient coordinate permutations to form their distinct conjugates, and counts factor-orbits under each complete group (not just its generating moves). It asserts the published orders, number of conjugates, full histograms, and the final spectrum. Recorded execution results are in `verification/output.txt`. The algorithm relies on the **external, previously established completeness** of the seven transitive-degree-seven types; it does not purport to reprove that group-theoretic classification.

## Relationship to prior work
Launer, Puzynina and Voloshinova [1, Section 5.2 and Open Problem 3] define universal group complexity and ask when a group complexity of four can occur for ternary minimal-complexity words of type III with abelian complexity three. Their Theorem 7 proves that at certain odd standard lengths a group attaining four **must be transitive**. It does not exclude transitive groups, compute the present seven-factor spectrum, or settle this length-seven instance. Here the missing transitive comparison is performed at the first nontrivial odd Fibonacci-standard image length in that construction. The group-classification lists [2,3] supply the exhaustive finite list of permutation types, but make no claim about these specific ternary word factors. No implication from a general group-complexity bound alone yields the excluded intermediate value.

## Limitations
This is an exact finite-length result at \(n=7\), not a theorem for all standard or prime lengths, and not a general answer to Open Problem 3. Its completeness uses the classical classification of the transitive subgroups of \(S_7\) as an external mathematical input. The standalone verification is reproducible but is not an independent audit. An unindexed derivation of the same finite spectrum in earlier permutation-group or word-complexity work cannot be ruled out by a literature search.

## References
[1] M. Launer, S. Puzynina, E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620, first posted 2026-07-08, https://arxiv.org/abs/2607.07620 . Particularly Section 5.2, Lemma 10, Theorem 7, and Open Problem 3.

[2] *Transitive Subgroups of S7*, Arizona State University permutation group data, https://hobbes.la.asu.edu/Groups/group-data/degree7.html . Lists exactly seven transitive conjugacy types and their orders.

[3] Magma Computational Algebra Group, *Database of Transitive Groups*, documentation version 2.29 (2026-08-03), https://magma.maths.usyd.edu.au/magma/handbook/text/820 . Describes the complete degree-seven transitive-group database and historical group-classification provenance.
