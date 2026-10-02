# Independent mathematical audit — SCOPE-20260918-71f63ad5f584

Final disposition: **FAILED**.

## Correctness
**PASS** — For a frozen-variable word w, the derivation D_w lowers the number of occurrences of the active generator by one, so it is locally nilpotent. Abelianization sends D_w exactly to the commutative coefficient times the active partial derivative; hence the kernel and affine fibers are the commutator ideal, and the degree formula is the dimension difference between free words and commutative monomials. In rank two, the published triangulability theorem for locally nilpotent derivations implies zero detection under abelianization. Thus the displayed algebraic statements are correct.

## Originality
**FAIL** — The final claim is mechanically implied by established rank-two triangulability together with elementary free-algebra facts. Crode-Shestakov prove that every rank-two locally nilpotent derivation is triangulable; abelianization of a one-variable triangular coefficient is injective, which gives the rank-two zero-detection statement. For rank at least three, the displayed invisible derivation with commutator coefficient is immediate from the definition, while the affine fibers and Hilbert series are tautological consequences of the abelianization map from a free algebra to its polynomial quotient. Under an implication-based originality bar, this is covered as a formal corollary/dictionary.

### Equivalent formulations
The advertised threshold is equivalent to combining a published rank-two classification with the canonical commutator-ideal quotient in rank at least three.

### Broader coverage
The relevant general classification dominates the only nontrivial low-rank direction; the higher-rank direction needs no new theorem.

### Exact database or table
Specific database absence does not restore originality when the implication comparison is decisive.

### Claim versus prior implication
These prior structural facts mechanically yield the threshold and its elementary kernel model.

## Value
**FAIL** — Although the threshold is a clear pedagogical way to organize the facts, its new part is a one-line elementary construction plus a dimension subtraction. It does not establish a nontrivial boundary beyond what the existing triangulability theorem and the defining universal properties already force. That makes it a routine deduction rather than a worthwhile new mathematical gap under the stated value standard.

## Source inspections
- **Locally nilpotent derivations and automorphisms of free associative algebra with two generators** (https://doi.org/10.1080/00927872.2020.1729363): primary publisher abstract stating full triangulability of every rank-two locally nilpotent derivation Assessment: STRONGER_PRIOR_STRUCTURE. Evidence: The theorem states that every locally nilpotent derivation of the two-generator free associative algebra is triangulable.
- **Locally Nilpotent Derivations of Free Algebra of Rank Two** (https://arxiv.org/abs/1909.13262): primary abstract and journal landing page Assessment: PRIOR_RANK_TWO_KERNEL_THEORY. Evidence: The paper studies kernels and structure of rank-two locally nilpotent derivations.
- **A Characterization of Local Nilpotence for Derivations of Ore Extensions** (https://arxiv.org/abs/2609.19470): primary abstract; verified full text was unavailable through the lawful retrieval route used Assessment: SOURCE_CONTEXT_WITH_ACCESS_LIMITATION. Evidence: The abstract explicitly says the free associative plane is analyzed through abelianization.

## Residual risks
- The 2026 source full text was unavailable through the lawful retrieval route used, but this does not affect the originality rejection because the decisive implication comes from the accessible 2020 triangulability theorem and elementary algebra.
- No correctness defect is asserted.
