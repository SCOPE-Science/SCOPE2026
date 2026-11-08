# Scientific review: first mean-phylogenetic-diversity ambiguity at nine taxa

## Correctness — PASS

The proof reduces equality of complete mean curves to equality of clade-size multisets, uses a complete induction-based generator of nonplane rooted binary trees through nine leaves, and gives an exact covariance polynomial for variance separation. The final difference is \(\operatorname{Var}(X_B(p))-\operatorname{Var}(X_A(p))=2p(1-p)^7\) for every \(p\in(0,1)\). Replaying `check_pd_fingerprints.py` yields 46 nine-leaf shapes, 45 mean fingerprints, exactly one two-shape class and exact independent enumeration of 512 survivor configurations for each witness. The mathematical claims are confined to the full-binary unit-length homogeneous model.

## Originality — PASS, with historical-priority risk

The closest relevant framework is Faller, Pardi and Steel (2007 preprint, 2008 journal): independent random extinction and PD distribution, whose inaccessible full text is a significant unclosed comparison. Steel, Mimoto and Mooers (2007) establish the tree-edge expectation approach; Nipperess and Matsen (2013) study variance under fixed-size rarefaction and discuss tree shape; Matsen and Evans (2012) study matrix spectral indistinguishability. None of the material actually inspected establishes the nine-tip first mean-fingerprint collision or its exact variance gap. Full-text inaccessibility is acknowledged rather than construed as evidence of noncoverage; independent historical verification remains worthwhile.

## Value — PASS

The mathematical object is the complete expected phylogenetic-diversity response to homogeneous extinction probability, a natural idealized conservation-risk summary. Determining the first size where that summary loses tree-shape information, and proving that the variance resolves precisely this first ambiguity, is a motivated finite structural identifiability cutoff. The result is not merely a fresh polynomial evaluation: it classifies all nonplane binary shapes at the first collision and provides an exact, all-probabilities second-moment discriminator.

## Scientific limits

The identification concerns unlabeled rooted shapes, with every edge of length one; there is no claim for arbitrary branch lengths, multifurcations, heterogeneous extinction, finite noisy observations or reconstructing taxon labels. The variance separation is small at intermediate survival probabilities, and historical novelty is provisional.

Self-review: passed. Independent audit: not yet performed.
