# Scientific review

## Correctness — PASS

The stationary renewal mixture is exact for Poisson complete resets. Conditional on the bounded orientation history, the position is Gaussian with explicitly integrated variance \(2D\tau F(u)\). The uniform \(O(\sqrt R)\) bound on the activity correction on compact ages, combined with the controlled small- and large-age tails, proves the leading logarithmic limit without assuming the orientational displacement is Gaussian. For the next \(\sqrt R\) term, the deterministic heading case follows from Laplace expansion, while Brownian angular full support gives matching upper and lower bounds at each fixed positive rotational diffusivity. The monotone saddle parameterization proves unique age selection. Differentiation and endpoint analysis prove strict concavity and the sharp \(3/2\) additive-gap ceiling and the singular distinction between rotating and frozen headings. The standalone numerical checker evaluates the mixture directly and verifies several independent identities; numerical data are not used as proof of asymptotics.

## Originality — PASS, qualified

The parent active-particle work provides the model and stationary second/fourth moments, but not the joint large-reset rare-displacement rate or its conditional age law. The passive paper by Franke and Sokolov gives an exact Gaussian stationary mixture and *the same implicit saddle equation* after changing variables; that equation and the fixed-reset far-tail exponential are **prior work**. The novel assertion is restricted to the singular joint limit, sharp global rate geometry, **the first active logarithmic correction and its positive-versus-zero rotational diffusivity threshold**, and the conditional-age concentration statement. Related random-acceleration resetting work has stretched-exponential asymptotics but not this damped active-crossover theorem. The fixed-rate passive tail results do not cover the simultaneous high-rate regime.

Residual priority risk: an unindexed analysis of the pre-existing passive saddle could contain the joint high-rate limit or equivalent consequences. Such a source would narrow or defeat originality; a search without an exact match is not a proof of priority. The existing saddle equation substantially limits the claim's scope.

## Value — PASS

At high reset rates the typical stationary mean-square displacement collapses, while observing a displacement of order \(\sqrt{r\tau}\) probes exceptionally old excursions. The theorem converts this physically motivated large deviation into a universal continuum profile, identifies the specific age of the responsible excursions, and quantifies the crossover between acceleration-controlled square-root action and friction-controlled linear action with a sharp additive gap. It supplies tail information unavailable from a finite set of moments and a subleading anisotropy transition: rare orientation histories erase the initial heading at every fixed positive angular diffusion, but a perfectly frozen heading retains anisotropy.

## Limits and risk

The theorem does not provide finite-rate tail prefactors, a uniform rate law near \(z=0\), a full process-level large-deviation principle, or results for partial resetting and changing propulsion speed. The first subleading asymptotic is not uniform in the angular diffusion coefficient near zero. The proof and verifier cover the exact assumptions in RESULT.md. An independent scientific priority and correctness audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
