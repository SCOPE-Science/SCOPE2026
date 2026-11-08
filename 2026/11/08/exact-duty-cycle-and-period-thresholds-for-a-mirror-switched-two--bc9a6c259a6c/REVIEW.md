# Scientific review: mirror-switched two-community SIS schedules

## Correctness — PASS

The exact trace is derived from the two traceless generators \(uX\pm vZ\), their common quadratic identity \((uX\pm vZ)^2=q^2I\), and the determinant of the monodromy. The resulting \(\operatorname{arcosh}\) exponent holds for all real parameters in the stated domain, including static duty endpoints. The strict convexity calculation for \(\operatorname{arsinh}(k\sinh s)\) proves the one-dimensional period monotonicity. The strict symmetry order in the duty fraction yields the complete boundary equations, unique critical period, and square-root edge asymptotics. Metzler comparison justifies nonlinear extinction only for negative Floquet exponent; no nonlinear converse or stochastic extinction-time statement is asserted. The standalone standard-library verifier passed 1,679 numerical consistency assertions against directly Taylor-expanded matrix products. Numerical checks are supporting checks and not substitutes for the analytic proof.

## Originality — PASS with priority risk

The relevant 2024 SIS temporal-network paper includes an explicit two-community switching framework and illustrates Parrondo suppression for fixed time fractions, but does not present the exact mirror-swapped duty/period phase diagram. The 1982 matrix-product paper establishes general convexity inequalities (including two-parameter spectral convexity and an ensuing monotonicity lemma), so general frequency monotonicity or balanced scheduling alone is expressly **not** asserted as original. The claim assessed here is the complete *explicit two-parameter epidemic threshold domain*, the unique critical total period, the exact permissible duty fraction interval, and its quantitative critical closure for this structurally meaningful contact exchange. Comparisons with relevant mathematical results and the inspected published literature did not identify a statement implying this whole explicit diagram. Exact equivalent work not indexed in the inspected records remains a risk; the 1990 and 2004 sources were only available in part, and stronger general theorems may subsume components.

## Value — PASS

For a natural two-community situation where a high-risk within-community exposure alternates between communities but cross-community contacts remain fixed, whether both harmful static regimes can jointly become safe is a decision-relevant question. A mere fast-switching existence theorem does not say how much one may lengthen the period or how unbalanced the duty fractions can be. The exact boundary gives both answers for all model parameters, with a quantitative square-root loss of schedule flexibility at the critical period. This is a complete naturally motivated classification, not a finite calculation or a generic convexity restatement. The applicability is limited to the deterministic SIS approximation and the mirror-swapped pair.

## Closest literature and limitations

- Sejunti, Taylor, Masuda, arXiv:2406.16787, full HTML version 3, sections 2.3 and 3.1–3.5 and Appendix B: the initiating two-community Parrondo SIS framework and Floquet products; not an optimized duty/period classification.
- Cohen, Friedland, Kato, Kelly (1982), *Eigenvalue Inequalities for Products of Matrix Exponentials*, Corollary 9 and Lemma 10: relevant general log-convexity/monotonicity; the general principle is prior mathematics and cannot be claimed as new.
- Lieb (1990), *On the spectral radius of the product of matrix exponentials*: abstract indicates two-dimensional convexity for one matrix-product class, potentially relevant to the monotonicity subclaim; full text not examined.
- Gökçek (2004), *Stability analysis of periodically switched linear systems using Floquet theory*: abstract describes fast-switching stabilization but not this analytic duty interval; full text not examined.
- Persoons, Sensi, Prasse, Van Mieghem (2024), *Transition from time-variant to static networks*: title and abstract concern timescale-separation bounds rather than the exact mirror-swapped phase diagram; full text not examined.

Self-review: passed. Independent audit: not yet performed.
