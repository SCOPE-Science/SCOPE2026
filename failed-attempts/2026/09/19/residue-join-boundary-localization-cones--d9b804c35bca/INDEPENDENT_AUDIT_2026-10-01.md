# Independent mathematical audit — SCOPE-20260919-d9b804c35bca

Final disposition: **FAILED**.

## Correctness
**PASS** — Finite \(t\)-depth follows from the localization hypothesis and \(1
otin tR\). The leading residue detects positivity exactly. For an incomparable normalized residue class, any common upper bound lies outside \(R\), and multiplying it by any coefficient-field scalar strictly between zero and one leaves it a common upper bound; hence no minimal upper bound exists. Surjectivity of the coefficient field onto \(R/tR\) gives totality, and Lemma 2.1 then makes every nonzero element a unit times a power of \(t\), so the DVR conclusion is correct.

## Originality
**FAIL** — The complete Wang-Yuan-Zhang-Zhu preprint already supplies the general localization criterion, explicitly identifies positivity with a positive coefficient-field residue modulo \(tR\), proves unique levels, and proves Proposition 2.7 by exactly the same 'halve any common upper bound' argument. Replacing their witness \(i\) by an arbitrary residue outside the coefficient field is a direct substitution in that proof. The lattice iff total iff residue-surjective boundary and DVR conclusion are then routine consequences of the same lemmas. The assigned theorem is therefore mechanically implied by the source proof even though its universal wording is not printed there.

### Equivalent formulations
The assigned leading-residue and no-join statements are the general form of an argument already written in the source.

### Broader coverage
Because the source theorem is already general, the assigned residue classification is a direct corollary of its stated framework and proof.

### Exact database or table
The lack of an exact title match is not novelty evidence because the primary source proof already implies the statement.

### Claim versus prior implication
This is a mechanical generalization from the published proof, so implication-based originality fails.

## Value
**FAIL** — The general residue formulation is clean exposition, but after the source's Remark and Proposition 2.7 the generalization requires no new structural lemma: it substitutes an arbitrary non-coefficient residue into the existing proof and applies standard local-ring reasoning. That falls below the value bar for a separate finding.

## Source inspections
- **Directed partial orders on the complex number field** (https://arxiv.org/abs/2609.20494): complete 11-page primary preprint, including Lemma 2.1, Theorem 2.2, the residue Remark, Proposition 2.3, Proposition 2.7, and Theorem 3.1 Assessment: PRIMARY_PROOF_MECHANICALLY_IMPLIES_FINAL_CLAIM. Evidence: The source already identifies positive residues and uses the same scalar-lowering argument to rule out a least upper bound.

## Residual risks
- No correctness defect is asserted; rejection is implication-based prior coverage.
