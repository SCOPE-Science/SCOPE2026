# Independent mathematical audit

## correctness

PASS

Reconstructed the cumulative difference H against removal of storage (not against accessible inert storage). The Laplace transform, with c=v+k and decay rates λ± from the two-state generator, is α[(ℓ−k)s+ℓv]/[s(s+c)(s+λ−)(s+λ+)]. Equivalently H(t)=α[(ℓ−k)g(t)+ℓv∫_0^t g(u)du] for g the convolution of the three decaying exponentials. All three rates are positive, so this independently checks the strict signs at ℓ=0 and ℓ≥k, the eventual gain, and the Taylor coefficients near ℓ=k. For 0<ℓ<k, the characteristic polynomial is negative at c and both density weights are positive; the density ratio to the no-storage exponential is strictly convex, starts at 1 with negative derivative and eventually exceeds 1, hence has exactly one positive crossing. The cumulative difference first decreases from zero, then rises to the strictly positive eventual gain αvℓ/[c(c(β+ℓ)+αℓ)], giving exactly one later positive crossing. Increasing ℓ can be coupled by adding a storage-only reaction clock; strict gain at any t>0 follows on paths entering and staying stored through the deadline with an added event and no lower-rate reaction. This strictly orders the roots. Continuity at each finite t gives the two endpoint limits of the root. Near zero reactivity, the spectral separation persists, the crossing is O(log(1/ℓ)) by exponential tail bounds, and balancing the slow spectral tail and the eventual gain gives the full logarithm with P₀ and ν in the record, since (λ−−ν)T_*→0. Near equal reactivity, g(t)=t²/2+O(t³) uniformly, and the nonzero root gives k−ℓ=(vk/3)T_*+O((k−ℓ)T_*+T_*²). This first implies T_*=O(k−ℓ) and then the stated quadratic-error expansion. The conclusions assume a mobile initial pulse, constant rates and an independent exponential mobile exit, not a general residence-time law. Inspected check.py; did not execute the supplied diagnostics.

## originality

PASS

On the checked evidence, the supported distinction is the exact cumulative-incidence sign classification against removing storage, including the unique monotone crossover and both endpoint laws. Separate channel/storage first-order uptake and generic phase-type formulas are not new. The exact catalogue match was this same frozen record, and the distinct same-day analogues were compared without assuming priority from their date.

## value

PASS

The sharp sign trichotomy answers when a longer observation window actually reverses the conclusion about adding storage, rather than just delaying removal. The divergent and collapsing crossover scales explain two different experimental horizon sensitivities even in the minimal model. The mathematical benchmark remains useful without a fitted stream model, but must not be interpreted as a downstream breakthrough prediction or a field-scale extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
