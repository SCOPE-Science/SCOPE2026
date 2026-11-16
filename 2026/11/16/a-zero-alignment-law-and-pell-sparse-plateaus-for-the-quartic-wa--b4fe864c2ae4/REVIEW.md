# Self-review

## Correctness — PASS
The quartic kernel normalization follows from the fourth elementary symmetric function of independent signs, and the endpoint norm is exactly the expectation of its absolute value. The independent-sign recursion and elementary identity for the mean of two absolute values prove the nonnegative increment. The four roots are distinct, inside the sampled interval, and separated by more than a parity-grid spacing for all dimensions covered. This makes the two-binomial sign-change formula and zero-alignment equivalence exact, including root-on-grid cases. A positive Pell descent reduces every possible zero increment to two integer orbits with exponential growth; hence the logarithmic upper bound holds without numerical evidence. Exact calculations confirm the stated plateau at dimension seven. The cutoff to \(10^{100}\) is explicitly a finite exact-integer check, not an unrestricted classification.

## Originality — PASS (provisional priority)
The closest source, Defant et al. (arXiv:2208.06467, Chapter 8; further treatment arXiv:2302.00233, Sections 3–4), proves the kernel expectation representation and fixed-degree Hermite asymptotics, both credited here. Neither inspected presentation supplies the exact successive-dimension quartic increment or its Pell-sparse equality mechanism. Chihara and Stanton's Krawtchouk zero analysis addresses integral roots, interlacing, and coding-theoretic consequences, but not norm plateaus of homogeneous Walsh projections. The accessible cubic projection plateau classification is degree three, and its quadratic families do not imply the quartic two-orbit condition. Specialist-equivalent formulations under coding theory or Krawtchouk quadrature remain possible; this is not an independent or exhaustive historical-priority determination.

## Mathematical value — PASS
The natural question is whether an endpoint projection norm must strictly increase when a Boolean coordinate is added. The answer is governed by an exact boundary sign-change contribution and, in degree four, a rare arithmetic zero-alignment phenomenon. The theorem gives a short exact evaluation rule, a complete per-dimension plateau test, an exponentially sparse list of candidate dimensions, and a fully reproducible exceptionally large finite cutoff. These distinguish the quartic behavior from the square-root-density dimension plateaus known in degree three and supply a usable structural link between projection norms and integral Krawtchouk zeros. The contribution is limited to canonical homogeneous projections and their endpoint norms; it does not settle the existence of further quartic plateaus beyond the certified range.

## Closest literature and risks
- Defant et al., *Projection constants for spaces of multivariate polynomials* (2022), Chapter 8: known norm kernel, no reviewed exact dimension-increment law.
- Defant et al., *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces* (2023), Sections 3–4: asymptotics and degree-four Hermite limit, not the finite-dimensional plateau criterion.
- Chihara–Stanton, *Zeros of generalized Krawtchouk polynomials*, Sections 2–4: known discrete polynomial identities and integral-root context, not endpoint-projection equality.
- Krasikov–Litsyn (1996) is a related integral-zero source. Only bibliographic details and abstract were accessible, so an uninspected equivalent statement remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
