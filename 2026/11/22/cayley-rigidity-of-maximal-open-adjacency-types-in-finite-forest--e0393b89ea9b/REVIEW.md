# Scientific review

## Correctness

PASS. The component-contraction graph is acyclic: no external vertex can meet one marked component twice, and deleting or contracting forest edges preserves acyclicity. This yields a budget of at most one new external multiple-neighbor pattern per inter-component link. Internal multiple-neighbor patterns are bounded using the two leaves of every nontrivial marked tree component. The combined inequality is \(|\mathcal T_F(A)|\leq2m-t(F,A)\). Equality forces the marked set to be independent, exactly \(m-1\) degree-two external bridge vertices and hence a spanning-tree family of two-element traces. Subdivision plus private leaves proves the converse; Cayley's theorem counts the families and a witness-counting argument gives the minimum host. The included checker executed the recorded finite tests successfully. Risk: the proof covers only finite simple loopless forests and one-point open-adjacency traces.

## Originality

PASS within inspected evidence, with residual historical-priority risk. The closest general result, Sylvester–Zamaraev–Zhukovskii (2026, arXiv:2611.15299), yields a qualitative linear upper bound for open-neighborhood patterns, not the exact extremum or rigidity. Berthe–Foucaud–Lehtilä–Parreau (2026, arXiv:2607.16889, Section 3) analyze closed neighborhoods and obtain a different sharp constant. Both comparisons were made against material text, including the relevant definitions. A 2025 general radius/profile paper was found by search but its full text was not inspected. Related exact analyses of other graph classes do not imply the present forest classification. This is not a formal uniqueness or historical-priority certification.

## Value

PASS. The result changes a broad linear existence theorem into an exact one-variable type count on a canonical width-one graph class. The equality structure is a complete classification of the extremal set systems, making their precise number the classical labelled-tree count rather than merely establishing an asymptotic coefficient. The sharp minimum-size host makes the structural representation optimal. These are natural, reusable invariants of graph adjacency concept families, not arbitrary parameter slices.

## Literature and limits

- Sylvester, Zamaraev and Zhukovskii, *Small classes have linear neighbourhood complexity* (2026), https://arxiv.org/abs/2611.15299.
- Berthe, Foucaud, Lehtilä and Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth* (2026), https://arxiv.org/abs/2607.16889.
- Beaudou, Bok, Foucaud, Quiroz and Raymond, *Profile and neighbourhood complexity of graphs with excluded minors and tree-structured graphs* (2025), https://arxiv.org/abs/2501.08895.

The claim is limited to quantifier-free, open-neighborhood traces. General first-order and closed-neighborhood type classifications are outside its scope. Prior-art searches and selected full-text inspections reduce but do not remove priority risk; independent external audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
