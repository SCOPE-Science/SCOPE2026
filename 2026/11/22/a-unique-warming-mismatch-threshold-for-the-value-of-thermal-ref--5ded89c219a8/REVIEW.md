# Scientific review: unique warming-mismatch threshold under dispersal

## Correctness — PASS

The claim is entirely about the dominant eigenvalue of a specified irreducible two-by-two Metzler matrix compared with a homogeneous version. The displayed eigenvalue in RESULT.md follows by exact characteristic-polynomial solution. The small-mismatch case uses entrywise Perron comparison; the large-mismatch case uses the strictly positive spectral contrast above the arithmetic mean. Only the intermediate regime needs a nontrivial argument: its eigenvalue decreases strictly in movement, and its critical movement curve is strictly increasing in climatic mismatch, as established by the explicit derivative identity and the monotonicity of \(\sinh(ax)/x\). The two endpoint limits and both first-order coefficients were derived from the exact formula. Independent numerical tests in `checker.py` are supplementary, not a substitute for these universal arguments.

## Originality — PASS on inspected evidence

The relevant published records and actual primary text do not state this combined Gaussian two-patch heterogeneity-versus-homogeneity classification, unique finite-migration warming threshold, or its sharp migration asymptotics. Backus, Clements and Baskett (2024, DOI 10.1002/ecy.4257) use stochastic density-dependent metapopulation simulations with a skew-normal response, rather than a closed-form spectral phase boundary. Amarasekare (2024, DOI 10.1111/1365-2656.14054) uses mechanistically temperature-dependent dispersal in an array of habitats, not this symmetric migration comparison. Grumbach et al. (2023, DOI 10.1007/s00285-023-01984-8) classify nonlinear equilibrium population-size responses to dispersal. Related published mathematical findings concerning patch variance, season ordering and dispersal-sensitive growth use other objects or objectives. Classical eigenvalue formulas and movement reduction are prior background, not asserted innovations. The exact new claim is the global warming-dependent classification and its proof.

Historical priority is provisional because semantic search is incomplete and one potentially relevant continuous-space paper (Terry, O'Sullivan and Rossberg 2023, DOI 10.1086/728002) could not be inspected in full at the accessible publisher/archive endpoints; its abstract and stated equations concern range shifts in a reaction-diffusion model, not the paired fixed thermal patches.

## Value — PASS

The question is motivated by whether restoring fine-scale spatial thermal heterogeneity aids climate-stressed populations and how movement might change its effectiveness. This result isolates a rigorous, ecologically interpretable three-region mechanism: too small a mean-temperature mismatch makes heterogeneity harmful at every migration rate; an intermediate mismatch allows heterogeneity to help only below a sharply determined migration rate; sufficiently large mismatch makes it beneficial at every finite rate. Its equivalent unique crossing in warming mismatch, migration monotonicity, and asymptotic limits go beyond reporting a single parameter example. The calculation can serve as a transparent comparison benchmark for complex spatial restoration simulations, without claiming direct field applicability.

## Closest literature and limits

The referenced ecological studies analyze different movement rules or population outcomes. This theorem assumes a symmetric Gaussian thermal niche, two equal patches, constant exchange and low-density linearization. It does not establish persistence, long-run stochastic growth, nonlinear equilibrium abundance, skewed thermal performance, or field-level benefit. The positive advantage becomes small far beyond the thermal niche. Same-paper and broader synonym coverage remain imperfect.

Self-review: passed. Independent audit: not yet performed.
