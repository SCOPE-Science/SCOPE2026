# Scientific review: Two peaks and a three-critical-point bound for rooted-broom outbreak variance

## Correctness
PASS. The root component decomposes exactly into an independent binomial leaf count and a truncated-geometric path count. Exact moment identities give the polynomial in RESULT.md. The derivative has three sign changes by Descartes' rule; exact inequalities show the signs +,-,+,- at p=0,2/3,3/4,1 throughout the claimed integer range. Together they prove exactly three simple interior stationary points and the sharp two-maxima upper bound **within rooted brooms**. The attached exact checker checks finite instantiations and direct edge-mask calculations, but is not used to substitute for infinite proof.

## Originality
PASS to the extent supported by inspected evidence. Moore--Newman (1999), Kenah--Robins (2007), Sharkey et al. (2013), and Nogawa--Hasegawa--Nemoto (2016) provide close modeling background, but their examined results do not establish the exact rooted-broom variance-curve critical-point bound and two-peak parameter regime. In particular, bimodality of an outbreak-size distribution is not bimodality of the variance as transmission probability changes. The nearest compared mathematical statements involve comparisons between sources, not two maxima of one source's variance. Searches are not a proof of historical uniqueness.

## Value
PASS. Two distinct variance peaks show that finite-tree outbreak uncertainty can have separated transmission windows even with homogeneous independent bonds. The complete three-critical-point bound in the canonical rooted-broom family and the infinite robust interval of leaf counts give structural content beyond an isolated numerical instance.

## Closest literature and limitations
- Moore and Newman, arXiv:cond-mat/9911492 (1999): independent-edge epidemic percolation and thresholds on small-world networks.
- Kenah and Robins, PMCID:PMC2215389 (2007): general SIR with random infectious periods is not equivalent to independent bond percolation.
- Sharkey et al., PMCID:PMC4541714 (2013): exact Markovian SIR moment equations on finite trees, but a different process and observable.
- Nogawa et al., arXiv:1602.00803 (2016): cluster-size PDF bimodality at fixed probability, not variance-curve bimodality.

Limits: only rooted brooms are classified; neither global minimum size nor all finite trees are classified. No independent historical-priority audit has been performed.

Self-review: passed. Independent audit: not yet performed.
