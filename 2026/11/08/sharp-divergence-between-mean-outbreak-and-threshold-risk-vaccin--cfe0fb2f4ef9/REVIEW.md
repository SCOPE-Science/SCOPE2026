# Self-review: sharp path vaccination objective conflict

## Correctness — PASS
The argument proves the entire parameter range rather than inferring universal behavior from enumerations. For each open path component, a weighted identity in the numbers of consecutive \(h\)- and \(h+1\)-blocks gives the exact probability-tail numerator after uniform seeding. Its affine dependence on component size and an exact gap \((h-1)p^h\) determine every threshold-risk optimizer. Pairwise connectivity and strictly increasing first differences determine the mean-optimal central vertices. The intersection cutoff and strict excess follow without a missing boundary case, including \(n<h\). The included standard-library exact-rational checks have been replayed; they are finite corroboration only.

## Originality — PASS within the inspected evidence
Miller (2008) treats size versus epidemic probability and bounding, Altarelli et al. (2013/2014) target expected infection-burden containment, and Holme (2017) studies exact small-graph epidemic node-importance rankings. Their inspected results do not imply the complete fixed-case-count threshold tail optimization on paths for every \(n\), \(h\), and \(0<p<1\). The all-order sharp divergence from the mean objective, not the elementary run-count identity by itself, is the proposed claim. Relevant published equivalent formulations in uninspected graph-reliability literature remain a historical-priority risk.

## Value — PASS
The two optimization objectives represent different intervention priorities. The classification proves that they agree only up to the exact cutoff \(n\le2h\); beyond it, expected-outbreak-optimal protection is provably suboptimal for threshold risk, with a computable positive gap. This supplies a useful path-topology benchmark for model-design and intervention comparisons. The result does not establish effectiveness under general disease dynamics or for large-epidemic fractions.

## Closest scientific sources and limits
See Miller, *Bounding the Size and Probability of Epidemics on Networks* (2008), https://arxiv.org/abs/0803.0999; Altarelli et al., *Containing epidemic outbreaks by message-passing techniques* (2013/2014), https://arxiv.org/abs/1309.2805; Holme, *Three faces of node importance in network epidemiology* (2017), https://doi.org/10.1103/PhysRevE.96.062305. The theorem assumes homogeneous independent undirected edge transmission, a uniformly seeded initial infection after perfect single-node protection, and an absolute outbreak-size threshold. Historical priority and validation by an independent party remain unperformed.

Self-review: passed. Independent audit: not yet performed.
