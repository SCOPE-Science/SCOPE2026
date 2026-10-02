# Independent scientific audit — SCOPE-20260919-87ff381e2668

Audited at: 2026-10-01T15:09:23.525185Z

Disposition: **failed**

## Correctness — PASS

The prior periodic gauge reduction puts the transverse equation in the \(s=1\) Whittaker-Hill form. The classical semifinite-gap theorem for \(s=2m+1\) closes all even gaps except the first \(m\); setting \(m=0\) therefore closes every periodic gap. The anti-periodic principal-edge expansion is consistent: solving \(A_\pm=1\pm r-r^2/8+O(r^3)\) with \(r=a/b\) and \(A=4/b^2-r^2/2\) gives \(b_\pm=2\pm a/2-a^2/32+O(a^3)\).

### Correctness sources

- assigned RESULT.md
- Hemery-Veselov semifinite-gap theorem
- published SCOPE Whittaker-Hill reduction

### Correctness risks

- The local Floquet exponent expansion is asymptotic near the principal resonance; it is not a global nonlinear-stability theorem.

## Originality — FAIL

The assigned record explicitly starts from an already-published SCOPE \(s=1\) Whittaker-Hill reduction. Hemery-Veselov's classical theorem then immediately gives the parity selection by substituting \(m=0\). The principal anti-periodic boundary is a standard two-mode degenerate perturbation of that already-published Hill equation. Thus the final claim is a direct corollary plus routine local perturbation, not an original mathematical mechanism.

### Equivalent formulations

The assigned parity statement is literally the \(m=0\) specialization of the classical theorem.

### Broader coverage

The broader spectral theorem dominates the assigned periodic-gap exclusion once the prior SCOPE reduction identifies \(s=1\).

### Exact database or table

The key coverage is theorem implication, not an exact tabulated formula.

### Claim versus prior implication

No extra lemma is needed for the parity rule. The principal tongue coefficients then follow by a two-dimensional perturbative eigenvalue calculation.

### Sources inspected

- Whittaker-Hill equation and semifinite-gap Schrödinger operators — https://arxiv.org/abs/0906.1697. COVERING: Its \(s=1\) case is exactly the assigned periodic-gap closure.
- Cohomological contraction and a Floquet edge in the trigonometric Nosé-Hoover flow — published SCOPE record 2026/09/19/cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19. COVERING_INGREDIENT: It supplies the source-specific reduction needed before applying the classical semifinite-gap theorem.
- Trigonometric Nosé-Hoover oscillator: chaos, periodic orbits and integrability — https://arxiv.org/abs/2609.19958. BACKGROUND: The source supplies the dynamical equation but not the assigned parity selection; that selection is covered by the classical spectral theorem after the prior reduction.

### Checked sources

- https://arxiv.org/abs/0906.1697
- https://arxiv.org/abs/2609.19958
- published SCOPE 2026/09/19/cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19

### Residual risks

- No residual literature uncertainty can restore originality of the parity rule because it is an explicit specialization of the cited classical theorem.

## Value — FAIL

The dynamical interpretation is useful, but the surviving mathematical content is a direct spectral-theorem specialization plus standard local perturbation algebra. Under the stated bar, that is explanatory synthesis rather than a distinct worthwhile new finding.

### Value sources

- Hemery-Veselov
- published SCOPE prior reduction

### Value risks

- This does not dispute the usefulness of identifying which resonances can open.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The statement concerns linear transverse stability of the exact central orbit and weak-coupling local tongues only.
