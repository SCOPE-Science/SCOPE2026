# Self-review

## Correctness: PASS

The exact finite-block MAP optimum is the sum over observed run totals of their maximum joint duration mass. Given the source, maximal input and output constant runs match, and independence makes these maxima factor across input runs. A positive composition of length \(r\) and sum \(L\) has an extreme candidate with mass \(a_1^{r-1}a_{L-r+1}\); summing over all totals proves the universal lower bound. For positive log-convex dwell laws, pairwise outward transfers increase products, giving equality at every total, not merely asymptotically. Log-concave inward transfers give balanced maximizing compositions and the stated double-series formula. The strict comparison at length \(L=r+2\) proves the strict gap. Conditional stochastic processing cannot increase the optimal exact-guessing probability. The Markov source identity follows by tilting only diagonal transitions. All assumptions and exceptional cases are explicitly stated. The exact-rational checker passes independent finite tests, with no claim that finite tests replace proof.

## Originality: PASS against inspected literature, with priority risk

The full accessible arXiv:2606.06808 sections defining geometric duplication, soft alignment and information-rate expressions do not establish the exact all-duration MAP success functional. Its conditional Shannon-entropy penalty does not imply the zero-one exact guessing probability. The complete author-hosted text of Mitzenmacher (2008) discusses general run-duration capacity but no source-given posterior-maxima law or log-curvature universality. Cheraghchi–Ribeiro arXiv:1806.06218 addresses capacity bounds. The accessible abstract of arXiv:2608.01433 is not sufficient to rule out implicit coverage; this specific gap and unindexed equivalent work remain possible. Indexed-result searches of duration recovery, log-convex MAP segmentation and equal-sum modes found no exact equivalent; absence from an index alone is not a proof. General extremal-product lemmas are acknowledged as classical rather than presented as newly invented. The combined conditional-channel recovery interpretation, exact all-parameter factorization and sharp dwell-class boundary are the assessed claim.

## Value: PASS

Individual dwell-time recovery is a natural operational synchronization task in nanopore and sticky replication channels, distinct from decoding the unknown source. The result solves its noiseless finite-block MAP probability for every known word and every positive iid dwell law, yields a sharp distribution-free envelope at fixed one-sample mass, and gives an unexpected entire log-convex universality class rather than merely geometric replication. The complementary log-concave series identifies how light-tailed dwell laws change the optimal segmentation, while a tilted transition matrix supplies exact Markov-source averages and a sharp downstream-noise converse. These are useful channel invariants, not arbitrary finite parameter slices.

## Residual limitations

Source information is given to the decoder; iid positive dwell assumptions and a distinguishable noiseless readout are essential. The paper arXiv:2608.01433 could not be inspected beyond its abstract; implicit priority or general posterior-guessing results may exist elsewhere. This self-review is not independent certification.

Self-review: passed. Independent audit: not yet performed.
