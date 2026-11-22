# Review of a labeled-rooted-tree record reconstruction theorem

## Correctness — PASS
For comparable vertices, insertion ranks along the one common root path are independent; for incomparable vertices, a direct two-variable uniform integral gives positive covariance \(k/((k+a)(k+b)(k+a+b))\). Marginals identify depth, and the only zero-covariance predecessor is the parent. The explicit lower bound \(1/[n^2(2n-1)]\), together with concentration for all empirical marginal and pairwise product moments, proves the stated high-probability exact recovery threshold. Exhaustive exact arithmetic and the standalone reproducible checker support every local algebraic step. No computational experiment is used to certify the universal theorem.

## Originality — PASS, qualified
The closest classical source, Janson (2004 preprint; 2006 journal), supplies the random-record process, independence on paths, and a two-leaf dependence example. The novelty assessed is not the record definition, nor classical exchangeability, but fully labeled tree recovery from binary record-vector moments with an explicit nonasymptotic sample guarantee. Burghart (2023 arXiv/2024 revision) proves completeness of certain polynomial invariants of unlabelled rooted-tree structures, not inversion of these binary record observations. Published records and topology-reconstruction searches did not identify direct or stronger coverage. The available 2004 preprint pages 1–4 were materially read, while its full set of sections and appendices could not be assessed completely; an older equivalent inference theorem remains a risk.

## Value — PASS
The natural statistical problem is whether the hidden ancestry relation can be reconstructed when only repeated record/no-record events at stable vertex identities are observable. The theorem identifies the complete population information needed, gives an exact positive separation from zero for every competing parent, and supplies a uniform confidence guarantee without seeing the continuous marks. This is an inverse result with an operational algorithm, not merely a restatement of known aggregate record-count formulas. It does not claim optimal statistical rate or apply to unlabeled observations.

## Limits and literature
For the model's iid atomless marks, vertex identities and complete binary observations are essential. Historical novelty is not independently certified. Main comparisons: Janson, doi:10.1002/rsa.20086; Burghart, arXiv:2302.08394; Holmgren, doi:10.1017/S096354830999068X.

Self-review: passed. Independent audit: not yet performed.
