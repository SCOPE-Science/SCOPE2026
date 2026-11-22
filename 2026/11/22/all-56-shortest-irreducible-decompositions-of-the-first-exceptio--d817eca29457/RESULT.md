# All 56 shortest irreducible decompositions of the first exceptional ordinary numerical semigroup

## Finding

Write \(H_{28}=\{0\}\cup\{28,29,\ldots\}\). An *irreducible decomposition* is an unordered, irredundant collection of irreducible numerical semigroups with intersection \(H_{28}\). **Exactly 56** such decompositions have the minimum length four. Exactly 28 have multiset of factor Frobenius numbers \((24,25,26,27)\), and exactly 28 have \((24,26,27,27)\). These exhaust the shortest decompositions.

More precisely, every shortest decomposition is uniquely constructed from four independently chosen factors \(A,B,C,D\). For a factor \(T\), put \(E(T)=\{14,\ldots,27\}\setminus T\). The choices are:

* \(A\) has Frobenius number 24. Its set \(E(A)\) is one of
  \[\{24\},\ \{15,24\},\ \{17,24\},\ \{15,17,24\},\ \{14,24\},\ \{14,15,24\},\ \{14,19,24\}.\]
  For each of these seven sets, exactly two distinct irreducible semigroups realize it.
* \(B\) is uniquely determined by either \((F(B),E(B))=(25,\{15,17,19,21,23,25\})\) or \((27,\{15,17,19,21,23,25,27\})\).
* \(C\) is the unique irreducible semigroup with \((F(C),E(C))=(26,\{14,18,22,26\})\).
* \(D\) is uniquely determined by either \((F(D),E(D))=(27,\{16,20,27\})\) or \((27,\{15,16,20,27\})\).

All \(7\cdot2\cdot2\cdot2=56\) resulting unordered collections are distinct, irredundant and have intersection \(H_{28}\). The motivating paper already exhibits a four-factor decomposition and identifies the first failure of its constructive bound; the new result is the complete classification and exact multiplicities, with a fully explicit finite noncoverage certificate for three factors.

## Assumptions and scope

Throughout, \(\mathbb N=\{0,1,\ldots\}\). A numerical semigroup is a cofinite additive submonoid of \(\mathbb N\). Its Frobenius number \(F(T)\) is its greatest gap. Irreducibility means that \(T\) cannot be an intersection of two strictly larger numerical semigroups. For an odd \(F\), an irreducible semigroup is symmetric; for an even \(F\), it is pseudo-symmetric. Equivalently, it contains exactly one element of every complementary pair \(\{a,F-a\}\), for \(1\le a<F/2\), omits \(F\), and, for even \(F\), omits \(F/2\). Additive closure remains necessary. The classification here is for the *single mathematically distinguished* first counterexample to tightness of the published logarithmic constructive bound, not a claim about larger ordinary semigroups.

The special gaps of \(H_{28}\) are exactly \(\Omega=\{14,15,\ldots,27\}\). A collection of oversemigroups intersects in \(H_{28}\) if and only if their missing sets cover \(\Omega\); this is the standard special-gap criterion, and it is also easy here: for every \(1\le t<14\), the multiple \(k t\), where \(k=\lceil14/t\rceil\), lies in \(\Omega\). Any additive submonoid that omits this multiple necessarily omits \(t\). The length-four claim is for unordered collections, not ordered tuples.

## Proof

**1. Exhaustion of admissible factors.** Every irreducible factor \(T\) containing \(H_{28}\) has \(F(T)\le27\). A factor with \(F(T)<14\) misses no special gap and is redundant, so cannot occur in an irredundant decomposition. Thus consider only \(14\le F\le27\). For each such integer, form all \(2^{\lfloor(F-1)/2\rfloor}\) complementary-pair choices. Add \(0\) and all integers greater than \(F\), omit \(F\) and the even midpoint, and reject a choice whenever two included positive integers sum to an omitted integer at most \(F\). The remaining sets are precisely all irreducible oversemigroups with that Frobenius number. Necessity is the symmetric/pseudo-symmetric characterization. Sufficiency follows from closure, cofiniteness and the same characterization. Distinct bit masks represent distinct numerical semigroups.

**2. Exact intersection test.** For each retained factor encode \(E(T)\) by a 14-bit mask. The finite enumeration yields 285 relevant irreducible factors, with 163 distinct nonempty masks. Two independent checks can be applied to the resulting catalogue. First, form all unions of exactly three masks: among 8,788 different unions, the maximum population is 13, whereas \(|\Omega|=14\). Therefore at least four factors are necessary. The explicit generators
\[\langle13,14,15,16,17,18,19,20,21,22,23,25\rangle,\ \langle2,27\rangle,\ \langle4,15,17\rangle,\ \langle7,11,15,17,19,23\rangle\]
produce four irreducible factors whose special-gap sets, respectively, are \(\{24\}\), \(\{15,17,19,21,23,25\}\), \(\{14,18,22,26\}\), \(\{16,20,27\}\). Their union is \(\Omega\). This also establishes the minimum length independently of any interpretation of the motivating paper.

**3. Exhaustive classification.** Form all pairs of different nonzero missing-set masks; index pairs by their bitwise union. For each pair, join it to every lexicographically later disjoint pair of mask indices whose union covers the still-uncovered bits of \(\Omega\). Expand each mask into all distinct irreducible factors realizing it. Since the four mask indices are strictly increasing, every unordered four-factor decomposition appears exactly once. The 56 resulting decompositions have precisely the two Frobenius-number profiles stated above. Directly inspecting these 56 records gives the seven alternatives for \(E(A)\), with two distinct realizations each; the two alternatives for \(B\); the unique \(C\); and the two alternatives for \(D\). Every combination of these alternatives covers \(\Omega\); uniqueness follows because the named roles are determined by Frobenius numbers and missing-set patterns, even when \(B\) and \(D\) both have Frobenius number 27.

**4. Independent counting identity.** Let \(c(U)\) be the number of distinct relevant irreducible oversemigroups \(T\supseteq H_{28}\), each with Frobenius number at least 14, satisfying \(E(T)\subseteq U\), for each \(U\subseteq\Omega\). The inclusion-exclusion identity
\[N_4=\sum_{U\subseteq\Omega}(-1)^{14-|U|}\binom{c(U)}4\]
counts unordered four-factor collections whose union of missing sets is all of \(\Omega\). As no three factors suffice, every counted collection is automatically irredundant. An independently implemented subset-zeta transform evaluates this sum to 56, agreeing with the explicit pair-join classification. This second method uses the catalogue but not the pair-join search.

## Verification

Run \(\texttt{python3 verify.py}\) using Python 3 with only its standard library. It verifies the general symmetric/pseudo-symmetric enumeration against a separate direct membership-bit enumeration for all \(1\le F\le13\), checks the entire minimum-length census for \(2\le m\le32\), verifies explicitly that three factors never suffice at \(m=28\), and checks a concrete four-factor witness. It then reproduces every one of the 56 distinct shortest decompositions and both Frobenius signatures. An independent inclusion-exclusion calculation returns the same count, printing `CLASSIFICATION_OK 56` and `INCLUSION_EXCLUSION_OK 56`.

The finite computation is exhaustive because every possible irreducible factor falls into one enumerated complementary-pair assignment, closure is decided by all sums at most its Frobenius number, and each four-element subset of distinct masks is considered exactly once before expanding the distinct factors represented by its masks. The implementation is a complete finite proof certificate for this fixed semigroup; it does not imply claims for untested multiplicities.

## Relationship to prior work

García-Sánchez and O'Neill, *Lengths of irreducible decompositions of numerical semigroups* (arXiv:2602.00404v1, January 30, 2026), introduce a constructive interval of irreducible decomposition lengths for ordinary numerical semigroups. Their Example 4.2 gives a five-factor decomposition of \(H_{28}\), while Remark 4.4 explicitly supplies a *four*-factor decomposition and says that \(m=28\) is the first multiplicity at which their construction misses the minimum. **These are prior results, not new claims here.** The present contribution determines *all* shortest decompositions, their exact number 56, and the two complete Frobenius-signature classes. García-Sánchez, *Factorizations into irreducible numerical semigroups* (arXiv:2410.13729v1, 2024) establishes general decomposition-length context but does not give this fixed-object four-factor census. No claim is made that lack of a matching search result proves global historical priority.

## Limitations

The classification concerns irreducible oversemigroups and intersections for \(H_{28}\) alone; it is not a general formula for the number of minimal decompositions of arbitrary numerical semigroups. The proof of the seven-mask classification uses a fully specified exhaustive finite algorithm, not a conceptual uniform parametrization over all multiplicities. An unindexed earlier count or a pre-existing computational table may affect priority; independently performed expert review has not occurred.

## References

1. P. A. García-Sánchez and C. O'Neill, *Lengths of irreducible decompositions of numerical semigroups*, arXiv:2602.00404v1 (first publicly posted 2026-01-30), especially §4, Example 4.2, Theorem 4.3, Remark 4.4. https://arxiv.org/abs/2602.00404
2. P. A. García-Sánchez, *Factorizations into irreducible numerical semigroups*, arXiv:2410.13729v1 (2024). https://arxiv.org/abs/2410.13729
