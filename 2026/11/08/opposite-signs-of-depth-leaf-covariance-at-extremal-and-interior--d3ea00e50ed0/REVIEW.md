# Scientific review

## Correctness (C): PASS

The theorem states the tree construction, finite ranges and two different leaf conventions precisely. The ancestor-interval-minimum formula and the local-maxima representation of internal leaves reduce the covariance to explicitly listed conditional probabilities. The conditional local-maximum lemma includes near-endpoint and length-two corrections; the resulting rational sums establish the three key-rank regimes and signs for every integer order at least three. Directly reconstructed BSTs and independently evaluated interval-minimum events produce 423,989 exact checks through exhaustive orders up to eight plus complete rank scans through order 120. Those checks substantiate, but do not replace, the arbitrary-order proof. Proof risk: a historical alternative representation may yield a shorter derivation, not a correctness caveat.

## Originality (O): PASS, with remaining historical-priority risk

The closest checked primary studies address rank-indexed and weighted depths in the same BST (Aguech–Amri–Sulzbach, arXiv:1707.00165), one-sided and local-maxima leaf counts (Devroye, 1991), and differently colored leaf-count covariance matrices in random trees including BSTs (Desmarais–Holmgren–Wagner, arXiv:2110.15050). Their inspected materials do not state or imply the exact mixed covariance with the depth of each fixed key and the universal endpoint/interior sign split. Specifically, marginal depth and leaf moments determine neither mixed moments nor signs, and an aggregate colored-leaf covariance does not identify fixed-key depth dependence. The available published-results comparison also found a covariance of root imbalance with BST path length, but this uses different observables; random-recursive-tree rank covariance statements do not dominate the BST theorem. An unlocated earlier mixed generating function could already encode the result; that is the principal residual priority risk.

## Value (V): PASS

Search depth is an algorithmic cost for an individual ranked query, whereas internal leaf count is a global tree-shape statistic relevant to storage and shape balance. Their opposite dependence signs at extreme and interior keys constitute a nontrivial complete rank classification, not a mere textbook marginal calculation or an arbitrary parameter slice. The exact fixed-size law and distinct endpoint, near-endpoint and bulk limits explain an unexpected boundary effect across every size of the standard random BST model.

## Sources and limitations

- Aguech, Amri, Sulzbach (2017), *On weighted depths in random binary search trees*, arXiv:1707.00165v1, inspected main text, in particular Section 4.1 and the rank-indexed ancestor construction.
- Devroye (1991), *Limit laws for local counters in random binary search trees*, inspected main text for its leaf/local-maximum representation and leaf limit results.
- Desmarais, Holmgren, Wagner (2021), *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1, inspected its leaf-count covariance section and BST context.

A primary literature search and a published mathematical-record comparison cannot establish exhaustive historical novelty. All statements are specific to the specified uniform BST model and internal leaves; independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
