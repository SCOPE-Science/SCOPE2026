# Scientific review: an alternating-edge SIS critical asymptotic

## Correctness: PASS

The claim is restricted to the deterministic nodewise mean-field SIS equation with two prescribed half-period adjacency matrices. The monodromy product is explicitly computed, with one neutral Perron eigenvalue and two strictly stable modes at criticality; \(F'(x)\), strict monotonicity and the critical parameter interval follow algebraically. Order preservation and strict quadratic subhomogeneity establish the global below-/above-threshold dichotomy. The positive periodic adjoint weight is a strict one-period Lyapunov function at neutrality; all nonzero trajectories tend to zero. The Poincaré Taylor expansion, stable-complement reduction, and reciprocal-difference lemma yield \(nr_n\to1/q\) and the phasic law uniformly. The exact reflection symmetry evaluates \(q\) in exponentials, and a standalone code replay independently checks the spectral algebra, eigenvectors, quadrature and numerical asymptotics. Computation is supporting evidence, not the infinite-time proof.

## Originality: PASS on a best-knowledge, non-certifying comparison

The *linear propagator threshold and generic benefit of slower switching are already known principles*, as in Speidel et al. (2016), Valdano et al. (2015, 2017), and earlier related exact mirror-switched epidemic examples. They are **not** the novel claim. The actual claim distinguished here is a universal nonlinear *phase-dependent* critical decay coefficient, evaluated in closed form for the three-site alternating-edge path and valid from every nonzero initial infection vector. Persoons–Sensi–Prasse–Van Mieghem (first public 2023) analyze time-varying NIMFA timescale separation, not this exact phase law. Cai–Nie–Holme (2023) treat activity-driven SIS criticality with a different random-contact model. Ait Rami et al. (2013) establish switched SIS stability and periodic-orbit criteria, and Prasse–Van Mieghem (2020) treat near-threshold trajectories for static NIMFA. These broader results substantially cover the general methods and off-critical ideas, but the inspected claims do not furnish the displayed phase-dependent three-site critical coefficient. Closest known critical inverse-time laws in other epidemic models cannot imply the full periodic vector profile without establishing the specific adjoint neutral mode and quadratic coefficient. Searches and substantial mathematical portions of the accessible primary sources were compared by objects, assumptions and implications rather than by titles alone. Unindexed equivalent critical-reduction literature is a genuine residual priority risk, not a proof of novelty.

## Value: PASS

A temporal-network spectral threshold locates invasion only; it does not quantify nonlinear decay precisely on the knife edge, nor whether the entire population shares a universal periodic critical profile. This theorem resolves those questions completely in the first connected path needing both distinct contacts, providing an interpretable three-site benchmark for critical slowdown and explicit contact-phase dependence. The closed positive coefficient makes the profile quantitatively usable; it is not an arbitrary single-number computation. The model is intentionally deterministic and minimal, so the value is exact mechanism identification, not direct stochastic forecasting.

## Closest sources and scope limits

- Persoons et al., arXiv:2305.12446 (2023-05-21 initial posting): time-varying NIMFA and timescale separation, no exact critical periodic vector law.
- Ait Rami et al., arXiv:1306.0135 (2013): general switched SIS stability and positive periodic orbit existence; does not state the calculated critical amplitude.
- Prasse and Van Mieghem (2020), DOI 10.1007/s00285-020-01542-6: near-threshold analytic NIMFA trajectories for static contact networks; the periodic switching coefficient is not a specialization without additional work.
- Cai, Nie and Holme, arXiv:2311.12175 (2023-11-20 initial posting): temporal criticality on activity-driven contact networks; distinct dynamic correlations and assumptions.
- Speidel et al., arXiv:1602.00859 (2016): general noncommuting propagator and slow-contact effect; covers the linear mechanism, not the displayed nonlinear critical vector coefficient.
- Valdano et al., arXiv:1406.4815 and arXiv:1706.05968: temporal epidemic propagator and continuous-time threshold principles; not the claimed critical nonlinear amplitude.
- Sanatkar et al., arXiv:1501.02472: spectral switching-threshold framework, not the explicit critical decay profile.

The nonlinear theorem is for deterministic NIMFA, not finite stochastic SIS. The precise coefficient at the critical half-period does not assert a stochastic survival probability, global extensions to other temporal paths, or new novelty for the underlying linear Floquet test.

Self-review: passed. Independent audit: not yet performed.
