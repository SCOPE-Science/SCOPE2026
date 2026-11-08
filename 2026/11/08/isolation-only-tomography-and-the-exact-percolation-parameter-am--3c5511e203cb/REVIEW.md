# Scientific review: isolation-only site-percolation identifiability

## Correctness: PASS

The exact isolation product \(I_v=B_v\prod_{w\in N(v)}(1-B_w)\) gives the marginal and pairwise probabilities. Adjacent vertices cannot both be isolated, while nonadjacent co-isolation has positive probability and exhibits an exact common-neighbor factor. The covariance signs therefore reconstruct all edges. The remaining parameter argument is exhaustive: a distance-two pair yields the retention probability from the pairwise moment ratio; otherwise every component is a clique, and distinct clique degrees yield the parameter from a ratio of means. Equal-size clique components reduce the full isolation-vector law to a categorical singleton event with probability \(p(1-p)^{k-1}\), whose derivative proves the twofold exception and its sole critical point. A union bound proves the stated finite-sample guarantee. The independent finite checker passed 102,616 assertions, but this enumeration is not substituted for the analytic proof.

## Originality: PASS, qualified

The closest literature examines site-percolation component-size phase transitions (Chakraborty, 2017), motif or component estimation under randomly sampled graph observations (Klusowski and Wu, 2018), and reconstruction from noisy unlabelled graph traces (McGregor and Sengupta, 2024). The present observation channel discards every sampled edge and every nonisolated retained vertex but preserves the original vertex labels. The inspected results do not imply the complete identifiability/ambiguity classification for that channel. A published result on singleton slices of Bernoulli products subsumes the scalar two-root ambiguity occurring in one clique; this mechanism is credited and is not claimed as new by itself. The host-wide sign theorem and exact classification across all graph families are not entailed by that scalar result. A historical-priority risk remains, particularly for graphical-model formulations of co-isolation support. The published singleton-slice full text was not accessible for complete inspection; its available abstract is sufficient to recognize the overlapping special case, not to certify comprehensive absence of related extensions.

## Value: PASS

Repeated observations of only isolated retained vertices are a severe information restriction on graph sampling. It is meaningful to characterize exactly which hidden graphs and unknown retention parameters are identifiable under that restriction. The theorem gives a complete arbitrary-host answer, a sharp exceptional family for an entire observable law (not only an estimator), exact recovery of adjacency and two-hop structure from covariance signs, and a valid finite-sample edge decoder. The distinction between recovering the graph and recovering the parameter is a structural aspect of the inverse problem. The guarantee is not claimed optimal or applicable to unlabelled/noisy observations.

## Closest sources and limits

- Chakraborty (arXiv:1712.03334), primary interest: percolation phase transitions on pseudorandom hosts.
- Klusowski and Wu (arXiv:1801.04339 and 1802.07773), primary interest: subgraph-sampling estimators of component and motif totals.
- McGregor and Sengupta (arXiv:2405.04261), primary interest: noisy unlabelled subgraph traces and vertex pairing.
- *Sharp identifiability boundary for singleton slices of Bernoulli products*, published note: overlapping equal-clique scalar ambiguity but no available evidence of arbitrary-host isolation-vector tomography.

The observation labels and independent, homogeneous site-retention assumption are essential. No claim is made about optimal sample size, heterogeneous retention, or general unlabelled traces.

Self-review: passed. Independent audit: not yet performed.
