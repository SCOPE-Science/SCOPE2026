# Scientific review

## Correctness: PASS

On the specified graphs, every vertex state has exactly one successor under the explicitly defined two-contact update. Full reverse indegree elimination on all 177,147 and 531,441 states leaves only the zero fixed state and yields the first-rest histograms. A separately coded C++17 transition and forward trajectory census confirms the histogram and the sharp cutoffs of five and six. The maximal-delay witnesses and one-contact three-cycles are individually replayable. A separate four-cycle on the 4-regular, triangle-free biclique demonstrates the scope boundary. The computational proof is exhaustive only for these two labelled finite graphs; it is not an infinite-family proof.

## Originality: PASS, with historical-priority risk

The 1993 Durrett–Griffeath source describes threshold-dependent excitable cellular automata and lattice phase behavior but not the enumerated Grötzsch/Chvátal two-contact extinction histograms. Gravner–Lyu–Sivakoff (2016), consulted in full HTML, use one-contact finite-graph Greenberg–Hastings dynamics, not this threshold. The full published half-degree-rigidity proof identifies initial three-periodicity at half degree, but does not eliminate other temporal periods or obtain this census. The full four-state Chvátal enumeration uses four refractory phases with one-contact excitation rather than the present three-state two-contact update. Exact source and alias searches found no stronger implication or exact table for this claim. An unindexed historical table remains possible.

## Value: PASS

The Grötzsch and Chvátal graphs are canonical triangle-free four-chromatic test cases. The complete first-rest distributions reveal distinct sharp delay layers and a threshold-driven collapse from persistent one-contact three-waves to universal extinction. The explicit oscillatory \(K_{4,4}\) boundary establishes why their extinction is not just a generic degree or triangle-free consequence. The fully reproducible finite classifications are useful benchmarks for threshold sensitivity on small networks, without claiming a wider theorem.

## Limits and closest sources

The finding depends on correct implementation of the stated finite graph definitions and update rule. The two independently implemented algorithms agree, but no independent external audit has been performed. Relevant prior work: Durrett and Griffeath, *Asymptotic Behavior of Excitable Cellular Automata* (1993); Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (2016); *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles* (public mathematical record); and *Four-state Chvátal excitation: period collapse and six extremal symmetry classes* (public mathematical record).

Self-review: passed. Independent audit: not yet performed.
