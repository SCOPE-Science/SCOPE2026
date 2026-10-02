# Independent scientific audit — SCOPE-20260918-8119d118c382

Audited at: 2026-10-01T07:11:57.147372Z

Disposition: **failed**

## Correctness — PASS

The mathematical chain is sound. Han–Liu's Corollary 4.8 gives the dual von Neumann–Jordan constant at most \(1+8\sqrt\delta\) under the almost-BCD hypotheses. Passer's quantitative Jordan–von Neumann theorem converts \(C_{NJ}=1+\varepsilon\) into \(1+O_m(\varepsilon)\) Banach–Mazur distance, yielding the displayed square-root rate. Han–Liu's perturbation theorem gives BCD error of quadratic order in the perturbation, and the standard lower comparison from parallelogram defect to Banach–Mazur distance yields square-root sharpness.

## Originality — FAIL

The main conclusion is mechanically implied by two published theorems on exactly the needed quantities. Han–Liu already state the \(1+8\sqrt\delta\) von Neumann–Jordan control, and Passer already proves that small von Neumann–Jordan excess quantitatively forces Banach–Mazur Euclideanity. The sharpness scale likewise follows directly from Han–Liu's published perturbation estimates plus standard inequalities.

### Equivalent formulations

Composing these statements is exactly the audited upper theorem.

### Broader coverage

The prior results are broader than the record's application and dominate its substantive steps.

### Exact database or table

Exact wording is immaterial under implication-based novelty.

### Claim versus prior implication

No new nonstandard lemma is needed to obtain the final scientific implication.

## Value — FAIL

As a new finding, the result is a routine composition of two quantitative stability theorems plus standard duality/comparison steps. The affine-geometric restatement can be useful exposition, but it does not open a distinct mathematical gap under the stated value bar.

## Sources inspected

- On the Geometry of Wasserstein Barycenter II: Riemannian Rigidity, Essential Non-Branching, and Finsler Models — https://arxiv.org/abs/2609.19564. COVERING_INGREDIENT: Corollary 4.8 already gives the dual von Neumann–Jordan constant at most \(1+8\sqrt\delta\), and the perturbation theorem gives quadratic BCD error.
- An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces — https://arxiv.org/abs/1305.3546. COVERING_INGREDIENT: The theorem supplies the quantitative Banach–Mazur conclusion once the von Neumann–Jordan excess is bounded.

## Checked sources

- https://arxiv.org/abs/2609.19564
- https://arxiv.org/abs/1305.3546
- Resultary semantic search

## Residual risks

- The exact numerical coefficient inherited from Passer's theorem was not the originality issue; even a coefficient refinement would need separate motivation and comparison.
- Scientific rejection is for coverage and value, not mathematical correctness.

## Limitations

- The mathematical estimates are correct, but the main Banach–Mazur conclusion is a direct composition of Han–Liu's published almost-BCD control of the von Neumann–Jordan defect with Passer's published quantitative Jordan–von Neumann theorem; the sharp square-root scale likewise follows from Han–Liu's perturbation estimates and standard comparisons. It is therefore not accepted as a new independent finding.
