# Scientific review — sharp all-horizon coupled-fold contraction

## Correctness: PASS

The incremental-slope hypothesis gives the two indispensable facts \(at\le h(t)\le t\) and monotonicity of \(t-h(t)\). The ordered-coordinate calculation gives the **exact** formula for the maximum norm after one and two steps. The elementary inequality \(y+|y-h(x)|\ge h(x)\) yields the global \(1-a^2\) factor without approximation. The linear-feedback example attains it for every horizon; a uniform blow-up at the origin transfers exact optimality to the smooth softplus model. The original-coordinate estimate follows from a bounded inverse-logit derivative. The included program passed 126000 floating finite-horizon comparisons and 70 exact rational extremizer comparisons. These checks are corroboration, not substitutes for the written infinite proof.

## Originality: PASS within inspected evidence

Satur's primary paper gives critical global convergence and the exact logarithmic fold, but not an all-horizon uniform sup-norm rate. Its \(3/4\) determinant estimate is about area contraction and does not imply this claim. The closest prior research note derives sharper **pointwise asymptotic** amplitudes and the limiting two-step \(3/4\) factor for nonsymmetric trajectories; its conclusions do not state a uniform sharp bound over all initial states at every finite iteration or the \(a\)-parameter feedback class. Searches for coupled absolute feedback, sharp finite-horizon contraction, and these equivalences found no such claim. A historical nonlinear contraction theorem with stronger coverage remains a priority risk.

## Mathematical value: PASS

The parameter-free critical-state convergence known from the model's original analysis is upgraded to a computable worst-case error certificate valid from the first step, uniformly over initial states, with a provably optimal rate at every horizon. The structural theorem identifies the lower incremental slope as the only needed quantitative input across an infinite family of folded nonlinear maps; it avoids differentiability assumptions and distinguishes nonexpansive single-step behavior from strict two-step attraction. This is a motivated global quantitative gap rather than an arbitrary numeric example.

## Relation to prior literature and limitations

Sources: Satur (2026), arXiv:2611.13318v1, especially Lemmas 2–3 and Theorem 2; the published note *Nonlinear critical-collapse amplitudes and a quadratic phase law in two-player maxima dynamics*. There is no assertion of pairwise norm contraction, off-critical stability, an independently verified priority claim or a physical-time universal constant. The earlier orbitwise amplitude theory is credited, not duplicated.

Self-review: passed. Independent audit: not yet performed.
