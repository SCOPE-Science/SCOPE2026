# Scientific review: exact one-threshold position-feedback walk

## Correctness — PASS

The claim is about the **exact lattice rule** at \(\ell=1\), for all integer \(r\ge1\) and all initial integer sites. The proof enumerates all one-step images, constructs and normalizes the unique closed-class invariant law, and checks every inward transition type. The unbounded ladders are handled through geometric series, not finite cutoffs. Direct four- or five-step global minorizations prove uniform geometric ergodicity, including states outside the stationary support. The one-step conditional drift, together with the minorization, proves finite-time absolute-moment growth. The strict-tail staircases give genuine distinct liminf/limsup constants, so no smooth \(C/z\) tail is claimed. The standalone exact-arithmetic checker passed 6,982 assertions; finite sampling is corroboration rather than an infinite proof.

## Originality — PASS, with explicit prior coverage

Lima and Curado's May 21, 2026 work [1] supplies exactly the microscopic step rule and studies continuum approximation and larger-threshold simulations; the newly investigated regime here is the minimal integer threshold. Montero and Villarroel's 2016 Sisyphus process [2] and Zanette and Manrubia's 2020 multiplicative-reset analysis [3] already contain the general geometric reset ladder and moment threshold. Indeed the \(r\ge2\) radial sector of this walk is *affinely conjugate* to the classical multiplicative-reset chain; these components, isolated, are not presented as original. The new claim is the **entire microscopic family classification**, especially the \(r=1\) central-state recurrence, exact origin mass and altered moment slope, the sharp disappearance of central stationary support at the next admissible integer parameter, and global-start mixing constants for the original lattice chain. Neither cited reset kernel has the physical three-state core and opposite-sign accelerated reset rule. Search uncertainty persists for unindexed papers on this exact boundary model, and independent priority review remains necessary.

## Value — PASS

The 2026 source makes a smooth continuum stationary prediction and calls for studies of transient dynamics and moment scaling. At the smallest spatial threshold, the exact microscopic system has an atomic lacunary law; a one-unit change in the acceleration parameter eliminates all stationary central occupation. It also has uniform total-variation equilibration **simultaneously** with explicit linear growth of the unbounded absolute-position observable. These exact distinctions provide a meaningful boundary test for extrapolating continuum-scale stationarity to small lattice thresholds, not an arbitrary enumeration or an increment to a known parameter table. The significant scientific object is the coupled central random walk and accelerated exterior, not the already-known geometric reset process considered alone.

## Closest literature and limitations

1. H. S. Lima and E. M. F. Curado, *Emergent heavy-tailed distributions from a Markovian random walk*, arXiv:2605.22933v1 (May 21, 2026): original state-dependent rule, continuum density, simulations, future transient-moment question. https://arxiv.org/abs/2605.22933
2. M. Montero and J. Villarroel, *Directed random walk with random restarts*, *Physical Review E* **94**, 032132 (2016): generalized two-sided renewal and geometric invariant distribution; no identical three-state central passage mechanism. https://doi.org/10.1103/PhysRevE.94.032132
3. D. H. Zanette and S. Manrubia, *Fat tails and black swans: Exact results for multiplicative processes with resets*, *Chaos* **30**, 033104 (2020): the geometric stationary ladder and critical moment growth are generic results and therefore credited. https://arxiv.org/abs/2105.11679

The result is limited to \(\ell=1\) and integer \(r\), and the inferred sharp switch is not a continuous physical phase transition. A more general published renewal-with-core theorem could imply the classification after reduction. No independent audit or experimental validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
