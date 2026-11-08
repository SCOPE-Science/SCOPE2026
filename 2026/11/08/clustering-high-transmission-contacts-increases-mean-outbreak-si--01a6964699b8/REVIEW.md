# Scientific review

## Correctness — PASS

The domain is fixed precisely: \(n\ge4\), \(0<q<p<1\), two distinguished edges, independent undirected bonds, and a uniformly sampled source. The two-arc inclusion–exclusion formula is exact on a simple cycle. In the interval expansion, the linear term is position-independent, and the difference between numbers of length-\(k\) intervals covering both special edges is the indicator \(d+1\le k\le n-d-1\); this proves strict mean ordering and all equality cases. On the four-cycle, the count of open bonds has an arrangement-independent distribution. Exactly two open bonds are the sole case whose pattern can affect seed-size-biased moments; their adjacent-open probability difference is \((p-q)^2\). This yields both exact moment differences. The variance phase classification follows from strict monotonicity of an explicit polynomial, its two endpoint signs, and uniqueness of the homogeneous-mean crossing. The standalone exact finite-state and polynomial verifier passed 67 assertions. The analytical proof, not an enumeration cutoff, supports the universal claim.

## Originality — PASS within inspected evidence, provisional

The exact claim concerns (i) a strict finite-cycle rearrangement inequality for the mean size of a uniformly seeded percolation component and (ii) an explicit, complete variance sign-switch classification for the two nonisomorphic placements of two high-probability edges on \(C_4\). Published comparison sources were inspected at the level of mathematical objects and implications:

- Moore and Newman (1999), https://arxiv.org/abs/cond-mat/9911492, study epidemic/percolation thresholds and epidemic spread on small-world networks. The inspected framework uses homogeneous local bond probabilities and random shortcuts, not fixed two-edge probability placement.
- Moore and Newman (2000), https://arxiv.org/html/cond-mat/0001393v1, derive outbreak-size moments through generating functions for the large-network small-world model (particularly the local-cluster and bond-percolation sections). The stated moment formulas do not compare placement of two heterogeneous edges on a finite cycle.
- Allard and collaborators (2008), https://arxiv.org/html/0811.2349v2, allow heterogeneous transmissibility by vertex types on large random networks. Their small-component calculations assume locally tree-like behavior as network size tends to infinity; their analysis does not establish this finite-cycle positional rearrangement or the four-cycle variance sign diagram.
- Kenah and Robins (2006/2007), https://pmc.ncbi.nlm.nih.gov/articles/PMC2215389/, explain the non-equivalence between independent bond percolation and general SIR with random infectious durations. The present claim deliberately concerns the independent-bond model, not the excluded general mechanism.
- Volz and collaborators (2011), https://www.bio.utexas.edu/research/meyers/_docs/publications/VolzPLoSCB11.pdf, study heterogeneous and clustered contact patterns at the network-model level; the inspected portions do not contain the exact fixed-cycle theorem. Partial inspection of this work remains a residual risk, and no whole-document negative assertion is made about it.

Exact aliases searched included 'inhomogeneous cycle bond percolation', 'two enhanced edges', 'mean component size', 'susceptibility', 'rearrangement', 'adjacent versus alternating', and 'variance risk reversal'. No inspected published source entailed the pair of statements. The proof is elementary enough that an older reliability or arrangement theorem under different vocabulary could cover it; independent historical-priority verification is still required. Search absence alone is not novelty evidence.

## Value — PASS

This is a motivated allocation problem: with the same total number and multiset of contact transmissibilities, does spatial concentration or dispersion make a uniformly initiated outbreak larger? The strict ordering gives the full answer for every finite cycle length, not just a four-vertex numerical observation. The variance result is a meaningful second-risk metric because high-transmissibility concentration can change the direction of variance while never changing the sign of the mean difference. The switch is located sharply and has complete equality cases. This directly distinguishes expected epidemic burden from fluctuation risk in a tractable benchmark, without claiming an empirical intervention recommendation or an extension to correlated-transmission SIR.

## Scientific limitations and residual risk

Independent bond probabilities, homogeneous weaker edges, two stronger edges, uniform outbreak source, and a fixed cycle are essential. No variance classification beyond four vertices is claimed. A comprehensive historical audit of specialized graph reliability and percolation rearrangement results is outstanding. No independent mathematical validation is represented.

Self-review: passed. Independent audit: not yet performed.
