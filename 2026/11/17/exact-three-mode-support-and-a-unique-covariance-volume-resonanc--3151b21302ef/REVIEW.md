# Scientific assessment

## Correctness — PASS

The stationary convolution is unique because all three decay rates are positive. The binary-chain covariance decays exponentially at the total switching rate; integrating the two time orderings yields all nine covariance entries. The exact determinant identity and its derivative were independently re-evaluated symbolically; Descartes' one-positive-root count and the endpoint signs establish the unique global maximum. The support is characterized by moment coordinates of the common binary history, and the fixed-mass, fixed-first-moment quadratic rearrangement yields both sharp third-moment bounds. Positivity of every finite switching-history probability supplies the reverse support inclusion. The section area integrates exactly to volume \(1/30\). A packaged checker verifies the algebra, while the reachability and maximization quantifiers follow from the written proof.

## Originality — PASS with residual publication-priority risk

The exact model appears in Benaïm–Bichard, arXiv:2406.17891, Example 1.5; Proposition 2.1 establishes stationary-law uniqueness and an implicitly defined reachable support, while Theorem 2.2 treats regularity. Bakhtin et al., arXiv:2009.01299, already describe the planar support by two switching-flow arcs. Those results are credited and not presented as new. No statement in the inspected texts gives the explicit \(1:2:3\) three-dimensional support inequalities, its volume \(1/30\), or the unique covariance-determinant optimizer \(\kappa_*\). General formulas for moments of telegraph-driven filters are known, and Pawula's 1987 abstract explicitly announces such formulas; the elementary covariance entry formula alone is not new. The substantive assessed addition is the coupled three-dimensional support/volume and strict rate-resonance classification, not the general filtering technique. An exact equivalent in older signal-processing or moment-body literature remains a risk.

## Mathematical value — PASS

The exact support geometry makes the accessible set concrete for a natural three-dimensional nonelliptic switching model previously given only abstractly. In particular, its volume is independent of both Markov transition rates, while the determinant measuring stationary dispersion has a strict *interior* maximum at one universal normalized switching rate; both very slow and very fast switching lose generalized variance. This resolves a motivated parameter-design question on this canonical three-mode example rather than reporting a numerical peak or an arbitrary selected slice. The novelty/value conclusion is restricted to this natural fixed spectral ratio.

## Scope and limitations

No assertion is made for arbitrary contraction spectra, non-Markov signals, the smoothness of the invariant density, or general information-theoretic optimality. The support calculation uses classical moment rearrangements. The algebra was replayed with SymPy, but the finite numerical cases do not establish the infinite-dimensional reachable-set claim; that claim is proved separately by chattering and positive-probability cylinder events. Two relevant preprints were materially inspected; the older Pawula article's abstract, not full text, was inspected and remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
