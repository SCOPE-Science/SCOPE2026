# Scientific review

**Correctness — PASS.** The proof classifies minimal absent factors by their number of one-symbols, uses southwest-closed factor-occurrence rectangles and tests maximal proper prefix and suffix directly. The bound \(K+13\) forces a finite complement region, and an explicit affine-stability argument extends 3,432 checked anchor cases to arbitrarily large zero gaps. The standalone program checks 10,626 examples by independent factor enumeration; these examples are checks, not a substitute for the proof.

**Originality — PASS (qualified).** Pinho et al. (2009), Crochemore et al. (2015), Charalampopoulos et al. (2018), and Akagi et al. (2022) give general MAW definitions, algorithms, asymptotic upper/lower bounds or RLE-type results. The inspected primary statements do not imply the exact sharp bound \(n\) at fixed weight three or its two labeled maximizers. Search coverage is incomplete for unindexed special cases, which remain a genuine historical-priority risk.

**Value — PASS.** A natural sparsity-restricted family has a complete absent-factor classification and a sharp length-capacity boundary, with all extremizers at every \(n\ge7\). The result goes beyond generic enumeration of one instance, though it does not establish a new unrestricted code/string bound.

**Limitations.** The maximum's equality classification assumes at least seven positions and exactly three ones. The proof has a finite, executable arithmetic certificate for a small exceptional region and an analytical argument for all larger gaps. Higher weights, circular MAWs, absent subsequences and independent mathematical validation are not covered.

## Closest literature

- Pinho et al. (2009), DOI https://doi.org/10.1186/1471-2105-10-137: definition, characterization and computation.
- Crochemore et al. (2015), https://arxiv.org/abs/1506.04917: broad alphabet-size-times-length upper bound and sequence comparison.
- Charalampopoulos et al. (2018), https://arxiv.org/abs/1806.02718: asymptotic tightness, including binary two-marker examples.
- Akagi et al. (2022), https://arxiv.org/abs/2202.13591: MAW structure and efficient reporting from run-length encoding.

Self-review: passed. Independent audit: not yet performed.
