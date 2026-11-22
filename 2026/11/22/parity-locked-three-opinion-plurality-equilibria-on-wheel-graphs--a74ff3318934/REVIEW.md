# Scientific review

## Correctness — PASS

For hub color \(0\), an adjacent \(0\)/nonzero pair on the rim forces the nonzero vertex to update, hence a nonunanimous fixed rim excludes the hub color entirely. The resulting two-color rim is locally fixed exactly when neither color has an isolated cyclic singleton. The hub then sees only the two rim colors and remains unchanged exactly at equality of their counts, forcing even rim size. Conversely these requirements satisfy every update rule. Marking one of the \(r\) runs of one color gives the factor \(n/r\) in the exact double-composition formula. An independent transfer matrix has characteristic polynomial \(\lambda^4-(1+z)\lambda^3+z\lambda^2-z^2\); its primitive dominant root, variance \((5+3\sqrt5)/40\) and the two distinguishably weighted self-loops justify the claimed lattice central limit asymptotic. Full-state and independent transfer checks pass in their stated finite ranges.

## Originality — PASS, qualified

The accessible relevant literature describes plurality aggregation (Mossel–Neeman–Tamuz), Nash and coalition equilibria in neighbor-coordination games (Apt et al.), and alternative three-opinion deterministic rules (Di Ianni). The closest prior published wheel findings concern binary synchronous majority, not the three-opinion wheel fixed-state class. The structural implication does not transfer: the extra states require two equally represented rim colors *different* from the hub color. The full arXiv papers' stated results and applicable model sections, the later open full-text article, targeted indexing searches and accessible nearby claims did not provide the claimed all-rim parity classification or exact formula. The coordination-game fixed-state model is not equivalent: our tie-retaining rule can freeze an incumbent that is *not* among tied leading neighbor colors, while a pure Nash best response cannot. In particular, every new nonunanimous wheel fixed state has a hub with zero supporters, so a Nash theorem cannot cover it as a stationary configuration. The remaining limitation is possible unindexed tie-retaining plurality enumerations or related combinatorial cyclic-word results.

## Value — PASS

The wheel is the canonical single-hub cyclic network. With three opinions, every odd-rim wheel has three equilibria, while every even-rim wheel supports an exponentially growing population of perfectly balanced non-consensus equilibria; moreover, the hub has **zero** supporters on the rim in each such equilibrium. This precise parity-dependent qualitative change is absent in the two-opinion case and answers the natural stationary-state count question for a complete graph family. The exact asymptotic entropy and Gaussian \(n^{-1/2}\) factor quantify the effect. No claim is made about the entire attraction dynamics.

## Closest literature and limitations

- Mossel, Neeman and Tamuz, arXiv:1207.0893 (first public 2012-07-04): multi-opinion aggregation and consensus, not wheel equilibrium enumeration.
- Apt, de Keijzer, Rahn, Schäfer and Simon, arXiv:1501.07388 (first public 2015-01-29): neighbor-agreement best responses differ from the incumbent-retaining plurality rule at ties excluding the incumbent; general Nash existence does not imply the wheel count.
- Di Ianni (2025), DOI:10.3390/appliedmath5040147: other three-opinion majority-based rules and complexity theory, not wheel fixed-state enumeration.
- Published binary-majority wheel census: same graph family but different alphabet, with only two unanimous fixed points.

A comprehensive historical priority guarantee would require wider bibliographic verification. Exhaustive computations prove only the inspected finite cases; the all-length statement rests on the supplied mathematical argument.

Self-review: passed. Independent audit: not yet performed.
