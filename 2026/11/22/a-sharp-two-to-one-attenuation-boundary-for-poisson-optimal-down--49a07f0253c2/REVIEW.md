# Scientific review: Poisson-optimal downstream DNA sampling

## Correctness — PASS

The claimed domain is \(A>0\), \(0<p<1\), \(0<\lambda<\mu\), \(e_0,e_1>0\), and exactly two independent Poisson counts, one at the origin and one at a chosen downstream location. The Fisher determinant follows from the two score outer products, and is independent of the nuisance amplitude \(A\). Converting distance into \(t=e^{-(\mu-\lambda)x}\) gives a strictly positive objective with zero endpoint limits. Its log derivative has a concave quadratic numerator with opposite endpoint signs and exactly one positive zero, proving uniqueness globally, not just local optimality. Differentiating the log derivative with respect to \(p\) proves monotonicity. Balancing powers of \(p\) in that same exact polynomial gives the three rare-fraction limits. The symbolic checker verifies the critical identities; tests do not substitute for proof.

## Originality — PASS on inspected evidence

The primary 2024 river-DNA transport source develops decay and settling prediction, not a two-class Poisson Fisher-optimal downstream location. A 2025 ecological sampling-design study treats a different network regression and observation-error model. The 2006 classical paper on D-optimal exponential regression fits unknown rates and amplitudes under homoscedastic Gaussian errors, not the exact fixed-two-rate Poisson two-location design or its sharp \(\mu=2\lambda\) rare-fraction transition. Publicly indexed related results on two-exponential observation scheduling and Poisson-sensor design concern different underlying design problems. The new result does not claim that Fisher information, exponential mixtures, or D-optimality themselves are novel. Complete historical priority is unproved; an older specialized optimal-design corollary could still exist.

## Mathematical value — PASS

The concrete applied design asks how far downstream a second copy-count sample should be placed to distinguish two DNA particle classes while also estimating unknown source intensity. Under the fixed two-site, fixed-effort experiment the answer is unique for every physically interior mixture. The exact two-to-one attenuation boundary exposes a singular design limit: as slow-particle abundance vanishes, the preferred downstream location either remains finite or retreats logarithmically, with a distinct critical scaling at equality. This is a motivated structural quantitative boundary rather than a small numerical optimization gain. Practical use requires nominal rates and mixture fraction and is not asserted for finite-sample risk, assay noise, or an uncontrolled river.

## Closest literature and limitations

- Didier Pont (2024), *Predicting downstream transport distance of fish eDNA in lotic environments*, https://doi.org/10.1111/1755-0998.13934; physical source model and sampling motivation.
- Timothy D. Lambert and Stephen P. Ellner (2025), *SDM meets eDNA: optimal sampling of environmental DNA to estimate species–environment relationships in stream networks*, https://doi.org/10.1111/ecog.07644; broader spatial design, different observations and targets.
- Holger Dette, Viatcheslav B. Melas and Weng Kee Wong (2006), *Locally D-optimal designs for exponential regression models*, https://doi.org/10.17877/DE290R-15075; established Gaussian nonlinear-design theory.
- Pedro F. P. Brandão-Dias and colleagues (2023), *Suspended Materials Affect Particle Size Distribution and Removal of Environmental DNA in Flowing Waters*, https://doi.org/10.1021/acs.est.3c02638; relevant particle-size effects, abstract inspected only.

The source rates are assumed known and constant, and the independent Poisson-count approximation excludes overdispersion, background, exchange and site-dependent expense. An inaccessible specialized prior result remains possible. No empirical calibration or independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
