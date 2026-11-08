# Scientific review: matched-degree seed-budget reversals

## Correctness — PASS

For irreversible two-neighbor activation on finite connected simple graphs, the proof reduces unsuccessful seeding to the existence of an unseeded fort. This criterion directly enumerates all failure configurations at seed budgets three and four in the two displayed six-vertex witnesses. The lower budgets vanish by the seven-edge versus eight-required-edge counting argument; the higher budgets are immediate. The independent-seeding crossover follows from the exact profile generating polynomial. The order-six minimality and uniqueness are certified by a standalone exhaustive enumeration over **all** labelled graph edge masks up to order six, with a separate permutation-based automorphism/orbit check. The executable certificate was rerun from its actual file and passed. Numerical evaluation at sample parameters is not substituted for the algebraic all-parameter proof.

## Originality — PASS within inspected evidence, with residual risk

Watts (2002, https://pmc.ncbi.nlm.nih.gov/articles/PMC122850/) introduces and analyzes global cascades on random graphs using a related social-threshold process. Freund, Poloczek and Reichman (2015, https://arxiv.org/pdf/1503.00158) analyze minimum contagious-set size using density, edge counts and degree conditions, rather than all exact seed-budget coefficients on six-vertex degree-matched graphs. Feige, Krivelevich and Reichman (2016, https://arxiv.org/pdf/1602.01751) study asymptotic contagious-set existence and bounds for random graphs, not the finite seed-profile comparison. Guilbeault and Centola (2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8292353/) explicitly study degree-preserving rewiring and cascade frequency, but use larger graphs, numerical comparisons and clustered seeding, not a proof of this unique order-six crossover. Existing results on complete multipartite conversion sets apply to another graph class and do not imply the displayed theta/barbell result.

The inspection compared claims and applicable hypotheses, not just paper titles. The exact profile polynomial, unique six-vertex degree class, isomorphism classification and Bernoulli threshold were not found in the inspected material. This is a provisional originality judgment; terminology variants, older enumerations or unpublished finite tables could alter historical priority. The Centola–Macy (2007) publisher page was readable only through the abstract and citation data, so its full body was not certified as noncovering.

## Value — PASS

Degree distributions and fixed seeding budgets are basic summaries and intervention constraints in social diffusion. This theorem isolates the smallest connected-network setting where **even a complete degree sequence cannot rank cascade reliability consistently as budget changes**. The reversal is not just an arbitrary example: it is a sharp, unique first obstruction, with explicit percentages at consecutive budgets and a closed-form independent-seeding crossover at \(p=2/3\). The two topologies contrast redundant parallel pathways against densely clustered communities joined by a narrow bridge, motivating the mechanism of multi-neighbor reinforcement. It does not assert empirical relevance beyond the specified irreversible threshold model.

## Limitations and closest literature

The minimality classification is finite and computationally exhaustive, not a general theorem for all network orders. Larger networks and heterogeneous or fractional thresholds may behave differently. Historical novelty awaits independent inspection. Closest primary literature: Watts (2002), Freund–Poloczek–Reichman (2015), Feige–Krivelevich–Reichman (2016), Guilbeault–Centola (2021), and Centola–Macy (2007; abstract-only access). No formal-machine proof, empirical validation, or independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
