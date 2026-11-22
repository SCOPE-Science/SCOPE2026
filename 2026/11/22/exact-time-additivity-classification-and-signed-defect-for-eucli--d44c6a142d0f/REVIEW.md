# Review of time-additivity of Euclidean norm proximal maps

## Correctness

**PASS.** The minimizer is unique; the \(p=1,2\) formulas are immediate by convex first-order conditions. At \(p=\infty\), duality identifies the output with coordinate clipping, and a scalar positive-part decomposition proves exact composition including extinction boundaries. For every finite \(p>1\), smoothness on the positive orthant justifies the implicit-function expansion through quadratic order. The exact product \(\nabla^2\|x\|_p\,\nabla\|x\|_p\) at the displayed positive input has a first coordinate that vanishes precisely when \(p=2\); its sign proves the asserted local defect. The executable checks agree but are not substitutes for the analytic steps. The proof does not depend on rounded computations.

## Originality

**PASS, with a historical-priority risk.** Bërdëllima–Steidl (arXiv:2104.05304, §6.2) constructs nonlinear semigroups as iterated-resolvent limits, rather than asserting additivity of individual finite steps. Bungert et al. (arXiv:1901.06979, §§4.2, 5.2–5.3) supplies broad flow/variational equivalence criteria and explicitly treats the two nonsmooth norm endpoints. Those known sufficient mechanisms are acknowledged. The present claim distinguishes all \(\ell_p\) exponents, proves the finite-exponent exclusion with one common witness, and computes its signed second-order defect. Source searches and full relevant source sections did not identify the exact classification; a previously unstated corollary or older equivalent assertion is still possible. Vilches (arXiv:2007.03798) is a related general proximal-identifiability source, not an identified dominating statement.

## Mathematical value

**PASS.** A full natural-family classification answers exactly when a finite proximal step equals the time evolution obtained by splitting regularization across steps. The exceptional \(\ell_\infty\) endpoint, despite nonsmoothness, and the sign change at the Euclidean exponent are structural; the explicit quadratic defect quantifies the first discrepancy in the nonadditive cases. The result differentiates finite-step resolvents from general continuous gradient-flow semigroups, rather than claiming generic nonexpansivity as a novel observation.

## Closest literature and limits

The closest general literature covers nonlinear resolvent semigroup limits, exact flow/variational equivalence under structural hypotheses, and known soft-thresholding/radial-clipping mechanisms. Those results substantially motivate the classification and limit any originality claim to the all-exponent necessity boundary and its quantified defect. The result does not solve other norm families or independent publication-priority questions.

Self-review: passed. Independent audit: not yet performed.
