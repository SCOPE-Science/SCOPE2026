# Scientific review

## Correctness — PASS

The exact domain is \(N,\beta,\gamma,\phi>0\) and every nonnegative SIR triple with fixed total \(N\). The two directly modeled coordinates are rational and nonnegative. For each infected fraction, the recovered output decreases strictly with the susceptible fraction; consequently the boundary \(r=0\) is extremal. There the recovered output factors into a positive denominator, \(\tau i\), and \(1+\tau\rho-\tau\rho^2 i(1-i)\). The sharp elementary maximum \(i(1-i)=1/4\) proves both implications, including the equality boundary, while the discriminant gives the full unsafe interval. Exact-rational checks reproduce the formula and the negative witness. The proof does not rely on a sampled grid.

## Originality — PASS, with historical-priority qualifications

The primary 2026 source establishes positivity of the **modeled** components and expressly notes that algebraically recovered population can be negative. It does not classify the parameter and timestep region for exact physical rates. Earlier 2014 and 2021–2022 SIR discretizations preserve transfer fluxes using updated susceptible states or different denominators; they do not state the sharp criterion for the specific old-state infection gain and diagonal loss update. Searches of mathematical research records, published SIR NSFD schemes and terminology variants found no theorem that subsumes the sharp physical-simplex criterion or its unsafe-state region. The mathematical method is elementary and related to known discrete invariant-set tests; unindexed equivalent derivations remain possible.

## Value — PASS

The result quantitatively closes a warning left open by the motivating numerical method: a nonnegative two-coordinate gain–loss layer plus algebraic recovery does not always define a nonnegative physical SIR state. It gives a **necessary-and-sufficient whole-simplex safety test** rather than only one counterexample, with an attainable threshold, explicit unsafe initial conditions, and a clear distinction between exact physical rates and independently learned rates. Its threshold \(\rho=4\) is not the epidemic invasion threshold \(\rho=1\). These precise distinctions matter when setting timestep and denominator ranges for physically interpretable simulation layers; no neural-training performance claim is made.

## Closest literature and limits

- Zinihi, Ehrhardt and Sidi Ammi, arXiv:2607.10858v1 (2026), Section 3, Section 5, Remark 2: closest numerical update and explicit warning; the new full-simplex classification is absent.
- *An NSFD scheme for SIR epidemic models of childhood diseases with constant vaccination strategy* (2014), Section 3: infection gain uses updated susceptible variable and recovered state is updated directly; hence its unconditional positivity does not imply the claim for the old-state infection gain.
- *Nonstandard Finite Difference Schemes for an SIR Epidemic Model* (2021), Section 3, and *Efficient Numerical Solutions to a SIR Epidemic Model* (2022), Sections 3 and 6: related but distinct conservative schemes and predictor–corrector steps.

This is a deterministic theorem for exact rates on one closed SIR model. It does not cover fitted networks, time-varying parameters, other models, finite-precision boundary rounding or global convergence rates.

Self-review: passed. Independent audit: not yet performed.
