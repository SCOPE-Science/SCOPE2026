# Self-review

## Correctness (C): PASS

Both cubic equations are smooth (binary factors separable in characteristic five), and the isomorphism over \(\mathbb F_{25}\) follows from projective equivalence of the binary-root triples. All 27 geometric lines are explicitly constructed: nine root-pair lines and 18 graph lines, with graph matrices exhaustively found by exact \(\mathbb F_{25}\) coefficient comparison. Exact rank tests and line-incidence matrices produce unimodular rank-seven Picard bases; the fifth-power Frobenius matrices square to the identity and preserve these forms. The integer kernel bases are saturated, yielding ranks 6 and 4, Smith invariants and full zeta functions. The standalone code was executed against the final calculations. Risks: the classical 27-line and cubic-surface Picard facts are invoked as standard geometric theorems; computations are reproducible but not independently audited.

## Originality (O): PASS, qualified

The initiating source's Section 4.1 gives the split local cubic and Section 4.3 its nonsplit-looking equation only over \(\mathbb F_{25}\); the paper computes extension-field point totals but not the relative descent of these two explicit \(\mathbb F_5\) equations, their line Frobenius cycles and integral arithmetic Picard lattices. McKean establishes general allowed line counts and structural incidence constraints, not this pair's arithmetic lattices. Rybakov–Trepalin classifies broader Galois possibilities for minimal cubics, not the explicit pair at hand. Multiple actual published-finding corpus searches found unrelated cubic-surface and del Pezzo arithmetic, not the same pair. Direct priority comparison against all historical finite-field cubic tables is incomplete; this is a residual risk, not evidence of absolute novelty.

## Value (V): PASS

The two equations are a natural arithmetic-descent issue raised by the passage from the characteristic-five tangent cubic to the \(\mathbb F_{25}\) normal form in the recent threefold resolution. Their distinct arithmetic Picard lattices and full zeta functions identify exactly what information is lost in that extension: the same geometric exceptional cubic has rational Picard ranks 6 or 4 and discriminator orders 2 or 8, with point counts 51 or 31 over \(\mathbb F_5\). This is a complete structural answer for naturally specified arithmetic forms, not an arbitrary finite census. It does not claim a new general classification of cubic surfaces or a new Calabi–Yau resolution.

## Prior sources and limits

- Burek–Chmiel–Cynk–Oczko, arXiv:2611.15943v1, full HTML Sections 4.1, 4.3 and the displayed cubic equations, November 11, 2026.
- McKean, arXiv:2101.08217, full arXiv text, Theorems 1.1–1.2 and Section 5 line-count incidence and fifteen-line double-six discussion.
- Rybakov–Trepalin, arXiv:1611.02475, abstract and general W(E6) minimal-cubic statement only; full text not inspected. Older cubic-surface arithmetic tables could contain equivalent specializations.

Self-review: passed. Independent audit: not yet performed.
