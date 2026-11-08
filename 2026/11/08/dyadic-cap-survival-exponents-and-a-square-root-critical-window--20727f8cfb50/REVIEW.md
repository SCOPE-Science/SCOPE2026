# Scientific review: dyadic cap-survival exponents

## Correctness

**PASS.** The forward polar map is an increasing homeomorphism for each \(0<t<1\), and its inverse is exactly \(Q_t(\theta)=\theta+\arcsin(t\sin\theta)\). Hence the nonentrance set is a spherical cap complement with an explicit one-dimensional surface-area integral. The exact deficit recurrence \(r_{j+1}=r_j-\arcsin((1-\delta)\sin r_j)\) is independently rederived from that inverse. Smooth pre-collapse iterations, the branch expansion near \(\pi/2\), and a mean-value estimate after collapse yield the advertised powers and constants. The proof fixes each dimension and iteration count; it never infers an infinite limit from numerical tests. The standalone checker tests the inverse relationship and the limiting coefficients at multiple parameters and dimensions.

## Originality

**PASS within inspected evidence.** The map and its topological properties predate this result. Shah–Yadav (arXiv:1606.08797, 2016) proves the homeomorphism and studies distality and fixed points, mostly on the circle. Choudhuri–Faraco–Yadav (arXiv:2209.05236, 2022) treats distality, expansivity and orbit behavior on spheres; its full-length preprint text was checked at the definitions and relevant results. Known normalized-translation flow formulas also give single-step inverse and Jacobian calculations. None of the inspected sources states an iterated surface-area cap-survival law with a dyadic exponent staircase and an explicit square-root boundary-layer profile. Published-record searches for the same map, its inverse formula and the crossover returned only different dynamical systems or other spherical geometric probabilities, rather than a stronger covering statement. Novelty is therefore a best-knowledge scientific assessment, not a global priority certificate.

## Value

**PASS.** A normalized affine sphere homeomorphism becomes noninvertible at the limiting parameter. The probability that uniformly sampled initial points avoid a target cap measures the geometry of this loss of invertibility. Even the qualitative existence of an attracting pole does not predict the observable's sharp rarity, the count-dependent exponent, or a half-integer exponent at each dyadic angular resonance. The full family of resonances and its universal crossover is a natural quantitative classification of that singular geometry, not a parameter substitution or a fixed-number table.

## Closest prior literature and limitations

The principal background is Choudhuri, Faraco and Yadav, *On the distality and expansivity of certain maps on spheres*, arXiv:2209.05236 (first posted 2022-09-12), and Shah and Yadav, *Dynamics of Certain Distal Actions on Spheres*, arXiv:1606.08797 (first posted 2016-06-28). Their qualitative conclusions do not imply the stated metric-statistical constants. Broad normalized-translation-flow literature could contain equivalent but unindexed calculations; the available evidence does not rule out every such possibility. The result applies to a centered spherical cap under a pure translation followed by normalization, for fixed iteration number as \(t\uparrow1\). It does not address off-axis caps, general affine maps, or simultaneous long-time limits.

Self-review: passed. Independent audit: not yet performed.
