# Independent mathematical audit — 2026-10-01

## Final claim assessed

Corrected critical-feedback equation and a three-halves edge law in feedback-trained recurrent networks

## Correctness — PASS

PASS. The corrected stationary equation is internally consistent with the source model as represented in the record, and the symbolic expansion is correct. The inspected verifier reproduces the F and G series, the inversion for u_c, the cancellation of the fourth-order epsilon term, the three-halves law, and the numerical g=1.3 consistency check. The target-amplitude law is the algebraic inverse of that local asymptotic. These are statements about the quasi-static DMFT equations, not a finite-network theorem.

## Originality — FAIL

FAIL. The final result is obtained by correcting a missing Gaussian variable in one printed equation using the source's own immediately preceding DMFT equations and then carrying out an ordinary Taylor-series inversion of those same equations. The 2026 primary source already identifies the critical feedback strength and bifurcation in precisely this model. No new structural input is introduced; the three-halves exponent and target inverse law are mechanically determined by the source equations once the typo is repaired. Under the required implication standard, the exact coefficient need not have been printed previously for the result to be covered.

### equivalent_formulations

Searches: Resultary semantic search: feedback trained recurrent neural network critical feedback three halves Vaidya; arXiv:2609.19288 critical feedback strength

Evidence: The exact published-record search returns the audited record; the primary paper already supplies the critical-feedback equations/model whose local expansion is being taken.

Reasoning: The three-halves law is the leading normal-form asymptotic of the source's corrected critical system, not an independent theorem about a different object.

### broader_coverage

Searches: Vaidya 2609.19288 DMFT critical feedback bifurcation; Sompolinsky Crisanti Sommers chaos transition recurrent networks

Evidence: The source directly studies the feedback-driven chaos-to-stability bifurcation and critical feedback strength; older work supplies the underlying chaos marginality criterion.

Reasoning: The audited result refines the local expansion but does not add an independent mechanism beyond the equations already derived in the source.

### exact_database_or_table

Searches: published mathematical record search for y_c proportional to (g-1)^(3/2) in this source model

Evidence: No database/table is relevant because the coefficient is obtained by formal series expansion of existing equations.

Reasoning: The absence of a pre-tabulated coefficient does not establish originality when the answer is mechanically implied by the prior equations.

### claim_vs_prior_implication

Searches: arXiv:2609.19288 corrected Eq 4.6 critical feedback; critical feedback target amplitude recurrent network

Evidence: The source identifies the same critical feedback variable and bifurcation; the finding itself states that its corrected equation comes directly from preceding source equations.

Reasoning: Once that correction is made, routine series inversion implies the exponent, coefficient and target boundary, so originality fails.

## Scientific value — PASS

PASS. Detecting a numerically material equation inconsistency and determining the critical onset law is useful for readers of a new DMFT model. The source-specific correction has a substantive modeling consequence even though it does not clear the originality bar.

## Source inspections

- **Learning-Induced Dynamical Transition in Recurrent Neural Networks** — https://arxiv.org/abs/2609.19288. Material read: Primary-source abstract/indexed statement material; full text was not retrievable through the available open interface during this run. Assessment: DECISIVE_MODEL_SOURCE. Evidence: The source identifies a critical feedback strength and a learning-driven bifurcation in the same DMFT model. The audited record explicitly derives its correction from the source's preceding equations.
- **Suppression of chaos in random neural networks by external input** — https://doi.org/10.1103/PhysRevE.82.011903. Material read: Bibliographic and indexed result context. Assessment: BACKGROUND_NOT_NEEDED_FOR_FAILURE. Evidence: The originality failure already follows from the source-specific implication.

## Limitations and residual risks

The calculation concerns the source paper's quasi-static DMFT approximation and does not prove a sharp transition for finite networks.

- The source full text was not retrievable in this run; the failure rests on the finding's own explicit statement that the corrected equation follows directly from the source's preceding equations.
- The numerical q=1 crossing is not interval-certified and is not a finite-network threshold.

## Disposition

**failed**
