# Independent audit — 2026-10-01

## Final claim

For centralizer matrix algebras, the Cartan matrix has the stated gap-diagonal stable integral form and Cartan group; singular equivalence preserves that stable form and group; every finite abelian group is realized by a nilpotent one-matrix centralizer algebra.

## Correctness — PASS

The mathematics is correct. For each primary exponent set the min-matrix Cartan block is integrally diagonalized by successive differences, so its stable integral form is the gap multiset and its cokernel is the corresponding direct sum of cyclic groups. Chen--Xi's singular-equivalence classification preserves the multiset \(U_c\), hence the stable diagonal form and Cartan group. Choosing cumulative block sizes from invariant factors realizes any finite abelian group. No computational certificate is needed beyond these exact integer arguments.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- X. Li, C. Xi, Derived and stable equivalences of centralizer matrix algebras, arXiv:2312.08794, complete 28-page primary preprint inspected; Lemma 2.18 gives the integral congruence/gap criterion.
- Z. Chen, C. Xi, Singular equivalences and homological conjectures, arXiv:2603.20643v2, complete 30-page primary preprint inspected; Definition 3.1 and Theorem 4.9 give Sg-equivalence and \(U_c=U_d\) under singular equivalence.
- Published-record semantic search for centralizer Cartan groups, stable integral forms, and nilpotent realizations.

Residual risks:
- None.

## Originality — FAIL

Originality fails under the required implication/corollary standard. Li--Xi already prove that the relevant Cartan min-matrices are integrally congruent exactly when their gap multisets agree. Chen--Xi later prove that singular equivalence of centralizer matrix algebras is exactly Sg-equivalence and explicitly note that Sg-equivalence gives \(U_c=U_d\). Combining those two published statements immediately yields the assigned stable integral Cartan form and Cartan-cokernel invariance. The finite-abelian-group realization is then a routine substitution into the same gap formula by choosing cumulative block sizes.

### Equivalent formulations

Searches:
- Published-record semantic query: centralizer matrix algebra Cartan group stable integral congruence singular equivalence nilpotent realization
- Li--Xi arXiv:2312.08794 Lemma 2.18
- Chen--Xi arXiv:2603.20643 Definition 3.1

Evidence:
- Li--Xi identify the integral congruence class with the ordered gap multiset.
- Chen--Xi define Sg-equivalence by data that imply \(U_c=U_d\).

Reasoning: Cartan cokernel, Smith data, stable integral form, and gap multiset are equivalent formulations here once the min-matrix block is diagonally reduced.

### Broader coverage

Searches:
- Li--Xi 2023 full preprint
- Chen--Xi 2026 full preprint

Evidence:
- Li--Xi give the exact integral-congruence theorem for these Cartan matrices.
- Chen--Xi classify singular equivalence and preserve the exact multiset needed by Li--Xi.

Reasoning: Together the published results dominate the main invariant claim, even though Chen--Xi state only the determinant consequence in their headline theorem.

### Exact database or table

Searches:
- Li--Xi Lemma 2.18 gap multiset
- Chen--Xi \(U_c\) data

Evidence:
- The exact diagonal entries are the successive gaps and final exponent; entries equal to one are stably trivial.
- The singular classification preserves their multiset.

Reasoning: No separate numerical table is needed: the database-equivalent datum is already the preserved gap multiset.

### Claim versus prior implication

Searches:
- Chen--Xi Theorem 4.9 plus Definition 3.1
- Li--Xi Lemma 2.18

Evidence:
- Singular equivalence implies Sg-equivalence, hence \(U_c=U_d\).
- Equal gap multisets give integral congruence of the Cartan min-matrices.

Reasoning: The stable congruence and cokernel invariance are a direct published-theorem composition; the realization statement is a direct cumulative-gap construction and therefore also a routine corollary rather than an independent new theorem.

### Source inspections

- **Derived and stable equivalences of centralizer matrix algebras** — Decisive prior ingredient: congruence is equivalent to equality of the gap multiset. Material read: Complete 28-page primary preprint, with Lemma 2.18 inspected in full. Method: Primary full-text and rendered-page inspection. Evidence: Lemma 2.18 explicitly diagonalizes the Cartan-type min-matrices to successive gaps and characterizes integral congruence by those gaps.
- **Singular equivalences and homological conjectures** — Decisive prior ingredient: singular equivalence is Sg-equivalence, and Sg-equivalence explicitly preserves \(U_c\). Material read: Complete 30-page primary preprint, including Definition 3.1, Theorem 4.9, and the Cartan-determinant consequence. Method: Primary full-text and rendered-page inspection. Evidence: Definition 3.1 states Sg-equivalence and \(U_c=U_d\); Theorem 4.9 makes it equivalent to singular equivalence.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- X. Li, C. Xi, Derived and stable equivalences of centralizer matrix algebras, arXiv:2312.08794, complete 28-page primary preprint inspected; Lemma 2.18 gives the integral congruence/gap criterion.
- Z. Chen, C. Xi, Singular equivalences and homological conjectures, arXiv:2603.20643v2, complete 30-page primary preprint inspected; Definition 3.1 and Theorem 4.9 give Sg-equivalence and \(U_c=U_d\) under singular equivalence.
- Published-record semantic search for centralizer Cartan groups, stable integral forms, and nilpotent realizations.

Residual risks:
- None.

## Scientific value — FAIL

Stable Cartan groups and realizations are natural objects, but in this case the answer is already mechanically determined by two published classification statements. The remaining work is a short composition of known gap data with known integral congruence and a direct cumulative-gap substitution, which falls below the requested value bar for a genuinely open or non-mechanically-implied gap.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- X. Li, C. Xi, Derived and stable equivalences of centralizer matrix algebras, arXiv:2312.08794, complete 28-page primary preprint inspected; Lemma 2.18 gives the integral congruence/gap criterion.
- Z. Chen, C. Xi, Singular equivalences and homological conjectures, arXiv:2603.20643v2, complete 30-page primary preprint inspected; Definition 3.1 and Theorem 4.9 give Sg-equivalence and \(U_c=U_d\) under singular equivalence.
- Published-record semantic search for centralizer Cartan groups, stable integral forms, and nilpotent realizations.

Residual risks:
- None.

## Conclusion

The finding is scientifically rejected because all three axes must pass. Correctness evidence is preserved, but the final claim fails the required originality and scientific-value standards.
