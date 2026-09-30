# Independent audit — 2026-09-29
- Source: `2026/09/12/096`
- Assigned/current tree SHA: `ff13870f7509ed9892a229196a19ffe1a8c0d6f5`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **failed**

## Three-axis assessment

### Correctness

**FAILED** — The central obstruction is false as stated. A finite étale morphism of non-archimedean curves does not force skeleton-edge dilation/expansion factor 1. Étale annulus covers can have degree d>1 (Kummer-type covers); on the skeleton the map has degree/expansion factor d and metric radii/lengths scale accordingly. Therefore the asserted “étale pullback total length = 3 times the base total” argument does not follow, and 18≠9 does not rule out the proposed cover.

### Originality

**NOT_ASSESSED_DUE_TO_CORRECTNESS_FAILURE** — No originality credit is assigned because the headline non-liftability theorem depends on the invalid dilation-1 premise. The standard literature explicitly treats positive integer edge expansion factors for finite morphisms of skeleta.

### Scientific value

**FAILED** — The explicit Schottky curve may be a valid worked construction, but the record’s advertised scientific contribution is the non-liftability decision. Since that decision is unsupported by the metric argument, the package cannot remain a validated finding.

## Independent checks

- verified the algebraic matrix/fixed-point arithmetic and the stated theta edge-length bookkeeping separately
- checked the decisive definition against Berkovich annulus-cover theory
- confirmed that an étale annulus-to-annulus cover may have one dominant term of degree d and induces degree d on the skeleton, contradicting the record’s d=1 assertion
- confirmed the current main record tree matches the assigned source-tree SHA

## Limitations

- This audit does not assert that the requested degree-3 Mumford cover actually exists; it establishes that the published impossibility proof is invalid and therefore cannot support the headline.
- The Schottky certification and theta-length calculation are not the failure point.
- Open full text from Publications mathématiques de Besançon was available; Oxford Download was not needed.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/096
- https://www.numdam.org/item/10.5802/pmb.18.pdf
- https://doi.org/10.1186/s40687-014-0019-0
- https://doi.org/10.2140/ant.2015.9.267
