# Mathematical review

## Correctness

PASS. The normalized coherent-state sample matrix has an exact diagonal \(We^{-R^2}R^{2k}/k!\) for every angular design. The Rayleigh quotient produces a lower bound on the sharp frame-bound ratio, and log-concavity reduces its denominator to the two endpoint degrees. The ratio is strictly decreasing, then increasing, in squared radius; equality at the unique optimum forces the constant-mode basis vector into a minimum eigenspace. This rigorously yields all moment-vanishing conditions. The square-Vandermonde argument classifies minimum-cardinality equality cases; Stirling gives the stated exponential growth. CHECK.py passed 400 finite tests; the universal proof is independent of them.

## Originality

PASS relative to accessible literature and published-record comparisons, not an assertion of worldwide priority. The nearest motivating full text (Bownik–Yu, arXiv:2603.10423v1) concerns unrestricted-domain discretization and near-tightness. Escudero–Haimi–Romero treat planar Fock density conditions; Berman–Feuer treat unit-circle Vandermonde conditioning without the Fock factorial radial scale. Janszky–Domokos–Adam (1993) and Luo–Tang–Zhang (2024) discuss circular coherent-state superpositions, but available evidence concerns quantum optical features, not the optimal *full projected-frame operator* under arbitrary positive sensor weights. Their complete texts were not all accessible, leaving a stated priority risk. Published-record comparisons, including related Szegő orbit conditioning and positive Fourier sampling, show structurally different sampling spaces and invariants. No novelty is attributed to basic Vandermonde or Stirling tools.

## Value

PASS. The result is a complete, sharp impossibility-and-equality classification for a natural measurement-design restriction, quantifies the exponential cost of one-radius coherent-state sensing of increasing polynomial degree, and identifies precisely which weighted angular placements attain the global optimum. The minimum-sensor regular-polygon rigidity and impossibility of any tight one-circle frame for degrees at least two provide design-relevant boundaries rather than arbitrary numerical instances.

## Limitations

The analysis treats degree-limited Fock polynomials, point evaluations with positive weights and one common radius. Multi-radius schemes and arbitrary preconditioners are outside the claim. The closest older circular-state full texts could not be decisively excluded. Numerical checks do not prove asymptotic claims.

Self-review: passed. Independent audit: not yet performed.
