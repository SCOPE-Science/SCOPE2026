# Independent audit — 2026-10-01

## Final claim

Exact spherical-harmonic Hessian and instability index for the Gaussian volume product

## Correctness — PASS

The first variation of Gaussian measure in support coordinates and the exact radial formula for the polar give the stated second derivatives. Their product yields the displayed Hessian. Spherical harmonics diagonalize the quadratic form with coefficient \(2(n-\sigma^{-2})-\ell(\ell+n-2)\) on degree \(\ell\ge1\), so degree two and above are strictly negative, degree one changes sign at \(\sigma^2=2/(n+1)\), and the radial integral identity makes the constant mode strictly negative. This independently reconstructs the stated index/nullspace conclusions.

Checked sources: Resultary 2026-09-17: Exact second-variation spectrum of the uncentered Gaussian volume product at the ball; Artstein-Avidan–Fradelizi–Wyczesany, Uncentered Blaschke–Santaló inequalities for the Gaussian measure, arXiv:2609.18472; Huang–Xi–Zhao, The Minkowski problem in Gaussian probability space, Adv. Math. 385 (2021)

Residual risks: The result is second-order only and does not settle nonlinear/global behavior at the critical or open parameters.

## Originality — FAIL

Originality fails decisively. Resultary contains a 2026-09-17 record—one day earlier—with the same Gaussian volume product, the same full support-function Hessian, the same spherical-harmonic eigenvalues, the same constant-mode proof, the same \(2/(n+1)\) translation threshold, the same nullspace/positive-index conclusion, and the same open-interval infinitesimal-stability corollary.

### Equivalent formulations

Searches: Resultary: Gaussian volume product Hessian spherical harmonics instability index translated ball

Evidence: The top earlier hit is the 2026-09-17 'Exact second-variation spectrum of the uncentered Gaussian volume product at the ball'. Its complete RESULT.md was inspected.

Reasoning: The formulations are mathematically identical after notation changes \(f\leftrightarrowarphi\), \(M_\sigma\leftrightarrow M\), and \(a_\sigma\leftrightarrow a\).

### Broader coverage

Searches: Resultary prior Gaussian Santaló Hessian records; Artstein-Avidan–Fradelizi–Wyczesany

Evidence: The 2026-09-17 SCOPE record strictly covers every asserted second-variation conclusion; the motivating primary preprint supplies the degree-one translated-ball threshold.

Reasoning: The final claim is wholly covered by the earlier SCOPE theorem.

### Exact database or table

Searches: Resultary record 714d3bdc8013 exact formulas

Evidence: The earlier record prints the same boxed Hessian and identical spectral cases.

Reasoning: This is exact duplicate coverage, not merely a related title.

### Claim versus prior implication

Searches: Complete RESULT.md of prior 2026-09-17 record

Evidence: Every substantive theorem clause in the assigned record is already present.

Reasoning: Prior implication is equality of statements.

### Source inspections

- **Exact second-variation spectrum of the uncentered Gaussian volume product at the ball** (https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-gaussian-volume-product-hessian-spectrum--714d3bdc8013): COVERING: essentially identical theorem and proof precede the assigned record by one day. Material read: Complete RESULT.md, including theorem, proof, harmonic diagonalization and literature section. Evidence: The prior record states the same Hessian formula, degree-one threshold, degree-two coefficient, constant-mode negativity, exact kernel and index.
- **Uncentered Blaschke–Santaló inequalities for the Gaussian measure** (arXiv:2609.18472): Supplies the motivating translation instability but is not needed for the decisive originality failure. Material read: Abstract/translated-ball threshold context. Evidence: The source identifies the \(2/(n+1)\) translated-ball transition and the open global interval.

Checked sources: Resultary 2026-09-17: Exact second-variation spectrum of the uncentered Gaussian volume product at the ball; Artstein-Avidan–Fradelizi–Wyczesany, Uncentered Blaschke–Santaló inequalities for the Gaussian measure, arXiv:2609.18472; Huang–Xi–Zhao, The Minkowski problem in Gaussian probability space, Adv. Math. 385 (2021)

Residual risks: None material for originality: the earlier Resultary theorem matches the final claim essentially formula-for-formula.

## Scientific value — FAIL

Although the Hessian theorem is mathematically meaningful, this assigned record does not fill an unknown gap: an earlier published SCOPE record already contains the same theorem and proof. Under the value standard for an exact invariant, a known answer does not qualify as a new worthwhile finding.

Checked sources: Resultary 2026-09-17: Exact second-variation spectrum of the uncentered Gaussian volume product at the ball; Artstein-Avidan–Fradelizi–Wyczesany, Uncentered Blaschke–Santaló inequalities for the Gaussian measure, arXiv:2609.18472; Huang–Xi–Zhao, The Minkowski problem in Gaussian probability space, Adv. Math. 385 (2021)

Residual risks: None material for originality: the earlier Resultary theorem matches the final claim essentially formula-for-formula.

## Limitations

- Scientific rejection is due to exact prior coverage; the mathematical Hessian computation itself is correct.
- The theorem is second-variation only and does not settle the global maximization gap.

## Conclusion

Disposition: **failed**. A validated finding requires all three axes to pass.
