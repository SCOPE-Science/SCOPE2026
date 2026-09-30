# Independent audit — 2026-09-29
- Source: `2026/09/12/095`
- Assigned/current tree SHA: `79b3ef744ac6a77be68b0ff029de315a9a83b3ac`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **failed**

## Three-axis assessment

### Correctness

**PASSED** — The explicit Q3 construction is mathematically sound. Direct rational arithmetic verifies gamma2 = phi*diag(27,1)*phi^{-1}, fixed points 0,∞,1,2, multipliers 27 and 1/27, and the displayed ultrametric identities transfer the standard ping-pong inclusions from the 0/∞ pair to the 1/2 pair. The four radius-1/3 residue discs are pairwise disjoint, so the stated rank-two Schottky conclusion follows.

### Originality

**FAILED** — The scientific content is already a routine consequence of the standard good-fundamental-domain construction. Gerritzen–van der Put theory, as restated by Masdeu–Xarles, gives the converse construction: any suitable collection of 2g pairwise-disjoint non-archimedean balls with the radius-product condition admits generators in good position. For Q3 the four maximal residue balls are exactly such a collection, so existence with four distinct residue classes follows mechanically; the submitted matrices are merely one elementary coordinate realization.

### Scientific value

**FAILED** — The exact matrices are a useful worked example, but they do not add a new theorem, invariant, extremal phenomenon, or nontrivial classification beyond the standard Schottky construction. “Maximal residue spread” is forced simply by choosing the four distinct P1(F3) residue balls, so the package is pedagogical rather than a standalone research finding.

## Independent checks

- verified all listed matrix identities, determinants, fixed points and multipliers independently in exact arithmetic
- checked the non-archimedean ping-pong inclusions and the phi identities in both directions
- compared the claim with the converse good-fundamental-domain theorem, which directly constructs Schottky generators from suitable pairwise-disjoint balls
- confirmed the current main record tree matches the assigned source-tree SHA

## Limitations

- The audit does not claim that the exact two displayed matrices occurred previously in print; failure is because the existence/result follows directly from a standard general construction, not because of an exact-string match.
- The computation itself remains correct and could be kept as an example or tutorial outside the validated-finding corpus.
- Open-access preprint/published material was sufficient; Oxford Download was not needed.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/095
- https://arxiv.org/abs/2408.14918
- https://doi.org/10.1090/mcom/4066
- https://link.springer.com/article/10.1007/s00208-021-02173-y
